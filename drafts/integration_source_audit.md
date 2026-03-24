# Integration Source Audit

## Purpose

This file is the traceability record for [integration.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/integration.md). It is meant to answer one question clearly: when the review cites a paper, is it calling the right paper for the right point?

## Evidence Used

All checks in this audit were done against the local paper corpus and derived local files:

- [reading_index.md](C:/Users/kapil/OneDrive/Desktop/sta50journals/metadata/reading_index.md)
- [figure_reference_index.csv](C:/Users/kapil/OneDrive/Desktop/sta50journals/images/figure_reference_index.csv)
- extracted local HTML files in `html/`
- extracted local text files in `metadata/meatdatagenerated/text/`

The current line-by-line citation mapping for the latest manuscript text is in [integration_citation_calls.csv](C:/Users/kapil/OneDrive/Desktop/sta50journals/drafts/integration_citation_calls.csv). Use that file when you want the freshest line numbers after later editorial passes.

## Status Labels

- `Verified-direct`: the manuscript sentence matches an explicit method, result, or framing used in the cited paper.
- `Verified-contextual`: the manuscript uses the paper for background or scope in a way that is fair to the source.
- `Review-synthesis`: the paper is being used as part of this review’s broader interpretation, not as the sole direct source of the whole sentence.

## Metadata Corrections Applied During Audit

- `[31]` corrected to “Timing Analysis and Optimization Method with Interdependent Flip-Flop Timing Model for Near-Threshold Design.”
- `[45]` corrected to “Delay-Correlation-Aware SSTA Based on Conditional Moments.”

## Audit Entries

- `[1]` Lines `13, 19, 35, 39, 67, 69, 121, 129, 157, 183`. Verified use: placement-stage GNN guidance predicts candidate sizing and buffering actions, groups likely violating paths, and is correctly used as an action-oriented optimization example. Status: `Verified-direct`; broader “design-intent shift” usage is `Review-synthesis`.
- `[2]` Lines `69, 183`. Verified use: complex-network features augment placement-stage timing prediction and critical-path identification; the review uses it correctly as topology-aware feature engineering. Status: `Verified-direct`.
- `[3]` Lines `69, 129, 157, 203`. Verified use: derivable gradient boosting is correctly cited for optimization-compatible timing prediction at placement stage and for closed-loop evaluation relevance. Status: `Verified-direct`.
- `[4]` Lines `87, 133, 187`. Verified use: transfer learning across timing arcs reduces characterization cost and is fairly used for “label cost” and “transfer across tasks” arguments. Status: `Verified-direct`.
- `[5]` Lines `39, 77, 161, 191`. Verified use: GAT-based pre-routing slack prediction is correctly cited for endpoint-slack learning, propagation-structured modeling, and graph-model scalability discussion. Status: `Verified-direct`.
- `[6]` Lines `87, 145, 187`. Verified use: cross-node timing transfer is correctly cited for technology migration and transfer-learning robustness. Status: `Verified-direct`.
- `[7]` Lines `19, 35, 83, 125, 161, 183, 203`. Verified use: signoff-oriented routing-topology optimization is correctly cited for signoff alignment, topology change during closure, and closed-loop optimization. Status: `Verified-direct`; broader “design intent shift” use is `Review-synthesis`.
- `[8]` Lines `81, 129, 161, 187, 191`. Verified use: PRO-TIME is correctly cited for optimization-aware prerouting prediction, feature mismatch under timing optimization, and multimodal stage alignment. Status: `Verified-direct`.
- `[9]` Lines `91, 115, 121, 165, 199`. Verified use: TimeBoost is correctly cited for method selection rather than direct timing regression and for uncertainty-aware deployment logic. Status: `Verified-direct`.
- `[10]` Lines `13, 83, 125, 161, 183, 187`. Verified use: GR-to-DR mismatch correction is correctly cited for stage correlation gaps, signoff alignment, and correction-bridge deployment. Status: `Verified-direct`.
- `[11]` Lines `95, 115, 141, 169`. Verified use: ML-based timing-table interpolation with GPU parallelization is correctly cited as an inner-loop primitive improvement that must stay runtime-feasible. Status: `Verified-direct`.
- `[12]` Lines `19, 27, 35, 95, 125, 133, 145, 169, 195`. Verified use: dynamic-supply-noise-aware STA with JIT-integrated ML is correctly cited for operating-state drift, primitive-model integration, and multi-physics timing. Status: `Verified-direct`; broader “silicon intent shift” use is `Review-synthesis`.
- `[13]` Lines `73, 125, 161, 187`. Verified use: ensemble-tree post-placement delay correction is correctly cited as a conservative correlation-restoration method. Status: `Verified-direct`.
- `[14]` Lines `27, 99, 145, 173, 195`. Verified use: aging-aware cell timing via graph learning is correctly cited for primitive aging modeling and lifetime robustness. Status: `Verified-direct`.
- `[15]` Lines `19, 27, 99, 145, 173, 183, 195`. Verified use: path-level aging-aware timing prediction is correctly cited for workload-sensitive degradation and path-level lifetime prediction. Status: `Verified-direct`; broader use in the review taxonomy is `Review-synthesis`.
- `[16]` Lines `11, 19, 35, 91, 115, 121, 145, 165, 183, 199`. Verified use: multicorner acceleration with Bayesian decision logic is correctly cited for iterative physical design, uncertainty-aware gating, and safe fallback. Status: `Verified-direct`.
- `[17]` Lines `13, 39, 77, 133, 161, 183, 191, 203`. Verified use: hierarchical pre-route timing prediction and optimization is correctly cited for net-R/net-C/length intermediates, delay/slew prediction, and downstream optimization impact. Status: `Verified-direct`.
- `[18]` Lines `47, 153`. Verified use: histogram-based SSTA through a modern optimization lens is correctly used as an example that classical statistical timing can be formulated in optimization terms. Status: `Verified-direct`.
- `[19]` Lines `19, 35, 87, 129, 183, 203`. Verified use: TSTL-GNN is correctly cited for ECO-induced distribution shift, transition-to-delay transfer structure, and ECO-aware closed-loop evaluation. Status: `Verified-direct`.
- `[20]` Lines `17, 27`. Verified use: the paper is correctly cited as a survey of ML-based STA in agile design. Status: `Verified-contextual`.
- `[21]` Lines `27, 109, 141, 169`. Verified use: GPU-accelerated PBA is correctly cited for runtime reduction of high-fidelity path analysis and cheaper fallback. Status: `Verified-direct`.
- `[22]` Lines `11, 27, 111, 141, 169, 183`. Verified use: heterogeneous CPU-GPU STA is correctly cited for acceleration of trusted timing-engine kernels, incremental updates, and multicorner propagation. Status: `Verified-direct`.
- `[23]` Lines `27, 35, 99, 137, 145, 173`. Verified use: aging-aware critical-path selection is correctly cited for aged criticality ranking and top-set accuracy rather than only scalar prediction. Status: `Verified-direct`.
- `[24]` Line `95`. Verified use: deep-learning cell-delay modeling is correctly cited as a waveform-aware primitive timing model beyond standard LUT abstractions. Status: `Verified-direct`.
- `[25]` Lines `73, 125, 161, 187`. Verified use: Random-Forest post-placement delay correction is correctly cited as a correlation-restoration layer between abstractions. Status: `Verified-direct`.
- `[26]` Lines `99, 173`. Verified use: AVATAR is correctly cited for aging- and variation-aware dynamic timing analysis and for the broader move toward runtime-aware timing robustness. Status: `Verified-direct`; the sentence about overlap with runtime adaptivity is `Review-synthesis`.
- `[27]` Lines `61, 137, 157`. Verified use: early RTL delay prediction is correctly cited for early risk ranking and architectural triage rather than final signoff replacement. Status: `Verified-direct`.
- `[28]` Lines `91, 115, 121, 145, 165`. Verified use: dominant-corner-based multicorner timing prediction is correctly cited for scenario reduction and timing-closure acceleration. Status: `Verified-direct`.
- `[29]` Lines `39, 63, 133, 157`. Verified use: preplacement net-length and timing estimation is correctly cited for explicit intermediate physical surrogates and preplacement WNS/TNS/slack prediction. Status: `Verified-direct`.
- `[30]` Line `103`. Verified use: neural timing analysis under PVT variation is correctly cited for learned mean and standard deviation estimation plus viability analysis. Status: `Verified-direct`.
- `[31]` Line `55`. Verified use: the near-threshold interdependent flip-flop timing model is correctly cited for setup-hold-clock-to-Q interaction in low-voltage timing analysis. Status: `Verified-direct`.
- `[32]` Line `51`. Verified use: copula-based gate-delay modeling is correctly cited for non-Gaussian dependence modeling in variation-aware timing. Status: `Verified-direct`.
- `[33]` Line `103`. Verified use: path-delay variation prediction by learning is correctly cited for multi-corner variation prediction and characterization reduction. Status: `Verified-direct`.
- `[34]` Line `103`. Verified use: NN-SSTA is correctly cited for learned approximation of statistical max and convolution operations in discrete SSTA. Status: `Verified-direct`.
- `[35]` Lines `51, 137`. Verified use: adjacency criticality is correctly cited for redefining gate importance in statistical timing-yield optimization and for ranking-oriented evaluation. Status: `Verified-direct`.
- `[36]` Line `51`. Verified use: the near-subthreshold analytical delay model is correctly cited for variation-aware delay modeling in low-voltage regimes. Status: `Verified-direct`.
- `[37]` Lines `43, 137, 153`. Verified use: extended STA is correctly cited for timing-error probability and the gap between graph-critical and operationally critical paths. Status: `Verified-direct`.
- `[38]` Lines `55, 173`. Verified use: time-varying SSTA for potential critical path selection is correctly cited for lifetime-varying path criticality and aging-aware closure. Status: `Verified-direct`.
- `[39]` Lines `17, 27`. Verified use: the reliability-oriented survey is correctly cited as background for timing under reliability and lifetime effects. Status: `Verified-contextual`.
- `[40]` Lines `43, 137, 153`. Verified use: viability-analysis-based critical-path identification is correctly cited for true-path reasoning under process variation. Status: `Verified-direct`.
- `[41]` Line `51`. Verified use: stochastic logical effort is correctly cited for lightweight variation-aware delay and timing-yield estimation. Status: `Verified-direct`.
- `[42]` Line `51`. Verified use: current-fluctuation-aware gate-delay modeling is correctly cited for wide-range PVT robustness within conventional STA-compatible modeling. Status: `Verified-direct`.
- `[43]` Lines `47, 153, 191`. Verified use: hierarchical statistical timing-model extraction is correctly cited for IP modularity, correlation reconstruction, and scalable hierarchy. Status: `Verified-direct`.
- `[44]` Lines `19, 27, 55, 173, 195`. Verified use: BTI variability impact on timing is correctly cited for lifetime drift and the physical basis of aging-aware timing. Status: `Verified-direct`; broader silicon-intent framing is `Review-synthesis`.
- `[45]` Lines `47, 153`. Verified use: delay-correlation-aware SSTA based on conditional moments is correctly cited for path-delay distributions and correlation-aware statistical timing. Status: `Verified-direct`.
- `[46]` Lines `25, 55, 145`. Verified use: interdependent timing constraints are correctly cited for robustness through setup-hold interaction and reduced delay uncertainty. Status: `Verified-direct`.
- `[47]` Lines `47, 153`. Verified use: smart Monte Carlo SSTA is correctly cited for simulation-grounded statistical timing acceleration. Status: `Verified-direct`.
- `[48]` Lines `25, 55, 145, 195`. Verified use: FA-STAC is correctly cited for coupling-aware STA, iterative dependence, and convergence acceleration. Status: `Verified-direct`.
- `[49]` Lines `17, 25, 47, 145, 195`. Verified use: the SSTA survey is correctly cited as the main statistical timing foundation for the review. Status: `Verified-contextual`.
- `[50]` Lines `25, 39, 153`. Verified use: slack semantics are correctly cited from Vygen’s paper and used as a methodological warning about label meaning in modern ML timing work. Status: `Verified-direct`.

## Overall Audit Conclusion

The integrated manuscript is using the right papers for the right major claims. The main body does not show evidence of citation hallucination in the sense of attaching a paper to an unrelated statement. The remaining distinction is between:

- direct paper-backed statements, which dominate the manuscript, and
- broader review conclusions, which are this paper’s synthesis across multiple sources.

That distinction is acceptable for a review paper as long as it stays explicit. In the current manuscript, the source-backed statements are sentence-level and the higher-level conclusions are generally signaled with phrases such as “collectively,” “this review argues,” or “the corpus suggests.”
