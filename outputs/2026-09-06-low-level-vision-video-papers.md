---
title: 2026-09-06｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-09-06｜底层视觉与视频论文速览

生成时间：2026-09-06

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜P-PatchDiff: Progressive Patch Diffusion Models for Low-light Image Enhancement｜2026-09-01
2. 底层视觉、视频处理｜DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation｜2026-09-03
3. 底层视觉、视频处理｜SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving｜2026-09-03
4. 底层视觉｜Perceptually Regularized Diffusion Model for Image Super-Resolution｜2026-09-02
5. 顶会论文｜SynCrash: A Multi-Stage Pipeline for Zero-Shot Accident Detection and Localization in Traffic Surveillance Video｜2026-08-30
6. 底层视觉｜Mapping-Based Image Diffusion｜2026-08-29
7. 底层视觉｜SPARK: Input-Conditioned Sparse Activation Modulation for Frozen DiT-based Super-Resolution｜2026-09-03
8. 底层视觉｜ToPO: Token-Conditioned Preference Routing for Attention-Based Latent Diffusion Models｜2026-09-03
9. 底层视觉｜Tree-Structured Vector Quantization For Efficient And Progressive Image Compression｜2026-09-03
10. 底层视觉｜FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow｜2026-09-03
11. 视频处理｜Neural Video Compression Based on Deformable Temporal Alignment and Difference-aware Fusion｜2026-09-03
12. 底层视觉｜SafeRestore: Detector-Relative Risk Certificates for Selective Industrial Image Restoration｜2026-09-03
13. 底层视觉｜Learning to Attract and Repel: Dual Quality Margin Learning for Face Recognition (DQM-Face)｜2026-09-02
14. 底层视觉｜Fine-Grained Anomaly Perception in Wild UGC-Enhanced Images: A Comprehensive Dataset and Difference-Fusion Framework｜2026-09-02
15. 底层视觉｜UnCapsTSR: An Unsupervised Transformer-based Image Super-Resolution Approach for Capsule Endoscopy Images｜2026-09-02
16. 底层视觉｜ProSR: Semantic-Prototype-Guided Discrete Modeling for Physically Consistent SAR Super-Resolution｜2026-09-02
17. 视频处理｜VoRTeC: Taming Foundation Flow for One-step Real time Video Compression｜2026-09-02
18. 底层视觉｜LaST-SR: Laplace-Inspired Steady-Transient Complex-Frequency Decomposition for Single Image Super-Resolution｜2026-09-02
19. 底层视觉｜SelfLift: Accelerating Few-Step Diffusion via Self-Recovering Resolution Transition｜2026-09-02
20. 底层视觉｜InstEditSeg: Instruction-Driven Image Editing for Polyp and Skin Lesion Segmentation｜2026-09-02
21. 底层视觉｜Linear Fusion MultiDiffusion for Fast Training-Free Spherical Panorama Generation｜2026-09-02
22. 底层视觉｜SliceBridge: context-consistent repair of corrupted slice intervals in T1-weighted MRI｜2026-09-01
23. 底层视觉｜Reliability Challenges in Diffusion Vision-Language Models｜2026-09-01
24. 底层视觉｜TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models｜2026-09-01
25. 底层视觉｜One Prompt Is Enough: Watermark Laundering Through Foundation Image Models｜2026-09-01
26. 底层视觉｜Physics-Driven Independent Pair Generation for Iterative Self-Supervised Low-Dose CT Denoising｜2026-09-01
27. 底层视觉｜ASSERT: Adaptive Stochastic Sampling for Robust Diffusion Models on Analog Compute-in-Memory Hardware｜2026-09-01
28. 底层视觉｜Denoising Diffusion Generative Models Secretly Calculate Attentions｜2026-09-01
29. 底层视觉｜ReBridge-Flow: Re-Coupling Posterior Bridges in Flow Matching for Image Restoration｜2026-09-01
30. 底层视觉｜EarthLD: Towards Unified Open-World Landslide Understanding via Vision-Language Guided Diffusion Models｜2026-09-01

## 论文摘要

### 1. P-PatchDiff: Progressive Patch Diffusion Models for Low-light Image Enhancement

- 方向：底层视觉
- 作者：Ruoyu Guo, Haonan Zhong, Maurice Pagnucco, Yang Song
- 日期：2026-09-01
- 分类：cs.CV
- 关键词：image restoration、denoising、image enhancement
- arXiv：2609.01123v1

摘要：

Recent advancements in low-light image enhancement have leveraged diffusion models for their strong ability to generate perceptually realistic, detailed images. Patch diffusion models further offer a promising solution to size-agnostic image restoration while improving efficiency. However, existing methods typically rely on small, fixed patches (e.g., 64$\times$64) that cannot capture image-level brightness context, whereas enlarging the receptive field improves brightness and colour estimation but substantially in...

### 2. DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation

- 方向：底层视觉、视频处理
- 作者：Shuaiting Li, Zelin Gao, Haibin Shen, Yujun Shen, Haotong Qin, Yinghao Xu
- 日期：2026-09-03
- 分类：cs.CV
- 关键词：denoising、video denoising
- arXiv：2609.04031v1

摘要：

Video diffusion models (VDMs) have achieved impressive progress in text-to-video generation, but their high memory and computational costs hinder practical deployment. Quantization-aware training (QAT) is an effective solution for compressing and accelerating advanced generative models without runtime overhead at inference. However, existing QAT methods suffer from a distinctive challenge in VDMs: while they often preserve prompt semantics, global layout, and coarse motion, the quantized model severely degrades vis...

### 3. SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving

- 方向：底层视觉、视频处理
- 作者：Jinyang Wang, Shiwei Li, Junjian Wang, Zhiqiang Deng, Jianbin Gao, Yihang Zhao, et al.
- 日期：2026-09-03
- 分类：cs.CV, cs.RO
- 关键词：denoising、video denoising
- arXiv：2609.03602v1

摘要：

World models (WMs) have demonstrated strong potential for end-to-end autonomous driving by learning predictive representations of future scene dynamics. However, generating future videos during inference introduces substantial computational overhead, leading many recent driving WMs to adopt a single front camera as input for efficient deployment. This design restricts spatial coverage in safety-critical maneuvers such as lane changes, merges, and turns. To address this limitation, we propose SV-WAM, a surround-view...

### 4. Perceptually Regularized Diffusion Model for Image Super-Resolution

- 方向：底层视觉
- 作者：Chuxiangbo Wang, Pavithra Venkatachalapathy, Ying Liang, Min Wang, Jing Qin, Yifei Lou, et al.
- 日期：2026-09-02
- 分类：eess.IV, cs.CV, cs.LG
- 关键词：image super-resolution、super resolution
- arXiv：2609.02016v1

摘要：

Image super-resolution, which aims to reconstruct high-resolution images from their low-resolution observations, is fundamental to medical imaging, remote sensing, surveillance, microscopy, and scientific visualization. Traditional model-based methods formulate super-resolution as an inverse problem with hand-crafted regularization priors. While interpretable and theoretically grounded, they rely on fixed assumptions and require computationally intensive iterative solvers. Deep learning methods offer data-driven fl...

### 5. SynCrash: A Multi-Stage Pipeline for Zero-Shot Accident Detection and Localization in Traffic Surveillance Video

- 方向：顶会论文
- 作者：Arkya Jyoti Bagchi, Ritul Jangir, Varun Raskar
- 日期：2026-08-30
- 分类：cs.CV, cs.AI
- 关键词：CVPR 2026、CVPR
- arXiv：2608.29759v1

摘要：

We present SynCrash, a multi-stage pipeline for zero-shot accident detection, spatial localization, and collision-type classification in fixed-view CCTV surveillance video. Our approach addresses the ACCIDENT at CVPR 2026 Challenge, which requires predicting when an accident occurs, where in the frame the impact happens, and what type of collision it is, all without access to labeled real-world training data. The pipeline operates in three decoupled stages: (1) Temporal localization via a VideoMAEv2-giant backbone...

### 6. Mapping-Based Image Diffusion

- 方向：底层视觉
- 作者：Freddie Åström, Michael Felsberg, George Baravdish
- 日期：2026-08-29
- 分类：cs.CV
- 关键词：denoising、image enhancement
- arXiv：2608.29164v1

摘要：

In this work, we introduce a novel tensor-based functional for targeted image enhancement and denoising. Via explicit regularization, our formulation incorporates application dependent and contextual information using first principles. Few works in literature treat variational models that describe both application dependent information and contextual knowledge of the denoising problem. We prove the existence of a minimizer and present results on tensor symmetry constraints, convexity, and geometric interpretation o...

### 7. SPARK: Input-Conditioned Sparse Activation Modulation for Frozen DiT-based Super-Resolution

- 方向：底层视觉
- 作者：Federico Putamorsi, Leonardo Zini, Marcella Cornia, Lorenzo Baraldi
- 日期：2026-09-03
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2609.03813v1

摘要：

Real-world image super-resolution (SR) increasingly relies on Diffusion Transformer (DiT) backbones, whose internal activations can be dominated by a small number of massive channels. Yet improving perceptual quality in these models still typically requires fine-tuning the network or attaching additional adapters, leaving this structured activation space largely unexplored for adaptation. We investigate whether dominant channels can instead serve as a compact adaptation interface for frozen DiT-based SR models. We...

### 8. ToPO: Token-Conditioned Preference Routing for Attention-Based Latent Diffusion Models

- 方向：底层视觉
- 作者：Juntao Xu, Shihong Li, Hoi Fan Au, Ning Zhu
- 日期：2026-09-03
- 分类：cs.CV
- 关键词：denoising
- arXiv：2609.03688v1

摘要：

Pairwise preference labels rank complete images, yet Diffusion-DPO applies their effect over many spatial and denoising-time coordinates. For attention-based, noise-prediction latent diffusion, ToPO (Token-Oriented Preference Optimization) constructs a per-minibatch, detached, separable spatial-temporal route from branchwise squared-residual contrast in a frozen reference denoiser. Preferred-branch cross-attention uses content tokens to modulate the spatial factor, and an auxiliary pixel-midpoint ordering term is a...

### 9. Tree-Structured Vector Quantization For Efficient And Progressive Image Compression

- 方向：底层视觉
- 作者：Xinkun Wang, Tianyi Xu, Qingyu Luo, Mingming Ma, Changzhe Jiao, Fu Li, et al.
- 日期：2026-09-03
- 分类：cs.CV
- 关键词：image compression
- arXiv：2609.03641v1

摘要：

Vector-quantization based image compression has achieved strong rate--distortion performance, yet most of them still produce a separate compressed representation for each target bitrate. Such variable-rate behavior allows one model to operate at multiple rates, but it does not necessarily provide a progressive bitstream whose prefixes are themselves decodable and can be refined by appending additional bits. We propose \textbf{Tree-VQ}, a progressive tree-structured vector quantization framework for learned image co...

### 10. FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow

- 方向：底层视觉
- 作者：Byeongjun Park, Byung-Hoon Kim, Hyungjin Chung
- 日期：2026-09-03
- 分类：cs.CV
- 关键词：denoising
- arXiv：2609.03563v1

摘要：

We present FlashRender, a few-step generative rendering framework that retakes a source video along a target camera trajectory in seconds. We identify sampling-step-dependent camera control as a prominent manifestation of discretization error in existing multi-step generative rendering models and show that resolving this inconsistency substantially lowers denoising trajectory curvature, facilitating subsequent step distillation. To this end, we introduce Representation Transformation and Alignment (RETA), which ali...

### 11. Neural Video Compression Based on Deformable Temporal Alignment and Difference-aware Fusion

- 方向：视频处理
- 作者：Chuyue Shan, Songlin Sun, Wang Chenwei, Shen Zihan
- 日期：2026-09-03
- 分类：cs.CV, cs.AI
- 关键词：video compression
- arXiv：2609.03520v1

摘要：

In conditional coding-based neural video compression, the quality of temporal context directly affects compression per- formance. Existing methods mostly construct context from prop- agated reference features, but they are vulnerable to motion esti- mation and local alignment errors in regions with complex mo- tion, occlusion, and high-frequency textures, resulting in inaccu- rate temporal information. To address this issue, this paper pro- poses a method combining deformable temporal alignment and difference-aware...

### 12. SafeRestore: Detector-Relative Risk Certificates for Selective Industrial Image Restoration

- 方向：底层视觉
- 作者：Shaoliang Yang, Jun Wang
- 日期：2026-09-03
- 分类：cs.CV, stat.AP
- 关键词：image restoration
- arXiv：2609.03475v1

摘要：

Industrial inspection pipelines often restore a measured image before a detector acts on it, yet restoration can suppress detector-supported defect structure or create clean-region activations. We formulate restoration as a selective action problem over the measured display, five restored candidates, and review. SafeRestore ranks candidates with action-specific fitted scores, chooses a gate on threshold-tuning data, and evaluates the fixed gate on a disjoint certification sample with two one-sided exact binomial bo...

### 13. Learning to Attract and Repel: Dual Quality Margin Learning for Face Recognition (DQM-Face)

- 方向：底层视觉
- 作者：El Ouanas Belabbaci, Bhavesh Wani, Philipp Terhörst
- 日期：2026-09-02
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2609.02644v1

摘要：

Face recognition in unconstrained environments remains highly challenging due to diverse and extreme variations encountered in real-world scenarios. To mitigate these effects, existing margin-based approaches model sample quality through feature magnitude. However, magnitude-based modeling alone is susceptible to identity-agnostic noise, which can degrade the reliability and discriminative power of learned representations. In this paper, we propose Dual Quality Margin Learning for Face Recognition (DQM-Face), a nov...

### 14. Fine-Grained Anomaly Perception in Wild UGC-Enhanced Images: A Comprehensive Dataset and Difference-Fusion Framework

- 方向：底层视觉
- 作者：Yan Zhong, Gefei Chen, Qiufang Ma, Zhen Wang, Zhiwei Fan, Lei Shi, et al.
- 日期：2026-09-02
- 分类：cs.CV, cs.AI
- 关键词：image enhancement
- arXiv：2609.02529v1

摘要：

Image enhancement and restoration have become standard back-end operations on short-video and social media platforms to boost UGC visual experience. Yet these processes inevitably introduce visual anomalies--especially in faces, texts, and textures--that directly undermine perceptual fidelity and viewer trust. While existing IQA methods perform well on classic distortions, they target holistic quality assessment and fail to capture the specific, localized anomalies caused by enhancement algorithms in real-world UGC...

### 15. UnCapsTSR: An Unsupervised Transformer-based Image Super-Resolution Approach for Capsule Endoscopy Images

- 方向：底层视觉
- 作者：Anjali Sarvaiya, Shubh Kawa, Lalit Agrawal, Jagrit Joshi, Kishor Upla, Kiran Raja
- 日期：2026-09-02
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2609.02476v1

摘要：

Wireless Capsule Endoscopy (WCE) captures and streams video while passing through a patient's Gastrointestinal (GI) tract and is used to examine its irregularities. Although advantageous over conventional endoscopy, WCE suffers from limitations related to capsule size and wireless transmission, resulting in images with coarser resolution. This work presents UnCapsTSR, an unsupervised transformer-based Generative Adversarial Network (GAN) framework for improving the spatial resolution of Low-Resolution (LR) WCE imag...

### 16. ProSR: Semantic-Prototype-Guided Discrete Modeling for Physically Consistent SAR Super-Resolution

- 方向：底层视觉
- 作者：Byoungwoo Kim, Munchurl Kim
- 日期：2026-09-02
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2609.02377v1

摘要：

High-resolution Synthetic Aperture Radar (SAR) imagery is critical for precision analysis such as automatic target recognition, yet its acquisition is costly. Although generative image super-resolution (ISR) models offer a promising alternative, current smooth-approximation based diffusion frameworks often struggle to preserve the coherent scattering statistics, causing stochastic structural distortions that are less consistent with real SAR physics. To address this, we propose Semantic Prototype-Guided Super-Resol...

### 17. VoRTeC: Taming Foundation Flow for One-step Real time Video Compression

- 方向：视频处理
- 作者：Yichong Xia, Qinhong Wu, Bin Chen, Jinpeng Wang, Zeyuan Chen, Haoqian Wang
- 日期：2026-09-02
- 分类：cs.CV, cs.AI
- 关键词：video compression
- arXiv：2609.02291v2

摘要：

Ultra-low bitrate video compression still faces critical challenges: traditional neural video compression inevitably introduces blurring artifacts, while diffusion-based generative video compression suffers from excessive decoding latency and poor temporal consistency. To address these issues, we propose $\mathtt{VoRTeC}$, a Video Compression framework built upon a foundational flow model (Wan2.1). By compactly encoding latent video representations, predicting the positions of compressed representations along flow...

### 18. LaST-SR: Laplace-Inspired Steady-Transient Complex-Frequency Decomposition for Single Image Super-Resolution

- 方向：底层视觉
- 作者：Linhao Li, Zhaojie Pan, Langkun Chen
- 日期：2026-09-02
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2609.02063v1

摘要：

Single-image super-resolution (SISR) requires global context modeling for structurally consistent reconstruction. Fourier operators are increasingly adopted for global feature modeling. However, their periodic spectral bases constrain the representation of localized aperiodic variations, limiting the recovery of irregular structures and fine details. In dynamical systems, the Laplace neural operator extends Fourier modes to complex frequencies and decomposes the output signal into complementary steady-state and tra...

### 19. SelfLift: Accelerating Few-Step Diffusion via Self-Recovering Resolution Transition

- 方向：底层视觉
- 作者：Tingyan Wen, Chenqian Yan, Xurui Peng, Xiazhang Fang, Shuai Wang, Xueqian Wang, et al.
- 日期：2026-09-02
- 分类：cs.CV
- 关键词：denoising
- arXiv：2609.02036v1

摘要：

Few-step diffusion models substantially compress temporal computation, making the spatial cost of each model evaluation an increasingly dominant source of inference latency. Progressive-resolution inference reduces this cost by performing early denoising at low resolution and reserving high-resolution computation for refinement. However, existing methods typically lift intermediate latents directly and rely on subsequent steps to absorb the induced distribution mismatch. In the few-step regime, the limited recovery...

### 20. InstEditSeg: Instruction-Driven Image Editing for Polyp and Skin Lesion Segmentation

- 方向：底层视觉
- 作者：Ziquan Liu, Zhewei Zhu, Xuyang Shi
- 日期：2026-09-02
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2609.02004v1

摘要：

Accurate segmentation of polyps and skin lesions is pivotal for clinical diagnosis, yet existing methods struggle with low contrast, ambiguous boundaries, and cross-domain distribution discrepancies. Discriminative networks and most diffusion-based segmentation approaches predict standalone binary masks, leaving the visual priors of large-scale pretrained generative models largely unexploited. We propose InstEditSeg, a unified generative framework that reformulates medical segmentation as an instruction-driven imag...

### 21. Linear Fusion MultiDiffusion for Fast Training-Free Spherical Panorama Generation

- 方向：底层视觉
- 作者：Akio Hayakawa, Yusuke Mukuta, Tatsuya Harada
- 日期：2026-09-02
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2609.01997v1

摘要：

We propose LF-MultiDiffusion, a training-free panorama generation method that extends MultiDiffusion to support linear projections between target and reference image spaces. Our key idea is to reformulate latent aggregation as a regularized least-squares problem and solve it efficiently with a Krylov-based iterative solver inside the denoising loop. This formulation enables denser and more natural mappings than prior training-free methods, yielding more stable generation with far fewer perspective views. As a resul...

### 22. SliceBridge: context-consistent repair of corrupted slice intervals in T1-weighted MRI

- 方向：底层视觉
- 作者：Jiheng Li, Michael E. Kim, Trent Schwartz, Gaurav Rudravaram, Derek B. Archer, Timothy J. Hohman, et al.
- 日期：2026-09-01
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2609.01827v1

摘要：

Structural magnetic resonance imaging (MRI) images are sometimes corrupted over a contiguous set of slices, where acquisition, motion, hardware, or reconstruction effects leave a single slice or short interval inconsistent with its neighbors while the rest of the image remains usable. Such localized corruption can bias downstream morphometric analysis, yet discarding or reacquiring an otherwise usable image is costly. We formulate this as an image restoration problem: given the location of the affected interval, re...

### 23. Reliability Challenges in Diffusion Vision-Language Models

- 方向：底层视觉
- 作者：Md. Atabuzzaman, Chris Thomas
- 日期：2026-09-01
- 分类：cs.CV, cs.CL
- 关键词：denoising
- arXiv：2609.01318v1

摘要：

Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our key findings are: (1...

### 24. TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models

- 方向：底层视觉
- 作者：Chao Zhou, Yiling Chen, Qi Chu, Tao Gong, Nenghai Yu, Tianyi We
- 日期：2026-09-01
- 分类：cs.CV, cs.AI, cs.MM
- 关键词：denoising
- arXiv：2609.01277v1

摘要：

Although pretrained joint audio-visual diffusion models offer rich control over \emph{what} to generate, they provide no explicit control over \emph{when} an utterance should occur. To address this, we study \emph{inference-time speech scheduling}, a novel task that places coupled speech and visual articulation within user-specified begin--end intervals without finetuning the backbone model. We uncover two intrinsic properties of the denoising process that enable this task. First, a timing-sensitive text-to-audio c...

### 25. One Prompt Is Enough: Watermark Laundering Through Foundation Image Models

- 方向：底层视觉
- 作者：Jidong Yang, Qi Li, Wei Zong, Yang-Wai Chow, Willy Susilo, Huaike Yu, et al.
- 日期：2026-09-01
- 分类：cs.CV, cs.AI, cs.CR
- 关键词：denoising
- arXiv：2609.01249v1

摘要：

Invisible watermarks are typically evaluated against predefined perturbations such as compression, blur, noise, cropping, and denoising. Public foundation image models expose a distinct threat: an attacker can submit a watermarked image with a single reconstruction prompt and obtain a visually faithful output from which the invisible watermark can no longer be decoded reliably. We formalize this failure mode as watermark laundering and evaluate it using a joint payload-fidelity profile that combines bit error rate...

### 26. Physics-Driven Independent Pair Generation for Iterative Self-Supervised Low-Dose CT Denoising

- 方向：底层视觉
- 作者：Xianlei Han, Shaoyu Wang, Jiancheng Fang, Weiwen Wu, Qiegen Liu
- 日期：2026-09-01
- 分类：cs.CV
- 关键词：denoising
- arXiv：2609.02654v1

摘要：

Low-dose computed tomography (LDCT) measurements contain mixed Poisson-Gaussian noise. However, most self-supervised methods rely on generic image statistics and do not explicitly model this noise, which may limit their ability to effectively suppress realistic LDCT noise. To address this issue, we propose a physics-driven framework with cross-domain iteration for self-supervised LDCT denoising. The proposed framework proceeds in three main steps. First, a learned sinogram prior and the LDCT noise model guide poste...

### 27. ASSERT: Adaptive Stochastic Sampling for Robust Diffusion Models on Analog Compute-in-Memory Hardware

- 方向：底层视觉
- 作者：Yuannuo Feng, Yizhe Chen, Wenshuai Yao, Yuxin Xie, Ngai Wong, Wenyong Zhou, et al.
- 日期：2026-09-01
- 分类：cs.CV
- 关键词：denoising
- arXiv：2609.00955v1

摘要：

Diffusion models achieve strong image generation quality but incur high iterative denoising costs. Analog compute-in-memory (CIM) can accelerate matrix-vector multiplications, yet spatial memory variations perturb weights and accumulate during sampling. Unlike conventional neural networks, diffusion models' temporal sensitivity to hardware noise remains underexplored. We investigate diffusion inference using a noise model calibrated and validated against measurements collected from multiple physical CIM chips. Our...

### 28. Denoising Diffusion Generative Models Secretly Calculate Attentions

- 方向：底层视觉
- 作者：Farzan Haddadi, Leila Monfared, Ebrahim Rezaii, Mohammadreza Malek-Mohammadi, Pejman Zakalvand, Narges Mokhtari
- 日期：2026-09-01
- 分类：cs.AI, cs.CV, cs.LG, cs.NE
- 关键词：denoising
- arXiv：2609.00885v1

摘要：

Denoising diffusion models are the dominant architecture for image generation, whereas most natural language generation and modeling are primarily handled by well-known transformer architectures employing attention mechanism. Here, we show that diffusion models also inherently use an attention mechanism very similar to that of transformers. Therefore, attention emerges as a universal machine learning principle, based on a general training objective. We also show similarities in basic functional principle of auto-en...

### 29. ReBridge-Flow: Re-Coupling Posterior Bridges in Flow Matching for Image Restoration

- 方向：底层视觉
- 作者：Jiaqi Zhang, Yiqi Wang, Hongjie Wu, Bohan Guo, Xinan Wang, Zichen Luo, et al.
- 日期：2026-09-01
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2609.00811v1

摘要：

Flow Matching provides an efficient generative prior for image restoration by learning continuous transport between source and data distributions. However, existing methods typically incorporate measurement constraints through local corrections. Such corrections may disrupt the source-clean endpoint coupling implicitly encoded by the pretrained flow, making the corrected endpoint pair incompatible with the current state. To address this issue, we propose ReBridge-Flow, a posterior bridge re-coupling method. Specifi...

### 30. EarthLD: Towards Unified Open-World Landslide Understanding via Vision-Language Guided Diffusion Models

- 方向：底层视觉
- 作者：Yuanchao Su, Lianru Gao, Mengying Jiang, Jiangyi Chen, Jiaxin Cheng, Yicong Zhou
- 日期：2026-09-01
- 分类：cs.CV
- 关键词：denoising
- arXiv：2609.00712v1

摘要：

Landslides are widespread geological hazards, yet their automated detection and mapping in remote sensing imagery remain challenging because of their irregular morphology, ambiguous spectral signatures, and substantial domain shifts across imaging platforms. To overcome these challenges, we propose EarthLD, a vision-language-guided diffusion framework for open-world landslide understanding, enabling unified landslide recognition, mapping, and trigger interpretation. At its core, EarthLD formulates landslide underst...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-09-06-low-level-vision-video-papers.md`
