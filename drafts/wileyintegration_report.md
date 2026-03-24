# Wiley Integration Report

## Output

- Wiley manuscript file: [wileyintegration.tex](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/wileyintegration.tex)
- Source manuscript used: [integration.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/integration.md)
- BibTeX file: [references.bib](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/references.bib)
- Citation review: [wileyintegration_citation_review.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/wileyintegration_citation_review.md)
- Reference map: [wileyintegration_reference_map.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/wileyintegration_reference_map.md)
- Images folder manifest: [images/README.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/images/README.md)

## Done

- Created a separate Wiley-format manuscript file without modifying the source paper content in [integration.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/integration.md).
- Preserved the current paper title, abstract, keywords, section text, inline numbered citations, and reference ordering from the integrated manuscript.
- Converted inline numbered citations from raw bracketed references to LaTeX `\cite{refN}` calls.
- Preserved the original corpus numbering internally through stable BibTeX keys `ref1` through `ref50`.
- Converted the three markdown tables in the source manuscript into LaTeX tables inside the Wiley manuscript.
- Inserted `16` figure environments into the Wiley manuscript at the relevant sections based on the existing image plan.
- Used compile-safe figure placeholders so the Wiley manuscript can still be completed even before the actual image assets are generated.
- Created a separate `references.bib` file and switched the Wiley manuscript to `\bibliography{references}`.
- Normalized fetched BibTeX entries for LaTeX safety, including escaped ampersands and normalized page-range dashes.
- Created an `images` folder layout for the Wiley manuscript and documented the expected figure filenames.
- Added a separate reference-map audit so each `refN` key can be checked against the original fixed-corpus source list.

## Bibliography generation

- `ref1` -> DOI `10.3390/electronics14020329` using `doi-metadata` metadata.
- `ref2` -> DOI `10.1016/j.asoc.2025.114100` using `doi-metadata` metadata.
- `ref3` -> DOI `10.1145/3780100` using `doi-metadata` metadata.
- `ref4` -> DOI `10.1016/j.mejo.2024.106542` using `doi-metadata` metadata.
- `ref5` -> DOI `10.3390/automation6020020` using `doi-metadata` metadata.
- `ref6` -> DOI `10.1109/TCAD.2024.3523426` using `doi-metadata` metadata.
- `ref7` -> DOI `10.1109/TCAD.2024.3506216` using `doi-metadata` metadata.
- `ref8` -> DOI `10.1109/TCAD.2025.3569488` using `doi-metadata` metadata.
- `ref9` -> DOI `10.1016/j.aeue.2025.155870` using `doi-metadata` metadata.
- `ref10` -> DOI `10.1145/3626959` using `doi-metadata` metadata.
- `ref11` -> DOI `10.1109/TCAD.2023.3316991` using `doi-metadata` metadata.
- `ref12` -> DOI `10.1109/TCAD.2023.3342603` using `doi-metadata` metadata.
- `ref13` -> DOI `10.1016/j.vlsi.2024.102193` using `doi-metadata` metadata.
- `ref14` -> DOI `10.1109/TCSII.2023.3298917` using `doi-metadata` metadata.
- `ref15` -> DOI `10.3390/electronics13173479` using `doi-metadata` metadata.
- `ref16` -> DOI `10.1109/TCAD.2024.3361401` using `doi-metadata` metadata.
- `ref17` -> DOI `10.1016/j.vlsi.2024.102262` using `doi-metadata` metadata.
- `ref18` -> DOI `10.1007/s11081-023-09847-3` using `doi-metadata` metadata.
- `ref19` -> DOI `10.3390/electronics13152897` using `doi-metadata` metadata.
- `ref20` -> DOI `10.3724/SP.J.1089.2023.19557` using `doi-metadata` metadata.
- `ref21` -> DOI `10.1109/TCAD.2023.3272274` using `doi-metadata` metadata.
- `ref22` -> DOI `10.1109/TCAD.2023.3286261` using `doi-metadata` metadata.
- `ref23` -> DOI `10.1109/TCAD.2023.3276944` using `doi-metadata` metadata.
- `ref24` -> DOI `10.1016/j.asej.2022.101828` using `doi-metadata` metadata.
- `ref25` -> DOI `10.1016/j.vlsi.2023.02.011` using `doi-metadata` metadata.
- `ref26` -> DOI `10.1109/TCAD.2023.3255167` using `doi-metadata` metadata.
- `ref27` -> DOI `10.1016/j.micpro.2022.104671` using `doi-metadata` metadata.
- `ref28` -> DOI `10.3390/electronics11101571` using `doi-metadata` metadata.
- `ref29` -> DOI `10.1109/TCAD.2022.3149977` using `doi-metadata` metadata.
- `ref30` -> DOI `10.1016/j.mejo.2022.105480` using `doi-metadata` metadata.
- `ref31` -> DOI `10.3390/electronics11223670` using `doi-metadata` metadata.
- `ref32` -> DOI `10.1016/j.mejo.2020.104938` using `doi-metadata` metadata.
- `ref33` -> DOI `10.3390/electronics9010157` using `doi-metadata` metadata.
- `ref34` -> DOI `10.1016/j.eswa.2020.113309` using `doi-metadata` metadata.
- `ref35` -> DOI `10.1049/iet-cds.2018.5616` using `doi-metadata` metadata.
- `ref36` -> DOI `10.1109/ACCESS.2019.2955091` using `doi-metadata` metadata.
- `ref37` -> DOI `10.1109/TCAD.2018.2821563` using `doi-metadata` metadata.
- `ref38` -> DOI `10.1109/TVLSI.2019.2893020` using `doi-metadata` metadata.
- `ref39` -> DOI `10.2197/ipsjtsldm.11.2` using `doi-metadata` metadata.
- `ref40` -> DOI `10.1109/TVLSI.2017.2703623` using `doi-metadata` metadata.
- `ref41` -> DOI `10.1016/j.vlsi.2014.07.003` using `doi-metadata` metadata.
- `ref42` -> DOI `10.1016/j.vlsi.2013.01.003` using `doi-metadata` metadata.
- `ref43` -> DOI `10.1109/TCAD.2012.2228305` using `doi-metadata` metadata.
- `ref44` -> DOI `10.1109/TDMR.2013.2237910` using `doi-metadata` metadata.
- `ref45` -> DOI `10.1016/j.mejo.2012.01.003` using `doi-metadata` metadata.
- `ref46` -> DOI `10.1016/j.mejo.2011.11.005` using `doi-metadata` metadata.
- `ref47` -> DOI `10.1109/TCAD.2011.2108030` using `doi-metadata` metadata.
- `ref48` -> DOI `10.1109/TVLSI.2009.2035323` using `doi-metadata` metadata.
- `ref49` -> DOI `10.1016/j.vlsi.2008.10.002` using `doi-metadata` metadata.
- `ref50` -> DOI `10.1109/TCAD.2005.858348` using `doi-metadata` metadata.

## Figure placeholders inserted

- `images/wiley_fig01_corpus_scope.pdf` inserted under `Review type, corpus, and classification protocol` with caption based on the planned Wiley figure set.
- `images/wiley_fig02_intent_robust_map.pdf` inserted under `Operational definition of intent-robustness` with caption based on the planned Wiley figure set.
- `images/wiley_fig03_preplacement_netlength_timing.pdf` inserted under `Early-stage timing prediction: it must preserve ranking, not claim signoff` with caption based on the planned Wiley figure set.
- `images/wiley_fig04_placement_guidance.pdf` inserted under `Placement-stage prediction must change the next physical move` with caption based on the planned Wiley figure set.
- `images/wiley_fig05_preroute_hierarchical.pdf` inserted under `Pre-route prediction works best when it models missing physics explicitly` with caption based on the planned Wiley figure set.
- `images/wiley_fig06_protime_mismatch.pdf` inserted under `Stage mismatch is a first-class problem, not a small residual error` with caption based on the planned Wiley figure set.
- `images/wiley_fig07_gr_dr_alignment.pdf` inserted under `Stage mismatch is a first-class problem, not a small residual error` with caption based on the planned Wiley figure set.
- `images/wiley_fig08_bayesian_multicorner.pdf` inserted under `Safe ML integration is often about selecting what to run, not predicting everything` with caption based on the planned Wiley figure set.
- `images/wiley_fig09_psn_timing_integration.pdf` inserted under `Primitive timing models are now an active ML frontier` with caption based on the planned Wiley figure set.
- `images/wiley_fig10_aging_cell_to_path.pdf` inserted under `ML is increasingly reliability-aware rather than nominal-only` with caption based on the planned Wiley figure set.
- `images/wiley_fig11_aging_path_shift.pdf` inserted under `ML is increasingly reliability-aware rather than nominal-only` with caption based on the planned Wiley figure set.
- `images/wiley_fig12_gpu_sta_taskflow.pdf` inserted under `GPU acceleration keeps trusted timing inside the loop` with caption based on the planned Wiley figure set.
- `images/wiley_fig13_gpu_pba_tradeoff.pdf` inserted under `GPU acceleration keeps trusted timing inside the loop` with caption based on the planned Wiley figure set.
- `images/wiley_fig14_integrated_closure_stack.pdf` inserted under `The Integration Blueprint: A Practical Architecture for Intent-Robust Timing Closure` with caption based on the planned Wiley figure set.
- `images/wiley_fig15_execution_sequence.pdf` inserted under `Representative execution sequence` with caption based on the planned Wiley figure set.
- `images/wiley_fig16_evaluation_matrix.pdf` inserted under `Experimental Methodology, Deployment Lessons, and Open Challenges` with caption based on the planned Wiley figure set.

## Pending

- Actual figure image files are still pending. The Wiley manuscript currently points to planned asset filenames and shows placeholders if those files are absent.
- Real Wiley front-matter metadata is still pending: authors, affiliations, corresponding author details, funding, acknowledgements, conflict of interest, and final journal section.
- The workspace does not currently contain the `wiley-article` class files or related journal assets, so compilation is expected to happen in an Overleaf/Wiley environment or after those files are added locally.
- Final figure callouts can be polished after the actual graphics are created and inserted.

## Notes

- The purpose of this pass was format conversion, not content rewriting.
- The remaining visual work is already mapped in [integration_image_plan.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/integration_image_plan.md).
- The status of the broader manuscript revision work remains recorded in [integration_verification.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/integration_verification.md).
