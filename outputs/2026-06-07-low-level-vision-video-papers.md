---
title: 2026-06-07｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-06-07｜底层视觉与视频论文速览

生成时间：2026-06-07

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 28 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜RQUL-UIE: Revitalizing Quality-Unstable Labels for Underwater Image Enhancement via In-Dataset Self-Supervision｜2026-06-04
2. 顶会论文｜Answer Self-Consistency with Margin-Triggered Question Re-Arbitration for the CVPR 2026 VidLLMs Challenge｜2026-06-03
3. 底层视觉｜LL-Bench: Rethinking Low-Level Vision Evaluation in the Era of Large-Scale Generative Models｜2026-06-01
4. 底层视觉｜Hallucination-Aware Diffusion Sampling for Inverse Problems via Robust Prior Updates｜2026-06-01
5. 顶会论文｜Training-Free Composed Video Retrieval via Visual Representation-Guided Video-LLM Reasoning｜2026-06-01
6. 顶会论文｜PerBite: A Curated Diagnostic Workflow for Bite-Aware Food Volume Estimation｜2026-06-01
7. 底层视觉｜Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them｜2026-06-04
8. 底层视觉｜RhymeFlow: Training-Free Acceleration for Video Generation with Asynchronous Denoising Flow Scheduling｜2026-06-04
9. 底层视觉｜Geodesic Flow Matching on a Riemannian Degradation Manifold for Blind Image Restoration｜2026-06-04
10. 底层视觉｜ReCache: Learning Budget-Aware Caching Schedules for Diffusion Models via REINFORCE｜2026-06-04
11. 底层视觉｜Let It Be Simple: One-Step Action Generation for Vision-Language-Action Models｜2026-06-04
12. 底层视觉｜Noise-Aware Visual Representation Learning for Medical Visual Question Answering｜2026-06-04
13. 底层视觉｜The Invisible Hand of Physics: When Video Diffusion Models Know More Than They Show｜2026-06-03
14. 底层视觉｜MaCo-GAN: Manifold-Contrastive Adversarial Learning for Single Image Super-Resolution｜2026-06-03
15. 底层视觉｜Flash-WAM: Modality-Aware Distillation for World Action Models｜2026-06-03
16. 底层视觉｜DSA: Dynamic Step Allocation for Fast Autoregressive Video Generation｜2026-06-03
17. 视频处理｜Ultra-Fast Neural Video Compression｜2026-06-03
18. 底层视觉｜Efficient and Training-Free Single-Image Diffusion Models｜2026-06-03
19. 底层视觉｜An Attention-Based Denoising Model for Diffusion Weighted Imaging｜2026-06-02
20. 底层视觉｜Unified Video-Action Joint Denoising for Dexterous Action and Data Generation｜2026-06-02
21. 底层视觉｜GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance｜2026-06-02
22. 底层视觉｜Inverting the Generation Process of Denoising Diffusion Implicit Models: Empirical Evaluation and a Novel Method｜2026-06-02
23. 底层视觉｜MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data｜2026-06-01
24. 底层视觉｜Drifting Preference Optimization for One-Step Generative Models｜2026-06-01
25. 底层视觉｜Deep Learning for Remote Sensing to Improve Flood Inundation Mapping｜2026-06-01
26. 底层视觉｜FocusDiT: Masking Queries in Diffusion Transformers for Fine-grained Image Generation｜2026-06-01
27. 视频处理｜TIDES: Time-Derivative Event Simulation via Deformable Reconstruction｜2026-06-01
28. 底层视觉｜Distortion-Aware Fusion of Statistical and Vision-Language Features for Blind Image Quality Assessment｜2026-06-01

## 论文摘要

### 1. RQUL-UIE: Revitalizing Quality-Unstable Labels for Underwater Image Enhancement via In-Dataset Self-Supervision

- 方向：底层视觉
- 作者：Haochen Hu, Yanrui Bin, Chih-yung Wen, Bing Wang
- 日期：2026-06-04
- 分类：cs.CV
- 关键词：denoising、image enhancement
- arXiv：2606.06176v1

摘要：

Underwater Image Enhancement (UIE) is essential for mitigating degradations caused by water medium. Although learning-based methods have advanced significantly, most rely on paired datasets with unstable label quality, which bottlenecks model performance. This paper proposes a diffusion-based, in-dataset self-supervised learning strategy designed to exploit the quality distribution of training labels. Specifically, we evaluate label quality via semantic perception embeddings from a pre-trained diffusion model in a...

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

### 7. Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them

- 方向：底层视觉
- 作者：Woojung Han, Seil Kang, Youngjun Jun, Min-Hung Chen, Fu-En Yang, Seong Jae Hwang
- 日期：2026-06-04
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.06361v1

摘要：

Image-to-Video diffusion models leverage input images to generate visually stunning content, yet frequently produce motion that violates physical laws. We reveal a surprising finding: a 2-step generation often exhibits better physical consistency than a 50-step output from the same model. Through spectral analysis, we trace this to phase erosion during denoising; the phase degrades significantly (dropping by $\approx 18%$ from step 2 to step 50), whereas the magnitude remains relatively stable. Building on this ins...

### 8. RhymeFlow: Training-Free Acceleration for Video Generation with Asynchronous Denoising Flow Scheduling

- 方向：底层视觉
- 作者：Chensheng Dai, Shengjun Zhang, Yifan Li, Zhang Zhang, Zheng Zhu, Yueqi Duan
- 日期：2026-06-04
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.06309v1

摘要：

Video generation models based on Diffusion Transformers (DiTs) have achieved remarkable performance in video synthesis, yet they suffer from high inference latency and computational costs due to the quadratic complexity of 3D attention. Existing acceleration methods primarily reduce computational complexity within each individual denoising steps through techniques such as sparse attention and KV-caching. However, they rigidly adhere to the inherent constraint of the standard diffusion pipeline: every frame in the t...

### 9. Geodesic Flow Matching on a Riemannian Degradation Manifold for Blind Image Restoration

- 方向：底层视觉
- 作者：Akshay Janardan Bankar, Ankita Chatterjee, Sayan Banerjee, Shreyas Pandith, Kalakonda Sai Shashank, Amit Satish Unde
- 日期：2026-06-04
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2606.06278v1

摘要：

Blind image restoration requires recovering clean images from observations corrupted by unknown and potentially mixed degradations. While recent deterministic flow-based methods model restoration as transport processes that map degraded images to clean ones, they typically rely on Euclidean interpolation, implicitly assuming linear degradation geometry. In this paper, we explicitly model degradations as points on a low-dimensional Riemannian manifold and formulate restoration as geodesic transport on the joint imag...

### 10. ReCache: Learning Budget-Aware Caching Schedules for Diffusion Models via REINFORCE

- 方向：底层视觉
- 作者：Mishan Aliev, Eva Neudachina, Ilya Bykov, Aleksandr Oganov, Kirill Struminsky, Aibek Alanov, et al.
- 日期：2026-06-04
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.06060v1

摘要：

Modern diffusion models generate high-quality images and videos, but their iterative denoising process makes inference expensive. Feature caching accelerates sampling by reusing or predicting intermediate activations across neighboring denoising steps, exploiting the redundancy of computations along the reverse trajectory. In this work, we focus on the caching schedule: selecting which denoising steps should be fully recomputed. Existing schedules are either fixed (e.g. uniform) or chosen adaptively from per-step e...

### 11. Let It Be Simple: One-Step Action Generation for Vision-Language-Action Models

- 方向：底层视觉
- 作者：Yitong Chen, Shiduo Zhang, Jingjing Gong, Xipeng Qiu
- 日期：2026-06-04
- 分类：cs.CV, cs.AI, cs.LG, cs.RO
- 关键词：denoising
- arXiv：2606.05737v1

摘要：

Diffusion-based vision-language-action (VLA) models often inherit the image-generation view: actions are generated by iterative denoising. We argue that VLA action generation has a different condition-target structure: the policy is conditioned on rich observations, language, and state, but predicts only a compact, low-dimensional action chunk. Under this asymmetry, strong one-step action generation should not necessarily require the advanced one-step methods developed for image synthesis. We keep standard velocity...

### 12. Noise-Aware Visual Representation Learning for Medical Visual Question Answering

- 方向：底层视觉
- 作者：I Putu Adi Pratama, Bahadorreza Ofoghi, Atul Sajjanhar, Shang Gao
- 日期：2026-06-04
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2606.05535v1

摘要：

Medical visual question answering (Med-VQA) has strong potential for clinical decision support by enabling AI models to interpret medical images and answer clinically relevant queries. Recent approaches typically connect off-the-shelf vision encoders with large language models (LLMs) through lightweight mapping networks to reduce computational cost. However, these methods often overlook the importance of handling noise and small irrelevant changes in visual representations. To address these challenges, we propose a...

### 13. The Invisible Hand of Physics: When Video Diffusion Models Know More Than They Show

- 方向：底层视觉
- 作者：Parsa Esmati, Somjit Nath, Katja Hofmann, Derek Nowrouzezahrai, Samira Ebrahimi Kahou, Majid Mirmehdi
- 日期：2026-06-03
- 分类：cs.GR, cs.AI, cs.CV, cs.LG
- 关键词：denoising
- arXiv：2606.05328v1

摘要：

Modern video diffusion models generate increasingly realistic and temporally coherent videos, motivating their use as candidate world simulators. Yet it remains unclear whether these models internally encode physical structure, or merely reproduce motion patterns seen during training. We study this question by probing video diffusion models along latent trajectories corresponding to real videos with known physical plausibility. To obtain such trajectories, we approximately invert the deterministic sampling process...

### 14. MaCo-GAN: Manifold-Contrastive Adversarial Learning for Single Image Super-Resolution

- 方向：底层视觉
- 作者：Daeyoung Han, Seongmin Hwang, Moongu Jeon
- 日期：2026-06-03
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2606.05068v1

摘要：

Conventional Generative Adversarial Networks (GANs) for Single Image Super-Resolution (SISR) often struggle with hallucinated artifacts, largely because standard discriminators evaluate overall image naturalness rather than strict conditional realism. To address this, we propose MaCo-GAN, a novel manifold-contrastive GAN framework that replaces the conventional adversarial loss with a supervised contrastive objective. A core component of our method is a dynamic fake sample synthesizer that transforms ground truth (...

### 15. Flash-WAM: Modality-Aware Distillation for World Action Models

- 方向：底层视觉
- 作者：Arman Akbari, Ci Zhang, Arash Akbari, Lin Zhao, Yixiao Chen, Weiwei Chen, et al.
- 日期：2026-06-03
- 分类：cs.LG, cs.CV, cs.RO
- 关键词：denoising
- arXiv：2606.05254v1

摘要：

World-action models (WAMs) jointly generate future video and robot actions through iterative diffusion, achieving strong performance on manipulation benchmarks but requiring tens of denoising steps, a cost that precludes real-time control. Step distillation has emerged as the natural remedy, but off-the-shelf methods break down in the joint video-action setting because video and action streams use different SNR-shifted noise schedules and reach training with substantially different marginal noise distributions, an...

### 16. DSA: Dynamic Step Allocation for Fast Autoregressive Video Generation

- 方向：底层视觉
- 作者：Thanh-Tung Le, Yunhan Zhao, Menglei Chai, Zhengyang Shen, Zhe Cao, Danhang Tang, et al.
- 日期：2026-06-03
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.04432v1

摘要：

Video diffusion transformers have achieved state-of-the-art visual quality, but their high inference cost remains a major bottleneck for real-time applications. Recent distillation frameworks produce autoregressive video diffusion models with reduced latency, yet these models still use a fixed number of denoising steps per frame, wasting computation on predictable frames and under-refining challenging ones. We present DSA, a confidence-guided adaptive computation framework for AR video diffusion. DSA introduces a l...

### 17. Ultra-Fast Neural Video Compression

- 方向：视频处理
- 作者：Jiahao Li, Wenxuan Xie, Zhaoyang Jia, Bin Li, Zongyu Guo, Xiaoyi Zhang, et al.
- 日期：2026-06-03
- 分类：cs.CV
- 关键词：video compression
- arXiv：2606.04410v1

摘要：

While neural video codecs (NVCs) have demonstrated superior compression ratio, their prohibitive computational complexity remains a critical barrier to real-world deployment. This paper introduces a chunk-based coding framework designed to significantly improve the rate-distortion-complexity trade-off. Instead of processing frames sequentially, our approach encodes a chunk of multiple frames into a single compact latent representation and decodes them simultaneously. This is enabled by cross-frame interaction modul...

### 18. Efficient and Training-Free Single-Image Diffusion Models

- 方向：底层视觉
- 作者：Haojun Qiu, Kiriakos N. Kutulakos, David B. Lindell
- 日期：2026-06-03
- 分类：cs.CV, cs.LG
- 关键词：image restoration
- arXiv：2606.04299v1

摘要：

We consider the problem of generating images whose internal structure -- defined by the distribution of patches across multiple scales -- matches that of a single reference image. Recent approaches address this problem by training a diffusion model on a single image. But even in this setting, training is computationally expensive and requires hours of optimization. Instead, we model the image using a dataset of its patches at different scales. As this dataset is finite and the dimensionality of its patches is small...

### 19. An Attention-Based Denoising Model for Diffusion Weighted Imaging

- 方向：底层视觉
- 作者：Prithviraj Verma, Pawan Kumar, Chandan Deshani, Prasun Chandra Tripathi
- 日期：2026-06-02
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.03903v1

摘要：

Diffusion-weighted imaging (DWI) is used for whole-body cancer screening, but it typically requires a long acquisition time. When the scan time is reduced, the image quality often suffers, leading to increased noise in the scans. Magnitude reconstruction in DWI introduces signal-dependent Rician noise, which makes denoising more challenging for conventional convolution-based methods. To address this limitation, we propose a noise-aware attention-driven denoising framework that integrates hierarchical Swin Transform...

### 20. Unified Video-Action Joint Denoising for Dexterous Action and Data Generation

- 方向：底层视觉
- 作者：Dingrui Wang, YuAn Wang, Jinkun Liu, Yue Zhang, Mattia Piccinini, Yu Sun, et al.
- 日期：2026-06-02
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.03868v1

摘要：

Recent world action models leverage video foundation models by aligning broad visual-dynamics priors with executable robot actions. We revisit this alignment from a distributional perspective. Existing formulations typically narrow the aligned prior into an observation-conditioned policy distribution over future actions. In contrast, we keep the distribution broader by modeling the joint space of interaction videos and executable hand trajectories under multiple conditioning regimes. We propose Donk, a unified vide...

### 21. GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance

- 方向：底层视觉
- 作者：Zehua Chen, Yucheng Yang, Binjie Yuan, Kaiwen Zheng, Jun S. Liu, Jun Zhu
- 日期：2026-06-02
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- arXiv：2606.03119v1

摘要：

Guidance methods, such as classifier-free guidance (CFG) and auto-guidance (AG), have advanced noise-to-data generation in diffusion models. Recently, bridge models have introduced a data-to-data generative process that can exploit an instructive clean prior. In this work, inspired by previous methods creating quality difference between denoising results as guidance, we propose a training-free bridge guidance method, termed Prior Guidance (PG). Specifically, we introduce a weak prior, which is unseen during bridge...

### 22. Inverting the Generation Process of Denoising Diffusion Implicit Models: Empirical Evaluation and a Novel Method

- 方向：底层视觉
- 作者：Yan Zeng, Masanori Suganuma, Takayuki Okatani
- 日期：2026-06-02
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.03111v1

摘要：

This paper studies the problem of inverting the DDIM image generation process to recover latent variables, particularly the initial noise map, from a generated image. Existing methods often struggle with accuracy in this task. We propose a novel hybrid approach that combines direct inversion via gradient descent for the first step, followed by a fixed-point method for subsequent steps. Empirical evaluations across three datasets demonstrate that our method significantly improves the prediction of initial latent var...

### 23. MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data

- 方向：底层视觉
- 作者：Teng Hu, Mingchun Lu, Yating Wang, Jiangning Zhang, Jinkun Hao, Ye Pan, et al.
- 日期：2026-06-01
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2606.02753v1

摘要：

Video world models are a foundational generative technology for embodied AI and the Metaverse, yet existing approaches are inherently limited to a single agent observing from a single perspective. Extending these models to multi-agent settings introduces two critical challenges: data scarcity (coordinated multi-view recordings are prohibitively expensive to collect for general open-domain scenarios) and world state alignment (independently generated video streams cannot ensure that shared physical environments and...

### 24. Drifting Preference Optimization for One-Step Generative Models

- 方向：底层视觉
- 作者：Zhou Jiang, Yandong Wen, Zhen Liu
- 日期：2026-06-01
- 分类：cs.LG, cs.CV
- 关键词：denoising
- arXiv：2606.02521v3

摘要：

One-step text-to-image generators are attractive for deployment because they generate an image with a single forward pass, but preference finetuning them remains difficult: standard alignment methods often rely on policy likelihoods, denoising trajectories, differentiable reward gradients, or test-time optimization. We propose Drifting Preference Optimization (DrPO), an online preference-finetuning method for deterministic one-step generators. For each prompt, DrPO samples candidates from the current generator, ran...

### 25. Deep Learning for Remote Sensing to Improve Flood Inundation Mapping

- 方向：底层视觉
- 作者：Yogesh Bhattarai, Vijay Chaudhary, Wai Lim Kim, Sanjib Sharma
- 日期：2026-06-01
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2606.02310v1

摘要：

Flooding is the most pervasive natural disaster worldwide. Timely and accurate flood inundation mapping are essential for informing disaster risk management. Optical satellite missions provide high-resolution, multispectral observations critical for flood detection and inundation mapping. However, their operational utility is severely constrained by cloud cover during extreme precipitation events. Conventional cloud-removal techniques based on temporal compositing or interpolation often fail to capture inundation d...

### 26. FocusDiT: Masking Queries in Diffusion Transformers for Fine-grained Image Generation

- 方向：底层视觉
- 作者：Xueji Fang, Liyuan Ma, Jianhao Zeng, Jinjin Cao, Mingyuan Zhou, Guo-Jun Qi
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：denoising
- arXiv：2606.02090v2

摘要：

Diffusion transformer (DiT) has been widely adopted in the generative diffusion field, advancing the denoising of query tokens through attention and Feed-Forward (\text{FFN}) layers. FFN actually acts as the key-value vocabulary for decoding visual contents where the value embeds the visual semantical knowledge. We present that focusing on critical query tokens corresponding to more complex details and encouraging the model to improve these tokens is essential for fine-grained visual generation. To this end, we pro...

### 27. TIDES: Time-Derivative Event Simulation via Deformable Reconstruction

- 方向：视频处理
- 作者：Christopher Thirgood, Dipon Kumar Ghosh, Simon Hadfield
- 日期：2026-06-01
- 分类：cs.CV, cs.RO
- 关键词：frame interpolation
- arXiv：2606.02058v1

摘要：

Event cameras emit asynchronous events in response to environmental appearance changes. The scarcity of real-world event datasets makes simulation essential. However, most simulators infer event timestamps from frame sequences, forcing many threshold crossings to share a small set of discrete times; a failure mode we term timestamp batching that worsens under fast motion and occlusion. We present TIDES, a continuous-time event simulator built on dynamic Gaussian splatting. Because TIDES operates on an explicit 3D s...

### 28. Distortion-Aware Fusion of Statistical and Vision-Language Features for Blind Image Quality Assessment

- 方向：底层视觉
- 作者：Bishr Omer Abdelrahman Adam, Xu Li
- 日期：2026-06-01
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2606.02002v1

摘要：

Blind image quality assessment (BIQA) aims to predict perceived image quality without access to a reference image. Classical natural scene statistics (NSS) descriptors and modern vision-language model (VLM) embeddings address this problem from fundamentally different perspectives, yet whether combining them yields complementary benefits and how to weight their contributions per input image remains unexplored. We propose a distortion-aware fusion framework that integrates a 138-dimensional NSS descriptor with two co...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-06-07-low-level-vision-video-papers.md`
