# Image Source Cross-Check

Purpose:
- verify that each figure file used in `drafts/overleaf_bundle/main.tex` maps to the cited source paper
- verify that the cited paper contains a matching figure caption in the local PDF metadata
- note any manuscript corrections needed after the audit

Evidence used:
- `usedImages/README.md`
- `metadata/meatdatagenerated/json/*.json`
- local PDFs in `papers50/`
- current manuscript: `drafts/overleaf_bundle/main.tex`

## Results

| Manuscript image | Cited ref | Verified source figure | Source caption check | Status |
| --- | --- | --- | --- | --- |
| `01_overall_ml_timing_closure_process.png` | `ref28` | `Fig. 10` | `The commercial timing closure process (left) and machine-learning-based timing closure process (right).` | Verified |
| `02_sta_illustration.jpg` | `ref49` | `Fig. 8` | `Illustration of static timing analysis.` | Verified |
| `03_block_vs_path_traversal.jpg` | `ref49` | `Fig. 10` | `Path-based (above) and block-based (below) timing graph traversal.` | Verified |
| `04_placement_guidance_framework.png` | `ref1` | `Figure 2` | `Overview of optimization guidance framework based on physical and timing prediction to improve placement quality.` | Verified |
| `05_preroute_timing_prediction_flow.jpg` | `ref17` | `Fig. 7` | `The overall flow of our proposed timing prediction (blue line) and optimization (red line) framework.` | Verified |
| `06_protime_endpoint_embedding.png` | `ref8` | `Fig. 2` | `Overview of our proposed end-to-end endpoint embedding framework PRO-TIME...` | Verified |
| `07_gr_dr_timing_consistency.jpg` | `ref10` | `Fig. 7` | `Flows that use different parasitic estimates for post-GR timing optimizations...` | Verified |
| `08_bayesian_multicorner_workflow.png` | `ref16` | `Fig. 1` | `Workflow of our timing prediction method... with Bayesian decision theory.` | Verified |
| `09_psn_mlp_architecture.png` | `ref12` | `Fig. 9` | `Architecture of the proposed MLP model.` | Verified |
| `10_aging_critical_cell_pipeline.png` | `ref23` | `Fig. 6` | `Framework of GAT-based critical cell detection...` | Verified |
| `11_aging_path_shift_example.png` | `ref23` | `Fig. 1` | `Example showing how the path, which was uncritical before aging, became critical after aging...` | Verified |
| `12_gpu_sta_taskflow.png` | `ref22` | `Fig. 4` | `Overall taskflow of our GPU-accelerated multicorner STA engine.` | Verified |
| `13_gpu_pba_preprocess.png` | `ref21` | `Fig. 6` | `Overview of preprocessing steps for path constraints handling.` | Verified after caption correction |

## Manuscript corrections applied after audit

- Figure captions were updated to cite the exact source figure numbers in the local papers.
- The GPU PBA figure was corrected to match `ref21` Figure 6 specifically.
  Before correction, the caption wording was broader than the actual source figure.
  After correction, it now matches the verified source content: preprocessing for path-constraint handling before parallel PBA kernels.
- The aging discussion was tightened so that the two aging figures are explicitly anchored to `ref23`, while `ref14` and `ref15` are used as complementary model-level evidence rather than as the direct source of those two images.

## Overall conclusion

The current image set in `drafts/overleaf_bundle/main.tex` is source-traceable against the local paper corpus. After the caption fix for the GPU PBA figure, all figure files used in the manuscript are aligned with the cited source papers and with matching figure captions in the local PDF metadata.
