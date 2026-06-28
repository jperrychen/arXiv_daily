---
title: 2026-06-28｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-06-28｜底层视觉与视频论文速览

生成时间：2026-06-28

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜VSANet: View-aware Sparse Attention Network for Light Field Image Denoising｜2026-06-23
2. 视频处理｜UniRED: Unified RGB-D Video Frame Interpolation with Event Guidance｜2026-06-23
3. 底层视觉｜Poisson2Gaussian: Noise Gaussianization to Enhance Image Denoising｜2026-06-22
4. 底层视觉、视频处理｜ZeroGVC: Zero-Shot Generative Video Compression with Autoregressive Diffusion Priors｜2026-06-21
5. 底层视觉｜DnA: Denoising Attention for Visual Tasks｜2026-06-25
6. 底层视觉｜PhysiFormer: Learning to Simulate Mechanics in World Space｜2026-06-25
7. 底层视觉｜Focusing on What Matters: Saliency-Harnessing Accurate Routing for Diffusion MoE｜2026-06-25
8. 底层视觉｜MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation｜2026-06-25
9. 底层视觉｜TaskTok: Delving into Task Tokens for Task-driven Image Restoration｜2026-06-25
10. 底层视觉｜LogicIR: Logic Gate Networks for Image Restoration｜2026-06-25
11. 底层视觉｜A Benchmark for Heterogeneous Stereo Deblurring with Physically- and Epipolar-constrained Cross Attention｜2026-06-24
12. 底层视觉｜FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images｜2026-06-24
13. 底层视觉｜Shift Variant Image Degradation and Restoration Using Singular Value Decomposition｜2026-06-24
14. 底层视觉｜UniTeD: Unified Temporal Diffusion for Joint Perception and Planning in Autonomous Driving｜2026-06-24
15. 底层视觉｜Spatio-Temporal Mixture-of-Modality-Experts Diffusion for Quantitative DCE-MRI Synthesis from Incomplete MR Sequences｜2026-06-24
16. 底层视觉｜High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology｜2026-06-23
17. 底层视觉｜Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization｜2026-06-23
18. 底层视觉｜S1-Omni-Image: A Unified Model for Scientific Image Understanding, Generation, and Editing｜2026-06-23
19. 视频处理｜TIGER: Taming Identity, Geometry, and Generative Priors for High-Quality Face Video Restoration｜2026-06-23
20. 底层视觉｜MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving｜2026-06-23
21. 底层视觉｜Cyclic Denoising Reveals Ultrastable Memories in Diffusion Models｜2026-06-22
22. 顶会论文｜The Professor: Multi-Teacher Unsupervised Prompt Distillation for Vision-Language Models｜2026-06-22
23. 底层视觉｜C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model｜2026-06-22
24. 底层视觉｜Ocean4D: Generative Underwater 4D Reconstruction via Medium-Aware Video Diffusion｜2026-06-22
25. 底层视觉｜Safe Few-Step Generation via Velocity Editing｜2026-06-22
26. 底层视觉｜NGPS: Structure-Preserving Self-Supervised Denoising via Neighbor-Guided Patch Sampling｜2026-06-22
27. 底层视觉｜BEV-Denoise: Learning Intrinsic Noise for Accurate Bird's-Eye-View Semantic Segmentation｜2026-06-22
28. 底层视觉｜Learning Adaptive Dynamical Features via Multi-$τ$ Liquid-Mamba for All-in-one Image Restoration｜2026-06-22
29. 底层视觉｜FlowDec: Temporal Conditional Flow Decorruptor for Robust Continuous Vision-Language Navigation｜2026-06-21
30. 底层视觉｜Interest Entanglement: The Hidden Barrier to Blind Super-Resolution Optimization｜2026-06-21

## 论文摘要

### 1. VSANet: View-aware Sparse Attention Network for Light Field Image Denoising

- 方向：底层视觉
- 作者：Gargi Panda, Soumitra Kundu, Saumik Bhattacharya, Aurobinda Routray
- 日期：2026-06-23
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2606.24737v1

摘要：

Light field (LF) image denoising is challenging due to the high-dimensional structure of LF data. While noise is independent across sub-aperture images, scene content exhibits strong cross-view correlations. We introduce VSANet, a view-aware sparse attention network for LF denoising. Specifically, we propose a view-aware sparse attention (VSA) block that represents the 4D LF feature map as a unified spatial-angular token space and performs cross-view aggregation via locality-sensitive hashing-based sparse attention...

### 2. UniRED: Unified RGB-D Video Frame Interpolation with Event Guidance

- 方向：视频处理
- 作者：Yinuo Zhang, Guangshun Wei, Yuanfeng Zhou, Yiran Shen
- 日期：2026-06-23
- 分类：cs.CV
- 关键词：video interpolation、frame interpolation
- arXiv：2606.24282v1

摘要：

High frame-rate RGB-D videos are crucial for a variety of downstream tasks, including motion analysis, dynamic scene understanding, and 3D reconstruction. However, due to hardware and sensing constraints, practical RGB-D cameras are typically limited to low frame rates, making it difficult to capture rapid scene dynamics. Existing video interpolation methods have achieved strong performance on RGB data, but they are not readily applicable to RGB-D scenarios, where they often yield blurry boundaries, visible artifac...

### 3. Poisson2Gaussian: Noise Gaussianization to Enhance Image Denoising

- 方向：底层视觉
- 作者：Xirou Zhou, Zijing Xu, Yibo Qu, Qi Zhang, Xiaowan Hu, Xinyang Li
- 日期：2026-06-22
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2606.23098v1

摘要：

The quantum nature of light determines the inherent Poisson stochasticity of photon detection, which is ubiquitous in photography, microscopy, and astronomy. However, our controlled numerical studies reveal that the signal-dependency, heteroscedasticity, and statistical asymmetry of Poisson-mixed noise make it challenging for existing denoisers to learn. In contrast, i.i.d. Gaussian noise, with its statistical independence and symmetric distribution, is easier to model for networks. To address this gap, we propose...

### 4. ZeroGVC: Zero-Shot Generative Video Compression with Autoregressive Diffusion Priors

- 方向：底层视觉、视频处理
- 作者：Yixin Gao, Xiaohan Pan, Lin Liu, Xin Li, Zhibo Chen, Qi Tian
- 日期：2026-06-21
- 分类：eess.IV, cs.CV
- 关键词：denoising、video compression
- arXiv：2606.22371v2

摘要：

Recent generative video compression methods leverage powerful generative priors to achieve perceptually pleasing reconstructions. However, most existing approaches require additional training to adapt generative models to produce realistic reconstructions from compact representations. In this paper, we propose ZeroGVC, a zero-shot generative video compression framework that leverages pretrained autoregressive diffusion priors for low-delay video reconstruction. ZeroGVC encodes the first frame of each group of pictu...

### 5. DnA: Denoising Attention for Visual Tasks

- 方向：底层视觉
- 作者：Ron Campos, Subhajit Maity, Xin Li, Srijan Das, Aritra Dutta
- 日期：2026-06-25
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.27372v1

摘要：

The softmax activation in multihead attention (MHA) is the de facto standard for attention-based models in visual perception tasks. However, standard softmax can produce noisy attention patterns that dilute relevant features and degrade its performance. In this paper, we propose Denoising Attention or DnA, in which, first, a positive query identifies which image features belong to the correct class, and a negative query identifies closely associated but irrelevant image features. DnA then projects these interaction...

### 6. PhysiFormer: Learning to Simulate Mechanics in World Space

- 方向：底层视觉
- 作者：Yiming Chen, Yushi Lan, Andrea Vedaldi
- 日期：2026-06-25
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.27364v1

摘要：

We present PhysiFormer, a diffusion transformer for physically-plausible 3D object motion. Unlike video world models that operate in view-dependent pixel space, PhysiFormer represents objects as 3D meshes expressed in world coordinates. Given the initial vertex positions and velocities, as well as object material type, rigid or elastic, the model samples future vertex trajectories. While related neural physics approaches build on ad-hoc latent spaces or explicitly enforce rigidity and causality, PhysiFormer shows t...

### 7. Focusing on What Matters: Saliency-Harnessing Accurate Routing for Diffusion MoE

- 方向：底层视觉
- 作者：Haoyou Deng, Keyu Yan, Chaojie Mao, Xiang Wang, Yu Liu, Changxin Gao, et al.
- 日期：2026-06-25
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.26938v1

摘要：

Mixture-of-Experts (MoE) architectures have emerged as a powerful paradigm for scaling diffusion models in visual generation. Recent advancements have focused on adaptively allocating computational resources across diverse tokens to improve efficiency and performance. However, we identify a routing assignment problem in existing diffusion MoE frameworks: the router fails to accurately allocate more computational resources to salient tokens. Our analysis attributes this failure to the router's reliance on noise-corr...

### 8. MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation

- 方向：底层视觉
- 作者：Jingjun Gu, Chaojie Shen, Yifeng Cao, Wei Zhang, Yiliu Li, Aobo Fan
- 日期：2026-06-25
- 分类：eess.IV, cs.AI, cs.CV
- 关键词：denoising
- arXiv：2606.26712v1

摘要：

Skin lesion segmentation is a key task in computer-aided dermatological diagnosis, where accuracy directly impacts downstream analysis and disease classification. However, dermoscopic images are challenging due to blurred boundaries, low contrast, large shape variations, and artifacts such as hair and shadows. Recently, diffusion models have shown strong performance in medical image segmentation thanks to their progressive denoising and distribution modeling capabilities. Nevertheless, existing diffusion-based meth...

### 9. TaskTok: Delving into Task Tokens for Task-driven Image Restoration

- 方向：底层视觉
- 作者：Hongjae Lee, Sojung Kang, Jaeseong Yu, Seung-Won Jung
- 日期：2026-06-25
- 分类：cs.CV, eess.IV
- 关键词：image restoration
- arXiv：2606.26615v1

摘要：

While traditional image restoration focuses on perceptual quality, Task-Driven Image Restoration (TDIR) aims to maximize the performance of downstream high-level vision tasks. Recent approaches leveraging generative priors have shown promise for TDIR; however, they typically suffer from computational inefficiency and potential semantic alteration by indiscriminately updating all latent tokens. In this paper, we posit that not all visual information is equally important for machine perception. Through an analysis of...

### 10. LogicIR: Logic Gate Networks for Image Restoration

- 方向：底层视觉
- 作者：Hongjae Lee, Myungjun Son, Jaeseong Yu, Seung-Won Jung
- 日期：2026-06-25
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.26609v1

摘要：

Image restoration aims to reconstruct high-quality images from degraded low-quality inputs. As the computational demands of image restoration models continue to rise, there is growing interest in lightweight architectures optimized for fast and efficient inference. Logic gate networks (LGNs), which operate using fundamental logic operations such as NAND and XOR, have recently emerged as a promising direction for achieving highly efficient computation. However, their potential remains largely untapped in the domain...

### 11. A Benchmark for Heterogeneous Stereo Deblurring with Physically- and Epipolar-constrained Cross Attention

- 方向：底层视觉
- 作者：Hoju Shin, Jiah Kim, Seung-Wook Kim, Seowon Ji
- 日期：2026-06-24
- 分类：cs.CV
- 关键词：deblurring
- arXiv：2606.25962v1

摘要：

Modern stereo-capable smartphones enable immersive XR content capture. However, hardware heterogeneity across camera modules often causes severe asymmetric blur artifacts. Existing methods and benchmarks largely assume homogeneous stereo setups and therefore do not explicitly address such asymmetric degradation. To bridge this gap, we present a dedicated framework for heterogeneous stereo deblurring. First, we introduce the heterogeneous stereo deblurring (HSD) dataset, constructed from real smartphone stereo captu...

### 12. FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images

- 方向：底层视觉
- 作者：Pengwei Wang, José Morano, Virginia Mares, Hrvoje Bogunović
- 日期：2026-06-24
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2606.25915v1

摘要：

Color fundus photography (CFP) is the most common ophthalmic imaging modality for large-scale screening. However, it is highly susceptible to degradations, making robust fundus image quality assessment (FIQA) crucial. The criteria for what constitutes high-quality at the image level vary across clinical tasks, making FIQA dependent on expert knowledge. This motivated the development of automated methods and datasets. While existing datasets aim to standardize image-level quality, their criteria often differ. Furthe...

### 13. Shift Variant Image Degradation and Restoration Using Singular Value Decomposition

- 方向：底层视觉
- 作者：Arun D. Kulkarni
- 日期：2026-06-24
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.25818v1

摘要：

Shift-variant image degradation is frequently encountered in practical imaging systems where the point spread function (PSF) varies across the image field due to motion, optical aberrations, atmospheric turbulence, or sensor-related effects. Unlike shift-invariant, shift-variant degradation presents significant challenges for image restoration because the degradation process cannot be represented by a single convolution kernel. This paper proposes a singular value decomposition (SVD)-based framework for restoring i...

### 14. UniTeD: Unified Temporal Diffusion for Joint Perception and Planning in Autonomous Driving

- 方向：底层视觉
- 作者：Bo Zhao, Xinting Zhao, Naifan Li, Erkang Cheng, Haibin Ling
- 日期：2026-06-24
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.25736v1

摘要：

Diffusion models have shown strong potential for multi-modal planning in end-to-end autonomous driving. However, most existing methods confine diffusion to the planning module, conditioning on fixed outputs from separate discriminative perception networks. This decoupled design propagates perception errors to the planner, increasing optimization difficulty and reducing robustness. To overcome these limitations, we propose UniTeD, a Unified Temporal Diffusion framework that jointly models perception and planning thr...

### 15. Spatio-Temporal Mixture-of-Modality-Experts Diffusion for Quantitative DCE-MRI Synthesis from Incomplete MR Sequences

- 方向：底层视觉
- 作者：Junhyeok Lee, Kyu Sung Choi
- 日期：2026-06-24
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.25535v1

摘要：

Quantitative maps from dynamic contrast-enhanced MRI (DCE-MRI) are essential for tumor assessment but are often unavailable due to contrast-agent risks and protocol variability. Prior methods predict these maps from other MRI modalities, yet most assume fixed, fully observed inputs and fail under realistic missingness. We present Spatio-Temporal Mixture-of-Modality-Experts (ST-MoME), a conditional diffusion framework that synthesizes 3D DCE parameter maps from diverse subsets of multimodal MRI. ST-MoME fuses modali...

### 16. High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology

- 方向：底层视觉
- 作者：Johannes Boehm, Bappaditya Dey
- 日期：2026-06-23
- 分类：cs.CV, eess.IV
- 关键词：denoising
- arXiv：2606.24817v1

摘要：

Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse datasets needed for downstream machine learning (ML). Synthetic data generation is becoming essential, but current generative models often miss TEM-specific noise, structural detail, and stochastic variability crucial for evaluation. We present a Denoising Diffusion Probabilistic Model (DDPM) framework for syn...

### 17. Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization

- 方向：底层视觉
- 作者：Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, et al.
- 日期：2026-06-23
- 分类：cs.CV, cs.RO
- 关键词：low-level vision
- arXiv：2606.24767v1

摘要：

Indoor visual relocalization plays a critical role in emerging spatial and embodied AI applications. However, prior research was predominantly devoted to low-level vision schemes, struggling to perceive scene semantics and compositions, which limits both interpretability and applicability. In this paper, we explore the issue of how to organize rich object information in a scene, including semantics, layout, and geometry, into a structured map representation, thereby utilizing object units exclusively to drive the c...

### 18. S1-Omni-Image: A Unified Model for Scientific Image Understanding, Generation, and Editing

- 方向：底层视觉
- 作者：Qingxiao Li, Zikai Wang, Qingli Wang, Nan Xu
- 日期：2026-06-23
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2606.24441v1

摘要：

We present S1-Omni-Image, an open-weight unified multimodal model for scientific image understanding, generation, and editing. Unlike general-purpose image generation models, scientific image tasks require not only high-fidelity synthesis, but also robust understanding of scientific semantics, structural relations, domain knowledge, and task intent. To this end, S1-Omni-Image builds on the scientific multimodal reasoning backbone S1-VL-32B and couples its understanding capability with an image generation module und...

### 19. TIGER: Taming Identity, Geometry, and Generative Priors for High-Quality Face Video Restoration

- 方向：视频处理
- 作者：Yang Zhou, Wenxue Li, Peng Zhang, Yifei Chen, Fei Wang, Daiguo Zhou
- 日期：2026-06-23
- 分类：cs.CV
- 关键词：video restoration
- arXiv：2606.24336v1

摘要：

Face Video Restoration (FVR) aims to recover high-fidelity facial videos from degraded input while preserving identity and semantic consistency across frames. Existing methods often struggle to simultaneously address three key challenges: identity shift, viewpoint-entangled guidance, and perceptual realism. To tackle these issues, we propose TIGER, a structured tri-prior fusion framework that Tames Identity, Geometry, and gEnerative pRiors for high-quality FVR. Specifically, an Identity Prior is first established b...

### 20. MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving

- 方向：底层视觉
- 作者：Hongli Xiao, Youjian Zhang, Yucai Bai, Chaoyue Wang, Yaohui Jin, Xiaoguang Ren, et al.
- 日期：2026-06-23
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.24301v1

摘要：

Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment. However, most existing vehicle generation methods fail to fully exploit multimodal sensors i.e. multi-view images and LiDAR point clouds) and rely on neural rendering based reconstruction, leading to low-quality mesh. Recently, native 3D generative models have made significant progress, yet they are not built for arbitrary multi-view inputs and often struggle with in-t...

### 21. Cyclic Denoising Reveals Ultrastable Memories in Diffusion Models

- 方向：底层视觉
- 作者：Rishabh Sharma, Stefano Martiniani
- 日期：2026-06-22
- 分类：cs.LG, cond-mat.dis-nn, cs.CR, cs.CV
- 关键词：denoising
- arXiv：2606.24000v1

摘要：

We introduce cyclic denoising -- repeated forward and reverse diffusion at controlled noise amplitudes -- as an extraction attack for image diffusion models. Inspired by random organization in disordered solids, cyclic denoising exposes regions of the learned distribution that are largely inaccessible to standard sampling. The dynamics drive samples toward attractors with a broad stability spectrum. The deepest attractors are ultrastable: they regenerate after near-total corruption and persist through thousands of...

### 22. The Professor: Multi-Teacher Unsupervised Prompt Distillation for Vision-Language Models

- 方向：顶会论文
- 作者：Ahmad Algadhi, Ahmed Alzuhair, Omar Alkhulaif, Muzammil Behzad
- 日期：2026-06-22
- 分类：cs.CV, cs.AI
- 关键词：CVPR
- arXiv：2606.23897v1

摘要：

Prompt distillation compresses large vision-language models (VLMs) such as CLIP into lightweight student models by matching teacher predictions on unlabeled domain images. PromptKD (CVPR 2024) established this paradigm with a single PromptSRC-finetuned ViT-L/14 teacher and a ViT-B/16 student. We propose TheProfessor, a multi-teacher extension that distills from a fixed two-teacher ensemble: a domain-finetuned PromptSRC ViT-L/14 teacher and a zero-shot EVA-CLIP-L/14 teacher whose logits are pre-computed per dataset....

### 23. C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model

- 方向：底层视觉
- 作者：Wei Li, Jingyang Zhang, Guoan Wang, Junzhi Ning, Yang Chen, Guang Yang, et al.
- 日期：2026-06-22
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.23473v1

摘要：

Universal segmentation models exhibit significant potential for diverse tasks involving different imaging modalities and segmentation objectives. Task-Incremental Learning provides a privacy-preserving approach to continually evolve a universal model on tasks from sequentially-arriving medical departments. However, training the model solely on the incoming task induces forgetting on past tasks, since consecutive tasks exhibit concurrent shifts in image appearance and segmentation objective. To address this problem,...

### 24. Ocean4D: Generative Underwater 4D Reconstruction via Medium-Aware Video Diffusion

- 方向：底层视觉
- 作者：Yuqiang Huang, Yuxi Wang, Junyu Dong, Zhaoxiang Zhang
- 日期：2026-06-22
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.23298v1

摘要：

Underwater 4D reconstruction remains challenging due to the coupling between degraded light transport in participating media and dynamic water variations. Most existing Methods are developed under in-air assumptions and do not explicitly account for underwater absorption and backscatter. Additionally, near-static assumptions make these approaches sensitive to drifting particles and dynamic distractors , leading to unstable geometry and inconsistent cross-view results. To address these issues, we propose a generativ...

### 25. Safe Few-Step Generation via Velocity Editing

- 方向：底层视觉
- 作者：Yujin Choi, Jaehong Yoon
- 日期：2026-06-22
- 分类：cs.CV, cs.CY
- 关键词：denoising
- arXiv：2606.23267v1

摘要：

Flow matching has recently emerged as a strong paradigm for state-of-the-art text-to-image (T2I) generation, enabling high-quality generation with a small number of sampling steps. As these models are increasingly integrated into real-world applications, ensuring safe and non-sensitive content generation has become a critical requirement. However, adapting safety and concept removal methods to this new generation framework remains an open challenge. Specifically, prior methods largely rely on iterative trajectory s...

### 26. NGPS: Structure-Preserving Self-Supervised Denoising via Neighbor-Guided Patch Sampling

- 方向：底层视觉
- 作者：Jaehyun Cho, YoungJoon Yoo
- 日期：2026-06-22
- 分类：eess.IV, cs.CV
- 关键词：denoising
- arXiv：2606.23200v1

摘要：

Neighboring-slice self-supervised denoising is attractive for volumetric medical imaging, yet inter-slice misalignment breaks anatomical correspondence and often yields ghosting and blurred margins when adjacent slices are used naively as targets. We propose Neighbor-Guided Patch Sampling (NGPS), a lightweight framework that constructs neighboring supervision under local inter-slice misalignment without explicit registration. To avoid learning from misleading targets, prior methods commonly mask discrepant regions,...

### 27. BEV-Denoise: Learning Intrinsic Noise for Accurate Bird's-Eye-View Semantic Segmentation

- 方向：底层视觉
- 作者：Dooseop Choi, Kyounghwan An, Kyoung-Wook Min
- 日期：2026-06-22
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2606.22931v1

摘要：

In this paper, we present a framework dubbed \textbf{BEV-Denoise} that estimates and removes intrinsic noise from learned Bird's-Eye-View (BEV) features to achieve accurate BEV semantic segmentation. Inspired by the noise estimation capability of Denoising Diffusion Probabilistic Models (DDPM), we design a UNet-based noise estimation module that learns to estimate the noise from the learned BEV features. The estimated noise is then subtracted from the BEV features and fed to BEV map decoders for the final predictio...

### 28. Learning Adaptive Dynamical Features via Multi-$τ$ Liquid-Mamba for All-in-one Image Restoration

- 方向：底层视觉
- 作者：Hu Gao, Changshuo Wang, Yulong Chen, Lizhuang Ma
- 日期：2026-06-22
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.22801v1

摘要：

Image restoration aims to recover high-quality images from degraded observations. Recent Mamba-based image restoration models have demonstrated strong potential in modeling long-range dependencies with linear complexity. However, most existing designs still rely on a single state-evolution timescale, which limits their adaptability to spatially heterogeneous and task-dependent degradation patterns in all-in-one image restoration. In this paper, we propose Multi-$τ$ Liquid-Mamba, an adaptive state space module that...

### 29. FlowDec: Temporal Conditional Flow Decorruptor for Robust Continuous Vision-Language Navigation

- 方向：底层视觉
- 作者：Yufei Zhang, Changhao Chen
- 日期：2026-06-21
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.22424v2

摘要：

Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires agents to follow natural-language instructions in unseen scenes. While Large Models (LMs) have advanced VLN-CE, their performance remains severely degraded by real-world visual corruptions, a critical yet underexplored domain constraint. We introduce Temporal Conditional Flow Decorruptor (FlowDec), a novel image restoration framework tailored for LM-based VLN-CE. FlowDec integrates a hybrid temporal conditioning strategy to align the genera...

### 30. Interest Entanglement: The Hidden Barrier to Blind Super-Resolution Optimization

- 方向：底层视觉
- 作者：Junxiong Lin, Xinji Mai, Qianyu Guo, Haoran Wang, Zeng Tao, Xuan Tong, et al.
- 日期：2026-06-21
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2606.22353v1

摘要：

Fidelity and perceptual quality are two inherently competing and conflicting objectives in the image super-resolution (SR) task. Different loss functions focus on these objectives to varying extents. Regression losses enhance the model's fidelity but lack sufficient attention to high-frequency details, resulting in a loss of fine details. In contrast, perception losses improve the model's visual quality but may introduce undesirable artifacts. Balancing these two optimization goals can be viewed as a Multi-Objectiv...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-06-28-low-level-vision-video-papers.md`
