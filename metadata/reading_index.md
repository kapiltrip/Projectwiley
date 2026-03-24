# Paper Reading Index

Processed papers: 50

This index is derived from local PDF extraction. Author fields are taken from PDF metadata when available and otherwise guessed from the first page.

## 1. TimeBoost: Accelerating timing analysis engines using XGBoost

- Source file: `1-s2.0-S1434841125002110-main.pdf`
- Authors: Anastasis Vagenas
- Journal: AEUE - International Journal of Electronics and Communications
- Year: 2025
- DOI: 10.1016/j.aeue.2025.155870
- Pages: 9
- Citation: Anastasis Vagenas (2025). TimeBoost: Accelerating timing analysis engines using XGBoost. AEUE - International Journal of Electronics and Communications. https://doi.org/10.1016/j.aeue.2025.155870
- Abstract: Timing analysis is an essential verification method for the design and optimization of integrated circuits, while it also constitutes the cornerstone of the final signoff. However, the increasing complexity of modern designs, driven by aggressive technology scaling, necessitates more efficient timing engines. In this article, we introduce TimeBoost, a novel learning-based approach for performance optimization of gate-level timing analysis. TimeBoost employs GPU-accelerated XGBoost classifiers to evaluate stage complexity and select the optimal timing analysis method, exploiting the available runtime and accuracy trade-off. Unlike prior works that predict timing directly, our approach ensures reliable and accurate timing estimation by leveraging timing analysis methods as prediction targets. Moreover, our models utilize representative electrical, topological, and gate features for each stage, which can be extracted with minimal effort. We assess several Machine Learning (ML) models, including XGBoost, Artificial Neural Networks, and K-Nearest Neighbors, and explore their different hyperparameters. Experimental evaluation on one million stages demonstrates that our MLbased approach achieves a runtime improvement of up to 3.86× over our best available method, imposing only a 3%–4% overhead to timing analysis while maintaining high accuracy. Thus, the proposed models can be integrated into signoff tools or timing-driven iterative optimization flows to expedite timing closure.
- HTML: `html/1-s2.0-S1434841125002110-main.html`
- JSON: `metadata/meatdatagenerated/json/1-s2.0-S1434841125002110-main.json`

## 2. Complex network based machine learning method for predicting circuit timing

- Source file: `1-s2.0-S1568494625014139-main.pdf`
- Authors: Tingyuan Nie
- Journal: Applied Soft Computing
- Year: 2026
- DOI: 10.1016/j.asoc.2025.114100
- Pages: 8
- Citation: Tingyuan Nie (2026). Complex network based machine learning method for predicting circuit timing. Applied Soft Computing. https://doi.org/10.1016/j.asoc.2025.114100
- Abstract: Due to the high cost of timing signoff in the routing stage of VLSI (very large-scale integration), timing analysis in the placement stage is usually used to assist the implementation. Still, uncertainty exists due to the lack of detailed wiring information. Considering the close relationship between signal propagation and circuit topology, we propose a machine-learning method to predict the circuit timing using complex network features and construct basic and augmented models for comparison. Firstly, in the placement stage, the fundamental circuit features related to timing optimization are extracted, and the complex network features on the timing path are computed by complex network modeling, based on which the dataset for machine learning is generated. Secondly, we use machine learning algorithms to compare the performance of the two models in predicting circuit timing. Experimental results show that the augmented model combining complex network features outperforms the basic model in timing prediction accuracy. The augmented model achieves a 12.5 % reduction in MSE (mean squared error) for predicting slack, reaching 0.004515. It also shows a 1.06 % improvement in R 2 , reaching 0.9314, and a 0.54 % improvement in r, reaching 0.9652. For predicting delay, the MSE is reduced by 11.69 %, reaching 0.000302, while R 2 improves by 0.03 % to 0.9973, and r improves by 0.02 % to 0.9987. The deviation in predicting WNS (worst negative slack) is reduced by 6.53 %, reaching 5.30 %, and for TNS (total negative slack), it is reduced by 1.59 %, reaching 12.38 %. The AUC (area under the ROC (receiver operating characteristic) curve) value for identifying critical paths increases by 0.26 %, reaching 0.9873. These results demonstrate the efficiency of the proposed method in utilizing complex network features for predicting circuit timing.
- HTML: `html/1-s2.0-S1568494625014139-main.html`
- JSON: `metadata/meatdatagenerated/json/1-s2.0-S1568494625014139-main.json`

## 3. Knowledge transferring framework for cell library characterization

- Source file: `1-s2.0-S1879239124002467-main.pdf`
- Authors: Zhengguang Tang
- Journal: Microelectronics Journal
- Year: 2025
- DOI: 10.1016/j.mejo.2024.106542
- Pages: 8
- Citation: Zhengguang Tang (2025). Knowledge transferring framework for cell library characterization. Microelectronics Journal. https://doi.org/10.1016/j.mejo.2024.106542
- Abstract: To evaluate digital circuit performance across PVT (process, voltage, and temperature) corners, standard cell library characterization requires costly simulations. Leveraging machine learning (ML) can improve the efficiency of this process. However, existing ML-based methods for cell library characterization often neglect the knowledge embedded across different timing arcs, leading to the need for extensive training data. In this paper, we propose a transfer learning (TL) framework to enhance timing characterization across multiple timing arcs. By quantifying the similarity among training tasks in the cell library using a fine-grained metric, our method enables rapid and accurate cell delay predictions through pre-training knowledge. Compared to conventional ML approaches, our TL framework improves both prediction accuracy and efficiency. Experimental results on 45 nm MOSFET and 14 nm FINFET technologies show significant error reductions of up to 80% and 67%, respectively.
- HTML: `html/1-s2.0-S1879239124002467-main.html`
- JSON: `metadata/meatdatagenerated/json/1-s2.0-S1879239124002467-main.json`

## 4. Accurate Interpolation of Library Timing Parameters Through Recurrent Convolutional Neural Network

- Source file: `11.pdf`
- Authors: Daijoon Hyun , Member, IEEE, Younggwang Jung , Graduate Student Member, IEEE, and Youngsoo Shin , Fellow, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2024
- DOI: 10.1109/TCAD.2023.3316991
- Pages: 5
- Citation: Daijoon Hyun , Member, IEEE, Younggwang Jung , Graduate Student Member, IEEE, and Youngsoo Shin , Fellow, IEEE (2024). Accurate Interpolation of Library Timing Parameters Through Recurrent Convolutional Neural Network. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2023.3316991
- Abstract: Interpolation is used to approximate the timing parameters of logic cells not specified in timing tables. Bilinear interpolation has been taken for granted in the industry, but the error increases as the nonlinearity of the timing parameters increases. In this article, we propose machine learning (ML)-based interpolation to obtain more accurate timing parameters. Recurrent convolutional neural network (R-CNN) is employed and various ranges of table entries form a sequence of input data, in which the recurrent network allows them to influence the interpolation. In addition, variational autoencoder (VAE) is used to capture the distribution feature of the table. ML interpolation is parallelized in GPU to minimize the runtime overhead from numerous arithmetic operations. Experimental results demonstrate that ML interpolation reduces timing parameter error by 19.7% and path delay error by 3.4% compared to bilinear interpolation at the cost of 13% runtime overhead.
- HTML: `html/11.html`
- JSON: `metadata/meatdatagenerated/json/11.json`

## 5. Dynamic Supply Noise Aware Timing Analysis With JIT Machine Learning Integration

- Source file: `12.pdf`
- Authors: Yufei Chen, Graduate Student Member, IEEE, Zizheng Guo , Student Member, IEEE, Runsheng Wang , Member, IEEE, Ru Huang, Fellow, IEEE, Yibo Lin , Member, IEEE, and Cheng Zhuo , Senior Member, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2024
- DOI: 10.1109/TCAD.2023.3342603
- Pages: 14
- Citation: Yufei Chen, Graduate Student Member, IEEE, Zizheng Guo , Student Member, IEEE, Runsheng Wang , Member, IEEE, Ru Huang, Fellow, IEEE, Yibo Lin , Member, IEEE, and Cheng Zhuo , Senior Member, IEEE (2024). Dynamic Supply Noise Aware Timing Analysis With JIT Machine Learning Integration. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2023.3342603
- Abstract: The incessant decrease in transistor size has led to reduced voltage noise margins and exacerbated power integrity challenges. This trend intensifies concerns about the efficacy of conventional static timing analysis (STA), which traditionally assumes a constant power supply level, often resulting in imprecise and overly conservative outcomes. To address this, this article proposes a dynamic-noise-aware STA engine enhanced by just-in-time (JIT) machine learning (ML) integration. This approach employs the Weibull cumulative distribution function (CDF) to accurately represent dynamic power supply noise (PSN). We perform gate-level characterization, assessing delay and transition time for each timing arc under variations in input transition time, output capacitance, and three PSN-aware parameters. The timing for each timing arc can then be predicted by a multilayer perceptron (MLP), trained with the characterization data. Finally, by incorporating JIT compilation techniques, we integrate trained MLP models into the STA engine, achieving both computational efficiency and flexibility. Experimental results show that the proposed method can accurately estimate the timing fluctuation due to dynamic PSN, with an average relative error of 4.89% for single-cell estimations and 6.27% for path delay estimations.
- HTML: `html/12.html`
- JSON: `metadata/meatdatagenerated/json/12.json`

## 6. Enhancing cell delay accuracy in post-placed netlists using ensemble tree-based algorithms

- Source file: `13.pdf`
- Authors: Yassine Attaoui
- Journal: Integration
- Year: 2024
- DOI: 10.1016/j.vlsi.2024.102193
- Pages: 10
- Citation: Yassine Attaoui (2024). Enhancing cell delay accuracy in post-placed netlists using ensemble tree-based algorithms. Integration. https://doi.org/10.1016/j.vlsi.2024.102193
- Abstract: Nowadays, the ASIC design is increasing in complexity, and PPA targets are pushed to the limit. The lack of physical information at the early design stages hinders precise timing predictions and may lead to design re-spins. In previous work, we successfully improved timing prediction at the post-placement stage using the Random Forest model, achieving 91.25% cell delay accuracy. Building upon this, we further investigate the potential of Ensemble Tree-based algorithms, specifically focusing on ‘‘Extremely Randomized Trees’’ and ‘‘Gradient Boosting’’, to close the gap in cell delay accuracy. In this paper, we enrich the training dataset with new 16 nm industrial designs. The results demonstrate a substantial improvement, with an average cell delay accuracy of 92.01% and 84.26% on unseen data. The average Root-Mean-Square-Error is significantly reduced from 12.11 to 3.23 and 7.76 on unseen data.
- HTML: `html/13.html`
- JSON: `metadata/meatdatagenerated/json/13.json`

## 7. Fast and Accurate Aging-Aware Cell Timing Model via Graph Learning

- Source file: `14.pdf`
- Authors: Yuyang Ye , Tinghuan Chen, Zicheng Wang , Hao Yan , Bei Yu , Senior Member, IEEE, and Longxing Shi
- Journal: IEEE Transactions on Circuits and Systems II: Express Briefs
- Year: 2024
- DOI: 10.1109/TCSII.2023.3298917
- Pages: 5
- Citation: Yuyang Ye , Tinghuan Chen, Zicheng Wang , Hao Yan , Bei Yu , Senior Member, IEEE, and Longxing Shi (2024). Fast and Accurate Aging-Aware Cell Timing Model via Graph Learning. IEEE Transactions on Circuits and Systems II: Express Briefs. https://doi.org/10.1109/TCSII.2023.3298917
- Abstract: With transistors scaling down, aging effects become increasingly significant in circuit design. Thus, the aging-aware cell timing model is necessary for evaluating the aging-induced delay degradation and their impact on circuit performance. However, the tradeoff between accuracy and efficiency becomes a bottleneck in traditional methods. In this brief, we propose a fast and accurate aging-aware cell timing model via graph learning. The information of multi-typed devices on different arcs can be embedded by heterogeneous graph attention networks (H-GAT) and the embedded results help improve the accuracy of our aging-aware timing model. The experimental results indicate the proposed timing model can achieve high accuracy efficiently.
- HTML: `html/14.html`
- JSON: `metadata/meatdatagenerated/json/14.json`

## 8. Multi-View Graph Learning for Path-Level Aging-Aware Timing Prediction

- Source file: `15.pdf`
- Authors: Aiguo Bu, Xiang Li, Zeyu Li and Yizhen Chen
- Journal: As CMOS technology continues to scale down
- Year: 2024
- DOI: 10.3390/electronics13173479
- Pages: 15
- Citation: Aiguo Bu, Xiang Li, Zeyu Li and Yizhen Chen (2024). Multi-View Graph Learning for Path-Level Aging-Aware Timing Prediction. As CMOS technology continues to scale down. https://doi.org/10.3390/electronics13173479
- Abstract: As CMOS technology continues to scale down, the aging effect—known as negative bias temperature instability (NBTI)—has become increasingly prominent, gradually emerging as a key factor affecting device reliability. Accurate aging-aware static timing analysis (STA) at the early design phase is critical for establishing appropriate timing margins to ensure circuit reliability throughout the chip lifecycle. However, traditional aging-aware timing analysis methods, typically based on Simulation Program with Integrated Circuit Emphasis (SPICE) simulations or aging-aware timing libraries, struggle to balance prediction accuracy with computational cost. In this paper, we propose a multi-view graph learning framework for path-level aging-aware timing prediction, which combines the strengths of the spatial–temporal Transformer network (STTN) and graph attention network (GAT) models to extract the aging timing features of paths from both timing-sensitive and workloadsensitive perspectives. Experimental results demonstrate that our proposed framework achieves an average MAPE score of 3.96% and reduces the average MAPE by 5.8 times compared to FFNN and 2.2 times compared to PNA, while maintaining acceptable increases in processing time.
- HTML: `html/15.html`
- JSON: `metadata/meatdatagenerated/json/15.json`

## 9. Multicorner Timing Analysis Acceleration for Iterative Physical Design of ICs

- Source file: `16.pdf`
- Authors: Wei W. Xing , Member, IEEE, Longze Wang, Student Member, IEEE, Zhelong Wang, Student Member, IEEE, Zhaoyu Shi, Student Member, IEEE, Ning Xu, Member, IEEE, Yuanqing Cheng , Senior Member, IEEE, and Weisheng Zhao , Fellow, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2024
- DOI: 10.1109/TCAD.2024.3361401
- Pages: 12
- Citation: Wei W. Xing , Member, IEEE, Longze Wang, Student Member, IEEE, Zhelong Wang, Student Member, IEEE, Zhaoyu Shi, Student Member, IEEE, Ning Xu, Member, IEEE, Yuanqing Cheng , Senior Member, IEEE, and Weisheng Zhao , Fellow, IEEE (2024). Multicorner Timing Analysis Acceleration for Iterative Physical Design of ICs. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2024.3361401
- Abstract: We propose a multicorner multistage timing analysis prediction framework using a generalized linear model with latent features. We then further improve such methods using kernel trick extension, transfer learning with knowledge from previous designs, and multioutput feature engineering to deliver state-of-the-art (SOTA) prediction accuracy with very limited training data. Most importantly, our method is equipped with a Bayesian decision strategy to deliver reliable predictions with accuracy close to 100%, pushing the frontier of the machine-learning-based static timing analysis (STA) for practical implementation in the industry environment, where reliability is highly desired. Experimental results show that the accuracy of our proposed method outperforms the SOTA competitors by up to 4x and can improve prediction accuracy to 100% with little extra STA executions.
- HTML: `html/16.html`
- JSON: `metadata/meatdatagenerated/json/16.json`

## 10. Pre-route timing prediction and optimization with graph neural network models

- Source file: `17.pdf`
- Authors: Kyungjoon Chang
- Journal: Integration
- Year: 2024
- DOI: 10.1016/j.vlsi.2024.102262
- Pages: 13
- Citation: Kyungjoon Chang (2024). Pre-route timing prediction and optimization with graph neural network models. Integration. https://doi.org/10.1016/j.vlsi.2024.102262
- Abstract: In recent years, the application of deep learning (DL) models has sparked considerable interest in timing prediction within the place-and-route (P&R) flow of IC chip design. Specifically, at the pre-route stage, an accurate prediction of post-route timing is challenging due to the lack of sufficient physical information. However, achieving precise timing prediction significantly accelerates the design closure process, saving considerable time and effort. In this work, we propose pre-route timing prediction and optimization framework with graph neural network (GNN) models combined with convolution neural network (CNN). Our framework is divided into two main stages, each of which is further subdivided into smaller steps. Precisely, our GNNdriven arc delay/slew prediction model is divided into two levels: in level-1, it predicts net resistance (net R) and net capacitance (net C) using GNN while the arc length is predicted using CNN. These predictions are hierarchically passed on to level-2 where delay/slew is estimated with our GNN based prediction model. The timing optimization model utilizes the precise delay/slew predictions obtained from the GNN-driven prediction model to accurately set the path margin during the timing optimization stage. This approach effectively reduces unnecessary turn-around iterations in the commercial EDA tools. Experimental results show that by using our proposed framework in P&R, we are able to improve the pre-route prediction accuracy by 42%/36% on average on arc delay/slew, and improve timing metrics in terms of WNS, TNS, and the number of timing violation paths by 77%, 77%, and 64%, which are an increase of 32%/35% on arc delay/slew and 30%, 20% and 31% on timing optimization compared with the existing DL prediction model.
- HTML: `html/17.html`
- JSON: `metadata/meatdatagenerated/json/17.json`

## 11. Statistical static timing analysis via modern optimization lens: I. Histogram-based approach

- Source file: `18.pdf`
- Authors: Adam Bosák
- Journal: Optimization and Engineering
- Year: 2024
- DOI: 10.1007/s11081-023-09847-3
- Pages: 25
- Citation: Adam Bosák (2024). Statistical static timing analysis via modern optimization lens: I. Histogram-based approach. Optimization and Engineering. https://doi.org/10.1007/s11081-023-09847-3
- Abstract: Abstract not cleanly detected.
- HTML: `html/18.html`
- JSON: `metadata/meatdatagenerated/json/18.json`

## 12. TSTL-GNN: Graph-Based Two-Stage Transfer Learning for Timing Engineering Change Order Analysis Acceleration

- Source file: `19.pdf`
- Authors: Wencheng Jiang, Zhenyu Zhao, Zhiyuan Luo, Jie Zhou, Shuzheng Zhang, Bo Hu and Peiyun Bian
- Journal: Timing Engineering Change Order (ECO) is time-consuming in IC design
- Year: 2024
- DOI: 10.3390/electronics13152897
- Pages: 13
- Citation: Wencheng Jiang, Zhenyu Zhao, Zhiyuan Luo, Jie Zhou, Shuzheng Zhang, Bo Hu and Peiyun Bian (2024). TSTL-GNN: Graph-Based Two-Stage Transfer Learning for Timing Engineering Change Order Analysis Acceleration. Timing Engineering Change Order (ECO) is time-consuming in IC design. https://doi.org/10.3390/electronics13152897
- Abstract: Timing Engineering Change Order (ECO) is time-consuming in IC design, requiring multiple rounds of timing analysis. Compared to traditional methods for accelerating timing analysis, which focus on a specific design, timing ECO requires higher accuracy and generalization because the design changes considerably after ECO. Additionally, there are challenges with slow acquisition of data for large designs and insufficient data for small designs. To solve these problems, we propose TSTL-GNN, a novel approach using two-stage transfer learning based on graph structures. Significantly, considering that delay calculation relies on transition time, we divide our model into two stages: the first stage predicts transition time, and the second stage predicts delay. Moreover, we employ transfer learning to transfer the model’s parameters and features from the first stage to the second due to the similar calculation formula for delay and transition time. Experiments show that our method has good accuracy on open-source and industrial applications with an average R2score/MAE of 0.9952/13.36, and performs well with data-deficient designs. Compared to previous work, our model reduce prediction errors by 37.1 ps on the modified paths, which are changed by 24.27% on average after ECO. The stable R2 score also confirms the generalization of our model. In terms of time cost, our model achieved results for path delays consuming up to 80 times less time compared to open-source tool. Citation: Jiang, W.; Zhao, Z.; Luo, Z.; Zhou, J.; Zhang, S.; Hu, B.; Bian. P.
- HTML: `html/19.html`
- JSON: `metadata/meatdatagenerated/json/19.json`

## 13. Microsoft Word - 14---19557-贺旭C.doc

- Source file: `20.pdf`
- Authors: Administrator
- Journal: 第35 卷 第4 期 计算机辅助设计与图形学学报 Vol.35 No.4 2023 年4 月 Journal of Computer-Aided Design & Computer Graphics Apr. 2023
- Year: 2023
- DOI: 10.3724/SP.J.1089.2023.19557
- Pages: 13
- Citation: Administrator (2023). Microsoft Word - 14---19557-贺旭C.doc. 第35 卷 第4 期 计算机辅助设计与图形学学报 Vol.35 No.4 2023 年4 月 Journal of Computer-Aided Design & Computer Graphics Apr. 2023. https://doi.org/10.3724/SP.J.1089.2023.19557
- Abstract: Abstract not cleanly detected.
- HTML: `html/20.html`
- JSON: `metadata/meatdatagenerated/json/20.json`

## 14. A GPU-Accelerated Framework for Path-Based Timing Analysis

- Source file: `21.pdf`
- Authors: Guannan Guo , Tsung-Wei Huang , Member, IEEE, Yibo Lin , Member, IEEE, Zizheng Guo , Sushma Yellapragada, and Martin D. F. Wong, Fellow, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2023
- DOI: 10.1109/TCAD.2023.3272274
- Pages: 14
- Citation: Guannan Guo , Tsung-Wei Huang , Member, IEEE, Yibo Lin , Member, IEEE, Zizheng Guo , Sushma Yellapragada, and Martin D. F. Wong, Fellow, IEEE (2023). A GPU-Accelerated Framework for Path-Based Timing Analysis. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2023.3272274
- Abstract: As a key routine in static timing analysis (STA), path-based analysis (PBA) plays a very important role in refining the critical path report by reducing excessive slack pessimism. PBA is also well known for its long execution time, which makes it a hot topic for parallel computing in the STA community. However, nearly all of the parallel PBA algorithms are restricted to CPU architectures, which greatly limits their scalability. To achieve a new performance milestone on PBA, we must leverage the high throughput computing in the graphics processing unit (GPU). Therefore, in this work, we propose a new GPU-accelerated PBA framework which contains compact data structures and highly efficient kernels. By integrating with GPU-accelerated preprocessing steps, our framework can also effectively handle extensive critical path constraints. Besides, we highlight many optimization techniques that can overcome the execution bottleneck and further boost the performance. In experiments, we demonstrate 543× speed-up compared to the state-of-the-art PBA algorithm on the design with 1.6 million gates, which outperforms 25×–45× over the state-of-the-art parallel PBA algorithm on 40 CPU cores. A fully optimized framework can achieve 3×–5× speed-up on top of that.
- HTML: `html/21.html`
- JSON: `metadata/meatdatagenerated/json/21.json`

## 15. Accelerating Static Timing Analysis Using CPU&#x2013;GPU Heterogeneous Parallelism

- Source file: `22.pdf`
- Authors: Zizheng Guo , Tsung-Wei Huang , Member, IEEE, and Yibo Lin , Member, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2023
- DOI: 10.1109/TCAD.2023.3286261
- Pages: 12
- Citation: Zizheng Guo , Tsung-Wei Huang , Member, IEEE, and Yibo Lin , Member, IEEE (2023). Accelerating Static Timing Analysis Using CPU&#x2013;GPU Heterogeneous Parallelism. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2023.3286261
- Abstract: Static timing analysis (STA) is an essential yet time-consuming task during the circuit design flow to ensure the correctness and performance of the design. Thanks to the advancement of general-purpose computing on graphics processing units (GPUs), new possibilities and challenges have arisen for boosting the performance of STA. In this work, we present an efficient and holistic GPU-accelerated STA engine. We accelerate major STA tasks, including levelization, delay computation, graph propagation, and multicorner analysis, by developing high-performance GPU kernels and data structures. By dividing the STA workloads into CPU–GPU concurrent tasks with managed dependencies, our acceleration framework supports versatile incremental updates. Furthermore, we have extended our approach to multicorner analysis by exploring a large amount of corner-level data parallelism using GPU computing. Our implementation based on the open-source STA engine OpenTimer has achieved up to 4.07× speed-up on single corner analysis, and up to 25.67× speed-up on multicorner analysis on TAU 2015 contest designs and a 14-nm technology.
- HTML: `html/22.html`
- JSON: `metadata/meatdatagenerated/json/22.json`

## 16. Aging-Aware Critical Path Selection via Graph Attention Networks

- Source file: `23.pdf`
- Authors: Yuyang Ye , Tinghuan Chen , Member, IEEE, Yifei Gao , Hao Yan , Member, IEEE, Bei Yu , Senior Member, IEEE, and Longxing Shi , Senior Member, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2023
- DOI: 10.1109/TCAD.2023.3276944
- Pages: 14
- Citation: Yuyang Ye , Tinghuan Chen , Member, IEEE, Yifei Gao , Hao Yan , Member, IEEE, Bei Yu , Senior Member, IEEE, and Longxing Shi , Senior Member, IEEE (2023). Aging-Aware Critical Path Selection via Graph Attention Networks. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2023.3276944
- Abstract: In advanced technology nodes, aging effects like negative and positive bias temperature instability (NBTI and PBTI) become increasingly significant, making timing closure and optimization more challenging. Unfortunately, conventional critical path (CP) selection tools used in reliability-aware design flow cannot accurately identify CPs under different aging conditions. To address this issue, we propose an aging-aware CP selection flow comprising two parts: 1) critical cell detection and 2) path criticality (PC) computation. We employ graph-attention (GAT) networks to predict the critical cells in the aged circuits, and a PC computation algorithm that takes into account circuitlevel and transistor-level parameters to generate PC rank lists. Our experimental results demonstrate that our GAT model outperforms classical machine learning models in detecting critical cells. Additionally, compared with the commercial tool, our agingaware flow achieves an average accuracy of 99.52%, 98.69%, and 97.20% for top-10%, top-5%, and top-1% path sets, respectively, in five industrial designs subjected to different aging conditions and workloads.
- HTML: `html/23.html`
- JSON: `metadata/meatdatagenerated/json/23.json`

## 17. Deep-learning cell-delay modeling for static timing analysis

- Source file: `24.pdf`
- Authors: Waseem Raslan
- Journal: Ain Shams Engineering Journal
- Year: 2023
- DOI: 10.1016/j.asej.2022.101828
- Pages: 8
- Citation: Waseem Raslan (2023). Deep-learning cell-delay modeling for static timing analysis. Ain Shams Engineering Journal. https://doi.org/10.1016/j.asej.2022.101828
- Abstract: Delay and transition timetables plus voltage waveforms are used to characterize standard cell delays. More accurate models explode cell library size and degrades design flow performance. Our proposed deep learning non-linear delay model, DL-NLDM, technique outperformed 77 NLDM-LUT in average percentage errors with up to 1.4% error compared to SPICE and outperformed the non-standard 100100 NLDM- LUT in maximum percentage errors. The proposed DL Autoencoder-based waveform compression outperformed singular value decomposition by 1.79. Additionally, a novel DL waveform-delay model, DL- WFDM, models cell delays using encoded waveforms instead of delay and transition time. DL-WFDM outperformed DL-NLDM in maximum delay percentage errors.  2022 The Authors. Published by Elsevier B.V. on behalf of Faculty of Engineering, Ain Shams University This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-ncnd/4.0/).
- HTML: `html/24.html`
- JSON: `metadata/meatdatagenerated/json/24.json`

## 18. Machine learning application for cell delay accuracy improvement at post-placement stage: A case study for combinational cells

- Source file: `25.pdf`
- Authors: Yassine Attaoui
- Journal: Integration
- Year: 2023
- DOI: 10.1016/j.vlsi.2023.02.011
- Pages: 10
- Citation: Yassine Attaoui (2023). Machine learning application for cell delay accuracy improvement at post-placement stage: A case study for combinational cells. Integration. https://doi.org/10.1016/j.vlsi.2023.02.011
- Abstract: In the early VLSI design stages, as most interest is given to timing closure, various techniques are deployed to satisfy the timing constraints and close design timing. Nevertheless, timing still needs to be accurate at the early stages due to the lack of physical design information. Therefore, the challenge for most EDA Logic Synthesis engines is to improve the overall timing accuracy at higher levels of abstraction. In this paper, we shall reduce the error gap in Cell Delay estimation for a placed gate-level netlist. We will generate the post-placed netlist from two different Siemens EDA tools. The purpose is to improve the accuracy of the cell delays of Oasys-RTL Synthesis tool, based on accurate cell delays from Aprisa PnR. We have trained and tested various Machine Learning models on several 16 nm designs. We achieved the highest accuracy using the Random Forest model, where the average accuracy is 91.25%. Furthermore, as the accuracy of the Cell delay is improved, the average Root-Mean-Square-Error (RMSE) is reduced from 16.958 to 4.469.
- HTML: `html/25.html`
- JSON: `metadata/meatdatagenerated/json/25.json`

## 19. AVATAR: An Aging- and Variation-Aware Dynamic Timing Analyzer for Error-Efficient Computing

- Source file: `26.pdf`
- Authors: Zuodong Zhang , Zizheng Guo , Yibo Lin , Member, IEEE, Meng Li, Member, IEEE, Runsheng Wang , Member, IEEE, and Ru Huang, Fellow, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2023
- DOI: 10.1109/TCAD.2023.3255167
- Pages: 13
- Citation: Zuodong Zhang , Zizheng Guo , Yibo Lin , Member, IEEE, Meng Li, Member, IEEE, Runsheng Wang , Member, IEEE, and Ru Huang, Fellow, IEEE (2023). AVATAR: An Aging- and Variation-Aware Dynamic Timing Analyzer for Error-Efficient Computing. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2023.3255167
- Abstract: As the timing guardband consumes more and more design margin with the technology scaling, better-than-worst-case (BTWC) techniques have gained more attention as a promising solution. BTWC techniques can relax the design margin by transcending the pessimistic static timing constraints and utilizing the dynamic timing information. However, to guarantee the design reliability throughout the lifetime, the conventional dynamic timing analysis (DTA) engines need an extra reliability guardband, which is commonly evaluated under the worst-case corners of aging and variation. This type of guardbanding consumes the precious design margin, thus hindering the efficiency improvement from BTWC techniques. Therefore, in this article, we propose AVATAR, an aging- and variation-aware dynamic timing analyzer that can perform DTA with the impact of transistor aging and random process variation, including the gate-level aging analysis and random variation model that can accurately calculate cell delay under the impact of transistor aging and random variation, and an event-based DTA algorithm that avoids the pessimistic property of graph-based analysis. We also propose a machine learning (ML)-assisted DTA acceleration flow for the multicycle DTA of homogeneous multicore designs. We present two case studies using AVATAR to show its effectiveness. First, we present an application-based dynamic-voltage-frequency-scaling (DVFS) design methodology based on AVATAR, which can exploit application-level dynamic timing slack (DTS) to improve energy efficiency and performance. The results demonstrate that, compared to the design based on the conventional corner-based DTA, the additional performance improvement of the design based on AVATAR can be up to 14% or the additional power-saving can be up to 20%. Second, we demonstrate using the proposed ML-assisted acceleration flow for reliability-aware deep neural network (DNN) accelerator simulation. We use the proposed flow to estimate the impact of timing errors due to aging and random Manuscript received 28 September 2022; revised 9 January 2023; accepted 3 March 2023. Date of publication 9 March 2023; date of current version 20 October 2023. This work was supported in part by the National Key Research and Development Program under Grant 2020YFB2205500; in part by NSFC under Grant 62125401, Grant 62141404, and Grant 62034007; and in part by the 111 Project under Grant B18001. This preliminary version, titled “AVATAR: An Aging- and Variation-Aware Dynamic Timing Analyzer for Application-based DVAFS,” has been presented at the Design Automation Conference (DAC) in 2022 [DOI: 10.1145/3489517.3530530]. This article was recommended by Associate Editor C. Maneux. (Corresponding authors: Yibo Lin; Meng Li.) Zuodong Zhang and Zizheng Guo are with the School of Integrated Circuits, Peking University, Beijing 100871, China. Yibo Lin, Runsheng Wang, and Ru Huang are with the School of Integrated Circuits and the Institute of Electronic Design Automation, Peking University, Wuxi 214028, China, and also with the Beijing Advanced Innovation Center for Integrated Circuits, Beijing 100871, China (e-mail: yibolin@pku.edu.cn). Meng Li is with the School of Integrated Circuits and the Institute for Artificial Intelligence, Peking University, Beijing 100871, China (e-mail: meng.li@pku.edu.cn). Digital Object Identifier 10.1109/TCAD.2023.3255167
- HTML: `html/26.html`
- JSON: `metadata/meatdatagenerated/json/26.json`

## 20. Early RTL delay prediction using neural networks

- Source file: `27.pdf`
- Authors: Daniela Sánchez Lopera
- Journal: Microprocessors and Microsystems
- Year: 2022
- DOI: 10.1016/j.micpro.2022.104671
- Pages: 11
- Citation: Daniela Sánchez Lopera (2022). Early RTL delay prediction using neural networks. Microprocessors and Microsystems. https://doi.org/10.1016/j.micpro.2022.104671
- Abstract: Nowadays, the digital chip design flow starts with formal specifications, which are mapped to Register Transfer Level (RTL) models using different underlying (micro-) architectures. By doing so, a hardware designer predicts and resolves time-critical parts to achieve an RTL-design that meets all constraints after synthesis. However, wrong predictions can be detected only later in the design flow, thus leading to long design iterations. Classical methods estimating delay in early design stages are constrained to the type of components or are computationally expensive for larger designs. This paper proposes a machine learningbased approach to estimate pin-to-pin delays for RTL combinational circuits. To improve the quality of the predictions we combine slew and delay estimation. To that end, training data are built using features of components generated by a model-driven hardware generator framework. Ground truth labels for delays, slews, and their interdependencies are extracted using open-source tools for logic synthesis and static timing analysis. Two different datasets are built: one targeting logic gates and multiplexers and an enlarged one, which generalizes to more RTL primitives A model trained using the former dataset achieves, on average, a coefficient of determination R2 of 87% when evaluating over 4-bit prefix adders. Using the enlarged dataset, the best model reaches an R2 of 77%. On average, our models are 8.4× faster w.r.t the time required to run synthesis and timing analysis. Results show that generalizing to more primitives decreases the models’ performance, but the runtime benefit is maintained. Based on the delay estimation, critical areas of the design can be detected and proper microarchitecture decisions can be taken earlier and faster in the design flow.
- HTML: `html/27.html`
- JSON: `metadata/meatdatagenerated/json/27.json`

## 21. Machine-Learning-Based Multi-Corner Timing Prediction for Faster Timing Closure

- Source file: `28.pdf`
- Authors: Zhenyu Zhao, Shuzheng Zhang, Guoqiang Liu, Chaochao Feng, Tianhao Yang, Ao Han and Lei Wang
- Journal: For the purpose of fixing timing violations
- Year: 2022
- DOI: 10.3390/electronics11101571
- Pages: 15
- Citation: Zhenyu Zhao, Shuzheng Zhang, Guoqiang Liu, Chaochao Feng, Tianhao Yang, Ao Han and Lei Wang (2022). Machine-Learning-Based Multi-Corner Timing Prediction for Faster Timing Closure. For the purpose of fixing timing violations. https://doi.org/10.3390/electronics11101571
- Abstract: For the purpose of fixing timing violations, static timing analysis (STA) of full-corners is repeatedly executed, which is time-consuming. Given a timing path, timing results at some corners (“dominant corners”) are utilized to predict timing at other corners (“non-dominant corners”), which can greatly shorten the runtime of STA. However, the huge number of combinations of the dominant corners and the wide difference in prediction accuracy make it difficult to apply multi-corner timing prediction to chip industrial design. In this paper, we propose a dominant corner selection strategy to quickly determine the dominant corner combination with high prediction accuracy, along with which a new multi-corner timing prediction process is established to speed up STA. Experimental results show that our method can not only effectively accelerate STA, but also ensure the high prediction accuracy of the prediction timing. On the public ITC’99 benchmark, the prediction accuracy of the dominant corner combination selected by the proposed method is up to 98.2%, which is an improvement of 15% compared to the state-of-the-art method. For industrial application, we apply our method by using timing results on only 2 dominant corners to predict the other 12 non-dominant corners, which accelerates the runtime of the timing closure process by more than 2×. Citation: Zhao, Z.; Zhang, S.; Liu, G.; Feng, C.; Yang, T.; Han, A.; Wang, L.
- HTML: `html/28.html`
- JSON: `metadata/meatdatagenerated/json/28.json`

## 22. Preplacement Net Length and Timing Estimation by Customized Graph Neural Network

- Source file: `29.pdf`
- Authors: Zhiyao Xie , Rongjian Liang , Xiaoqing Xu, Member, IEEE, Jiang Hu, Fellow, IEEE, Chen-Chia Chang, Jingyu Pan , Graduate Student Member, IEEE, and Yiran Chen , Fellow, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2022
- DOI: 10.1109/TCAD.2022.3149977
- Pages: 14
- Citation: Zhiyao Xie , Rongjian Liang , Xiaoqing Xu, Member, IEEE, Jiang Hu, Fellow, IEEE, Chen-Chia Chang, Jingyu Pan , Graduate Student Member, IEEE, and Yiran Chen , Fellow, IEEE (2022). Preplacement Net Length and Timing Estimation by Customized Graph Neural Network. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2022.3149977
- Abstract: Net length is a key proxy metric for optimizing timing and power across various stages of a standard digital design flow. However, the bulk of net length information is not available until cell placement, and hence, it is a significant challenge to explicitly consider net length optimization in design stages prior to placement, such as logic synthesis. In addition, the absence of net length information makes accurate preplacement timing estimation extremely difficult. Poor predictability on the timing not only affects timing optimizations but also hampers the accurate evaluation of synthesis solutions. This work addresses these challenges by a preplacement prediction flow with estimators on both net length and timing. We propose a graph attention network (GAT) method with customization, called Net2, to estimate individual net length before cell placement. Its accuracy-oriented version Net2a achieves about 15% better accuracy than several previous works in identifying both long nets and long critical paths. Its fast version Net2f is more than 1000× faster than placement while still outperforms previous works and other neural network techniques in terms of various accuracy metrics. Based on net size estimations, we propose the first machine learning-based preplacement timing estimator. Compared with the preplacement timing report from commercial tools, it improves the correlation coefficient in arc delays by 0.08, and reduces the mean absolute error in slack, worst negative slack, and total negative slack estimations by more than 50%.
- HTML: `html/29.html`
- JSON: `metadata/meatdatagenerated/json/29.json`

## 23. Timing analysis algorithm using a neural network under PVT variations

- Source file: `30.pdf`
- Authors: Yan Liu
- Journal: Microelectronics Journal
- Year: 2022
- DOI: 10.1016/j.mejo.2022.105480
- Pages: 5
- Citation: Yan Liu (2022). Timing analysis algorithm using a neural network under PVT variations. Microelectronics Journal. https://doi.org/10.1016/j.mejo.2022.105480
- Abstract: Process-voltage-temperature variations result in an increase in logic gate delays, which further lead to timing violations. Because of the computational complexity of the operators such as max and sum in statistical static timing analysis, this paper proposes a timing analysis algorithm using neural network to evaluate circuit timing under the PVT variations. In the proposed algorithm, a neural network method is applied to model the mean or standard deviation of the gate delay. Then, a viability analysis method is introduced to recognize the true critical path. The simulation results on ISCAS89 benchmarks illustrate that compared with SPICE Monte Carlo simula tion, the error in the mean calculated by the proposed algorithm is less than 2%, and the error in the standard deviation is less than 3.64%. In addition, for s298, s344, s832, s1238 and s13207, the viability analysis algorithm achieves 1.04X, 1.01X, 2.77X, 1.62X and 4.48X speedup over full path search, respectively.
- HTML: `html/30.html`
- JSON: `metadata/meatdatagenerated/json/30.json`

## 24. Timing Analysis and Optimization Method with Interdependent Flip-Flop Timing Model for Near-Threshold Design

- Source file: `31.pdf`
- Authors: Peng Cao, Yuan Qin and Haiyang Jiang
- Journal: Near-threshold Voltage (NTV) design is receiving wide attention due to remarkable energy efficiency improvement at the cost of performance degradation. The interdependency between the setup–hold time and clock-to-q delay of flip-flops has been exploited in the Super-threshold Voltage (STV) domain to improve circuit performance but faces the severe challenge of nonlinear relationship and wider effective coverage in the NTV region
- Year: 2022
- DOI: 10.3390/electronics11223670
- Pages: 13
- Citation: Peng Cao, Yuan Qin and Haiyang Jiang (2022). Timing Analysis and Optimization Method with Interdependent Flip-Flop Timing Model for Near-Threshold Design. Near-threshold Voltage (NTV) design is receiving wide attention due to remarkable energy efficiency improvement at the cost of performance degradation. The interdependency between the setup–hold time and clock-to-q delay of flip-flops has been exploited in the Super-threshold Voltage (STV) domain to improve circuit performance but faces the severe challenge of nonlinear relationship and wider effective coverage in the NTV region. https://doi.org/10.3390/electronics11223670
- Abstract: Near-threshold Voltage (NTV) design is receiving wide attention due to remarkable energy efficiency improvement at the cost of performance degradation. The interdependency between the setup–hold time and clock-to-q delay of flip-flops has been exploited in the Super-threshold Voltage (STV) domain to improve circuit performance but faces the severe challenge of nonlinear relationship and wider effective coverage in the NTV region, which prevents the application of interdependent flip-flop model for timing analysis and optimization for NTV design. In this paper, a novel interdependent flip-flop timing model is proposed by Artificial Neural Network (ANN) to predict the clock-to-q delay with training data generated by SPICE simulation in a restricted hexagonal area of the two-dimensional setup-hold time space. By integrating the proposed model into Static Timing Analysis (STA) flow, a novel iterative optimization method is proposed to improve performance for NVT circuits based on a Genetic Algorithm (GA). The proposed timing analysis and optimization method were validated under Semiconductor Manufacturing International Corporation (SMIC) 40 nm process at the voltage of 0.6 V with the International Symposium on Circuits and Systems (ISCAS)’89 benchmark circuits. Experimental results demonstrate that the ANN-based interdependent timing model for flip-flop achieves considerable accurate prediction with the Mean Absolute Relative Error (MARE) of less than 0.69%. The minimum clock periods for ISCAS’89 benchmark circuits are reduced by 1.70~6.28% compared to traditional STA results without any setup and hold violations and hardware cost, which achieves at most 6.7% performance improvement for NTV design. 2022, 11, 3670. https://doi.org/ 10.3390/electronics11223670
- HTML: `html/31.html`
- JSON: `metadata/meatdatagenerated/json/31.json`

## 25. Statistical gate-delay modeling with copulas

- Source file: `32.pdf`
- Authors: Walter Schneider
- Journal: Microelectronics Journal
- Year: 2020
- DOI: 10.1016/j.mejo.2020.104938
- Pages: 10
- Citation: Walter Schneider (2020). Statistical gate-delay modeling with copulas. Microelectronics Journal. https://doi.org/10.1016/j.mejo.2020.104938
- Abstract: The growing impact of process variations on circuit performance has become a major concern for deep-submicron integrated circuit design, resulting in numerous SSTA-algorithms. The acceptance of such algorithms in industry however will be dependent on modeling the real silicon behavior in SSTA. This includes that the statistical gate-delay models must consider arbitrary process variations and dependencies. In this paper, we introduce the innovative concept of Copulas to handle this topic. A complete Matlab based framework starting from process parameter statistics up to the computation of the statistical gate-delay distribution is presented. Experimental results demonstrate the importance of accounting realistic process variations.
- HTML: `html/32.html`
- JSON: `metadata/meatdatagenerated/json/32.json`

## 26. electronics Article Novel Prediction Framework for Path Delay Variation Based on Learning Method Jingjing Guo , Peng Cao , Zhaohao Sun, Bingqian Xu, Zhiyuan Liu and Jun Yang *

- Source file: `33.pdf`
- Authors: Not reliably extracted
- Journal: Not reliably extracted
- Year: 2019
- DOI: 10.3390/electronics9010157
- Pages: 11
- Citation: (2019). electronics Article Novel Prediction Framework for Path Delay Variation Based on Learning Method Jingjing Guo , Peng Cao , Zhaohao Sun, Bingqian Xu, Zhiyuan Liu and Jun Yang *. https://doi.org/10.3390/electronics9010157
- Abstract: Path delay variation becomes a serious concern in advanced technology, especially for multi-corner conditions. Plenty of timing analysis methods have been proposed to solve the issue of path delay variation, but they mainly focus on every single corner and are based on a characterized timing library, which neglects the correlation among multiple corners, resulting in a high characterization effort for all required corners. Here, a novel prediction framework is proposed for path delay variation by employing a learning-based method using back propagation (BP) regression. It can be used to solve the issue of path delay variation prediction under a single corner. Moreover, for multi-corner conditions, the proposed framework can be further expanded to predict corners that are not included in the training set. Experimental results show that the proposed model outperforms the traditional Advanced On-Chip Variation (AOCV) method with 1.4X improvement for the prediction of path delay variation for single corners. Additionally, while predicting new corners, the maximum error is 4.59%, which is less than current state-of-the-art works.
- HTML: `html/33.html`
- JSON: `metadata/meatdatagenerated/json/33.json`

## 27. NN-SSTA: A deep neural network approach for statistical static timing analysis

- Source file: `34.pdf`
- Authors: M. Amin Savari
- Journal: Expert Systems With Applications
- Year: 2020
- DOI: 10.1016/j.eswa.2020.113309
- Pages: 20
- Citation: M. Amin Savari (2020). NN-SSTA: A deep neural network approach for statistical static timing analysis. Expert Systems With Applications. https://doi.org/10.1016/j.eswa.2020.113309
- Abstract: Discrete statistical static timing analysis (SSTA) performs the timing analysis by using statistical maximum and convolution operations. The maximum is basically a non-linear operator and it is not a simple task to capture the skewness introduced by it. On the other hand, the convolution has a potential to “blow-up” the number of discrete samples as we going deep inside the timing graph and hence, results in exponential timing complexity. Therefore, in this paper we present novel deep neural network based operations which can accurately approximate the signal arrival-time’s distributions with linear-time complexity. The various deep neural network (DNN) architectures have been used to implement both the maximum and the convolution operations using proper training dataset. Simulation results on various benchmark circuits (ISCAS 85, ISCAS 89, and ITC 99) show that the proposed method estimate the mean and standard deviation (STD) of critical path delay distribution with an average error of 0.75% and 2.56% as compared to Monte Carlo (MC), respectively. Our SSTA speeds up the traditional discrete approach by a factor of 20.7x on average. Furthermore, the PDF obtained from our method matches the ones obtained from MC with a reasonable error. Furthermore, we have proposed multi-wise maximum operations to reduce the arrival-time computational complexity at multi-inputs gates. Comparing to MC, the proposed method shows 0.97% and 2.58% average error in mean and STD respectively and the speeding up factor reaches 24.4x on average for all benchmarks. © 2020 Elsevier Ltd. All rights reserved.
- HTML: `html/34.html`
- JSON: `metadata/meatdatagenerated/json/34.json`

## 28. Adjacency criticality: a simple yet effective metric for statistical timing yield optimisation of digital integrated circuits

- Source file: `35.pdf`
- Authors: ISSN 1751-858X Received on 24th December 2018 Revised 3rd April 2019 Accepted on 7th May 2019 E-First on 22nd October 2019 doi: 10.1049/iet-cds.2018.5616 www.ietdl.org
- Journal: IET Circuits
- Year: 2019
- DOI: 10.1049/iet-cds.2018.5616
- Pages: 9
- Citation: ISSN 1751-858X Received on 24th December 2018 Revised 3rd April 2019 Accepted on 7th May 2019 E-First on 22nd October 2019 doi: 10.1049/iet-cds.2018.5616 www.ietdl.org (2019). Adjacency criticality: a simple yet effective metric for statistical timing yield optimisation of digital integrated circuits. IET Circuits. https://doi.org/10.1049/iet-cds.2018.5616
- Abstract: As CMOS devices become smaller, process variations-induced uncertainty imposes a large spread in the circuit timing and therefore, it becomes one of the main issues for circuit yield. To analyse/optimise the timing of the circuit under process variation effects, statistical analysis/optimisation techniques are more suitable than the traditional static analysis/ optimisation counterparts. Statistical gate sizing is an effective technique that is widely used to guide the timing yield improvement of digital circuits. Gate criticality, defined as the probability that a gate lies on a critical path, forms the basis for many of the existing statistical gate sizing techniques. Here, the authors introduce adjacency criticality to address the drawbacks of the conventional definition of gate criticality. It is defined as the probability of manufacturing a chip in which the gate lies on the critical path due to process variation considering the effect of the gates in its fan-out cone. Furthermore, the authors present the levelised Adjacency Criticality metric which provides a trade-off between the runtime of the criticality metric and accuracy of the Adjacency Criticality metric. In order to show the efficacy of the proposed metric, an adjacency criticalitybased statistical gate sizing method is presented for improving timing yield of the circuit.
- HTML: `html/35.html`
- JSON: `metadata/meatdatagenerated/json/35.json`

## 29. An Analytical Gate Delay Model in Near/Subthreshold Domain Considering Process Variation

- Source file: `36.pdf`
- Authors: Not reliably extracted
- Journal: IEEE Access
- Year: 2019
- DOI: 10.1109/ACCESS.2019.2955091
- Pages: 10
- Citation: (2019). An Analytical Gate Delay Model in Near/Subthreshold Domain Considering Process Variation. IEEE Access. https://doi.org/10.1109/ACCESS.2019.2955091
- Abstract: Abstract not cleanly detected.
- HTML: `html/36.html`
- JSON: `metadata/meatdatagenerated/json/36.json`

## 30. Calculated Risks: Quantifying Timing Error Probability With Extended Static Timing Analysis

- Source file: `37.pdf`
- Authors: Kevin E. Murray , Student Member, IEEE, Andrea Suardi, Vaughn Betz, Senior Member, IEEE, and George Constantinides, Senior Member, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2019
- DOI: 10.1109/TCAD.2018.2821563
- Pages: 14
- Citation: Kevin E. Murray , Student Member, IEEE, Andrea Suardi, Vaughn Betz, Senior Member, IEEE, and George Constantinides, Senior Member, IEEE (2019). Calculated Risks: Quantifying Timing Error Probability With Extended Static Timing Analysis. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2018.2821563
- Abstract: Timing analysis is a key step in the digital design process. By modeling device delay variations statistical static timing analysis (SSTA) reduces pessimism compared to traditional static timing analysis (STA). However, it ignores the circuit’s logic which causes some timing paths to never, or only rarely, be sensitized. We introduce a general timing analysis approach and tool to calculate the probability that individual timing paths are sensitized, enabling the calculation of bounding delay distributions over all input combinations. We show how this analysis is related to the well-known #SAT problem and present approaches to improve scalability, achieving, on average, results 75% to 37% less pessimistic than STA while running 569 to 16 times faster than Monte-Carlo timing simulation.
- HTML: `html/37.html`
- JSON: `metadata/meatdatagenerated/json/37.json`

## 31. Potential Critical Path Selection Based on a Time-Varying Statistical Timing Analysis Framework

- Source file: `38.pdf`
- Authors: P. R. Chithira , Student Member, IEEE, and Vinita Vasudevan, Member, IEEE
- Journal: IEEE Transactions on Very Large Scale Integration (VLSI) Systems
- Year: 2019
- DOI: 10.1109/TVLSI.2019.2893020
- Pages: 12
- Citation: P. R. Chithira , Student Member, IEEE, and Vinita Vasudevan, Member, IEEE (2019). Potential Critical Path Selection Based on a Time-Varying Statistical Timing Analysis Framework. IEEE Transactions on Very Large Scale Integration (VLSI) Systems. https://doi.org/10.1109/TVLSI.2019.2893020
- Abstract: Negative bias temperature instability along with the presence of process variations has resulted in time-varying path criticalities. To ensure reliable circuit operation, aging sensors are used at the end of potential critical paths (PCPs) for delay monitoring. Optimization of the number of delay sensors requires accurate computational models for prediction of criticality and selection of PCPs. We identify a path as a PCP if its maximum global criticality over the lifetime exceeds a certain threshold. However, the global criticality of a path could vary nonmonotonically over the lifetime of the device. In this paper, we propose a framework for time-varying statistical static timing analysis (TV-SSTA), wherein the circuit delay is obtained as a collection of time-varying canonicals with breakpoints in time which define the end of validity of one and the start of the next canonical. We show that the global criticality of any path will be maximum either at t = 0 or at these breakpoints. Hence, criticality computation and PCP selection need to be done only at these time points, which typically is less than four. The TV-SSTA is integrated with a previously proposed criticality computation technique to identify the PCPs and the results are validated against Monte Carlo simulations.
- HTML: `html/38.html`
- JSON: `metadata/meatdatagenerated/json/38.json`

## 32. 20_01.dvi

- Source file: `39.pdf`
- Authors: Not reliably extracted
- Journal: IPSJ Transactions on System LSI Design Methodology Vol.11 2–15 (Feb. 2018)
- Year: 2018
- DOI: 10.2197/ipsjtsldm.11.2
- Pages: 14
- Citation: (2018). 20_01.dvi. IPSJ Transactions on System LSI Design Methodology Vol.11 2–15 (Feb. 2018). https://doi.org/10.2197/ipsjtsldm.11.2
- Abstract: In advanced technology nodes, transistors and interconnects with shrinking physical dimensions suffer large process variations during manufacturing and are prone to reliability issues. These underlying changes require an overhaul of the design methodologies for digital circuits. In this paper, we provide an overview of techniques introduced recently to analyze the effect of uncertainty in manufacturing and reliability issues of devices due to the diminishing feature size. These techniques range from variation/aging modeling to circuit-level analysis. In addition, active techniques to counter these effects, such as clock skew tuning and voltage tuning are also covered in this paper.
- HTML: `html/39.html`
- JSON: `metadata/meatdatagenerated/json/39.json`

## 33. untitled

- Source file: `40.pdf`
- Authors: Not reliably extracted
- Journal: 2668 IEEE TRANSACTIONS ON VERY LARGE SCALE INTEGRATION (VLSI) SYSTEMS, VOL. 25, NO. 9, SEPTEMBER 2017
- Year: 2017
- DOI: Not found
- Pages: 5
- Citation: (2017). untitled. 2668 IEEE TRANSACTIONS ON VERY LARGE SCALE INTEGRATION (VLSI) SYSTEMS, VOL. 25, NO. 9, SEPTEMBER 2017.
- Abstract: In this brief, we propose an effective adaptation of viability analysis in statistical static timing analysis. The adaption benefits well from a dynamic programming implementation of the viability function. For a rapid identification of statistical longest true paths, the technique makes use of a fast preprocessing step identifying the gates with a small probability of being viable in the circuit, and a number of simple optimization techniques. This makes the approach fast without lowering its accuracy. The efficacy of the proposed statistical timing analysis is assessed using ISCAS benchmark circuits and carry skip adders. The results show that the proposed technique leads to, on average, 18× higher speed compared to those of the state-of-the-art technique. This improvement is achieved at the cost of −1.7% precision lost compared to that of the Monte-Carlo method.
- HTML: `html/40.html`
- JSON: `metadata/meatdatagenerated/json/40.json`

## 34. Stochastic logical effort as a variation aware delay model to estimate timing yield

- Source file: `41.pdf`
- Authors: Alp Arslan Bayrakci
- Journal: Integration
- Year: 2014
- DOI: 10.1016/j.vlsi.2014.07.003
- Pages: 8
- Citation: Alp Arslan Bayrakci (2014). Stochastic logical effort as a variation aware delay model to estimate timing yield. Integration. https://doi.org/10.1016/j.vlsi.2014.07.003
- Abstract: Article history: Received 18 July 2013 Received in revised form 27 July 2014 Accepted 29 July 2014 Available online 8 August 2014 Considerable effort has been expended in the EDA community during the past decade in trying to cope with the so-called statistical timing problem. In this paper, we not only present a fast and approximate gate delay model called stochastic logical effort (SLE) to capture the effect of statistical parameter variations on the delay but also combine this model with a previously proposed transistor level smart Monte Carlo method to construct ISLE timing yield estimator. The results demonstrate that our approximate SLE model can capture the delay variations and ISLE achieves the same accuracy as the standard Monte Carlo estimator with a cost reduction of about 180  on the average for ISCAS’85 benchmark circuits and in the existence of both inter- and intra-die variations. & 2014 Elsevier B.V. All rights reserved.
- HTML: `html/41.html`
- JSON: `metadata/meatdatagenerated/json/41.json`

## 35. A gate-delay model focusing on current fluctuation over wide range of process–voltage–temperature variations

- Source file: `42.pdf`
- Authors: Ken-ichi Shinkai
- Journal: Integration
- Year: 2013
- DOI: 10.1016/j.vlsi.2013.01.003
- Pages: 14
- Citation: Ken-ichi Shinkai (2013). A gate-delay model focusing on current fluctuation over wide range of process–voltage–temperature variations. Integration. https://doi.org/10.1016/j.vlsi.2013.01.003
- Abstract: Article history: Received 20 February 2011 Received in revised form 14 September 2012 Accepted 19 January 2013 Available online 5 February 2013 This paper proposes a gate-delay model suitable for timing analysis that takes into consideration wideranging process–voltage–temperature (PVT) variations. The proposed model translates an outputcurrent fluctuation due to PVT variations into modifications of the output load and input waveform. After translation, any conventional model can compute delay taking into account PVT variations by using the modified output load and reshaped input waveform. Experimental results with 90- and 45-nm technologies demonstrate that the average error of the fall and rise delay estimation in single- and multi-stage gates was approximately 5% on average over a wide range of input slews, output loads, and PVT variations. The proposed model can be used in Monte Carlo STA (static timing analysis) in addition to corner-based timing analysis. It can be also used in statistical STA to calculate the sensitivities of delays to variation parameters on-the-fly even when the nominal operating condition changes as well. & 2013 Elsevier B.V. All rights reserved.
- HTML: `html/42.html`
- JSON: `metadata/meatdatagenerated/json/42.json`

## 36. On Timing Model Extraction and Hierarchical Statistical Timing Analysis

- Source file: `43.pdf`
- Authors: Bing Li, Ning Chen, Yang Xu, and Ulf Schlichtmann, Member, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2013
- DOI: 10.1109/TCAD.2012.2228305
- Pages: 14
- Citation: Bing Li, Ning Chen, Yang Xu, and Ulf Schlichtmann, Member, IEEE (2013). On Timing Model Extraction and Hierarchical Statistical Timing Analysis. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2012.2228305
- Abstract: In this paper, we investigate the challenges of applying statistical static timing analysis in hierarchical design flow, where modules supplied by IP vendors are used to hide design details for IP protection and to reduce the complexity of design and verification. For the three basic circuit types, combinational, flip-flop-based, and latch-controlled, we propose methods for extracting timing models that contain interfacing and compressed internal constraints. Using these compact timing models, the runtime of full-chip timing analysis can be reduced, while circuit details from IP vendors are not exposed. We also propose a method for reconstructing correlation between modules during full-chip timing analysis. This correlation cannot be incorporated into timing models because it depends on the layout of the corresponding modules in the chip. In addition, we investigate how to apply the extracted timing models with the reconstructed correlation to evaluate the performance of the complete design. Experiments demonstrate that using the extracted timing models and reconstructed correlation full-chip timing analysis can be several times faster than applying the flattened circuit directly, while the accuracy of statistical timing analysis is still well maintained.
- HTML: `html/43.html`
- JSON: `metadata/meatdatagenerated/json/43.json`

## 37. The Impact of BTI Variations on Timing in Digital Logic Circuits

- Source file: `44.pdf`
- Authors: Jianxin Fang and Sachin S. Sapatnekar, Fellow, IEEE
- Journal: IEEE Transactions on Device and Materials Reliability
- Year: 2013
- DOI: 10.1109/TDMR.2013.2237910
- Pages: 10
- Citation: Jianxin Fang and Sachin S. Sapatnekar, Fellow, IEEE (2013). The Impact of BTI Variations on Timing in Digital Logic Circuits. IEEE Transactions on Device and Materials Reliability. https://doi.org/10.1109/TDMR.2013.2237910
- Abstract: A new framework for analyzing the impact of bias temperature instability (BTI) variations on timing in large-scale digital logic circuits is proposed in this paper. This approach incorporates both the reaction–diffusion model and the chargetrapping model for BTI and embeds these into a temporal statistical static timing analysis framework capturing process variations and path correlations. Experimental results on 32-, 22-, and 16-nm technology models, which were verified through Monte Carlo simulation, confirm that the proposed approach is fast, accurate, and scalable and indicate that BTI variations make a significant contribution to circuit-level timing variations.
- HTML: `html/44.html`
- JSON: `metadata/meatdatagenerated/json/44.json`

## 38. Delay-correlation-aware SSTA based on conditional moments

- Source file: `45.pdf`
- Authors: Zeqin Wu
- Journal: Microelectronics Journal
- Year: 2012
- DOI: 10.1016/j.mejo.2012.01.003
- Pages: 11
- Citation: Zeqin Wu (2012). Delay-correlation-aware SSTA based on conditional moments. Microelectronics Journal. https://doi.org/10.1016/j.mejo.2012.01.003
- Abstract: Article history: Received 28 June 2011 Received in revised form 5 January 2012 Accepted 6 January 2012 Available online 25 January 2012 Corner-based Timing Analysis (CTA) becomes more and more pessimistic as feature size shrinks. This trend has motivated the development of Statistical Static Timing Analysis (SSTA). In this paper, we propose a new path-based SSTA framework that allows the estimation of path delay distributions and delay correlations by propagating iteratively mean and variance of cell delay. These moments, conditioned on input slope and output load values, are pre-characterized by an improved method: log-logistic distribution based input signals and inverters as output load. In applications, the delay gains of this SSTA framework with respect to CTA are shown to be significant. It is also highlighted that the discrepancy of critical paths orderings obtained by SSTA and CTA depends on two factors: cell-tocell delay correlation and standard deviation of cell delay. & 2012 Elsevier Ltd. All rights reserved.
- HTML: `html/45.html`
- JSON: `metadata/meatdatagenerated/json/45.json`

## 39. Utilizing interdependent timing constraints to enhance robustness in synchronous circuits

- Source file: `46.pdf`
- Authors: E. Salman
- Journal: Microelectronics Journal
- Year: 2011
- DOI: 10.1016/j.mejo.2011.11.005
- Pages: 9
- Citation: E. Salman (2011). Utilizing interdependent timing constraints to enhance robustness in synchronous circuits. Microelectronics Journal. https://doi.org/10.1016/j.mejo.2011.11.005
- Abstract: Article history: Received 24 July 2011 Received in revised form 15 November 2011 Accepted 16 November 2011 Available online 3 December 2011 Interdependent setup-hold times are exploited during the design process to improve the robustness of a circuit. Considering this interdependence only during static timing analysis (STA), as demonstrated in the previous work, is insufficient to fully exploit the capabilities offered by interdependence. This result is due to the strong dependence of STA results on the specific circuit, cell library, and operating frequency. Interdependence is evaluated in this paper for several technologies to determine the overall reduction in delay uncertainty rather than improvements in STA. Reducing delay uncertainty produces a more robust synchronous circuit. The increasing efficacy of interdependence in deeply scaled technologies is also demonstrated by investigating the effect of technology scaling on interdependent timing constraints. & 2011 Elsevier Ltd. All rights reserved.
- HTML: `html/46.html`
- JSON: `metadata/meatdatagenerated/json/46.json`

## 40. Fast Statistical Static Timing Analysis Using Smart Monte Carlo Techniques

- Source file: `47.pdf`
- Authors: Vineeth Veetil, Kaviraj Chopra, David Blaauw, Senior Member, IEEE, and Dennis Sylvester, Fellow, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2011
- DOI: 10.1109/TCAD.2011.2108030
- Pages: 14
- Citation: Vineeth Veetil, Kaviraj Chopra, David Blaauw, Senior Member, IEEE, and Dennis Sylvester, Fellow, IEEE (2011). Fast Statistical Static Timing Analysis Using Smart Monte Carlo Techniques. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2011.2108030
- Abstract: In this paper, we propose a stratification+hybrid quasi Monte Carlo (SH-QMC) approach to improve the efficiency of Monte Carlo-based statistical static timing analysis (SSTA) using sample size reduction. Sample size reduction techniques proposed in the literature exhibit a tradeoff between accuracy of the Monte Carlo estimate with fewer samples and their ability to handle large number of variables in multidimensional space. This paper proposes to target several such techniques to different sets of process variation variables by using information about the importance of these variables to the circuit delay, and the capability of the techniques to handle multiple dimensions. Simulations on benchmark circuits up to 90 K gates show that the proposed method requires up to 224 samples for varying levels of process variation to achieve accurate timing estimates. Results also show that when SH-QMC is performed with multiple parallel threads on a quad-core processor, the approach is faster than traditional SSTA with comparable accuracy. When the proposed SH-QMC technique is supplemented with a graph pruning method the runtime is further reduced by 46–48% on average. The technique is also extended to include an incremental approach to recompute a percentile delay metric after engineering change order.
- HTML: `html/47.html`
- JSON: `metadata/meatdatagenerated/json/47.json`

## 41. FA-STAC: An Algorithmic Framework for Fast and Accurate Coupling Aware Static Timing Analysis

- Source file: `48.pdf`
- Authors: Debasish Das, Student Member, IEEE, Ahmed Shebaita, Hai Zhou, Senior Member, IEEE, Yehea Ismail, Senior Member, IEEE, and Kip Killpack
- Journal: IEEE Transactions on Very Large Scale Integration (VLSI) Systems
- Year: 2011
- DOI: 10.1109/TVLSI.2009.2035323
- Pages: 14
- Citation: Debasish Das, Student Member, IEEE, Ahmed Shebaita, Hai Zhou, Senior Member, IEEE, Yehea Ismail, Senior Member, IEEE, and Kip Killpack (2011). FA-STAC: An Algorithmic Framework for Fast and Accurate Coupling Aware Static Timing Analysis. IEEE Transactions on Very Large Scale Integration (VLSI) Systems. https://doi.org/10.1109/TVLSI.2009.2035323
- Abstract: This paper presents an algorithmic framework for fast and accurate static timing analysis considering coupling. With technology scaling to smaller dimensions, the impact of coupling induced delay variations can no longer be ignored. Timing analysis considering coupling is iterative, and can have considerably larger run-times than a single pass approach. We propose two different classes of coupling delay models: heuristic-based coupling model and current source-based coupling model, and present techniques to increase the convergence rate of timing analysis when such coupling models are employed. Our proposed coupling model show promising accuracy improvements compared to SPICE. Experimental results on ISCAS85 benchmarks validates the effectiveness of our efficient iteration scheme. Our iteration algorithm obtained speedups of up to 62.1% using a heuristic coupling model while 2.7 using a current-based coupling model in comparison to traditional approaches.
- HTML: `html/48.html`
- JSON: `metadata/meatdatagenerated/json/48.json`

## 42. doi:10.1016/j.vlsi.2008.10.002

- Source file: `49.pdf`
- Authors: Cristiano Forzan; Davide Pandini
- Journal: INTEGRATION, the VLSI journal 42 (2009) 409–435
- Year: 2009
- DOI: Not found
- Pages: 27
- Citation: Cristiano Forzan; Davide Pandini (2009). doi:10.1016/j.vlsi.2008.10.002. INTEGRATION, the VLSI journal 42 (2009) 409–435.
- Abstract: As the device and interconnect physical dimensions decrease steadily in modern nanometer silicon technologies, the ability to control the process and environmental variations is becoming more and more difficult. As a consequence, variability is a dominant factor in the design of complex system-onchip (SoC) circuits. A solution to the problem of accurately evaluating the design performance with variability is statistical static timing analysis (SSTA). Starting from the probability distributions of the process parameters, SSTA allows to accurately estimating the probability distribution of the circuit performance in a single timing analysis run. An excellent survey on SSTA was recently published [D. Blaauw, K. Chopra, A. Srivastava, L. Scheffer, Statistical timing analysis: from basic principles to state of the art, IEEE Trans. Computer-Aided Design 27 (2008) 589–607], where the authors presented a general overview of the subject and provided a comprehensive list of references. The purpose of this survey is complementary with respect to Blaauw et al. (2008), and presents the reader a detailed description of the main sources of process variation, as well as a more in-depth review and analysis of the most important algorithms and techniques proposed in the literature that have been applied for an accurate and efficient statistical timing analysis. & 2008 Elsevier B.V. All rights reserved.
- HTML: `html/49.html`
- JSON: `metadata/meatdatagenerated/json/49.json`

## 43. Slack in static timing analysis

- Source file: `50.pdf`
- Authors: J. Vygen
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2006
- DOI: 10.1109/TCAD.2005.858348
- Pages: 10
- Citation: J. Vygen (2006). Slack in static timing analysis. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2005.858348
- Abstract: The notion of slack is central in static timing analysis and very large scale integration (VLSI) design in general. Negative slack means that a timing constraint is violated, while a positive slack of x ps is intended to mean that an extra delay of x ps (or a smaller delay by x ps in early mode) could be tolerated. However, this property does not hold with the standard static timing analysis model. The paper defines slack properly, shows how to compute it efficiently, and proves that it has the intended properties. The proposed idea is based on enhanced slew propagation.
- HTML: `html/50.html`
- JSON: `metadata/meatdatagenerated/json/50.json`

## 44. A Machine Learning Approach to Improving Timing Consistency between Global Route and Detailed Route

- Source file: `3626959.pdf`
- Authors: Not reliably extracted
- Journal: ACM Trans. Des. Autom. Electron. Syst. 2024.29:1-25
- Year: 2024
- DOI: 10.1145/3626959
- Pages: 26
- Citation: (2024). A Machine Learning Approach to Improving Timing Consistency between Global Route and Detailed Route. ACM Trans. Des. Autom. Electron. Syst. 2024.29:1-25. https://doi.org/10.1145/3626959
- Abstract: Abstract not cleanly detected.
- HTML: `html/3626959.html`
- JSON: `metadata/meatdatagenerated/json/3626959.json`

## 45. Efficient Timing Prediction and Optimization Using Derivable Gradient Boosting Machine Model at Placement Stage

- Source file: `3780100.pdf`
- Authors: Not reliably extracted
- Journal: ACM Trans. Des. Autom. Electron. Syst. 0.0
- Year: 2026
- DOI: 10.1145/3780100
- Pages: 21
- Citation: (2026). Efficient Timing Prediction and Optimization Using Derivable Gradient Boosting Machine Model at Placement Stage. ACM Trans. Des. Autom. Electron. Syst. 0.0. https://doi.org/10.1145/3780100
- Abstract: Abstract not cleanly detected.
- HTML: `html/3780100.html`
- JSON: `metadata/meatdatagenerated/json/3780100.json`

## 46. Pre-Routing Slack Prediction Based on Graph Attention Network

- Source file: `automation-06-00020.pdf`
- Authors: Jinke Li, Jiahui Hu, Yue Wu and Xiaoyan Yang
- Journal: Static Timing Analysis (STA) plays a crucial role in realizing timing convergence of integrated circuits. In recent years
- Year: 2025
- DOI: 10.3390/automation6020020
- Pages: 15
- Citation: Jinke Li, Jiahui Hu, Yue Wu and Xiaoyan Yang (2025). Pre-Routing Slack Prediction Based on Graph Attention Network. Static Timing Analysis (STA) plays a crucial role in realizing timing convergence of integrated circuits. In recent years. https://doi.org/10.3390/automation6020020
- Abstract: Static Timing Analysis (STA) plays a crucial role in realizing timing convergence of integrated circuits. In recent years, there has been growing research on pre-routing timing prediction using Graph Neural Networks (GNNs). However, existing approaches struggle with scalability on large graphs and lack generalizability to new designs, limiting their applicability to large-scale, complex circuit problems. To address this issue, this paper proposes a timing engine based on Graph Attention Network (GAT) to predict the slack of timing endpoints. Firstly, our model computes net embeddings for each node prior to training using a gated self-attention module. Subsequently, inspired by the Nonlinear Delay Model (NLDM), the node embeddings are propagated through multiple levels by alternately applying net propagation layers and cell propagation layers. Evaluated on 21 real circuits, the framework achieved a 16.62% improvement in average R2 score for slack prediction and a 15.55% reduction in runtime compared to the state-of-the-art (SOTA) method.
- HTML: `html/automation-06-00020.html`
- JSON: `metadata/meatdatagenerated/json/automation-06-00020.json`

## 47. A GNN-Based Placement Optimization Guidance Framework by Physical and Timing Prediction

- Source file: `electronics-14-00329-v2.pdf`
- Authors: Peng Cao,Zhi Li and Wenjie Ding
- Journal: Placement is crucial in physical design flow with significant impact on later routability and ultimate manufacturability in terms of performance
- Year: 2024
- DOI: 10.3390/electronics14020329
- Pages: 12
- Citation: Peng Cao,Zhi Li and Wenjie Ding (2024). A GNN-Based Placement Optimization Guidance Framework by Physical and Timing Prediction. Placement is crucial in physical design flow with significant impact on later routability and ultimate manufacturability in terms of performance. https://doi.org/10.3390/electronics14020329
- Abstract: Placement is crucial in physical design flow with significant impact on later routability and ultimate manufacturability in terms of performance, power, and area (PPA), which may deviate from finding the optimal solution and/or lead to unnecessary iterations suffering from interleaved optimization steps and inaccurate PPA estimation. To solve this issue, we propose a physical- and timing-related placement optimization guidance framework which provides candidate gate sizing and buffer insertion solutions as well as a path group for potential violated paths based on graph neural networks (GNNs) to improve placement quality significantly and efficiently. Experimental results on the OpenCores benchmarks with 22 nm technology demonstrate that the proposed placement optimization guidance framework achieves up to 35.66% and 43.51% worst negative slack (WNS) and total negative slack (TNS) improvement and 52.17% reduction in the number of violating paths (NVP), which is beneficial to later routing stages with 2.33% wirelength decrease.
- HTML: `html/electronics-14-00329-v2.html`
- JSON: `metadata/meatdatagenerated/json/electronics-14-00329-v2.json`

## 48. PRO-TIME: Prerouting Optimization-Aware Timing Prediction via Multimodal Learning

- Source file: `J153-TCAD2025-PRO-TIME.pdf`
- Authors: Ziyi Wang , Siting Liu , Yuan Pu , Song Chen , Member, IEEE, Tsung-Yi Ho , Fellow, IEEE, and Bei Yu , Senior Member, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2025
- DOI: 10.1109/TCAD.2025.3569488
- Pages: 14
- Citation: Ziyi Wang , Siting Liu , Yuan Pu , Song Chen , Member, IEEE, Tsung-Yi Ho , Fellow, IEEE, and Bei Yu , Senior Member, IEEE (2025). PRO-TIME: Prerouting Optimization-Aware Timing Prediction via Multimodal Learning. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2025.3569488
- Abstract: Fast and accurate prerouting timing prediction is crucial in the very-large-scale integration (VLSI) design flow. Existing machine learning (ML)-assisted prerouting timing evaluators neglect the impact of timing optimization, which may render their approaches impractical in real circuit design flows. To address the challenges posed by timing optimization, we propose PRO-TIME, a prerouting optimization-aware timing prediction framework that is driven by multimodal learning. Specifically, we propose a novel endpoint embedding framework that integrates both netlist and layout information. A customized graph neural network (GNN) model is used for extracting endpoint-wise netlist information, which is motivated by the delay propagation process. Meanwhile, we apply the U-net model with a masking strategy to extract endpoint-wise layout information. Furthermore, we propose an adaptive layout mask adjustment scheme to boost performance by leveraging the layout information more effectively. Comprehensive experiments on large-scale RISC-V designs with advanced 7-nm technology node demonstrate the superiority of our model compared to the stateof-the-art prerouting timing evaluators.
- HTML: `html/J153-TCAD2025-PRO-TIME.html`
- JSON: `metadata/meatdatagenerated/json/J153-TCAD2025-PRO-TIME.json`

## 49. Prerouting Timing Prediction Across Different Technology Nodes

- Source file: `Prerouting_Timing_Prediction_Across_Different_Technology_Nodes.pdf`
- Authors: Xinyun Zhang , Binwu Zhu , Fangzhou Liu, Jiaxi Jiang, Ziyi Wang , Peng Xu , Hong Xu , Senior Member, IEEE, and Bei Yu , Senior Member, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2025
- DOI: 10.1109/TCAD.2024.3523426
- Pages: 14
- Citation: Xinyun Zhang , Binwu Zhu , Fangzhou Liu, Jiaxi Jiang, Ziyi Wang , Peng Xu , Hong Xu , Senior Member, IEEE, and Bei Yu , Senior Member, IEEE (2025). Prerouting Timing Prediction Across Different Technology Nodes. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2024.3523426
- Abstract: In the domain of very-large-scale integration (VLSI) design, the accuracy of prerouting timing prediction is of paramount importance for ensuring the performance and reliability of integrated circuits. Traditional methods based on machine learning necessitate the availability of extensive and high-quality datasets. However, this requirement poses significant challenges for advanced technology nodes due to the laborious and time-intensive nature of data preparation. To address this critical issue, we introduce a novel transfer learning framework that leverages data from preceding technology nodes to facilitate learning and prediction on the target node. Our methodology commences with the disentanglement and alignment of timing path features across different nodes, ensuring the preservation and effective translation of intrinsic timing path properties. Subsequently, we employ a Bayesian-based model to predict the arrival times of individual timing paths. This model is particularly adept at managing the high-variability inherent in arrival times and exhibits strong generalization capabilities to novel design scenarios. Moreover, we propose a new algorithm to reweight the preceding node data during training by estimating their transferability through the cell type distribution. We validate the efficacy of our proposed framework through comprehensive experimental evaluations, demonstrating successful transfer learning from 130 or 45 to 7-nm technology nodes. The results underscore the potential of our approach to significantly mitigate the dependency on extensive data preparation while maintaining high accuracy in timing prediction for cutting-edge VLSI designs.
- HTML: `html/Prerouting_Timing_Prediction_Across_Different_Technology_Nodes.html`
- JSON: `metadata/meatdatagenerated/json/Prerouting_Timing_Prediction_Across_Different_Technology_Nodes.json`

## 50. Sign-Off Timing Considerations via Concurrent Routing Topology Optimization

- Source file: `Sign-Off_Timing_Considerations_via_Concurrent_Routing_Topology_Optimization.pdf`
- Authors: Siting Liu , Ziyi Wang , Fangzhou Liu, Yibo Lin , Member, IEEE, Bei Yu , Senior Member, IEEE, and Martin D. F. Wong , Fellow, IEEE
- Journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- Year: 2025
- DOI: 10.1109/TCAD.2024.3506216
- Pages: 12
- Citation: Siting Liu , Ziyi Wang , Fangzhou Liu, Yibo Lin , Member, IEEE, Bei Yu , Senior Member, IEEE, and Martin D. F. Wong , Fellow, IEEE (2025). Sign-Off Timing Considerations via Concurrent Routing Topology Optimization. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems. https://doi.org/10.1109/TCAD.2024.3506216
- Abstract: Timing closure is considered across the circuit design flow. Generally, the early stage timing optimization can only focus on improving early timing metrics, e.g., rough timing estimation using linear RC model or prerouting path length, since obtaining sign-off performance needs a time-consuming routing flow. However, there is no consistency guarantee between early stage metrics and sign-off timing performance. Therefore, we utilize the power of deep learning techniques to bridge the gap between the early stage analysis and the sign-off analysis. A well-designed deep learning framework guides the adjustment of Steiner points to enable explicit early stage timing optimization. Cooperating with deep Steiner point adjustment, we propose the routing topology reconstruction to accelerate the convergence and hold a reasonable routing topology. Further, we also introduce Steiner point simplification as a post-processing technique to avoid unnecessary routing constraints. This article demonstrates the ability of the learning-assist framework to perform robust and efficient timing optimization in the early stage with comprehensive and convincing experimental results on real-world designs. With Steiner point adjustment alone, TSteinerPt, can help the state-of-the-art open-source router to obtain 11.2% and 7.1% improvement for the sign-off worst-negative slack and total negative slack, respectively. Under the additional joint optimization with routing topology reconstruction and simplification, TSteinerRec can further save 25.9% optimization duration with a better-sign-off performance.
- HTML: `html/Sign-Off_Timing_Considerations_via_Concurrent_Routing_Topology_Optimization.html`
- JSON: `metadata/meatdatagenerated/json/Sign-Off_Timing_Considerations_via_Concurrent_Routing_Topology_Optimization.json`
