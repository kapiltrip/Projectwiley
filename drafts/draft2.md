# Machine Learning and GPU-Accelerated Static Timing Analysis for Intent-Robust Timing Closure

## Abstract

Static timing analysis (STA) remains the central correctness and signoff methodology for digital integrated circuits, yet modern timing closure is increasingly constrained by design scale, multi-corner and multi-mode scenario growth, expensive late-stage physical effects, and reliability phenomena such as aging, supply noise, and process variation. Recent research responds along two complementary axes. One axis accelerates trustworthy timing analysis through GPU and heterogeneous computing. The other axis uses machine learning (ML) to predict, correct, prioritize, or guide timing decisions earlier in the flow so that expensive tool iterations are reduced rather than merely accelerated. This review synthesizes fifty papers spanning ML-driven timing prediction, optimization guidance, signoff-aligned correction, library and waveform modeling, multicorner acceleration, statistical timing, aging-aware analysis, and GPU-accelerated STA and path-based analysis. We frame *intent-robust timing closure* as the ability of a timing methodology to preserve actionable accuracy and safety under changing design intent, changing operating intent, and changing silicon conditions. Using that lens, we identify recurring system patterns that appear most deployable in practice: learning decisions rather than replacing signoff, coupling prediction with explicit fallback logic, using multimodal and transfer-based representations to survive distribution shift, and pairing ML with accelerated timing engines so that high-fidelity analysis remains cheap enough to stay inside the closure loop.

Keywords: static timing analysis, timing closure, machine learning, graph neural networks, multicorner analysis, GPU acceleration, path-based analysis, statistical timing, aging, power supply noise, routing topology optimization

## Introduction

Timing closure is not a single analysis step. It is an iterative control loop that repeatedly invokes a timing engine, identifies violations, applies targeted modifications, and re-analyzes until constraints are met with acceptable margin. The multicorner acceleration framework in [16] makes the cost problem explicit by targeting repeated STA inside iterative physical design. The heterogeneous CPU-GPU engine in [22] makes the same point from the implementation side by accelerating the exact single-corner, multicorner, and incremental workloads that dominate practical turnaround time.

Inaccurate early timing estimates amplify that cost because they create unnecessary iterations and can bias optimization toward the wrong objectives. The placement-guidance framework in [1] is motivated by this problem at placement stage. The pre-route optimization framework in [17] shows the same issue at prerouting stage, where poor early timing guidance creates downstream P&R inefficiency. The post-placement correction study in [25] also demonstrates that even when timing is available, correlation gaps between abstractions can be large enough to justify learned correction.

Two trends stand out across the literature. The first is that hardware acceleration is becoming necessary rather than optional. GPU acceleration of path-based analysis in [21] shows that high-fidelity pessimism reduction can be made tractable at scales that would otherwise be too expensive. GPU acceleration of full STA in [22] shows that even the main graph-propagation engine can benefit substantially when the workload is mapped carefully.

The second trend is that ML is moving away from a simple "predict timing" mindset. The TimeBoost framework in [9] learns which timing analysis method to invoke, not the final delay directly. The Bayesian multicorner framework in [16] decides when a prediction is safe and when more STA should be run. The placement-guidance framework in [1] outputs candidate actions rather than only endpoint values. The field is therefore moving from regression alone toward decision support inside closure loops.

This review adopts *intent-robustness* as its organizing lens. A model may look accurate on a fixed snapshot and still fail under ECO churn, node migration, workload-sensitive aging, new corner definitions, or changed routing constraints. The ECO framework in [19] treats design modification as the primary problem rather than as noise. The cross-node predictor in [6] treats technology migration as a first-class transfer problem. The path-level aging predictor in [15] treats workload-sensitive degradation as part of the timing target itself. The PSN-aware STA engine in [12] similarly treats dynamic operating state as part of timing truth rather than an afterthought.

Recent survey literature already covers important parts of this space. The agile-design survey in [20] reviews ML-based STA across the RTL-to-GDSII pipeline. The broader SSTA survey in [49] remains foundational for uncertainty and variation handling. The reliability-oriented survey in [39] widens the timing discussion beyond process variation toward aging and lifetime effects. What is still missing is a synthesis that treats ML prediction, statistical timing, reliability-aware modeling, and GPU acceleration as parts of the same closure problem. That is the gap this review addresses.

## Foundations of STA and Timing Closure

STA operates on a timing graph, propagates arrival and required times, and derives slack as the central indicator of timing margin. Slack is not merely a bookkeeping artifact. Vygen shows that standard STA slack does not always preserve the intended interpretation of tolerable extra delay, and therefore develops a corrected slack definition with better optimization meaning [50]. That observation matters directly for modern ML papers because endpoint slack is the explicit target in the GAT-based prerouting model [5]. WNS and TNS are explicit targets in the preplacement predictor in [29]. Those same metrics are also used as optimization outcomes in [1], [17], and [25].

The standard industrial distinction between graph-based analysis and path-based analysis also remains essential. Graph-based STA is dominant because it is scalable, but it is conservative. Path-based analysis reduces pessimism at the cost of much higher runtime. The GPU PBA framework in [21] focuses precisely on that cost barrier. The paper is important not only as an acceleration result, but also as a reminder that accuracy and runtime are still traded against each other at the engine level.

Variation handling appears in two broad forms. Multi-corner STA is the dominant industrial strategy and motivates acceleration and prediction methods such as [16], [22], and [28]. SSTA treats timing as a distributional problem instead of a finite-corner problem. The survey in [49] covers the classical algorithmic space. The optimization-lens formulation in [18] shows that histogram-based SSTA can also be expressed as binary-integer programming or geometric programming. The conditional-moment path-based framework in [45] extends this line by handling delay correlation explicitly rather than treating it as a secondary concern.

Classical timing closure must also grapple with effects that are increasingly prominent in advanced nodes. The PSN-aware timing engine in [12] shows that static-supply assumptions can be overly conservative or inaccurate once dynamic noise becomes important. Aging-aware critical-path ranking in [23] shows that the identity of the critical path can change over lifetime. BTI-aware temporal statistical timing analysis in [44] makes the same point from a more physical angle by embedding aging variability and path correlation together.

Finally, robustness depends on the timing quantities that are modeled in the library itself. The interdependent-constraint paper in [46] shows that setup-hold interaction can be exploited to reduce delay uncertainty and improve robustness in synchronous circuits. The NVT-focused timing model in [31] carries that same idea into more recent flip-flop timing analysis and optimization. Current-fluctuation-based delay modeling in [42] and near-subthreshold analytical delay modeling in [36] similarly show that robust closure often begins with better primitive models rather than only better global propagation.

## Machine Learning Methods for Timing Prediction and Closure

### ML tasks mapped to the design flow

ML-assisted timing tasks differ sharply by design stage and by label fidelity. The RTL predictor in [27] estimates pin-to-pin delay and slew to support very early design decisions, where physical detail is still unavailable. The preplacement framework in [29] predicts net lengths first and then timing, reflecting the fact that timing is downstream of geometry even before legal placement exists. The pre-route optimization work in [17] predicts interconnect proxies and timing quantities before detailed routing. The ECO framework in [19] treats post-change timing as its own transfer-learning problem. The multicorner acceleration system in [16] focuses on repeated signoff-adjacent analysis rather than early estimation.

This mapping matters because distribution shift is stage-specific. RTL labels are further from signoff truth but structurally easier to generate [27]. Pre-route labels must bridge missing geometry and parasitics [17]. ECO labels are explicitly generated under design change [19]. Robust formulation therefore starts with choosing the right timing task, not only the right model architecture.

### Graph neural networks and topology-aware representations

Graph learning dominates the modern literature because circuit structure and timing dependence are inherently relational. The placement-guidance model in [1] uses graph learning to propose candidate gate sizing and buffer insertion actions and to identify path groups likely to violate timing. The pre-route framework in [17] combines GNN and CNN stages to infer net R, net C, arc length, and finally delay and slew. The ECO framework in [19] uses graph-based transfer learning so that timing predictions survive structural change after ECO edits.

Graph awareness does not always require end-to-end deep graph models. The placement-stage predictor in [2] uses complex-network features derived from timing paths and combines them with conventional placement-stage features. The result is still topology-aware, but through engineered structural descriptors rather than a fully learned message-passing model. That is a useful reminder that graph sensitivity can be encoded in multiple ways.

The graph-attention model in [5] is especially notable because it mimics timing propagation structure. Net propagation and cell propagation are alternated in a way that resembles a timing engine rather than a generic graph regressor. That architectural choice reflects a broader trend across the best-performing papers: ML tends to work better when it borrows causal structure from timing analysis instead of ignoring it.

### Tree-based ensembles and gradient-boosted models

Tree-based models remain highly competitive when feature engineering is strong and deployment demands robustness. The post-placement correction study in [25] uses Random Forest to reduce cell-delay error against a stronger reference estimator. The ensemble extension in [13] studies extra trees and gradient boosting and reports further accuracy gains on unseen industrial designs. These papers are valuable because they position ML as a correlation-restoration tool between abstractions rather than as a wholesale replacement of analysis.

The derivable gradient boosting model in [3] pushes tree-based learning in a more ambitious direction. Instead of using the predictor only as a reporting function, the paper reformulates it into a derivable timing model that can participate in placement optimization. This is a key step toward intent robustness, because the model is designed to survive integration into the closure loop instead of remaining a detached oracle.

TimeBoost in [9] is another important tree-based paper, but for a different reason. It does not predict timing values directly. It predicts which analysis method should be used for a given stage complexity. That is a safer and more deployable problem formulation because the ML system sits above trusted analysis methods rather than competing with them directly.

Primitive timing modeling also remains an active ML target. Deep-learning cell-delay modeling in [24] revisits the library-model problem directly by replacing or augmenting conventional LUT-style timing abstractions with learned waveform-aware models. That direction complements system-level timing prediction because it improves the building blocks used by the timing engine itself.

### Cross-node, cross-stage, and multimodal learning

Cross-domain robustness is increasingly central to timing prediction. The technology-node transfer framework in [6] addresses the data problem that appears when moving from older nodes to advanced nodes. Rather than assuming direct portability, it aligns path features across nodes and reweights source-node data based on cell-type distributions. PRO-TIME in [8] tackles a different form of shift by making prerouting prediction optimization-aware and multimodal. The predictor is trained to survive the timing optimization loop that changes the very features it consumes.

Timing consistency across stages is treated most directly in [10], where ML is used to improve consistency between global route and detailed route. That paper is important because it judges the value of the model by whether earlier optimization decisions improve later timing outcomes, not only by predictor fidelity on held-out labels. Taken together, [6], [8], and [10] show that robust timing learning requires explicit treatment of domain drift rather than hope that generic generalization will be enough.

## GPU-Accelerated Timing Analysis and Hybrid ML-GPU Systems

### GPU acceleration of STA primitives

GPU acceleration is compelling when timing workloads expose substantial parallelism. The heterogeneous engine in [22] accelerates levelization, delay computation, graph propagation, multicorner analysis, and incremental updates using GPU-oriented data structures and CPU-GPU concurrency. The reported speedups matter because they target exactly the high-frequency timing workloads that dominate practical closure.

The PBA framework in [21] attacks a different bottleneck. Path-based analysis is valuable because it reduces graph-based pessimism, but it is often too expensive to invoke repeatedly. By redesigning data structures and kernels around GPU execution, [21] shows that PBA can become much more practical at large scale. The main systems implication is not only speed; it is that higher-fidelity path reasoning can move earlier into the iterative closure loop.

### GPU-parallel ML components integrated into timing

GPU is also used to keep learned timing components cheap enough to deploy. The library interpolation work in [11] replaces bilinear interpolation with an ML-based interpolator and parallelizes the resulting arithmetic on GPU so that the inner-loop cost remains controlled. TimeBoost in [9] similarly relies on GPU-accelerated XGBoost so that method selection does not become its own bottleneck.

These examples show why ML and GPU acceleration are complementary rather than redundant. ML reduces how often expensive analysis must be run or decides where effort should be concentrated. GPU acceleration lowers the cost of the accurate analysis itself. Hybrid systems therefore attack both the frequency and the cost of high-fidelity timing calls.

## Intent-Robustness Under Variations, Aging, and ECO

### Reliability-aware timing under aging and BTI

Aging shifts timing truth over lifetime, which means nominal criticality can become misleading. Aging-aware critical-path selection in [23] reframes the problem as ranking under aged conditions rather than nominal path reporting. The heterogeneous-graph cell-timing model in [14] focuses on aging-aware primitive modeling inside the cell library. The multi-view graph framework in [15] lifts aging prediction to full path timing and treats workload-sensitive degradation as part of the target. BTI variability work in [44] grounds these timing shifts in a more physical modeling framework. Together, these papers show that robust closure must treat aging not as a final guardband, but as a changing timing landscape.

### Noise-aware STA and dynamic analysis

Dynamic power-supply noise is another source of intent shift because delay now depends on operating conditions not represented by nominal static corners. The PSN-aware STA engine in [12] integrates ML predictors into timing analysis using just-in-time compilation and noise-aware characterization. AVATAR in [26] broadens the scope further by combining aging, variation, and dynamic timing analysis for error-efficient computing. These papers are important because they move robust timing away from static worst-case margins and toward state-conditioned analysis.

### ECO as explicit intent drift

Timing ECO is the clearest example of design intent drift. The graph-based two-stage transfer-learning framework in [19] models transition first and delay second, matching the causal structure of timing computation. That formulation is more robust under design change than a single monolithic regressor because it transfers timing structure rather than only fitted coefficients.

### Variability and statistical timing as robustness frameworks

Many papers in the corpus treat robustness as a probabilistic question rather than a deterministic one. The timing-and-reliability survey in [39] explains why process variation, aging, and uncertainty cannot be reduced to a few scalar margins. The SSTA survey in [49] remains foundational for the corresponding algorithmic space. Timing-model extraction for hierarchical SSTA in [43] is important because realistic designs are rarely flat at signoff scale. Delay-correlation-aware SSTA in [45] addresses a major weakness in crude variation handling by estimating both cell and path correlations.

Other papers push on specific pieces of the same statistical problem. Copula-based gate-delay modeling in [32] addresses non-Gaussian dependence structures. NN-SSTA in [34] learns statistical max and convolution operations to reduce discrete SSTA cost. Smart Monte Carlo acceleration in [47] preserves simulation grounding while reducing runtime. Extended STA in [37] links deterministic timing analysis to timing-error probability. The time-varying critical-path framework in [38] and the viability-analysis method in [40] both show that path importance under uncertainty is richer than nominal longest-path ranking.

The variation-aware modeling literature also contributes directly to intent robustness. The neural timing-analysis algorithm in [30] learns mean and standard deviation of gate delay under PVT variation and combines that with viability analysis. The path-delay-variation framework in [33] learns delay variation directly for corner-sensitive prediction. The adjacency-criticality metric in [35] improves timing-yield optimization by redefining how gate importance is measured. Stochastic logical effort in [41] provides a yield-oriented delay abstraction. The near-subthreshold delay model in [36] addresses process variation in low-voltage regimes. The current-fluctuation delay model in [42] extends robust modeling across wide PVT ranges. The interdependent timing-constraint analysis in [46] shows that robustness can also be embedded in constraint modeling, not only in the timing engine.

## Experimental Methodology and Practical Deployment

Prediction-quality metrics dominate the ML literature, but they do not all mean the same thing for closure. The complex-network model in [2] reports improvements in MSE, R2, and critical-path classification. The path-level aging model in [15] reports MAPE. The ECO model in [19] reports R2 and MAE. These metrics are useful for model development, but they do not by themselves show that timing closure improved.

Closure-oriented metrics are more informative when the question is deployability. The placement-guidance framework in [1] reports WNS, TNS, and violating-path reductions. The pre-route optimization work in [17] reports timing improvements after integration into a P&R flow. The post-placement correction study in [25] uses timing accuracy improvements to justify fewer misleading optimization decisions. The best papers therefore tend to connect predictor quality to actual flow behavior rather than to isolated regression scores.

Label fidelity is another practical bottleneck. Library characterization remains expensive, which motivates transfer-learning approaches such as [4]. Early timing prediction suffers from missing geometry and parasitics, which motivates hierarchical proxy prediction in [17]. Cross-node transfer is needed because advanced-node labels are expensive to generate and often proprietary [6]. Any deployable ML timing system therefore depends as much on label strategy as on model choice.

The clearest route to signoff-safe deployment is hybridization. Bayesian decision logic in [16] allows predictions to be used only when confidence is high enough. Method selection in [9] preserves a trusted analysis back end. GPU acceleration in [22] reduces the cost of fallback to accurate analysis. GPU PBA in [21] reduces the cost of higher-fidelity pessimism reduction. These patterns are preferable to systems that silently replace timing analysis with an opaque predictor.

Several research directions follow directly from this synthesis. First, closure-in-the-loop evaluation is still too rare. Many papers report predictor accuracy, but fewer report iteration count, final QoR, or runtime under realistic ECO sequences. The integrated optimization papers in [1], [3], [7], [17], and [19] point in the right direction, but the field still lacks standardized benchmarking. Second, uncertainty calibration remains underdeveloped beyond examples such as [16] and [9]. Third, multi-physics timing remains fragmented across noise-aware work such as [12], aging-aware work such as [14] and [15], and coupling-aware work such as [48]. Finally, optimization-compatible surrogates remain a promising direction. The derivable timing model in [3] and the optimization-aware predictor in [8] suggest that the next generation of timing ML will be judged not only by how well it predicts, but by how safely it participates in optimization.

## References

[1] “A GNN-Based Placement Optimization Guidance Framework by Physical and Timing Prediction,” *Electronics*, 2025. doi: 10.3390/electronics14020329.  
[2] “Complex Network Based Machine Learning Method for Predicting Circuit Timing,” *Applied Soft Computing*, 2026. doi: 10.1016/j.asoc.2025.114100.  
[3] “Efficient Timing Prediction and Optimization Using Derivable Gradient Boosting Machine Model at Placement Stage,” *ACM Transactions on Design Automation of Electronic Systems*, 2025. doi: 10.1145/3780100.  
[4] “Knowledge Transferring Framework for Cell Library Characterization,” *Microelectronics Journal*, 2025. doi: 10.1016/j.mejo.2024.106542.  
[5] “Pre-Routing Slack Prediction Based on Graph Attention Network,” *Automation*, 2025. doi: 10.3390/automation6020020.  
[6] “Prerouting Timing Prediction Across Different Technology Nodes,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2025. doi: 10.1109/TCAD.2024.3523426.  
[7] “Sign-Off Timing Considerations via Concurrent Routing Topology Optimization,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2025. doi: 10.1109/TCAD.2024.3506216.  
[8] “PRO-TIME: Prerouting Optimization-Aware Timing Prediction via Multimodal Learning,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2025. doi: 10.1109/TCAD.2025.3569488.  
[9] “TimeBoost: Accelerating Timing Analysis Engines Using XGBoost,” *AEU - International Journal of Electronics and Communications*, 2025. doi: 10.1016/j.aeue.2025.155870.  
[10] “A Machine Learning Approach to Improving Timing Consistency between Global Route and Detailed Route,” *ACM Transactions on Design Automation of Electronic Systems*, 2024. doi: 10.1145/3626959.  
[11] “Accurate Interpolation of Library Timing Parameters Through Recurrent Convolutional Neural Network,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2024. doi: 10.1109/TCAD.2023.3316991.  
[12] “Dynamic Supply Noise Aware Timing Analysis With JIT Machine Learning Integration,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2024. doi: 10.1109/TCAD.2023.3342603.  
[13] “Enhancing Cell Delay Accuracy in Post-Placed Netlists Using Ensemble Tree-Based Algorithms,” *Integration, the VLSI Journal*, 2024. doi: 10.1016/j.vlsi.2024.102193.  
[14] “Fast and Accurate Aging-Aware Cell Timing Model via Graph Learning,” *IEEE Transactions on Circuits and Systems II: Express Briefs*, 2024. doi: 10.1109/TCSII.2023.3298917.  
[15] “Multi-View Graph Learning for Path-Level Aging-Aware Timing Prediction,” *Electronics*, 2024. doi: 10.3390/electronics13173479.  
[16] “Multicorner Timing Analysis Acceleration for Iterative Physical Design of ICs,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2024. doi: 10.1109/TCAD.2024.3361401.  
[17] “Pre-Route Timing Prediction and Optimization with Graph Neural Network Models,” *Integration, the VLSI Journal*, 2024. doi: 10.1016/j.vlsi.2024.102262.  
[18] “Statistical Static Timing Analysis via Modern Optimization Lens: I. Histogram-Based Approach,” *Optimization and Engineering*, 2024. doi: 10.1007/s11081-023-09847-3.  
[19] “TSTL-GNN: Graph-Based Two-Stage Transfer Learning for Timing Engineering Change Order Analysis Acceleration,” *Electronics*, 2024. doi: 10.3390/electronics13152897.  
[20] “A Survey on Machine Learning-Based Technology for Static Timing Analysis in Agile Design,” *Journal of Computer-Aided Design & Computer Graphics*, 2023. doi: 10.3724/SP.J.1089.2023.19557.  
[21] “A GPU-Accelerated Framework for Path-Based Timing Analysis,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2023. doi: 10.1109/TCAD.2023.3272274.  
[22] “Accelerating Static Timing Analysis Using CPU-GPU Heterogeneous Parallelism,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2023. doi: 10.1109/TCAD.2023.3286261.  
[23] “Aging-Aware Critical Path Selection via Graph Attention Networks,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2023. doi: 10.1109/TCAD.2023.3276944.  
[24] “Deep-Learning Cell-Delay Modeling for Static Timing Analysis,” *Ain Shams Engineering Journal*, 2023. doi: 10.1016/j.asej.2022.101828.  
[25] “Machine Learning Application for Cell Delay Accuracy Improvement at Post-Placement Stage: A Case Study for Combinational Cells,” *Integration, the VLSI Journal*, 2023. doi: 10.1016/j.vlsi.2023.02.011.  
[26] “AVATAR: An Aging- and Variation-Aware Dynamic Timing Analyzer for Error-Efficient Computing,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2023. doi: 10.1109/TCAD.2023.3255167.  
[27] “Early RTL Delay Prediction Using Neural Networks,” *Microprocessors and Microsystems*, 2022. doi: 10.1016/j.micpro.2022.104671.  
[28] “Machine-Learning-Based Multi-Corner Timing Prediction for Faster Timing Closure,” *Electronics*, 2022. doi: 10.3390/electronics11101571.  
[29] “Preplacement Net Length and Timing Estimation by Customized Graph Neural Network,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2022. doi: 10.1109/TCAD.2022.3149977.  
[30] “Timing Analysis Algorithm Using a Neural Network under PVT Variations,” *Microelectronics Journal*, 2022. doi: 10.1016/j.mejo.2022.105480.  
[31] “Timing Analysis and Optimization Method with Interdependent Flip-Flop Timing Model for NVT Circuits,” *Electronics*, 2022. doi: 10.3390/electronics11223670.  
[32] “Statistical Gate-Delay Modeling with Copulas,” *Microelectronics Journal*, 2021. doi: 10.1016/j.mejo.2020.104938.  
[33] “Novel Prediction Framework for Path Delay Variation Based on Learning Method,” *Electronics*, 2020. doi: 10.3390/electronics9010157.  
[34] “NN-SSTA: A Deep Neural Network Approach for Statistical Static Timing Analysis,” *Expert Systems with Applications*, 2020. doi: 10.1016/j.eswa.2020.113309.  
[35] “Adjacency Criticality: A Simple Yet Effective Metric for Statistical Timing Yield Optimisation of Digital Integrated Circuits,” *IET Circuits, Devices & Systems*, 2019. doi: 10.1049/iet-cds.2018.5616.  
[36] “An Analytical Gate Delay Model in Near-Subthreshold Domain Considering Process Variation,” *IEEE Access*, 2019. doi: 10.1109/ACCESS.2019.2955091.  
[37] “Calculated Risks: Quantifying Timing Error Probability With Extended Static Timing Analysis,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2019. doi: 10.1109/TCAD.2018.2821563.  
[38] “Potential Critical Path Selection Based on a Time-Varying Statistical Timing Analysis Framework,” *IEEE Transactions on Very Large Scale Integration (VLSI) Systems*, 2019. doi: 10.1109/TVLSI.2019.2893020.  
[39] “From Process Variations to Reliability: A Survey of Timing of Digital Circuits in the Nanometer Era,” *IPSJ Transactions on System LSI Design Methodology*, 2018. doi: 10.2197/ipsjtsldm.11.2.  
[40] “Efficient Critical Path Identification Based on Viability Analysis Method Considering Process Variations,” *IEEE Transactions on Very Large Scale Integration (VLSI) Systems*, 2017. doi: 10.1109/TVLSI.2017.2703623.  
[41] “Stochastic Logical Effort as a Variation Aware Delay Model to Estimate Timing Yield,” *Integration, the VLSI Journal*, 2015. doi: 10.1016/j.vlsi.2014.07.003.  
[42] “A Gate-Delay Model Focusing on Current Fluctuation over Wide Range of Process-Voltage-Temperature Variations,” *Integration, the VLSI Journal*, 2013. doi: 10.1016/j.vlsi.2013.01.003.  
[43] “On Timing Model Extraction and Hierarchical Statistical Timing Analysis,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2013. doi: 10.1109/TCAD.2012.2228305.  
[44] “The Impact of BTI Variations on Timing in Digital Logic Circuits,” *IEEE Transactions on Device and Materials Reliability*, 2013. doi: 10.1109/TDMR.2013.2237910.  
[45] “Delay-Correlation-Aware SSTA Based on Conditional Linear Regression,” *Microelectronics Journal*, 2012. doi: 10.1016/j.mejo.2012.01.003.  
[46] “Utilizing Interdependent Timing Constraints to Enhance Robustness in Synchronous Circuits,” *Microelectronics Journal*, 2012. doi: 10.1016/j.mejo.2011.11.005.  
[47] “Fast Statistical Static Timing Analysis Using Smart Monte Carlo Techniques,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2011. doi: 10.1109/TCAD.2011.2108030.  
[48] “FA-STAC: An Algorithmic Framework for Fast and Accurate Coupling Aware Static Timing Analysis,” *IEEE Transactions on Very Large Scale Integration (VLSI) Systems*, 2011. doi: 10.1109/TVLSI.2009.2035323.  
[49] “Statistical Static Timing Analysis: A Survey,” *Integration, the VLSI Journal*, 2009. doi: 10.1016/j.vlsi.2008.10.002.  
[50] “Slack in Static Timing Analysis,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2006. doi: 10.1109/TCAD.2005.858348.
