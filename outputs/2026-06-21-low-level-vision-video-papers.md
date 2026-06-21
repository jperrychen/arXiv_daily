---
title: 2026-06-21｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-06-21｜底层视觉与视频论文速览

生成时间：2026-06-21

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜The Third Challenge on Image Denoising at NTIRE 2026: Methods and Results｜2026-06-14
2. 底层视觉｜AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement｜2026-06-16
3. 底层视觉｜teasr: training-efficient any-step diffusion transformer for real-world image super-resolution｜2026-06-15
4. 底层视觉｜JanusMesh: Fast and Zero-Shot 3D Visual Illusion Generation via Cross-Space Denoising｜2026-06-18
5. 底层视觉｜On the Redundancy of Timestep Embeddings in Diffusion Models｜2026-06-18
6. 底层视觉｜Through the PRISM: Preference Representation in Intermediate States of Video Diffusion Models｜2026-06-18
7. 底层视觉｜EFIQA: Explainable Fundus Image Quality Assessment via Anatomical Priors｜2026-06-18
8. 底层视觉｜DiffMath: Symbol- and Graph-Aware Latent Diffusion Transformer for Handwritten Mathematical Expression Generation｜2026-06-18
9. 视频处理｜Gaussian Process Prior Variational Autoencoder for Endoscopic Videos｜2026-06-18
10. 底层视觉｜Linear Recurrent Unit with Semantic Modulation for Image Super-Resolution｜2026-06-18
11. 底层视觉｜Flow Map Denoisers: Traversing the Distortion-Perception Plane for Inverse Problems｜2026-06-18
12. 底层视觉｜One-Shot Novel View and Pose Human Image Synthesis via 3D Prior Guided Diffusion Model｜2026-06-18
13. 底层视觉｜Learning When to Denoise: Optimizing Asynchronous Schedules for Latent Diffusion｜2026-06-18
14. 底层视觉｜ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?｜2026-06-17
15. 底层视觉｜Cinematic Compositing Using Character-Environment-Harmonized Video Generation Models｜2026-06-17
16. 底层视觉｜DVANet: Degradation-aware Visual-prior Alignment Network for Image Restoration｜2026-06-17
17. 底层视觉｜BindEdit: Taming Attention Leakage for Precise Multi-Object Image Editing｜2026-06-17
18. 底层视觉｜Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow｜2026-06-17
19. 底层视觉｜Bridging Single Distortion Artifacts and Mmultifactorial Clinical Quality: Few-shot Biparametric MRI Quality Assessment via Distortion-trained Prototypical Networks｜2026-06-17
20. 底层视觉｜Learning to Distort: Weakly-Supervised Image Quality Transfer for Prostate DWI Correction｜2026-06-17
21. 底层视觉｜Spiking Pyramid Wavelet Transformation for High-efficient and Low-energy Image Restoration｜2026-06-17
22. 底层视觉｜Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement｜2026-06-16
23. 底层视觉｜BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics｜2026-06-16
24. 底层视觉｜Do We Really Need Diffusion? A Fast U-Net for Paired Medical Image Translation｜2026-06-16
25. 底层视觉｜Test-Time Training for Robust Text-Guided Open-Vocabulary Object Counting｜2026-06-16
26. 底层视觉｜Universal Image Restoration via Internalized Chain-of-Thought Reasoning｜2026-06-16
27. 底层视觉｜UoU: A Universal Fingerprint Foundation Model Based on Large-Scale Unsupervised Learning｜2026-06-16
28. 底层视觉｜Exact Posterior Score Estimation for Solving Linear Inverse Problems｜2026-06-15
29. 底层视觉｜Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment｜2026-06-15
30. 底层视觉｜WaveDINO: Learning-Based Atmospheric Correction of Unwrapped InSAR Interferograms Validated by GNSS: Results at Laguna del Maule and Campi Flegrei Volcanoes｜2026-06-15

## 论文摘要

### 1. The Third Challenge on Image Denoising at NTIRE 2026: Methods and Results

- 方向：底层视觉
- 作者：Lei Sun, Hang Guo, Bin Ren, Shaolin Su, Xian Wang, Danda Pani Paudel, et al.
- 日期：2026-06-14
- 分类：cs.CV
- 关键词：image restoration、image denoising、denoising
- arXiv：2606.16031v1

摘要：

This paper reports on the NTIRE 2026 Challenge on Image Denoising, specifically focusing on the high-noise regime ($σ= 50$). The competition investigates advanced neural architectures designed to restore high-fidelity details from images corrupted by additive white Gaussian noise (AWGN). Unlike constrained benchmarks, this track emphasizes peak quantitative performance, measured by Peak Signal-to-Noise Ratio (PSNR), without limitations on parameter count or computational overhead. By synthesizing contributions from...

### 2. AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement

- 方向：底层视觉
- 作者：Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, et al.
- 日期：2026-06-16
- 分类：cs.CV
- 关键词：low-light enhancement、image enhancement
- arXiv：2606.17998v1

摘要：

Existing low-light image enhancement methods often face a bottleneck between the representation capacity of illumination-field modeling and computational complexity. To address this issue, this paper proposes an Adaptive Illumination Gaussian Splatting Network (AIGS-Net), an ultra-lightweight architecture for fast low-light enhancement. Unlike conventional static priors, AIGS-Net constructs an input-adaptive 2D Gaussian Splatting illumination field. The opacity of Gaussian basis functions is dynamically modulated b...

### 3. teasr: training-efficient any-step diffusion transformer for real-world image super-resolution

- 方向：底层视觉
- 作者：Xiang Gao, Chenxin Zhu, Yushun Fang, Qiang Hu, Xiaoyun Zhang
- 日期：2026-06-15
- 分类：cs.CV
- 关键词：image super-resolution、denoising
- arXiv：2606.16188v1

摘要：

Diffusion models excel in Real-World Image Super-Resolution (Real-ISR) due to their powerful generative priors but suffer from slow iterative sampling. Although existing one-step distillation methods accelerate inference, they typically require auxiliary teacher models that inflate training memory and restrict scalability to large-scale architectures. Furthermore, these fixed-step models lack the flexibility to trade off speed for quality. In this paper, we propose TEASR, a training-efficient any-step diffusion fra...

### 4. JanusMesh: Fast and Zero-Shot 3D Visual Illusion Generation via Cross-Space Denoising

- 方向：底层视觉
- 作者：Siang-Ling Zhang, Huai-Hsun Cheng, Tsung-Ju Yang, Yu-Lun Liu
- 日期：2026-06-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.20563v1

摘要：

Creating 3D visual illusions, a single 3D mesh that reveals entirely different semantics from various viewing angles, is a fascinating but tough challenge. Existing optimization-based methods are slow and can produce oversaturated colors. In contrast, naive stitching approaches fail to produce geometrically coherent objects. This results in visible unnatural seams and semantic leaks. In this paper, we present a fast and training-free framework for generating text-driven 3D visual illusions. Our approach decouples t...

### 5. On the Redundancy of Timestep Embeddings in Diffusion Models

- 方向：底层视觉
- 作者：José A. Chávez
- 日期：2026-06-18
- 分类：cs.LG, cs.CV
- 关键词：denoising
- arXiv：2606.20416v1

摘要：

Diffusion models rely heavily on explicit timestep embeddings to modulate the denoising process across various noise scales. In this work, we challenge the necessity of these temporal signals by analyzing their impact on U-Net and Diffusion Transformer architectures. Beyond empirical evidence, we provide a theoretical framework demonstrating that, under certain conditions, the global minimizer of the diffusion training objective can be achieved without explicit timestep conditioning. Our findings reveal a surprisin...

### 6. Through the PRISM: Preference Representation in Intermediate States of Video Diffusion Models

- 方向：底层视觉
- 作者：Haoxuan Wu, Lai Man Po, Mengyang Liu, Kun Li, Hongzheng Yang, Wei Liu
- 日期：2026-06-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.20310v1

摘要：

Evaluating video generation with clean, pixel-based reward models disconnects evaluation from the noisy diffusion process and incurs massive VAE decoding costs. In this paper, we challenge this paradigm by asking a fundamental question: Can a powerful video generator inherently discriminate preferences directly from noisy latents? To answer this, we introduce \textbf{PRISM} (\textbf{P}reference \textbf{R}epresentation in \textbf{I}ntermediate \textbf{S}tates of Diffusion \textbf{M}odels). PRISM employs a lightweigh...

### 7. EFIQA: Explainable Fundus Image Quality Assessment via Anatomical Priors

- 方向：底层视觉
- 作者：Pengwei Wang, José Morano, Qian Wan, Hrvoje Bogunović
- 日期：2026-06-18
- 分类：cs.CV, cs.LG
- 关键词：image quality assessment
- arXiv：2606.20108v1

摘要：

Image quality control is vital for a wide range of downstream applications. Deep learning-based image quality assessment methods typically train classifiers on dataset-specific quality labels, inheriting two limitations: (1) generalization is tied to the labeling criteria of the training set and (2) these methods cannot provide spatial feedback on where the quality is degraded, lacking explainability. In this work, we propose EFIQA, a framework that requires no quality-related supervision and produces spatial quali...

### 8. DiffMath: Symbol- and Graph-Aware Latent Diffusion Transformer for Handwritten Mathematical Expression Generation

- 方向：底层视觉
- 作者：Wei Pan, Xuhan Zheng, Yilin Shi, Huiguo He, Hiuyi Cheng, Dezhi Peng, et al.
- 日期：2026-06-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.19939v1

摘要：

Handwritten Mathematical Expression Generation (HMEG) is challenging due to the complex two-dimensional layouts and long-range structural dependencies of mathematical expressions. Existing methods typically rely on explicit spatial supervision, such as symbol-level bounding boxes, which incurs high annotation costs and limits scalability. In this work, we propose DiffMath, a symbol- and graph-aware latent diffusion framework that leverages the hierarchical structure inherent in LaTeX as a structural prior, eliminat...

### 9. Gaussian Process Prior Variational Autoencoder for Endoscopic Videos

- 方向：视频处理
- 作者：Ivan De Boi, Xinxing Shi, Xiaoyu Jiang, Tim J. M. Jaspers, Francisco Caetano, Mauricio A. Alvarez, et al.
- 日期：2026-06-18
- 分类：cs.CV
- 关键词：video restoration
- arXiv：2606.19908v1

摘要：

Endoscopic video analysis is essential for gastrointestinal diagnosis and computer-assisted interventions, but video sequences are routinely degraded by specular reflections, motion artifacts, and missing frames. These transient corruptions can distract clinicians, reduce image interpretability, and disrupt downstream tasks such as 3D reconstruction and navigation. Effective restoration therefore requires methods that exploit temporal continuity rather than treating frames in isolation. We introduce a Gaussian Proc...

### 10. Linear Recurrent Unit with Semantic Modulation for Image Super-Resolution

- 方向：底层视觉
- 作者：Mingyu Choi, Woo Kyoung Han, Sunghoon Im, Kyong Hwan Jin
- 日期：2026-06-18
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2606.19901v1

摘要：

Linear recurrent unit (LRU), designed with a principled formulation for stable linear recurrence, has demonstrated promising accuracy and robustness on long-range dependency tasks. However, its static parameterization and single-scan method limits its applicability to 2D vision tasks. In this study, we propose a LRU-based restoration network with a semantic modulating unit (SMU) to achieve a harmonious balance between performance and efficiency in single-image super-resolution. The SMU plays three key roles: LRU mo...

### 11. Flow Map Denoisers: Traversing the Distortion-Perception Plane for Inverse Problems

- 方向：底层视觉
- 作者：Nicolas Zilberstein, Morteza Mardani, Santiago Segarra
- 日期：2026-06-18
- 分类：cs.LG, cs.CV
- 关键词：image restoration
- arXiv：2606.19802v1

摘要：

Image restoration faces a fundamental tradeoff: methods that minimize error produce blurry reconstructions, while those that maximize perceptual quality yield sharp but less faithful images. Existing approaches either commit to a single operating point on this distortion perception (DP) frontier or require paired-data supervision, auxiliary models, or hyperparameter tuning of the sampler to access different points. We show that flow map models, a recent extension of flow matching for few-step sampling that learns a...

### 12. One-Shot Novel View and Pose Human Image Synthesis via 3D Prior Guided Diffusion Model

- 方向：底层视觉
- 作者：Shenjian Gong, Kangkan Wang, Shanshan Zhang, Jian Yang
- 日期：2026-06-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.19718v1

摘要：

This paper addresses the challenge of one-shot novel view and pose human image synthesis. The existing methods transfer the reference human image to a target pose using a set of 2D pose keypoints or synthesize human images based on generalizable human NeRF which uses human model priors to extract point-wise features. However, pose transfer based methods can not handle complex human pose using ambiguous 2D pose as the condition, while generalizable human NeRFs may be inaccurate to recover occluded/invisiable human p...

### 13. Learning When to Denoise: Optimizing Asynchronous Schedules for Latent Diffusion

- 方向：底层视觉
- 作者：Bingshuo Qian, Xiang Cheng
- 日期：2026-06-18
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.19662v1

摘要：

Multi-representation diffusion models can improve visual synthesis by denoising complementary views of an image, but their performance depends critically on the asynchronous schedule that determines when each representation is denoised. We propose to learn this schedule. Our method formulates asynchronous flow matching over multiple representation spaces and uses a schedule-corrected objective that keeps each representation's local noising-time weights fixed as the schedule changes. We instantiate the schedule with...

### 14. ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?

- 方向：底层视觉
- 作者：Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin, Jingbo Zhang, et al.
- 日期：2026-06-17
- 分类：cs.CV, cs.RO
- 关键词：denoising
- arXiv：2606.19531v1

摘要：

World Action Models (WAMs) commonly rely on video generation to bridge visual world modeling and robot control. However, video-based WAMs face three coupled limitations: dense multi-frame future tokens make inference costly, full video prediction spends capacity on action-irrelevant temporal and appearance details, and long-horizon future imagination may introduce errors that mislead action prediction. These issues raise a simple question: Does world action model really need video generation? We propose ImageWAM, a...

### 15. Cinematic Compositing Using Character-Environment-Harmonized Video Generation Models

- 方向：底层视觉
- 作者：Tianyi Xiang, Mingming He, Li Ma, Jing Liao
- 日期：2026-06-17
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.20233v1

摘要：

Cinematic compositing aims to integrate green-screen characters into novel environments while maintaining physical and photometric realism. Previous methods often fail to capture the complex bidirectional interactions between characters and their surroundings, which we characterize as Character-to-Environment (C2E) physical interaction and Environment-to-Character (E2C) lighting harmonization. To address this, we propose an end-to-end video diffusion framework that jointly models C2E and E2C interactions, specifica...

### 16. DVANet: Degradation-aware Visual-prior Alignment Network for Image Restoration

- 方向：底层视觉
- 作者：Yanjie Tu, Qingsen Yan, Axi Niu, Tao Hu, Haokui Zhang, Jiantao Zhou
- 日期：2026-06-17
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.19097v1

摘要：

All-in-One image restoration aims to develop a unified restoration framework for handling diverse degradation types. Existing end-to-end methods usually regard the restoration process as a black-box mapping, lacking an explicit optimization interpretation. Although deep unfolding provides an interpretable iterative modeling paradigm for image restoration, existing methods mostly rely on fixed degradation assumptions or predefined degradation information, making them difficult to adapt to unified restoration require...

### 17. BindEdit: Taming Attention Leakage for Precise Multi-Object Image Editing

- 方向：底层视觉
- 作者：Chaewon Park, Soyoon Lee, Naeun Lee, Minjung Shin, Seogkyu Jeon, Kibeom Hong
- 日期：2026-06-17
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.18906v1

摘要：

Real image editing enables precise manipulation of visual content, yet existing methods often fail in complex multi-object scenarios, causing semantic blending, object duplication, or incomplete edits. We attribute these failures to attention leakage, where signals across spatial regions and text tokens become entangled during the denoising process. Specifically, we identify two distinct forms of leakage: Edit-Token Leakage, where ambiguous token-region alignment leads to object blending, and Source Dominance Leaka...

### 18. Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow

- 方向：底层视觉
- 作者：Veit Hucke, Thomas Pinetz, Gregor Reiter, Ursula Schmidt-Erfurth, Hrvoje Bogunović
- 日期：2026-06-17
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2606.18876v1

摘要：

Optical coherence tomography (OCT) is essential in ophthalmology, but inconsistent image quality especially in low-cost devices hinders automated analysis. To address this, we introduce a flow-matching-based test-time adaptation method that generates high-quality surrogate images from noisy inputs. Typically, domain gaps between test and training data cause pixel distribution mismatches during the denoising process. We overcome this by matching the test image's histogram to synthetic reference trajectories, success...

### 19. Bridging Single Distortion Artifacts and Mmultifactorial Clinical Quality: Few-shot Biparametric MRI Quality Assessment via Distortion-trained Prototypical Networks

- 方向：底层视觉
- 作者：Yuheng Tang, Alexander Ng, Wen Yan, Natasha Thorley, Pawel Rajwa, Yipei Wang, et al.
- 日期：2026-06-17
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2606.18872v1

摘要：

Clinical prostate multi-parametric MRI relies heavily on high-quality diffusion-weighted imaging (DWI), yet reading DWI is frequently compromised by geometric distortion, often caused by rectal air. Assessing quality via the PI-QUAL scoring system is an emerging clinical standard, but it is subjective, time-consuming and suffers from a class imbalance where low-quality cases are diverse and relatively scarce. Using the PRIME clinical trial as an example, there are $6%$ images with PI-QUAL scores lower than 4, $87%$...

### 20. Learning to Distort: Weakly-Supervised Image Quality Transfer for Prostate DWI Correction

- 方向：底层视觉
- 作者：YuCheng Tang, Wen Yan, Alexander Ng, Natasha Thorley, Pawel Rajwa, Yipei Wang, et al.
- 日期：2026-06-17
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2606.18869v1

摘要：

Single-shot echo-planar prostate diffusion-weighted imaging (DWI) is frequently complicated by geometric distortions, which impact the ability to derive reliable diagnoses from such images. Developing automated correction methods is challenged by the absence of paired distorted and undistorted clinical scans. In this paper, we first propose a novel weakly-supervised image quality transfer (IQT) framework from undistorted to distorted images that utilizes image quality assessment (IQA) signals to supervise the trans...

### 21. Spiking Pyramid Wavelet Transformation for High-efficient and Low-energy Image Restoration

- 方向：底层视觉
- 作者：Chen Zhao, Xiantao Hu, Song Wu, Qian Wang, Chen Wu, Rui Xie, et al.
- 日期：2026-06-17
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.18644v1

摘要：

Spiking neural networks (SNNs) have garnered significant interest in computer vision due to their potential for efficiency and biological inspiration. While spiking CNN-based methods have shown promise for image restoration (IR) tasks, their performance is constrained by the inherent receptive field limitations of CNN operations. In the paper, we explore the benefits of discrete wavelet transformation and propose a spiking pyramid wavelet-based model (SPWM) for high-efficient and low-energy target. Specifically, we...

### 22. Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement

- 方向：底层视觉
- 作者：Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, et al.
- 日期：2026-06-16
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2606.17985v1

摘要：

Existing unsupervised low-light image enhancement methods often encounter local exposure imbalance and color distortion under complex non-uniform illumination. In addition, most Vision Transformers lack an explicit mechanism for modeling the physical priors of illumination degradation. To address these limitations, we propose GLFS, a Gaussian light field splatting-based Vision Transformer that integrates continuous physical illumination modeling from Gaussian splatting into the Transformer architecture. In GLFS, sc...

### 23. BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics

- 方向：底层视觉
- 作者：Junfeng Xia, Wenhao Ye, Junxiang Zhang, Xuanye Pan, Mo Wang, Quanying Liu
- 日期：2026-06-16
- 分类：cs.CV, q-bio.NC
- 关键词：denoising
- arXiv：2606.17742v1

摘要：

Whole-brain 4D fMRI generation is valuable for modeling functional brain dynamics, yet existing fMRI foundation models mainly target representation learning and downstream prediction rather than conditional predictive generation. We introduce BrainWorld, a structural-prior-conditioned generative model for whole-brain 4D fMRI dynamics. BrainWorld uses sMRI as subject-level anatomical context to guide future fMRI generation, integrating structural information into the denoising process rather than treating it as a pa...

### 24. Do We Really Need Diffusion? A Fast U-Net for Paired Medical Image Translation

- 方向：底层视觉
- 作者：Alicia Pirwass, Birte Glimm, Michael Munz, Hans-Joachim Wilke
- 日期：2026-06-16
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.17675v1

摘要：

Magnetic resonance imaging-signal fat fraction (MRI-SFF) quantifies tissue fat and serves as an established biomarker for metabolic and musculoskeletal disorders. The acquisition requires, however, specialized MRI sequences, which are not available routinely. We investigate whether SFF can be estimated from widely available T2-weighted (T2w) MRI via image-to-image translation (I2I). We further compare a lightweight 4-level U-Net to a state-of-the-art Denoising Diffusion Probabilistic Model (DDPM) using a dataset of...

### 25. Test-Time Training for Robust Text-Guided Open-Vocabulary Object Counting

- 方向：底层视觉
- 作者：Hao-Yuan Ma, Yuda Zou, Li Zhang, Yongchao Xu
- 日期：2026-06-16
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.17601v1

摘要：

Text-guided Open-vocabulary Object Counting (TOOC) enables counting arbitrary object categories specified by text prompts, offering substantially greater flexibility than conventional closed-set counting. However, existing TOOC methods are developed and evaluated primarily on ideal images, while real-world scenes often suffer from adverse conditions such as rain, fog, darkness, and sensor noise, which severely degrade visual quality and impair vision-language alignment. To bridge this gap, we introduce Robust-TOOC,...

### 26. Universal Image Restoration via Internalized Chain-of-Thought Reasoning

- 方向：底层视觉
- 作者：Yu Guo, Zhengru Fang, Shengfeng He, Senkang Hu, Yihang Tao, Phone Lin, et al.
- 日期：2026-06-16
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.17557v1

摘要：

Image restoration seeks to recover high-quality images from degraded inputs but becomes highly ill-posed under complex, mixed degradations. While unified all-in-one models are common, their performance declines as degradation complexity increases. Recent works adopt Chain-of-Thought (CoT) reasoning for multi-round restoration using specialized modules. However, this approach faces two key limitations: (i) increased computational cost due to multi-step processing, and (ii) weak modeling of interactions between degra...

### 27. UoU: A Universal Fingerprint Foundation Model Based on Large-Scale Unsupervised Learning

- 方向：底层视觉
- 作者：Xiongjun Guan, Jianjiang Feng, Jie Zhou
- 日期：2026-06-16
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.17436v1

摘要：

Fingerprint recognition is still dominated by task-specific pipelines, where enhancement, structural parsing, alignment, and matching are optimized in isolation. Although effective in narrow settings, this design limits representation reuse across sensors, qualities, and downstream applications. We therefore present UoU, short for ``a \textbf{U}niversal fingerprint foundation model based \textbf{o}n large-scale \textbf{U}nsupervised learning,'' which reframes fingerprint feature extraction as a domain-specific foun...

### 28. Exact Posterior Score Estimation for Solving Linear Inverse Problems

- 方向：底层视觉
- 作者：Abbas Mammadov, Ozgur Kara, Kaan Oktay, Iskander Azangulov, Adil Kaan Akan, Hyungjin Chung, et al.
- 日期：2026-06-15
- 分类：cs.LG, cs.CV, stat.ML
- 关键词：denoising
- arXiv：2606.17048v1

摘要：

Diffusion and flow-based models learn powerful data priors by training a denoiser to reverse Gaussian corruption. To use this prior to solve a linear inverse problem, one needs to sample from the posterior, but the score that the prior provides is the unconditional score, not the posterior score. Existing methods either steer a fixed pretrained denoiser with approximate measurement-matching corrections, or train a conditional restoration model that abandons the denoising structure of the prior. We derive the exact...

### 29. Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment

- 方向：底层视觉
- 作者：Zijie Meng
- 日期：2026-06-15
- 分类：cs.CV, cs.AI
- 关键词：image quality assessment
- arXiv：2606.16799v1

摘要：

Existing vision-language model (VLM)-based AI-generated image quality assessment (AIGIQA) methods suffer from a fundamental semantic-distortion dimensional conflict: monolithic representations optimized for semantic discrimination inherently entangle compositional understanding with low-level perceptual sensitivity, rendering them blind to fine-grained quality degradations. We introduce MST-CLIPIQA, a multi-scale two-stream framework that achieves hierarchical vision-language alignment through explicit representati...

### 30. WaveDINO: Learning-Based Atmospheric Correction of Unwrapped InSAR Interferograms Validated by GNSS: Results at Laguna del Maule and Campi Flegrei Volcanoes

- 方向：底层视觉
- 作者：Robert Popescu, Juliet Biggs, Tianyuan Zhu, Nantheera Anantrasirichai
- 日期：2026-06-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.16795v1

摘要：

Interferometric Synthetic Aperture Radar (InSAR) enables effective monitoring of volcanic deformation; however, the observed signals are often corrupted by atmospheric phase delays, seasonal surface changes, and decorrelation effects. Existing atmospheric correction methods, such as numerical weather model-based methods, can reduce these effects but do not consistently remove atmospheric artefacts and may introduce residual biases. To address these limitations, we propose a novel learning-based method for denoising...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-06-21-low-level-vision-video-papers.md`
