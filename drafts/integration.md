# Integration: Machine Learning and GPU-Accelerated Static Timing Analysis for Intent-Robust Timing Closure

## Abstract

Static timing analysis (STA) remains the dominant formal method for timing verification and signoff, but timing closure in advanced digital design is now constrained by several interacting problems: inaccurate early-stage timing estimates, exploding multi-corner and multi-mode scenario counts, costly path-based and incremental signoff analysis, and reliability effects such as aging, dynamic supply noise, and process variation that reshape criticality over time. Recent research responds along two complementary directions. One direction uses machine learning (ML) to predict, correct, rank, or guide timing outcomes earlier in the flow so that expensive iterations are avoided. The other direction accelerates trustworthy analysis through GPU and heterogeneous computing so that high-fidelity timing engines remain usable inside optimization loops. This review integrates fifty papers spanning classical STA semantics, statistical timing, aging- and noise-aware modeling, ML-based timing prediction and optimization, multicorner decision layers, and GPU-accelerated STA and path-based analysis. We use *intent-robust timing closure* as the central lens: a timing methodology is intent-robust if it preserves actionable accuracy and safety under changing design intent, changing operating intent, and changing silicon conditions. Under that lens, the papers that hold up in deployment do not replace signoff outright. They learn correlation bridges between stages, learn decisions rather than final truth, preserve physical structure in their representations, and pair prediction with explicit fallback or acceleration mechanisms. Based on the corpus, this paper contributes three things beyond a conventional survey: a unified taxonomy that connects ML, SSTA, reliability-aware timing, and acceleration; a synthesis of deployment behaviors that survive ECO churn, corner growth, and node migration; and an integrated closure blueprint in which learned models triage and shape optimization while GPU-backed engines preserve signoff trustworthiness. The resulting picture is not “ML versus STA.” It is a layered architecture in which ML ranks risky logic, selects methods or corners, and proposes optimization moves; statistical and physical timing models define whether slack, criticality, and yield claims are meaningful; and acceleration keeps trusted feedback available at the cadence required by modern closure loops.

Keywords: static timing analysis, timing closure, machine learning, graph neural networks, multicorner analysis, GPU acceleration, path-based analysis, statistical timing analysis, aging-aware timing, dynamic supply noise

## 1. Introduction

Timing closure is no longer a narrow signoff task performed at the end of implementation. It is an iterative control loop that repeatedly estimates timing, optimizes the design, and validates the result under increasingly accurate physical assumptions. The multicorner acceleration work in [16] is explicit about this loop: timing analysis is repeatedly invoked inside iterative physical design, and the runtime bottleneck is no longer a single final run but the cost of many timing evaluations under many scenarios. The heterogeneous CPU-GPU STA engine in [22] makes the same point from the systems side by accelerating levelization, delay computation, propagation, incremental updates, and multicorner analysis because those are precisely the high-frequency workloads designers already pay for in real flows.

The cost of that loop is amplified when early timing surrogates are poorly aligned with post-route signoff. The placement-guidance framework in [1] is motivated by the fact that placement decisions strongly shape later routing and timing outcomes. The pre-route optimization framework in [17] shows that better delay and slew prediction can materially reduce unnecessary place-and-route iteration. The GR-to-DR correction framework in [10] goes further and demonstrates that stage mismatch itself is a first-order problem: optimization based on inaccurate post-global-route timing can steer the flow away from the detailed-route outcome that determines signoff.

This pressure has created two active research fronts. The first front uses ML to predict timing, identify criticality, select methods, guide placement or routing changes, or reduce characterization and corner costs. The second front accelerates the timing engines that designers already trust, especially multicorner STA and path-based analysis (PBA), through GPU and heterogeneous parallelism. The first front changes *what* gets evaluated or optimized. The second front changes *how fast* trustworthy evaluation can be delivered. Treating them separately misses their combined value.

Several recent works survey only one slice of this landscape at a time. The survey in [20] catalogs ML uses across agile-design timing tasks such as prediction and acceleration. The survey in [49] organizes SSTA around block-based versus path-based propagation, variation sources, and correlation handling. The review in [39] extends timing discussion from manufacturing variation to reliability mechanisms such as aging and adaptive countermeasures. Yet none of these surveys treats ML prediction, statistical timing, reliability-aware modeling, and accelerated timing engines as parts of the same closure problem. The missing piece is composition: current deployment decisions are about how to combine these techniques without losing signoff trustworthiness.

This paper uses *intent-robust timing closure* as its organizing idea. A timing methodology is intent-robust if it continues to produce correct optimization, screening, or verification decisions when the intent of the flow shifts. Design intent shifts when placement optimization resizes gates or inserts buffers [1], when routing topology is modified to improve signoff [7], or when ECO edits restructure timing paths [19]. Operating intent shifts when the relevant corner set changes or when only a subset of scenarios can be afforded in each iteration [16]. Silicon intent shifts when aging, BTI, dynamic supply noise, or process variability alter which paths dominate and how delay should be interpreted [12], [15], [44]. A robust method therefore must survive distribution shift by construction, not by luck.

The rest of this review is structured around that claim. Section 2 defines the review scope and clarifies what this paper adds beyond existing surveys. Section 3 revisits the classical timing foundations that current ML and GPU work still inherit, including slack semantics, statistical timing, coupling, and true-path reasoning. Section 4 synthesizes ML work across the RTL-to-GDSII stack. Section 5 examines GPU and heterogeneous acceleration of trusted timing engines and inner-loop primitives. Section 6 distills the deployment patterns that most consistently improve robustness. Section 7 proposes an integrated closure blueprint that blends the strongest ideas from the fifty-paper corpus. Section 8 discusses evaluation, deployment, and research gaps. Section 9 concludes.

## 2. Review Scope and Contribution

### 2.1 Review type, corpus, and classification protocol

This paper should be read as a structured fixed-corpus review with an architectural synthesis, not as an open-ended bibliometric survey. The evidence base is the local fifty-paper corpus assembled for this project and processed into searchable text and HTML. The corpus spans 2006 through 2026 and intentionally mixes recent ML papers with older timing-analysis papers that still define the labels and failure modes used by newer work. That choice is necessary because modern learning papers often optimize quantities whose meaning was formalized much earlier. Slack semantics in [50] still shape how WNS, TNS, and endpoint slack should be interpreted. The SSTA survey in [49] still defines the main algorithmic language for timing under uncertainty. The coupling-aware framework in [48] and the interdependent-constraint work in [46] remain relevant because they expose modeling assumptions that many newer predictors still inherit.

Inclusion was driven by technical relevance to timing analysis or timing closure rather than by ML popularity alone. A paper was kept in the review if timing analysis, timing prediction, timing optimization, timing-criticality interpretation, or timing-engine acceleration was a primary contribution, and if it clearly touched at least one of the review axes: early-stage prediction, stage-alignment correction, statistical timing, multicorner reasoning, reliability-aware timing, or GPU/heterogeneous acceleration. Papers where timing appeared only as a minor downstream metric were not used as primary evidence. Each included paper was then classified along five dimensions: design-flow stage, predicted or accelerated object, trust mechanism, robustness axis, and evaluation mode. That classification is what supports the synthesis in Sections 4 through 8.

### 2.2 What this review adds beyond prior surveys

The review also extends beyond narrowly “ML for STA” papers. Survey [20] catalogs agile-flow ML uses, but it does not address whether those predictors can coexist with fast fallback to trusted analysis. That is why the GPU PBA framework in [21] and the heterogeneous STA engine in [22] are central here: [21] lowers the cost of pessimism reduction, and [22] lowers the cost of multicorner and incremental signoff workloads. Likewise, the reliability survey in [39] is included not as background alone but because it reframes timing from a process-variation problem into a reliability problem that includes aging and adaptation. Under that framing, aging-aware cell timing [14], path-level aging prediction [15], aging-aware critical-path ranking [23], BTI-aware temporal timing [44], and dynamic-noise-aware STA [12] become part of the timing core rather than side topics.

Table 1 makes the novelty claim explicit by comparing this manuscript to the three most relevant surveys in the corpus.

| Review | Primary scope | ML timing prediction | SSTA and timing semantics | Aging/noise/reliability | GPU or engine acceleration | Integrated closure blueprint |
| --- | --- | --- | --- | --- | --- | --- |
| [20] | ML-based STA in agile design | Yes | Limited | Limited | No | No |
| [49] | SSTA survey | No | Yes | No | No | No |
| [39] | Timing from process variation to reliability | Limited | Moderate | Yes | No | No |
| This paper | Timing closure under intent drift | Yes | Yes | Yes | Yes | Yes |

### 2.3 Operational definition of intent-robustness

The term *intent-robust timing closure* is only useful if it can be applied consistently. In this review, a method is treated as more intent-robust when it satisfies more of the criteria in Table 2 under realistic closure conditions. The point is not to collapse all methods into one score. The point is to prevent “robustness” from meaning only low held-out error on one frozen design snapshot.

| Axis | Question used in this review | Typical evidence in the literature |
| --- | --- | --- |
| Label semantics | Does the target preserve the timing meaning designers actually optimize? | Slack semantics [50], true-path reasoning [37], [40] |
| Stage robustness | Does the method stay useful as the flow moves from early estimates to routed signoff? | GR-to-DR correction [10], optimization-aware preroute prediction [8] |
| Transformation robustness | Does the method survive ECOs, sizing, buffering, or topology change? | Placement actions [1], ECO transfer learning [19], derivable placement model [3] |
| Scenario robustness | Does the method cope with corner growth and method-choice uncertainty? | Bayesian multicorner fallback [16], dominant-corner selection [28], TimeBoost [9] |
| Lifetime robustness | Does the method account for aging, BTI, or dynamic-noise perturbation? | Aging-aware timing [14], [15], [23]; PSN-aware STA [12]; BTI-aware timing [44] |
| Trust mechanism | Is there an explicit signoff anchor, fallback path, or physics-preserving intermediate? | Post-placement correction [25], [13]; GPU fallback [21], [22]; intermediate surrogates [17], [29] |
| Iteration viability | Can the method run at the cadence required by closure loops? | GPU STA/PBA [21], [22]; reduced characterization cost [4]; faster corner execution [16], [28] |

### 2.4 Contribution stance and citation method

Against that background, this paper makes three specific contributions beyond the existing drafts and beyond prior surveys. First, it builds a single taxonomy that connects ML predictors, SSTA methods, reliability-aware timing, and engine acceleration under the same closure objective. Second, it extracts deployment rules that are more operational than a list of model architectures: learn decisions instead of raw truth, model the transformation that breaks correlation, preserve a signoff anchor, and accelerate fallback rather than pretending fallback is unnecessary. Third, it proposes an *integration* blueprint for conference-style presentation: a layered architecture that explains how to combine early-stage prediction, stage-alignment correction, uncertainty-aware gating, and accelerated high-fidelity analysis in one timing-closure workflow.

Throughout the review, each numbered citation is used in one of two ways. In sentence-level factual statements, the citation points to a specific method, result, or framing in the cited paper. In broader conclusions, the manuscript makes the synthesis explicit and treats the conclusion as the review’s interpretation across several sources rather than as a claim made by any single paper. This distinction is necessary in a review paper because it separates paper-backed facts from review-level integration.

## 3. What Makes Timing Closure Hard in Advanced Nodes

### 3.1 Timing closure is a moving-target optimization problem

Timing closure is difficult not because arrival-time propagation is conceptually mysterious, but because the target keeps moving while the flow is optimizing toward it. The netlist changes during sizing and buffering [1]. The routing topology changes when timing-driven routing is refined [7]. The same design is evaluated under many corners, modes, and constraint settings [16]. ECO iterations change path structure late in the flow [19]. Aging changes which paths remain critical over lifetime [23]. Dynamic supply noise changes delay under real operating conditions [12]. In other words, closure is not a single prediction task. It is a sequence of related but drifting timing tasks.

### 3.2 Slack is indispensable, but its semantics are subtle

Slack remains the summary quantity that guides most optimization loops, yet its interpretation is less trivial than many ML papers assume. Vygen shows in [50] that positive slack in the standard STA model does not necessarily imply that the circuit can tolerate an equal additional delay at the same point. That is more than a theoretical objection. If a model is trained to predict slack, or an optimizer is trained to improve WNS and TNS, the underlying semantics of the label matter. The pre-routing slack predictor in [5] learns endpoint slack directly. The preplacement framework in [29] uses slack, WNS, and TNS as core evaluation targets. The placement-guidance method in [1] and the pre-route optimization framework in [17] both report WNS and TNS improvement as closure metrics. Those reported gains are meaningful only if the slack label still carries the decision semantics designers intend to optimize.

### 3.3 Graph-critical paths are not always the true operationally critical paths

Classical STA identifies graph-critical paths under worst-case assumptions, but operational criticality depends on sensitization and probability as well as topological delay. Extended STA in [37] makes this point directly by quantifying timing-error probability over input combinations and reducing pessimism relative to standard STA while remaining far faster than Monte Carlo timing simulation. Viability-analysis-based true-path identification in [40] reaches a similar conclusion from a different angle: the statistically longest true paths can be found more efficiently than exhaustive search, and they are not always the same as the nominal longest graph paths. These papers affect learning-based timing directly because training labels built from ordinary graph-criticality assumptions can encode the wrong notion of risk.

### 3.4 Statistical timing remains the deeper robustness framework

Multi-corner STA dominates practice because it is operationally simple, but the deeper uncertainty problem is statistical. The survey in [49] defines the main SSTA split between block-based and path-based analysis and explains why delay correlation is central rather than optional. Bosak in [18] recasts histogram-based SSTA as binary-integer and geometric programming, which makes the timing engine look less like a fixed heuristic and more like an optimization problem. Li et al. in [43] address hierarchical SSTA directly by extracting compact IP timing models and then reconstructing intermodule correlation during full-chip analysis. Wu et al. in [45] estimate path-delay distributions and cell-to-cell and path-to-path correlations by propagating conditional moments conditioned on input slope and output load. Veetil et al. in [47] stay closer to simulation by accelerating Monte Carlo itself with smart sampling, which keeps statistical timing grounded in sampled behavior while reducing runtime.

### 3.5 Robust timing depends on the quality of primitive models

Timing closure is also limited by how well the underlying delay primitives capture physics. Copula-based gate-delay modeling in [32] addresses non-Gaussian dependence structures that Gaussian approximations miss. Adjacency criticality in [35] improves statistical timing-yield optimization by redefining gate importance to include fan-out-cone effects rather than only local criticality. Stochastic logical effort in [41] provides a lightweight variation-aware delay abstraction and combines effectively with smart Monte Carlo yield estimation. The current-fluctuation delay model in [42] translates wide PVT variation into modified output load and reshaped input waveform so that conventional models can still be used accurately. The near-subthreshold analytical model in [36] addresses a regime where process randomness is amplified by voltage scaling and where conventional assumptions become especially fragile.

### 3.6 Coupling, constraint interaction, and aging all alter timing meaning

Several papers remind us that robust timing is not only about variation. FA-STAC in [48] treats crosstalk delay as an iterative coupling problem and accelerates convergence with heuristic and current-source-based models plus scheduling and partitioning. Salman in [46] studies interdependent setup-hold constraints and shows that using the interaction directly reduces delay uncertainty instead of leaving that margin hidden inside conservative guardbands. Cao et al. in [31] extend the same idea to near-threshold flip-flops, where setup, hold, and clock-to-Q dependence becomes more nonlinear and the usable timing region changes more sharply with voltage. Chithira and Vasudevan in [38] show that aging-aware global criticality peaks at t = 0 or at discrete breakpoint times, which means a time-varying analysis can avoid evaluating every instant. Wang et al. in [44] add BTI variability and path correlation to temporal statistical timing, so aging is treated as a correlated stochastic timing problem rather than as a fixed derate.

## 4. Machine Learning Across the RTL-to-GDSII Flow

### 4.1 Early-stage timing prediction: it must preserve ranking, not claim signoff

The earliest ML timing papers in the corpus are careful about scope. The RTL framework in [27] predicts pin-to-pin delay and slew for combinational RTL blocks and reports an 8.4x runtime improvement over running the full downstream flow. Its contribution is early ranking of risky logic regions before synthesis, placement, and routing make the correction cost high. It does not attempt to replace physical timing; it screens where later implementation effort should be spent.

Preplacement estimation is harder because geometry has not yet emerged from placement. The customized GNN approach in [29] addresses this by inserting a predicted net-length surrogate between topology and timing. Instead of mapping netlist structure directly to slack with no explicit physical bridge, the model predicts net lengths first and then derives timing estimates from them. The paper reports a fast variant that is over 1000x faster than placement and lower MAE for slack, WNS, and TNS than commercial preplacement timing reports. The methodological lesson is concrete: early-stage ML is more stable when it reconstructs at least one missing physical variable instead of pretending the variable does not matter.

### 4.2 Placement-stage prediction must change the next physical move

Placement is where ML starts to interact directly with optimization. The GNN-based framework in [1] does not only predict timing. It predicts candidate gate-sizing and buffer-insertion solutions and identifies path groups likely to violate timing. In reported experiments it improves WNS, TNS, and the number of violating paths while also slightly reducing wirelength. The point of the paper is procedural: the model output is already phrased as the next optimization move.

The placement-stage model in [3] goes a step further by making the predictor derivable. Instead of using gradient boosting as a black-box regressor, the paper converts it into a function that can provide optimization guidance inside iterative placement. The complex-network approach in [2] attacks the same stage from a different angle. It augments standard placement features with timing-path topology descriptors and reports lower MSE for slack and delay, smaller WNS and TNS deviation, and better AUC for critical-path identification. Read together with [1], these papers make two separate requirements visible: the representation must encode signal-propagation structure, and the output must be usable by the optimizer rather than only by an offline evaluator.

### 4.3 Post-placement correction is a conservative deployment approach with direct closure payoff

A large share of the ML work that transfers cleanly into deployment does not attempt to replace physics or signoff. It restores correlation between abstractions. The Random-Forest study in [25] raises average cell-delay accuracy to about 91.25% and reduces RMSE from 16.958 to 4.469 by learning the gap between a post-placement estimator and a higher-fidelity reference. The ensemble-tree extension in [13] extends that idea to Extremely Randomized Trees and Gradient Boosting on enriched 16 nm industrial data, reporting 92.01% average accuracy and 84.26% on unseen data. In both papers, ML is not the final judge of timing; it is a correction layer that moves a cheap stage closer to a higher-fidelity one.

### 4.4 Pre-route prediction works best when it models missing physics explicitly

Pre-route prediction is attractive because routing dominates closure cost, but it is also where naive ML is most exposed. The GAT-based slack predictor in [5] follows the timing graph with alternating attention and propagation layers, so its structure mirrors net and cell updates rather than treating the design as a generic graph. The hierarchical GNN+CNN framework in [17] is even more explicit about what is missing before routing. Its level-1 models predict net resistance, net capacitance, and arc-length increment; its level-2 models then use those outputs to predict arc delay and arc slew. In the reported flow, that structure improves arc delay and slew accuracy by 42% and 36% on average and improves WNS, TNS, and violation count by 77%, 77%, and 64%. The concrete lesson is that pre-route ML becomes more stable when it reconstructs the absent physical quantities instead of trying to jump directly to post-route timing.

### 4.5 Stage mismatch is a first-class problem, not a small residual error

Several of the best recent papers focus on stage mismatch directly. PRO-TIME in [8] argues that many prerouting predictors are mis-specified because they are trained on flows that omit timing optimization, even though timing optimization is precisely what reshapes the netlist and the endpoint features that matter in practice. Its multimodal architecture combines a customized GNN for the netlist with a U-net-based layout encoder and an adaptive masking strategy. That is not architectural ornamentation. It is a response to feature mismatch caused by the flow itself.

The GR-to-DR correction paper in [10] addresses a related but more deployment-oriented mismatch: post-global-route wire parasitics derived from route guides and Steiner trees can deviate substantially from post-detailed-route truth, especially in macro-heavy designs. The paper learns corrected post-DR parasitics and timing from post-GR features, adds macro-blockage features, and shows that the corrected estimates improve post-DR slack without increasing congestion. The signoff-oriented routing-topology framework in [7] closes the same gap from the optimization side. It uses a learned signoff evaluator to guide Steiner-point adjustment and topology reconstruction, reporting 11.2% WNS improvement, 7.1% TNS improvement, and 25.9% shorter optimization duration in its joint flow. In both cases, the model is only meaningful because it changes the routed signoff result rather than merely fitting a held-out label.

### 4.6 Transfer learning is central because timing knowledge is partly reusable and partly domain-specific

Timing prediction is expensive largely because labels are expensive. Transfer learning addresses that problem in several places in the corpus. The cell-library characterization framework in [4] transfers knowledge across timing arcs by quantifying task similarity and reports error reductions of up to 80% in 45 nm MOSFET libraries and 67% in 14 nm FinFET libraries. The cross-node timing predictor in [6] transfers from older-node data to 7 nm by disentangling path features and reweighting source data using cell-type distributions, rather than assuming naive fine-tuning will work. The ECO framework in [19] applies transfer inside one evolving design: it predicts transition time first, then delay, reuses the first-stage representation, reports average R2 around 0.9952 with MAE around 13.36, and cuts path-delay evaluation time by up to 80x. These are different transfer problems, but each one identifies a concrete piece of timing structure that survives the domain shift.

### 4.7 Safe ML integration is often about selecting what to run, not predicting everything

Some of the most convincing deployment papers avoid direct timing prediction as the end goal. The multicorner framework in [16] combines latent-feature modeling with a Bayesian decision layer that requests extra STA when prediction confidence is too low; that is how it pushes toward near-100% reliable prediction rather than just lower average error. The dominant-corner strategy in [28] attacks the scenario-selection problem directly and reports more than 2x timing-closure acceleration by predicting non-dominant corners from a small dominant set. TimeBoost in [9] moves the learning target one level higher again: it classifies stage complexity and selects among existing timing-analysis methods, reaching up to 3.86x runtime improvement with only 3%-4% overhead. These papers all learn when and where timing effort should be spent.

### 4.8 Primitive timing models are now an active ML frontier

ML is also being applied below the graph level. Deep-learning cell-delay modeling in [24] revisits the conventional NLDM abstraction and shows that waveform-aware learned models can beat a standard 7x7 NLDM-LUT in average percentage error while also improving maximum error relative to a much larger 100x100 LUT. The interpolation framework in [11] attacks a narrower but pervasive bottleneck: it uses an R-CNN plus VAE to interpolate timing tables, cuts timing-parameter error by 19.7%, reduces path-delay error by 3.4%, and limits runtime cost to a reported 13% overhead through GPU parallelism. The PSN-aware timing engine in [12] trains MLP models on noise-aware arc data and integrates them through JIT compilation; its reported average relative error is 4.89% for single-cell timing and 6.27% for path delay. These papers focus on primitive timing kernels rather than full-chip prediction.

### 4.9 ML is increasingly reliability-aware rather than nominal-only

Aging-aware cell timing via heterogeneous graph attention in [14] improves primitive timing modeling under degradation by embedding multi-typed devices and arc structure inside the cell model. Path-level aging prediction in [15] combines a spatial-temporal transformer with graph attention so that both topology and workload history shape the predicted degradation; the paper reports an average MAPE of 3.96%. Aging-aware critical-path selection in [23] focuses on ranking and reports top-10%, top-5%, and top-1% path-set accuracies of 99.52%, 98.69%, and 97.20% on industrial designs. AVATAR in [26] goes beyond static signoff and combines aging, variation, and dynamic timing analysis for better-than-worst-case operation. These papers are solving different lifetime problems at different levels of the timing stack.

### 4.10 Learning inside statistical timing targets the expensive operators directly

Several papers embed ML into timing uncertainty itself rather than only into nominal delay prediction. The neural timing-analysis algorithm in [30] learns the mean and standard deviation of gate delay under PVT variation, keeps mean error below 2% and standard-deviation error below 3.64% relative to SPICE Monte Carlo, and combines that with viability analysis for true-path reasoning. The path-delay-variation framework in [33] learns cross-corner variation directly to reduce characterization effort for multi-corner prediction. NN-SSTA in [34] does not predict path delay at all; it approximates the statistical max and convolution operators inside discrete SSTA and reports about 20.7x average speedup over the conventional discrete flow. The common thread is precise: ML is being used to approximate the expensive operators of statistical timing, not only the final labels.

## 5. GPU-Accelerated Timing Analysis and Hybrid ML-GPU Systems

### 5.1 GPU acceleration keeps trusted timing inside the loop

The rise of ML in timing does not reduce the need for acceleration. It raises the premium on being able to call trusted reference analysis more often. The GPU PBA framework in [21] addresses the most expensive exact-analysis step by redesigning data structures, preprocessing, and kernels for GPU execution. Because PBA reduces graph-based pessimism but is often too expensive to call repeatedly, the reported speedups on million-gate designs change how frequently pessimism reduction can participate in closure rather than being reserved for the very end.

The CPU-GPU heterogeneous STA engine in [22] covers more of the engine workload. It accelerates levelization, delay computation, graph propagation, incremental updates, and multicorner analysis, all while preserving a realistic execution model with CPU-GPU concurrency and managed dependencies. Its multicorner acceleration is not an incidental benchmark result; it directly targets the scenario explosion that dominates timing-closure runtime in modern flows.

### 5.2 GPU and ML solve different bottlenecks and therefore combine naturally

GPU acceleration and ML should not be seen as two alternative answers to the same question. TimeBoost in [9] trims analysis cost by choosing among timing methods from stage-complexity features. The interpolation framework in [11] trims the overhead of a better timing primitive by parallelizing large batches of table queries. The multicorner system in [16] trims wasted STA runs by gating predictions with a Bayesian decision layer. The dominant-corner system in [28] trims the scenario set by selecting a small corner subset to execute directly. The split is concrete: ML reduces how much exact analysis is needed, and GPU acceleration reduces the cost of the exact analysis that still remains.

## 6. Design Patterns for Intent-Robust Timing Closure

This section extracts reusable design rules from the corpus. Section 7 then composes those rules into one staged closure workflow. The separation is intentional: Section 6 answers *what repeatedly works*, while Section 7 answers *how those pieces can be assembled in one loop*.

### 6.1 Learn decisions, not just delays

The first recurring design rule is that ML systems transfer better into flows when they learn *which action or method should be taken* instead of predicting final timing unconditionally. TimeBoost in [9] learns the timing-method choice from stage complexity. The Bayesian multicorner framework in [16] learns whether a prediction should be accepted or whether another STA run should be triggered. The dominant-corner approach in [28] learns which scenarios should be executed and which can be inferred. The placement-guidance framework in [1] learns candidate sizing and buffering moves. These are bounded action spaces, which is one reason they are easier to trust than unconstrained end-to-end delay regressors.

### 6.2 Preserve a signoff anchor

The second design rule is that ML performs better in deployment when it is tied to a higher-fidelity reference analysis rather than treated as a replacement. Post-placement correction in [25] and [13] learns toward higher-fidelity cell-delay references. GR-to-DR correction in [10] learns detailed-route parasitics and timing from cheaper global-route features. The routing-topology framework in [7] still optimizes against final signoff WNS and TNS instead of a free-standing proxy objective. The PSN-aware engine in [12] preserves the outer STA structure and replaces only the arc-delay primitive with JIT-integrated learned models. In each case, the trusted timing notion remains visible.

### 6.3 Model the transformation that breaks correlation

Predictors fail in closure not only because the mapping is hard, but because the input distribution changes during the very optimization loop they are supposed to help. PRO-TIME models optimization-induced feature mismatch explicitly [8]. TSTL-GNN is designed for ECO-induced topology change [19]. The placement-guidance framework in [1] produces actions in a regime where gate sizing and buffering are themselves changing topology. The derivable timing model in [3] is designed to live inside iterative placement rather than outside it. This suggests a concrete rule for future work: if the flow itself changes the feature space, robustness requires modeling that transformation explicitly.

### 6.4 Use intermediate physical quantities as stabilizers

Another consistent design rule is that models become more robust when they predict physically meaningful intermediates. The preplacement model in [29] predicts net length before timing because topology alone does not encode wire geometry. The pre-route flow in [17] predicts net R, net C, and arc-length increment before arc delay and slew. The transfer framework in [4] uses similarity among timing arcs as the reusable intermediate structure rather than treating every arc as a separate task. The PSN-aware engine in [12] parameterizes noise by quantities such as amplitude, duration, and shape before regressing arc timing. These intermediate quantities make the learning problem less brittle because they are closer to how delay is physically formed.

### 6.5 Optimize for ranking and critical-set capture, not only regression error

Timing closure is usually a prioritization problem before it is a scalar-regression problem. Aging-aware path selection in [23] uses top-set accuracy because designers care whether the right paths are surfaced. Extended STA in [37] and viability analysis in [40] refine the notion of true criticality by moving from graph-longest paths toward probabilistically relevant paths. Adjacency criticality in [35] improves yield-oriented optimization by redefining gate importance. Even early RTL delay prediction in [27] serves chiefly as a screen for risky regions rather than a source of final-delay values. A robust timing methodology therefore should be evaluated by how well it preserves the right ordering and the right critical set.

### 6.6 Accelerate fallback instead of pretending fallback is unnecessary

The systems that integrate cleanly into real flows do not eliminate fallback to trusted analysis. They make fallback cheaper. GPU PBA in [21] makes pessimism reduction callable during closure instead of only near tapeout. Heterogeneous STA in [22] reduces the cost of multicorner and incremental graph analysis. GPU-parallel interpolation in [11] reduces the cost of a more accurate primitive. This rule is central to ML deployment because predictive uncertainty is inevitable. A system with cheap fallback is safer than a system that must trust every prediction.

### 6.7 Robustness is multidimensional and must be addressed layer by layer

The corpus repeatedly shows that there is no single robustness axis. The SSTA survey in [49] deals with process variation and correlation. FA-STAC in [48] deals with crosstalk-induced delay interaction. Salman’s interdependent-constraint work in [46] deals with uncertainty in sequential timing windows. The cross-node predictor in [6] deals with technology migration. The aging models in [14], [15], and [23] deal with lifetime drift at cell, path, and ranking levels. The PSN-aware engine in [12] deals with dynamic operating-state variation. The multicorner systems in [16] and [28] deal with scenario explosion. The point is specific: each paper addresses a different failure mode, so “robustness” cannot be summarized by one benchmark.

Table 3 turns the narrative into a comparison matrix. It is not exhaustive over all fifty papers, but it captures the main families, their trust anchors, and the main way each family can fail if used naively.

| Family | Representative papers | What is learned or accelerated | Trust anchor | Main failure mode if used naively |
| --- | --- | --- | --- | --- |
| Early screening | [27], [29] | RTL delay or preplacement timing ranking | Ranking utility rather than signoff replacement | Over-trusting estimates before physical variables exist |
| Placement-stage action models | [1], [2], [3] | Sizing, buffering, or optimization-compatible surrogates | Direct coupling to placement decisions | Feature drift as optimization changes topology |
| Correlation-restoration models | [25], [13], [10], [7] | Post-placement or GR-to-DR correction toward stronger truth | Stronger downstream reference or signoff metric | Toolflow-specific correction that may not transfer |
| Transfer and ECO models | [4], [6], [19] | Reusable arc, node, or stage representations | Explicit transfer structure | Domain shift when the reusable structure is misidentified |
| Scenario and method decision layers | [16], [28], [9] | Corner selection, fallback gating, or method selection | Bayesian gating or bounded method choice | Missed violations if uncertainty control is weak |
| Primitive timing models | [24], [11], [12], [30], [34] | Cell-delay kernels, interpolation, PSN arcs, or statistical operators | Physics-preserving primitive inside STA/SSTA | Better local error without guaranteed closure benefit |
| Engine acceleration | [21], [22] | PBA or multicorner STA kernels | Trusted timing engine remains in the loop | Runtime gains reduced by irregularity or integration overhead |

## 7. The Integration Blueprint: A Practical Architecture for Intent-Robust Timing Closure

This section synthesizes the corpus into a single workflow that can organize a conference paper and, more importantly, a timing-closure story that stays connected to signoff. The key idea is not to replace signoff with a universal learned model. It is to align different methods with different closure decisions and to ensure that every layer either preserves trustworthiness or reduces the cost of restoring it.

### 7.1 Layer 1: semantics and statistical guardrails

Any integrated flow should begin by treating timing metrics as semantically loaded rather than purely numerical. Slack semantics from [50] determine whether a learned slack target still means “available timing margin.” True-path reasoning from [37] and [40] determines whether the reported critical path is merely graph-longest or actually operationally relevant. Bosak in [18] provides the optimization formulation when histogram propagation must coexist with explicit constraints. Li et al. in [43] provide the compression-and-recorrelation machinery needed when IP-level timing models are abstracted and then reassembled at full-chip scope. Wu et al. in [45] provide conditional-moment propagation when path-delay distributions and correlation structure must be carried explicitly. Veetil et al. in [47] provide a simulation-grounded fallback when sampled statistical checks are still needed but brute-force Monte Carlo is too slow. This layer is the guardrail against optimizing the wrong quantity.

### 7.2 Layer 2: cheap early-stage triage

At the earliest stages, the objective is not signoff equivalence. It is triage. RTL delay prediction in [27] screens risky combinational regions before implementation. Preplacement estimation in [29] adds a net-length surrogate so timing can be ranked before placement exists. Placement-stage guidance in [1] proposes candidate sizing and buffering actions, and derivable placement modeling in [3] turns the timing surrogate into a usable optimization signal inside placement. In this layer, the key question is not whether the model matches final signoff numerically; it is whether the model points the optimizer toward the right early decisions.

### 7.3 Layer 3: stage-alignment and correlation restoration

Once the flow enters placement and routing, the dominant problem becomes alignment to higher-fidelity downstream truth. The Random-Forest corrector in [25] learns the cell-delay gap between a post-placement estimator and a higher-fidelity reference, and the ensemble follow-up in [13] shows the same idea survives richer 16 nm industrial data. The hierarchical pre-route model in [17] predicts net R, net C, arc length, arc delay, and arc slew before routing, while the slack model in [5] follows the timing graph with alternating attention and propagation layers. PRO-TIME in [8] addresses the next failure mode by making the target optimization-aware and by fusing netlist and layout embeddings so endpoint features remain meaningful after timing optimization. The GR-to-DR model in [10] learns detailed-route parasitics from global-route features, and the routing-topology framework in [7] uses a learned signoff evaluator to modify Steiner topology itself. This layer earns trust only when it narrows the gap between the current abstraction and final routed timing.

### 7.4 Layer 4: uncertainty-gated scenario reduction

As corner count grows, unconditional execution of every scenario in every iteration becomes unrealistic. The dominant-corner method in [28] reduces the scenario set by selecting a small subset of corners to execute directly and predicting the rest from them. The Bayesian multicorner framework in [16] adds the next safeguard by deciding when a prediction is reliable enough and when an extra STA run is still needed. TimeBoost in [9] performs a similar gating step at the method level by choosing whether a stage deserves a cheaper or more accurate analysis routine. These systems save runtime only because they make the trust decision explicit.

### 7.5 Layer 5: accelerated high-fidelity truth

The integrated flow still needs a trustworthy analysis substrate. GPU PBA in [21] accelerates shortest-path-forest generation, ranking, constrained subgraph handling, and other path-based kernels so that pessimism reduction can be used earlier and more often. Heterogeneous STA in [22] accelerates levelization, RC computation, propagation, LUT lookup, incremental updates, and multicorner batching inside a trusted engine. GPU-parallel interpolation in [11] keeps a more accurate timing-table primitive cheap enough for repeated use, and JIT-integrated noise-aware arc models in [12] make PSN-aware timing feasible inside STA rather than in an external script. This is the layer that keeps exact timing affordable enough to remain the fallback.

### 7.6 Layer 6: reliability and lifetime closure

Finally, closure must remain valid beyond nominal operation. The cell-level model in [14] learns aging-aware delay from multi-typed device graphs. The path-level model in [15] adds workload-aware degradation through a spatial-temporal transformer plus graph attention. The ranking flow in [23] identifies which path sets become critical after aging instead of assuming the nominal critical set remains dominant. AVATAR in [26] extends the question into dynamic timing and better-than-worst-case operation. BTI-aware statistical timing in [44] and time-varying SSTA in [38] provide the physical and probabilistic basis for those models. In a mature integrated flow, these are the mechanisms that decide whether “closed timing” stays closed after deployment.

### 7.7 What this blueprint implies for evaluation

An integrated timing-closure methodology should be evaluated on four axes at once. First, does early-stage prediction preserve the right ranking and decision signal? Second, does stage alignment improve final signoff QoR rather than only held-out regression error? Third, does uncertainty gating reduce runtime without silently missing violations? Fourth, does the methodology remain stable under ECOs, corner-set change, technology migration, and reliability drift? These evaluation criteria follow directly from the corpus and are stricter than the isolated MAE or R2 metrics that still dominate many ML papers.

### 7.8 Representative execution sequence

The blueprint becomes less abstract when written as one representative closure loop:

1. Screen the design early with RTL or preplacement models so risky logic regions and likely long nets are surfaced before physical implementation [27], [29].
2. Use placement-stage action models to propose sizing, buffering, or gradient-based placement moves rather than only predicting timing passively [1], [3].
3. After placement and during routing, restore correlation to downstream truth with post-placement correction, hierarchical pre-route prediction, optimization-aware embeddings, and GR-to-DR correction [25], [13], [17], [8], [10].
4. When scenario count becomes prohibitive, reduce analysis load with dominant-corner selection, Bayesian multicorner gating, or method selection, but keep explicit fallback to extra STA when confidence is weak [28], [16], [9].
5. Invoke accelerated trusted analysis for the expensive steps that still matter, especially PBA, multicorner propagation, and high-volume timing-kernel execution [21], [22], [11], [12].
6. Re-evaluate closure under aging, BTI, workload drift, and dynamic operating conditions before treating nominal closure as final [14], [15], [23], [44], [38], [26].

Written this way, the integration blueprint is not merely a taxonomy. It is an execution order for how learned models and trusted engines can coexist inside one closure loop.

## 8. Experimental Methodology, Deployment Lessons, and Open Challenges

### 8.1 Prediction metrics are necessary but insufficient

The corpus uses MAE, MSE, R2, MAPE, correlation, and classification AUC extensively. The complex-network model in [2] uses MSE, R2, correlation, and AUC to evaluate slack, delay, WNS, TNS, and critical-path identification. The ECO model in [19] uses R2 and MAE because it is judged on post-change path-delay fidelity. The aging path model in [15] uses MAPE because it predicts continuous degradation. Those metrics alone do not show whether a model improves closure. Papers that push further report closure-facing measures: the placement-guidance flow in [1] reports WNS, TNS, and violating-path count; the routing-topology flow in [7] reports signoff WNS, TNS, and optimization duration; the GR-to-DR correction flow in [10] reports post-DR timing and congestion behavior; the multicorner framework in [16] measures reliable runtime reduction; the pre-route optimization flow in [17] measures WNS, TNS, and violation reduction inside P&R; and the heterogeneous STA engine in [22] measures end-to-end runtime on trusted analysis tasks.

### 8.2 Data generation remains a structural bottleneck

High-quality timing labels are expensive because they depend on signoff tools, parasitic extraction, or SPICE characterization. The transfer-learning framework in [4] addresses this by reusing information across similar timing arcs instead of characterizing each arc from scratch. The cross-node model in [6] addresses it by transferring older-node knowledge into a new node with feature alignment and cell-distribution reweighting. PRO-TIME in [8] addresses it by redefining the data-generation process so the labels actually reflect a timing-optimized flow rather than a simplified one. The correction frameworks in [10], [13], and [25] address it by learning the gap to higher-fidelity truth from a narrower supervised slice. Data strategy is therefore part of the method, not preprocessing.

### 8.3 Scalability of graph models is still unresolved

Graph models dominate the modern literature because circuits are graphs, but large-netlist scalability remains difficult. The graph-attention slack predictor in [5] already exposes the problem by alternating expressive attention and propagation over timing graphs. The hierarchical pre-route model in [17] reduces the learning burden by splitting the task into level-1 physical surrogates and level-2 timing quantities. PRO-TIME in [8] reduces it differently by using endpoint embeddings and a separate layout encoder instead of one monolithic graph model. The hierarchical timing-model work in [43] suggests an older but still relevant systems answer: compress the timing problem before running the expensive inference step. The open problem is how to combine expressive graph models with this kind of compression without losing the timing relationships that matter.

### 8.4 Multi-physics closure is still fragmented

The literature on dynamic supply noise [12], aging-aware cell modeling [14], path-level aging [15], BTI-aware timing [44], coupling-aware STA [48], and statistical timing under process variation [49] is still largely segmented by effect. Each paper is precise about its own perturbation: [12] models PSN with noise-aware arc parameters and JIT-integrated MLPs, [14] models cell aging from device graphs, [15] models workload-conditioned path aging, [44] models BTI variability over time, [48] models crosstalk through iterative coupling analysis, and [49] covers statistical variation more broadly. What is missing is a single flow that can represent several of these perturbations at once without exploding runtime or collapsing them into one pessimistic guardband.

### 8.5 Uncertainty calibration needs explicit mechanisms

The Bayesian decision strategy in [16] couples every prediction with the option of extra STA when confidence is inadequate. TimeBoost in [9] manages uncertainty differently but just as explicitly: it avoids free-running delay regression and instead chooses among existing analysis methods whose runtime and fidelity are already known. Future work should extend this idea from method selection and corner gating to calibrated endpoint-slack uncertainty, out-of-distribution detection under ECO or node migration, and explicit safe-underestimation controls for violation screening.

### 8.6 Closed-loop benchmarking should become standard

One of the most visible gaps in the literature is that many papers still evaluate predictors outside the optimization loop they are meant to influence. The derivable placement model in [3], the routing-topology framework in [7], the pre-route optimization framework in [17], and the ECO accelerator in [19] all move toward more realistic closed-loop evaluation. More work should follow that direction. A mature benchmark suite for timing ML should include incremental ECO sequences, changing corner sets, fixed runtime budgets, and final QoR outcomes, not only held-out prediction error.

### 8.7 Threats to validity of this review and of cross-paper comparison

This manuscript synthesizes a fixed fifty-paper corpus rather than claiming an exhaustive crawl of all databases and venues. That choice makes the paper coherent, but it also creates scope limits that should be stated plainly. First, reported metrics are heterogeneous by construction: some papers optimize WNS and TNS, some predict slack or path delay, some report runtime only, and some focus on classification accuracy for critical-path ranking. Directly comparing those numbers without task context would be misleading.

Second, toolchains, nodes, and datasets differ sharply across the corpus. Industrial 7 nm or 16 nm studies [8], [13], [16] are not directly comparable to open benchmark studies or older-node methodology papers [27], [29], [47]. Some papers evaluate on routed industrial designs, some on academic benchmarks, and some on SPICE-characterized cell data. That heterogeneity is exactly why this review emphasizes trust mechanisms, deployment position, and robustness axis rather than a single leaderboard.

Third, publication and confidentiality effects bias the visible evidence. Industrially relevant failures may be underreported, while publishable academic results often emphasize accuracy or speedup on the metrics that are easiest to disclose. GPU acceleration can look cleaner in papers than in production flows when host-device movement, memory irregularity, or integration overhead is not fully surfaced [21], [22]. Transfer and correction models can also appear more stable than they are when the reference flow and deployment flow are closely matched [10], [13], [25].

Finally, *intent-robust timing closure* is a review-level synthesis term, not a label claimed by the original papers themselves. The rubric in Table 2 is therefore an interpretive device introduced by this manuscript. Its value depends on whether it helps distinguish methods in a way that is clearer than task-by-task reporting. The paper should be judged on that analytical usefulness, not on whether any single source uses the same phrase.

## 9. Conclusion

The fifty-paper corpus does not point to one replacement for STA. It points to a division of labor across four developments: sharper treatment of timing semantics, ML models that screen or guide decisions earlier, accelerated engines that keep trusted analysis callable, and timing models that include variation, aging, and noise. The papers that remain convincing are the ones that respect the structure of timing analysis, preserve a signoff anchor, expose uncertainty, and reduce the cost of restoring truth when prediction is not enough.

The main conclusion of this review is therefore architectural. Intent-robust timing closure should be built as a layered system. Early-stage models should triage and rank. Mid-stage models should restore correlation to higher-fidelity downstream truth. Decision layers should determine where prediction is safe. GPU-backed engines should keep high-fidelity analysis inside the loop. Reliability-aware and statistical models should define what “safe timing” means beyond nominal signoff. That combination is the most defensible way to bring ML and acceleration together in a conference-quality timing-closure paper.

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
[31] “Timing Analysis and Optimization Method with Interdependent Flip-Flop Timing Model for Near-Threshold Design,” *Electronics*, 2022. doi: 10.3390/electronics11223670.  
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
[45] “Delay-Correlation-Aware SSTA Based on Conditional Moments,” *Microelectronics Journal*, 2012. doi: 10.1016/j.mejo.2012.01.003.  
[46] “Utilizing Interdependent Timing Constraints to Enhance Robustness in Synchronous Circuits,” *Microelectronics Journal*, 2012. doi: 10.1016/j.mejo.2011.11.005.  
[47] “Fast Statistical Static Timing Analysis Using Smart Monte Carlo Techniques,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2011. doi: 10.1109/TCAD.2011.2108030.  
[48] “FA-STAC: An Algorithmic Framework for Fast and Accurate Coupling Aware Static Timing Analysis,” *IEEE Transactions on Very Large Scale Integration (VLSI) Systems*, 2011. doi: 10.1109/TVLSI.2009.2035323.  
[49] “Statistical Static Timing Analysis: A Survey,” *Integration, the VLSI Journal*, 2009. doi: 10.1016/j.vlsi.2008.10.002.  
[50] “Slack in Static Timing Analysis,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 2006. doi: 10.1109/TCAD.2005.858348.
