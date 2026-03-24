from __future__ import annotations

import csv
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
FIGURE_INDEX = ROOT / "images" / "figure_reference_index.csv"
SOURCE_MANIFEST = ROOT / "images" / "wiley_source_manifest.json"

TARGET_DIRS = [
    ROOT / "images",
    ROOT / "drafts" / "images",
    ROOT / "overleaf_bundle" / "images",
    ROOT / "drafts" / "overleaf_bundle" / "images",
]

EDGE_CANDIDATES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
]

VIEWPORT = (1800, 1120)
SCALE = 2


FIGURES = [
    {
        "filename": "wiley_fig01_corpus_scope.pdf",
        "kind": "custom",
        "title": "Corpus Construction And Scope",
        "subtitle": "Fixed-corpus review framing for the 50-paper STA timing-closure survey",
        "footer": "Original synthesis figure based on the local HTML corpus and manuscript structure.",
        "boxes": [
            ["50-paper local corpus", "Timing analysis, prediction, optimization, acceleration"],
            ["Inclusion logic", "Primary timing contribution plus at least one robustness axis"],
            ["Classification dimensions", "Flow stage | object | trust mechanism | robustness axis | evaluation mode"],
            ["Topic buckets", "ML timing | SSTA/semantics | reliability-aware timing | multicorner | GPU engines"],
        ],
    },
    {
        "filename": "wiley_fig02_intent_robust_map.pdf",
        "kind": "custom",
        "title": "Intent-Robust Timing Closure Map",
        "subtitle": "Three kinds of intent drift and the analysis layers that answer them",
        "footer": "Original synthesis figure reflecting the taxonomy used in the integrated review.",
        "bands": [
            ("Design intent drift", "Sizing, buffering, routing topology, ECO edits"),
            ("Operating intent drift", "Corner-set change, scenario reduction, method switching"),
            ("Silicon intent drift", "Aging, BTI, PSN, process variation"),
        ],
        "bottom_boxes": [
            "ML triage and guidance",
            "Statistical timing and label semantics",
            "Reliability-aware timing models",
            "Accelerated trusted STA/PBA",
        ],
    },
    {
        "filename": "wiley_fig03_preplacement_netlength_timing.pdf",
        "kind": "flow",
        "title": "Preplacement Timing Through Net-Length Estimation",
        "subtitle": "HTML-derived adaptation of the Net2 timing flow",
        "footer_source": "10.1109/TCAD.2022.3149977",
        "nodes": [
            "Netlist topology",
            "Customized GNN net-length estimator",
            "Predicted net sizes",
            "Preplacement timing estimator",
            "Slack / WNS / TNS estimate",
        ],
        "source_tag": "[29]",
    },
    {
        "filename": "wiley_fig04_placement_guidance.pdf",
        "kind": "flow",
        "title": "Placement Guidance As Action-Oriented ML",
        "subtitle": "HTML-derived adaptation of the placement optimization guidance framework",
        "footer_source": "10.3390/electronics14020329",
        "nodes": [
            "Global placement netlist",
            "Graph embedding",
            "Gate-sizing guidance",
            "Buffer-insertion guidance",
            "Path-group timing guidance",
            "Improved detail placement",
        ],
        "source_tag": "[1]",
    },
    {
        "filename": "wiley_fig05_preroute_hierarchical.pdf",
        "kind": "flow_two_stage",
        "title": "Hierarchical Pre-Route Timing Prediction",
        "subtitle": "HTML-derived adaptation of the two-level prediction pipeline",
        "footer_source": "10.1016/j.vlsi.2024.102262",
        "stage1": ["Net R", "Net C", "Arc length"],
        "stage2": ["Arc delay", "Arc slew", "Timing-margin guidance"],
        "source_tag": "[17]",
    },
    {
        "filename": "wiley_fig06_protime_mismatch.pdf",
        "kind": "flow",
        "title": "Optimization-Aware Multimodal Preroute Prediction",
        "subtitle": "HTML-derived adaptation of the PRO-TIME endpoint embedding workflow",
        "footer_source": "10.1109/TCAD.2025.3569488",
        "nodes": [
            "Netlist structure",
            "Layout context",
            "Endpoint embedding",
            "Optimization-aware target",
            "Prediction after feature mismatch control",
        ],
        "source_tag": "[8]",
    },
    {
        "filename": "wiley_fig07_gr_dr_alignment.pdf",
        "kind": "split_compare",
        "title": "Global-Route To Detailed-Route Alignment",
        "subtitle": "HTML-derived adaptation of the GR to DR correction idea",
        "footer_source": "10.1145/3626959",
        "left_title": "Post-GR estimate",
        "left_body": "Route-guide parasitics\nStage mismatch\nMacro effect missing",
        "right_title": "ML-corrected post-DR alignment",
        "right_body": "Parasitic correction\nTiming consistency\nBetter signoff-directed optimization",
        "source_tag": "[10]",
    },
    {
        "filename": "wiley_fig08_bayesian_multicorner.pdf",
        "kind": "decision",
        "title": "Safe Multicorner Prediction With Fallback",
        "subtitle": "HTML-derived adaptation of multicorner prediction plus Bayesian decision gating",
        "footer_source": "10.1109/TCAD.2024.3361401",
        "left_nodes": ["Run selected corners", "Predict remaining corners", "Estimate confidence"],
        "decision": "Confidence high?",
        "yes_nodes": ["Accept prediction", "Proceed with closure iteration"],
        "no_nodes": ["Invoke extra STA runs", "Return verified corner values"],
        "source_tag": "[16]",
    },
    {
        "filename": "wiley_fig09_psn_timing_integration.pdf",
        "kind": "flow",
        "title": "PSN-Aware Timing Inside STA",
        "subtitle": "HTML-derived adaptation of the ML-integrated dynamic supply-noise timing engine",
        "footer_source": "10.1109/TCAD.2023.3342603",
        "nodes": [
            "Noise-aware characterization",
            "PSN parameterization",
            "ML arc model",
            "JIT integration",
            "STA cell/path timing output",
        ],
        "source_tag": "[12]",
    },
    {
        "filename": "wiley_fig10_aging_cell_to_path.pdf",
        "kind": "split_compare",
        "title": "Aging-Aware Timing From Cell To Path",
        "subtitle": "Composite HTML-derived figure from cell-level and path-level aging modeling papers",
        "footer_source": "10.1109/TCSII.2023.3298917 | 10.3390/electronics13173479",
        "left_title": "Cell-level aging modeling",
        "left_body": "Device graph\nAging-aware delay\nFast cell timing update",
        "right_title": "Path-level aging prediction",
        "right_body": "Multi-view graph learning\nWorkload sensitivity\nPath delay degradation",
        "source_tag": "[14] + [15]",
    },
    {
        "filename": "wiley_fig11_aging_path_shift.pdf",
        "kind": "path_shift",
        "title": "Aging Changes Which Paths Matter",
        "subtitle": "HTML-derived interpretation of nominal-critical versus aged-critical paths",
        "footer_source": "10.1109/TCAD.2023.3276944",
        "source_tag": "[23]",
    },
    {
        "filename": "wiley_fig12_gpu_sta_taskflow.pdf",
        "kind": "flow",
        "title": "CPU-GPU Heterogeneous STA Taskflow",
        "subtitle": "HTML-derived adaptation of the multicorner STA engine pipeline",
        "footer_source": "10.1109/TCAD.2023.3286261",
        "nodes": [
            "CPU graph prep",
            "GPU levelization",
            "GPU delay / LUT evaluation",
            "GPU propagation",
            "Multicorner batching",
            "Incremental update handoff",
        ],
        "source_tag": "[22]",
    },
    {
        "filename": "wiley_fig13_gpu_pba_tradeoff.pdf",
        "kind": "tradeoff",
        "title": "Runtime Versus Fidelity For PBA",
        "subtitle": "HTML-derived tradeoff panel from the GPU path-based analysis paper",
        "footer_source": "10.1109/TCAD.2023.3272274",
        "source_tag": "[21]",
    },
    {
        "filename": "wiley_fig14_integrated_closure_stack.pdf",
        "kind": "stack",
        "title": "Integrated Closure Stack",
        "subtitle": "Six-layer architecture proposed by the review",
        "footer": "Original synthesis figure derived from the integrated manuscript blueprint.",
        "layers": [
            "Semantics and statistical guardrails",
            "Early-stage triage",
            "Stage-alignment correction",
            "Uncertainty-gated scenario reduction",
            "Accelerated high-fidelity truth",
            "Reliability and lifetime closure",
        ],
    },
    {
        "filename": "wiley_fig15_execution_sequence.pdf",
        "kind": "flow",
        "title": "Representative Execution Sequence",
        "subtitle": "HTML-rendered flowchart of the review's six-step closure loop",
        "footer": "Original synthesis figure corresponding to Section 7.8.",
        "nodes": [
            "Early screening",
            "Placement actions",
            "Routing-stage correlation restoration",
            "Scenario reduction with confidence gate",
            "Accelerated trusted analysis",
            "Reliability re-check before signoff",
        ],
    },
    {
        "filename": "wiley_fig16_evaluation_matrix.pdf",
        "kind": "matrix",
        "title": "Evaluation Matrix For Intent-Robust Closure",
        "subtitle": "Criteria that matter beyond held-out prediction error",
        "footer": "Original synthesis figure derived from the review's evaluation rubric.",
        "rows": [
            "Prediction fidelity",
            "Critical-path ranking",
            "Signoff alignment",
            "Missed-violation risk",
            "ECO robustness",
            "Corner robustness",
            "Runtime per iteration",
            "Lifetime robustness",
        ],
        "cols": ["ML triage", "Correction", "Decision layer", "Trusted engine", "Reliability layer"],
    },
]


PALETTE = {
    "bg": "#eef3f8",
    "card": "#ffffff",
    "ink": "#0f172a",
    "muted": "#4b5563",
    "edge": "#cbd5e1",
    "accent": "#154c79",
    "accent2": "#dbeafe",
    "soft": "#f8fafc",
    "warn": "#fde68a",
    "good": "#d1fae5",
    "bad": "#fee2e2",
}


def edge_path() -> Path:
    for candidate in EDGE_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("No supported headless browser found.")


def load_manifest() -> dict[str, dict]:
    if not SOURCE_MANIFEST.exists():
        return {}
    data = json.loads(SOURCE_MANIFEST.read_text(encoding="utf-8"))
    out = {}
    for entry in data:
        doi = (entry.get("doi") or "").strip()
        if doi:
            out[doi] = entry
    return out


def load_figure_index() -> dict[str, list[dict]]:
    if not FIGURE_INDEX.exists():
        return {}
    out: dict[str, list[dict]] = {}
    with FIGURE_INDEX.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            doi = (row.get("doi") or "").strip()
            if doi:
                out.setdefault(doi, []).append(row)
    return out


def wrap_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def source_footer(fig: dict, manifest: dict[str, dict], figure_index: dict[str, list[dict]]) -> str:
    doi = fig.get("footer_source")
    if not doi:
        return wrap_html(fig.get("footer", ""))
    parts = []
    for single in [d.strip() for d in doi.split("|")]:
        entry = manifest.get(single)
        if entry:
            title = entry.get("title", "")
            citation = entry.get("citation", "")
            parts.append(f"{title}. {citation}")
        elif single in figure_index:
            parts.append(single)
        else:
            parts.append(single)
    return wrap_html("Adapted from HTML-derived source metadata: " + " | ".join(parts))


def node_box(label: str, cls: str = "") -> str:
    return f'<div class="node {cls}">{wrap_html(label)}</div>'


def custom_boxes(boxes: list[list[str]]) -> str:
    html = ['<div class="grid four">']
    for title, body in boxes:
        html.append(
            '<div class="panel"><div class="panel-title">'
            + wrap_html(title)
            + '</div><div class="panel-body">'
            + wrap_html(body)
            + "</div></div>"
        )
    html.append("</div>")
    return "".join(html)


def render_body(fig: dict) -> str:
    kind = fig["kind"]
    if kind == "flow":
        inner = '<div class="flow">'
        for idx, label in enumerate(fig["nodes"]):
            if idx:
                inner += '<div class="arrow">-&gt;</div>'
            inner += node_box(label)
        inner += "</div>"
        if fig.get("source_tag"):
            inner += f'<div class="source-tag">{wrap_html(fig["source_tag"])}</div>'
        return inner

    if kind == "flow_two_stage":
        return (
            '<div class="stage-wrap">'
            '<div class="stage"><div class="stage-title">Level 1</div>'
            + "".join(node_box(x) for x in fig["stage1"])
            + '</div><div class="arrow tall">-&gt;</div>'
            + '<div class="stage"><div class="stage-title">Level 2</div>'
            + "".join(node_box(x, "accent") for x in fig["stage2"])
            + "</div></div>"
            + f'<div class="source-tag">{wrap_html(fig["source_tag"])}</div>'
        )

    if kind == "split_compare":
        return (
            '<div class="split">'
            f'<div class="half"><div class="panel-title">{wrap_html(fig["left_title"])}</div>'
            f'<div class="big-text">{wrap_html(fig["left_body"]).replace(chr(10), "<br>")}</div></div>'
            f'<div class="half"><div class="panel-title">{wrap_html(fig["right_title"])}</div>'
            f'<div class="big-text">{wrap_html(fig["right_body"]).replace(chr(10), "<br>")}</div></div>'
            '</div>'
            + f'<div class="source-tag">{wrap_html(fig["source_tag"])}</div>'
        )

    if kind == "decision":
        left = "".join(node_box(x) for x in fig["left_nodes"])
        yes = "".join(node_box(x, "good") for x in fig["yes_nodes"])
        no = "".join(node_box(x, "bad") for x in fig["no_nodes"])
        return (
            '<div class="decision-wrap"><div class="col">'
            + left
            + '</div><div class="diamond">'
            + wrap_html(fig["decision"])
            + '</div><div class="col two"><div class="branch yes">'
            + yes
            + '</div><div class="branch no">'
            + no
            + '</div></div></div>'
            + f'<div class="source-tag">{wrap_html(fig["source_tag"])}</div>'
        )

    if kind == "path_shift":
        return (
            '<div class="split">'
            '<div class="half pathpanel"><div class="panel-title">Nominal condition</div>'
            '<div class="pathrow"><span class="pathbox hot">Path A</span><span class="line"></span><span class="pathbox">Path B</span></div>'
            '<div class="big-text">Nominal ranking surfaces Path A as critical.</div></div>'
            '<div class="half pathpanel"><div class="panel-title">After aging</div>'
            '<div class="pathrow"><span class="pathbox">Path A</span><span class="line"></span><span class="pathbox hot">Path B</span></div>'
            '<div class="big-text">Aged ranking shifts criticality to Path B.</div></div>'
            '</div>'
            + f'<div class="source-tag">{wrap_html(fig["source_tag"])}</div>'
        )

    if kind == "tradeoff":
        return (
            '<div class="tradeoff">'
            '<div class="axes"><div class="ylabel">Fidelity / pessimism reduction</div><div class="xlabel">Runtime cost</div></div>'
            '<div class="plot">'
            '<div class="pt p1">GBA</div>'
            '<div class="pt p2">CPU PBA</div>'
            '<div class="pt p3">GPU PBA</div>'
            '<svg viewBox="0 0 900 500" preserveAspectRatio="none" class="plotline">'
            '<polyline points="120,360 440,220 760,110" fill="none" stroke="#154c79" stroke-width="6"/>'
            '</svg></div></div>'
            + f'<div class="source-tag">{wrap_html(fig["source_tag"])}</div>'
        )

    if kind == "stack":
        return (
            '<div class="stack">'
            + "".join(f'<div class="stack-layer">{wrap_html(layer)}</div>' for layer in fig["layers"])
            + "</div>"
        )

    if kind == "matrix":
        header = "".join(f"<th>{wrap_html(col)}</th>" for col in fig["cols"])
        rows = []
        classes = ["good", "warn", "accent", "soft", "bad"]
        for r_idx, row in enumerate(fig["rows"]):
            cells = "".join(f'<td class="{classes[(r_idx + c_idx) % len(classes)]}"></td>' for c_idx, _ in enumerate(fig["cols"]))
            rows.append(f"<tr><th>{wrap_html(row)}</th>{cells}</tr>")
        return '<table class="matrix"><thead><tr><th></th>' + header + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>"

    if kind == "custom":
        if "boxes" in fig:
            return custom_boxes(fig["boxes"])
        return (
            '<div class="band-grid">'
            + "".join(
                f'<div class="band"><div class="panel-title">{wrap_html(a)}</div><div class="panel-body">{wrap_html(b)}</div></div>'
                for a, b in fig["bands"]
            )
            + '</div><div class="bottom-grid">'
            + "".join(f'<div class="bottom-box">{wrap_html(x)}</div>' for x in fig["bottom_boxes"])
            + "</div>"
        )

    raise ValueError(f"Unsupported figure kind: {kind}")


def build_html(fig: dict, manifest: dict[str, dict], figure_index: dict[str, list[dict]]) -> str:
    footer = source_footer(fig, manifest, figure_index)
    body = render_body(fig)
    width, height = VIEWPORT
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    :root {{
      --bg: {PALETTE["bg"]};
      --card: {PALETTE["card"]};
      --ink: {PALETTE["ink"]};
      --muted: {PALETTE["muted"]};
      --edge: {PALETTE["edge"]};
      --accent: {PALETTE["accent"]};
      --accent2: {PALETTE["accent2"]};
      --soft: {PALETTE["soft"]};
      --warn: {PALETTE["warn"]};
      --good: {PALETTE["good"]};
      --bad: {PALETTE["bad"]};
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      width: {width}px;
      height: {height}px;
      overflow: hidden;
      background: linear-gradient(180deg, #eef4f8 0%, #f7fafc 100%);
      color: var(--ink);
      font-family: Georgia, "Times New Roman", serif;
    }}
    .frame {{
      width: 100%;
      height: 100%;
      padding: 46px 52px 36px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .hero {{
      background: var(--card);
      border: 2px solid var(--edge);
      border-radius: 26px;
      padding: 28px 34px 22px;
      box-shadow: 0 16px 40px rgba(15, 23, 42, 0.08);
    }}
    .title {{
      font-size: 40px;
      line-height: 1.15;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 10px;
    }}
    .subtitle {{
      font-size: 21px;
      line-height: 1.35;
      color: var(--muted);
    }}
    .content {{
      flex: 1;
      background: var(--card);
      border: 2px solid var(--edge);
      border-radius: 24px;
      padding: 28px 30px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      box-shadow: 0 14px 30px rgba(15, 23, 42, 0.06);
    }}
    .flow {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      flex-wrap: wrap;
    }}
    .node, .panel, .bottom-box, .stack-layer {{
      background: var(--soft);
      border: 2px solid var(--edge);
      border-radius: 18px;
      padding: 16px 18px;
      min-width: 220px;
      text-align: center;
      font-size: 22px;
      line-height: 1.28;
      font-weight: 600;
    }}
    .node.accent {{ background: var(--accent2); }}
    .node.good {{ background: var(--good); }}
    .node.bad {{ background: var(--bad); }}
    .arrow {{
      font-size: 34px;
      font-weight: 700;
      color: var(--accent);
      padding: 0 4px;
    }}
    .arrow.tall {{
      align-self: stretch;
      display: flex;
      align-items: center;
    }}
    .grid.four {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 22px;
    }}
    .panel-title {{
      font-size: 24px;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 10px;
    }}
    .panel-body, .big-text {{
      font-size: 22px;
      line-height: 1.4;
      color: var(--ink);
    }}
    .band-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 18px;
      margin-bottom: 20px;
    }}
    .band {{
      background: var(--soft);
      border: 2px solid var(--edge);
      border-radius: 18px;
      padding: 18px;
      min-height: 190px;
    }}
    .bottom-grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 16px;
    }}
    .bottom-box {{
      min-width: 0;
      background: var(--accent2);
    }}
    .stage-wrap {{
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: stretch;
      gap: 18px;
    }}
    .stage {{
      display: grid;
      gap: 14px;
      background: var(--soft);
      border: 2px solid var(--edge);
      border-radius: 20px;
      padding: 20px;
    }}
    .stage-title {{
      font-size: 26px;
      font-weight: 700;
      color: var(--accent);
      text-align: center;
      margin-bottom: 4px;
    }}
    .split {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 22px;
      align-items: stretch;
    }}
    .half {{
      background: var(--soft);
      border: 2px solid var(--edge);
      border-radius: 20px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      min-height: 340px;
    }}
    .decision-wrap {{
      display: grid;
      grid-template-columns: 1fr 220px 1fr;
      gap: 22px;
      align-items: center;
    }}
    .col {{
      display: grid;
      gap: 14px;
    }}
    .col.two {{
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
    }}
    .branch {{
      display: grid;
      gap: 12px;
      background: var(--soft);
      border: 2px solid var(--edge);
      border-radius: 18px;
      padding: 14px;
    }}
    .branch.yes {{ background: #f0fdf4; }}
    .branch.no {{ background: #fef2f2; }}
    .diamond {{
      width: 220px;
      height: 220px;
      margin: 0 auto;
      transform: rotate(45deg);
      background: var(--warn);
      border: 2px solid #d1a93f;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 16px;
      font-size: 26px;
      line-height: 1.2;
      text-align: center;
      color: var(--ink);
      font-weight: 700;
    }}
    .diamond > * {{ transform: rotate(-45deg); }}
    .tradeoff {{
      display: grid;
      grid-template-columns: 220px 1fr;
      gap: 18px;
      align-items: stretch;
      min-height: 430px;
    }}
    .axes {{
      position: relative;
      background: var(--soft);
      border: 2px solid var(--edge);
      border-radius: 18px;
    }}
    .ylabel {{
      position: absolute;
      left: 22px;
      top: 50%;
      transform: translateY(-50%) rotate(-90deg);
      transform-origin: left top;
      font-size: 22px;
      font-weight: 700;
      color: var(--accent);
      width: 360px;
      text-align: center;
    }}
    .xlabel {{
      position: absolute;
      bottom: 24px;
      left: 30px;
      font-size: 22px;
      font-weight: 700;
      color: var(--accent);
    }}
    .plot {{
      position: relative;
      background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
      border: 2px solid var(--edge);
      border-radius: 18px;
      min-height: 430px;
      overflow: hidden;
    }}
    .plotline {{
      position: absolute;
      inset: 0;
    }}
    .pt {{
      position: absolute;
      background: var(--accent);
      color: white;
      padding: 10px 14px;
      border-radius: 16px;
      font-size: 22px;
      font-weight: 700;
    }}
    .p1 {{ left: 120px; top: 300px; }}
    .p2 {{ left: 430px; top: 180px; }}
    .p3 {{ left: 720px; top: 80px; }}
    .stack {{
      display: grid;
      gap: 14px;
    }}
    .stack-layer {{
      background: linear-gradient(90deg, #eef6ff 0%, #ffffff 100%);
      text-align: left;
      font-size: 24px;
      padding-left: 28px;
    }}
    .matrix {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 10px;
      table-layout: fixed;
      font-size: 20px;
    }}
    .matrix th, .matrix td {{
      border: 2px solid var(--edge);
      border-radius: 14px;
      padding: 14px 10px;
      text-align: center;
    }}
    .matrix th {{ background: var(--soft); font-size: 19px; }}
    .matrix td.good {{ background: var(--good); }}
    .matrix td.warn {{ background: var(--warn); }}
    .matrix td.accent {{ background: var(--accent2); }}
    .matrix td.soft {{ background: #eef2ff; }}
    .matrix td.bad {{ background: #fee2e2; }}
    .pathpanel .pathrow {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      margin: 20px 0 26px;
    }}
    .pathbox {{
      min-width: 120px;
      padding: 18px 16px;
      background: white;
      border: 2px solid var(--edge);
      border-radius: 16px;
      font-size: 24px;
      font-weight: 700;
      text-align: center;
    }}
    .pathbox.hot {{
      background: #fee2e2;
      border-color: #f87171;
    }}
    .line {{
      height: 4px;
      flex: 1;
      background: var(--accent);
      border-radius: 4px;
      min-width: 80px;
    }}
    .source-tag {{
      margin-top: 18px;
      text-align: right;
      font-size: 20px;
      color: var(--muted);
      font-weight: 700;
    }}
    .footer {{
      background: var(--card);
      border: 2px solid var(--edge);
      border-radius: 18px;
      padding: 16px 22px;
      font-size: 18px;
      line-height: 1.35;
      color: var(--muted);
    }}
  </style>
</head>
<body>
  <div class="frame">
    <div class="hero">
      <div class="title">{wrap_html(fig["title"])}</div>
      <div class="subtitle">{wrap_html(fig["subtitle"])}</div>
    </div>
    <div class="content">
      {body}
    </div>
    <div class="footer">{footer}</div>
  </div>
</body>
</html>
"""


def render_html_to_png(browser: Path, html_path: Path, png_path: Path) -> None:
    args = [
        str(browser),
        "--headless",
        "--disable-gpu",
        f"--window-size={VIEWPORT[0]},{VIEWPORT[1]}",
        f"--force-device-scale-factor={SCALE}",
        f"--screenshot={png_path}",
        html_path.as_uri(),
    ]
    subprocess.run(args, check=True, capture_output=True)


def png_to_pdf(png_path: Path, pdf_path: Path) -> None:
    with Image.open(png_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(pdf_path, "PDF", resolution=300.0)


def ensure_targets() -> None:
    for directory in TARGET_DIRS:
        directory.mkdir(parents=True, exist_ok=True)


def main() -> None:
    ensure_targets()
    manifest = load_manifest()
    figure_index = load_figure_index()
    browser = edge_path()

    with tempfile.TemporaryDirectory(prefix="html_fig_render_") as tmp_name:
        tmp = Path(tmp_name)
        for fig in FIGURES:
            stem = Path(fig["filename"]).stem
            html_path = tmp / f"{stem}.html"
            png_path = tmp / f"{stem}.png"
            pdf_path = tmp / fig["filename"]

            html_path.write_text(build_html(fig, manifest, figure_index), encoding="utf-8", newline="\n")
            render_html_to_png(browser, html_path, png_path)
            png_to_pdf(png_path, pdf_path)

            for directory in TARGET_DIRS:
                shutil.copy2(png_path, directory / f"{stem}.png")
                shutil.copy2(pdf_path, directory / fig["filename"])

    print(f"Updated {len(FIGURES)} HTML-rendered figure assets as PNG and PDF files.")


if __name__ == "__main__":
    main()
