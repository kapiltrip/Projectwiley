# Wiley Images Folder

This folder is reserved for the figure assets referenced by `wileyintegration.tex`.
The LaTeX file is compile-safe even if these files are still missing because it falls back to placeholders.

## Planned figure files

### Review type, corpus, and classification protocol

- `wiley_fig01_corpus_scope.pdf`: Corpus construction and scope of this review. Original synthesis figure showing the fixed fifty-paper corpus, the inclusion logic, and the classification dimensions used in the manuscript.

### Operational definition of intent-robustness

- `wiley_fig02_intent_robust_map.pdf`: Intent-robust timing closure map. Original synthesis figure showing design-intent drift, operating-intent drift, silicon-intent drift, and the corresponding roles of ML, statistical timing, reliability-aware timing, and accelerated trusted analysis.

### Early-stage timing prediction: it must preserve ranking, not claim signoff

- `wiley_fig03_preplacement_netlength_timing.pdf`: Preplacement timing through explicit net-length estimation. Redrawn based on the flow in [29].

### Placement-stage prediction must change the next physical move

- `wiley_fig04_placement_guidance.pdf`: Placement-stage action-oriented learning. Redrawn based on the guidance framework in [1].

### Pre-route prediction works best when it models missing physics explicitly

- `wiley_fig05_preroute_hierarchical.pdf`: Hierarchical pre-route timing prediction. Redrawn based on the two-level framework in [17].

### Stage mismatch is a first-class problem, not a small residual error

- `wiley_fig06_protime_mismatch.pdf`: Optimization-aware multimodal preroute prediction. Redrawn and simplified from [8].
- `wiley_fig07_gr_dr_alignment.pdf`: Global-route to detailed-route timing mismatch and correction. Redrawn based on the stage-alignment analysis in [10].

### Safe ML integration is often about selecting what to run, not predicting everything

- `wiley_fig08_bayesian_multicorner.pdf`: Safe multicorner prediction with Bayesian fallback. Redrawn based on the workflow in [16].

### Primitive timing models are now an active ML frontier

- `wiley_fig09_psn_timing_integration.pdf`: Dynamic-supply-noise-aware timing integration inside STA. Redrawn based on the model structure in [12].

### ML is increasingly reliability-aware rather than nominal-only

- `wiley_fig10_aging_cell_to_path.pdf`: Aging-aware timing from cell-level modeling to path-level prediction. Composite figure to be redrawn from [14] and [15].
- `wiley_fig11_aging_path_shift.pdf`: Aging changes which paths matter. Redrawn based on the motivating example in [23].

### GPU acceleration keeps trusted timing inside the loop

- `wiley_fig12_gpu_sta_taskflow.pdf`: CPU-GPU heterogeneous multicorner STA taskflow. Redrawn based on [22].
- `wiley_fig13_gpu_pba_tradeoff.pdf`: Runtime-versus-fidelity tradeoff for path-based analysis. Redrawn based on [21].

### The Integration Blueprint: A Practical Architecture for Intent-Robust Timing Closure

- `wiley_fig14_integrated_closure_stack.pdf`: Integrated closure stack proposed in this review. Original synthesis figure showing the six layers of intent-robust timing closure.

### Representative execution sequence

- `wiley_fig15_execution_sequence.pdf`: Representative execution sequence for an intent-robust closure loop. Original synthesis flowchart based on Section 7.8.

### Experimental Methodology, Deployment Lessons, and Open Challenges

- `wiley_fig16_evaluation_matrix.pdf`: Evaluation matrix for intent-robust timing closure. Original synthesis figure covering fidelity, ranking, signoff alignment, missed-violation risk, runtime, and lifetime robustness.
