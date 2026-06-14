---
title: 2026-06-14｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-06-14｜底层视觉与视频论文速览

生成时间：2026-06-14

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Dual-Constrained Diffusion Image Compression for Operational Rate-Distortion-Perception Optimization｜2026-06-11
2. 底层视觉、视频处理｜Next Forcing: Causal World Modeling with Multi-Chunk Prediction｜2026-06-09
3. 底层视觉｜UniPET: a universal network for high-quality PET image denoising across varied dose reduction factors｜2026-06-09
4. 底层视觉｜U-TTT: Towards Generalizable PET Image Denoising via Test-Time Training｜2026-06-09
5. 顶会论文｜The 1st PortraitCraft Challenge: A CVPR 2026 Workshop Competition on Portrait Composition Understanding and Generation｜2026-06-09
6. 底层视觉、视频处理｜LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution｜2026-06-08
7. 顶会论文｜Claude Code-Driving Scenario Mining for the Argoverse 2 Challenge｜2026-06-08
8. 底层视觉｜World Tracing: Generative Pixel-Aligned Geometry Beyond the Visible｜2026-06-11
9. 视频处理｜EvTexture++: Event-Driven Texture Enhancement for Video Super-Resolution｜2026-06-11
10. 底层视觉｜Budget-Constrained Step-Level Diffusion Caching｜2026-06-11
11. 底层视觉｜SmartFont: Dynamic Condition Allocation for Few-Shot Font Generation｜2026-06-11
12. 底层视觉｜DuET: Dual Expert Trajectories for Diffusion Image Editing｜2026-06-11
13. 底层视觉｜High-Fidelity Two-Step Image Generation via Teacher-Aligned End-to-End Distillation｜2026-06-10
14. 顶会论文｜Metadata-Aware Multi-Prompt Reasoning for Zero-Shot Accident Understanding｜2026-06-10
15. 底层视觉｜Image Quality Assessment of Identity Cards Using Measures from Open Face Image Quality｜2026-06-10
16. 底层视觉｜Scene-Adaptive Nonlinear Tone Curves for Pseudo Ground-Truth Generation in Low-Light 3D Gaussian Splatting｜2026-06-10
17. 底层视觉｜RankVR: Low-Rank Structure Perception and Value Recalibration for Robust Composed Image Retrieval｜2026-06-10
18. 底层视觉｜Adv-TGD: Adversarial Text-Guided Diffusion for Face Recognition Impersonation Attacks｜2026-06-10
19. 视频处理｜AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference｜2026-06-09
20. 底层视觉｜Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization｜2026-06-09
21. 底层视觉｜Envision4D: Envisioning Visual Futures via Feed-forward 4D Gaussian Splatting for Autonomous Driving｜2026-06-09
22. 底层视觉｜Few-step Generative Models as Lossy Compression｜2026-06-09
23. 底层视觉｜PF-Trans: Physics-Embedded Frequency-Aware Transformer for Spectral Reconstruction｜2026-06-09
24. 底层视觉｜ClinReadNet: A clinical reading-inspired network for low-dose abdominal CT image quality assessment｜2026-06-09
25. 底层视觉｜Overlapped Wavelet Diffusion for Low-Light Image Enhancement｜2026-06-09
26. 底层视觉｜FoA-SR: Faithful or Aesthetic? Profile-Aware Preference Optimization for Real-World Image Super-Resolution｜2026-06-09
27. 底层视觉｜An Improved Generative Adversarial Network for Micro-Resistivity Imaging Logging Restoration｜2026-06-08
28. 底层视觉｜MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models｜2026-06-08
29. 底层视觉｜PTL-Diffusion: Manifold-Aware Diffusion with Periodic Terminal Laws｜2026-06-08
30. 底层视觉｜TUDSR: Twice Upsampling-Diffusion for Higher Super-Resolution｜2026-06-08

## 论文摘要

### 1. Dual-Constrained Diffusion Image Compression for Operational Rate-Distortion-Perception Optimization

- 方向：底层视觉
- 作者：Sanxin Jiang, Jiro Katto, Heming Sun
- 日期：2026-06-11
- 分类：cs.CV, cs.MM
- 关键词：denoising、image compression
- arXiv：2606.13366v1

摘要：

The rate-distortion-perception (RDP) trade-off extends classical rate--distortion theory by imposing a distributional constraint on reconstructions, providing a unified framework for neural image compression that jointly governs fidelity and perceptual realism. While prior work achieves near-optimal rate--perception trade-offs, practical frameworks explicitly realizing the full RDP surface remain scarce, primarily due to the difficulty of introducing common randomness at the decoder. We propose DCIC (Dual-Constrain...

### 2. Next Forcing: Causal World Modeling with Multi-Chunk Prediction

- 方向：底层视觉、视频处理
- 作者：Gangwei Xu, Qihang Zhang, Jiaming Zhou, Xing Zhu, Yujun Shen, Xin Yang, et al.
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：denoising、video denoising
- arXiv：2606.11187v1

摘要：

Autoregressive video generation has emerged as a powerful paradigm for World Action Models (WAMs). However, existing approaches suffer from slow training convergence and limited converged accuracy, particularly at high frame rates, as the training supervision is confined to the current chunk without explicit signals about future dynamics; they also suffer from slow inference due to iterative video denoising. In this paper, we present Next Forcing, a multi-chunk prediction (MCP) framework for causal world modeling t...

### 3. UniPET: a universal network for high-quality PET image denoising across varied dose reduction factors

- 方向：底层视觉
- 作者：Zhiwen Yang, Yang Zhou, Haowei Chen, Hui Zhang, Dan Zhao, Bingzheng Wei, et al.
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2606.11131v1

摘要：

Most existing deep learning-based PET image denoising methods assume a fixed and known dose reduction factor (DRF) for low-dose PET images. However, these methods encounter significant performance degradation when the DRF varies beyond the assumed one in practical applications. To address the challenge posed by varied DRFs, several preliminary studies focus on the task of universal PET image denoising, aiming to train a universal model over low-dose data across DRFs. Nonetheless, these vanilla universal models ofte...

### 4. U-TTT: Towards Generalizable PET Image Denoising via Test-Time Training

- 方向：底层视觉
- 作者：Zhiwen Yang, Jiayin Li, Hao Lu, Hui Zhang, Zihua Wang, Bingzheng Wei, et al.
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2606.11032v1

摘要：

Existing deep learning models for Positron Emission Tomography (PET) image denoising often suffer from severe performance degradation under distribution shifts, fundamentally restricting their robust clinical deployment. This lack of generalization stems from the conventional paradigm of fixed-parameter models that cannot adapt to variations in test data (e.g., dose levels or scanner types) after training. To overcome this limitation and achieve robust generalization, we introduce U-TTT, a novel U-shaped model that...

### 5. The 1st PortraitCraft Challenge: A CVPR 2026 Workshop Competition on Portrait Composition Understanding and Generation

- 方向：顶会论文
- 作者：Zijie Lou, Youyun Tang, Xiaochao Qu, Haoxiang Li, Ting Liu, Luoqi Liu, et al.
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- arXiv：2606.10894v1

摘要：

This paper presents an overview of the inaugural PortraitCraft Challenge, held as one of the official competitions at CVPR 2026. The challenge focuses on portrait composition understanding and generation, aiming to advance AI research in portrait aesthetics analysis and controllable image synthesis. Unlike existing datasets and tasks that primarily focus on global aesthetic scoring, PortraitCraft introduces a unified evaluation framework comprising two complementary tracks. Track 1 requires models to perform struct...

### 6. LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution

- 方向：底层视觉、视频处理
- 作者：Yu Cao, Ziquan Liu, Zhensong Zhang, Jiankang Deng, Shaogang Gong, Jifei Song
- 日期：2026-06-08
- 分类：cs.CV
- 关键词：denoising、video super-resolution
- arXiv：2606.09250v1

摘要：

Adapting large-scale pre-trained video generators for Video Super-Resolution (VSR) in novel domains remains computationally prohibitive. Methods that reformulate generation as direct Low-Quality to High-Quality mappings deviate from the original generative formulation, demanding extensive fine-tuning. ControlNet-style adapters lose their efficiency under modern Diffusion Transformers since the absence of encoder-decoder hierarchy forces duplication of the entire backbone. We observe that flow matching offers a prin...

### 7. Claude Code-Driving Scenario Mining for the Argoverse 2 Challenge

- 方向：顶会论文
- 作者：Wei Deng, Caoshengzhe Xue, Shuaikun Liu, Zhaohong Liu, Mengshi Qi, Huadong Ma
- 日期：2026-06-08
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- arXiv：2606.09180v1

摘要：

We present our submission to the CVPR 2026 Argoverse 2 Scenario Mining Challenge. Our system uses a four-stage pipeline: (1) autonomous code generation via a Claude Code agent powered by GLM~5.1, (2) iterative training set screening with Timestamp Balanced Accuracy threshold 0.8 to curate few-shot examples, (3) semantic code review by a separate Claude Code session, and (4) Qwen3-VL scene-level verification to filter false positives. We report results on the Argoverse 2 test set.

### 8. World Tracing: Generative Pixel-Aligned Geometry Beyond the Visible

- 方向：底层视觉
- 作者：Hao Zhang, Mohamed El Banani, Jen-Hao Cheng, Paul Zhang, Yi Hua, Ben Mildenhall, et al.
- 日期：2026-06-11
- 分类：cs.CV, cs.GR
- 关键词：denoising
- arXiv：2606.13652v1

摘要：

Image-to-3D methods often trade off faithfulness and completeness: depth estimators are anchored to input pixels but stop at the visible surface, while image-to-3D models generate complete shapes that are often misaligned with the input. We introduce World Tracing, a generative pixel-aligned geometry representation that predicts 3D points aligned with observed pixels while completing geometry beyond the visible surface. For each input pixel, World Tracing predicts an ordered stack of camera-space 3D points, where t...

### 9. EvTexture++: Event-Driven Texture Enhancement for Video Super-Resolution

- 方向：视频处理
- 作者：Dachun Kai, Jiayao Lu, Yueyi Zhang, Xiaoyan Sun
- 日期：2026-06-11
- 分类：cs.CV, cs.AI
- 关键词：video super-resolution
- arXiv：2606.13580v1

摘要：

Event-based vision has drawn increasing attention owing to its distinctive properties, including ultra-high temporal resolution and extreme dynamic range. Recent works have introduced it to video super-resolution (VSR) to enhance flow estimation and temporal alignment. In contrast, this paper shifts the focus of event signals from motion refinement to texture enhancement in VSR. We propose EvTexture++, the first event-driven framework dedicated to texture enhancement in VSR. It leverages high-frequency spatiotempor...

### 10. Budget-Constrained Step-Level Diffusion Caching

- 方向：底层视觉
- 作者：Mingkun Lei, Tong Zhao, Liangyu Yuan, Chi Zhang
- 日期：2026-06-11
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.13496v1

摘要：

Step-level caching accelerates diffusion models by exploiting temporal redundancy across denoising steps. Existing methods make per-step cache decisions using threshold-based heuristics, without directly optimizing for final output quality. As a result, their inference latency varies across inputs and is difficult to control at deployment. In this work, we propose BudCache, which inverts this formulation: rather than letting per-step error thresholds dictate the runtime cost, we fix the compute budget in advance an...

### 11. SmartFont: Dynamic Condition Allocation for Few-Shot Font Generation

- 方向：底层视觉
- 作者：Zian Yang, Zixin Wang
- 日期：2026-06-11
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2606.13382v1

摘要：

Few-shot font generation simultaneously requires global structural completeness and fine-grained local style fidelity. Existing methods usually either rely on global content-style modeling, which is robust but imperfectly disentangled, or emphasize component/local modeling, which captures fine details but relies heavily on local priors and reference coverage. We argue that the key challenge is not merely to learn purer conditions, but to organize complementary yet biased global and local conditions through multi-le...

### 12. DuET: Dual Expert Trajectories for Diffusion Image Editing

- 方向：底层视觉
- 作者：Lidia Troeshestova, Alexander Ustyuzhanin, Sergey Kastryulin
- 日期：2026-06-11
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.13303v1

摘要：

Recent diffusion editors perform diverse instruction-based edits while conditioning on the source image at every denoising step. Yet persistent source-image conditioning can limit how fully an edit is executed and how natural the result appears, especially when the target scene diverges substantially from the input. We introduce DuET (Dual Expert Trajectories), a training-free inference method that temporarily relaxes source-image conditioning by transitioning through a text-to-image phase before returning to edit...

### 13. High-Fidelity Two-Step Image Generation via Teacher-Aligned End-to-End Distillation

- 方向：底层视觉
- 作者：Dongyang Liu, Ruoyi Du, David Liu, Dengyang Jiang, Liangchen Li, Qilong Wu, et al.
- 日期：2026-06-10
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.12575v1

摘要：

Few-step diffusion distillation has become increasingly mature for 4-8-step generation, yet pushing further to 2 steps remains challenging. In this work, we introduce Z-Image Turbo++, a high-quality 2-step image generation model distilled from the 8-step Z-Image Turbo teacher. Our method addresses the central bottlenecks of increased task difficulty and limited model capacity in 2-step generation through three simple but effective design choices tailored to this regime. First, we propose Distribution-Aligned Advers...

### 14. Metadata-Aware Multi-Prompt Reasoning for Zero-Shot Accident Understanding

- 方向：顶会论文
- 作者：Tarandeep Singh, Soumyanetra Pal, Soham Biswas, Nishanth Chandran
- 日期：2026-06-10
- 分类：cs.CV, cs.AI, stat.ML
- 关键词：CVPR
- arXiv：2606.12047v1

摘要：

In this paper, we address the problem of zero-shot understanding of accidents from surveillance videos by identifying when an impact event occurs, what type of impact it is, and where in the frame it occurs using natural language. We propose a three-stage pipeline that decomposes the accident understanding into when, what, and where. The first stage extracts a short temporal window around the impact using vision-language similarity. In the second stage, we perform metadata-driven multi-prompt reasoning with five co...

### 15. Image Quality Assessment of Identity Cards Using Measures from Open Face Image Quality

- 方向：底层视觉
- 作者：Gregor Grote, Juan E. Tapia, Christian Rathgeb
- 日期：2026-06-10
- 分类：cs.CV, cs.CR
- 关键词：image quality assessment
- arXiv：2606.11884v1

摘要：

This paper addresses the challenge of assessing image quality in ID cards in remote verification systems by applying capture-related quality measures from the Open Face Image Quality (OFIQ) standard to ID card images. Our preprocessing pipeline includes corner detection, perspective normalization, and comprehensive foreground masking to ensure accurate and unbiased quality measure computation. We evaluate the effectiveness of these measures by analyzing their correlation with the performance of three presentation a...

### 16. Scene-Adaptive Nonlinear Tone Curves for Pseudo Ground-Truth Generation in Low-Light 3D Gaussian Splatting

- 方向：底层视觉
- 作者：Mingzhe Lyu, Jinqiang Cui, Hong Zhang
- 日期：2026-06-10
- 分类：cs.CV
- 关键词：low-light enhancement
- arXiv：2606.11841v1

摘要：

Low-light novel view synthesis is challenging because dark multi-view images contain noise, weak structural detail, and compressed dynamic range. Recent 3D Gaussian Splatting (3DGS) methods address these challenges by generating pseudo ground-truth (pseudo-GT) images as supervision targets when paired normal-light references are unavailable. Existing pseudo-GT methods apply a uniform linear gain to all pixels, which clips bright regions while providing insufficient enhancement in dark regions, limiting reconstructi...

### 17. RankVR: Low-Rank Structure Perception and Value Recalibration for Robust Composed Image Retrieval

- 方向：底层视觉
- 作者：Jiale Huang, Zixu Li, Zhiheng Fu, Zhiwei Chen, Qinlei Huang, Yupeng Hu
- 日期：2026-06-10
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.11689v1

摘要：

Composed Image Retrieval (CIR) constitutes a pivotal paradigm requiring models to perform joint reasoning on reference images and modification texts. However, the prevalence of Noisy Triplet Correspondence (NTC) in large-scale datasets severely constrains model performance. Existing denoising methods either target binary mismatches or rely on scalar-based point-wise estimation, neglecting rich global structural correlations among sample populations and dynamic value variations during training, thereby yielding subo...

### 18. Adv-TGD: Adversarial Text-Guided Diffusion for Face Recognition Impersonation Attacks

- 方向：底层视觉
- 作者：Omid Ahmadieh, Nima Karimian
- 日期：2026-06-10
- 分类：cs.CV, cs.CR, cs.LG
- 关键词：denoising
- arXiv：2606.11615v1

摘要：

The widespread adoption of face recognition (FR) technologies raises serious privacy concerns, as facial data can be exploited without consent. To address this challenge, we propose Adv-TGD, a generative adversarial attack framework that synthesizes photorealistic faces capable of impersonating target identities and deceiving face recognition systems. Built upon Stable Diffusion, Adv-TGD performs per-sample LoRA fine-tuning conditioned on concise textual prompts to generate natural yet adversarially manipulated ide...

### 19. AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference

- 方向：视频处理
- 作者：Hangfeng Liang, Yutao Hu, Yanhan Hu, Xiaohan Wu, Wenqi Shao, Ying Fu
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：video enhancement
- arXiv：2606.11186v1

摘要：

Low-light video enhancement (LLVE) remains a challenging task due to severe information degradation under low-illumination conditions. Recent multimodal approaches have significantly improved enhancement performance by incorporating auxiliary modalities, such as event streams and infrared images. However, these methods typically assume the availability of these modalities at inference, which is often not feasible in real-world scenarios. To solve this problem, in this work, we propose AMNet, a unified multimodal fr...

### 20. Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization

- 方向：底层视觉
- 作者：Paul Hyunbin Cho, Jinhyuk Jang, SeokYoung Lee, Joungbin Lee, Siyoon Jin, Heeseong Shin, et al.
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.11180v1

摘要：

Diffusion-based lip synchronization models achieve strong visual quality and audio-visual alignment, but full-sequence bidirectional attention and many denoising steps make them impractical for real-time inference. We present Lip Forcing, to our knowledge the first autoregressive diffusion method for video-to-video (V2V) lip synchronization, which distills a 14B audio-conditioned bidirectional video diffusion teacher into causal students. At inference, the students generate each chunk in only two denoising steps wi...

### 21. Envision4D: Envisioning Visual Futures via Feed-forward 4D Gaussian Splatting for Autonomous Driving

- 方向：底层视觉
- 作者：Qi Song, Yifei He, Chi Zhang, Zheng Fu, Xuhe Zhao, Mengmeng Yang, et al.
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.10656v1

摘要：

Forecasting the future evolution of dynamic scenes is crucial in autonomous driving. However, existing feed-forward paradigms are primarily designed for interpolation. When extended to future extrapolation, they suffer from ghosting artifacts under large displacements and are constrained by simplified motion assumptions or strict future priors. To overcome these challenges, we propose Envision4D, a fully self-supervised feed-forward framework for pose-free future extrapolation. Specifically, we introduce a Future P...

### 22. Few-step Generative Models as Lossy Compression

- 方向：底层视觉
- 作者：Fuma Kimishima, Jinjia Zhou
- 日期：2026-06-09
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2606.10450v1

摘要：

DiffC provides a principled way to reuse pre-trained diffusion models for lossy compression, but its encoding and decoding procedures remain slow because they require many discretized forward and reverse steps. We study whether few-step generative models -- Rectified Flow, Consistency Trajectory Models (CTM), and MeanFlow -- can be cast as codecs within the same reverse channel coding (RCC) framework. The main challenge is that RCC requires posterior and shared distribution parameters, whereas these models do not e...

### 23. PF-Trans: Physics-Embedded Frequency-Aware Transformer for Spectral Reconstruction

- 方向：底层视觉
- 作者：Yuzhe Gui, Tianzhu Liu, Yanfeng Gu, Xian Li
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.10373v1

摘要：

Snapshot Broadband Filter Array (BFA) imaging provides high light throughput for spectral reconstruction but introduces severe spectral aliasing due to complex modulation. Current deep learning approaches, limited to spatial denoising, often fail to address the global frequency-specific degradations caused by the mask structure. To address this, we propose a Physics-embedded Frequency-aware Transformer (PF-Trans) for high-fidelity remote sensing spectral reconstruction. Our method explicitly integrates the physical...

### 24. ClinReadNet: A clinical reading-inspired network for low-dose abdominal CT image quality assessment

- 方向：底层视觉
- 作者：Xianye Xiao, Yulong Zou, Yujie Luo, Taihui Yu, Cun-Jing Zheng, Yuan-ming Geng, et al.
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2606.10372v1

摘要：

In abdominal CT imaging, developing a low-dose, no-reference image quality assessment (No-reference IQA) model that mimics doctors' reading habits for evaluating CT image quality has significant practical value. This paper proposes a novel deep learning-based framework, ClinReadNet, whose design aligns with the clinical reading logic of radiologists: first, it introduces the Sobel ordinal quality network (SOQN) module, which can simultaneously focus on edge details highly relevant to image quality and the quality d...

### 25. Overlapped Wavelet Diffusion for Low-Light Image Enhancement

- 方向：底层视觉
- 作者：Fen Peng, Taizo Suzuki, Seisuke Kyochi
- 日期：2026-06-09
- 分类：eess.IV, cs.CV
- 关键词：image enhancement
- arXiv：2606.10280v1

摘要：

In this study, we propose an overlapped wavelet diffusion framework for Low-Light Image Enhancement (LLIE), which incorporates two complementary components to achieve blocking artifact-free and detail-preserving enhancement. Although recent diffusion-based LLIE methods have demonstrated remarkable performance compared with traditional approaches, DiffLL still suffers from blocking artifacts caused by the Haar Wavelet Transform (WT) and blurred edges or over-smoothed textures due to the limitations of its High-Frequ...

### 26. FoA-SR: Faithful or Aesthetic? Profile-Aware Preference Optimization for Real-World Image Super-Resolution

- 方向：底层视觉
- 作者：Amjad Mahdi Alqarni, Peizhong Ju
- 日期：2026-06-09
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2606.10275v1

摘要：

Real-world image super-resolution (SR) is often designed with a single restoration objective, despite the current capacity of generative models to produce multiple high-quality reconstructions for the same input. In this paper, we argue that the best restoration strategy is subject to the specific restoration profile: a Faithful restoration prioritizes reference consistency, structure preservation, and hallucination suppression, whereas an Aesthetic restoration prioritizes visually pleasing and natural-looking deta...

### 27. An Improved Generative Adversarial Network for Micro-Resistivity Imaging Logging Restoration

- 方向：底层视觉
- 作者：Ahmed Faizul Haque, S. M. Riaz Rahman Antu, Saif Ahmed, Asadullah Hil Galib, Souvik Pramanik, Mohammad Ashrafuzzaman Khan, et al.
- 日期：2026-06-08
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：image restoration
- arXiv：2606.10200v2

摘要：

An improved GAN-based imaging logging image restoration method is presented in this paper for solving the problem of partially missing micro-resistivity imaging logging images. The method uses FCN as the generative network infrastructure and adds a depth-separable convolutional residual block to learn and retain more effective pixel and semantic information; an Inception module is added to increase the multi-scale perceptual field of the network and reduce the number of parameters in the network; and a multi-scale...

### 28. MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models

- 方向：底层视觉
- 作者：Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou, Tiancai Wang, et al.
- 日期：2026-06-08
- 分类：cs.RO, cs.CV
- 关键词：denoising
- arXiv：2606.09827v1

摘要：

Temporal modeling is essential for robotic manipulation, as effective control requires both memory of past interactions and imagination of future states. However, most VLA models rely primarily on the current observation and therefore struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived context, the hippocampal system to preserve episodic memory of past experience, and internal models to imagine possible future state evolution. I...

### 29. PTL-Diffusion: Manifold-Aware Diffusion with Periodic Terminal Laws

- 方向：底层视觉
- 作者：Danqi Zhuang, Jisui Huang, Xiaoyue Xi, Andrew Kiggins, Xiaojie Wang, Ke Chen, et al.
- 日期：2026-06-08
- 分类：cs.CV, cs.AI, math.PR
- 关键词：denoising
- arXiv：2606.09816v1

摘要：

Standard diffusion models typically use a single time-homogeneous Gaussian terminal distribution as the reference law for generation. While this choice is analytically convenient and empirically powerful, it provides little explicit structure for data concentrated near low-dimensional manifolds, where different regions of the data distribution may correspond to distinct local geometric or semantic factors. As a result, the reverse model must recover manifold-level structure almost entirely from an unstructured term...

### 30. TUDSR: Twice Upsampling-Diffusion for Higher Super-Resolution

- 方向：底层视觉
- 作者：Zhiqiang Wu, Yitong Dong, Xian Wei
- 日期：2026-06-08
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2606.09608v1

摘要：

Diffusion-based generative models have achieved remarkable success in real-world image super-resolution (SR). With tiled diffusion techniques, these models can produce high-resolution images that exceed their native-supported resolution. However, the quality of such high-resolution (e.g $2048^2$) outputs often remains extremely poor, primarily due to two factors we consider: the image upsampling ratio (e.g $\times8$) exceeding the model's native-supported upsampling ratio (e.g $\times4$), and the model's native-sup...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-06-14-low-level-vision-video-papers.md`
