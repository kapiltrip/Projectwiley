# PDF-Verified Image List

This list replaces the custom/original figure slots with figures that were verified to exist in the local `papers50` PDF set.

Verification basis:
- local JSON metadata extracted from the PDFs in `metadata/meatdatagenerated/json`
- figure captions matched by exact figure identifiers such as `Fig. 1`, `Fig. 2`, `Figure 10`

Important:
- These are **actual paper-backed figures**.
- Some of them are **replacements** for the earlier custom synthesis figures.
- If every figure in the final paper must come from a source PDF, this is the usable set.

## Main set

1. Intro / STA foundation
- Source paper ref: `[49]`
- Use: `Fig. 8`
- Caption: `Illustration of static timing analysis.`
- PDF: [49.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/49.pdf)

2. STA traversal foundation
- Source paper ref: `[49]`
- Use: `Fig. 10`
- Caption: `Path-based (above) and block-based (below) timing graph traversal.`
- PDF: [49.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/49.pdf)

3. Placement guidance
- Source paper ref: `[1]`
- Use: `Figure 2`
- Caption: `Overview of optimization guidance framework based on physical and timing prediction to improve placement quality.`
- PDF: [electronics-14-00329-v2.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/electronics-14-00329-v2.pdf)

4. Preplacement timing estimation
- Source paper ref: `[29]`
- Use: `Fig. 3`
- Caption: `Net size and timing prediction flow.`
- PDF: [29.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/29.pdf)

5. Pre-route timing prediction and optimization
- Source paper ref: `[17]`
- Use: `Fig. 7`
- Caption: `The overall flow of our proposed timing prediction (blue line) and optimization (red line) framework.`
- PDF: [17.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/17.pdf)

6. Optimization-aware multimodal prediction
- Source paper ref: `[8]`
- Use: `Fig. 2`
- Caption: `Overview of our proposed end-to-end endpoint embedding framework PRO-TIME...`
- PDF: [J153-TCAD2025-PRO-TIME.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/J153-TCAD2025-PRO-TIME.pdf)
- Backup: `Fig. 1` in the same PDF

7. GR to DR stage mismatch
- Source paper ref: `[10]`
- Use: `Fig. 7`
- Caption: `Flows that use different parasitic estimates for post-GR timing optimizations...`
- PDF: [3626959.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/3626959.pdf)
- Backup: `Fig. 4` in the same PDF

8. Safe multicorner prediction
- Source paper ref: `[16]`
- Use: `Fig. 1`
- Caption: `Workflow of our timing prediction method... with Bayesian decision theory.`
- PDF: [16.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/16.pdf)

9. Noise-aware ML inside STA
- Source paper ref: `[12]`
- Use: `Fig. 9`
- Caption: `Architecture of the proposed MLP model.`
- PDF: [12.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/12.pdf)
- Backup: `Fig. 10` in the same PDF

10. Aging-aware cell timing
- Source paper ref: `[14]`
- Use: `Fig. 2`
- Caption: `The flow of generating node representations for multi-typed devices...`
- PDF: [14.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/14.pdf)
- Backup: `Fig. 1` in the same PDF

11. Aging-aware path timing
- Source paper ref: `[15]`
- Use: `Figure 2`
- Caption: `The overall process of the aging-aware timing prediction model.`
- PDF: [15.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/15.pdf)

12. Aging changes path ranking
- Source paper ref: `[23]`
- Use: `Fig. 1`
- Caption: `(a) Example showing how the path, which was uncritical before aging, became critical after aging...`
- PDF: [23.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/23.pdf)

13. GPU-accelerated multicorner STA
- Source paper ref: `[22]`
- Use: `Fig. 4`
- Caption: `Overall taskflow of our GPU-accelerated multicorner STA engine...`
- PDF: [22.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/22.pdf)
- Backup: `Fig. 5` in the same PDF

14. GPU PBA tradeoff
- Source paper ref: `[21]`
- Use: `Fig. 1`
- Caption: `Computational tradeoff between runtime and pessimism reduction on path-based timing analysis.`
- PDF: [21.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/21.pdf)
- Backup: `Fig. 3` in the same PDF

## Best replacements for the earlier custom-only slots

1. Earlier custom slot: `intent-robust timing closure map`
- Replace with: `[28] Figure 10`
- Caption: `The commercial timing closure process (left) and machine-learning-based timing closure process (right).`
- PDF: [28.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/28.pdf)

2. Earlier custom slot: `integrated closure stack`
- Replace with: `[26] Fig. 3`
- Caption: `Overview of the task flow for AVATAR.`
- PDF: [26.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/26.pdf)

3. Earlier custom slot: `representative execution sequence`
- Replace with: `[27] Fig. 1`
- Caption: `General flow for dataset collection.`
- PDF: [27.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/27.pdf)

4. Earlier custom slot: `evaluation matrix`
- Replace with: `[25] Fig. 3`
- Caption: `Scatter plots of predicted cell delay vs. Actual cell delay for each design.`
- PDF: [25.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/25.pdf)

## Reserve set

15. Timing closure workflow comparison
- Source paper ref: `[28]`
- Use: `Figure 10`
- PDF: [28.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/28.pdf)

16. Timing-table interpolation model
- Source paper ref: `[11]`
- Use: `Fig. 3`
- PDF: [11.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/11.pdf)

17. Cell-delay deep learning
- Source paper ref: `[24]`
- Use: `Fig. 5`
- PDF: [24.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/24.pdf)

18. Post-placement correction scatter
- Source paper ref: `[25]`
- Use: `Fig. 3`
- PDF: [25.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/25.pdf)

19. AVATAR ML-assisted flow
- Source paper ref: `[26]`
- Use: `Fig. 7`
- PDF: [26.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/26.pdf)

20. Dataset generation flow
- Source paper ref: `[27]`
- Use: `Fig. 1`
- PDF: [27.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/27.pdf)

21. Multicorner ML application flow
- Source paper ref: `[28]`
- Use: `Figure 5`
- PDF: [28.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/28.pdf)

22. SSTA neural operator view
- Source paper ref: `[34]`
- Use: `Fig. 1`
- PDF: [34.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/34.pdf)

23. Buffer-location routing effect
- Source paper ref: `[10]`
- Use: `Fig. 4`
- PDF: [3626959.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/3626959.pdf)

24. GPU PBA algorithm overview
- Source paper ref: `[21]`
- Use: `Fig. 3`
- PDF: [21.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/21.pdf)

25. Aging-aware STA flow
- Source paper ref: `[23]`
- Use: `Fig. 3`
- PDF: [23.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/23.pdf)

26. Parallel critical-path selection
- Source paper ref: `[23]`
- Use: `Fig. 9`
- PDF: [23.pdf](/C:/Users/kapil/OneDrive/Desktop/sta50journals/papers50/23.pdf)
