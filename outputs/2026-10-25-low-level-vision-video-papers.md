---
title: 2026-10-25｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-10-25｜底层视觉与视频论文速览

生成时间：2026-10-25

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜HP-PnP-Flow: Hybrid Time Scheduling and Projection for Plug-and-Play Image Restoration via Flow Matching｜2026-10-19
2. 底层视觉｜GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching｜2026-10-22
3. 底层视觉、视频处理｜ResGVC: Residual Coding for High-fidelity Generative Video Compression｜2026-10-22
4. 底层视觉｜WaFIR: Wavelet-Fourier Mixture-of-Experts with Subband-Adaptive Routing for Blind All-in-One Image Restoration｜2026-10-21
5. 底层视觉｜Diffusion Posterior Sampling with Uncertain Forward Models｜2026-10-21
6. 底层视觉｜GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution｜2026-10-22
7. 底层视觉｜WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models｜2026-10-22
8. 底层视觉｜Self-Supervised Multibeam Sonar Restoration via Coherent Forward Modeling｜2026-10-22
9. 底层视觉｜I$^2$-KAN: Interpretable Intra- and Inter-Modal Multi-Pathway Representation Learning for Multimodal Sentiment Analysis｜2026-10-22
10. 底层视觉｜GraphCAD: Geometry-Aware Diffusion on Edge-Adjacency Graphs for CAD Generation｜2026-10-22
11. 底层视觉｜Bound-Conditioned Latent Inference for Progressive Image Compression｜2026-10-22
12. 底层视觉｜CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation｜2026-10-22
13. 底层视觉｜DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models｜2026-10-22
14. 底层视觉｜Self-Distilling Future Video Representations for World Action Models｜2026-10-21
15. 底层视觉｜Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation｜2026-10-21
16. 底层视觉｜Training-free Acceleration for Blind Compressed Image Restoration via Activation-Calibrated Singular Value Decomposition｜2026-10-21
17. 底层视觉｜CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion｜2026-10-21
18. 底层视觉｜How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs｜2026-10-21
19. 底层视觉｜Efficient Generative Image Compression with Quantized Latents Refinement｜2026-10-21
20. 底层视觉｜Spatially Gated Demographic Steering for Debiasing Multi-Person Text-to-Image Generation｜2026-10-21
21. 底层视觉｜Rethinking Underwater Image Enhancement: Learning through Text-Guided Degradation Curriculum｜2026-10-21
22. 底层视觉｜Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers｜2026-10-21
23. 底层视觉｜Seeing through Denoising: Frequency-guided One-step Denoising for Infrared Small Target Detection｜2026-10-21
24. 底层视觉｜OpenMAP-HIE: Pathology Informed Score-based Diffusion Model for Unsupervised Neonatal Hypoxic-Ischemic Encephalopathy Lesion Segmentation｜2026-10-21
25. 底层视觉｜OccJEPA: Occlusion as Masking for Amodal Video Segmentation｜2026-10-21
26. 底层视觉｜Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks｜2026-10-20
27. 底层视觉｜JUICE: Unified Multimodal Modeling in Pretrained Representation Spaces｜2026-10-20
28. 底层视觉｜SolarRenderer: Few-Step Generative Reference Rendering｜2026-10-20
29. 底层视觉｜WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution｜2026-10-20
30. 底层视觉｜Unified RAW Image Exposure Correction and Restoration via Linear Illumination and Frequency-Adaptive Enhancement｜2026-10-20

## 论文摘要

### 1. HP-PnP-Flow: Hybrid Time Scheduling and Projection for Plug-and-Play Image Restoration via Flow Matching

- 方向：底层视觉
- 作者：Yong Li, Xiaojie Wang, Xiaoyan Zhang
- 日期：2026-10-19
- 分类：cs.CV
- 关键词：image restoration、denoising、deblurring
- arXiv：2610.26183v1

摘要：

Image restoration is a fundamental inverse problem that seeks to recover high-quality images from degraded observations. Plug-and-Play (PnP) methods provide a flexible framework for integrating pretrained denoisers into iterative reconstruction, whereas flow matching offers an efficient generative modeling approach based on continuous-time ODE dynamics. Very recently, Martin et al.\ (ICLR, 2025) developed a PnP-Flow method, which integrates the PnP framework with flow matching through a time-dependent denoiser cons...

### 2. GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching

- 方向：底层视觉
- 作者：Ariel Lapid, Yuval Haitman, Reuven Peretz, Arnon Netzer, Idit Diamant
- 日期：2026-10-22
- 分类：cs.CV
- 关键词：image restoration、image enhancement
- arXiv：2610.31222v1

摘要：

Low-light image enhancement (LLIE) aims to recover well-exposed and perceptually faithful images from severely degraded observations. Recent diffusion-based generative methods achieve strong perceptual quality by leveraging powerful image priors, but their iterative sampling incurs substantial computational cost, limiting practical deployment. Despite recent efficiency gains in generative LLIE, high-quality enhancement with a single function evaluation and low overall computation remains challenging, particularly u...

### 3. ResGVC: Residual Coding for High-fidelity Generative Video Compression

- 方向：底层视觉、视频处理
- 作者：Ding Ding, Daowen Li, Ying Chen, Kai Li
- 日期：2026-10-22
- 分类：cs.CV
- 关键词：denoising、video compression
- arXiv：2610.31039v1

摘要：

Generative video compression (GVC) methods usually employ decoder-side diffusion models to denoise reconstructed signals based on generative priors. Besides, most of these methods perform denoising in latent space rather than directly in pixel domain. In this paper, we propose ResGVC, a residual coding framework for GVC that guides denoising toward original pictures by transmitting residual signals. ResGVC first encodes the original pictures within a learned video codec, and then decomposes the distortion between t...

### 4. WaFIR: Wavelet-Fourier Mixture-of-Experts with Subband-Adaptive Routing for Blind All-in-One Image Restoration

- 方向：底层视觉
- 作者：Trong Nhan Nguyen, Vu Hoang Minh Doan, Thanh Dat Le, Truong Tien Vo, Thi Thu Ha Vu, Tan Hung Vo, et al.
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：image restoration、denoising
- arXiv：2610.29108v1

摘要：

Blind all-in-one image restoration must adapt a shared model to heterogeneous and sometimes mixed degradations without a task label at test time. We introduce WaFIR, a decoder module that decomposes features into Haar subbands, summarizes each subband with a compact Fourier descriptor, and routes it to prompt-conditioned spectral modulation experts. Unlike image-level frequency conditioning, WaFIR makes routing decisions at the subband level, enabling frequency-specific processing while retaining the task context l...

### 5. Diffusion Posterior Sampling with Uncertain Forward Models

- 方向：底层视觉
- 作者：Wentao Shangguan, Vivek K Goyal
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：deblurring、motion deblur
- arXiv：2610.29102v1

摘要：

Diffusion posterior samplers reconstruct signals by combining a pretrained diffusion prior with a measurement likelihood specified by a forward model and a noise model. Calibration and reference data can characterize uncertainty in the forward model's parameters, such as blur kernels or detector responses. Fixing these parameters at estimated values leaves their uncertainty out of the likelihood, and parameter errors are thus absorbed into the reconstruction. We introduce an uncertainty-aware likelihood (UAL), a Ga...

### 6. GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution

- 方向：底层视觉
- 作者：Matteo Fusconi, Alex Costanzino, Pierluigi Zama Ramirez, Luigi Di Stefano
- 日期：2026-10-22
- 分类：cs.CV
- 关键词：image compression
- arXiv：2610.31644v1

摘要：

Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due to their compactness, resolution-agnosticism and amenability to direct neural processing. On the other hand, gigapixel images are becoming increasingly widespread across a variety of scientific, cultural, and industrial domains. In this paper, we present GigaBench, the first benchmark and experimental evaluation focused...

### 7. WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models

- 方向：底层视觉
- 作者：Chenxi Song, Yanming Yang, Tong Zhao, Ruibo Li, Joey Tianyi Zhou, Chi Zhang
- 日期：2026-10-22
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.31640v1

摘要：

Video diffusion models have learned rich 3D/4D priors, making them promising for scene generation and video re-rendering. However, their use in spatial tasks is limited by imprecise camera control, spatial and temporal inconsistencies, and entangled camera motion with scene dynamics. Existing approaches, such as task-specific fine-tuning and post-process warping, often introduce visual artifacts, generalize poorly, or incur high computational costs. We propose WorldForge V2 to achieve accurate camera control while...

### 8. Self-Supervised Multibeam Sonar Restoration via Coherent Forward Modeling

- 方向：底层视觉
- 作者：Zixin Wang, James Hopgood, Mike Davies
- 日期：2026-10-22
- 分类：eess.IV, cs.CV, eess.SP
- 关键词：deblurring
- arXiv：2610.31490v1

摘要：

Multibeam imaging sonar produces intensity images degraded by coherent speckle and system-induced blur, while clean reflectivity targets are rarely available. Existing despeckling methods often rely on simplified intensity-domain noise models, synthetic clean targets, or blind-spot self-supervision, and typically do not jointly model deblurring and speckle suppression. We propose a physics-consistent self-supervised framework for joint despeckling and deblurring of multibeam imaging sonar. A stochastic coherent ima...

### 9. I$^2$-KAN: Interpretable Intra- and Inter-Modal Multi-Pathway Representation Learning for Multimodal Sentiment Analysis

- 方向：底层视觉
- 作者：Xiaoting Xie, Feng Qiao, Xianwei Zhang, Hailong Chen, Kaiwen Zheng, Joemon M. Jose, et al.
- 日期：2026-10-22
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.31087v1

摘要：

Multimodal sentiment analysis (MSA) aims to infer sentiment by integrating linguistic, acoustic, and visual information. However, many fusion methods integrate modality-specific representations and cross-modal interactions into joint representations, making it difficult to determine whether predictive utility arises from a modality itself or from its interactions with others. More fundamentally, a modality's standalone predictive utility may not faithfully reflect its interaction-conditioned predictive utility. To...

### 10. GraphCAD: Geometry-Aware Diffusion on Edge-Adjacency Graphs for CAD Generation

- 方向：底层视觉
- 作者：Wenhao Zheng, Xianggen Liu, Li Yue, Jiancheng Shi, Jiancheng Lv
- 日期：2026-10-22
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.30974v1

摘要：

Generative modeling for Computer-Aided Design (CAD) remains fundamentally challenged by the need to capture the intricate interplay between discrete topological connectivity and precise spatial geometry inherent in Boundary Representations (B-reps). Existing generative approaches largely formulate CAD construction as a sequence modeling problem, but consequently lack an explicit topological inductive bias. In this work, we present GraphCAD, a geometry-aware generative framework that centers modeling on the Edge-Adj...

### 11. Bound-Conditioned Latent Inference for Progressive Image Compression

- 方向：底层视觉
- 作者：Jaeseok Jang, Seungmin Jeon, Kwang Pyo Choi, Chang-Su Kim
- 日期：2026-10-22
- 分类：eess.IV, cs.CV
- 关键词：image compression
- arXiv：2610.30966v1

摘要：

Progressive image compression reconstructs images from prefixes of a single bitstream and therefore involves sequential latent inference under partial observations. Existing trit-plane codecs mainly treat decoded trits as discrete symbols for probability prediction, without fully exploiting their role as interval constraints on the underlying continuous latents. We propose bound-conditioned latent inference (BLI), a framework that reformulates progressive trit-plane coding as sequential latent inference under shrin...

### 12. CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation

- 方向：底层视觉
- 作者：Lifan Jiang, Yibo Zhao, Senlin cheng, Bolei Xu, Xiaobo Li, Can Ye, et al.
- 日期：2026-10-22
- 分类：cs.CV, cs.SD
- 关键词：denoising
- arXiv：2610.30854v1

摘要：

Diffusion-based audio-visual generation methods typically perform joint denoising of audio and video latents throughout the entire sampling trajectory, repeatedly executing modality-specific denoising branches and cross-modal attention at every timestep. However, we observe that such uniform joint computation is not always necessary. The key is a modality-asymmetric recoverability: audio-side drift introduced by mid-stage caching can be substantially reduced by only a few terminal joint denoising steps, whereas vid...

### 13. DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models

- 方向：底层视觉
- 作者：Adam Lee, Mutian Xu, Yukang Cao, Shulin Tian, Ziwei Liu
- 日期：2026-10-22
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.30781v1

摘要：

Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like. Existing approaches typically entangle action-conditioned dynamics, camera motion, and visual synthesis within a video generation model, or represent dynamics as point trajectories without explicit object structure. We introduce DeXplicit, a dexterous manipulation world model that instead predicts how the world evolves explicitly in metric 3D before rendering its vi...

### 14. Self-Distilling Future Video Representations for World Action Models

- 方向：底层视觉
- 作者：Huiwon Jang, Suhyeok Jang, Hyeonmo Kang, Seungku Kim, Jinwoo Shin, Sihyun Yu
- 日期：2026-10-21
- 分类：cs.RO, cs.CV
- 关键词：denoising
- arXiv：2610.30320v1

摘要：

World Action Models (WAMs) have emerged as a promising approach to learning generalist robot policies using rich spatiotemporal priors from pre-trained video diffusion models. A recent line of WAMs improves inference efficiency by conditioning a separate action decoder on intermediate future video representations extracted from a single denoising step, avoiding costly iterative denoising required for video generation. This design makes action prediction depend directly on the quality of these future representations...

### 15. Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation

- 方向：底层视觉
- 作者：Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu, Ying Shan, et al.
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.29989v1

摘要：

Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong temporal redundancy may allow local visual continuity to serve as a shortcut for current-chunk denoising, reducing the pressure to model visual evolution. We introduce Future Chunk Prediction (FCP), an auxiliary objective jointly optimized with teacher-forced denoising that predicts temporally separated chunks without access...

### 16. Training-free Acceleration for Blind Compressed Image Restoration via Activation-Calibrated Singular Value Decomposition

- 方向：底层视觉
- 作者：Suhang Yao, Xin Li, Xijun Wang, Yufei Wang, Yeying Jin, Zhibo Chen
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2610.29959v2

摘要：

Transformer-based models achieve strong performance on blind compressed image restoration (CIR) under unknown compression settings, but their densely stacked projection operators make deployment costly. We study training-free acceleration for such models through an empirical, operator-level analysis. Specifically, we profile where computation is concentrated, characterize channel-wise activation distributions under compressed inputs, and examine the singular-value decay of representative projection weights. These m...

### 17. CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion

- 方向：底层视觉
- 作者：Kai Zhu, Yintianrun Zhang, Shuwei Jiang, Ruolin Zuo, Yixin Chen, Duomin Wang, et al.
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.29915v1

摘要：

Diffusion-based video generation models (VGMs) can produce visually plausible videos, yet their camera ego-motion often drifts over long horizons. Camera ego-motion determines how the viewpoint changes between frames and is essential for maintaining consistent geometry and trajectories. To address this problem, we propose CausalAlign, a causal alignment framework with two components. First, we diagnose how precise ego motion is represented, used, and retained within VGMs using linear probes and causal interventions...

### 18. How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs

- 方向：底层视觉
- 作者：Gyeonghun Kang, William Xingxu Chen, Xiang Cheng
- 日期：2026-10-21
- 分类：cs.CV, stat.ML
- 关键词：denoising
- arXiv：2610.29854v1

摘要：

How do diffusion transformers (DiTs) represent image content and learn rules for reusing it to generalize? We develop an aggregator--predictor view of DiTs as input-adaptive local denoisers, in which context aggregation and patch prediction provide functional roles for interpreting attention and MLPs. We first establish that, for Gaussian Markov random field (GMRF) priors, the global Bayes denoiser can be approximated using only a subset of context patches, with error decaying exponentially in context radius. We fu...

### 19. Efficient Generative Image Compression with Quantized Latents Refinement

- 方向：底层视觉
- 作者：Hao Cao, Yinhuan Huang, Wenqi Guo, Zhijin Qin, Jungong Han
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：image compression
- arXiv：2610.29691v1

摘要：

Generative image compression (GIC) delivers strong perceptual quality at low bitrates. However, GIC methods with strong perceptual quality often rely on pretrained diffusion models with high latency, while recent lightweight GIC methods reduce latency but deliver lower perceptual quality. We observe that, for lightweight GIC methods at low bitrates, coarse deterministic quantization can collapse nearby encoder latents corresponding to different fine details to the same point, making these details difficult to recov...

### 20. Spatially Gated Demographic Steering for Debiasing Multi-Person Text-to-Image Generation

- 方向：底层视觉
- 作者：Venkatesh Thirugnana Sambandham, Torsten Schon
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.29651v1

摘要：

Text-to-Image models reproduce societal stereotypes, and existing mitigation applies one demographic correction to the whole scene. In multi-person scene generation this creates a trade-off: global steering improves aggregate balance only by homogenizing the people within an image. Steering-based methods like Embedding Arithmetic drive the intra-image diversity below the unsteered baseline. Text- and latent-projection approaches shift the aggregate skew with only marginal gains in intra-image diversity. We present...

### 21. Rethinking Underwater Image Enhancement: Learning through Text-Guided Degradation Curriculum

- 方向：底层视觉
- 作者：Hongri Tian, Wenxue Li, Tian Ye, Sixiang Chen, Zongxian Su, Lujia Wang, et al.
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2610.29569v2

摘要：

Existing paired clean-degraded datasets have advanced learning-based underwater image enhancement, but they remain either limited in scale or difficult to acquire, and still fail to adequately cover the diverse degradations encountered in real-world underwater environments. Such scarce and insufficient data ultimately restrict the generalization of underwater image enhancement models, highlighting the need for realistic and controllable degradation modeling to better capture real underwater conditions and improve e...

### 22. Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers

- 方向：底层视觉
- 作者：Tianze Xia, Xiaoling Zhou, Ruya Lan, Yiqiao Liao, Chengru Song, Shiming Xiang
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.29441v1

摘要：

Full 3D attention is costly in video Diffusion Transformers. Block-sparse attention reduces this cost by computing only selected attention blocks. However, existing methods either overlook the potential to optimize sparsity allocation or rely on heuristic rules or local metrics to guide it. In this work, we observe that sparsifying attention in different layers and at different denoising steps affects final-video fidelity to substantially different degrees. Yet the identities of the most sensitive layer-step pairs...

### 23. Seeing through Denoising: Frequency-guided One-step Denoising for Infrared Small Target Detection

- 方向：底层视觉
- 作者：Xuelin Qian, Zixuan Wang, Chang Xu, Dingwen Zhang, Junwei Han
- 日期：2026-10-21
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.29361v1

摘要：

Infrared small target detection (IRSTD) is a challenging task due to the extremely small size of targets, low signal-to-noise ratios, and heavy background clutter in infrared imagery. While the progress of deep learning has advanced this field, existing methods primarily adopt discriminative paradigms that directly map images to target masks, overlooking the potential of generative modeling. In this paper, we propose DiffIRSTD, a novel generative framework that reformulates infrared small target detection as a back...

### 24. OpenMAP-HIE: Pathology Informed Score-based Diffusion Model for Unsupervised Neonatal Hypoxic-Ischemic Encephalopathy Lesion Segmentation

- 方向：底层视觉
- 作者：Pengyu Kan, Craig Jones, Kenichi Oishi
- 日期：2026-10-21
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2610.29322v2

摘要：

Accurate localization of neonatal hypoxic--ischemic encephalopathy (HIE) lesions on apparent diffusion coefficient (ADC) images is clinically important but is limited by scarce expert annotations and substantial variation in lesion appearance. We propose OpenMAP-HIE, a pathology-informed score-based diffusion model for unsupervised HIE lesion localization without voxel-wise lesion supervision. A denoising diffusion model learns the healthy neonatal ADC distribution, while a ControlNet-based conditional branch prese...

### 25. OccJEPA: Occlusion as Masking for Amodal Video Segmentation

- 方向：底层视觉
- 作者：Genpei Zhang
- 日期：2026-10-21
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2610.29061v1

摘要：

Amodal video segmentation asks for the complete mask of an object in every frame, including the parts hidden behind other objects. The best current methods generate these masks with fine-tuned video diffusion models, which need many denoising steps and an extra depth network, and give a different answer for every sample. Self-supervised video world models of the JEPA family are trained on a closely related task: predicting the representation of masked space-time regions from the visible ones. We therefore treat occ...

### 26. Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks

- 方向：底层视觉
- 作者：Ivan Listopadov, Maksim Nakhodnov, Aibek Alanov
- 日期：2026-10-20
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.28889v1

摘要：

Selecting intermediate features from a frozen diffusion model for discriminative tasks is non-trivial because the useful signal is distributed across the denoising trajectory, network depth, and channels. In practice, this requires choosing a timestep, a block, and a channel subset. Existing methods either fix these choices by hand or optimize only a few extraction hyperparameters, most often the timestep, then reuse the same rule across inputs and budgets. We introduce Policy-Mask, a budget-conditioned policy trai...

### 27. JUICE: Unified Multimodal Modeling in Pretrained Representation Spaces

- 方向：底层视觉
- 作者：Jiahan Li, Huangyuan Su, Shengbang Tong, Shusheng Yang, Ruihan Guo, Suozhi Huang, et al.
- 日期：2026-10-20
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.28801v1

摘要：

Most unified multimodal models treat images and text asymmetrically: a pretrained language model generates text, an attached diffusion head generates images, and outputs that contain both are produced in a fixed order, so the first output cannot adapt to the second. We ask whether both modalities can instead be generated by one process that is trained on them jointly from scratch. Pretrained encoder spaces hold both modalities in one continuous form and carry knowledge learned at scale, and recent work finds them e...

### 28. SolarRenderer: Few-Step Generative Reference Rendering

- 方向：底层视觉
- 作者：Guian Fang, Shengju Qian, Dongyue Lu, Junchao Huang, Lutao Jiang, Xin Wang, et al.
- 日期：2026-10-20
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.28630v1

摘要：

Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, need tens of denoising steps or a costly distillation of their own, and learn from conditions that are not aligned with their target videos. We present SolarRenderer, a structure-conditioned video renderer that adapts a fr...

### 29. WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution

- 方向：底层视觉
- 作者：Junyuan Deng, Xinyi Wu, Zhenyao Wu, Song Wang, Yu Wang, Congchao Zhu
- 日期：2026-10-20
- 分类：cs.CV, cs.AI
- 关键词：image super-resolution
- arXiv：2610.28423v1

摘要：

Generative-prior-based super-resolution (SR) methods leverage implicit knowledge learned from large-scale models to enhance low-resolution inputs. However, such priors are inherently stochastic and optimized for diverse generation, conflicting with the deterministic, high-fidelity reconstruction required for SR. It is also tied to the base model, costly to update, and prone to hallucinations as real-world data evolves. To address these limitations, we introduce WorldSR, a novel framework that augments SR with expli...

### 30. Unified RAW Image Exposure Correction and Restoration via Linear Illumination and Frequency-Adaptive Enhancement

- 方向：底层视觉
- 作者：Yingkai Zhang, Yunhao Zou, Ying Fu
- 日期：2026-10-20
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.28191v1

摘要：

Incorrect exposure degrades both image brightness and recoverable scene detail. Existing sRGB-based correction methods are limited by the non-linear image signal processing pipeline, whereas RAW-based methods are usually developed for a single degradation type, such as low-light denoising or high-light recovery. In this paper, we focus on joint exposure correction and restoration directly in the RAW domain and propose a unified RAW Image Exposure Correction and Restoration (RIECR) framework for both under- and over...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-10-25-low-level-vision-video-papers.md`
