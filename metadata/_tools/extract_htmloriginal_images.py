from __future__ import annotations

import base64
import csv
import hashlib
import io
import shutil
import urllib.parse
import urllib.request
from pathlib import Path

from lxml import html
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
HTML_ORIGINAL_DIR = ROOT / "htmloriginal"
OUTPUT_ROOT = ROOT / "images" / "htmloriginal_extracted"
MANIFEST_CSV = ROOT / "images" / "htmloriginal_extracted_manifest.csv"
REPORT_MD = ROOT / "images" / "htmloriginal_extraction_report.md"

WILEY_IMAGE_DIRS = [
    ROOT / "images",
    ROOT / "overleaf_bundle" / "images",
    ROOT / "drafts" / "images",
    ROOT / "drafts" / "overleaf_bundle" / "images",
]

MIN_WIDTH = 200
MIN_HEIGHT = 200
HTTP_TIMEOUT = 20


def remove_old_wiley_assets() -> list[Path]:
    removed: list[Path] = []
    for directory in WILEY_IMAGE_DIRS:
        if not directory.exists():
            continue
        for path in directory.glob("wiley_fig*.*"):
            path.unlink()
            removed.append(path)
    return removed


def reset_output_root() -> None:
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)


def load_html_document(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    return html.fromstring(text)


def load_image_bytes(src: str, base_dir: Path) -> tuple[bytes, str] | None:
    src = (src or "").strip()
    if not src:
        return None

    if src.startswith("data:image/"):
        header, payload = src.split(",", 1)
        mime = header.split(";", 1)[0].split(":", 1)[1].strip()
        return base64.b64decode(payload), mime

    if src.startswith("http://") or src.startswith("https://"):
        with urllib.request.urlopen(src, timeout=HTTP_TIMEOUT) as resp:
            data = resp.read()
            mime = resp.headers.get_content_type() or "application/octet-stream"
        return data, mime

    decoded = urllib.parse.unquote(src)
    candidate = (base_dir / decoded).resolve()
    if candidate.exists() and candidate.is_file():
        return candidate.read_bytes(), ""
    return None


def image_info(blob: bytes) -> tuple[str, int, int] | None:
    try:
        with Image.open(io.BytesIO(blob)) as img:
            fmt = (img.format or "PNG").lower()
            width, height = img.size
        return fmt, width, height
    except Exception:
        return None


def extract_from_html(path: Path) -> tuple[int, list[dict[str, str | int]]]:
    doc = load_html_document(path)
    out_dir = OUTPUT_ROOT / path.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    saved = 0
    seen_hashes: set[str] = set()
    rows: list[dict[str, str | int]] = []

    for index, node in enumerate(doc.xpath("//img"), start=1):
        loaded = load_image_bytes(node.get("src") or "", path.parent)
        if loaded is None:
            continue

        blob, mime = loaded
        info = image_info(blob)
        if info is None:
            continue

        fmt, width, height = info
        if width < MIN_WIDTH or height < MIN_HEIGHT:
            continue

        digest = hashlib.sha256(blob).hexdigest()
        if digest in seen_hashes:
            continue
        seen_hashes.add(digest)

        saved += 1
        filename = f"image_{saved:03d}.{fmt}"
        out_path = out_dir / filename
        out_path.write_bytes(blob)

        rows.append(
            {
                "source_html": path.name,
                "source_stem": path.stem,
                "image_index": saved,
                "saved_path": str(out_path.relative_to(ROOT)).replace("\\", "/"),
                "width": width,
                "height": height,
                "mime_hint": mime,
                "img_class": node.get("class") or "",
                "sha256": digest,
            }
        )

    return saved, rows


def write_manifest(rows: list[dict[str, str | int]]) -> None:
    fieldnames = [
        "source_html",
        "source_stem",
        "image_index",
        "saved_path",
        "width",
        "height",
        "mime_hint",
        "img_class",
        "sha256",
    ]
    with MANIFEST_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(
    scanned_files: int,
    extracted_total: int,
    removed_assets: list[Path],
    per_file_counts: list[tuple[str, int]],
) -> None:
    lines = [
        "# htmloriginal Image Extraction Report",
        "",
        f"- Scanned HTML files: `{scanned_files}`",
        f"- Extracted non-trivial images: `{extracted_total}`",
        f"- Removed old generated `wiley_fig*` assets: `{len(removed_assets)}`",
        "",
        "## What Was Extracted",
        "",
        "- The new `htmloriginal` files contain embedded image payloads.",
        "- In the sampled files, these are mixed embedded images from the HTML export, including figure-level snippets and larger page-derived assets.",
        f"- Extracted images are stored under `{OUTPUT_ROOT.relative_to(ROOT).as_posix()}`.",
        "- Tiny 1x1 helper images were ignored.",
        "- Duplicate images inside the same HTML file were deduplicated by SHA-256.",
        "",
        "## Per-File Counts",
        "",
    ]

    for name, count in per_file_counts:
        lines.append(f"- `{name}`: `{count}` images")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- The old synthetic `wiley_fig*` images were removed from the image folders to avoid mixing generated assets with extracted assets.",
            "- The current Wiley `.tex` file is not automatically remapped to these extracted images.",
            "- Use `htmloriginal_extracted_manifest.csv` to locate each saved image.",
            "",
        ]
    )

    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def refresh_overleaf_zip() -> None:
    bundle_dir = ROOT / "overleaf_bundle"
    zip_path = ROOT / "overleaf_bundle.zip"
    if not bundle_dir.exists():
        return

    import zipfile

    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in bundle_dir.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(bundle_dir))


def main() -> None:
    if not HTML_ORIGINAL_DIR.exists():
        raise FileNotFoundError(f"Missing directory: {HTML_ORIGINAL_DIR}")

    removed_assets = remove_old_wiley_assets()
    reset_output_root()

    all_rows: list[dict[str, str | int]] = []
    per_file_counts: list[tuple[str, int]] = []

    html_files = sorted(HTML_ORIGINAL_DIR.glob("*.html"), key=lambda p: p.name.lower())
    for path in html_files:
        count, rows = extract_from_html(path)
        all_rows.extend(rows)
        per_file_counts.append((path.name, count))

    write_manifest(all_rows)
    write_report(len(html_files), len(all_rows), removed_assets, per_file_counts)
    refresh_overleaf_zip()

    print(f"Scanned {len(html_files)} HTML files.")
    print(f"Extracted {len(all_rows)} images to {OUTPUT_ROOT}.")
    print(f"Removed {len(removed_assets)} old generated wiley_fig assets.")


if __name__ == "__main__":
    main()
