---
title: 2026-11-01｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-11-01｜底层视觉与视频论文速览

生成时间：2026-11-01

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉、视频处理｜Blind Video Denoising for Vocal Tract rtMRI using a Self-Supervised Ensemble｜2026-10-29
2. 底层视觉｜What Does LOL Measure? Hidden Label Shifts in Low-Light Enhancement Benchmarks｜2026-10-28
3. 底层视觉｜Image Modeling: From Handcrafted Priors to Foundation Image Models｜2026-10-27
4. 底层视觉｜HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model｜2026-10-29
5. 底层视觉｜SCOPE: Semantic COdec Pre-Editing for Object-Preserving Compression｜2026-10-29
6. 底层视觉｜MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport｜2026-10-29
7. 底层视觉｜FFAI: Flow Matching with Feedback Training and Adaptive Initialization for CT Reconstruction｜2026-10-29
8. 底层视觉｜Regional Anchor Routing for Multi-Object Motion Transfer｜2026-10-29
9. 底层视觉｜Calibrating Attention-Based Token Pruning for Efficient Multi-Image Synthesis in UMMs｜2026-10-29
10. 底层视觉｜Multi-level Constrained Learning for Underwater Image Enhancement｜2026-10-29
11. 底层视觉｜CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation｜2026-10-29
12. 视频处理｜AlbumVSR: Identity-Preserving Face Video Super-Resolution from a Personal Photo Album｜2026-10-28
13. 视频处理｜Residual Motion Splatting for Continuous Space-Time Video Super-Resolution｜2026-10-28
14. 底层视觉｜Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation｜2026-10-27
15. 底层视觉｜The Noise Plane: A Diffusion Bridge Across Exponent and Dispersion｜2026-10-27
16. 视频处理｜Taming Noise Initialization for Zero-shot Video Restoration with Image Diffusion Priors｜2026-10-27
17. 底层视觉｜VGIQA: Fine-Grained Image Quality Assessment with Visual Grounding Rewards｜2026-10-27
18. 底层视觉｜A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation｜2026-10-27
19. 底层视觉｜TriDifNet: A Unified Three-Task Diffusion Network for End-to-End RGB-T Perception｜2026-10-27
20. 视频处理｜Explicit Regional Representations For Video Quality Assessment｜2026-10-27
21. 底层视觉｜Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs｜2026-10-27
22. 底层视觉｜Spatial-Frequency Learning for Scanning Transmission Electron Microscopy Image Enhancement｜2026-10-27
23. 底层视觉｜OSWAM: An Effective World Action Model with One-Step Action Generation｜2026-10-26
24. 底层视觉｜HiFiPix: Bringing High-Fidelity Real-World Super-Resolution Back to Pixel Space｜2026-10-26
25. 底层视觉｜Shared-Factor-Conditioned Diffusion for Low-Rank Tensor Recovery｜2026-10-26
26. 底层视觉｜Low-rank MERA Decomposition of 3D OCT Image Volume for Compression, Denoising, Feature Extraction and Diagnosis of Retinal Diseases｜2026-10-26
27. 视频处理｜Learning Dual-Camera Smooth Zoom via Decoupled Geometric-Photometric Data Synthesis｜2026-10-26
28. 底层视觉｜PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry｜2026-10-26
29. 底层视觉｜ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing｜2026-10-26
30. 底层视觉｜EditDistill: Is It Possible to Guide Video Editing with Image Editing?｜2026-10-25

## 论文摘要

### 1. Blind Video Denoising for Vocal Tract rtMRI using a Self-Supervised Ensemble

- 方向：底层视觉、视频处理
- 作者：Julian Andres Hernandez-Potes, Tomás Arias-Vergara, Daiqi Liu, Andreas Maier, Paula Andrea Perez-Toro
- 日期：2026-10-29
- 分类：eess.IV, cs.CV
- 关键词：denoising、video denoising
- arXiv：2610.39972v1

摘要：

Real-time magnetic resonance imaging of the vocal tract makes speech articulation directly observable, but the trade-off between temporal resolution and signal quality introduces substantial noise and obscures fine articulatory detail. Since clean references cannot be acquired for a moving vocal tract, supervised denoising approaches are not applicable in this setting. We propose a self-supervised denoising framework that combines spatiotemporal super-resolution learning with pseudo-supervision derived from a varia...

### 2. What Does LOL Measure? Hidden Label Shifts in Low-Light Enhancement Benchmarks

- 方向：底层视觉
- 作者：Adityan Thirumani Srinivasan
- 日期：2026-10-28
- 分类：cs.CV, cs.LG, eess.IV
- 关键词：low-light enhancement、image enhancement
- arXiv：2610.38121v1

摘要：

LOL-v1 and LOLv2-Real are the standard benchmarks for supervised low-light image enhancement, and several leading methods ship hand-set test-time adjustments with their evaluation scripts. We audit both benchmarks with 18 public checkpoints of eight methods under one metric implementation that reproduces every published number to within 0.09 dB, and find that their test labels differ from their training labels. (i) The 15 LOL-v1 test labels are rendered differently: the same captures appear in LOLv2 with labels of...

### 3. Image Modeling: From Handcrafted Priors to Foundation Image Models

- 方向：底层视觉
- 作者：A. Murat Tekalp
- 日期：2026-10-27
- 分类：eess.IV, cs.CV
- 关键词：image restoration、denoising
- arXiv：2610.36646v1

摘要：

This paper unifies six decades of image modeling, evolving from handcrafted mathematical tractable priors to solve inverse problems in imaging to data-driven deep foundation image models for both image generation and solving inverse problems, under a common Bayesian framework that formulates image modeling as an implicit or explicit probabilistic characterization of a data manifold. Every image restoration or generative task fundamentally seeks to answer the same question: What makes an image look like a real image...

### 4. HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

- 方向：底层视觉
- 作者：Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang, Xinguang Xiang, et al.
- 日期：2026-10-29
- 分类：cs.CV, cs.RO
- 关键词：denoising
- arXiv：2610.40373v1

摘要：

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately, while directly incorporating predicted futures into action policies without sufficiently considering...

### 5. SCOPE: Semantic COdec Pre-Editing for Object-Preserving Compression

- 方向：底层视觉
- 作者：Silvia Dani, Leonardo Galteri, Marco Bertini
- 日期：2026-10-29
- 分类：cs.CV
- 关键词：image compression
- arXiv：2610.39778v1

摘要：

Image compression is increasingly used before machine vision systems, yet standard codecs are mainly optimized for human perception rather than downstream task accuracy. We propose SCOPE (Semantic COdec Pre-Editing), a conditional image pre-editor that modifies images before compression to improve the bitrate and detection accuracy trade-off. The model is conditioned on the codec family and compression severity, allowing a single trained network to adapt to multiple compression settings without retraining or loadin...

### 6. MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport

- 方向：底层视觉
- 作者：Hailong Yan, Yongrui Zhang, Xiangtao Zhang, Le Zhang
- 日期：2026-10-29
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.39530v1

摘要：

We propose MorphSIG, a training-free framework that reformulates subject-driven image generation (SIG) as pseudo-video feature transport. MorphSIG contains two core modules: Progressive Decoupled Anchoring, which uses frequency-domain decoupling and structural scrambling during early denoising to break structural locking and enable a gradual transition from free composition to identity alignment; and Pseudo-flow Guided Feature Transport, which constructs a latent-space pseudo-flow field to mimic Image-to-Video temp...

### 7. FFAI: Flow Matching with Feedback Training and Adaptive Initialization for CT Reconstruction

- 方向：底层视觉
- 作者：Jigang Duan, Heran Wang, Genwei Ma, Xing Zhao
- 日期：2026-10-29
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2610.39517v1

摘要：

Although low-dose, sparse-view, and limited-angle CT involve distinct degradation mechanisms, all three pose reconstruction challenges due to limited measurement information and can therefore be addressed within a unified framework. In iterative image restoration with flow matching, prediction errors may cause inference states to deviate from the prescribed training path, while a fixed initialization may be unsuitable for inputs with varying degradation severity. We propose a unified conditional flow matching metho...

### 8. Regional Anchor Routing for Multi-Object Motion Transfer

- 方向：底层视觉
- 作者：Yuze Li, Fuchen Long, Xinlong Sun, Cheng Yan, Xinyu Zhang, Xi Chen
- 日期：2026-10-29
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.39478v1

摘要：

Compositional motion transfer requires a model to extract motions from multiple reference videos, and apply each motion to a user-specified object in one target scene. Existing methods normally struggle to reliably assign different reference motions to the correct target objects, thus a motion intended for one object may affect another. Meanwhile, some motion-specific tuning approaches are still facing another issue: they must run a new optimization whenever the reference video changes, making repeated transfers in...

### 9. Calibrating Attention-Based Token Pruning for Efficient Multi-Image Synthesis in UMMs

- 方向：底层视觉
- 作者：Zimeng Wu, Qijian Tian, Penghui Du, Changqian Yu, Jiaxin Chen, Yunhong Wang
- 日期：2026-10-29
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.39467v1

摘要：

Unified Multimodal Models (UMMs) enable powerful multi-image synthesis but incur substantial computation from long visual contexts. While token pruning offers a direct route to accelerating inference, existing methods are primarily adapted from understanding tasks, suffering from insufficient reference image exploration, confused conditional guidance, and pooling-induced ambiguity that degrades generation quality. To address these issues, we propose CATP, the first training-free context-compression method tailored...

### 10. Multi-level Constrained Learning for Underwater Image Enhancement

- 方向：底层视觉
- 作者：Wangtao Bao, Liping Xie, Kanjian Zhang, Huimin Lu
- 日期：2026-10-29
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2610.39183v1

摘要：

Underwater image enhancement aims to correct color and recover detail degraded by wavelength-dependent attenuation, scattering, and noise. Paired-reference supervision constrains output similarity, but does not by itself specify the color mapping, the strength of local detail corrections, or consistency with the degraded observation. We propose MCL-UIE, a paired-supervised framework that addresses these requirements by constraining restoration operations and the training objective. Monotonic Chromatic Transform (MC...

### 11. CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation

- 方向：底层视觉
- 作者：Huangchao Song, Lingyun Yu, Cong Li, Peiqi Jiang, Mingqi Fang, Hongtao Xie
- 日期：2026-10-29
- 分类：cs.CV, cs.CR
- 关键词：denoising
- arXiv：2610.39160v1

摘要：

With the rapid advancement of text-to-image diffusion models, increasingly realistic AI-generated content has raised serious concerns about misuse and copyright infringement. Digital watermarking offers a promising solution by enabling user-level traceability, yet existing methods remain difficult to deploy at scale, hindered by costly model retraining or detection, poor effectiveness-fidelity trade-offs, and limited robustness to image transformations. To address these challenges, we propose CLaW (Codec-guided Lat...

### 12. AlbumVSR: Identity-Preserving Face Video Super-Resolution from a Personal Photo Album

- 方向：视频处理
- 作者：Nianyao Du, Xijun Wang, Stanley H. Chan
- 日期：2026-10-28
- 分类：cs.CV, eess.IV
- 关键词：video super-resolution
- arXiv：2610.39001v1

摘要：

Severe blur, downsampling, noise, and compression can erase the identity cues needed to faithfully restore a person's face. We therefore use photographs of the same person as an external source of identity. AlbumVSR conditions a frozen, one-step streaming diffusion transformer on a personal album. We use four MagFace/CLIP set tokens to encode the album, and 64 texture tokens which come from a fused UV atlas rendered at the current window's estimated face pose. These tokens are appended to the transformer's cached c...

### 13. Residual Motion Splatting for Continuous Space-Time Video Super-Resolution

- 方向：视频处理
- 作者：Vincent Herfeld, Eva Coupet{é}, Julien Mairal, Jean Ponce
- 日期：2026-10-28
- 分类：cs.CV
- 关键词：video super-resolution
- arXiv：2610.38499v1

摘要：

Continuous space-time video super-resolution produces a high-resolution, highframe-rate video from a low-resolution, low-frame-rate one at arbitrary spatial scales and temporal instants. Classical spatial multi-frame super-resolution has shown that detail beyond a single frame's sampling limit can be recovered by aligning complementary observations with sub-pixel precision and accumulating them on a finer grid. Existing learning-based methods largely depart from this principle: some align and fuse frames only at lo...

### 14. Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation

- 方向：底层视觉
- 作者：Kaihua Chen, Yiming Gong, Deva Ramanan, Tarasha Khurana
- 日期：2026-10-27
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.37983v1

摘要：

We address the task of long-video, camera-controlled generation from a single image. The dominant autoregressive paradigm suffers from two key limitations: (1) error accumulation over time, as distant frames are conditioned on previously generated outputs rather than ground truth, leading to drift; and (2) ambiguity in how to incorporate camera control. Standard solutions to both--such as self-forcing and conditioning on explicit 6-DOF poses--either incur significant computational overhead or produce drifting scene...

### 15. The Noise Plane: A Diffusion Bridge Across Exponent and Dispersion

- 方向：底层视觉
- 作者：Xuran Hu, Yuru Jia, Tengxi Wang, Miloš Daković, Ljubiša Stanković, Wufan Zhao
- 日期：2026-10-27
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.37576v1

摘要：

Diffusion-based denoising commonly uses Gaussian perturbations, whereas sensor noise follows diverse signal-dependent statistical laws. In this paper, we propose $p$-Bridge, a unified measurement-indexed diffusion framework for Tweedie noise. The noise exponent $p$ describes the variance--intensity relation, while accumulated measurement $ν$ controls the noise level. Together, they define a noise plane that includes Gaussian, Poisson, and Gamma models. The stochastic bridge connects measurement distributions throug...

### 16. Taming Noise Initialization for Zero-shot Video Restoration with Image Diffusion Priors

- 方向：视频处理
- 作者：Chong Wang, Zixuan Fu, Hao Cheng, Siyuan Yang, Alex C. Kot, Bihan Wen
- 日期：2026-10-27
- 分类：cs.CV
- 关键词：video restoration
- arXiv：2610.37290v1

摘要：

Recent advances in diffusion models have achieved remarkable success in restoring high-quality images in a zero-shot manner. Unfortunately, extending this success to video restoration is challenging due to the substantial computational resources required to pre-train video diffusion models. A rising trend seeks to address video restoration by utilizing a pre-trained image diffusion model, initiating restoration from either frame-wise independent or identical Gaussian noise. Yet, these approaches often fall short, a...

### 17. VGIQA: Fine-Grained Image Quality Assessment with Visual Grounding Rewards

- 方向：底层视觉
- 作者：Weichang Wang, Liyu Chen, Shuyue Guan, Jie Hu, Fei Gao, Wei Li, et al.
- 日期：2026-10-27
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2610.37186v1

摘要：

Image quality assessment (IQA) aims to evaluate the perceptual visual quality of images. Recently, the rapid development of Multi-modal Large Language Models (MLLMs) has significantly advanced the IQA field. By integrating chain-of-thought (CoT) reasoning and reinforcement learning (RL), these models can generate more accurate and interpretable results while relying on less training data. However, existing MLLM-based methods are predominantly constrained to holistic, image-level evaluations and lack the capability...

### 18. A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation

- 方向：底层视觉
- 作者：Wenwu Tang, Dong Wang, Yun Cheng, Olga Saukh
- 日期：2026-10-27
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2610.37110v1

摘要：

Distribution-matching distillation enables high-quality image generation in only a few denoising steps. However, distilled student models often map different initial noise samples to similar outputs under the same prompt. To locate where diversity is lost, we compare the teacher and student along the sampling trajectory. The largest measured reduction in the response to different initial noises occurs during the first, high-noise step. When we replace the first step with the teacher's corresponding trajectory and l...

### 19. TriDifNet: A Unified Three-Task Diffusion Network for End-to-End RGB-T Perception

- 方向：底层视觉
- 作者：Qianchao He, Jing Liu, Yunhao Li, Xiaoqing Tian
- 日期：2026-10-27
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.37097v1

摘要：

Infrared--visible (IR--VIS) multi-modal perception supports robust scene understanding under challenging illumination. Infrared and visible images are often misaligned due to platform motion, viewpoint changes, and modality-dependent distortions, causing registration errors to propagate into subsequent fusion and detection stages. We propose TriDifNet, a unified three-task diffusion network for end-to-end RGB-T perception. To the best of our knowledge, TriDifNet is the first diffusion-based network that jointly opt...

### 20. Explicit Regional Representations For Video Quality Assessment

- 方向：视频处理
- 作者：Fuyi Yang, Lei Yang, Andrew Liu, Chenyu Wei, Xiaoyi Guo, Ming Kai Hsu
- 日期：2026-10-27
- 分类：cs.CV
- 关键词：video quality assessment
- arXiv：2610.36978v1

摘要：

End-to-end video quality assessment (VQA) methods leave the regional evidence underlying their predictions largely implicit. We introduce an explicit pixel-level regional representation for VQA, instantiated as a Quality-Relevance Heatmap (QRH) that combines localized degradation evidence with perceptual priors under vision-language model guidance, without requiring pixel-level annotations. We apply QRH to existing VQA models through two deterministic fragment-sampling strategies: distribution-preserving sampling a...

### 21. Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs

- 方向：底层视觉
- 作者：Donghyeon Cho, Joowon Kim, Seungho Shin, Eunho Yang
- 日期：2026-10-27
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- arXiv：2610.36671v1

摘要：

Diffusion vision-language models (DVLMs) process their entire input at every denoising step. Since visual tokens make up 89-97% of this input on the benchmarks we study, most of the decoding computation is spent repeatedly processing the same image. Visual token pruning methods partially relieve this burden by removing part of the visual tokens, but they lose the removed information and still process the remaining image at every step. To measure how often the image is actually needed, we compare LLaDA-V's predictio...

### 22. Spatial-Frequency Learning for Scanning Transmission Electron Microscopy Image Enhancement

- 方向：底层视觉
- 作者：Hesong Li, Ying Fu, Ziqi Wu, Ruiwen Shao, Tao Zhang
- 日期：2026-10-27
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2610.36487v1

摘要：

Scanning Transmission Electron Microscopy (STEM) enables the observation of atomic arrangements at sub-angstrom resolution and plays a key role in the discovery and characterization of advanced materials. Raw STEM images are often noisy and blurred due to multiple degradations. Although recent deep learning methods improve STEM images, their performance remains limited under severe degradations. In this work, we propose a spatial-frequency learning framework for STEM image enhancement. Specifically, we design a spa...

### 23. OSWAM: An Effective World Action Model with One-Step Action Generation

- 方向：底层视觉
- 作者：Guowen Zhang, Liyi Chen, Xu Hu, Pengfei Wang, Jingfan Chen, Chenhang He, et al.
- 日期：2026-10-26
- 分类：cs.CV, cs.RO
- 关键词：denoising
- arXiv：2610.35850v1

摘要：

Direct-policy World Action Models (WAM) have demonstrated the benefits of decoupling action generation from explicit future visual prediction for efficient inference in autonomous driving and embodied control. However, they still require tens of denoising steps to achieve competitive action quality, incurring substantial latency and hindering real-time deployment. Simply reducing the number of denoising steps will collapse the nonlinear multi-step denoising trajectory into coarse updates, substantially degrading ac...

### 24. HiFiPix: Bringing High-Fidelity Real-World Super-Resolution Back to Pixel Space

- 方向：底层视觉
- 作者：Wenjie Li, Du Chen, Hui Wang, Linlong Fan, Youwei Lv, Zeyi Chen, et al.
- 日期：2026-10-26
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2610.35515v1

摘要：

Diffusion-based real-world image super-resolution suffers from limited reconstruction fidelity due to information loss in VAE-based latent representations. Recently, pixel-space diffusion models offer a promising high-faithfulness alternative by avoiding latent compression, but adapting them to Real-ISR remains challenging due to inherent patch boundary artifacts and degraded generative capability. To address the issues and maximize the potential of pretrained pixel-space diffusion models, we propose HiFiPix, a pix...

### 25. Shared-Factor-Conditioned Diffusion for Low-Rank Tensor Recovery

- 方向：底层视觉
- 作者：Zhengyun Cheng, Guanwen Zhang, Wei Zhou
- 日期：2026-10-26
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2610.35368v1

摘要：

Tensor recovery spans heterogeneous data structures and observation processes, calling for a representation that can adapt across modalities and tasks. We propose DiffTR, an unsupervised framework that unifies tensor completion, denoising, and hyperspectral super-resolution through coordinate-conditioned diffusion. Shared factors indexed by tensor coordinates condition a compact score network, and score matching jointly learns the factors and an implicit tensor representation from the available observations. Scalar...

### 26. Low-rank MERA Decomposition of 3D OCT Image Volume for Compression, Denoising, Feature Extraction and Diagnosis of Retinal Diseases

- 方向：底层视觉
- 作者：Ivica Kopriva, Fei Shi, Marija Štanfel, Qin Peng, Jianhao Bao, Gaowei Li, et al.
- 日期：2026-10-26
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.35271v1

摘要：

Optical coherence tomography (OCT) is a non-invasive imaging modality used for visualization of retinal tissue. However, OCT volumes are affected by speckle noise, which degrades image contrast and obscures fine structural details. Furthermore, modern clinical practice requires large field-of-view, high-resolution OCT volumes, whose storage and transmission are demanding for archiving and teleophthalmology applications. To address aforementioned challenges, we propose a low-rank multi-scale entanglement renormaliza...

### 27. Learning Dual-Camera Smooth Zoom via Decoupled Geometric-Photometric Data Synthesis

- 方向：视频处理
- 作者：Junjie Fan, Zhilu Zhang, Renlong Wu, Dazhi Zhang, Wangmeng Zuo
- 日期：2026-10-26
- 分类：cs.CV
- 关键词：frame interpolation
- arXiv：2610.34854v1

摘要：

When zooming between dual cameras on smartphones, prominent discontinuities in both geometric perspective and color rendition inevitably degrade the visual experience of users. To address this issue, we introduce the dual-camera smooth zoom (DCSZ) task, aiming to synthesize continuous intermediate frames for fluid zooming. However, directly applying existing video frame interpolation (VFI) models to this task is severely hindered by substantial domain gaps and the practical intractability of capturing real-world co...

### 28. PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry

- 方向：底层视觉
- 作者：Yihang Chen, Bin Tan, Yujun Shen, Yinghao Xu, Nan Xue
- 日期：2026-10-26
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.34845v1

摘要：

Recent multi-view Transformers (e.g., DUSt3R and VGGT) have advanced 3D reconstruction by scaling training data and model capacity from two views to many views and long sequences, subsuming the classical SfM/SLAM pipeline of feature extraction, matching, and pose estimation in a single feed-forward pass. Yet this subsumption hides the interfaces between pipeline stages---correspondences, geometry, and pose are entangled in a single forward pass, leaving supervised fine-tuning as the major path to improvement and of...

### 29. ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing

- 方向：底层视觉
- 作者：Caiyi Sun, Yujing Sun, Siu-Ming Yiu
- 日期：2026-10-26
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2610.34782v1

摘要：

Recent generic reference-based image generation models natively support multiple conditions by concatenating all reference image and text tokens into a joint sequence processed by a single Diffusion Transformer (DiT). However, this versatile paradigm comes at an efficiency cost: accommodating multiple references leads to a token explosion, incurring massive $\mathcal{O}(N^2)$ computational complexity. Most acceleration methods operate inside the DiT, showing limited capability in reducing spatial redundancy and fai...

### 30. EditDistill: Is It Possible to Guide Video Editing with Image Editing?

- 方向：底层视觉
- 作者：Guojun Lei, Hong Li, Hongbing Yang, Lixue Gong, Chi Wang, Zheng Dong
- 日期：2026-10-25
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.34303v1

摘要：

Recent advances in image editing have enabled fine-grained and highly controllable visual modifications. However, achieving similar levels of controllability in video editing remains an open challenge, particularly for precise local edits, dynamic temporal effects, and consistent lighting across frames.In this paper, we propose EditDistill, a framework that distills image-level visual transformations from edits to guide video editing.Specifically, given a source video and an edit prompt, we first generate an edited...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`latest.md`
