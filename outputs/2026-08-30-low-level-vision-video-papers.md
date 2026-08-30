---
title: 2026-08-30｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-08-30｜底层视觉与视频论文速览

生成时间：2026-08-30

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Targeted Iterative Filtering｜2026-08-23
2. 底层视觉、视频处理｜Zero-Shot Video Restoration and Enhancement with Text-to-Image Latent Diffusion Models and Multi-Modal References｜2026-08-27
3. 底层视觉｜Uncertainty-Guided Latent Diffusion Models for Faithful Super Resolution｜2026-08-26
4. 底层视觉｜Learning spatially varying regularisation parameters of low regularity for image reconstruction｜2026-08-25
5. 顶会论文｜Results of the 1st Asynchronous CASTLE Challenge at the Joint Egocentric Vision Workshop in Conjunction with CVPR 2026｜2026-08-24
6. 视频处理｜Following Motion for Sequential Modeling in Video Frame Interpolation｜2026-08-24
7. 底层视觉｜On the Choice of Tensor Estimation for Corner Detection, Optical Flow and Denoising｜2026-08-23
8. 底层视觉｜On Tensor-Based PDEs and their Corresponding Variational Formulations with Application to Color Image Denoising｜2026-08-23
9. 底层视觉｜GAN-Diff : Coupling Pretrained WGAN-GP Features with Conditional Diffusion U-Nets｜2026-08-23
10. 底层视觉｜Multi-Person Human Motion Forecasting in Complex Scenes｜2026-08-27
11. 底层视觉｜Rethinking Image Processing for the Age of AI: A Problem-First Framework for Scientific Progress｜2026-08-27
12. 底层视觉｜Real-time Unsupervised Object Discovery from Asynchronous Event Streams｜2026-08-27
13. 底层视觉｜Learning Late, Guiding Early: Timestep-Decoupled Semantic Guidance for Fair Face Generation｜2026-08-26
14. 底层视觉｜Precipitation Downscaling Using Foundation Model-Conditioned Diffusion｜2026-08-26
15. 底层视觉｜Unsupervised Anatomical Feature Learning via Diffusion Models: Enhanced Medical Image Segmentation with Denoising Diffusion Probabilistic Models｜2026-08-26
16. 底层视觉｜CrossMambaTuning: Synergistic Spatial and Cross-Layer Adaptation for Machine Vision Compression｜2026-08-26
17. 底层视觉｜4DStreamCtrl: Interactive Video Generation with Online 4D Control｜2026-08-26
18. 底层视觉｜Token-Oriented Semantic Communication with Pretrained Vision Transformers｜2026-08-26
19. 底层视觉｜GraftSR: Grafting Authentic Textures for Real-World Image Super-Resolution via Identical-Instance Guidance｜2026-08-26
20. 底层视觉｜Score-Based Ideal Observer Approximation via Denoising Score Matching for Signal-Known-Exactly Detection Tasks｜2026-08-25
21. 底层视觉｜Deep Learning Super Resolution for Satellite Cloud Mask Downscaling｜2026-08-25
22. 底层视觉｜On-Policy Self-Distillation in Diffusion Models｜2026-08-25
23. 底层视觉｜Bridging Adversarial and Collaborative Learning for AI-Generated Image Quality Assessment｜2026-08-25
24. 底层视觉｜Event-Based Motion Estimation via Oriented Distance Fields｜2026-08-25
25. 底层视觉｜DRRG: A Discrete Diffusion Framework for Radiology Report Generation｜2026-08-25
26. 底层视觉｜AffineTok: Semantic Affine Consistency for Diffusion-Friendly Visual Tokenizer｜2026-08-24
27. 底层视觉｜Restoring Without Forgetting: Continual Learning Across Image Degradations｜2026-08-24
28. 底层视觉｜Scaling Reinforcement Learning for Diffusion Models via Velocity Matching｜2026-08-24
29. 底层视觉｜Controllable blind deblurring with diffusion models｜2026-08-24
30. 底层视觉｜Bridge Damage Detection from Low-Light UAV Imagery via Degradation-Aware Mixture-of-Experts Enhancement｜2026-08-24

## 论文摘要

### 1. Targeted Iterative Filtering

- 方向：底层视觉
- 作者：Freddie Åström, Michael Felsberg, George Baravdish, Claes Lundström
- 日期：2026-08-23
- 分类：cs.CV
- 关键词：image denoising、denoising、image compression
- arXiv：2608.22299v1

摘要：

The assessment of image denoising results depends on the respective application area, i.e. image compression, still-image acquisition, and medical images require entirely different behavior of the applied denoising method. In this paper we propose a novel, nonlinear diffusion scheme that is derived from a linear diffusion process in a value space determined by the application. We show that application-driven linear diffusion in the transformed space compares favorably with existing nonlinear diffusion techniques.

### 2. Zero-Shot Video Restoration and Enhancement with Text-to-Image Latent Diffusion Models and Multi-Modal References

- 方向：底层视觉、视频处理
- 作者：Cong Cao, Huanjing Yue, Xin Liu, Jingyu Yang
- 日期：2026-08-27
- 分类：cs.CV
- 关键词：image restoration、video restoration
- arXiv：2608.26476v1

摘要：

Zero-shot image restoration methods with text-to-image latent diffusion models have achieved great success in universal image restoration tasks without training. However, applying them to video restoration will result in severe temporal flickering. In this paper, we propose a novel framework for zero-shot video restoration and enhancement which uses a text-to-image latent diffusion model and multi-modal references. Through the proposed dual prompt tuning inversion and sampling, the inference time can be reduced to...

### 3. Uncertainty-Guided Latent Diffusion Models for Faithful Super Resolution

- 方向：底层视觉
- 作者：Ren Wang, Yung-Yu Chuang
- 日期：2026-08-26
- 分类：cs.CV
- 关键词：image super-resolution、super resolution
- arXiv：2608.25998v1

摘要：

The perception-distortion trade-off poses a fundamental challenge in single-image super-resolution (SR). Although diffusion-based SR methods excel at generating perceptually realistic images, achieving high fidelity remains a key limitation. Recent advances in diffusion-based SR have shown promise in improving fidelity, but these methods often compromise perceptual quality due to their high reliance on a high-fidelity image. To address this, we introduce UGDiff, a novel diffusion guidance paradigm designed to furth...

### 4. Learning spatially varying regularisation parameters of low regularity for image reconstruction

- 方向：底层视觉
- 作者：Kostas Papafitsoros, Luca Calatroni, Andreas Kofler
- 日期：2026-08-25
- 分类：eess.IV, cs.CV, math.OC
- 关键词：image denoising、denoising
- arXiv：2608.25127v1

摘要：

In this chapter, we review and discuss the regularity properties of spatially adaptive regularisation weight functions used in variational image reconstruction. Incorporating such weights into classical model-based regularisers, such as Total Variation (TV) and Total Generalised Variation (TGV), allows the regularisation strength to vary across the image and adapt to local image content. When appropriately estimated, these weights can thus significantly improve edge and detail preservation in the reconstructions. W...

### 5. Results of the 1st Asynchronous CASTLE Challenge at the Joint Egocentric Vision Workshop in Conjunction with CVPR 2026

- 方向：顶会论文
- 作者：Luca Rossetto, Werner Bailer, Cathal Gurrin, Graham Healy, Omar Shahbaz Khan, Stevan Rudinac, et al.
- 日期：2026-08-24
- 分类：cs.CV, cs.MM
- 关键词：CVPR 2026、CVPR
- arXiv：2608.22914v1

摘要：

This report summarizes the contributions and results of the 1st Asynchronous CASTLE Challenge at the Joint Egocentric Vision Workshop in conjunction with CVPR 2026.

### 6. Following Motion for Sequential Modeling in Video Frame Interpolation

- 方向：视频处理
- 作者：Jaehyun Park, Nam Ik Cho
- 日期：2026-08-24
- 分类：cs.CV
- 关键词：video interpolation、frame interpolation
- arXiv：2608.22861v1

摘要：

State Space Models (SSMs) have surfaced as a promising architecture in Video Frame Interpolation (VFI), as they can capture long-range dependencies with linear computational complexity. However, their predefined scanning order limits their effectiveness in modeling the dynamic motion trajectories inherent in VFI problems. To tackle this challenge, we propose Motion-Guided Mamba for Video Frame Interpolation (MGMVFI), an adaptation of the selective state space model tailored explicitly for VFI. MGMVFI introduces Mot...

### 7. On the Choice of Tensor Estimation for Corner Detection, Optical Flow and Denoising

- 方向：底层视觉
- 作者：Freddie Åström, Michael Felsberg
- 日期：2026-08-23
- 分类：cs.CV
- 关键词：denoising、image enhancement
- arXiv：2608.22314v1

摘要：

Many image processing methods such as corner detection, optical flow and iterative enhancement make use of image tensors. Generally, these tensors are estimated using the structure tensor. In this work we show that the gradient energy tensor can be used as an alternative to the structure tensor in several cases. We apply the gradient energy tensor to common image problem applications such as corner detection, optical flow and image enhancement. Our experimental results suggest that the gradient energy tensor enable...

### 8. On Tensor-Based PDEs and their Corresponding Variational Formulations with Application to Color Image Denoising

- 方向：底层视觉
- 作者：Freddie Åström, George Baravdish, Michael Felsberg
- 日期：2026-08-23
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2608.22302v1

摘要：

The case when a partial differential equation (PDE) can be considered as an Euler-Lagrange (E-L) equation of an energy functional, consisting of a data term and a smoothness term is investigated. We show the necessary conditions for a PDE to be the E-L equation for a corresponding functional. This energy functional is applied to a color image denoising problem and it is shown that the method compares favorably to current state-of-the-art color image denoising techniques.

### 9. GAN-Diff : Coupling Pretrained WGAN-GP Features with Conditional Diffusion U-Nets

- 方向：底层视觉
- 作者：Saif Ahmed, Ashadulla Hil Galib, S. M. Riaz Rahman Antu, Ahmed Faizul Haque Dhrubo, Souvik Pramanik, Mohammad Abdul Qayum, et al.
- 日期：2026-08-23
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：image restoration、denoising
- arXiv：2608.22272v1

摘要：

Generative adversarial networks (GANs) can provide efficient image generation, while diffusion models offer high-quality image restoration but require iterative sampling. This paper presents a hybrid GAN-guided diffusion framework that uses a pretrained Wasserstein GAN with gradient penalty (WGAN-GP) as a feature prior for conditional diffusion-based image restoration. Intermediate features from the frozen WGAN-GP generator are incorporated into a diffusion U-Net through cross-attention and remain fixed during the...

### 10. Multi-Person Human Motion Forecasting in Complex Scenes

- 方向：底层视觉
- 作者：Serdar Ozsoy, Lars Doorenbos, Juergen Gall
- 日期：2026-08-27
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2608.27039v1

摘要：

Accurately forecasting the movement of people in complex scenes requires reasoning over the past and present state of the entire environment. In this context, effectively incorporating object information and social interactions into a unified framework remains particularly challenging. To address this, we propose Object-Conditioned Social Diffusion (OCSD), a conditional diffusion model that integrates motion history, multi-person interactions, and object cues into a single framework. OCSD uses an object-conditionin...

### 11. Rethinking Image Processing for the Age of AI: A Problem-First Framework for Scientific Progress

- 方向：底层视觉
- 作者：Guoping Qiu
- 日期：2026-08-27
- 分类：cs.CV
- 关键词：low-light enhancement
- arXiv：2608.26833v1

摘要：

Modern AI has greatly expanded the capabilities of image processing. However, the ready availability of powerful models, public datasets, and benchmark leaderboards has also en- couraged a model-first research pattern: researchers increasingly begin with an available architecture and optimize it on a public benchmark, rather than beginning with the underlying real-world imaging problem. This can produce impressive benchmark results without necessarily improving our understanding or solution of the real problem. Thi...

### 12. Real-time Unsupervised Object Discovery from Asynchronous Event Streams

- 方向：底层视觉
- 作者：Pratham G. Shenwai, Hemant Kumar Singh, Sridhar Ravi
- 日期：2026-08-27
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.26644v1

摘要：

Event cameras capture pixel-level intensity changes with microsecond resolution to produce highly sparse asynchronous data streams. For visual perception in latency-critical environments, we propose a lightweight, training-free framework for discovery of moving objects based on spatio-temporal clustering. This framework is driven by two core contributions. First, a linear-time Spatio-temporal Probabilistic Event Filter (SPEF) that introduces an adaptive event acceptance threshold to distinguish salient motion struc...

### 13. Learning Late, Guiding Early: Timestep-Decoupled Semantic Guidance for Fair Face Generation

- 方向：底层视觉
- 作者：Subir Kumar Parida, Rajbabu Velmurugan, Ketan Kotwal, R. S. Sengar, Swati Hiremath
- 日期：2026-08-26
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.25862v2

摘要：

Demographic imbalance in synthetic face generation can propagate to downstream face recognition systems, making fairness an important consideration when diffusion models are used for data generation. Existing fairness-aware generation approaches often require model retraining, architectural modifications, or repeated guidance throughout the reverse diffusion process. In this work, we introduce Semantic Boundary Predictor (SBP), an inference-time framework that performs demographic guidance through a one-shot interv...

### 14. Precipitation Downscaling Using Foundation Model-Conditioned Diffusion

- 方向：底层视觉
- 作者：Victor Nascimento Ribeiro, Jorge Guevara, Jorge Sebastian Moraga, Chris Lucas, Natalie Lord, Andrew Taylor, et al.
- 日期：2026-08-26
- 分类：cs.CV, cs.LG, physics.ao-ph
- 关键词：denoising
- arXiv：2608.25858v1

摘要：

High-resolution precipitation fields are essential for hydrological impact assessment, yet global climate model outputs are too coarse and biased for direct use. AI-based statistical downscaling with diffusion models offers a promising approach, but the mechanism by which large-scale atmospheric predictors condition generation remains largely unexplored. We investigate three conditioning strategies for a denoising diffusion probabilistic model applied to daily precipitation downscaling: channel concatenation of ups...

### 15. Unsupervised Anatomical Feature Learning via Diffusion Models: Enhanced Medical Image Segmentation with Denoising Diffusion Probabilistic Models

- 方向：底层视觉
- 作者：Akshat G, Divyansh Gupta, Shaleen Bhatnagar, Shilpa Ankalaki, Tusar Kanti Mishra
- 日期：2026-08-26
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- arXiv：2608.25693v1

摘要：

Acquiring pixel-level annotations for medical image segmentation is a severe bottleneck. Traditional U-Net architectures, while effective, learn local texture patterns and lack awareness of global anatomical structures, leading to boundary delineation failures in low-data regimes. This research paper proposes utilizing unsupervised Denoising Diffusion Probabilistic Models (DDPMs) to extract anatomical features. We train a DDPM on 21 unlabeled abdominal CT scans to learn structural representations, transferring the...

### 16. CrossMambaTuning: Synergistic Spatial and Cross-Layer Adaptation for Machine Vision Compression

- 方向：底层视觉
- 作者：Haobo Xiong, Shaobo Liu, Kai Liu, Chongyang Ding
- 日期：2026-08-26
- 分类：cs.CV, cs.AI
- 关键词：image compression
- arXiv：2608.25568v1

摘要：

To reduce deployment cost and retraining overhead, adapting pretrained learned image compression (LIC) models to downstream machine vision tasks has attracted growing attention. However, existing methods typically insert fine-tuning modules independently into frozen backbones, lacking explicit mechanisms for cross-layer coordination. To address this limitation, we propose a novel framework named CrossMambaTuning, which integrates State Space Models with cross-layer interaction mechanisms for parameter-efficient fin...

### 17. 4DStreamCtrl: Interactive Video Generation with Online 4D Control

- 方向：底层视觉
- 作者：Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, et al.
- 日期：2026-08-26
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2608.25479v2

摘要：

Generative video models now synthesize footage nearly indistinguishable from reality. Their promise as interactive tools hinges on fine-grained control of how objects and the camera move over time, yet each existing approach captures only part of this: camera-parameter methods steer the viewpoint but cannot move objects, 2D-trajectory methods act in the image plane and ignore depth and occlusion, and recent 3D methods add geometry but run only offline at a fixed length. In particular, none combines 3D-consistent co...

### 18. Token-Oriented Semantic Communication with Pretrained Vision Transformers

- 方向：底层视觉
- 作者：Jiwoong Im, Minwoo Kim, Jaeho Lee, Yo-Seb Jeon, Yongjune Kim
- 日期：2026-08-26
- 分类：eess.SP, cs.AI, cs.CV, cs.LG
- 关键词：image compression
- arXiv：2608.25410v1

摘要：

Token communications realize the semantic communication principle at the granularity of transformer tokens, providing a promising direction for client--server collaborative inference in resource-constrained edge systems. However, directly transmitting token embeddings presents two practical challenges: substantial communication cost and limited interoperability across model-specific token embedding spaces. To address these challenges, we propose a \emph{token-oriented} semantic communication framework. In this fram...

### 19. GraftSR: Grafting Authentic Textures for Real-World Image Super-Resolution via Identical-Instance Guidance

- 方向：底层视觉
- 作者：Qifan Yu, Haoran Bai, Zongyao He, Weijie He, Sibin Deng, Honggang Qi, et al.
- 日期：2026-08-26
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2608.25334v1

摘要：

Diffusion-based real-world image super-resolution (SR) achieves impressive perceptual quality but inherently suffers from severe texture hallucination. To overcome this limitation, we propose GraftSR, a texture-reference-guided generative SR framework that leverages reference images of the identical instance to anchor the restoration of authentic textures. However, severe spatial misalignment between low-quality inputs and their references poses significant challenges, often leading to ambiguous transfer targets an...

### 20. Score-Based Ideal Observer Approximation via Denoising Score Matching for Signal-Known-Exactly Detection Tasks

- 方向：底层视觉
- 作者：Weimin Zhou
- 日期：2026-08-25
- 分类：eess.IV, cs.AI, cs.CV, cs.LG, stat.CO
- 关键词：denoising
- arXiv：2608.24768v1

摘要：

The Bayesian Ideal Observer (IO) establishes the theoretical upper bound on task performance for binary detection tasks. However, analytical computation of the IO test statistic is generally intractable. Numerical approaches based on Markov-chain Monte Carlo (MCMC) methods, including their recent deep generative model-based extensions, typically require extensive posterior sampling for each test image. Supervised learning has also been investigated to approximate the IO performance. However, such methods are typica...

### 21. Deep Learning Super Resolution for Satellite Cloud Mask Downscaling

- 方向：底层视觉
- 作者：Angelos Georgakis, Valentina Kanaki, Giorgos Giannopoulos, Stella Girtsou, Ioannis Kontogiorgakis, Charalampos Kontoes, et al.
- 日期：2026-08-25
- 分类：cs.CV, cs.AI
- 关键词：super resolution
- arXiv：2608.24715v1

摘要：

A vast amount of optical satellite data is being transmitted to Earth-based servers every day, and more than half of this data is affected by haze or clouds. Additionally, this data suffers from the fundamental trade-off between spatial and temporal resolution, which remains largely unresolved, making the acquisition of continuous high-resolution satellite observations of clouds an ongoing challenge. This work addresses this challenge by proposing two Deep Learning super-resolution methods for the accurate downscal...

### 22. On-Policy Self-Distillation in Diffusion Models

- 方向：底层视觉
- 作者：Wei Zhou, Xiongwei Zhu, Lingdong Kong, Bo Chen, Lei Zhang, Yongyuan Liang, et al.
- 日期：2026-08-25
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.24646v1

摘要：

Reinforcement learning can align diffusion models with human preferences and task-specific objectives, but endpoint rewards do not specify how an intermediate denoising prediction should change. We introduce DiffusionOPSD as an on-policy self-distillation framework that converts image-level reward guidance into explicit targets for clean-output predictions at sampled queries. At each outer iteration, a frozen behavior policy generates trajectories and supplies query states and anchors. Reward gradients construct bo...

### 23. Bridging Adversarial and Collaborative Learning for AI-Generated Image Quality Assessment

- 方向：底层视觉
- 作者：Baoliang Chen, Qing Lin, Sijie Mai
- 日期：2026-08-25
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2608.24372v1

摘要：

AI-generated image quality assessment (AIGIQA) requires jointly reasoning about perceptual fidelity and prompt alignment, two quality dimensions that are often treated as independent in existing AIGIQA models. However, by re-examining human ratings, we uncover a previously overlooked phenomenon: the two dimensions are interdependent and exhibit both competitive and cooperative interactions during human rating. This observation suggests that a unified model should neither collapse the two dimensions nor rigidly sepa...

### 24. Event-Based Motion Estimation via Oriented Distance Fields

- 方向：底层视觉
- 作者：Lei Sun, Yuqin Ma, Weilun Li, Haoran Liang, Runyi Yang, Kaiwei Wang, et al.
- 日期：2026-08-25
- 分类：cs.CV, cs.RO
- 关键词：deblurring
- arXiv：2608.24223v1

摘要：

Event-based motion estimation is central to tasks that demand high temporal resolution and robustness to fast motion. Existing methods typically rely on iterative optimization or repeated hypothesis comparison, offsetting the sensor's low-latency advantage. We propose Oriented Distance Field Motion Estimation (ODF Motion Estimation), which replaces this optimization with a single averaging step over a precomputed field of event distance vectors, combined with an adaptive event-count selection strategy and a paramet...

### 25. DRRG: A Discrete Diffusion Framework for Radiology Report Generation

- 方向：底层视觉
- 作者：Shaoyang Zhoua, Yingshu Li, Yunyi Liu, Lijun Pu, Lingqiao Liu, Lei Wang, et al.
- 日期：2026-08-25
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.24105v1

摘要：

Purpose: Automatic radiology report generation (RRG) has been widely explored to improve reporting accuracy and reduce radiologists' workload. Most existing methods rely on autoregressive (AR) frameworks that generate reports token by token and cannot revise earlier content, making them prone to error propagation and inconsistent with the iterative refinement process of radiological reporting. In contrast, discrete diffusion large language models (DLLMs) generate text through iterative denoising, naturally enabling...

### 26. AffineTok: Semantic Affine Consistency for Diffusion-Friendly Visual Tokenizer

- 方向：底层视觉
- 作者：Junqiu Yu, Pandeng Li, Yikai Wang, Jiaxing Zhao, Yujie Wei, Kaixun Jiang, et al.
- 日期：2026-08-24
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.23864v1

摘要：

Visual tokenizers increasingly inject semantic supervision into latent spaces to make downstream diffusion easier. Yet how these semantics should be organized to facilitate denoising remains underexplored. In this paper, we define the semantic recovery objective: the denoising process should recover the semantic content of the clean image from noisy latent, and a good tokenizer should make it easier. Existing approaches train a projector to predict the semantics directly from the noisy latent. We argue that this pr...

### 27. Restoring Without Forgetting: Continual Learning Across Image Degradations

- 方向：底层视觉
- 作者：Alif Ashrafee, Bartosz Krawczyk
- 日期：2026-08-24
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：image restoration
- arXiv：2608.23799v1

摘要：

Recent progress in image restoration has converged on all-in-one architectures that jointly handle multiple degradations within a single network. These methods are effective on static benchmarks but target a closed-world setting that assumes simultaneous access to every target degradation at training time. In practice, degradations are encountered sequentially as field-deployed systems progressively face new environmental conditions, and historical training data is often unavailable due to privacy or storage constr...

### 28. Scaling Reinforcement Learning for Diffusion Models via Velocity Matching

- 方向：底层视觉
- 作者：Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, et al.
- 日期：2026-08-24
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2608.23664v1

摘要：

Reward fine-tuning is becoming an important tool for adapting diffusion models to human preferences and task-specific objectives, but existing methods largely inherit policy-gradient machinery from large language models. Unlike autoregressive models, diffusion models do not provide tractable likelihoods for generated samples. As a result, current approaches either construct trajectory likelihoods from stochastic denoising transitions or approximate endpoint likelihoods with evidence lower bound, introducing additio...

### 29. Controllable blind deblurring with diffusion models

- 方向：底层视觉
- 作者：Imane Si Salah, Emile Cribelier, Thomas Veit, Wolf Hauser, Arthur Leclaire
- 日期：2026-08-24
- 分类：cs.CV
- 关键词：deblurring
- arXiv：2608.23343v2

摘要：

Image acquisition with a camera involves several degradations due to the optical system, sensor, or low-level processing steps. We address blind deblurring in professional photography: we aim to invert unknown isotropic blur without knowledge of the degradation kernel. For such inverse problems,where some high-frequency information is lost, it is challenging to use generative models to produce details that are both photo-realistic and faithful to the input. We propose SuperSharpen, a diffusion-based blind deblurrin...

### 30. Bridge Damage Detection from Low-Light UAV Imagery via Degradation-Aware Mixture-of-Experts Enhancement

- 方向：底层视觉
- 作者：Hu Wang, Hongxu Pu, Zhiqi Hu, Fangzhou Lin, Wang Wang
- 日期：2026-08-24
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2608.23136v1

摘要：

Poor illumination obscures small, low-contrast defects in UAV bridge imagery, reducing the reliability and operational flexibility of automated inspection. This paper investigates whether degradation-aware image restoration can improve bridge damage detection under low-light conditions and transfer from synthetic degradations to real inspection scenes. We propose DaL- MoE, a detector-agnostic restoration front end trained with an ISP-aware low-light synthesis pipeline and equipped with degradation-aware guidance es...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-08-30-low-level-vision-video-papers.md`
