# Final Integration Image Shortlist

This shortlist is based on the actual argument structure of `drafts/integration.md`, not on the older generic image plan.

Selection rule:
- only figures verified to exist in the local PDF set
- chosen to match the paper's narrative from Sections 1 through 8
- biased toward workflow, architecture, and closure-process visuals rather than scatter plots

## Recommended final set for the integrated paper

### 1. Overall timing-closure framing
- Final paper role:
  best replacement for the opening high-level overview image
- Use:
  `[28] Figure 10`
- Figure name:
  `The commercial timing closure process (left) and machine-learning-based timing closure process (right).`
- PDF:
  [28.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/28.pdf)
- Why it fits this paper:
  `integration.md` opens by arguing that timing closure is an iterative loop and that ML changes the closure process, not just one predictor. This figure matches that opening directly.

### 2. STA foundation
- Final paper role:
  Section 3 foundation figure
- Use:
  `[49] Fig. 8`
- Figure name:
  `Illustration of static timing analysis.`
- PDF:
  [49.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/49.pdf)
- Why it fits this paper:
  Section 3 revisits classical STA before discussing ML and acceleration, so this gives the reader the baseline.

### 3. Block-based versus path-based timing
- Final paper role:
  Section 3 figure for why trusted analysis still matters
- Use:
  `[49] Fig. 10`
- Figure name:
  `Path-based (above) and block-based (below) timing graph traversal.`
- PDF:
  [49.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/49.pdf)
- Why it fits this paper:
  The integrated paper repeatedly contrasts cheap graph-level timing with more accurate but more expensive analysis.

### 4. Placement-stage action-oriented ML
- Final paper role:
  Section 4.2 figure
- Use:
  `[1] Figure 2`
- Figure name:
  `Overview of optimization guidance framework based on physical and timing prediction to improve placement quality.`
- PDF:
  [electronics-14-00329-v2.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/electronics-14-00329-v2.pdf)
- Why it fits this paper:
  Section 4.2 argues that placement-stage ML should change the next physical move. This is the clearest paper-backed image for that point.

### 5. Preplacement timing through explicit intermediate physics
- Final paper role:
  Section 4.1 or early Section 4 figure
- Use:
  `[29] Fig. 3`
- Figure name:
  `Net size and timing prediction flow.`
- PDF:
  [29.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/29.pdf)
- Why it fits this paper:
  Section 4.1 and Section 6.4 both emphasize intermediate physical quantities as stabilizers. This figure directly supports that theme.

### 6. Pre-route timing prediction and optimization
- Final paper role:
  Section 4.4 figure
- Use:
  `[17] Fig. 7`
- Figure name:
  `The overall flow of our proposed timing prediction (blue line) and optimization (red line) framework.`
- PDF:
  [17.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/17.pdf)
- Why it fits this paper:
  This is one of the strongest figures for the paper because Section 4.4 is central to the integrated argument.

### 7. Optimization-aware multimodal prediction
- Final paper role:
  Section 4.5 figure
- Use:
  `[8] Fig. 2`
- Figure name:
  `Overview of our proposed end-to-end endpoint embedding framework PRO-TIME...`
- PDF:
  [J153-TCAD2025-PRO-TIME.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/J153-TCAD2025-PRO-TIME.pdf)
- Backup:
  `[8] Fig. 1`
- Why it fits this paper:
  Section 4.5 and Section 6.3 treat feature mismatch under timing optimization as a major deployment problem. This figure is exactly on point.

### 8. Stage mismatch and correlation restoration
- Final paper role:
  Section 4.5 or Section 7.3 figure
- Use:
  `[10] Fig. 7`
- Figure name:
  `Flows that use different parasitic estimates for post-GR timing optimizations...`
- PDF:
  [3626959.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/3626959.pdf)
- Backup:
  `[10] Fig. 4`
- Why it fits this paper:
  This is the best figure for one of the paper's strongest claims: stage mismatch is a first-class closure problem.

### 9. Safe multicorner prediction with fallback
- Final paper role:
  Section 4.7 and Section 7.4 figure
- Use:
  `[16] Fig. 1`
- Figure name:
  `Workflow of our timing prediction method... with Bayesian decision theory.`
- PDF:
  [16.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/16.pdf)
- Why it fits this paper:
  The final manuscript repeatedly argues that good ML systems learn decisions and preserve fallback. This is the cleanest visual proof.

### 10. Dynamic-noise-aware timing inside STA
- Final paper role:
  Section 4.8 figure
- Use:
  `[12] Fig. 9`
- Figure name:
  `Architecture of the proposed MLP model.`
- PDF:
  [12.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/12.pdf)
- Backup:
  `[12] Fig. 10`
- Why it fits this paper:
  Section 4.8 is about primitive timing models embedded into trusted analysis. This figure supports that exact argument.

### 11. Aging changes what is critical
- Final paper role:
  Section 4.9 and Section 7.6 figure
- Use:
  `[23] Fig. 1`
- Figure name:
  `(a) Example showing how the path, which was uncritical before aging, became critical after aging...`
- PDF:
  [23.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/23.pdf)
- Why it fits this paper:
  This is the most intuitive reliability figure in the corpus and fits the paper's lifetime-robustness message perfectly.

### 12. GPU-accelerated trusted multicorner STA
- Final paper role:
  Section 5.1 and Section 7.5 figure
- Use:
  `[22] Fig. 4`
- Figure name:
  `Overall taskflow of our GPU-accelerated multicorner STA engine...`
- PDF:
  [22.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/22.pdf)
- Backup:
  `[22] Fig. 5`
- Why it fits this paper:
  Section 5.1 depends heavily on the argument that acceleration keeps trusted analysis inside the loop. This is the best engine figure for that.

### 13. GPU PBA runtime-versus-fidelity tradeoff
- Final paper role:
  Section 5.1 follow-up figure
- Use:
  `[21] Fig. 1`
- Figure name:
  `Computational tradeoff between runtime and pessimism reduction on path-based timing analysis.`
- PDF:
  [21.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/21.pdf)
- Backup:
  `[21] Fig. 3`
- Why it fits this paper:
  It supports the manuscript's core systems point that accurate fallback is valuable only if it is fast enough to use repeatedly.

## Best 10-image version if space gets tight

If the paper must be tighter, keep these ten:

1. `[28] Figure 10` from [28.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/28.pdf)
2. `[49] Fig. 8` from [49.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/49.pdf)
3. `[1] Figure 2` from [electronics-14-00329-v2.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/electronics-14-00329-v2.pdf)
4. `[17] Fig. 7` from [17.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/17.pdf)
5. `[8] Fig. 2` from [J153-TCAD2025-PRO-TIME.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/J153-TCAD2025-PRO-TIME.pdf)
6. `[10] Fig. 7` from [3626959.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/3626959.pdf)
7. `[16] Fig. 1` from [16.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/16.pdf)
8. `[23] Fig. 1` from [23.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/23.pdf)
9. `[22] Fig. 4` from [22.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/22.pdf)
10. `[21] Fig. 1` from [21.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/21.pdf)

## Good reserve images

- `[12] Fig. 9` from [12.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/12.pdf)
- `[14] Fig. 2` from [14.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/14.pdf)
- `[15] Figure 2` from [15.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/15.pdf)
- `[26] Fig. 3` from [26.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/26.pdf)
- `[11] Fig. 3` from [11.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/11.pdf)
- `[25] Fig. 3` from [25.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/25.pdf)

## Final recommendation

For this specific integrated paper, the strongest visual story is:

- one closure-process overview
- one STA foundation visual
- four ML workflow figures across the flow
- one stage-mismatch correction figure
- one safe-fallback figure
- one reliability figure
- two GPU/trusted-analysis figures

That is the image mix that best matches the manuscript you currently have.
