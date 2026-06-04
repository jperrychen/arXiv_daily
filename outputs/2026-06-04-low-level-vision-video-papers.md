---
title: 2026-06-04｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-06-04｜底层视觉与视频论文速览

生成时间：2026-06-04

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 29 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉、顶会论文｜Perception First: A Frontier Native-Video Model with Self-Consistency for Implicit Video Question Answering｜2026-05-31
2. 顶会论文｜Answer Self-Consistency with Margin-Triggered Question Re-Arbitration for the CVPR 2026 VidLLMs Challenge｜2026-06-03
3. 底层视觉｜LL-Bench: Rethinking Low-Level Vision Evaluation in the Era of Large-Scale Generative Models｜2026-06-01
4. 底层视觉｜Hallucination-Aware Diffusion Sampling for Inverse Problems via Robust Prior Updates｜2026-06-01
5. 顶会论文｜Training-Free Composed Video Retrieval via Visual Representation-Guided Video-LLM Reasoning｜2026-06-01
6. 顶会论文｜PerBite: A Curated Diagnostic Workflow for Bite-Aware Food Volume Estimation｜2026-06-01
7. 顶会论文｜3rd Place at CVPR 2026 CASTLE Challenge: Agentic Multi-View Long-Context Video Understanding via Hierarchical Knowledge Graph Retrieval｜2026-06-01
8. 底层视觉｜MaCo-GAN: Manifold-Contrastive Adversarial Learning for Single Image Super-Resolution｜2026-06-03
9. 底层视觉｜DSA: Dynamic Step Allocation for Fast Autoregressive Video Generation｜2026-06-03
10. 视频处理｜Ultra-Fast Neural Video Compression｜2026-06-03
11. 底层视觉｜Efficient and Training-Free Single-Image Diffusion Models｜2026-06-03
12. 底层视觉｜An Attention-Based Denoising Model for Diffusion Weighted Imaging｜2026-06-02
13. 底层视觉｜Unified Video-Action Joint Denoising for Dexterous Action and Data Generation｜2026-06-02
14. 底层视觉｜GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance｜2026-06-02
15. 底层视觉｜Inverting the Generation Process of Denoising Diffusion Implicit Models: Empirical Evaluation and a Novel Method｜2026-06-02
16. 底层视觉｜MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data｜2026-06-01
17. 底层视觉｜Drifting Preference Optimization for One-Step Generative Models｜2026-06-01
18. 底层视觉｜Deep Learning for Remote Sensing to Improve Flood Inundation Mapping｜2026-06-01
19. 底层视觉｜FocusDiT: Masking Queries in Diffusion Transformers for Fine-grained Image Generation｜2026-06-01
20. 视频处理｜TIDES: Time-Derivative Event Simulation via Deformable Reconstruction｜2026-06-01
21. 底层视觉｜Distortion-Aware Fusion of Statistical and Vision-Language Features for Blind Image Quality Assessment｜2026-06-01
22. 底层视觉｜Physics-Aware Linearized ADMM and Its Unrolling｜2026-06-01
23. 底层视觉｜PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation｜2026-06-01
24. 底层视觉｜Pave-GRPO: Beyond Instantaneous Guidance through Principled Average Velocity Decomposition｜2026-06-01
25. 底层视觉｜Real-Time Generation of Streamable Talking Portrait Video with Reference-Guided Deep Compression VAEs｜2026-06-01
26. 底层视觉｜Exploiting Semantic and Pixel Representations for Ultra-Low Bitrate Image Compression｜2026-06-01
27. 底层视觉｜Splatshot: 3D Face Avatar Generation from a Single Unconstrained Photo｜2026-05-31
28. 底层视觉｜HiTokSR: A Coarse-to-Fine Tokenizer with Hierarchical Codebooks for High-Fidelity Real-World Image Super-Resolution｜2026-05-31
29. 底层视觉｜Decoupled Residual Denoising Diffusion Models for Unified and Data Efficient Image-to-Image Translation｜2026-05-31

## 论文摘要

### 1. Perception First: A Frontier Native-Video Model with Self-Consistency for Implicit Video Question Answering

- 方向：底层视觉、顶会论文
- 作者：Ali Alavi
- 日期：2026-05-31
- 分类：cs.CV, cs.LG
- 关键词：denoising、CVPR 2026、CVPR
- arXiv：2606.01485v1

摘要：

We describe our submission to the VRR Challenge @ CVPR 2026, built on the \emph{ImplicitQA} / \emph{VRR-QA} benchmark~\cite{implicitqa}: multiple-choice video question answering in which answers are deliberately \emph{not} observable in any single frame and must be inferred from spatial layout, motion, depth, viewpoint, causality, and social context across discontinuous frames of creative video. We conduct a systematic, training-free study spanning open-source Video-LMMs (Qwen2.5-VL~\cite{qwen25vl}, Qwen3-VL~\cite{...

### 2. Answer Self-Consistency with Margin-Triggered Question Re-Arbitration for the CVPR 2026 VidLLMs Challenge

- 方向：顶会论文
- 作者：Tomoya Miyazawa, Hiroyasu Okuno
- 日期：2026-06-03
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- arXiv：2606.04323v1

摘要：

In this report, we present our solution for Track 2 of the CVPR 2026 VidLLMs Challenge. This track evaluates visual relational reasoning in videos, where models must infer relations that are not always explicitly visible. We propose Answer Self-Consistency with Margin-Triggered Question Re-Arbitration (ASC-MQRA), a training-free test-time reasoning framework built on a multimodal reasoning model. The core ASC component performs multiple stochastic video question-answering runs and aggregates their answer choices th...

### 3. LL-Bench: Rethinking Low-Level Vision Evaluation in the Era of Large-Scale Generative Models

- 方向：底层视觉
- 作者：Lu Liu, Huiyu Duan, Chenxin Zhu, Jintong Lu, Haoyun Jiang, Liu Yang, et al.
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：low-level vision、image quality assessment
- arXiv：2606.02535v1

摘要：

Large-scale generative models have demonstrated remarkable capabilities across image generation and editing tasks. However, their performance in low-level vision tasks, which require pixel-wise control, remains insufficiently studied. To address this gap, we introduce \textbf{LL-Bench}, a comprehensive \textbf{Benchmark} for evaluating the capabilities of large-scale generative models on \textbf{L}ow-\textbf{L}evel vision tasks. The benchmark comprises 2,469 real-world degraded images covering 16 low-level degradat...

### 4. Hallucination-Aware Diffusion Sampling for Inverse Problems via Robust Prior Updates

- 方向：底层视觉
- 作者：Pengfei Jin, Yiqi Tian, Kailong Fan, Bingjie Qi, Quanzheng Li
- 日期：2026-06-01
- 分类：cs.CV, cs.LG
- 关键词：deblurring、motion deblur
- arXiv：2606.02331v1

摘要：

Diffusion-based inverse problem solvers can produce realistic reconstructions, but realism alone does not ensure that the recovered details are supported by the measurement. We study this failure as measurement-conditioned hallucination: visually meaningful content that is either implausible or inconsistent with the measured instance. Our analysis separates Bayes-rule-based diffusion inverse solvers into a prior update and a measurement-conditioning step, showing that hallucinated content can enter through the prio...

### 5. Training-Free Composed Video Retrieval via Visual Representation-Guided Video-LLM Reasoning

- 方向：顶会论文
- 作者：Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Qingming Huang
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- arXiv：2606.02321v1

摘要：

Recent advances in large vision-language models have expanded video retrieval from simple text-based search to more flexible scenarios, where users may specify the desired result through both visual examples and textual instructions. In the CVPR 2026 Reason-Aware Composed Video Retrieval Challenge, the system is required to retrieve a target video according to a reference video and a modification instruction. To address this task, we develop Visual Representation-Guided Video-LLM Reasoning for Training-Free Compose...

### 6. PerBite: A Curated Diagnostic Workflow for Bite-Aware Food Volume Estimation

- 方向：顶会论文
- 作者：Ahmad AlMughrabi, Farid Al-Areqi, David Fernández Gómez, Umair Haroon, Marc Bolaños, Ricardo Marques, et al.
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- arXiv：2606.02021v1

摘要：

Can a visually plausible food mesh be trusted to estimate the volume of consumed food? \method investigates this question using selected paired before- and after-consumption states from the MetaFood CVPR 2026 Continuous 3D Reconstruction While Eating Challenge. The submitted workflow follows a curated reconstruction protocol: SAM~3 segments the food and plate regions; Hunyuan3D/SAM~3D generates a dimensionless food mesh; the plate diameter provides the metric scale; the plate geometry is removed in Blender; and the...

### 7. 3rd Place at CVPR 2026 CASTLE Challenge: Agentic Multi-View Long-Context Video Understanding via Hierarchical Knowledge Graph Retrieval

- 方向：顶会论文
- 作者：Raghad Albusayes, Munirah Alyahya
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- arXiv：2606.01933v1

摘要：

This paper presents our winning methodology for the CASTLE 2026 Challenge at the CVPR 2026 EgoVis Workshop, where our team secured third place globally. The challenge tasks participants with answering highly complex visual, spatiotemporal, and verbal questions, including visual counting, action localization, multi-view tracking and speaker temporal reasoning, within massive, multimodal video streams. The underlying dataset consists of over 600 hours synchronized footage captured by 15 ego and exo camera sources. To...

### 8. MaCo-GAN: Manifold-Contrastive Adversarial Learning for Single Image Super-Resolution

- 方向：底层视觉
- 作者：Daeyoung Han, Seongmin Hwang, Moongu Jeon
- 日期：2026-06-03
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2606.05068v1

摘要：

Conventional Generative Adversarial Networks (GANs) for Single Image Super-Resolution (SISR) often struggle with hallucinated artifacts, largely because standard discriminators evaluate overall image naturalness rather than strict conditional realism. To address this, we propose MaCo-GAN, a novel manifold-contrastive GAN framework that replaces the conventional adversarial loss with a supervised contrastive objective. A core component of our method is a dynamic fake sample synthesizer that transforms ground truth (...

### 9. DSA: Dynamic Step Allocation for Fast Autoregressive Video Generation

- 方向：底层视觉
- 作者：Thanh-Tung Le, Yunhan Zhao, Menglei Chai, Zhengyang Shen, Zhe Cao, Danhang Tang, et al.
- 日期：2026-06-03
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.04432v1

摘要：

Video diffusion transformers have achieved state-of-the-art visual quality, but their high inference cost remains a major bottleneck for real-time applications. Recent distillation frameworks produce autoregressive video diffusion models with reduced latency, yet these models still use a fixed number of denoising steps per frame, wasting computation on predictable frames and under-refining challenging ones. We present DSA, a confidence-guided adaptive computation framework for AR video diffusion. DSA introduces a l...

### 10. Ultra-Fast Neural Video Compression

- 方向：视频处理
- 作者：Jiahao Li, Wenxuan Xie, Zhaoyang Jia, Bin Li, Zongyu Guo, Xiaoyi Zhang, et al.
- 日期：2026-06-03
- 分类：cs.CV
- 关键词：video compression
- arXiv：2606.04410v1

摘要：

While neural video codecs (NVCs) have demonstrated superior compression ratio, their prohibitive computational complexity remains a critical barrier to real-world deployment. This paper introduces a chunk-based coding framework designed to significantly improve the rate-distortion-complexity trade-off. Instead of processing frames sequentially, our approach encodes a chunk of multiple frames into a single compact latent representation and decodes them simultaneously. This is enabled by cross-frame interaction modul...

### 11. Efficient and Training-Free Single-Image Diffusion Models

- 方向：底层视觉
- 作者：Haojun Qiu, Kiriakos N. Kutulakos, David B. Lindell
- 日期：2026-06-03
- 分类：cs.CV, cs.LG
- 关键词：image restoration
- arXiv：2606.04299v1

摘要：

We consider the problem of generating images whose internal structure -- defined by the distribution of patches across multiple scales -- matches that of a single reference image. Recent approaches address this problem by training a diffusion model on a single image. But even in this setting, training is computationally expensive and requires hours of optimization. Instead, we model the image using a dataset of its patches at different scales. As this dataset is finite and the dimensionality of its patches is small...

### 12. An Attention-Based Denoising Model for Diffusion Weighted Imaging

- 方向：底层视觉
- 作者：Prithviraj Verma, Pawan Kumar, Chandan Deshani, Prasun Chandra Tripathi
- 日期：2026-06-02
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.03903v1

摘要：

Diffusion-weighted imaging (DWI) is used for whole-body cancer screening, but it typically requires a long acquisition time. When the scan time is reduced, the image quality often suffers, leading to increased noise in the scans. Magnitude reconstruction in DWI introduces signal-dependent Rician noise, which makes denoising more challenging for conventional convolution-based methods. To address this limitation, we propose a noise-aware attention-driven denoising framework that integrates hierarchical Swin Transform...

### 13. Unified Video-Action Joint Denoising for Dexterous Action and Data Generation

- 方向：底层视觉
- 作者：Dingrui Wang, YuAn Wang, Jinkun Liu, Yue Zhang, Mattia Piccinini, Yu Sun, et al.
- 日期：2026-06-02
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.03868v1

摘要：

Recent world action models leverage video foundation models by aligning broad visual-dynamics priors with executable robot actions. We revisit this alignment from a distributional perspective. Existing formulations typically narrow the aligned prior into an observation-conditioned policy distribution over future actions. In contrast, we keep the distribution broader by modeling the joint space of interaction videos and executable hand trajectories under multiple conditioning regimes. We propose Donk, a unified vide...

### 14. GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance

- 方向：底层视觉
- 作者：Zehua Chen, Yucheng Yang, Binjie Yuan, Kaiwen Zheng, Jun S. Liu, Jun Zhu
- 日期：2026-06-02
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- arXiv：2606.03119v1

摘要：

Guidance methods, such as classifier-free guidance (CFG) and auto-guidance (AG), have advanced noise-to-data generation in diffusion models. Recently, bridge models have introduced a data-to-data generative process that can exploit an instructive clean prior. In this work, inspired by previous methods creating quality difference between denoising results as guidance, we propose a training-free bridge guidance method, termed Prior Guidance (PG). Specifically, we introduce a weak prior, which is unseen during bridge...

### 15. Inverting the Generation Process of Denoising Diffusion Implicit Models: Empirical Evaluation and a Novel Method

- 方向：底层视觉
- 作者：Yan Zeng, Masanori Suganuma, Takayuki Okatani
- 日期：2026-06-02
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.03111v1

摘要：

This paper studies the problem of inverting the DDIM image generation process to recover latent variables, particularly the initial noise map, from a generated image. Existing methods often struggle with accuracy in this task. We propose a novel hybrid approach that combines direct inversion via gradient descent for the first step, followed by a fixed-point method for subsequent steps. Empirical evaluations across three datasets demonstrate that our method significantly improves the prediction of initial latent var...

### 16. MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data

- 方向：底层视觉
- 作者：Teng Hu, Mingchun Lu, Yating Wang, Jiangning Zhang, Jinkun Hao, Ye Pan, et al.
- 日期：2026-06-01
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2606.02753v1

摘要：

Video world models are a foundational generative technology for embodied AI and the Metaverse, yet existing approaches are inherently limited to a single agent observing from a single perspective. Extending these models to multi-agent settings introduces two critical challenges: data scarcity (coordinated multi-view recordings are prohibitively expensive to collect for general open-domain scenarios) and world state alignment (independently generated video streams cannot ensure that shared physical environments and...

### 17. Drifting Preference Optimization for One-Step Generative Models

- 方向：底层视觉
- 作者：Zhou Jiang, Yandong Wen, Zhen Liu
- 日期：2026-06-01
- 分类：cs.LG, cs.CV
- 关键词：denoising
- arXiv：2606.02521v3

摘要：

One-step text-to-image generators are attractive for deployment because they generate an image with a single forward pass, but preference finetuning them remains difficult: standard alignment methods often rely on policy likelihoods, denoising trajectories, differentiable reward gradients, or test-time optimization. We propose Drifting Preference Optimization (DrPO), an online preference-finetuning method for deterministic one-step generators. For each prompt, DrPO samples candidates from the current generator, ran...

### 18. Deep Learning for Remote Sensing to Improve Flood Inundation Mapping

- 方向：底层视觉
- 作者：Yogesh Bhattarai, Vijay Chaudhary, Wai Lim Kim, Sanjib Sharma
- 日期：2026-06-01
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2606.02310v1

摘要：

Flooding is the most pervasive natural disaster worldwide. Timely and accurate flood inundation mapping are essential for informing disaster risk management. Optical satellite missions provide high-resolution, multispectral observations critical for flood detection and inundation mapping. However, their operational utility is severely constrained by cloud cover during extreme precipitation events. Conventional cloud-removal techniques based on temporal compositing or interpolation often fail to capture inundation d...

### 19. FocusDiT: Masking Queries in Diffusion Transformers for Fine-grained Image Generation

- 方向：底层视觉
- 作者：Xueji Fang, Liyuan Ma, Jianhao Zeng, Jinjin Cao, Mingyuan Zhou, Guo-Jun Qi
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.02090v2

摘要：

Diffusion transformer (DiT) has been widely adopted in the generative diffusion field, advancing the denoising of query tokens through attention and Feed-Forward (\text{FFN}) layers. FFN actually acts as the key-value vocabulary for decoding visual contents where the value embeds the visual semantical knowledge. We present that focusing on critical query tokens corresponding to more complex details and encouraging the model to improve these tokens is essential for fine-grained visual generation. To this end, we pro...

### 20. TIDES: Time-Derivative Event Simulation via Deformable Reconstruction

- 方向：视频处理
- 作者：Christopher Thirgood, Dipon Kumar Ghosh, Simon Hadfield
- 日期：2026-06-01
- 分类：cs.CV, cs.RO
- 关键词：frame interpolation
- arXiv：2606.02058v1

摘要：

Event cameras emit asynchronous events in response to environmental appearance changes. The scarcity of real-world event datasets makes simulation essential. However, most simulators infer event timestamps from frame sequences, forcing many threshold crossings to share a small set of discrete times; a failure mode we term timestamp batching that worsens under fast motion and occlusion. We present TIDES, a continuous-time event simulator built on dynamic Gaussian splatting. Because TIDES operates on an explicit 3D s...

### 21. Distortion-Aware Fusion of Statistical and Vision-Language Features for Blind Image Quality Assessment

- 方向：底层视觉
- 作者：Bishr Omer Abdelrahman Adam, Xu Li
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2606.02002v1

摘要：

Blind image quality assessment (BIQA) aims to predict perceived image quality without access to a reference image. Classical natural scene statistics (NSS) descriptors and modern vision-language model (VLM) embeddings address this problem from fundamentally different perspectives, yet whether combining them yields complementary benefits and how to weight their contributions per input image remains unexplored. We propose a distortion-aware fusion framework that integrates a 138-dimensional NSS descriptor with two co...

### 22. Physics-Aware Linearized ADMM and Its Unrolling

- 方向：底层视觉
- 作者：Satoshi Takabe, Shunta Arai, Tadashi Wadayama
- 日期：2026-06-01
- 分类：eess.SP, cs.CV
- 关键词：image restoration
- arXiv：2606.01652v1

摘要：

Recently, partial differential equations (PDEs) have been used to directly model the measurement process in signal processing, although their evaluation is costly. In this paper, we propose a novel alternating direction method of multipliers (ADMM)-based algorithm called physics-aware linearized ADMM (PA-LADMM) for inverse problems from PDE-based measurement processes. The key idea is the linearization of the subproblem with PDEs, leading to a cost-efficient update rule that calls only a PDE solver and its gradient...

### 23. PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation

- 方向：底层视觉
- 作者：Weixing Chen, Zhuoqian Feng, Yang Liu, Yexin Zhang, Yifan Wen, Yinghong Liao, et al.
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.01649v2

摘要：

Generating physically consistent 3D tabletop scenes is a fundamental yet underexplored problem for interactive and generalist robotic learning. The challenge stems from dense object hierarchies and irregular affordances. Here, an interactive scene denotes a physically valid, collision-free environment directly loadable into physics simulators. Existing methods, ranging from decoupled symbolic solvers to end-to-end regression models, often suffer from error propagation or overfitting to noisy supervision containing...

### 24. Pave-GRPO: Beyond Instantaneous Guidance through Principled Average Velocity Decomposition

- 方向：底层视觉
- 作者：Pengyang Ling, Jiazi Bu, Yujie Zhou, Yibin Wang, Zhenyu Hu, Zihan Zhang, et al.
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.01636v1

摘要：

Post-training via Group Relative Policy Optimization (GRPO) has emerged as a powerful paradigm for aligning flow-based generative models with human preferences. However, the iterative denoising nature of flow models incurs substantial costs when generating group rollouts for policy-gradient updates, compelling existing methods to train with extremely few denoising steps. This temporal sparsity severely restricts preference optimization: reward feedback can only reach a handful of stages per trajectory, leaving the...

### 25. Real-Time Generation of Streamable Talking Portrait Video with Reference-Guided Deep Compression VAEs

- 方向：底层视觉
- 作者：Sicheng Xu, Yu Deng, Shoukang Hu, Yichuan Wang, Yizhong Zhang, Zhan Chen, et al.
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.01620v1

摘要：

Video diffusion models have significantly advanced portrait video generation, yet their high computational demands limit their use in interactive applications. This work presents a framework for streamable talking portrait video generation conditioned on speech audio and reference images. Designed meticulously for streaming scenarios, it features a causal video VAE for deep latent compression and an autoregressive latent denoising model. Our causal VAE integrates a variable number of reference images as guidance, a...

### 26. Exploiting Semantic and Pixel Representations for Ultra-Low Bitrate Image Compression

- 方向：底层视觉
- 作者：Hao Wei, Yanhui Zhou, Chenyang Ge, Saeed Anwar, Ajmal Mian
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：image compression
- arXiv：2606.01608v1

摘要：

Most existing extreme compression methods fail to achieve an optimal rate-distortion-perception trade-off, as they typically prioritize perceptual fidelity and visual realism over pixel-level accuracy. Consequently, the resulting reconstructions often deviate noticeably from the originals. Ultra-low bitrate image compression is therefore crucial-not only for producing extremely compact representations but also for ensuring that reconstructed images remain semantically coherent and faithful to the source at the pixe...

### 27. Splatshot: 3D Face Avatar Generation from a Single Unconstrained Photo

- 方向：底层视觉
- 作者：Hao Liang, Zhixuan Ge, Soumendu Majee, Joanna Li, Ashok Veeraraghavan, Guha Balakrishnan
- 日期：2026-05-31
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.01493v1

摘要：

Reconstructing a photorealistic 3D face avatar from a single unconstrained photograph is challenging: feed-forward 3D Gaussian Splatting (3DGS) models degrade on out-of-distribution inputs, while pretrained diffusion models produce high-fidelity images but lack multi-view consistency. We observe that these paradigms are fundamentally complementary: explicit 3D representations guarantee geometric consistency, whereas 2D diffusion priors ensure photorealism. Building on this, we propose SplatShot, a training-free fra...

### 28. HiTokSR: A Coarse-to-Fine Tokenizer with Hierarchical Codebooks for High-Fidelity Real-World Image Super-Resolution

- 方向：底层视觉
- 作者：Mingxi Li
- 日期：2026-05-31
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2606.01157v1

摘要：

Vector-quantized (VQ) generative models have shown promising results in real-world image super-resolution (Real-ISR). However, existing methods typically rely on a monolithic latent space that entangles low-frequency structures with high-frequency textures. This entanglement forces a single codebook to capture a combinatorially complex set of structure-texture pairings, which constrains representational capacity and limits codebook utilization. To address this issue, we present HiTokSR, a hierarchical token predict...

### 29. Decoupled Residual Denoising Diffusion Models for Unified and Data Efficient Image-to-Image Translation

- 方向：底层视觉
- 作者：Ziyue Lin, Jiahe Hou, Hongyu Xia, Xinrui Xie, Feifei Wang, Yuyin Zhou, et al.
- 日期：2026-05-31
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.01048v1

摘要：

We propose Decoupled Residual Denoising Diffusion models (DRDD) for unified and data-efficient image-to-image (I2I) translation. While diffusion models have advanced I2I translation in terms of quality and diversity, we uncover a previously under-explored property in diffusion models. Crucially, beyond its conventional role of manifold lifting (i.e., moving data off low-dimensional manifolds), injecting Gaussian noise facilitates domain harmonization by implicitly aligning feature distributions across domains, a pr...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-06-04-low-level-vision-video-papers.md`
