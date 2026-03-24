from __future__ import annotations

import csv
import html
import json
import re
import unicodedata
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / "papers50"
METADATA_DIR = ROOT / "metadata"
GENERATED_DIR = METADATA_DIR / "meatdatagenerated"
TEXT_DIR = GENERATED_DIR / "text"
JSON_DIR = GENERATED_DIR / "json"
HTML_DIR = ROOT / "html"
IMAGES_DIR = ROOT / "images"


def natural_sort_key(path: Path) -> list[object]:
    parts = re.split(r"(\d+)", path.name.lower())
    key: list[object] = []
    for part in parts:
        key.append(int(part) if part.isdigit() else part)
    return key


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.replace("\u00ad", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def collapse_inline_breaks(text: str) -> str:
    text = re.sub(r"-\n(?=[a-z])", "", text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def parse_pdf_date(value: str) -> str | None:
    if not value:
        return None
    match = re.search(r"(\d{4})(\d{2})(\d{2})", value)
    if not match:
        return None
    return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"


def extract_year(*sources: str | None) -> str | None:
    for source in sources:
        if not source:
            continue
        match = re.search(r"\b(19|20)\d{2}\b", source)
        if match:
            return match.group(0)
    return None


def extract_doi(*sources: str | None) -> str | None:
    pattern = re.compile(r"\b(10\.\d{4,9}/[-._;()/:A-Z0-9]+)\b", re.IGNORECASE)
    for source in sources:
        if not source:
            continue
        match = pattern.search(source)
        if match:
            return match.group(1).rstrip(").,;")
    return None


def extract_journal(subject: str | None, first_page_text: str) -> str | None:
    if subject:
        if ";" in subject:
            parts = [part.strip() for part in subject.split(";") if part.strip()]
            if parts:
                return parts[0]
        if "," in subject:
            return subject.split(",", 1)[0].strip()
        return subject.strip()

    for line in first_page_text.splitlines()[:10]:
        line = line.strip()
        if not line:
            continue
        if re.search(r"journal|transactions|conference|proceedings", line, re.IGNORECASE):
            return collapse_inline_breaks(line)
    return None


def title_is_usable(title: str | None) -> bool:
    if not title:
        return False
    stripped = title.strip()
    if len(stripped) < 8:
        return False
    if stripped.lower().endswith(".pdf"):
        return False
    return True


def looks_like_author_line(line: str) -> bool:
    line = line.strip()
    if not line:
        return False
    if re.search(r"\b(member|fellow|student|department|school|university|institute|laboratory|lab|college|received|accepted)\b", line, re.IGNORECASE):
        return True
    name_pattern = re.compile(
        r"^[A-Z][A-Za-z'`.-]+(?:\s+[A-Z][A-Za-z'`.-]+){0,4}"
        r"(?:\s*,\s*[A-Z][A-Za-z'`.-]+(?:\s+[A-Z][A-Za-z'`.-]+){0,4})*"
        r"(?:\s+and\s+[A-Z][A-Za-z'`.-]+(?:\s+[A-Z][A-Za-z'`.-]+){0,4})?$"
    )
    return bool(name_pattern.match(line))


def guess_title(meta_title: str | None, first_page_text: str, fallback: str) -> str:
    if title_is_usable(meta_title):
        return collapse_inline_breaks(meta_title)

    lines = [line.strip() for line in first_page_text.splitlines() if line.strip()]
    title_lines: list[str] = []
    for line in lines[:30]:
        if re.match(r"^\d+$", line):
            continue
        if re.search(r"journal homepage|contents lists available|vol\.|doi:|received ", line, re.IGNORECASE):
            continue
        if re.match(r"^(abstract|a\s*b\s*s\s*t\s*r\s*a\s*c\s*t|keywords?|index terms)\b", line, re.IGNORECASE):
            break
        if title_lines and looks_like_author_line(line):
            break
        if re.search(r"\bdepartment\b|\buniversity\b|\bschool\b|\binstitute\b", line, re.IGNORECASE):
            break
        title_lines.append(line)
        if len(" ".join(title_lines)) > 220:
            break

    guessed = collapse_inline_breaks("\n".join(title_lines))
    return guessed or fallback


def guess_authors(meta_author: str | None, first_page_text: str, title: str) -> str | None:
    if meta_author and meta_author.strip():
        return collapse_inline_breaks(meta_author)

    lines = [line.strip() for line in first_page_text.splitlines() if line.strip()]
    title_words = set(re.findall(r"\w+", title.lower()))
    title_index = 0
    for index, line in enumerate(lines[:30]):
        line_words = set(re.findall(r"\w+", line.lower()))
        if title_words and len(title_words & line_words) >= max(2, min(4, len(title_words))):
            title_index = index
            break

    author_lines: list[str] = []
    for line in lines[title_index + 1 : title_index + 8]:
        if re.match(r"^(abstract|a\s*b\s*s\s*t\s*r\s*a\s*c\s*t|keywords?|index terms|received|1\.|i\.)\b", line, re.IGNORECASE):
            break
        if re.search(r"\bdepartment\b|\buniversity\b|\bschool\b|\binstitute\b|\bemail\b|@", line, re.IGNORECASE):
            if author_lines:
                break
            continue
        if looks_like_author_line(line):
            author_lines.append(line)
        elif author_lines:
            break

    authors = collapse_inline_breaks("\n".join(author_lines))
    return authors or None


def extract_abstract(text: str) -> str | None:
    inline_patterns = [
        r"Abstract\s*[—:-]\s*(.+?)(?=\n(?:Index Terms|Keywords?|I\.\s+INTRODUCTION|1\.\s+Introduction|Introduction)\b)",
        r"\bABSTRACT\s*[:—-]\s*(.+?)(?=\n(?:Keywords?|Index Terms|1\.\s+Introduction|Introduction)\b)",
    ]
    for pattern in inline_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            abstract = collapse_inline_breaks(match.group(1))
            if abstract:
                return abstract

    paragraphs = [collapse_inline_breaks(block) for block in re.split(r"\n\s*\n", text)]
    paragraphs = [paragraph for paragraph in paragraphs if paragraph]

    def is_boundary(paragraph: str) -> bool:
        return bool(
            re.match(
                r"^(?:[IVXLC]+\.\s+[A-Z]|(?:\d+(?:\.\d+)*\.?)\s+[A-Z]|Introduction|References|Acknowledg)",
                paragraph,
            )
        )

    def is_metadata_paragraph(paragraph: str) -> bool:
        return bool(
            re.match(
                r"^(?:A\s*R\s*T\s*I\s*C\s*L\s*E\s*I\s*N\s*F\s*O|Keywords?:|Index Terms|Received |Available online|Contents lists available)",
                paragraph,
                re.IGNORECASE,
            )
        )

    def looks_like_keyword_list(paragraph: str) -> bool:
        words = re.findall(r"\w+", paragraph)
        return len(words) <= 20 and "." not in paragraph and not paragraph.lower().startswith(("this ", "we ", "to "))

    for index, paragraph in enumerate(paragraphs):
        inline_match = re.match(r"^(?:A\s*B\s*S\s*T\s*R\s*A\s*C\s*T|ABSTRACT)\s*[:—-]\s*(.+)$", paragraph, re.IGNORECASE)
        if inline_match:
            abstract = inline_match.group(1).strip()
            if len(re.findall(r"\w+", abstract)) >= 20:
                return abstract

        if re.fullmatch(r"A\s*B\s*S\s*T\s*R\s*A\s*C\s*T", paragraph, re.IGNORECASE) or paragraph.upper() == "ABSTRACT":
            collected: list[str] = []
            for candidate in paragraphs[index + 1 : index + 8]:
                if is_boundary(candidate):
                    break
                if is_metadata_paragraph(candidate) or looks_like_keyword_list(candidate):
                    continue
                collected.append(candidate)
                if len(collected) >= 2:
                    break
            abstract = " ".join(collected).strip()
            if len(re.findall(r"\w+", abstract)) >= 20:
                return abstract
    return None


def extract_keywords(text: str, pdf_keywords: str | None) -> list[str]:
    if pdf_keywords and pdf_keywords.strip():
        return [item.strip() for item in re.split(r"[;,]", pdf_keywords) if item.strip()]

    patterns = [
        r"Index Terms\s*[—:-]\s*(.+?)(?=\n(?:I\.\s+INTRODUCTION|1\.\s+Introduction|Introduction)\b)",
        r"Keywords?\s*[:—-]\s*(.+?)(?=\n(?:1\.\s+Introduction|Introduction)\b)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            raw = collapse_inline_breaks(match.group(1))
            return [item.strip(" .") for item in re.split(r"[;,]", raw) if item.strip()]
    return []


def extract_sections(text: str) -> list[str]:
    sections: list[str] = []
    seen: set[str] = set()
    pattern = re.compile(
        r"^(?:[IVXLC]+\.\s+[A-Z][A-Z0-9 ,:&()/+-]+|(?:\d+(?:\.\d+)*\.?)\s+[A-Z][A-Za-z0-9 ,:&()/+-]+)$"
    )
    for line in text.splitlines():
        candidate = collapse_inline_breaks(line)
        if not candidate or len(candidate) > 120:
            continue
        if candidate.lower().startswith(("fig.", "figure ", "table ")):
            continue
        if pattern.match(candidate):
            normalized = candidate.strip()
            if normalized not in seen:
                seen.add(normalized)
                sections.append(normalized)
    return sections[:50]


def extract_caption_paragraphs(text: str, kind: str) -> list[str]:
    prefix = "fig(?:ure)?\\.?" if kind == "figure" else "table"
    pattern = re.compile(rf"^(?:{prefix})\s*\d+[A-Za-z]?\b", re.IGNORECASE)
    captions: list[str] = []
    seen: set[str] = set()
    for paragraph in re.split(r"\n\s*\n", text):
        normalized = collapse_inline_breaks(paragraph)
        if not normalized:
            continue
        if pattern.match(normalized):
            if normalized not in seen:
                seen.add(normalized)
                captions.append(normalized)
    return captions


def block_to_paragraph(text: str) -> str:
    text = re.sub(r"-\n(?=[a-z])", "", text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def is_heading(text: str) -> bool:
    if len(text) > 110:
        return False
    if re.match(r"^(?:[IVXLC]+\.\s+|(?:\d+(?:\.\d+)*)\s+)", text):
        return True
    alpha_count = sum(char.isalpha() for char in text)
    upper_count = sum(char.isupper() for char in text)
    return alpha_count > 0 and upper_count >= alpha_count * 0.75


def build_citation(record: dict[str, object]) -> str:
    parts: list[str] = []
    authors = record.get("authors") or record.get("authors_guess")
    year = record.get("year")
    title = record.get("title")
    journal = record.get("journal")
    doi = record.get("doi")

    if authors:
        parts.append(str(authors))
    if year:
        parts.append(f"({year}).")
    if title:
        parts.append(f"{title}.")
    if journal:
        parts.append(f"{journal}.")
    if doi:
        parts.append(f"https://doi.org/{doi}")

    citation = " ".join(parts).strip()
    return citation or str(title or record["source_filename"])


def build_html(record: dict[str, object], page_blocks: list[list[str]]) -> str:
    def esc(value: object) -> str:
        return html.escape("" if value is None else str(value))

    metadata_rows = [
        ("Source PDF", f'<a href="../papers50/{esc(record["source_filename"])}">{esc(record["source_filename"])}</a>'),
        ("Pages", esc(record["page_count"])),
        ("Year", esc(record.get("year") or "")),
        ("Journal", esc(record.get("journal") or "")),
        ("DOI", esc(record.get("doi") or "")),
        ("Citation", esc(record.get("citation") or "")),
    ]

    lines = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="utf-8">',
        f"  <title>{esc(record['title'])}</title>",
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        "  <style>",
        "    :root { color-scheme: light; --ink: #1b1c1d; --muted: #5a6470; --paper: #ffffff; --edge: #dfe4ea; --accent: #194a8d; --wash: #f5f8fc; }",
        "    body { margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: linear-gradient(180deg, #eef3f9 0%, #f8fafc 100%); }",
        "    main { max-width: 980px; margin: 0 auto; padding: 32px 20px 64px; }",
        "    article { background: var(--paper); border: 1px solid var(--edge); border-radius: 18px; box-shadow: 0 10px 30px rgba(17, 24, 39, 0.08); overflow: hidden; }",
        "    header { padding: 32px; background: linear-gradient(135deg, #f7fbff 0%, #eef4fb 100%); border-bottom: 1px solid var(--edge); }",
        "    h1 { margin: 0 0 12px; font-size: 2rem; line-height: 1.15; }",
        "    h2 { margin: 0 0 12px; font-size: 1.2rem; }",
        "    h3 { margin: 24px 0 10px; font-size: 1rem; letter-spacing: 0.02em; text-transform: uppercase; color: var(--accent); }",
        "    p, li, dd { line-height: 1.65; font-size: 1rem; }",
        "    section { padding: 28px 32px; border-top: 1px solid var(--edge); }",
        "    .meta { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px 20px; }",
        "    .meta dt { font-size: 0.82rem; font-weight: 700; text-transform: uppercase; color: var(--muted); margin-bottom: 4px; }",
        "    .meta dd { margin: 0; }",
        "    .note { margin-top: 16px; padding: 14px 16px; border-left: 4px solid var(--accent); background: var(--wash); }",
        "    .page { background: #fff; }",
        "    .page-label { font-size: 0.8rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-bottom: 18px; }",
        "    ul { margin: 0; padding-left: 20px; }",
        "    a { color: var(--accent); }",
        "  </style>",
        "</head>",
        "<body>",
        "<main>",
        "<article>",
        "<header>",
        f"  <h1>{esc(record['title'])}</h1>",
    ]

    if record.get("authors") or record.get("authors_guess"):
        lines.append(f"  <p>{esc(record.get('authors') or record.get('authors_guess'))}</p>")
    if record.get("abstract"):
        lines.append('  <div class="note"><strong>Abstract.</strong> ' + esc(record["abstract"]) + "</div>")
    lines.extend(["</header>", '<section><h2>Paper Metadata</h2>', '<dl class="meta">'])
    for label, value in metadata_rows:
        lines.append(f"  <div><dt>{html.escape(label)}</dt><dd>{value}</dd></div>")
    lines.extend(["</dl>", "</section>"])

    if record.get("section_headings"):
        lines.extend(["<section>", "<h2>Detected Section Headings</h2>", "<ul>"])
        for heading in record["section_headings"]:
            lines.append(f"  <li>{esc(heading)}</li>")
        lines.extend(["</ul>", "</section>"])

    if record.get("figure_captions"):
        lines.extend(["<section>", "<h2>Detected Figure Captions</h2>", "<ul>"])
        for caption in record["figure_captions"]:
            lines.append(f"  <li>{esc(caption)}</li>")
        lines.extend(["</ul>", "</section>"])

    if record.get("table_captions"):
        lines.extend(["<section>", "<h2>Detected Table Captions</h2>", "<ul>"])
        for caption in record["table_captions"]:
            lines.append(f"  <li>{esc(caption)}</li>")
        lines.extend(["</ul>", "</section>"])

    lines.extend(
        [
            "<section>",
            "<h2>Image Insertion Note</h2>",
            "<p>This HTML is prepared for later figure insertion. Citation data for Wiley-style image credits is stored in the <code>images</code> folder.</p>",
            "</section>",
        ]
    )

    for page_number, blocks in enumerate(page_blocks, start=1):
        lines.extend(
            [
                '<section class="page">',
                f'  <div class="page-label">Page {page_number}</div>',
            ]
        )
        for block in blocks:
            tag = "h3" if is_heading(block) else "p"
            lines.append(f"  <{tag}>{esc(block)}</{tag}>")
        lines.append("</section>")

    lines.extend(["</article>", "</main>", "</body>", "</html>"])
    return "\n".join(lines) + "\n"


def main() -> None:
    for directory in [TEXT_DIR, JSON_DIR, HTML_DIR, IMAGES_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

    pdf_paths = sorted(PDF_DIR.glob("*.pdf"), key=natural_sort_key)
    catalog: list[dict[str, object]] = []
    figure_rows: list[dict[str, object]] = []
    errors: list[dict[str, str]] = []

    for pdf_path in pdf_paths:
        try:
            doc = fitz.open(pdf_path)
            pdf_meta = doc.metadata or {}
            page_blocks: list[list[str]] = []
            page_texts: list[str] = []

            for page in doc:
                blocks: list[str] = []
                for block in page.get_text("blocks", sort=True):
                    if len(block) < 7:
                        continue
                    if block[6] != 0:
                        continue
                    paragraph = block_to_paragraph(normalize_text(block[4]))
                    if paragraph:
                        blocks.append(paragraph)
                page_blocks.append(blocks)
                page_texts.append("\n\n".join(blocks))

            first_page_text = page_texts[0] if page_texts else ""
            full_text = normalize_text("\n\n".join(page_texts))
            title = guess_title(pdf_meta.get("title"), first_page_text, pdf_path.stem)
            authors = guess_authors(pdf_meta.get("author"), first_page_text, title)
            year = extract_year(
                pdf_meta.get("subject"),
                pdf_meta.get("creationDate"),
                pdf_meta.get("modDate"),
                first_page_text,
            )
            doi = extract_doi(pdf_meta.get("subject"), full_text[:5000], pdf_meta.get("keywords"))
            journal = extract_journal(pdf_meta.get("subject"), first_page_text)
            abstract = extract_abstract(full_text[:20000] if len(full_text) > 20000 else full_text)
            keywords = extract_keywords(full_text[:12000], pdf_meta.get("keywords"))
            section_headings = extract_sections(full_text)
            figure_captions = extract_caption_paragraphs(full_text, "figure")
            table_captions = extract_caption_paragraphs(full_text, "table")

            record: dict[str, object] = {
                "source_filename": pdf_path.name,
                "source_path": str(pdf_path.relative_to(ROOT)).replace("\\", "/"),
                "title": title,
                "authors": authors,
                "authors_guess": authors,
                "journal": journal,
                "year": year,
                "doi": doi,
                "page_count": doc.page_count,
                "word_count": len(re.findall(r"\b\w+\b", full_text)),
                "abstract": abstract,
                "keywords": keywords,
                "section_headings": section_headings,
                "figure_captions": figure_captions,
                "table_captions": table_captions,
                "pdf_metadata": pdf_meta,
                "pdf_dates": {
                    "creation_date": parse_pdf_date(pdf_meta.get("creationDate", "")),
                    "modified_date": parse_pdf_date(pdf_meta.get("modDate", "")),
                },
                "text_path": str((TEXT_DIR / f"{pdf_path.stem}.txt").relative_to(ROOT)).replace("\\", "/"),
                "json_path": str((JSON_DIR / f"{pdf_path.stem}.json").relative_to(ROOT)).replace("\\", "/"),
                "html_path": str((HTML_DIR / f"{pdf_path.stem}.html").relative_to(ROOT)).replace("\\", "/"),
            }
            record["citation"] = build_citation(record)

            (TEXT_DIR / f"{pdf_path.stem}.txt").write_text(full_text + "\n", encoding="utf-8")
            (JSON_DIR / f"{pdf_path.stem}.json").write_text(
                json.dumps(record, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            (HTML_DIR / f"{pdf_path.stem}.html").write_text(
                build_html(record, page_blocks),
                encoding="utf-8",
            )

            catalog.append(record)
            for index, caption in enumerate(figure_captions, start=1):
                figure_rows.append(
                    {
                        "source_filename": pdf_path.name,
                        "title": title,
                        "figure_id": f"Figure {index}",
                        "figure_caption": caption,
                        "citation": record["citation"],
                        "doi": doi or "",
                        "html_path": record["html_path"],
                        "json_path": record["json_path"],
                    }
                )
        except Exception as exc:
            errors.append({"source_filename": pdf_path.name, "error": str(exc)})

    catalog_path = METADATA_DIR / "catalog.json"
    catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    with (METADATA_DIR / "catalog.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "source_filename",
                "title",
                "authors",
                "journal",
                "year",
                "doi",
                "page_count",
                "word_count",
                "abstract",
                "html_path",
                "json_path",
            ],
        )
        writer.writeheader()
        for record in catalog:
            writer.writerow({key: record.get(key, "") for key in writer.fieldnames})

    with (IMAGES_DIR / "figure_reference_index.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "source_filename",
                "title",
                "figure_id",
                "figure_caption",
                "citation",
                "doi",
                "html_path",
                "json_path",
            ],
        )
        writer.writeheader()
        writer.writerows(figure_rows)

    image_manifest = [
        {
            "source_filename": record["source_filename"],
            "title": record["title"],
            "citation": record["citation"],
            "doi": record["doi"],
            "wiley_credit_template": f"Adapted from {record['citation']}" if record.get("citation") else "",
            "html_path": record["html_path"],
            "json_path": record["json_path"],
        }
        for record in catalog
    ]
    (IMAGES_DIR / "wiley_source_manifest.json").write_text(
        json.dumps(image_manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    summary_lines = [
        "# Paper Reading Index",
        "",
        f"Processed papers: {len(catalog)}",
        "",
        "This index is derived from local PDF extraction. Author fields are taken from PDF metadata when available and otherwise guessed from the first page.",
        "",
    ]
    for index, record in enumerate(catalog, start=1):
        summary_lines.extend(
            [
                f"## {index}. {record['title']}",
                "",
                f"- Source file: `{record['source_filename']}`",
                f"- Authors: {record.get('authors') or 'Not reliably extracted'}",
                f"- Journal: {record.get('journal') or 'Not reliably extracted'}",
                f"- Year: {record.get('year') or 'Unknown'}",
                f"- DOI: {record.get('doi') or 'Not found'}",
                f"- Pages: {record.get('page_count')}",
                f"- Citation: {record.get('citation')}",
                f"- Abstract: {record.get('abstract') or 'Abstract not cleanly detected.'}",
                f"- HTML: `{record.get('html_path')}`",
                f"- JSON: `{record.get('json_path')}`",
                "",
            ]
        )
    (METADATA_DIR / "reading_index.md").write_text("\n".join(summary_lines).strip() + "\n", encoding="utf-8")

    readme_lines = [
        "# Metadata Output",
        "",
        "Generated assets:",
        "- `catalog.json` and `catalog.csv`: cross-paper index.",
        "- `reading_index.md`: human-readable overview of the 50 papers.",
        "- `meatdatagenerated/text`: full extracted text per PDF.",
        "- `meatdatagenerated/json`: per-paper metadata, abstract, headings, figure captions, and output paths.",
        "- `../html`: one editable HTML file per PDF.",
        "- `../images`: citation manifests and figure-reference index for later Wiley-style figure insertion.",
        "",
        "Regenerate by running:",
        "",
        "```powershell",
        "python metadata\\_tools\\process_papers.py",
        "```",
        "",
    ]
    (METADATA_DIR / "README.md").write_text("\n".join(readme_lines), encoding="utf-8")

    images_readme = [
        "# Image Prep",
        "",
        "This folder is reserved for later image generation and insertion work.",
        "",
        "Available now:",
        "- `wiley_source_manifest.json`: one citation entry per paper for source attribution.",
        "- `figure_reference_index.csv`: detected figure captions mapped back to each source paper.",
        "",
        "Suggested Wiley-style credit pattern for adapted figures:",
        "- `Adapted from {citation}.`",
        "- `Reproduced from {citation}, with permission.`",
        "",
    ]
    (IMAGES_DIR / "README.md").write_text("\n".join(images_readme), encoding="utf-8")

    if errors:
        (METADATA_DIR / "errors.json").write_text(
            json.dumps(errors, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print(f"Processed {len(catalog)} PDFs")
    if errors:
        print(f"Errors: {len(errors)}")


if __name__ == "__main__":
    main()
