---
title: 2026-08-16｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-08-16｜底层视觉与视频论文速览

生成时间：2026-08-16

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Beyond Uniform Restoration: Empowering All-in-One Restoration with Pixel-Level Multimodal Guidance｜2026-08-10
2. 底层视觉｜Making Every Step Count: Spatio-Temporal Information Allocation for Imaging Inverse Problems｜2026-08-12
3. 底层视觉｜Hybrid-LUT: Channel-Aware Hybrid Lookup Table and Filtering for Efficient Image Denoising｜2026-08-12
4. 底层视觉、视频处理｜Generative Video Compression Based on Hierarchical Referencing｜2026-08-12
5. 底层视觉｜New Orthogonal Multiwavelet Filters Derived by Matrix Spectral Factorization｜2026-08-12
6. 底层视觉｜Towards Color-Faithful Low-Light Image Enhancement via Adaptive Color Debiasing and Saturation Rectification｜2026-08-11
7. 底层视觉｜NTIRE 2026 Low-light Enhancement: Twilight Cowboy Challenge｜2026-08-10
8. 底层视觉、视频处理｜World Tokens: Enhancing Embodied Policies with Training-Time World Modeling｜2026-08-10
9. 底层视觉｜DocPure: Prompt-Free Unified Document Restoration via Degradation-Aware Structure-Guided Wavelet Modulation｜2026-08-10
10. 底层视觉｜Bright-Channel Retinex Enhancement with a Conditional Overdispered-Noise Analysis｜2026-08-10
11. 底层视觉｜SCULPT: Subtractive Composition for 3D Part Generation｜2026-08-13
12. 视频处理｜SNM-VFI: Symmetric Nonlinear Motion-Guided Generative Video Frame Interpolation｜2026-08-13
13. 底层视觉｜Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation｜2026-08-13
14. 底层视觉｜GeoCache: Training-Free Acceleration of Multi-View Texture Diffusion via Geometric Delta Transport｜2026-08-13
15. 底层视觉｜Fidelity-Constrained Anchoring for Black-Box Denoisers｜2026-08-13
16. 底层视觉｜SketchSense: Learning to Interpret Imperfect Sketch Guidance for Image Inpainting｜2026-08-13
17. 底层视觉｜From Local Mismatch to Global Impact: Optimizing Cache Reuse Policy for Efficient Diffusion｜2026-08-13
18. 底层视觉｜HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation｜2026-08-13
19. 底层视觉｜BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving｜2026-08-13
20. 底层视觉｜XYZFlow:Scaling Multi dimensional Shortcut Flows for Efficient Generative Modeling｜2026-08-12
21. 底层视觉｜HAMP-LIC: Hessian-Aware Mixed-Precision Post-Training Quantization for Learned Image Compression｜2026-08-12
22. 底层视觉｜LoSA: Near-Lossless Sparse Attention for Training-Free Video Diffusion Acceleration｜2026-08-12
23. 底层视觉｜UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos｜2026-08-12
24. 底层视觉｜From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-Based Video Dereflection｜2026-08-12
25. 底层视觉｜VLMs Win a Systematic Evaluation of Underwater Image Reconstruction｜2026-08-11
26. 底层视觉｜Every Packet Counts: Dispersing Information for Loss-Resilient Learned Image Compression｜2026-08-11
27. 底层视觉｜HNDiff: Haze-Noise Diffusion for Image Dehazing｜2026-08-11
28. 底层视觉｜PEAK: Precise and Persistent Concept Erasure via k-Sparse Autoencoders｜2026-08-11
29. 底层视觉｜Multiple Scale Latents for Learned Image Compression｜2026-08-11
30. 底层视觉｜Mixture-of-Experts-based Entropy Model for Learned Image Compression｜2026-08-11

## 论文摘要

### 1. Beyond Uniform Restoration: Empowering All-in-One Restoration with Pixel-Level Multimodal Guidance

- 方向：底层视觉
- 作者：Chunxiao Liu, Wei Liu, Anbin Xiong, Erli Meng
- 日期：2026-08-10
- 分类：cs.CV, cs.AI
- 关键词：image restoration、denoising、deblurring、low-light enhancement、low-level vision
- arXiv：2608.09482v1

摘要：

All-in-one image restoration is a unified low-level vision task that aims to effectively recover high-quality images from inputs degraded by various types and levels of corruption using a single model. Recent works have achieved remarkable progress by learning degradation-adaptive prompts or network architectures. However, these methods typically apply a uniform restoration strategy across the entire image, neglecting the fact that different regions may suffer from distinct degradation types and varying degrees of...

### 2. Making Every Step Count: Spatio-Temporal Information Allocation for Imaging Inverse Problems

- 方向：底层视觉
- 作者：Yi Cao, Xiangyong Cao, Pei Liu, Yong-Jin Liu, Deyu Meng
- 日期：2026-08-12
- 分类：cs.CV
- 关键词：deblurring、motion deblur
- arXiv：2608.11747v1

摘要：

Flow-based generative models have emerged as powerful image priors for training-free inverse problem solving, capturing coherent semantics and fine-grained structure. Despite these strengths, existing flow-based inverse solvers primarily focus on the design of individual updates, largely overlooking spatio-temporal information allocation under a fixed number of function evaluations (NFEs). Temporally, insufficient early exploration can trap the flow trajectory in an incorrect semantic basin, whereas excessive alloc...

### 3. Hybrid-LUT: Channel-Aware Hybrid Lookup Table and Filtering for Efficient Image Denoising

- 方向：底层视觉
- 作者：Zhilin Ai, Boyu Li, Sidi Yang, Wenqing Shi, Wenyong Zhou, Binxiao Huang, et al.
- 日期：2026-08-12
- 分类：cs.CV, eess.IV
- 关键词：image denoising、denoising
- arXiv：2608.11646v1

摘要：

Lookup table (LUT)-based image denoising methods have attracted increasing attention due to their high efficiency and hardware-friendly properties. However, existing RGB-LUT approaches require three identical LUTs to process RGB channels in parallel, resulting in large on-chip SRAM consumption. A simple alternative is to apply LUT processing only to the luminance (Y) channel in the YUV color space to reduce memory usage. However, this naive strategy leads to degraded restoration quality, since ignoring the chromina...

### 4. Generative Video Compression Based on Hierarchical Referencing

- 方向：底层视觉、视频处理
- 作者：Daowen Li, Ding Ding, Zifu Zhang, Kai Li, Ying Chen
- 日期：2026-08-12
- 分类：cs.CV
- 关键词：denoising、video compression
- arXiv：2608.11618v1

摘要：

Diffusion-based generative video compression has emerged as a promising paradigm to improve perceptual quality, where latent frames are required to be encoded efficiently while serving as denoising conditions. However, existing methods neither carefully design reference and quality structures during latent coding nor account for the impact of frame-level quality variation on denoising procedure, which limits coding efficiency and aggravates artifact propagation during generative reconstruction. In this paper, we pr...

### 5. New Orthogonal Multiwavelet Filters Derived by Matrix Spectral Factorization

- 方向：底层视觉
- 作者：Vasil Kolev, Todor Cooklev, Fritz Keinert
- 日期：2026-08-12
- 分类：cs.CV, cs.DB, math.NA, stat.AP
- 关键词：denoising、image compression
- arXiv：2608.11518v1

摘要：

The paper considers the construction of two new orthogonal multiwavelets with supercompact support by using the Fast Bauer's method for matrix spectral factorization on the matrix product filter of the orthogonal CL multiwavelet filter. The new multiwavelets possess orthogonality, symmetry/antisymmetry, and one of them provides better coding and smoothness than other supercompact multiwavelets. The performance of the new multiwavelet filters in subband-based edge detection, grayscale and color image compression and...

### 6. Towards Color-Faithful Low-Light Image Enhancement via Adaptive Color Debiasing and Saturation Rectification

- 方向：底层视觉
- 作者：Zhichen Yang, Rui Xu, Yuzhen Niu, Fusheng Li, Hui Da, Ri Cheng
- 日期：2026-08-11
- 分类：cs.CV
- 关键词：low-light enhancement、image enhancement
- arXiv：2608.10512v1

摘要：

Low-light imaging often introduces color bias caused by the low signal-to-noise ratio and the image formation process. Although recent low-light image enhancement methods have achieved strong brightness recovery, faithful color restoration remains challenging, manifesting as overall color bias together with local under- and over-saturation. To address this issue, we propose CAGE, a cylindrical color correction framework with adaptive color debiasing and gamut-harmonized saturation rectification for color-faithful l...

### 7. NTIRE 2026 Low-light Enhancement: Twilight Cowboy Challenge

- 方向：底层视觉
- 作者：Aleksei Khalin, Egor Ershov, Artyom Panshin, Sergey Korchagin, Georgiy Lobarev, Arseniy Terekhin, et al.
- 日期：2026-08-10
- 分类：cs.CV
- 关键词：low-light enhancement、image enhancement
- arXiv：2608.09782v1

摘要：

This paper presents a review of the NTIRE 2026 Low-light Enhancement: Twilight Cowboy Challenge. The objective of the competition was to merge a set of misaligned smartphone images in the raw domain, captured in low-light conditions, into a single, clean image. Introduced setup simultaneously addresses two problems of low-light photography: visual degradations such as high noise and mixed scene illuminants, and the geometric inconsistencies caused by hand movement during multi-frame capture. To advance research in...

### 8. World Tokens: Enhancing Embodied Policies with Training-Time World Modeling

- 方向：底层视觉、视频处理
- 作者：Qu Tang, Benhui Zhuang, Bo Yuan, Xue Yu, Longteng Guo, Junlan Feng
- 日期：2026-08-10
- 分类：cs.CV, cs.RO
- 关键词：denoising、video denoising
- arXiv：2608.09730v1

摘要：

Vision-language-action (VLA) models are a widely adopted paradigm for embodied policies. They excel at efficient closed-loop control but do not explicitly model how physical scenes evolve as a task unfolds. Recently emerging world-action models (WAMs) leverage pretrained video world models to capture spatiotemporal evolution, yet retaining future generation or a large video backbone in the control loop substantially increases inference cost. We introduce World Tokens, an embodied policy architecture built around a...

### 9. DocPure: Prompt-Free Unified Document Restoration via Degradation-Aware Structure-Guided Wavelet Modulation

- 方向：底层视觉
- 作者：Lingming Su, Wanglong Lu, Tao Wang, Kaihao Zhang, Nan Zhang, Liyan An, et al.
- 日期：2026-08-10
- 分类：cs.CV
- 关键词：denoising、deblurring
- arXiv：2608.09536v1

摘要：

High-quality document images are pivotal for information archiving and downstream automatic processing. However, they are frequently compromised by diverse degradations during uncontrolled acquisition and transmission. While unified document restoration techniques have been proposed to restore images from multiple degradations, they often struggle with training multiple degradation-specific models, reliance on manual task-specific prompts, or cross-task data pairing. To address these limitations, we propose DocPure...

### 10. Bright-Channel Retinex Enhancement with a Conditional Overdispered-Noise Analysis

- 方向：底层视觉
- 作者：Jongpil Jeong
- 日期：2026-08-10
- 分类：cs.CV, eess.IV
- 关键词：denoising、low-light enhancement
- arXiv：2608.09137v1

摘要：

I present a training-free low-light enhancement method that combines local bright-channel illumination estimation, Retinex division, and edge-preserving denoising. For a fixed illumination estimate, a conditional Negative -Binominal psueduo-count method characterises the heteroscedastic noise amplified by division. The unconstrained reflectance ratio is the pixelwise maximum-likelihood estimate, with a boundary solution for zero-valued observations; the implemented estimate additionally applies illumination filteri...

### 11. SCULPT: Subtractive Composition for 3D Part Generation

- 方向：底层视觉
- 作者：Sikuang Li, Chen Yang, Jiemin Fang, Jiazhong Cen, Yuhe Wei, Jichen Pang, et al.
- 日期：2026-08-13
- 分类：cs.CV, cs.GR
- 关键词：denoising
- arXiv：2608.13541v1

摘要：

Part-aware 3D generation aims to create digital assets that are coherent as complete objects while exposing structural parts for editing, material assignment, animation, and reuse. Existing methods impose this structure outside the native generation loop: segmentation-based methods partition an already generated shape, while additive methods synthesize parts from predefined layouts, boxes, or tokens and then reconcile them into a whole. The former preserves the generated geometry but fixes the object before part bo...

### 12. SNM-VFI: Symmetric Nonlinear Motion-Guided Generative Video Frame Interpolation

- 方向：视频处理
- 作者：Jisoo Jeong, Hong Cai, Jamie Menjay Lin, Hanno Ackermann, Hyeonjun Sim, Yinhao Zhu, et al.
- 日期：2026-08-13
- 分类：cs.CV
- 关键词：frame interpolation
- arXiv：2608.13460v1

摘要：

We propose Symmetric Nonlinear Motion-guided Generative Video Frame Interpolation (SNM-VFI), a training-free framework for motion-controllable generative video frame interpolation with pre-trained optical flow and video diffusion models. Unlike conventional diffusion-based VFI methods that synthesize intermediate frames from random noise, SNM-VFI guides the generative process with correspondence-aware frames produced by a symmetric nonlinear motion model. Specifically, we first utilize a pre-trained optical flow mo...

### 13. Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation

- 方向：底层视觉
- 作者：Hmrishav Bandyopadhyay, Xuanchi Ren, Zijian Huang, Jay Zhangjie Wu, Tianshi Cao, Ruilong Li, et al.
- 日期：2026-08-13
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.13391v1

摘要：

Interactive autoregressive video generation demands both low-latency rollouts and precise online control. Few-step distillation accelerates generation by reducing denoising steps, while online control imposes a causal constraint: frames and blocks should depend on history and controls available during generation. Existing video distribution matching distillation (DMD) pipelines, however, often supervise causal few-step students using bidirectional teachers that score complete clips. The score for a target can there...

### 14. GeoCache: Training-Free Acceleration of Multi-View Texture Diffusion via Geometric Delta Transport

- 方向：底层视觉
- 作者：Haotang Li, Zhenyu Qi, Shaohan Henry Wang, Kebin Peng, Yutong Zhao, Zi Wang, et al.
- 日期：2026-08-13
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2608.13255v1

摘要：

Geometry-conditioned multi-view diffusion enables high-quality 3D texture generation, but its repeated per-view denoiser evaluations introduce substantial computational cost. Existing training-free accelerators primarily exploit temporal redundancy by reusing computation across denoising steps. In multi-view texturing, however, skipping a step also removes the cross-view interaction that continually aligns different observations of the same surface, leading to rapidly degraded consistency and fidelity. Our analysis...

### 15. Fidelity-Constrained Anchoring for Black-Box Denoisers

- 方向：底层视觉
- 作者：Masaki Satoh
- 日期：2026-08-13
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.13194v1

摘要：

We propose a fidelity-constrained framework that anchors the output of a black-box denoiser to its input without retraining and with little additional computation. The method linearly blends the denoised image with the input and selects the maximum blending factor that satisfies a prescribed local fidelity constraint using Peak Signal-to-Noise Ratio (PSNR) or Structural Similarity Index (SSIM). For PSNR control, a closed-form solution is obtained under a local constant-blending assumption. For SSIM control, we deri...

### 16. SketchSense: Learning to Interpret Imperfect Sketch Guidance for Image Inpainting

- 方向：底层视觉
- 作者：Zian Yang
- 日期：2026-08-13
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.13186v1

摘要：

Sketch-guided image inpainting provides intuitive structural control, yet real sketches often mix reliable global intent with locally crowded, displaced, incomplete, or deliberately unconventional strokes. Existing approaches typically either retain the input sketch as a fixed condition throughout denoising or refine it into a clean structure before RGB synthesis. The former assumes uniformly reliable strokes and can propagate local errors throughout generation; the latter must resolve ambiguous structure before em...

### 17. From Local Mismatch to Global Impact: Optimizing Cache Reuse Policy for Efficient Diffusion

- 方向：底层视觉
- 作者：Xichen Ye, Yifan Wu, Zhikang Xie, Xiangyu Yue, Cheng Jin, Weizhong Zhang
- 日期：2026-08-13
- 分类：cs.AI, cs.CV, cs.LG
- 关键词：denoising
- arXiv：2608.13043v1

摘要：

Diffusion models have achieved dominant performance in visual generation but suffer from substantial inference overhead. While cache-based acceleration has emerged as a promising solution, existing policies rely on local similarity heuristics, which we identify as being significantly misaligned with final generation quality. This discrepancy stems from the non-uniform propagation and accumulation of errors along the denoising trajectory. To address this, we propose Global-Impact Cache (GCache). We first establish a...

### 18. HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation

- 方向：底层视觉
- 作者：Yunhao Bai, Zhongwei Qiu, Guangyu Guo, Yiming Huang, Tony C. W. Mok, Qinji Yu, et al.
- 日期：2026-08-13
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.12904v1

摘要：

Clinical intelligence requires estimating a patient's underlying condition from incomplete observations rather than learning isolated mappings from scans to answers. Volumetric medical images provide dense observations of anatomy, attenuation, and lesions, whereas clinical language provides sparse but complementary semantic observations. We formulate CT-centered intelligence as inference over a shared latent patient state, under which readout, reconstruction, and simulation all become state-dependent prediction pro...

### 19. BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving

- 方向：底层视觉
- 作者：Bing Zhan, Shuyao Shang, Jiahao Gu, Shuo Lu, Yuan Xu, Zhao Wang, et al.
- 日期：2026-08-13
- 分类：cs.RO, cs.AI, cs.CV
- 关键词：denoising
- arXiv：2608.12854v1

摘要：

Autonomous driving requires planning under both semantic constraints and predictive dynamics. Existing end-to-end driving approaches, however, typically emphasize only one side of this requirement: Vision-Language-Action (VLA) models exploit VLM priors for semantic reasoning, while World Action Models (WAMs) provide future-aware prediction through generative world modeling. This naturally motivates a unified planner that can leverage both semantic priors and predictive dynamics. However, we find that a naive combin...

### 20. XYZFlow:Scaling Multi dimensional Shortcut Flows for Efficient Generative Modeling

- 方向：底层视觉
- 作者：Jinxiu Liu, Xuanming Liu, Kangfu Mei, Yandong Wen, Weiyang Liu
- 日期：2026-08-12
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.12276v2

摘要：

High-fidelity image generation faces a trade-off between speed and quality. Diffusion models produce strong visuals but require costly iterative sampling. Existing efficient methods mainly distill pretrained models into few-step samplers, a challenging process that depends heavily on teacher-model quality. In this paper, we introduce XYZFlow, a framework that rethinks efficient generation through multidimensional scaling of flow matching. Unlike single-step mappings, XYZFlow enhances expressivity by making probabil...

### 21. HAMP-LIC: Hessian-Aware Mixed-Precision Post-Training Quantization for Learned Image Compression

- 方向：底层视觉
- 作者：Yuefeng Zhang
- 日期：2026-08-12
- 分类：cs.CV, cs.AI, cs.MM
- 关键词：image compression
- arXiv：2608.12239v1

摘要：

Use this plain-text version for the arXiv abstract field: Learned image compression (LIC) models achieve strong rate-distortion performance but are hindered by high computational complexity and encoding-decoding mismatches across heterogeneous hardware platforms. Uniform fixed-precision quantization alleviates these issues but suffers severe quality degradation at low bit widths because it ignores differences in the quantization sensitivities of individual layers. To enable efficient and accurate low-bit deployment...

### 22. LoSA: Near-Lossless Sparse Attention for Training-Free Video Diffusion Acceleration

- 方向：底层视觉
- 作者：Enhuai Liu, Yunke Wang, Yutong Wang, Changming Sun, Chang Xu
- 日期：2026-08-12
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2608.12032v1

摘要：

Video diffusion transformers are costly to sample: every denoising step applies self-attention over a long 3D token sequence, a quadratic cost that dominates as resolution and duration grow. Sparse attention reduces this cost without retraining, but existing methods pursue aggressive sparsity, where further speedup costs disproportionately more attention fidelity. We target the opposite end of this trade-off: fix near-lossless fidelity by construction, and remove as much computation as this constraint permits. Two...

### 23. UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos

- 方向：底层视觉
- 作者：Yuxuan Zhang, Haozhong Xiong, Jiayi Song, Jinpeng Yu, Yang Shi, Jiaming Liu, et al.
- 日期：2026-08-12
- 分类：cs.CV, cs.SD
- 关键词：denoising
- arXiv：2608.11752v2

摘要：

Talking-video character replacement requires coordinated transfer of appearance and voice while preserving the source motion, scene, linguistic content, and audio-video timing. Existing methods use separately optimized models for the two modalities, making audio-visual consistency difficult to enforce. We present UniSwap, the first framework for streaming joint audio-visual identity replacement in talking videos. Given a source video, a reference image, and a reference voice clip, UniSwap transfers the reference ap...

### 24. From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-Based Video Dereflection

- 方向：底层视觉
- 作者：Zepeng Wang, Jiagao Hu, Fuhao Li, Yuxuan Chen, Fei Wang, Daiguo Zhou
- 日期：2026-08-12
- 分类：cs.CV, cs.AI, eess.IV
- 关键词：denoising
- arXiv：2608.11562v1

摘要：

Videos captured through glass often contain reflections that degrade visual quality and interfere with downstream vision tasks. Although single-image reflection removal has been extensively studied, video reflection removal remains largely underexplored due to the lack of paired video data, temporally coherent removal models, and dedicated evaluation benchmarks. We present a closed-loop framework that unifies physics-grounded reflection simulation, diffusion-based video dereflection, and benchmark evaluation. Our S...

### 25. VLMs Win a Systematic Evaluation of Underwater Image Reconstruction

- 方向：底层视觉
- 作者：Sara Aghajanzadeh, Yingxue Wang, Ieva Bagdonaviciute, David Forsyth
- 日期：2026-08-11
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2608.11425v1

摘要：

Underwater image restoration consists of recovering an image which looks like there is no water present. To date, evaluation has not been systematic. This paper describes a systematic evaluation pipeline for underwater reconstruction, which can be used to assess a method for accuracy; consistency of reconstruction over camera moves; and the effect of water parameters. We use this pipeline to evaluate a range of current procedures, from models constructed using explicit but approximate physical models of scattering...

### 26. Every Packet Counts: Dispersing Information for Loss-Resilient Learned Image Compression

- 方向：底层视觉
- 作者：Yuhang Wei, Chuqin Zhou, Yibo Shi, Jing Wang, Guo Lu
- 日期：2026-08-11
- 分类：cs.CV
- 关键词：image compression
- arXiv：2608.11096v1

摘要：

Learned image compression (LIC) has achieved impressive rate-distortion performance. However, existing methods remain highly vulnerable to packet loss, a common challenge in satellite and emergency communications. This vulnerability stems from non-uniform information distribution at the packetization stage and sequential decoding dependencies at the entropy coding stage. We propose an end-to-end loss-resilient image compression scheme that addresses both. Before packetization, we introduce an Inter-Channel Redistri...

### 27. HNDiff: Haze-Noise Diffusion for Image Dehazing

- 方向：底层视觉
- 作者：Jin-Ting He, Fu-Jen Tsai, Yan-Tsung Peng, Min-Hung Chen, Chia-Wen Lin, Yen-Yu Lin
- 日期：2026-08-11
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.10995v1

摘要：

Existing diffusion-based methods have recently made significant progress in image dehazing. However, they typically neglect the physics of haze formation and reconstruct clean images from pure Gaussian noise, thereby limiting their restoration potential. To address this issue, we propose Haze-Noise Diffusion (HNDiff), a novel diffusion framework that embeds the atmospheric scattering model as an inductive bias. By grounding diffusion in physical principles, HNDiff ensures that the restoration aligns more closely wi...

### 28. PEAK: Precise and Persistent Concept Erasure via k-Sparse Autoencoders

- 方向：底层视觉
- 作者：Man Jiang, Ouxiang Li, Weibao Xue, Zhenhua Tang, Yuan Wang, Shuo Wang, et al.
- 日期：2026-08-11
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.10985v1

摘要：

Erasing concepts from large-scale text-to-image (T2I) diffusion models has become increasingly crucial due to the growing concerns over copyright infringement, privacy violations, and offensive content. Existing approaches struggle to achieve both precise and persistent concept erasure: inaccurate localization of concept-related representations may cause unintended semantic interference, while incomplete removal of the underlying concept knowledge allows adversarial recovery. To address this dilemma, we propose PEA...

### 29. Multiple Scale Latents for Learned Image Compression

- 方向：底层视觉
- 作者：Jonas Brenig, Radu Timofte
- 日期：2026-08-11
- 分类：cs.CV
- 关键词：image compression
- arXiv：2608.10952v1

摘要：

Most learned image compression systems rely on a single latent representation combined with a hyperprior, which limits their ability to efficiently capture image structure across spatial scales. In this work, we propose a hierarchical latent representation to improve the efficiency of the entropy model. By using multiple latents at different scales, each with its own entropy model, we better capture the spatial structure of the latent representation. Our experiments show that this approach achieves a 17.9% BD-rate...

### 30. Mixture-of-Experts-based Entropy Model for Learned Image Compression

- 方向：底层视觉
- 作者：Jonas Brenig, Radu Timofte
- 日期：2026-08-11
- 分类：cs.CV
- 关键词：image compression
- arXiv：2608.10947v1

摘要：

Learned image compression has seen significant progress in recent years with the development of end-to-end learned models that achieve better compression efficiency than state-of-the-art conventional methods. Recently, Mixture of Experts (MoE) approaches have seen promising results in NLP and computer vision tasks. In this paper, we introduce the MoE approach to learned image compression. We propose a MoE-based Entropy model (MoEE) for learned image compression, allowing the model to selectively activate only the s...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-08-16-low-level-vision-video-papers.md`
