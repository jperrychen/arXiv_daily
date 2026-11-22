---
title: 2026-11-22｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-11-22｜底层视觉与视频论文速览

生成时间：2026-11-22

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Joint Image Denoising and Interpolation via Mixed Graph Filtering｜2026-11-18
2. 底层视觉、视频处理｜Harnessing Image Diffusion Prior for Photo-Realistic Video Restoration｜2026-11-17
3. 底层视觉｜AURA: AUdio-dRiven streaming Avatar｜2026-11-19
4. 底层视觉｜Fixing the Last Mile: Failure-Aware Image Restoration with Region-Specific Guidance｜2026-11-19
5. 底层视觉｜Fast Self-Supervised Generative CT Denoising via Few-Step Sampling｜2026-11-19
6. 视频处理｜OffBeat: Multicoset Sampling for 4D Capture Beyond the Camera Frame Rate｜2026-11-19
7. 底层视觉｜Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers｜2026-11-19
8. 底层视觉｜SpecWM: Turning Verification into Refinement for Streaming World Models｜2026-11-19
9. 底层视觉｜RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration｜2026-11-19
10. 视频处理｜FlexVSR: Continuous-Scale Super-Resolution for Streaming Video Generation｜2026-11-19
11. 视频处理｜Towards High-Fidelity Learned Video Compression｜2026-11-19
12. 底层视觉｜What One Sample Cannot See: Why Fewer Denoising Steps Can Score Higher on Physics Benchmarks｜2026-11-19
13. 底层视觉｜Anchored Inertial Proposals with Objective Verification for Diffusion-Prior Inverse Problems｜2026-11-19
14. 底层视觉｜Life-IQA+: Boosting Blind Image Quality Assessment via GCN-enhanced Layer Interaction and Flexible Hierarchical Expert Specialization｜2026-11-19
15. 底层视觉｜CANDOR: Contrastive Self-Denoising Rewards for Label-Free Text-to-Image Post-Training｜2026-11-19
16. 底层视觉｜Breaking Noise Shortcuts in Self-Supervised Learning Via Noise-Aligned View Generation｜2026-11-19
17. 底层视觉｜CalibCache: Cache-to-Full Feature Dynamics Calibration for Diffusion Transformers｜2026-11-18
18. 底层视觉｜Branch Caching After Step Distillation in Four- and Eight-Step Image Generators｜2026-11-18
19. 底层视觉｜CoRelate: Coordinated Human-Object Motion Synthesis through Interaction Relations｜2026-11-18
20. 底层视觉｜PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration｜2026-11-18
21. 底层视觉｜Edge-Efficient Joint RAW Image Compression and Restoration for Smart Wearable Devices｜2026-11-18
22. 底层视觉｜SCRiD: Spatial and Contextual References for Generalizable AI-Generated Video Detection｜2026-11-18
23. 底层视觉｜Every Query Routes Itself: Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention｜2026-11-18
24. 底层视觉｜Probing Physics in Motion Diffusion Models Against Their Own Estimate｜2026-11-18
25. 视频处理｜Semantic Guidance for Joint Infrared-Visible Video Fusion and Frame Interpolation｜2026-11-18
26. 底层视觉｜Spark-H3: Adaptive Block Sparse Attention for Video Diffusion Models｜2026-11-18
27. 底层视觉｜ViLFlow: Parallel Vision-Language Generation with Continuous Latent Flows｜2026-11-18
28. 底层视觉｜Psychometrics-Inspired Coreset Selection for Image Quality Assessment｜2026-11-18
29. 底层视觉｜Training Denoising Models of Any Architecture Without Stored Images｜2026-11-18
30. 底层视觉｜DetailScale-SR: Decoupling Restoration and Continuous Detail Control for Real-World Super-Resolution｜2026-11-18

## 论文摘要

### 1. Joint Image Denoising and Interpolation via Mixed Graph Filtering

- 方向：底层视觉
- 作者：Gene Cheung, Niruhan Viswarupan, Romisaa Elsaidy
- 日期：2026-11-18
- 分类：eess.IV, cs.CV, eess.SP
- 关键词：image denoising、denoising
- arXiv：2611.24242v1

摘要：

Images often require both denoising and interpolation, yet treating the two tasks separately is suboptimal: interpolation introduces correlated noise that complicates subsequent denoising, while denoising may remove image details useful for interpolation. In this paper, we study joint image denoising and interpolation from a mixed graph filtering perspective, where denoising is modeled using undirected graph filters and interpolation using directed graph filters. We first establish that, under mild conditions, any...

### 2. Harnessing Image Diffusion Prior for Photo-Realistic Video Restoration

- 方向：底层视觉、视频处理
- 作者：Fanghua Yu, Hongyu An, Jinfan Hu, Xinqi Lin, Zhiyuan You, Jian Wang, et al.
- 日期：2026-11-17
- 分类：cs.CV
- 关键词：denoising、video restoration
- arXiv：2611.22874v1

摘要：

Recent image generation models produce photo-realistic results with rich details, but transferring their powerful priors to video restoration remains difficult due to temporal inconsistency from stochastic detail synthesis. Existing video restoration methods improve temporal coherence but often sacrifice visual fidelity, leaving a gap between image-level quality and video-level stability. We propose a generative video restoration method that bridges this gap by enabling temporally consistent detail synthesis from i...

### 3. AURA: AUdio-dRiven streaming Avatar

- 方向：底层视觉
- 作者：Nathaniel Cohen, Nicolas Dufour, Amélie Royer, Alasdair Newson, Patrick Pérez
- 日期：2026-11-19
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2611.26540v1

摘要：

Current audio-driven video diffusion models can synthesize realistic talking-head videos but generally require dozens of diffusion denoising steps over multi-second video chunks, making them unsuitable for streaming applications such as voice assistants and virtual avatars, where low-latency and online causal generation are required properties. AURA generates video chunk by chunk with a rolling KV cache, requiring only the audio of the current chunk to start generating, rather than a multi-second audio look-ahead l...

### 4. Fixing the Last Mile: Failure-Aware Image Restoration with Region-Specific Guidance

- 方向：底层视觉
- 作者：Hongyu An, Fanghua Yu, Kainan Yan, Luc Van Gool, Chao Dong, Jinjin Gu
- 日期：2026-11-19
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2611.26456v1

摘要：

Recent advances in image restoration have greatly improved global image fidelity, producing visually plausible results across most regions of an image. Nevertheless, even high-quality restorations often exhibit localized failures, including artifacts in semantically important regions such as faces and text, structural inconsistencies, and texture mismatches. Although these errors typically affect only a small portion of the image, they often dominate the overall perceptual quality of the result. In this work, we pr...

### 5. Fast Self-Supervised Generative CT Denoising via Few-Step Sampling

- 方向：底层视觉
- 作者：Xingyi Yao, Zhengtao Ma, Zhennong Chen
- 日期：2026-11-19
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.26370v1

摘要：

Low-dose and thin-slice computed tomography (CT) images suffer from elevated noise that obscures anatomical detail, while clean references for supervised denoising are often unavailable. Although Noise2Noise permits self-supervised training from noisy pairs, direct regression tends to oversmooth fine structure. Averaging multiple independently generated samples mitigates this blur, though repeating multi-step diffusion sampling is costly. We introduce Noise2Noise with Improved Mean Flow (N2N-iMF) to accelerate this...

### 6. OffBeat: Multicoset Sampling for 4D Capture Beyond the Camera Frame Rate

- 方向：视频处理
- 作者：Chi-Wei Lee, An-Kai Chen, Cheng-Han Chiang, Yi-Chun Chang, Po-Chih Kuo
- 日期：2026-11-19
- 分类：cs.CV, eess.IV
- 关键词：frame interpolation
- arXiv：2611.26347v1

摘要：

For 4D reconstruction, a synchronized multi-camera rig records all views at the same timestamps and misses the motion between them. Staggered triggers spread the same frames over more timestamps. However, when the cameras along each row fire one after another, as in 4DSloMo's schedule on the N3DV rig, the row acts as one moving camera that confounds depth with motion. We introduce OffBeat, which models a staggered rig as a spatially distributed multicoset sampler: shifted copies of one sampling grid. From the calib...

### 7. Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers

- 方向：底层视觉
- 作者：Ryan Lucas, Petros Prastakos, Rahul Mazumder
- 日期：2026-11-19
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2611.26334v1

摘要：

Video diffusion transformers reuse key--value (KV) caches across denoising steps, which quickly becomes a bottleneck for long video generation. We find that quantizing temporally distant cache vectors leads to a large range and high quantization error, but that nearby video tokens in the KV-cache share a persistent pattern per channel. These patterns also vary across videos, motivating rotations that are adapted to each video's unique cache. We propose Temporal Rotation Quantization (TRQ), a method that rotates fra...

### 8. SpecWM: Turning Verification into Refinement for Streaming World Models

- 方向：底层视觉
- 作者：Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu, Xiaotong Zhao, et al.
- 日期：2026-11-19
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.26211v1

摘要：

Recently, video world models have advanced interactive generation, with large models offering higher quality and smaller models enabling faster inference. Existing speculative methods combine their strengths through fast draft generation and selective target regeneration guided by rewards on decoded frames. However, verification covers only the external scorer's evaluation dimensions and adds decoding and scoring costs. Moreover, these scores provide no correction, requiring costly target regeneration for rejected...

### 9. RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration

- 方向：底层视觉
- 作者：Weiyu Zhou, Jiacong Tang, Tao Hu, Axi Niu, Jinqiu Sun, Peng Wu, et al.
- 日期：2026-11-19
- 分类：cs.CV, cs.AI
- 关键词：image restoration
- arXiv：2611.26179v1

摘要：

Images under non-uniform coupled degradations require diverse restoration capabilities for different degraded regions. Existing methods employ globally uniform operations, potentially overlooking regional differences and causing incomplete restoration or even damage to image content. Moreover, a degraded region may require successive restoration actions, and earlier actions may alter residual degradation characteristics or introduce artifacts, potentially hindering subsequent restoration. To address these challenge...

### 10. FlexVSR: Continuous-Scale Super-Resolution for Streaming Video Generation

- 方向：视频处理
- 作者：Ji Wang, Haonan An, Jiasheng Zhang, Renlong Chen
- 日期：2026-11-19
- 分类：cs.CV
- 关键词：video super-resolution
- arXiv：2611.26178v1

摘要：

Real-time streaming video generation has gained rapid momentum in live content creation and interactive media. Deploying such systems in practice requires flexible scaling factors to accommodate diverse source resolutions, target displays, and computational budgets. However, extending fixed-scale generative video super-resolution (VSR) to varying target scales poses two challenges: downsampling from a larger fixed scale incurs redundant cost, while re-optimizing the diffusion transformer (DiT) is costly and alters...

### 11. Towards High-Fidelity Learned Video Compression

- 方向：视频处理
- 作者：Bumyoon Kim, Yongseong Kim, Inhyuk Jeong, Byeungwoo Jeon
- 日期：2026-11-19
- 分类：cs.CV
- 关键词：video compression
- arXiv：2611.25731v1

摘要：

Professional video workflows operate at qualities that learned video codecs do not reach. We measure how much of a professional quality range a codec covers, from the lowest quality of the standard test conditions, VVC at QP 37, to the highest 4:2:2 grade of the production codec ProRes. To compare inter-frame coding alone, every codec receives original frames as references at the intra positions. On 10-bit YCbCr 4:2:2 test sequences, four recent learned codecs cover 24 to 38% of this range. Their encoders are feed-...

### 12. What One Sample Cannot See: Why Fewer Denoising Steps Can Score Higher on Physics Benchmarks

- 方向：底层视觉
- 作者：Yutao Li, Chen Wang
- 日期：2026-11-19
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2611.25632v1

摘要：

When a storm can head north or south, a forecast down the middle may score better under squared error than either plausible path. The same paradox appears when video generators are tested as world models: fewer denoising steps can raise physics scores even as videos blur or stop moving early. Why? Physics-IQ compares each generated video with one recording, although a scene can have multiple valid futures. An exact decomposition shows its scores can reward reduced variation among generated futures, even when their...

### 13. Anchored Inertial Proposals with Objective Verification for Diffusion-Prior Inverse Problems

- 方向：底层视觉
- 作者：Minwoo Kim, Seunghyeok Shin, Dabin Kim, Hongki Lim
- 日期：2026-11-19
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.25551v1

摘要：

Training-free diffusion priors are powerful for inverse problems, but measurement guidance during reverse sampling is local: aggressive updates can improve immediate data fit while disrupting later denoising. We introduce an anchored inertial correction rule that separates proposal generation from acceptance. At each corrected step, the denoiser prediction anchors a frozen clean-space objective combining measurement fit with a noise-level-dependent proximal term. Heavy-ball dynamics with step size and momentum comp...

### 14. Life-IQA+: Boosting Blind Image Quality Assessment via GCN-enhanced Layer Interaction and Flexible Hierarchical Expert Specialization

- 方向：底层视觉
- 作者：Long Tang, Guoquan Zheng, Huiyu Duan, Jie Hao, Yucheng Zhu, Liang Yuan, et al.
- 日期：2026-11-19
- 分类：eess.IV, cs.CV
- 关键词：image quality assessment
- arXiv：2611.25510v1

摘要：

Blind image quality assessment (BIQA) is essential for evaluating and optimizing visual experience. Existing BIQA methods typically aggregate features from multiple backbone stages without accounting for their unequal contributions to quality prediction. Furthermore, uniformly supervising all experts may constrain their flexibility and limit the diversity of the learned quality representations. To address these issues, we present Life-IQA+, a quality representation decoding framework that combines graph convolution...

### 15. CANDOR: Contrastive Self-Denoising Rewards for Label-Free Text-to-Image Post-Training

- 方向：底层视觉
- 作者：Junhyeok Lee, Byung-Hoon Kim, Kyu Sung Choi
- 日期：2026-11-19
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.25457v1

摘要：

Post-training text-to-image generators with reinforcement learning usually relies on external reward models that need annotated preferences or auxiliary evaluators and are prone to reward hacking. We show that the generator's own denoising accuracy, used by a recent intrinsic reward, is a poor proxy for prompt fidelity. Within a same-prompt group, this absolute self-confidence is dominated by image complexity and ranks correct samples above incorrect ones near chance. We introduce CANDOR (Contrastive Alignment from...

### 16. Breaking Noise Shortcuts in Self-Supervised Learning Via Noise-Aligned View Generation

- 方向：底层视觉
- 作者：Oankar R. Patil, May D. Wang
- 日期：2026-11-19
- 分类：eess.IV, cs.AI, cs.CV
- 关键词：denoising
- arXiv：2611.25335v1

摘要：

Self-supervised learning (SSL) is increasingly applied to scientific imaging domains, such as microscopy, where labels are scarce but noisy data is abundant. These domains exhibit significant signal-dependent noise, which can create a representational shortcut: since both augmented views derive from the same noisy image, the encoder can boost view agreement by also encoding noise patterns rather than semantic content. To enable noise-robust representation learning without knowledge of underlying noise models, we in...

### 17. CalibCache: Cache-to-Full Feature Dynamics Calibration for Diffusion Transformers

- 方向：底层视觉
- 作者：Mingyu Liang, Dingkun Xu, Jingwei Xu
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.25296v1

摘要：

Diffusion Transformers generate high-quality images, but iterative sampling remains computationally expensive. Feature caching reduces the number of full network evaluations, yet its approximation error can become more severe under short sampling schedules, where fewer full-compute steps and a coarser sampling grid can make history-based extrapolation less reliable. In this paper, we propose CalibCache, a lightweight offline calibration method that corrects systematic discrepancies between cached and full-compute f...

### 18. Branch Caching After Step Distillation in Four- and Eight-Step Image Generators

- 方向：底层视觉
- 作者：Mingyu Liang, Dingkun Xu
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.25248v1

摘要：

Can a distilled image generator save time by reusing features between its few remaining denoising steps? We study a fixed branch cache that replaces selected attention and MLP evaluations while preserving the student's noise schedule. One full trajectory and one raw-cache trajectory from the same initial noise supply a scalar correction for each branch type and reuse position. At $1024^2$, one internal reuse reduces four-step Qwen-Image-Lightning denoising time from 1.279 to 0.977 seconds. Three reuses yield $1.51\...

### 19. CoRelate: Coordinated Human-Object Motion Synthesis through Interaction Relations

- 方向：底层视觉
- 作者：Zhiwen Qiu, Daisy Lin, Diyu Zhou, Jialin Wu, Rosita Ji, Saleh Kalantari
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.25166v1

摘要：

Human-object motion synthesis requires coordinated human participation as objects move toward specified goals. However, reaching object targets does not ensure that contact is established and maintained, while adjustments that improve contact may interfere with task completion. We introduce CoRelate, a diffusion framework that coordinates full-body human-object motion through explicit interaction relations and task feedback for rigid and articulated objects. We represent intended participation through hand-part rel...

### 20. PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration

- 方向：底层视觉
- 作者：Zhaocheng Yu, Kui Jiang, Jing Cao, Yiang Chen, Xiaocheng Feng, Junjun Jiang, et al.
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2611.24915v1

摘要：

Agentic image restoration composes operations to handle mixed degradations, yet its toolbox often requires storing multiple restoration networks. We propose PrismRestore, which constructs a compact bank of callable restoration actions from a single frozen all-in-one model. Our approach builds on task-dependent yet overlapping channel responses in the shared model. An offline task-prior search uses activation and gradient statistics to group channels with similar response profiles, then searches task-specific modula...

### 21. Edge-Efficient Joint RAW Image Compression and Restoration for Smart Wearable Devices

- 方向：底层视觉
- 作者：Yunong Sun, Sicheng Chen, Fei Xia
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：image compression
- arXiv：2611.24805v1

摘要：

Smart wearable devices, such as augmented reality glasses, increasingly rely on cameras to understand and interact with their surroundings. However, their compact sensors often capture noisy RAW images, while limited compute and power make high-quality on-device restoration difficult. This creates an emerging need to reduce both local computation and transmission cost without sacrificing image quality. Two common solutions are to offload restoration or to compress the raw data before transmission. The first makes R...

### 22. SCRiD: Spatial and Contextual References for Generalizable AI-Generated Video Detection

- 方向：底层视觉
- 作者：Hao Tan, Zekai Zuo, Boyang Chen, Jinghui Qin
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.24524v1

摘要：

Generalizable AI-generated video detection remains challenging because natural motion and content variations can resemble synthesis artifacts, making isolated video discrepancies unreliable indicators of authenticity. To address this challenge, we propose Spatial and Contextual Reference-informed Detection (SCRiD), a framework that interprets video variations through complementary spatial and contextual references. Specifically, we introduce Matched-Coordinate Residual Response (MCR) to characterize temporal residu...

### 23. Every Query Routes Itself: Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention

- 方向：底层视觉
- 作者：Zhen Huang, Shuwei Li, Ruizhe Yao, Xinrui Chen, Danyi Liu, Haoyuan Liang, et al.
- 日期：2026-11-18
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2611.24479v1

摘要：

Self-attention over long token sequences dominates the inference cost of video diffusion transformers. Clustering-based sparse attention clusters both queries and keys and lets all queries in a cluster share one selection of key clusters. We show that this sharing limits accuracy: with key clusters and density fixed, attention grows more accurate as the query clusters are refined, and is most accurate when each query selects on its own, which needs no query clustering at all. We therefore propose Per-Query Routed S...

### 24. Probing Physics in Motion Diffusion Models Against Their Own Estimate

- 方向：底层视觉
- 作者：Saeed Ghorbani
- 日期：2026-11-18
- 分类：cs.LG, cs.CV, cs.GR
- 关键词：denoising
- arXiv：2611.24423v1

摘要：

Recent studies report that video diffusion models "know more than they show": physical properties decode better from their activations than from their inputs or outputs. But a diffusion model computes its clean-sample estimate from those same activations, so such a comparison measures how easily a readout extracts the information. Whether the model hides anything is a separate question. We set out to find hidden physical knowledge in kinematic text-to-motion diffusion models, where the physics of every intermediate...

### 25. Semantic Guidance for Joint Infrared-Visible Video Fusion and Frame Interpolation

- 方向：视频处理
- 作者：Yushen Xu, Xiaosong Li, Huaming Wu, Dongwei Ren
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：frame interpolation
- arXiv：2611.24277v1

摘要：

Infrared and visible video fusion at high frame rates requires recovering missing observations when camera rates differ or fall below the desired output rate. Cascading interpolation and fusion can accumulate errors and cause brightness fluctuations. Motion and occlusion further complicate content selection, particularly when missing visible frames also remove direct semantic guidance. We propose SAFI, which uses semantics at the target time to guide joint interpolation and fusion. When the visible frame rate excee...

### 26. Spark-H3: Adaptive Block Sparse Attention for Video Diffusion Models

- 方向：底层视觉
- 作者：Zecheng Tang, Jiaye Fu, Youtian Lin, Xinyao Rao, Liuxuan Sun, Jian Zhang, et al.
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.24256v1

摘要：

Long video sequences make attention a substantial cost in video diffusion models. Block sparse attention (BSA) reduces this cost by computing selected blocks exactly while compressing the remaining blocks. However, fixed token grouping can place tokens with dissimilar attention preferences in the same group, while uniform key averaging can underestimate the attention mass of compressed blocks. We introduce Spark-Attn, a training-free BSA method comprising Spark-Reblock and Spark-Reweight. Spark-Reblock recursively...

### 27. ViLFlow: Parallel Vision-Language Generation with Continuous Latent Flows

- 方向：底层视觉
- 作者：Kevin Zhai, Bian Sun, Zhenyi Wang, Song Wang
- 日期：2026-11-18
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2611.24240v1

摘要：

Vision-language generation has predominantly relied on autoregressive and discrete diffusion models. Autoregressive models generate tokens sequentially, while discrete diffusion models typically predict tokens independently within each denoising step. We propose ViLFlow (Vision-Language Flow), a continuous-flow vision-language model that combines joint modeling of output embeddings with parallel token decoding. ViLFlow adapts pretrained continuous language generation to visual question answering and image captionin...

### 28. Psychometrics-Inspired Coreset Selection for Image Quality Assessment

- 方向：底层视觉
- 作者：Susu Jiang, Xuelin Shen, Baoliang Chen
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2611.24233v1

摘要：

Collecting large-scale subjective annotations remains a critical bottleneck in training accurate image quality assessment (IQA) models. Coreset selection reduces this burden by selecting representative images before annotation. However, diversity in a visual feature space does not necessarily reflect diversity in perceptual quality, raising a fundamental question about which quality-related factors the representation should encode. We propose GRAM, a quality-aware representation learning framework inspired by the g...

### 29. Training Denoising Models of Any Architecture Without Stored Images

- 方向：底层视觉
- 作者：Christos Koutlis, Ioannis Kompatsiaris, Symeon Papadopoulos
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.24223v1

摘要：

Can a pretrained denoising model replace the dataset used to train it? We investigate this question through teacher-supervised training, showing for the first time that continuous-time diffusion and flow models of any architecture and size can be trained from random initialization without stored images. Our students regress the teacher's velocity on a rolling pool of noisy samples, advanced along trajectories of random step counts to obtain independent, dense and approximately continuous noise levels. This saves co...

### 30. DetailScale-SR: Decoupling Restoration and Continuous Detail Control for Real-World Super-Resolution

- 方向：底层视觉
- 作者：Shengchuan Gao, Zhongjie Duan, Yingda Chen, Jingjing Chen
- 日期：2026-11-18
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2611.24212v1

摘要：

Real-world image super-resolution often seeks the most detailed plausible reconstruction, although more detail is not always desirable. The same degraded image may require restrained restoration, faithful reconstruction, or enhanced visual detail according to user intent. We present DetailScale-SR, a preference-conditioned framework that continuously controls reconstructed detail for a fixed low-resolution input without altering the scene being restored. Rather than relying on post-processing or repeatedly rewritin...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`latest.md`
