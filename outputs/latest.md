---
title: 2026-11-15｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-11-15｜底层视觉与视频论文速览

生成时间：2026-11-15

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Improved CNN-Transformer Network for Neutron Image Super-Resolution｜2026-11-12
2. 底层视觉、视频处理｜Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control｜2026-11-10
3. 底层视觉、视频处理｜When to Start Denoising? Adaptive Denoising Entry for Generative Video Compression｜2026-11-10
4. 底层视觉｜Flex-DDCM: Zero-Shot Task-Oriented Image Compression via Diffusion Trajectory Guidance｜2026-11-08
5. 底层视觉｜eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation｜2026-11-12
6. 视频处理｜HiVE-VQA: Hierarchical Interaction via Volumetric Embedding for Video Quality Assessment｜2026-11-12
7. 底层视觉｜TokenStream: Multi-Subject Personalized Video Generation with Token-wise LoRA and Guided Attention｜2026-11-12
8. 底层视觉｜What Limits Thermal Infrared Drone Detection? A Cross-Dataset Benchmark Analysis｜2026-11-12
9. 视频处理｜PiLLVD: A Real-World Low-Light Video Dataset for Dynamic Scenes Captured with Off-the-Shelf Cameras｜2026-11-12
10. 底层视觉｜HIFC-IQA: Train-Free Cross-Domain Image Quality Assessment via Dual-Process Cognition｜2026-11-12
11. 底层视觉｜TRACE: Trajectory Synchronization for Training-Free Resolution Extension in Video Generation｜2026-11-11
12. 底层视觉｜Taming Neural Fields with a Frequency-Lipschitz Curriculum for Sparse-View CT Reconstruction｜2026-11-11
13. 底层视觉｜WaveFlow-UIE: A Single-Pipeline Wavelet-Domain Flow Model for Efficient Underwater Image Restoration｜2026-11-11
14. 底层视觉｜Reading the Unreadable: Text-Aware Image Super-Resolution Needs Reasoning｜2026-11-11
15. 底层视觉｜CARE-Drive: Coupled Alternating Refinement for Ego-trajectories｜2026-11-11
16. 底层视觉｜C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference｜2026-11-10
17. 底层视觉｜From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models｜2026-11-10
18. 底层视觉｜TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation｜2026-11-10
19. 底层视觉｜Lipschitz-Controlled Flow Matching for Robust Image Restoration｜2026-11-10
20. 底层视觉｜Adapting a Vision Foundation Model for Fracture Characterization in Acoustic Image Logs｜2026-11-10
21. 底层视觉｜DUO: Dual Readouts of Diffusion Models for OOD Detection｜2026-11-09
22. 底层视觉｜Just Image Transformers with Late-Stage Pixel Refinement｜2026-11-09
23. 底层视觉｜Real-Time Volumetric Light Transport Inference without a Path｜2026-11-09
24. 底层视觉｜MPEG-Diffusion: Mixed-Resolution Video Generation｜2026-11-09
25. 底层视觉｜Four-Step Text-Bearing Image Generation via Distillation with Local Response Regularization and Teacher-Guided Training｜2026-11-09
26. 底层视觉｜Single Image Super-Resolution via Semantic Prompt and Cross-Modal Training on Content Area｜2026-11-09
27. 底层视觉｜MUTE: Multi-Level Alignment Uncoupling Against Talking-Head Exploitation for Voice Protection｜2026-11-09
28. 底层视觉｜Direct Trajectory Optimization for Inference-Time Alignment of Text-to-Image Diffusion Models｜2026-11-09
29. 底层视觉｜Preserving Cultural Records: A Large-Scale Benchmark and Visual-Prior Routing Network for Ancient Book Image Restoration｜2026-11-09
30. 底层视觉｜InfCoiL: Coordinated Planner-Controller Learning for Closed-Loop Physics-Based Human-Object Interaction｜2026-11-08

## 论文摘要

### 1. Improved CNN-Transformer Network for Neutron Image Super-Resolution

- 方向：底层视觉
- 作者：Yuheng Chu, Hongli Li, Tian Zhang
- 日期：2026-11-12
- 分类：cs.CV
- 关键词：image restoration、image super-resolution
- arXiv：2611.16620v1

摘要：

The spatial resolution of neutron images is of great importance for material defect diagnosis, structural characterization, and nondestructive testing. However, owing to limitations in neutron beam quality, scintillator conversion efficiency and light scattering, detector pixel size, and noise levels, conventional neutron images often suffer from speckle noise, blurred edges, and missing details, making them inadequate for high-precision analysis. To address these issues, an improved super-resolution model combinin...

### 2. Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control

- 方向：底层视觉、视频处理
- 作者：Haitian Li, Tianfu Li, Xuxi Zhao, Zizheng Liu, Yangcheng Yu, Yiwen Hou, et al.
- 日期：2026-11-10
- 分类：cs.RO, cs.CV
- 关键词：denoising、video denoising
- arXiv：2611.14257v1

摘要：

World-Action Models improve robot control by predicting future visual dynamics, but iterative video denoising incurs substantial inference overhead. Recent approaches reduce this cost through partial future denoising, yet typically rely on fixed refinement budgets. Our empirical observations reveal that preferred refinement depths vary across tasks and states, while different future regions exhibit varying relevance to action generation. Motivated by these findings, we propose Elastic-WAM, which adaptively allocate...

### 3. When to Start Denoising? Adaptive Denoising Entry for Generative Video Compression

- 方向：底层视觉、视频处理
- 作者：Zifu Zhang, Yuqiao Li, Ding Ding, Shengxi Li, Mai Xu, Daowen Li, et al.
- 日期：2026-11-10
- 分类：cs.CV
- 关键词：denoising、video compression
- arXiv：2611.13620v1

摘要：

Generative video compression offers a promising solution for compressing and reconstructing videos under extremely low bitrate constraints, among which the diffusion-based solutions still achieve the best performance by providing the powerful generative latent prior. However, their effectiveness critically depends on when the compressed latent is introduced into the diffusion process, which directly governs the trade-off between reconstruction fidelity and perceptual realism. To address this limitation, we identify...

### 4. Flex-DDCM: Zero-Shot Task-Oriented Image Compression via Diffusion Trajectory Guidance

- 方向：底层视觉
- 作者：Yixin Gao, Runsen Feng, Xin Li, Zhibo Chen
- 日期：2026-11-08
- 分类：cs.CV, cs.LG
- 关键词：denoising、image compression
- arXiv：2611.11427v1

摘要：

Recent zero-shot image compression methods exploit the powerful priors of pretrained diffusion models to produce perceptually pleasing reconstructions without compression-specific training. However, image compression serves not only human viewing but also machine analysis, while existing zero-shot codecs have limited flexibility in meeting the diverse reconstruction requirements of these applications. In this paper, we propose Flex-DDCM, a framework for zero-shot task-oriented image compression via diffusion trajec...

### 5. eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation

- 方向：底层视觉
- 作者：Tong Zhao, Xianfang Zeng, Yucheng Han, Ruoyu Wang, Mingkun Lei, Gang Yu, et al.
- 日期：2026-11-12
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.17194v1

摘要：

Distribution matching distillation (DMD) has emerged as a leading paradigm for distilling diffusion models into few-step students, where an auxiliary fake score model tracks the student's distribution and the discrepancy between the teacher and fake predictions drives the student toward the teacher. In multi-step distillation, although only the student's final output is delivered, existing methods train the fake model on intermediate states or across all denoising steps. Consequently, the student's update signal be...

### 6. HiVE-VQA: Hierarchical Interaction via Volumetric Embedding for Video Quality Assessment

- 方向：视频处理
- 作者：Robbie Hamilton, Fan Zhang, David Bull
- 日期：2026-11-12
- 分类：cs.CV
- 关键词：video quality assessment
- arXiv：2611.17146v1

摘要：

The proliferation of user-generated video content has made accurate and robust no-reference video quality assessment (NR-VQA) a highly important challenge. Existing research increasingly relies on architecturally complex multi-branch pipelines or computationally intensive fine-tuning of single-branch backbones. In this paper, we investigate whether a single frozen video foundation model can serve as an effective NR-VQA backbone, and propose HiVE-VQA, the first framework (to our knowledge) to apply a JEPA-based vide...

### 7. TokenStream: Multi-Subject Personalized Video Generation with Token-wise LoRA and Guided Attention

- 方向：底层视觉
- 作者：Hung Nguyen, Quang Qui-Vinh Nguyen, Khoi Nguyen
- 日期：2026-11-12
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.16897v1

摘要：

We introduce TokenStream, an optimization-based framework that composes independently learned subject identities in text-to-video generation without a reference-video training dataset or joint optimization of each new subject combination. Learning from a single reference image makes subject appearance difficult to separate from static-image bias, while merging independently trained adapters can mix identities. Token-wise LoRA (ToRA) restricts low-rank updates to the cross-attention value projections of subject-asso...

### 8. What Limits Thermal Infrared Drone Detection? A Cross-Dataset Benchmark Analysis

- 方向：底层视觉
- 作者：Tamara R. Lenhard, Jan Kels, Tobias Koch
- 日期：2026-11-12
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2611.16724v1

摘要：

Thermal infrared (IR) imaging enables drone detection with reduced dependence on ambient illumination, supporting continuous surveillance beyond the limitations of visible-spectrum sensing. However, substantial and often undocumented variability in camera systems, processing pipelines, and annotation practices across public IR drone datasets complicates the assessment of detector performance and cross-domain generalization. To examine these sources of variability and their implications for drone detection, we syste...

### 9. PiLLVD: A Real-World Low-Light Video Dataset for Dynamic Scenes Captured with Off-the-Shelf Cameras

- 方向：视频处理
- 作者：Yaser Abu Awwad, Paul L. Rosin, Oktay Karakuş
- 日期：2026-11-12
- 分类：cs.CV, eess.IV
- 关键词：video enhancement
- arXiv：2611.16515v1

摘要：

Low-light image and video enhancement has received increasing attention in recent years. However, most existing enhancement methods are developed and evaluated on still images, while progress in low-light video enhancement remains limited by the lack of real-world paired video datasets. Acquiring paired low-light and normal-light video sequences is challenging because it requires spatially and temporally aligned captures while avoiding motion blur, exposure mismatch, and correspondence errors in dynamic scenes. To...

### 10. HIFC-IQA: Train-Free Cross-Domain Image Quality Assessment via Dual-Process Cognition

- 方向：底层视觉
- 作者：Yu Li, Zhengran Shen, Puchao Zhou, Yukang Ding, Yachun Mi, Boyuan Yang, et al.
- 日期：2026-11-12
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2611.16451v1

摘要：

The gap between controlled synthetic distortions and complex real-world degradations introduces a critical domain shift challenge for No-Reference Image Quality Assessment. Although Unsupervised Domain Adaptation (UDA) approaches attempt to address this issue, they remain constrained by substantial retraining overhead and cumulative error propagation inherent in iterative pseudo-labeling. Inspired by the dual-process theory of human cognition for remarkable generalization ability, we propose Hierarchical Intuitive...

### 11. TRACE: Trajectory Synchronization for Training-Free Resolution Extension in Video Generation

- 方向：底层视觉
- 作者：Libo Zhu, Fan Li, Zhixin Wang, Binglu Wang, Weisheng Dong, Yulun Zhang
- 日期：2026-11-11
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.15983v1

摘要：

More text-to-video models are available, but many remain limited to low resolutions. Training them for higher resolutions is costly, while existing training-free methods still struggle with fine detail, scene structure, and efficiency. We propose TRACE, a training-free method that synchronizes low- and high-resolution generation trajectories. During early denoising, TRACE aligns predicted scene content at corresponding noise levels. It computes high-resolution updates from low-resolution predictions and the current...

### 12. Taming Neural Fields with a Frequency-Lipschitz Curriculum for Sparse-View CT Reconstruction

- 方向：底层视觉
- 作者：Songtao Hu, Jingrui Wu, Hong Ding, Fanhao Zhu, Yunhao Liu, Suyang Xi
- 日期：2026-11-11
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2611.15652v1

摘要：

Sparse-view computed tomography (SVCT) reduces radiation dose by acquiring fewer projection views, but the resulting under-determined inverse problem requires careful regularization to prevent reconstruction algorithms from fitting streak artifacts and hallucinated structures. Existing implicit neural representation (INR) methods rely on implicit spectral bias or iterative external denoising, yet they provide limited control over when high-frequency capacity is exposed during optimization. To address this limitatio...

### 13. WaveFlow-UIE: A Single-Pipeline Wavelet-Domain Flow Model for Efficient Underwater Image Restoration

- 方向：底层视觉
- 作者：Abdulaziz Alfaraj, Mohammed Al Naser, Hassan Al Nasser, Muzammil Behzad
- 日期：2026-11-11
- 分类：cs.CV, cs.AI
- 关键词：image restoration
- arXiv：2611.15457v1

摘要：

Underwater image restoration remains challenging because color distortion, scattering, and detail loss affect low- and high-frequency image components differently. Recent diffusion-based methods have shown strong restoration quality, but often rely on multi-stage pipelines and costly iterative refinement. We present WaveFlow-UIE, a single-pipeline wavelet-domain flow model that directly learns to transform degraded underwater wavelet representations into clean ones. Our method applies a discrete wavelet transform,...

### 14. Reading the Unreadable: Text-Aware Image Super-Resolution Needs Reasoning

- 方向：底层视觉
- 作者：Jaeseong Lee, Jinwoo Kim, Jinho Jeong, Seon Joo Kim
- 日期：2026-11-11
- 分类：cs.CV, cs.AI
- 关键词：image super-resolution
- arXiv：2611.15449v1

摘要：

Text-aware image super-resolution (TAISR) aims to recover high-resolution images from low-resolution inputs while preserving textual content. Existing methods treat this as a visual restoration problem, yet severely degraded text often cannot be read from local visual evidence alone. Humans instead read it by reasoning over image context, logical patterns, and prior knowledge. This raises a fundamental question: Does TAISR need reasoning? To answer this, we introduce two diagnostic tools. The first, ReasonText, is...

### 15. CARE-Drive: Coupled Alternating Refinement for Ego-trajectories

- 方向：底层视觉
- 作者：Xiao Ma, Yijun Chen, Zhiquan Hu, Jicheng Zhao, Yuming Li, Chuang Dai
- 日期：2026-11-11
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2611.15360v1

摘要：

Vision-language-action (VLA) models bring multimodal understanding and world knowledge to end-to-end autonomous driving. To further improve the quality of predicted trajectories, existing studies introduce candidate refinement, residual denoising, and token correction. However, these methods typically focus on unified refinement of the entire trajectory, paying limited attention to the distinct physical quantities and their interactions. We further investigate physical specialization and coordination in trajectory...

### 16. C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference

- 方向：底层视觉
- 作者：Guorui Lu, Qinyu Chen
- 日期：2026-11-10
- 分类：cs.CV, cs.LG
- 关键词：image compression
- arXiv：2611.14469v1

摘要：

Visual Question Answering (VQA) imposes substantial computational overhead on vision-language models (VLMs), motivating model-agnostic input reduction methods that can be readily applied across diverse VLMs, including in black-box settings. Simply enforcing a visual-token cap reduces computation, but it can discard information needed to answer the question. A single reduction strategy also struggles to accommodate different scenarios. Our key observation is that cropping and compression are complementary: cropping...

### 17. From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models

- 方向：底层视觉
- 作者：Guoqiang Liang, Yiqi Lin, Yanzhe Chen, Kevin Yuchen Ma, Mike Zheng Shou
- 日期：2026-11-10
- 分类：cs.CV, cs.RO
- 关键词：denoising
- arXiv：2611.14365v1

摘要：

Pretrained video diffusion models (VDMs) offer a powerful foundation for World Action Models (WAMs), which jointly predict robot actions and future observations. Building such models requires injecting low-dimensional robot signals (e.g. proprioception, actions, and values) into a latent space shaped by natural videos, and a key design choice is the interface through which these signals enter: existing schemes treat it as a formatting detail, spending a separate latent frame on each signal or bolting on dedicated e...

### 18. TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation

- 方向：底层视觉
- 作者：Qijun Gan, Chenwei Zhang, Xinyang Li, Meiguang Jin, Junfeng Ma
- 日期：2026-11-10
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.14307v1

摘要：

Streaming multi-reference video generation establishes a scene from specified people and objects, then continues it under changing instructions. We introduce TaoMate-R1, a streaming multi-reference generator that organizes adaptation parameters through temporal role specialization. It assigns separate low-rank adapters to scene establishment and continuation on a frozen backbone. Each adapter performs both denoising and context writing for its role; Self Gradient Forcing jointly trains the roles through the history...

### 19. Lipschitz-Controlled Flow Matching for Robust Image Restoration

- 方向：底层视觉
- 作者：Sedjro Salomon Hotegni, Konstantin Sonntag, Paul-Christian Bürkner, Sebastian Peitz
- 日期：2026-11-10
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2611.13995v1

摘要：

Flow-matching models can produce high-quality image restorations, but their learned dynamics may amplify small input perturbations and make reconstructions unstable. We introduce LipsFlower to reduce this amplification. We derive stability bounds for Flow-from-$Y$, which initializes the ordinary differential equation from a noise-perturbed observation, as well as for observation-conditioned posterior sampling, which conditions the velocity field on the observation throughout integration. Based on this analysis, we...

### 20. Adapting a Vision Foundation Model for Fracture Characterization in Acoustic Image Logs

- 方向：底层视觉
- 作者：Guangyu Wang, Xiaodong Ma, Xinming Wu
- 日期：2026-11-10
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2611.13911v1

摘要：

Natural fractures (NFs) and drilling-induced tensile fractures (DITFs) in acoustic image logs provide insights into rock mass structure and in situ stress, but manual characterization is time-consuming. Deep learning can automate this task, although expert-labeled data are scarce. We investigate whether adapting a pretrained vision foundation model (VFM) outperforms task-specific models trained from scratch with limited annotations. Using 80 annotated acoustic image samples, we fine-tuned DINOv3, pretrained on sate...

### 21. DUO: Dual Readouts of Diffusion Models for OOD Detection

- 方向：底层视觉
- 作者：Alireza Javid, Shirin Shoushtari, Nuria González Prelcic
- 日期：2026-11-09
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2611.13304v1

摘要：

Diffusion models are powerful generative methods for learning and sampling from complex data distributions. Safely deploying these models requires detecting inputs that fall outside their training distribution. Because diffusion models recover clean samples from noisy inputs, reconstruction error is often used for out-of-distribution (OOD) detection. This approach assumes that in-distribution (ID) inputs are reconstructed more accurately than OOD inputs. However, OOD inputs may be reconstructed equally well or even...

### 22. Just Image Transformers with Late-Stage Pixel Refinement

- 方向：底层视觉
- 作者：Denis Lukovnikov, Andreas Müller, Asja Fischer
- 日期：2026-11-09
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2611.13120v1

摘要：

Recent work on latent-free diffusion transformers has demonstrated the feasibility of training image generators without a latent VAE. This avoids compression artifacts from the VAE and simplifies the training pipeline. In particular, JiT showed that even a standard transformer can be trained to generate images when the model is trained to predict the final image ($x$-prediction). Even though JiT unlocks training efficiency comparable to latent models, it still suffers from reduced image quality likely arising from...

### 23. Real-Time Volumetric Light Transport Inference without a Path

- 方向：底层视觉
- 作者：Ludwic Leonard, Ruediger Westermann
- 日期：2026-11-09
- 分类：cs.GR, cs.CV
- 关键词：denoising
- arXiv：2611.12103v1

摘要：

We present a real-time method for reconstructing fully integrated pixel radiance in rendered volumetric media under direct and ambient environmental illumination, using compact, low-cost scene features and statistics. Unlike Monte Carlo denoising pipelines for volumetric rendering, which depend on computationally expensive path-traced radiance estimates, our approach directly infers the final light-transport solution from inexpensive primary-ray and environment sample evaluations. We show that these features form a...

### 24. MPEG-Diffusion: Mixed-Resolution Video Generation

- 方向：底层视觉
- 作者：Dennis Menn, Tianpei Gu, Guande He, Aryan V S, Yanke Song, Nan Liu, et al.
- 日期：2026-11-09
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.12069v1

摘要：

Video diffusion transformers (DiTs) generate realistic videos, but their heavy computational cost limits broader real-world applications. Mixed-resolution generation reduces this cost by generating the visually important region at high resolution (HR) and the rest at low resolution (LR), yet existing methods suffer a severe quality drop on videos and require knowing the HR region in advance. We show that these failures are not inherent to mixed resolution, and propose $\textbf{MPEG-Diffusion}$ to address their thre...

### 25. Four-Step Text-Bearing Image Generation via Distillation with Local Response Regularization and Teacher-Guided Training

- 方向：底层视觉
- 作者：Kairui Wen, Sheng Ye, Yong-Jin Liu
- 日期：2026-11-09
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.12042v1

摘要：

Generating text-bearing images requires coherent scenes and accurate characters. Large text-to-image models improve both capabilities through repeated denoising, at substantial sampling cost. Few-step distillation reduces this cost but requires the student to organize scenes and refine glyphs within a short trajectory. We present a four-step distillation framework combining local response regularization with teacher-guided text training. Built on distribution matching, the framework distills the GLM-Image DiT while...

### 26. Single Image Super-Resolution via Semantic Prompt and Cross-Modal Training on Content Area

- 方向：底层视觉
- 作者：Xiao Tan
- 日期：2026-11-09
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2611.12025v1

摘要：

Enhancing image quality through super-resolution is crucial in image and video processing. While contemporary deep learning models, such as CNNs and Transformers, excel in pixel-level enhancements, they often overlook the rich semantic context within images. To address this, we introduce a novel approach that synergizes pixel intensity with semantic information for superior detail recovery. Our method involves extracting semantic data, including textual descriptors and spatial positioning, and encoding this informa...

### 27. MUTE: Multi-Level Alignment Uncoupling Against Talking-Head Exploitation for Voice Protection

- 方向：底层视觉
- 作者：Donghyun Kim, Jin Hong, Seungmin Kim, Dain Kim, Junseok Kwon, Daeseon Choi
- 日期：2026-11-09
- 分类：cs.SD, cs.CV, cs.LG
- 关键词：denoising
- arXiv：2611.11989v1

摘要：

Talking-head generation models, which synthesize realistic facial animations from audio, are increasingly vulnerable to misuse in multimodal deepfake scenarios. Protecting such systems remains challenging, as talking-head models fundamentally rely on precise audio-visual alignment, while effective audio protection methods remain largely underexplored. In this work, we propose MUTE, an audio protection framework that uncouples the underlying audio-visual alignment through a multi-level strategy. Specifically, MUTE c...

### 28. Direct Trajectory Optimization for Inference-Time Alignment of Text-to-Image Diffusion Models

- 方向：底层视觉
- 作者：Huixuan Zhang, Li Lin, Junzhe Zhang, Xiaojun Wan
- 日期：2026-11-09
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2611.11821v2

摘要：

Alignment of text-to-image diffusion models with reward functions is a key challenge in controllable generation. Existing approaches typically rely on optimizing model inputs or fine-tuning denoising networks, which requires computationally expensive backpropagation through large denoising models. In this work, we propose Direct Trajectory Optimization (DTO), a training-free framework that performs alignment by directly optimizing the sampling trajectory of diffusion models. Specifically, DTO treats intermediate de...

### 29. Preserving Cultural Records: A Large-Scale Benchmark and Visual-Prior Routing Network for Ancient Book Image Restoration

- 方向：底层视觉
- 作者：Shumin Fan, Tianyu Song, Hongming Chen, Xiaodong Zhou, Xiang Chen
- 日期：2026-11-09
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2611.13010v1

摘要：

Ancient books preserve invaluable cultural heritage, yet their images often suffer from complex degradations caused by long-term ageing, environmental exposure, and physical damage. Existing ancient book image restoration benchmarks are limited in scale and rely on simplified degradation simulations, which cannot fully represent real-world degradation patterns and restrict the generalization ability of restoration models. To address these challenges, we introduce AncBench, a large-scale synthetic paired benchmark c...

### 30. InfCoiL: Coordinated Planner-Controller Learning for Closed-Loop Physics-Based Human-Object Interaction

- 方向：底层视觉
- 作者：Yude Zou, Yifei Yao, Yiwei Hao, Hanqing Wang, Xing Gao
- 日期：2026-11-08
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2611.11517v1

摘要：

Text- and goal-conditioned human-object interaction (HOI) provides an intuitive interface for specifying high-level intents in physics-based character animation. Mapping such intents to physically plausible, contact-rich behaviors naturally calls for a generative planner and a physics-based controller, yet existing planner-controller systems either execute plans open-loop or close the loop while keeping the planner fixed, so execution feedback never reshapes what is planned. We present InfCoiL, a closed-loop framew...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`latest.md`
