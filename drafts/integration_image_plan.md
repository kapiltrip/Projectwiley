# Integration Image Plan

## Goal

The final paper should feel visually rich but still disciplined. The right target is not “many screenshots from many papers.” The right target is a coherent figure system that helps a reviewer understand the paper quickly. For a 20-page conference-style review, a strong balance is:

- 4 original synthesis figures drawn specifically for this paper.
- 5 to 7 adapted or redrawn figures from source papers.
- 2 to 3 result plots that illustrate a key tradeoff or deployment lesson.

That mix keeps the paper image-heavy enough to feel substantial while avoiding the look of a collage.

## Figure list tied to the conference-critique items

Some weaknesses in the critique were fixed directly in text and tables inside `integration.md`. The remaining visual weaknesses should be solved with the following figures in the next iteration.

### Figure A. Corpus construction and scope figure

- Weakness addressed:
  Missing visible review methodology and corpus framing.
- Type:
  fully original.
- Content:
  Show the fixed-corpus review structure: fifty-paper corpus, inclusion logic, five classification dimensions, and the major topic buckets used in the paper.
- Best placement:
  Section 2.

### Figure B. Intent-robust timing closure map

- Weakness addressed:
  The paper needs a visual identity for the central concept rather than prose-only framing.
- Existing recommendation:
  Current Figure 1 in this plan.
- Best placement:
  Introduction or end of Section 2.

### Figure C. Integrated closure stack

- Weakness addressed:
  The blueprint is still conceptually dense and benefits from a single architecture figure.
- Existing recommendation:
  Current Figure 13 in this plan.
- Best placement:
  Section 7.

### Figure D. Representative execution sequence

- Weakness addressed:
  The blueprint now has a textual execution sequence, but it still needs a flowchart that shows how a design moves from early triage to trusted fallback and reliability closure.
- Type:
  fully original.
- Content:
  Draw the six-step loop now written in Section 7.8, including decision points for uncertainty gating and fallback to trusted STA/PBA.
- Best placement:
  Section 7, immediately after the integrated closure stack.

### Figure E. Evaluation matrix for intent-robust closure

- Weakness addressed:
  The paper now defines an operational rubric, but a visual matrix will make the evaluation framework clearer to reviewers.
- Existing recommendation:
  Current Figure 14 in this plan.
- Best placement:
  Section 8.

### Figure F. Stage-mismatch and correlation-restoration visual pair

- Weakness addressed:
  The paper’s strongest deployment argument is stage alignment, and that should be visually obvious.
- Existing recommendation:
  Current Figure 5 from [8] and Figure 6 from [10].
- Best placement:
  Section 4.5 or split across Sections 4.5 and 7.3.

### Figure G. Safe ML integration visual pair

- Weakness addressed:
  The paper argues that deployable ML learns decisions and preserves fallback; that argument should not remain text-only.
- Existing recommendation:
  Current Figure 7 from [16] and Figure 8 or Figure 9 from [22] and [21].
- Best placement:
  Sections 4.7 and 5.1, or summarized again in Section 7.

## Tables that already solve part of the critique inside the manuscript

These are already inserted directly into `integration.md` as text tables and do not need separate image creation unless we later choose to style them visually:

- Table 1:
  prior-survey comparison against [20], [39], and [49].
- Table 2:
  operational definition of intent-robustness.
- Table 3:
  cross-paper family matrix with trust anchors and failure modes.

## Visual policy

- Prefer redrawn figures over pasted screenshots, even when a source figure is strong.
- Prefer concept and workflow figures over dense benchmark plots.
- Use result plots only when they support a central argument such as runtime-versus-fidelity, stage mismatch, or safe fallback.
- Keep one visual language across all figures: same fonts, same line weights, same arrow style, same caption style.
- Favor open-access source figures first when possible. From the local HTML corpus, the MDPI papers in [1], [15], [19], [28], [31], and [33] clearly indicate CC BY terms, which makes them easier candidates for later adaptation with attribution.
- For ACM, IEEE, and Elsevier figures, the safest practical route is usually to redraw the concept in a new style and then cite the underlying source in the caption and references. Permission requirements still depend on the eventual venue and publisher, so that check should be done at the figure-insertion stage.

## Practical permission references checked for this plan

- ACM third-party material guidance:
  https://www.acm.org/publications/authors/third-party-material
- Wiley permissions guidance:
  https://authorservices.wiley.com/author-resources/Journal-Authors/Prepare/permissions-material.html
- Wiley licensing FAQ:
  https://authorservices.wiley.com/author-resources/Journal-Authors/licensing/licensing-info-faqs.html
- Elsevier permissions hub:
  https://www.elsevier.com/about/policies-and-standards/copyright/permissions

## Recommended figure set for the final paper

### Figure 1. Original synthesis figure: intent-robust timing closure map

- Section placement: Introduction or end of Section 2.
- Type: fully original.
- Content:
  Show the three dimensions of intent drift: design intent, operating intent, and silicon intent. Show where ML, SSTA, reliability-aware timing, and GPU acceleration sit relative to the closure loop.
- Why this figure matters:
  It gives the paper its own identity and prevents the review from looking like a collection of unrelated subfields.
- Source basis:
  Conceptually informed by [20], [39], and [49], but should be redrawn from scratch.

### Figure 2. Adapted from [1]: placement guidance as action-oriented ML

- Recommended source:
  [1], Figure 2, “Overview of optimization guidance framework based on physical and timing prediction to improve placement quality.”
- Section placement: Section 4.2.
- Preferred treatment: redraw.
- Why this figure:
  It communicates that ML at placement stage can suggest concrete actions rather than only predict numbers.

### Figure 3. Adapted from [29]: preplacement timing via explicit net-length estimation

- Recommended source:
  [29], Figure 2, “Net size and timing prediction flow.”
- Section placement: Section 4.1.
- Preferred treatment: redraw.
- Why this figure:
  It visually supports one of the paper’s recurring arguments: robust early-stage timing usually needs physically meaningful intermediate variables.

### Figure 4. Adapted from [17]: hierarchical pre-route timing prediction

- Recommended source:
  [17], Figure 12, “Architecture of our pre-route timing prediction framework.”
- Section placement: Section 4.4.
- Preferred treatment: redraw.
- Why this figure:
  This is one of the strongest pipeline figures in the corpus. It cleanly shows level-1 prediction of net R, net C, and arc length, followed by level-2 delay and slew prediction.

### Figure 5. Adapted from [8]: optimization-aware multimodal prediction

- Recommended source:
  [8], Figure 2, “Overview of our proposed end-to-end endpoint embedding framework PRO-TIME.”
- Backup source:
  [8], Figure 1, “Example of feature mismatching caused by timing optimization.”
- Section placement: Section 4.5.
- Preferred treatment: redraw and simplify.
- Why this figure:
  It explains the strongest recent point in the prerouting literature: a predictor that ignores optimization-induced feature mismatch is often mis-specified for real flows.

### Figure 6. Adapted from [10]: stage mismatch between global route and detailed route

- Recommended source:
  [10], Figure 10, “Flows that use different parasitic estimates for post-GR timing optimizations.”
- Backup source:
  [10], Figure 4, discrepancy between post-GR and post-DR wire delays.
- Section placement: Section 4.5 or early in Section 6.
- Preferred treatment: redraw.
- Why this figure:
  It is the cleanest visual support for the paper’s “correlation bridge” argument.

### Figure 7. Adapted from [16]: safe multicorner prediction with Bayesian fallback

- Recommended source:
  [16], Figure 1, “Workflow of our timing prediction method… with Bayesian decision theory.”
- Section placement: Section 4.7 or Section 7.
- Preferred treatment: redraw.
- Why this figure:
  This is one of the best figures for explaining safe ML integration. It supports the paper’s key synthesis that robust ML systems learn decisions and preserve fallback.

### Figure 8. Adapted from [22]: heterogeneous multicorner STA engine

- Recommended source:
  [22], Figure 5, “Overall taskflow of our GPU-accelerated multicorner STA engine.”
- Backup source:
  [22], Figure 2, PVT corner cube, if a simpler conceptual visual is needed.
- Section placement: Section 5.1.
- Preferred treatment: redraw.
- Why this figure:
  This is the core engine-acceleration figure in the corpus. It visually explains why GPU acceleration matters beyond toy kernels.

### Figure 9. Adapted from [21]: runtime-versus-fidelity argument for PBA

- Recommended source:
  [21], Figure 1, “Computational tradeoff between runtime and pessimism reduction on path-based timing analysis.”
- Backup source:
  [21], Figure 3, “Overview of core GPU-accelerated PBA algorithm.”
- Section placement: Section 5.1.
- Preferred treatment: use Figure 1 for the main paper and keep Figure 3 as reserve.
- Why this figure:
  It makes the runtime-versus-accuracy story legible in one glance.

### Figure 10. Adapted from [12]: dynamic supply noise aware STA integration

- Recommended source:
  [12], Figure 9, “Architecture of the proposed MLP model.”
- Backup source:
  [12], Figure 10, “Example ML model and JIT IR representation.”
- Section placement: Section 4.8 or Section 7.
- Preferred treatment: redraw.
- Why this figure:
  It supports the claim that ML can sit inside the timing engine as a structured primitive rather than as a black-box external regressor.

### Figure 11. Adapted from [14] and [15]: aging-aware timing from cell to path

- Recommended structure:
  Make this a composite custom figure rather than directly reproducing a single source figure.
- Left panel source:
  [14], Figure 1 or Figure 2 for heterogeneous graph-based cell timing.
- Right panel source:
  [15], Figure 3, “The overall process of the aging-aware timing prediction model.”
- Section placement: Section 4.9.
- Preferred treatment: fully redrawn composite.
- Why this figure:
  It lets the paper show a clean progression from cell-level aging modeling to path-level aging prediction, which is more valuable than showing either source alone.

### Figure 12. Adapted from [23]: aging changes which paths matter

- Recommended source:
  [23], Figure 1, “Example showing how the path, which was uncritical before aging, became critical after aging.”
- Section placement: Section 4.9 or Section 7.6.
- Preferred treatment: redraw.
- Why this figure:
  This is an unusually intuitive figure. It immediately communicates why nominal critical-path ranking is insufficient.

### Figure 13. Original synthesis figure: integrated closure stack

- Section placement: Section 7.
- Type: fully original.
- Content:
  Draw the six layers proposed in the paper: semantics and statistical guardrails, early-stage triage, stage-alignment correction, uncertainty-gated scenario reduction, accelerated high-fidelity truth, and reliability and lifetime closure.
- Why this figure matters:
  It is the most important custom figure in the paper because it converts the review into a reusable architecture.

### Figure 14. Original synthesis figure: evaluation matrix for robust timing closure

- Section placement: Section 8.
- Type: fully original.
- Content:
  Build a matrix with rows such as predictor fidelity, critical-path ranking, signoff alignment, missed-violation risk, ECO robustness, corner-transfer robustness, runtime per iteration, and lifetime robustness.
- Why this figure matters:
  It makes the paper look more mature and helps reviewers see that the paper is proposing an evaluative framework, not only summarizing methods.

## Reserve figures if extra space is available

- Reserve A:
  [28], Figure 10, workflow comparison between commercial timing closure and ML-based timing closure.
- Reserve B:
  [11], Figure 3, R-CNN structure for timing-table interpolation.
- Reserve C:
  [24], Figure 5, deep-learning waveform-delay modeling inside cell characterization.
- Reserve D:
  [25], Figure 3, predicted versus actual cell delay after post-placement correction.

## Best image mix for this paper

If the final paper carries 10 to 12 figures, my preferred mix is:

- 4 original synthesis figures:
  Figure 1, Figure 13, Figure 14, and one additional custom taxonomy or timeline if space allows.
- 6 adapted or redrawn method figures:
  [1], [17], [8], [10], [16], and [22].
- 2 adapted or redrawn tradeoff figures:
  [21] for runtime-versus-pessimism and [23] for aging-driven path-rank change.

That set gives the paper both originality and authority.

## My strongest recommendations

If later we have to cut aggressively, do not cut these:

- Original Figure 1: intent-robust timing closure map.
- [17] hierarchical pre-route timing framework.
- [8] optimization-aware multimodal prediction.
- [16] Bayesian multicorner fallback workflow.
- [22] GPU-accelerated multicorner STA engine.
- Original Figure 13: integrated closure stack.

Those six figures carry the main intellectual story of the paper.

## Caption and attribution strategy for the later insertion pass

- Original figures:
  Caption as normal, no source line needed.
- Redrawn or adapted figures from source papers:
  Caption should name the source paper explicitly and use “adapted from” or “redrawn based on.”
- If a figure merges two or more papers:
  Caption should explicitly say “synthesized from” and then cite each contributing paper separately.
- For the final venue:
  Confirm publisher-specific reuse and attribution rules before submission. The exact rule set depends on where the paper is submitted, not only on the source publisher.

## Final recommendation

The final paper should not aim to be “full of images” in the casual sense. It should aim to be *visually explanatory*. The best version of this paper will feel image-rich because every section opens with a clean conceptual or workflow figure, not because many benchmark plots were inserted. The strongest visual narrative is:

- define the problem,
- show how ML enters the flow,
- show how stage mismatch is corrected,
- show how safe fallback is handled,
- show how trusted engines are accelerated,
- show how the full integrated architecture fits together.
