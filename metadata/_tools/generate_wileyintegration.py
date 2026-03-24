from __future__ import annotations

import csv
import html
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[2]
DRAFTS = ROOT / "drafts"
SOURCE_MD = DRAFTS / "integration.md"
TARGET_TEX = DRAFTS / "wileyintegration.tex"
TARGET_REPORT = DRAFTS / "wileyintegration_report.md"
TARGET_BIB = DRAFTS / "references.bib"
IMAGES_DIR = DRAFTS / "images"
IMAGES_README = IMAGES_DIR / "README.md"
CITATION_REVIEW = DRAFTS / "wileyintegration_citation_review.md"
REFERENCE_MAP = DRAFTS / "wileyintegration_reference_map.md"
CATALOG_CSV = ROOT / "metadata" / "catalog.csv"


TABLE_CAPTIONS = [
    "Comparison between this manuscript and the three most relevant surveys in the corpus.",
    "Operational rubric used in this review to interpret intent-robust timing closure.",
    "Cross-paper comparison of major method families, trust anchors, and failure modes.",
]


FIGURES = {
    "Review type, corpus, and classification protocol": [
        {
            "file": "images/wiley_fig01_corpus_scope.pdf",
            "label": "fig:wiley-corpus-scope",
            "caption": "Corpus construction and scope of this review. Original synthesis figure showing the fixed fifty-paper corpus, the inclusion logic, and the classification dimensions used in the manuscript.",
        }
    ],
    "Operational definition of intent-robustness": [
        {
            "file": "images/wiley_fig02_intent_robust_map.pdf",
            "label": "fig:wiley-intent-map",
            "caption": "Intent-robust timing closure map. Original synthesis figure showing design-intent drift, operating-intent drift, silicon-intent drift, and the corresponding roles of ML, statistical timing, reliability-aware timing, and accelerated trusted analysis.",
        }
    ],
    "Early-stage timing prediction: it must preserve ranking, not claim signoff": [
        {
            "file": "images/wiley_fig03_preplacement_netlength_timing.pdf",
            "label": "fig:wiley-preplacement",
            "caption": "Preplacement timing through explicit net-length estimation. Redrawn based on the flow in [29].",
        }
    ],
    "Placement-stage prediction must change the next physical move": [
        {
            "file": "images/wiley_fig04_placement_guidance.pdf",
            "label": "fig:wiley-placement-guidance",
            "caption": "Placement-stage action-oriented learning. Redrawn based on the guidance framework in [1].",
        }
    ],
    "Pre-route prediction works best when it models missing physics explicitly": [
        {
            "file": "images/wiley_fig05_preroute_hierarchical.pdf",
            "label": "fig:wiley-preroute-hierarchical",
            "caption": "Hierarchical pre-route timing prediction. Redrawn based on the two-level framework in [17].",
        }
    ],
    "Stage mismatch is a first-class problem, not a small residual error": [
        {
            "file": "images/wiley_fig06_protime_mismatch.pdf",
            "label": "fig:wiley-protime",
            "caption": "Optimization-aware multimodal preroute prediction. Redrawn and simplified from [8].",
        },
        {
            "file": "images/wiley_fig07_gr_dr_alignment.pdf",
            "label": "fig:wiley-gr-dr",
            "caption": "Global-route to detailed-route timing mismatch and correction. Redrawn based on the stage-alignment analysis in [10].",
        },
    ],
    "Safe ML integration is often about selecting what to run, not predicting everything": [
        {
            "file": "images/wiley_fig08_bayesian_multicorner.pdf",
            "label": "fig:wiley-bayesian-fallback",
            "caption": "Safe multicorner prediction with Bayesian fallback. Redrawn based on the workflow in [16].",
        }
    ],
    "Primitive timing models are now an active ML frontier": [
        {
            "file": "images/wiley_fig09_psn_timing_integration.pdf",
            "label": "fig:wiley-psn",
            "caption": "Dynamic-supply-noise-aware timing integration inside STA. Redrawn based on the model structure in [12].",
        }
    ],
    "ML is increasingly reliability-aware rather than nominal-only": [
        {
            "file": "images/wiley_fig10_aging_cell_to_path.pdf",
            "label": "fig:wiley-aging-composite",
            "caption": "Aging-aware timing from cell-level modeling to path-level prediction. Composite figure to be redrawn from [14] and [15].",
        },
        {
            "file": "images/wiley_fig11_aging_path_shift.pdf",
            "label": "fig:wiley-aging-shift",
            "caption": "Aging changes which paths matter. Redrawn based on the motivating example in [23].",
        },
    ],
    "GPU acceleration keeps trusted timing inside the loop": [
        {
            "file": "images/wiley_fig12_gpu_sta_taskflow.pdf",
            "label": "fig:wiley-gpu-sta",
            "caption": "CPU-GPU heterogeneous multicorner STA taskflow. Redrawn based on [22].",
        },
        {
            "file": "images/wiley_fig13_gpu_pba_tradeoff.pdf",
            "label": "fig:wiley-gpu-pba",
            "caption": "Runtime-versus-fidelity tradeoff for path-based analysis. Redrawn based on [21].",
        },
    ],
    "The Integration Blueprint: A Practical Architecture for Intent-Robust Timing Closure": [
        {
            "file": "images/wiley_fig14_integrated_closure_stack.pdf",
            "label": "fig:wiley-closure-stack",
            "caption": "Integrated closure stack proposed in this review. Original synthesis figure showing the six layers of intent-robust timing closure.",
        }
    ],
    "Representative execution sequence": [
        {
            "file": "images/wiley_fig15_execution_sequence.pdf",
            "label": "fig:wiley-execution-sequence",
            "caption": "Representative execution sequence for an intent-robust closure loop. Original synthesis flowchart based on Section 7.8.",
        }
    ],
    "Experimental Methodology, Deployment Lessons, and Open Challenges": [
        {
            "file": "images/wiley_fig16_evaluation_matrix.pdf",
            "label": "fig:wiley-evaluation-matrix",
            "caption": "Evaluation matrix for intent-robust timing closure. Original synthesis figure covering fidelity, ranking, signoff alignment, missed-violation risk, runtime, and lifetime robustness.",
        }
    ],
}


@dataclass
class ReferenceEntry:
    number: int
    title: str
    journal: str
    year: str
    doi: str
    raw: str


UNICODE_REPLACEMENTS = {
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u2013": "--",
    "\u2014": "--",
    "\u2212": "-",
    "\u2026": "...",
    "\u00a0": " ",
    "\u00d7": "x",
    "\u2192": "->",
    "\u2194": "<->",
    "\u2264": "<=",
    "\u2265": ">=",
    "\u2248": "~",
}


SPECIALS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def normalize_unicode(text: str) -> str:
    for src, dst in UNICODE_REPLACEMENTS.items():
        text = text.replace(src, dst)
    return text


def escape_latex(text: str) -> str:
    text = normalize_unicode(text)
    return "".join(SPECIALS.get(ch, ch) for ch in text)


def convert_inline(text: str) -> str:
    placeholders: list[tuple[str, str, str]] = []

    def stash(kind: str, content: str) -> str:
        token = f"@@{kind.upper()}{len(placeholders)}@@"
        placeholders.append((token, kind, content))
        return token

    text = re.sub(r"`([^`]+)`", lambda m: stash("code", m.group(1)), text)
    text = re.sub(r"\*\*([^*]+)\*\*", lambda m: stash("bold", m.group(1)), text)
    text = re.sub(r"\*([^*]+)\*", lambda m: stash("emph", m.group(1)), text)
    text = escape_latex(text)

    for token, kind, content in placeholders:
        converted = escape_latex(content)
        if kind == "code":
            repl = rf"\texttt{{{converted}}}"
        elif kind == "bold":
            repl = rf"\textbf{{{converted}}}"
        else:
            repl = rf"\emph{{{converted}}}"
        text = text.replace(escape_latex(token), repl)

    return text


def replace_citations(text: str) -> str:
    return re.sub(r"\[(\d+)\]", lambda m: rf"\cite{{ref{m.group(1)}}}", text)


def strip_heading_number(title: str) -> str:
    title = re.sub(r"^\d+(?:\.\d+)*\.?\s*", "", title).strip()
    return title


def format_heading(line: str) -> tuple[str, str] | None:
    if line.startswith("## "):
        title = strip_heading_number(line[3:].strip())
        if title == "Abstract" or title == "References":
            return None
        return "section", title
    if line.startswith("### "):
        title = strip_heading_number(line[4:].strip())
        return "subsection", title
    return None


def is_table_line(line: str) -> bool:
    return line.strip().startswith("|") and line.strip().endswith("|")


def parse_table(lines: list[str], start: int) -> tuple[list[str], int]:
    block = []
    i = start
    while i < len(lines) and is_table_line(lines[i]):
        block.append(lines[i].strip())
        i += 1
    return block, i


def markdown_table_to_latex(block: list[str], caption: str, label: str) -> str:
    rows = []
    for line in block:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        rows.append(cells)
    rows = [row for row in rows if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in row)]
    header = rows[0]
    body = rows[1:]
    cols = len(header)
    spec = " ".join([">{\\raggedright\\arraybackslash}X"] * cols)
    out = []
    out.append(r"\begin{table}[tbp]")
    out.append(r"\centering")
    out.append(rf"\caption{{{convert_inline(caption)}}}")
    out.append(rf"\label{{{label}}}")
    out.append(r"\small")
    out.append(rf"\begin{{tabularx}}{{\textwidth}}{{{spec}}}")
    out.append(r"\toprule")
    out.append(" & ".join(rf"\textbf{{{convert_inline(cell)}}}" for cell in header) + r" \\")
    out.append(r"\midrule")
    for row in body:
        out.append(" & ".join(convert_inline(cell) for cell in row) + r" \\")
    out.append(r"\bottomrule")
    out.append(r"\end{tabularx}")
    out.append(r"\end{table}")
    return "\n".join(out)


def list_block(lines: list[str], start: int) -> tuple[list[str], int, str] | None:
    bullet_pat = re.compile(r"^\-\s+")
    enum_pat = re.compile(r"^\d+\.\s+")
    if start >= len(lines):
        return None
    line = lines[start].rstrip()
    if bullet_pat.match(line):
        kind = "itemize"
        pat = bullet_pat
    elif enum_pat.match(line):
        kind = "enumerate"
        pat = enum_pat
    else:
        return None
    items = []
    i = start
    while i < len(lines):
        raw = lines[i].rstrip()
        if raw.strip() == "":
            i += 1
            break
        if not pat.match(raw):
            break
        items.append(pat.sub("", raw, count=1).strip())
        i += 1
    return items, i, kind


def figure_block(fig: dict[str, str]) -> str:
    caption = convert_inline(fig["caption"])
    return "\n".join(
        [
            r"\begin{figure}[tbp]",
            r"\centering",
            rf"\wileyfig{{{fig['file']}}}{{{caption}}}",
            rf"\caption{{{caption}}}",
            rf"\label{{{fig['label']}}}",
            r"\end{figure}",
        ]
    )


def extract_sections(lines: list[str]) -> tuple[str, str, list[str], list[str]]:
    title_line = lines[0].strip()
    title = title_line.lstrip("#").strip()
    if ":" in title:
        title = title.split(":", 1)[1].strip()

    abs_start = lines.index("## Abstract")
    kw_idx = next(i for i, line in enumerate(lines) if line.startswith("Keywords:"))
    abstract_lines = [line.strip() for line in lines[abs_start + 1 : kw_idx] if line.strip()]
    abstract = " ".join(abstract_lines)
    keywords = lines[kw_idx].split("Keywords:", 1)[1].strip()

    body_start = next(i for i, line in enumerate(lines) if line.startswith("## 1. Introduction"))
    refs_start = lines.index("## References")
    body_lines = lines[body_start:refs_start]
    ref_lines = lines[refs_start + 1 :]
    return title, abstract, body_lines, ref_lines


def convert_body(lines: list[str]) -> str:
    out: list[str] = []
    i = 0
    table_index = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            out.append("")
            i += 1
            continue

        heading = format_heading(line)
        if heading:
            level, title = heading
            if level == "section":
                out.append(rf"\section{{{convert_inline(title)}}}")
            else:
                out.append(rf"\subsection{{{convert_inline(title)}}}")
            if title in FIGURES:
                out.append("")
                for fig in FIGURES[title]:
                    out.append(figure_block(fig))
                    out.append("")
            i += 1
            continue

        if is_table_line(line):
            block, i = parse_table(lines, i)
            caption = TABLE_CAPTIONS[table_index] if table_index < len(TABLE_CAPTIONS) else f"Table {table_index + 1}."
            label = f"tab:wiley-{table_index + 1}"
            out.append(markdown_table_to_latex(block, caption, label))
            out.append("")
            table_index += 1
            continue

        parsed_list = list_block(lines, i)
        if parsed_list:
            items, i, kind = parsed_list
            out.append(rf"\begin{{{kind}}}")
            for item in items:
                out.append(rf"\item {convert_inline(item)}")
            out.append(rf"\end{{{kind}}}")
            out.append("")
            continue

        out.append(replace_citations(convert_inline(line)))
        out.append("")
        i += 1
    return "\n".join(out).rstrip() + "\n"


def parse_reference_entries(ref_lines: list[str]) -> list[ReferenceEntry]:
    refs: list[ReferenceEntry] = []
    pat = re.compile(
        r'^\[(\d+)\]\s+“([^”]+),?”\s+\*([^*]+)\*,\s+(\d{4})\.\s+doi:\s*([^\s.]+(?:\.[^\s.]+)*)\.?\s*$'
    )
    for line in ref_lines:
        line = line.strip()
        if not line:
            continue
        m = pat.match(line)
        if m:
            refs.append(
                ReferenceEntry(
                    number=int(m.group(1)),
                    title=m.group(2),
                    journal=m.group(3),
                    year=m.group(4),
                    doi=m.group(5).rstrip("."),
                    raw=line,
                )
            )
            continue
        m2 = re.match(r"^\[(\d+)\]\s+(.*)$", line)
        if m2:
            num = int(m2.group(1))
            text = m2.group(2)
            doi_match = re.search(r"doi:\s*([^\s.]+(?:\.[^\s.]+)*)", text)
            doi = doi_match.group(1).rstrip(".") if doi_match else ""
            title_match = re.search(r"“([^”]+)”", text)
            journal_match = re.search(r"\*([^*]+)\*,\s+(\d{4})", text)
            refs.append(
                ReferenceEntry(
                    number=num,
                    title=title_match.group(1) if title_match else f"Reference {num}",
                    journal=journal_match.group(1) if journal_match else "Unknown Journal",
                    year=journal_match.group(2) if journal_match else "",
                    doi=doi,
                    raw=line,
                )
            )
    return refs


def load_catalog_authors() -> dict[str, str]:
    authors: dict[str, str] = {}
    if not CATALOG_CSV.exists():
        return authors
    with CATALOG_CSV.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            doi = (row.get("doi") or "").strip()
            auth = (row.get("authors") or "").strip()
            if doi and auth:
                authors[doi] = auth
    return authors


def fetch_bibtex_via_doi(doi: str) -> str | None:
    if not doi:
        return None
    url = f"https://doi.org/{quote(doi, safe='/:')}"
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/x-bibtex; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (compatible; Codex bibliography generator)",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read().decode("utf-8", errors="replace").strip()
            return data or None
    except Exception:
        return None


def fallback_bibtex(ref: ReferenceEntry, author_map: dict[str, str]) -> str:
    authors = author_map.get(ref.doi, "Unknown")
    title = ref.title.replace("{", "").replace("}", "")
    journal = ref.journal.replace("{", "").replace("}", "")
    return (
        f"@article{{ref{ref.number},\n"
        f"  author = {{{authors}}},\n"
        f"  title = {{{title}}},\n"
        f"  journal = {{{journal}}},\n"
        f"  year = {{{ref.year}}},\n"
        f"  doi = {{{ref.doi}}}\n"
        f"}}"
    )


def normalize_bibtex_key(bibtex: str, number: int) -> str:
    bibtex = normalize_unicode(html.unescape(bibtex.strip()))
    bibtex = bibtex.replace("&", r"\&")
    return re.sub(r"^@(\w+)\{[^,]+,", rf"@\1{{ref{number},", bibtex, count=1)


def build_references_bib(refs: list[ReferenceEntry]) -> tuple[str, list[str]]:
    author_map = load_catalog_authors()
    entries = []
    report_lines = []
    for ref in refs:
        bib = fetch_bibtex_via_doi(ref.doi)
        source = "doi-metadata"
        if bib is None:
            bib = fallback_bibtex(ref, author_map)
            source = "local-fallback"
        bib = normalize_bibtex_key(bib, ref.number)
        entries.append(bib)
        report_lines.append(f"- `ref{ref.number}` -> DOI `{ref.doi}` using `{source}` metadata.")
    return "\n\n".join(entries) + "\n", report_lines


def build_citation_review() -> str:
    tex = TARGET_TEX.read_text(encoding="utf-8")
    bib = TARGET_BIB.read_text(encoding="utf-8")
    cite_keys = sorted(set(re.findall(r"\\cite\{(ref\d+)\}", tex)), key=lambda s: int(s[3:]))
    bib_keys = sorted(set(re.findall(r"@\w+\{(ref\d+),", bib)), key=lambda s: int(s[3:]))
    body = tex.split(r"\section{Introduction}", 1)[1].split(r"\bibliography{references}", 1)[0]
    stray_numeric = re.findall(r"(?<![A-Za-z])\[(\d+)\](?![A-Za-z])", body)
    multi_key_cites = re.findall(r"\\cite\{[^}]*,\s*[^}]*\}", body)
    missing_in_bib = [k for k in cite_keys if k not in bib_keys]
    uncited_bib = [k for k in bib_keys if k not in cite_keys]
    return (
        "# Wiley Citation Review\n\n"
        f"- Citation keys found in `wileyintegration.tex`: `{len(cite_keys)}`\n"
        f"- BibTeX keys found in `references.bib`: `{len(bib_keys)}`\n"
        f"- Missing bib entries for cited keys: `{len(missing_in_bib)}`\n"
        f"- Uncited bib entries: `{len(uncited_bib)}`\n"
        f"- Multi-key cite commands like `\\cite{{ref1,ref2}}`: `{len(multi_key_cites)}`\n"
        f"- Remaining raw numeric bracket citations in LaTeX body: `{len(stray_numeric)}`\n\n"
        "## Mapping rule\n\n"
        "- Internal key mapping is preserved as `refN -> original source reference [N]`.\n"
        "- Final printed citation numbers in the compiled PDF are assigned by the Wiley bibliography style, not by the internal key name.\n\n"
        "## Checks\n\n"
        f"- Missing bib keys: `{', '.join(missing_in_bib) if missing_in_bib else 'none'}`\n"
        f"- Uncited bib keys: `{', '.join(uncited_bib) if uncited_bib else 'none'}`\n"
        f"- Multi-key cite commands still present: `{'; '.join(multi_key_cites[:20]) if multi_key_cites else 'none'}`\n"
        f"- Raw bracket citations still present: `{', '.join(stray_numeric[:20]) if stray_numeric else 'none'}`\n"
    )


def build_reference_map(refs: list[ReferenceEntry]) -> str:
    tex = TARGET_TEX.read_text(encoding="utf-8")
    cite_hits = re.findall(r"\\cite\{(ref\d+)\}", tex)
    cite_count: dict[str, int] = {}
    for key in cite_hits:
        cite_count[key] = cite_count.get(key, 0) + 1

    lines = [
        "# Wiley Reference Map",
        "",
        "This file maps the manuscript's internal LaTeX citation keys to the original fixed-corpus reference numbers.",
        "Use it to verify that `refN` in `wileyintegration.tex` corresponds to source reference `[N]` from the integrated review corpus.",
        "",
        "## Notes",
        "",
        "- Key rule: `refN` always points to original source reference `[N]`.",
        "- The compiled PDF may print different numeric labels depending on the Wiley bibliography style.",
        "- Citation counts below are counts of `\\cite{refN}` occurrences in `wileyintegration.tex`.",
        "",
        "## Key map",
        "",
    ]
    for ref in refs:
        key = f"ref{ref.number}"
        hits = cite_count.get(key, 0)
        lines.append(
            f"- `{key}` | source `[{ref.number}]` | cites in LaTeX: `{hits}` | "
            f"{ref.title}. *{ref.journal}*, {ref.year}. DOI: `{ref.doi}`"
        )
    return "\n".join(lines) + "\n"


def write_images_manifest() -> None:
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Wiley Images Folder",
        "",
        "This folder is reserved for the figure assets referenced by `wileyintegration.tex`.",
        "The LaTeX file is compile-safe even if these files are still missing because it falls back to placeholders.",
        "",
        "## Planned figure files",
        "",
    ]
    for heading, figs in FIGURES.items():
        lines.append(f"### {heading}")
        lines.append("")
        for fig in figs:
            lines.append(f"- `{Path(fig['file']).name}`: {fig['caption']}")
        lines.append("")
    IMAGES_README.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def build_tex(title: str, abstract: str, body: str, refs: str, keywords: str) -> str:
    kw = ", ".join(convert_inline(k.strip()) for k in keywords.split(","))
    abstract_tex = convert_inline(abstract)
    title_tex = convert_inline(title)
    return rf"""\documentclass[num-refs]{{wiley-article}}
\usepackage{{siunitx}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage{{tabularx}}
\usepackage{{array}}
\usepackage{{url}}
\usepackage{{hyperref}}
\usepackage{{enumitem}}

\papertype{{Review Article}}
\paperfield{{Review}}

\title{{{title_tex}}}

\abbrevs{{STA, static timing analysis; SSTA, statistical static timing analysis; ECO, engineering change order; PBA, path-based analysis; WNS, worst negative slack; TNS, total negative slack.}}

\author[1]{{Author details pending}}
\affil[1]{{Affiliation details pending}}
\corraddress{{Corresponding author details pending}}
\corremail{{email pending}}
\runningauthor{{Author details pending}}

\newcommand{{\wileyfig}}[2]{{%
  \IfFileExists{{#1}}{{%
    \includegraphics[width=0.95\linewidth]{{#1}}%
  }}{{%
    \fbox{{%
      \parbox[c][0.24\textheight][c]{{0.9\linewidth}}{{%
        \centering Pending figure asset\\[4pt]
        \texttt{{\detokenize{{#1}}}}\\[6pt]
        #2%
      }}%
    }}%
  }}%
}}

\begin{{document}}

\begin{{frontmatter}}
\maketitle

\begin{{abstract}}
{abstract_tex}

\keywords{{{kw}}}
\end{{abstract}}
\end{{frontmatter}}

% Pending front-matter details not present in the source manuscript:
% real author names, affiliations, corresponding author details, funding,
% acknowledgements, conflict of interest statement, and journal section.
% Figure blocks have been inserted using compile-safe placeholders so the
% manuscript can be completed in the next iteration without changing the text.

{body}

\bibliography{{references}}

% Pending end-matter sections from the Wiley template were not populated because
% they were not present in the source manuscript.

\end{{document}}
"""


def build_report(title: str, bib_report: list[str]) -> str:
    fig_count = sum(len(v) for v in FIGURES.values())
    figure_lines = []
    for heading, figs in FIGURES.items():
        for fig in figs:
            figure_lines.append(
                f"- `{fig['file']}` inserted under `{heading}` with caption based on the planned Wiley figure set."
            )
    figure_text = "\n".join(figure_lines)
    return f"""# Wiley Integration Report

## Output

- Wiley manuscript file: [wileyintegration.tex]({TARGET_TEX.as_posix()})
- Source manuscript used: [integration.md]({SOURCE_MD.as_posix()})
- BibTeX file: [references.bib]({TARGET_BIB.as_posix()})
- Citation review: [wileyintegration_citation_review.md]({CITATION_REVIEW.as_posix()})
- Reference map: [wileyintegration_reference_map.md]({REFERENCE_MAP.as_posix()})
- Images folder manifest: [images/README.md]({IMAGES_README.as_posix()})

## Done

- Created a separate Wiley-format manuscript file without modifying the source paper content in [integration.md]({SOURCE_MD.as_posix()}).
- Preserved the current paper title, abstract, keywords, section text, inline numbered citations, and reference ordering from the integrated manuscript.
- Converted inline numbered citations from raw bracketed references to LaTeX `\\cite{{refN}}` calls.
- Preserved the original corpus numbering internally through stable BibTeX keys `ref1` through `ref50`.
- Converted the three markdown tables in the source manuscript into LaTeX tables inside the Wiley manuscript.
- Inserted `{fig_count}` figure environments into the Wiley manuscript at the relevant sections based on the existing image plan.
- Used compile-safe figure placeholders so the Wiley manuscript can still be completed even before the actual image assets are generated.
- Created a separate `references.bib` file and switched the Wiley manuscript to `\\bibliography{{references}}`.
- Normalized fetched BibTeX entries for LaTeX safety, including escaped ampersands and normalized page-range dashes.
- Created an `images` folder layout for the Wiley manuscript and documented the expected figure filenames.
- Added a separate reference-map audit so each `refN` key can be checked against the original fixed-corpus source list.

## Bibliography generation

{chr(10).join(bib_report)}

## Figure placeholders inserted

{figure_text}

## Pending

- Actual figure image files are still pending. The Wiley manuscript currently points to planned asset filenames and shows placeholders if those files are absent.
- Real Wiley front-matter metadata is still pending: authors, affiliations, corresponding author details, funding, acknowledgements, conflict of interest, and final journal section.
- The workspace does not currently contain the `wiley-article` class files or related journal assets, so compilation is expected to happen in an Overleaf/Wiley environment or after those files are added locally.
- Final figure callouts can be polished after the actual graphics are created and inserted.

## Notes

- The purpose of this pass was format conversion, not content rewriting.
- The remaining visual work is already mapped in [integration_image_plan.md]({(DRAFTS / 'integration_image_plan.md').as_posix()}).
- The status of the broader manuscript revision work remains recorded in [integration_verification.md]({(DRAFTS / 'integration_verification.md').as_posix()}).
"""


def main() -> None:
    lines = SOURCE_MD.read_text(encoding="utf-8").splitlines()
    title, abstract, body_lines, ref_lines = extract_sections(lines)
    refs = parse_reference_entries(ref_lines)
    body = convert_body(body_lines)
    body = replace_citations(body)
    bib_text, bib_report = build_references_bib(refs)
    TARGET_BIB.write_text(bib_text, encoding="utf-8", newline="\n")
    tex = build_tex(title, abstract, body, "", next(line for line in lines if line.startswith("Keywords:")).split("Keywords:", 1)[1].strip())
    TARGET_TEX.write_text(tex, encoding="utf-8", newline="\n")
    write_images_manifest()
    CITATION_REVIEW.write_text(build_citation_review(), encoding="utf-8", newline="\n")
    REFERENCE_MAP.write_text(build_reference_map(refs), encoding="utf-8", newline="\n")
    TARGET_REPORT.write_text(build_report(title, bib_report), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
