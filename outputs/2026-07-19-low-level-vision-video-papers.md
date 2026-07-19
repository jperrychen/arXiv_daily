---
title: 2026-07-19｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-07-19｜底层视觉与视频论文速览

生成时间：2026-07-19

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Filtering-out poor-quality images for data preparation｜2026-07-14
2. 视频处理｜SVI360: Spherical Video Interpolation｜2026-07-13
3. 顶会论文｜Technical Report on the CVPR 2026@AdvML Workshop Challenge｜2026-07-13
4. 底层视觉｜Hierarchical Denoising For Multi-Step Visual Reasoning｜2026-07-16
5. 底层视觉｜QuReC: All-in-One Image Restoration with Query-Specific Guidance and Local-Global Response Calibration｜2026-07-16
6. 底层视觉｜DriftWorld: Fast World Modeling through Drifting｜2026-07-16
7. 底层视觉｜Weakly-Supervised RGB-D Salient Object Detection via SAM-driven Pseudo Annotation and State Space Interaction-based Diffusion｜2026-07-16
8. 底层视觉｜JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting｜2026-07-16
9. 底层视觉｜From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting｜2026-07-16
10. 底层视觉｜FlashDecoder: Real-Time Latent-to-Pixel Streaming Decoder with Transformers｜2026-07-16
11. 底层视觉｜MixCompress: Mixture of Experts for Variable Rate Learned Image Compression｜2026-07-15
12. 视频处理｜DCVC-MB: Neural B-Frame Video Compression using State Space Models｜2026-07-15
13. 底层视觉｜M$^\text{4}$World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming｜2026-07-15
14. 底层视觉｜Inference-Time Concept Suppression and Video-Centric Evaluation for Text-to-Video Models｜2026-07-15
15. 底层视觉｜Thresholded Cross-Attention for Reliable Intensity-Chromaticity Fusion in Low-Light Image Enhancement｜2026-07-15
16. 底层视觉｜DNA: Dual-stage Native Attribution for Generated Image Source Tracing｜2026-07-15
17. 视频处理｜LPM: Industrial-Scale Generative Video Restoration｜2026-07-15
18. 底层视觉｜Improving Medical Image Generative Models with Fréchet Distance Loss｜2026-07-14
19. 底层视觉｜Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation｜2026-07-14
20. 底层视觉｜The Seriality Gap in Video Diffusion Models｜2026-07-14
21. 底层视觉｜RFMSR: Residual Flow Matching for Image Super-Resolution｜2026-07-14
22. 底层视觉｜ARDepth: Auto-regressive Monocular Depth Estimation with Progressive Visual Conditioning｜2026-07-14
23. 底层视觉｜Virtual Chromoendscopy with Tunable Visibility Enhancement｜2026-07-14
24. 底层视觉｜IQA-T1: Tool-based Visual Evidence Reasoning for Image Quality Assessment｜2026-07-14
25. 底层视觉｜ACID: Adaptive Caching for vIDeo generation｜2026-07-14
26. 底层视觉｜Self-Consistent Flow: Unifying Velocity and Endpoint Prediction for Rectified Flow Models｜2026-07-13
27. 底层视觉｜DiffEEG: A Self-Supervised Denoising Diffusion Model for Learning EEG Generic Representations｜2026-07-13
28. 底层视觉｜Adaptive Routing for Efficient Diffusion Transformer-Based PNI Prediction｜2026-07-13
29. 底层视觉｜Diffusion MRI preprocessing affects ADC estimation and automatic PI-RADS v2.1 classification in bi-parametric prostate MRI｜2026-07-13
30. 底层视觉｜Structure-Detail Decoupled Autoregressive Generation for Fast and High-Fidelity Virtual Try-On｜2026-07-13

## 论文摘要

### 1. Filtering-out poor-quality images for data preparation

- 方向：底层视觉
- 作者：Roopdeep Kaur, Gour Karmakar, Muhammad Imran
- 日期：2026-07-14
- 分类：cs.CV
- 关键词：image denoising、denoising、image quality assessment
- arXiv：2607.12352v1

摘要：

Filtering noise is a fundamental part of data preparation that enhances image quality for applications such as object segmentation, detection, and recognition. Various noise reduction techniques are proposed in the literature, including the use of median, Gaussian, and bilateral filters. Convolutional neural networks (CNNs) have gained popularity in image denoising owing to their ability to extract complex patterns and features from data. CNNs are highly adaptable, making them effective tools for various image-deno...

### 2. SVI360: Spherical Video Interpolation

- 方向：视频处理
- 作者：Le-Kim Nguyen, Renato Martins, Pascal Vasseur, Cedric Demonceaux
- 日期：2026-07-13
- 分类：cs.CV
- 关键词：video interpolation、video enhancement
- arXiv：2607.11710v1

摘要：

This paper addresses the problem of omnidirectional video interpolation, which plays an essential role in applications such as virtual reality and immersive video enhancement. Existing video interpolation methods are not well-suited for spherical videos, as they have difficulty handling severe distortions close to the poles. To address this issue, we propose SVI360, a dual-branch framework that combines the image frame and its rotated orthogonal view to deal with these distortions. The core methodological aspect of...

### 3. Technical Report on the CVPR 2026@AdvML Workshop Challenge

- 方向：顶会论文
- 作者：Tianyuan Zhang, Zonglei Jing, Jiangfan Liu, Ligong Zhang, Ke Ma, Chengzhi Sun, et al.
- 日期：2026-07-13
- 分类：cs.CV, cs.AI
- 关键词：CVPR 2026、CVPR
- arXiv：2607.11560v1

摘要：

Vision-language agents (VLAs) are increasingly used to interpret complex driving scenes and support safety-critical reasoning. This report presents the CVPR 2026@AdvML Workshop Challenge on adversarial multimodal attacks against autonomous-driving VLAs. Built on DriveLM-style multi-view visual question answering, the challenge represents each scene with six synchronized camera images and a structured collection of driving-related question-answer pairs. Participants generate adversarial images and suffix-only textua...

### 4. Hierarchical Denoising For Multi-Step Visual Reasoning

- 方向：底层视觉
- 作者：Zezhong Qian, Xiaowei Chi, Chak-Wing Mak, Tianze Zhou, Ruibin Yuan, Yuhan Rui, et al.
- 日期：2026-07-16
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.15278v1

摘要：

Video models are evolving into vision foundation models, yet they still lack human-like multi-step reasoning. Streaming autoregressive diffusion models are efficient but limited in reasoning, while bidirectional diffusion enables global revision with high inference costs due to dense frame-level denoising. Both paradigms struggle to achieve logical consistency and low-latency streaming for complex reasoning tasks. We propose HDR (Hierarchical Denoising for Visual Reasoning), a unified framework that integrates hier...

### 5. QuReC: All-in-One Image Restoration with Query-Specific Guidance and Local-Global Response Calibration

- 方向：底层视觉
- 作者：Shen Zhou, Jinghui Zhang, Wenbo Huang, Xuwei Qian, Zhen Wu, Guangwen Peng, et al.
- 日期：2026-07-16
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2607.15097v1

摘要：

All-in-one image restoration aims to recover clean images degraded by multiple corruption types using a single unified model. Existing methods typically rely on image-level prompts or shared guidance to handle diverse degradations. However, such a paradigm becomes inadequate when degradations are spatially heterogeneous or even coexist in mixed forms within a single image. Yet spatially adaptive guidance alone is not sufficient, since accurate restoration also requires each spatial query to reliably aggregate compl...

### 6. DriftWorld: Fast World Modeling through Drifting

- 方向：底层视觉
- 作者：Susie Lu, Haonan Chen, Weirui Ye, Yilun Du
- 日期：2026-07-16
- 分类：cs.RO, cs.CV, cs.LG
- 关键词：denoising
- arXiv：2607.15065v1

摘要：

Predictive world models enable robots to plan by imagining the outcomes of their actions, but their value for control hinges on generating many rollouts quickly. This creates a bottleneck for diffusion-based world models: multistep sampling makes each rollout expensive, limiting large-scale action search at inference time. We introduce DriftWorld, an action-conditioned world model based on drifting generative models. Rather than denoising iteratively at inference, DriftWorld learns an action-conditioned drift durin...

### 7. Weakly-Supervised RGB-D Salient Object Detection via SAM-driven Pseudo Annotation and State Space Interaction-based Diffusion

- 方向：底层视觉
- 作者：Wenqi Si, Gongyang Li, Shixiang Shi, Weisi Lin
- 日期：2026-07-16
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.15041v1

摘要：

Weakly-supervised RGB-D Salient Object Detection (SOD) is explored to reduce the heavy burden of pixel-level annotations. But scribble annotations lack the structure and details of objects, resulting in inaccurate saliency maps. In this paper, we propose a novel scribble-supervised RGB-D SOD method, consisting of a Segment Anything Model (SAM)-driven pseudo annotation generation method (\emph{SAM-PAG}) and a state space interaction-based conditional diffusion model (\emph{$S^2$Diff}). Specifically, SAM-PAG is tailo...

### 8. JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting

- 方向：底层视觉
- 作者：Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao
- 日期：2026-07-16
- 分类：cs.CV
- 关键词：deblurring
- arXiv：2607.14990v1

摘要：

When a camera moves fast during exposure, blur destroys the intra-exposure motion a 3D model needs to recover the sharp scene, while event cameras capture exactly this signal at microsecond resolution. Turning them into reliable 3D supervision faces two obstacles. First, the two restoration priors fail in opposite ways: physics-based event-integration priors preserve edges but accumulate drift; learned networks recover texture but distort boundaries. Second, existing pipelines run in one direction only, so raw even...

### 9. From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting

- 方向：底层视觉
- 作者：Zizhao Chen, Ping Wei, Guang Dai, Jingdong Wang, Mengmeng Wang
- 日期：2026-07-16
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.14976v1

摘要：

Video object removal is a fundamental yet challenging task in video editing. Despite recent progress, existing methods typically fall into two categories. Traditional approaches based on optical flow or attention mechanisms often introduce noticeable artifacts and yield unnatural results. In contrast, diffusion-based methods improve visual realism but demand multiple denoising steps, limiting their practicality. To address these issues, we propose From-Draft-to-Draft-Free (D2DF), a framework that distills the abili...

### 10. FlashDecoder: Real-Time Latent-to-Pixel Streaming Decoder with Transformers

- 方向：底层视觉
- 作者：Minguk Kang, Suha Kwak
- 日期：2026-07-16
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2607.14898v1

摘要：

Real-time video generation demands fast decoding as much as fast denoising, yet current latent video diffusion models rely on 3D convolutional decoders that are slow and memory-intensive at high resolutions or for long video. We introduce FlashDecoder, a fast, memory-efficient pure-Transformer video decoder that decodes latents to pixels frame by frame. At each step, the current frame attends only to a fixed-size window of past frames through a rolling KV cache. The fixed temporal window keeps decoding fast and mem...

### 11. MixCompress: Mixture of Experts for Variable Rate Learned Image Compression

- 方向：底层视觉
- 作者：Calvin-Khang Ta, Praneet Singh, Tong Shao, Peng Yin
- 日期：2026-07-15
- 分类：cs.CV
- 关键词：image compression
- arXiv：2607.14334v1

摘要：

Learned image compression (LIC) is bottlenecked by the need to store independent models for each rate-distortion operating point. Existing variable bit-rate (VBR) methods aim to reduce this overhead via dense parameter modulation, but forcing a shared backbone to approximate divergent mappings causes severe feature entanglement. Specifically, low-rate smoothing gradients inherently conflict with the preservation of high-frequency textural details, leading to sub-optimal performance. To resolve this, we propose MixC...

### 12. DCVC-MB: Neural B-Frame Video Compression using State Space Models

- 方向：视频处理
- 作者：Arjun Arora, Calvin-Khang Ta, Carlos Restrepo-Galeano, Kruthi Murali, Naga Akhil E S, Arunkumar Mohananchettiar, et al.
- 日期：2026-07-15
- 分类：cs.CV
- 关键词：video compression
- arXiv：2607.14305v1

摘要：

In this paper we propose DCVC-Mamba (DCVC-MB), a neural video codec framework for B-frame coding. Our approach incorporates an IBP frame strategy for low-delay B-frame coding, a spatio-temporal fusion model based on state-space models for bidirectional temporal prediction, and an entropy-aware skipping mechanism that selectively omits coding certain latents to reduce entropy coding times. In addition to our model contributions we also implement two inference-time strategies that enhance compression performance. Exp...

### 13. M$^\text{4}$World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming

- 方向：底层视觉
- 作者：Ke Cheng, Hanqiao Ye, Lei Shi, Yahui Liu, Yunhan Shen, Jingtao Dong, et al.
- 日期：2026-07-15
- 分类：cs.CV, cs.RO
- 关键词：denoising
- arXiv：2607.14005v1

摘要：

Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability. We present M$^\text{4}$World, a Multi-view and Multimodal generative driving world model that synthesizes future surround-view video streams and synchronized LiDAR scans while supporting interactive object Manipulation and stable Minute-long streaming. Fine-grained object manipulation is realized through a flexible condi...

### 14. Inference-Time Concept Suppression and Video-Centric Evaluation for Text-to-Video Models

- 方向：底层视觉
- 作者：Wenxuan Chen, Wenjie Feng
- 日期：2026-07-15
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2607.14194v1

摘要：

Text-to-video (T2V) generators can synthesize realistic and temporally coherent videos, but controllably removing a target concept from a generator remains difficult. Unlike text-to-image concept erasure, T2V unlearning must suppress a target concept that may persist across frames while preserving non-target subjects, actions, scenes, and temporal structure. We propose \textbf{SIRUS}, a training-free inference-time framework for concept-level T2V unlearning. Given textual aliases of a target concept, SIRUS localize...

### 15. Thresholded Cross-Attention for Reliable Intensity-Chromaticity Fusion in Low-Light Image Enhancement

- 方向：底层视觉
- 作者：Yanyi Wu, Xu Zhang, Junkai Chen, Laibin Chang, Jiaqi Ma, Shi Chen, et al.
- 日期：2026-07-15
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2607.13925v1

摘要：

Low-Light Image Enhancement (LLIE) requires a careful balance among noise suppression, color fidelity, and efficiency. Recent HVI-based methods alleviate color entanglement by decoupling intensity and chromaticity, yet how reliably the two streams are fused again is an overlooked factor that largely determines the final quality. We observe that the confidence of cross-stream attention is strongly layer-dependent, so the fixed-quota selection of Top-K sparse attention is mismatched to it, discarding informative depe...

### 16. DNA: Dual-stage Native Attribution for Generated Image Source Tracing

- 方向：底层视觉
- 作者：Chao Wang, Kejiang Chen, Zijin Yang, Yaofei Wang, Yuang Qi, Weiming Zhang, et al.
- 日期：2026-07-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.13685v1

摘要：

The rapid evolution of image generation has produced numerous within-family variants, making source-model attribution of suspect images increasingly important for digital forensics. Existing proactive methods rely on watermark embedding or model modification, which may degrade visual quality and limit deployment flexibility. Passive methods often rely on large-scale supervised training or a single reconstruction signal, limiting their ability to handle unknown sources and distinguish highly similar within-family va...

### 17. LPM: Industrial-Scale Generative Video Restoration

- 方向：视频处理
- 作者：Bichuan Zhu, Fulin Li, Jiachao Gong, Jinhua Hao, Kai Zhao, Kun Yuan, et al.
- 日期：2026-07-15
- 分类：cs.CV
- 关键词：video restoration
- arXiv：2607.13460v1

摘要：

We present the Large Processing Model (LPM), a diffusion-based generative framework for photorealistic video restoration under complex, in-the-wild degradations. To our knowledge, LPM is the first generative video restoration model deployed at industrial scale. LPM addresses the diverse degradations in user-generated content (UGC) through a unified system encompassing large-scale data engineering, foundation-model training, and efficient inference. Its enhanced architecture, progressive training strategy, and tempo...

### 18. Improving Medical Image Generative Models with Fréchet Distance Loss

- 方向：底层视觉
- 作者：Andrew Marshall, Xuanang Xu, Xiaoran Zhang, Rui Wang, Lawrence Staib, James Duncan
- 日期：2026-07-14
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.13300v1

摘要：

Diffusion generative models have demonstrated immense potential for synthetic medical image generation. However, these models often struggle to capture complex morphological characteristics of heterogeneous tumors with irregular boundaries, limiting their utility for downstream clinical tasks such as segmentation. This limitation stems from the standard denoising objective: minimizing a per-pixel error, which smooths high-variance irregular structures characteristic of tumors. To address this, we propose finetuning...

### 19. Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation

- 方向：底层视觉
- 作者：Ruize Xia
- 日期：2026-07-14
- 分类：cs.CL, cs.CV, cs.LG
- 关键词：denoising
- arXiv：2607.13164v1

摘要：

Sign language is a primary communication channel for millions of Deaf and hard-of-hearing people, yet text-to-signer video generation remains costly because video diffusion models are expensive to train and evaluate. This paper presents Text2Sign, a text-conditioned diffusion model for short sign-language clips that runs on a single NVIDIA L4 GPU. It combines a frozen vision-language text encoder with a 3D encoder-decoder and factorized spatiotemporal attention to reduce the cost of full-video attention while prese...

### 20. The Seriality Gap in Video Diffusion Models

- 方向：底层视觉
- 作者：Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai
- 日期：2026-07-14
- 分类：cs.LG, cs.CV
- 关键词：denoising
- arXiv：2607.13031v1

摘要：

When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent, the degradation largely disappears, isolating dependent-event structure rather than video length as the cause. Across...

### 21. RFMSR: Residual Flow Matching for Image Super-Resolution

- 方向：底层视觉
- 作者：Shuwei Huang, Tianyao Luo, Jicheng Liu, Daizong Liu, Pan Zhou
- 日期：2026-07-14
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2607.12753v1

摘要：

Image super-resolution (ISR) has witnessed remarkable progress with diffusion models and flow matching. The dominant text-to-image (T2I) based approaches leverage large-scale foundation models as generative priors, achieving impressive perceptual quality but at the cost of massive model sizes and prohibitive training expenses. Recent flow-matching-based vision-only approaches have made significant strides; however, they adopt standard flow formulations that transport from a pure Gaussian prior to the data distribut...

### 22. ARDepth: Auto-regressive Monocular Depth Estimation with Progressive Visual Conditioning

- 方向：底层视觉
- 作者：Zijie Wang, Wei Zhang, Weiming Zhang, Xiao Tan, Weikai Chen, Xiaoxu Li, et al.
- 日期：2026-07-14
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2607.12433v1

摘要：

Diffusion models have recently become the dominant paradigm for monocular depth estimation (MDE). However, they implicitly assume that depth can be recovered as a globally smooth field through iterative denoising, which does not explicitly reflect the piecewise and scale-dependent organization of scene geometry. In practice, geometric structure emerges progressively across spatial scales, where coarse layout, surfaces, and boundaries are constructed in a hierarchical manner. Motivated by this observation, we introd...

### 23. Virtual Chromoendscopy with Tunable Visibility Enhancement

- 方向：底层视觉
- 作者：Yuhi Kanno, Yusuke Monno, Sho Suzuki, Tomohiro Tada, Masatoshi Okutomi
- 日期：2026-07-14
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2607.12416v1

摘要：

Chromoendoscopy (CE) is a common clinical practice that sprays indigo carmine blue dye onto the gastric surface to improve the visibility of gastric lesions, such as an early cancer. While CE is effective in detecting the lesions, preparing and spraying the dye needs additional cost and time, which is undesirable both for patients and medical practitioners. To overcome this issue, virtual chromoendoscopy (V-CE) was recently proposed, which applies a learned image translation model to virtually generate a CE image f...

### 24. IQA-T1: Tool-based Visual Evidence Reasoning for Image Quality Assessment

- 方向：底层视觉
- 作者：Jinjian Wu, Jiaqi Tang, Wei Wei, Yingying Yan, Jianmin Chen, Botong Geng, et al.
- 日期：2026-07-14
- 分类：cs.CV, cs.AI, eess.IV
- 关键词：image quality assessment
- arXiv：2607.12375v1

摘要：

Image Quality Assessment (IQA) in open-world environments remains challenging due to limited generalization and interpretability. Recent approaches based on multimodal large language models (MLLMs) introduce textual reasoning for quality prediction, yet their judgments rely heavily on semantically biased internal representations, making them insensitive to low-level perceptual degradations. We propose IQA-T1, a tool-based visual evidence reasoning framework that augments MLLM reasoning with explicit perceptual obse...

### 25. ACID: Adaptive Caching for vIDeo generation

- 方向：底层视觉
- 作者：Om Agrawal, Saurabh Agarwal, Aditya Akella
- 日期：2026-07-14
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.12358v2

摘要：

Video diffusion models produce high-quality generations but remain slow at inference due to their sequential denoising procedure. Caching-based acceleration methods address this by reusing intermediate model outputs: leading dynamic approaches such as TeaCache, EasyCache, and DiCache accumulate a drift signal and skip expensive model evaluations when accumulated drift stays below a fixed threshold $τ$. This threshold controls an apparent tradeoff - raising it yields faster generation at the cost of visual quality,...

### 26. Self-Consistent Flow: Unifying Velocity and Endpoint Prediction for Rectified Flow Models

- 方向：底层视觉
- 作者：Xu Han, Jiajing Hu, Li-Ping Liu
- 日期：2026-07-13
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- arXiv：2607.12171v1

摘要：

In rectified-flow-based generative models, the neural network can be trained to predict two different targets, such as the instantaneous velocity or the data endpoint, to perform denoising. Although prior work shows that these parameterizations lead to different empirical behaviors, the mechanisms underlying their respective advantages remain to be underexplored, and how to combine them effectively is still unclear. In this work, we analyze how learning errors from different parameterizations affect the generation...

### 27. DiffEEG: A Self-Supervised Denoising Diffusion Model for Learning EEG Generic Representations

- 方向：底层视觉
- 作者：Abdulkader Helwan, Lina Abou-Abbas, Hussein El Amouri, Belkacem Chikhaoui, Khadidja Henni
- 日期：2026-07-13
- 分类：cs.LG, cs.AI, cs.CV, eess.SP
- 关键词：denoising
- arXiv：2607.11578v1

摘要：

Deep learning for EEG-based seizure detection faces critical challenges: severe annotation scarcity and extreme class imbalance, where ictal events comprise less than 10% of clinical recordings. We present DiffEEG, a 9.6M-parameter self-supervised foundation model that addresses both limitations through denoising diffusion pre-training and reinforcement learning (RL)-based fine-tuning. Pre-trained on 1.3M unlabeled segments from the Temple University Hospital Seizure Corpus (TUHSZ), DiffEEG learns generic neural re...

### 28. Adaptive Routing for Efficient Diffusion Transformer-Based PNI Prediction

- 方向：底层视觉
- 作者：Youngung Han, Dohyun Kweon, Kyeonghun Kim, Hyunsu Go, Jina Jeong, Suah Park, et al.
- 日期：2026-07-13
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2607.11533v1

摘要：

Perineural invasion (PNI) is a critical prognostic factor in cholangiocarcinoma. However, its preoperative prediction from magnetic resonance imaging (MRI) remains challenging due to subtle imaging features that extend beyond tumor boundaries into surrounding regions. Conventional convolutional neural networks are limited in capturing long-range spatial dependencies. Transformer-based architectures improve global modeling of volumetric MRI by aggregating spatially distributed contextual cues, yet capturing subtle a...

### 29. Diffusion MRI preprocessing affects ADC estimation and automatic PI-RADS v2.1 classification in bi-parametric prostate MRI

- 方向：底层视觉
- 作者：Christos Kanakis, Mathias Perslev, Tim Schakel, Silvia Ingala, Akshay Pai, Dennis Klomp, et al.
- 日期：2026-07-13
- 分类：eess.IV, cs.CV
- 关键词：denoising
- arXiv：2607.11385v1

摘要：

Diffusion-weighted imaging (DWI) is acquired as part of bi-parametric prostate MRI, but suffers from artifacts that degrade downstream quantitative and diagnostic performance. While DWI preprocessing is standard in brain imaging, its adoption in prostate imaging remains limited and lacks standardized pipelines. This study investigated the effect of different DWI preprocessing strategies on apparent diffusion coefficient (ADC) estimation and automatic Prostate Imaging Reporting and Data System (PI-RADS) classificati...

### 30. Structure-Detail Decoupled Autoregressive Generation for Fast and High-Fidelity Virtual Try-On

- 方向：底层视觉
- 作者：Lu Yang, Xiaonan Hu, Yanan Li, Daqi Liu, Xiang Bai, Hao Lu
- 日期：2026-07-13
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.11233v1

摘要：

Virtual try-on (VTON) is a bi-conditional image generation problem that requires not only accurate person preservation but also faithful garment deformation and detail synthesis. Diffusion-based VTON methods can jointly model these factors in a compressed latent space, but suffer from high-frequency detail loss due to inherent latent compression, even with costly multi-step denoising. Recent visual autoregressive (VAR) models offer a promising alternative for high-quality generation with faster inference, yet remai...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-07-19-low-level-vision-video-papers.md`
