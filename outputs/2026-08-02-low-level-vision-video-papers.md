---
title: 2026-08-02｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-08-02｜底层视觉与视频论文速览

生成时间：2026-08-02

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜BlindPSNR: A No-Reference Fidelity Predictor for Low-Light Image Enhancement｜2026-07-30
2. 底层视觉｜LoTA-N2N: Local Trace Adaptation for Zero-Shot Self-Supervised Image Denoising｜2026-07-27
3. 底层视觉｜Trainable Nonexpansive Denoisers for Contractive Image Reconstruction｜2026-07-25
4. 底层视觉｜A Reference-Free Framework for Evaluating Single-Frame ISP Pipelines｜2026-07-25
5. 底层视觉｜What to Remove, What to Preserve: Dual-Ambiguity Rectification for All-in-One Image Restoration｜2026-07-30
6. 底层视觉｜Space2Ground 2.0: A Multi-Source Dataset and Framework for Agricultural Monitoring through Fusion of Street-Level and Satellite Imagery｜2026-07-30
7. 底层视觉｜Collaborative Feature Aggregation for Face Super-Resolution and Robust Re-Identification｜2026-07-30
8. 底层视觉｜Temporal Concentration from Rollout Errors: Implicit Preference Optimization for Text-to-Video Diffusion｜2026-07-30
9. 视频处理｜ENCORE: Event-Assisted Complementary Motion Refinement for Learned Video Compression｜2026-07-30
10. 底层视觉｜ARD-REFSM: Enhancing Reflection Symmetry Detection with Asymmetric Denoising and Rotation Equivariance｜2026-07-30
11. 底层视觉｜CoRE-UIR: Prior-guided common and residual experts for efficient all-in-one remote sensing image restoration｜2026-07-30
12. 底层视觉｜FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference｜2026-07-30
13. 底层视觉｜Learning Color Grading, No Photo Sharing: Federated Aesthetic Preference Learning for Personalized Image Enhancement｜2026-07-30
14. 底层视觉｜SciFigQual-Bench: A Benchmark for Scientific Figure Quality Assessment with Full-Manuscript Context｜2026-07-29
15. 底层视觉｜SciFigAlign: Scoring Scientific Figures by Fine-tuned Alignment of Visuals with Manuscript Evidence｜2026-07-29
16. 底层视觉｜Anchoring and Steering Diffusion: Enhancing the Faithfulness of Text-to-Image Generation at Inference Time｜2026-07-29
17. 底层视觉｜Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation｜2026-07-29
18. 底层视觉｜SpatialQ: Understanding 3D Gaussian Splatting Scene Quality via Visual-based MLLM｜2026-07-29
19. 底层视觉｜Rethinking Clinical Relevance in Chest X-ray Machine Learning: How Evaluation References Define Performance｜2026-07-28
20. 底层视觉｜Parallel Decoding Distillation for Fast Image and Video Generation｜2026-07-28
21. 底层视觉｜TIGA: Trajectory-Injected Generative Attack against Black-box AIGC Detectors｜2026-07-28
22. 底层视觉｜Explicit Layer Modeling for Video Object Insertion and Layer Decomposition｜2026-07-28
23. 底层视觉｜Beyond Facial Consistency: Personalized Person Image Generation with Holistic Identity Preservation｜2026-07-28
24. 底层视觉｜Noise-Free One-Step LoRA for Task-Driven Image Restoration with Diffusion Priors｜2026-07-28
25. 底层视觉｜ScaleResfusion: Residual Rectified Flow based on Residual Vector Field｜2026-07-28
26. 底层视觉｜MorphUNet: Alpha-Controlled Biometric Transport for Diffusion-Based Face Morphing Attacks｜2026-07-27
27. 底层视觉｜Spatio-Temporal Conditional Denoising Transformer for Modality-Missing RGBT Tracking｜2026-07-27
28. 底层视觉｜MMOE: Modernizing Diffusion Transformers with Efficient Expert Design｜2026-07-27
29. 底层视觉｜Denoising 3D images: robustness of persistent homology measures｜2026-07-27
30. 底层视觉｜TaoMate: Anchor-Guided Memory Bridging Evolving and Reference States for Real-Time Audio-Video Digital Human Generation｜2026-07-27

## 论文摘要

### 1. BlindPSNR: A No-Reference Fidelity Predictor for Low-Light Image Enhancement

- 方向：底层视觉
- 作者：Mingzhe Lyu, Jinqiang Cui, Hong Zhang
- 日期：2026-07-30
- 分类：cs.CV
- 关键词：image enhancement、image quality assessment
- arXiv：2607.27628v1

摘要：

Low-light image enhancement (LLIE) methods involve tunable parameters that are typically fixed, often leading to performance degradation when applied across scenes. Manually selecting the best configuration, however, can be time-consuming and not always practical. Peak signal-to-noise ratio (PSNR) is the natural fidelity criterion for automating parameter selection, yet it requires a ground-truth reference that is typically unavailable. To our knowledge, no learning-based method addresses no-reference PSNR predicti...

### 2. LoTA-N2N: Local Trace Adaptation for Zero-Shot Self-Supervised Image Denoising

- 方向：底层视觉
- 作者：Jintong Hu, Bin Xia, Junlin Liu, Jiayue Liu, Wenming Yang
- 日期：2026-07-27
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2607.24135v1

摘要：

Single-image self-supervised denoising replaces unavailable clean targets with surrogate targets constructed from noisy observations. Its effectiveness therefore depends on how closely the surrogate objective remains aligned with supervised denoising, especially when noise is correlated, spatially nonstationary, or unknown. We express the discrepancy between a broad class of MSE-based self-supervised objectives and supervised MSE as a parameter-independent constant and a trace interaction between the surrogate-targ...

### 3. Trainable Nonexpansive Denoisers for Contractive Image Reconstruction

- 方向：底层视觉
- 作者：Arghya Sinha, Aditya Banerjee, Trishit Mukherjee, Kunal N. Chaudhury
- 日期：2026-07-25
- 分类：eess.IV, cs.CV
- 关键词：denoising、deblurring
- arXiv：2607.23347v1

摘要：

Trainable denoisers with Lipschitz control have become central to convergent image reconstruction. However, training neural networks that simultaneously offer strong denoising performance and global Lipschitz guarantees is challenging. Existing approaches enforce Lipschitz control only empirically, providing no guarantees beyond the training data. In this work, we show that by exploiting the action of permutations on the image lattice, we can constrain a neural architecture that is globally nonexpansive (Lipschitz...

### 4. A Reference-Free Framework for Evaluating Single-Frame ISP Pipelines

- 方向：底层视觉
- 作者：Yujin Cho, Sira Ferradans, Jean-Michel Morel, Gabriele Facciolo, Thomas Eboli
- 日期：2026-07-25
- 分类：eess.IV, cs.CV
- 关键词：denoising、image quality assessment
- arXiv：2607.23321v1

摘要：

Evaluating camera image signal processing (ISP) pipelines requires measuring low-level artifacts introduced by operations such as denoising, demosaicing, tone mapping, and compression. Blind image quality assessment (IQA) techniques can grade visual quality without a reference, but they typically focus on semantic and high-level visual cues or human perceptual scores rather than the low-level image-processing artifacts introduced by camera pipelines. In contrast, full-reference metrics such as PSNR and SSIM measure...

### 5. What to Remove, What to Preserve: Dual-Ambiguity Rectification for All-in-One Image Restoration

- 方向：底层视觉
- 作者：Cencen Liu, Wen Yin, Dongyang Zhang, Dongmin Li, Shan Zhao, Bing Su, et al.
- 日期：2026-07-30
- 分类：cs.CV, cs.AI
- 关键词：image restoration
- arXiv：2607.28526v1

摘要：

All-in-one image restoration aims to handle diverse degradations within a unified framework. Existing methods commonly encode heterogeneous degradation conditions in a shared latent space, where degradation-related cues and scene content can remain entangled. We characterize the resulting challenge as dual ambiguity: semantic ambiguity in channel-wise modulation and spatial ambiguity in restoration responses, which can lead to content corruption and residual artifacts. To mitigate this issue, we propose DAR-Net, a...

### 6. Space2Ground 2.0: A Multi-Source Dataset and Framework for Agricultural Monitoring through Fusion of Street-Level and Satellite Imagery

- 方向：底层视觉
- 作者：Iason Tsardanidis, Alkiviadis Koukos, George Choumos, Vasileios Sitokontantinou, Charalampos Kontoes
- 日期：2026-07-30
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2607.28247v1

摘要：

Accurate and scalable parcel-level agricultural monitoring remains challenging because satellite Earth Observation alone provides only an overhead perspective of agricultural parcels, while optical observations are further affected by cloud-induced temporal gaps. This paper presents Space2Ground 2.0, a multi-source framework integrating Sentinel-1 SAR and Sentinel-2 multispectral time series with geo-tagged street-level imagery acquired using vehicle-mounted cameras and shared through the Mapillary platform. A larg...

### 7. Collaborative Feature Aggregation for Face Super-Resolution and Robust Re-Identification

- 方向：底层视觉
- 作者：Juheon Hwang, Taewan Kim, Jiwoo Kang
- 日期：2026-07-30
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2607.28130v1

摘要：

We propose a novel collaborative approach for face super-resolution (SR) and robust person re-identification from sequential or multi-view facial images. Traditional SR methods often suffer from blurring and distortion in faces recovered from poor-quality images due to low resolution. Image- and video-based facial SR methods using facial landmarks or segmentation also have similar challenges. To overcome these limitations, we leverage multiple correlated facial observations, across time or viewpoints, by introducin...

### 8. Temporal Concentration from Rollout Errors: Implicit Preference Optimization for Text-to-Video Diffusion

- 方向：底层视觉
- 作者：Henglin Liu, Fangyuan Kong, Jing Wang, Yizhou Lin, Nisha Huang, Chang Liu, et al.
- 日期：2026-07-30
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.28058v1

摘要：

Recent advances in preference alignment for diffusion-based video generation, particularly via Direct Preference Optimization (DPO), have significantly improved visual quality. However, temporally sparse artifacts such as motion collapse, object flickering, and color oversaturation remain a major barrier to perceptual realism. Existing methods struggle with these issues due to two key limitations: (1) the preference attribution bottleneck, where offline human annotations are costly and fail to accurately capture le...

### 9. ENCORE: Event-Assisted Complementary Motion Refinement for Learned Video Compression

- 方向：视频处理
- 作者：Shuhan Ye, Hongbin Yu, Chenqi Kong, Pingchuan Ma, Chong Wang, Jun Wan, et al.
- 日期：2026-07-30
- 分类：cs.CV
- 关键词：video compression
- arXiv：2607.28020v1

摘要：

Learned video compression relies on accurate temporal modeling to remove redundancy between adjacent frames. However, most existing codecs infer motion solely from discretely sampled RGB frames, making their estimates vulnerable to fast motion, blur, occlusion, weak texture, low illumination, and abrupt brightness changes. Event cameras asynchronously capture fine-grained intensity changes between RGB timestamps and therefore provide complementary evidence about inter-frame dynamics. We propose ENCORE, an Event-Ass...

### 10. ARD-REFSM: Enhancing Reflection Symmetry Detection with Asymmetric Denoising and Rotation Equivariance

- 方向：底层视觉
- 作者：Dongfu Yin, Rourou Su, Cong Zhao, Fei Yu
- 日期：2026-07-30
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2607.27927v1

摘要：

Reflection symmetry detection remains challenging due to interference from asymmetric regions and arbitrary orientations of symmetric patterns. Asymmetric regions introduce background clutter that disrupts symmetric pattern matching, whereas conventional convolutional neural networks lack rotation equivariance, leading to inconsistent feature representations under rotational transformations. To address these issues, we propose an Asymmetric Region Denoising (ARD) module and a Rotation Equivariant Feature Similarity...

### 11. CoRE-UIR: Prior-guided common and residual experts for efficient all-in-one remote sensing image restoration

- 方向：底层视觉
- 作者：Zaiyan Zhang, Qiangqiang Yuan, Jie Li, Ziyang Lihe, Yu Wan, Yuzeng Chen, et al.
- 日期：2026-07-30
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2607.27898v1

摘要：

Remote sensing images acquired by unmanned aerial vehicles (UAVs) and satellites are often degraded by adverse weather, illumination variation, and imaging artifacts, which may co-occur and jointly induce global distribution shifts and local structural corruption. Although All-in-One image restoration offers an appealing unified alternative to task-specific pipelines, existing methods still suffer from weak or implicit degradation cues and parameter redundancy caused by full-rank multi-expert designs with overlappi...

### 12. FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference

- 方向：底层视觉
- 作者：Hanshuai Cui, Zhiqing Tang, Zhi Yao, Qianli Ma, Fanshuai Meng, Weijia Jia
- 日期：2026-07-30
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2607.27842v1

摘要：

Diffusion models are widely used to generate high-quality images and videos, but their iterative denoising process remains computationally intensive. A growing class of training-free accelerators reduces this cost by reusing cached intermediate features or forecasting future ones. To control draft drift, these methods sometimes compute an exact block feature for verification. Yet the resulting exact feature is typically used only to measure discrepancy or guide a later decision and is then discarded. We find that t...

### 13. Learning Color Grading, No Photo Sharing: Federated Aesthetic Preference Learning for Personalized Image Enhancement

- 方向：底层视觉
- 作者：Chuanzhi Xu, Ziyuan Tao, Jean Julien KNell, Yanrong Chen, Haolan Guo, Xuanhua Yin, et al.
- 日期：2026-07-30
- 分类：cs.CV, cs.AI, cs.DC
- 关键词：image enhancement
- arXiv：2607.27659v1

摘要：

Personalized image enhancement should reflect individual aesthetic taste, yet learning such preferences commonly depends on private photos and ratings that are unsuitable for centralized collection. The task must infer preference from sparse, heterogeneous feedback and translate it into natural-looking color transformations on resource-constrained user devices. We introduce FedPAIE, a federated personalized aesthetic image enhancement framework for user-adaptive color grading without centralizing raw photos or rati...

### 14. SciFigQual-Bench: A Benchmark for Scientific Figure Quality Assessment with Full-Manuscript Context

- 方向：底层视觉
- 作者：Zihan Deng, Chuanzhi Xu, Huiqi Liang, Haoyang Li, Xiaozhen Zhong, Lequan Yu
- 日期：2026-07-29
- 分类：cs.CV, cs.AI
- 关键词：image quality assessment
- arXiv：2607.27084v1

摘要：

Scientific images are the core elements of presenting experimental conclusions, elaborating system architecture, and supporting comparative arguments in scientific papers. However, existing image quality assessment (IQA) methods are predominantly designed for natural photographs or AI-generated content, which cannot be directly applied to scientific papers. The few existing studies on scholarly charts remain confined to visual-surface comparisons, failing to verify caption alignment, citation relevance, or visual m...

### 15. SciFigAlign: Scoring Scientific Figures by Fine-tuned Alignment of Visuals with Manuscript Evidence

- 方向：底层视觉
- 作者：Chuanzhi Xu, Zihan Deng, Huiqi Liang, Chengkun Yue, Zhanlin Cui, Pengfei Ye, et al.
- 日期：2026-07-29
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2607.27066v1

摘要：

Scientific figure assessment in peer review differs fundamentally from general image quality evaluation: a figure must be visually legible, faithfully support the manuscript's claims, and communicate evidence with a clear visual hierarchy. However, if we apply traditional image assessment methods to scientific figure quality assessment, limitations emerge: classic IQA models capture perceptual quality or aesthetics but cannot judge whether a figure serves the paper's scientific argument; CLIP-based methods assess g...

### 16. Anchoring and Steering Diffusion: Enhancing the Faithfulness of Text-to-Image Generation at Inference Time

- 方向：底层视觉
- 作者：Xinyi Wang, Yuyang Huang, Yalin Su, Pengcheng Luan, Tao Zhang, Feiming Wei, et al.
- 日期：2026-07-29
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.26647v1

摘要：

While text-to-image diffusion models achieve impressive visual quality, they frequently struggle to maintain precise alignment with complex compositional prompts. An effective strategy is to improve the inference process of diffusion models, thereby better leveraging their pretrained priors to address misalignment. Existing training-free methods can be divided into two categories. The first category focuses on improving the randomly sampled initial noise, either performing costly search over noise pools or manipula...

### 17. Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation

- 方向：底层视觉
- 作者：Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, et al.
- 日期：2026-07-29
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.26646v1

摘要：

We address the problem of reconstructing a high-fidelity, freely navigable 3D scene from a single $360^\circ$ panorama, without per-scene optimization or multi-view capture. Existing methods either lack metric trajectory control, which hinders reliable downstream 3D reconstruction, or struggle with large disocclusions under long-range camera motion while requiring high-end multi-GPU servers.We present Genie Sim PanoWorld, a two-stage feed-forward pipeline that bridges generation and reconstruction via an explicit,...

### 18. SpatialQ: Understanding 3D Gaussian Splatting Scene Quality via Visual-based MLLM

- 方向：底层视觉
- 作者：Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao
- 日期：2026-07-29
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2607.26595v1

摘要：

3D Gaussian Splatting (3DGS) has emerged as an effective representation for novel view synthesis and 3D scene reconstruction, creating an increasing demand for reliable quality assessment. Unlike conventional image quality assessment (IQA), the quality of a 3DGS scene depends not only on the perceptual fidelity of rendered views, but also on scene-level factors such as spatial structure and cross-view consistency. Existing IQA methods are limited by their reliance on 2D perceptual cues, whereas general multimodal l...

### 19. Rethinking Clinical Relevance in Chest X-ray Machine Learning: How Evaluation References Define Performance

- 方向：底层视觉
- 作者：Panagiotis Fytas, Ian Selby, Clemens Karner, Judith Babar, Simon Baker, Jake Beckford, et al.
- 日期：2026-07-28
- 分类：eess.IV, cs.CV, cs.LG
- 关键词：image quality assessment
- arXiv：2607.26333v1

摘要：

Chest X-ray (CXR) machine learning relies heavily on automated evaluation using reference standards that aim to approximate clinical judgment. However, commonly used report-derived labels for pathology classification or generic image quality metrics for reconstruction may not reliably reflect clinical judgment. We systematically investigate how evaluation-reference choices affect model performance and ranking in both pathology classification and image quality assessment (IQA). To enable controlled comparison across...

### 20. Parallel Decoding Distillation for Fast Image and Video Generation

- 方向：底层视觉
- 作者：Neta Shaul, Chao Liu, Arash Vahdat, Julius Berner
- 日期：2026-07-28
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2607.26004v1

摘要：

Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process. Current state-of-the-art (SOTA) acceleration methods heavily rely on variational score distillation (VSD) and adversarial losses to distill diffusion models into few-step generators. Albeit achieving high-quality video generation, these training losses are notoriously hard to optimize and suffer from mode collapse, leading to loss of video diversity and lack of motion. In this paper, we introduc...

### 21. TIGA: Trajectory-Injected Generative Attack against Black-box AIGC Detectors

- 方向：底层视觉
- 作者：Xia Du, Zhuosen Bao, Zheng Lin, Jizhe Zhou, Jiawei Lian, Chi-man Pun, et al.
- 日期：2026-07-28
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.25894v1

摘要：

Recent diffusion models have achieved remarkable realism in facial image synthesis, posing growing challenges to artificial intelligence-generated content (AIGC) forensic detectors.Existing evasion methods typically perturb pre-generated images or require detector-aware training, which may introduce visible or statistical artifacts and limit applicability when the diffusion model must remain frozen and the target detector is accessible only through black-box queries. We propose Trajectory-Injected Generative Attack...

### 22. Explicit Layer Modeling for Video Object Insertion and Layer Decomposition

- 方向：底层视觉
- 作者：Kyujin Han, Seungjoo Shin, Sunghyun Cho
- 日期：2026-07-28
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.25802v2

摘要：

Most video editing systems still lack explicit layered video representations, limiting their ability to perform realistic compositing, object reuse, and consistent manipulation. This limitation is especially pronounced in video object insertion and video layer decomposition, where existing methods rely on implicit inference or per-scene optimization due to the absence of explicit foreground-layer supervision. We introduce TriLayer, a large-scale triplet video dataset containing aligned composite, background, and fo...

### 23. Beyond Facial Consistency: Personalized Person Image Generation with Holistic Identity Preservation

- 方向：底层视觉
- 作者：Yuxuan Xiao, Shanshan Zhang, Jian Yang, Shengcai Liao
- 日期：2026-07-28
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.25622v1

摘要：

Personalized person image generation requires preserving subject identity across both local facial details and broader appearance cues. Existing methods typically emphasize only one level of identity information, leading to an inherent trade-off between facial fidelity and overall appearance consistency. To address this, we first propose a simple dual-branch baseline that unifies global appearance control and local facial control within a shared generation framework. This simple combination of different branches yi...

### 24. Noise-Free One-Step LoRA for Task-Driven Image Restoration with Diffusion Priors

- 方向：底层视觉
- 作者：Jaeha Kim, Kyoung Mu Lee
- 日期：2026-07-28
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2607.25390v1

摘要：

Degraded images not only reduce visual quality but also impair downstream high-level vision tasks. Task-driven image restoration (TDIR) addresses this issue by jointly optimizing restoration quality and task performance. Recent works show that pretrained diffusion priors benefit TDIR, yet diffusion-based restoration is inherently stochastic, as the sampling process depends on a random noise term, which can undermine task consistency. In this paper, we show that a deterministic, noise-free one-step forward pass with...

### 25. ScaleResfusion: Residual Rectified Flow based on Residual Vector Field

- 方向：底层视觉
- 作者：Zhenning Shi, Chen Xu, Junhao Zhang, Kefei Zhang, Linjie Liu, Zhedong Zheng, et al.
- 日期：2026-07-28
- 分类：cs.CV, cs.AI
- 关键词：image restoration
- arXiv：2607.25275v1

摘要：

Real-world Image Restoration (Real-IR) aims to recover high-quality (HQ) images from complex and unknown degradations. Although recent diffusion-based methods have substantially improved perceptual quality, their current designs leave two key challenges unresolved. Methods that start from Gaussian noise are slow and often less faithful to the degraded input. Residual-based methods usually train from scratch, which makes it hard to exploit modern pre-trained generative priors. In this paper, we present ScaleResfusio...

### 26. MorphUNet: Alpha-Controlled Biometric Transport for Diffusion-Based Face Morphing Attacks

- 方向：底层视觉
- 作者：Taimoor Rizwan, Sara Atito, Zhenhua Feng, Muhammad Awais, Josef Kittler
- 日期：2026-07-27
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.25092v1

摘要：

Face morphing attacks create synthetic images verifiable against multiple identities, threatening border control and identity verification systems. We introduce MorphUNet, a diffusion morphing framework formulating two-parent generation as alpha-controlled biometric transport: each parent is decomposed into CLIP appearance and ArcFace identity evidence, aligned into a CLIP-compatible token space, with the two contributors preserved as separate identity-aware token banks. To our knowledge, MorphUNet is the first dif...

### 27. Spatio-Temporal Conditional Denoising Transformer for Modality-Missing RGBT Tracking

- 方向：底层视觉
- 作者：Andong Lu, Ziyi Zha, Jiandong Jin, Shihao Li, Chenglong Li, Jin Tang, et al.
- 日期：2026-07-27
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.24701v1

摘要：

Missing modalities in RGBT tracking often lead to incomplete and unstable multimodal feature representations that greatly degrade the performance. Existing methods typically attempt to recover missing modalities from available ones, but the quality of data generated in challenging scenarios might be unsatisfactory. In addition, current approaches exhibit limited flexibility in processing both missing and complete data. To overcome these limitations, we propose a Spatio-temporal Conditional Denoising Transformer (SC...

### 28. MMOE: Modernizing Diffusion Transformers with Efficient Expert Design

- 方向：底层视觉
- 作者：Yanhao Jia, Jiepeng Wang, Haibin Huang, Chi Zhang, Erik Cambria, Xuelong Li
- 日期：2026-07-27
- 分类：cs.CV, cs.GR, cs.LG
- 关键词：denoising
- arXiv：2607.24665v1

摘要：

Modern large language models scale successfully by pairing capacity growth with efficiency, keeping per-token and deployment costs under control as capacity grows. AIGC Foundation Models (AFMs), especially diffusion-transformer backbones, have begun to adopt sparse experts, but recent efforts mostly enlarge total parameter counts and sparsity ratios without importing the efficiency mechanisms that made LLM scaling practical, so generation quality is seldom balanced against training and deployment cost. This raises...

### 29. Denoising 3D images: robustness of persistent homology measures

- 方向：底层视觉
- 作者：Ebru Dagdelen, Aakash Karlekar, Manav Arora, Matthew Illingsworth, Jonathan Jaquette, Linda J. Cummings, et al.
- 日期：2026-07-27
- 分类：cs.CG, cs.CV, math.AT
- 关键词：denoising
- arXiv：2607.24579v1

摘要：

When computing sub/super-level-set persistent homology (PH), the effect of noise may introduce millions of (short-lived) topological generators, presenting an obstacle to both the computation of PH of large 3D images, and any analysis of PH that incorporates the number of generators. As such, it is often necessary to denoise the data before computing its PH. We analyze the PH of synthetic 3D images of porous media in the presence of spatially uncorrelated noise, and perform a comparative analysis of various topolog...

### 30. TaoMate: Anchor-Guided Memory Bridging Evolving and Reference States for Real-Time Audio-Video Digital Human Generation

- 方向：底层视觉
- 作者：Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma, Qiu Shen
- 日期：2026-07-27
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.24359v1

摘要：

Real-time long-form digital-human generation relies on causal models to extend audio-visual content while preserving subject appearance and audio-video synchronization across successive segments. A bounded cache retains local motion and phonetic context but discards older evidence, whereas attending to the complete generated history is computationally expensive and can propagate accumulated errors. We present \method, an anchor-guided persistent-memory framework for few-step joint audio-video generation. The framew...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-08-02-low-level-vision-video-papers.md`
