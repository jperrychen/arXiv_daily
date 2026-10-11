---
title: 2026-10-11｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-10-11｜底层视觉与视频论文速览

生成时间：2026-10-11

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉、视频处理｜LoopMoEVR: Loop-Based Degradation-Aware Mixture-of-Experts for Unified UHD Video Restoration｜2026-10-04
2. 底层视觉｜ContiLNN: Mitigating Slice Sampling Discontinuity with Liquid Neural Networks for Medical Image Restoration｜2026-10-08
3. 底层视觉、视频处理｜Streaming-Aware Diffusion for Real-Time Video Super-Resolution via Cross-Step Attention｜2026-10-08
4. 底层视觉｜DLC: A Metric-Guided Dynamic Loss Controller for Multi-Objective Training｜2026-10-08
5. 底层视觉｜InscriptionOCR: A Dataset and Method for Understanding Inscriptions｜2026-10-07
6. 底层视觉、视频处理｜TSRN-RTVD: Real-Time Video Deblurring System｜2026-10-06
7. 底层视觉｜Frequency-Decoupled Diffusion Guidance for Non-Blind Image Deblurring｜2026-10-05
8. 底层视觉｜Decomposition-Guided Curvelet Thresholding for Sharp-to-Soft CT Kernel Conversion｜2026-10-05
9. 底层视觉｜Gauss-Map Variation for Image Denoising: Geometric Analysis and an Anderson--Accelerated Majorization--Minimization Method｜2026-10-05
10. 底层视觉｜LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation｜2026-10-08
11. 底层视觉｜GenIA: Generative Reconstruction with Test-Time Input Alignment｜2026-10-08
12. 底层视觉｜Just Weather Scoring: Efficient End-to-end Nowcasting with Distributional Diffusion｜2026-10-08
13. 底层视觉｜Healthy Counterfactual Generation via Diffusion Inpainting for Mammography Classification｜2026-10-08
14. 底层视觉｜From Pixels to Structure: Lightweight Vision-Language Models for Document OCR and Structured JSON Extraction｜2026-10-08
15. 底层视觉｜Dino Forcing Flow Models: Do not denoise what you can predict｜2026-10-08
16. 底层视觉｜iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity｜2026-10-08
17. 底层视觉｜Attributing HOW, Not Just WHICH: Counterfactual Response Trajectories for Diffusion Models｜2026-10-08
18. 底层视觉｜A Unified Score Matching Paradigm for Video Anomaly Detection and Anticipation｜2026-10-08
19. 底层视觉｜Refine Connections, Close the Gap: A Reliable Enhancement Framework for Driving Scene Topology｜2026-10-08
20. 底层视觉｜Fluid-Gen-Zero: Grounding Pretrained Video Generators in Physics without Training｜2026-10-07
21. 底层视觉｜Enabling Preference-driven Unlearning in Few-step Distilled Text-to-Image Diffusion Models｜2026-10-07
22. 底层视觉｜GRACE: Generation-aware latent compression for efficient video generation｜2026-10-07
23. 底层视觉｜MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration｜2026-10-07
24. 底层视觉｜SGF+: Decoupling Gradient Flows for Autoregressive Video Generation｜2026-10-07
25. 底层视觉｜Position Forcing: Self-Conditioning 3D Generation｜2026-10-07
26. 底层视觉｜HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration｜2026-10-07
27. 底层视觉｜Do Generative Priors Align with Human Naturalness Perception?｜2026-10-07
28. 底层视觉｜ORCA: Hunting Compositional Failures in Text-to-Image Diffusion｜2026-10-07
29. 底层视觉｜Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning｜2026-10-07
30. 底层视觉｜PhyDiCT: Plug-and-Play CT Reconstruction from Sparse X-Rays via Differentiable Rendering and Strong Priors｜2026-10-07

## 论文摘要

### 1. LoopMoEVR: Loop-Based Degradation-Aware Mixture-of-Experts for Unified UHD Video Restoration

- 方向：底层视觉、视频处理
- 作者：Yucheng Xin, Runci Bai, Yongcong Wang, Guangwei Gao, Jiao Liu, Dianjie Lu, et al.
- 日期：2026-10-04
- 分类：cs.CV
- 关键词：image restoration、denoising、low-light enhancement、video restoration
- arXiv：2610.05109v1

摘要：

Recently, unified high-definition image restoration has attracted considerable attention; however, existing models tend to excessively increase their depth in pursuit of improved generalization, which often yields only limited gains. Meanwhile, loop-based learning paradigms have drawn widespread attention due to their low parameter counts and strong regression capability, as exemplified by GPT-6 and looped Transformers. In this paper, we introduce the loop learning paradigm to address restoration tasks that require...

### 2. ContiLNN: Mitigating Slice Sampling Discontinuity with Liquid Neural Networks for Medical Image Restoration

- 方向：底层视觉
- 作者：Jialei He, Enhe Liu, Sifan Song, Pengfei Jin, Jionglong Su, Hongbin Wang, et al.
- 日期：2026-10-08
- 分类：cs.CV, cs.AI
- 关键词：image restoration、denoising
- arXiv：2610.12337v1

摘要：

Anatomical continuity provides complementary information for medical image restoration, but its use requires accounting for local anatomy and variations in slice sampling. We introduce ContiLNN, which augments two-dimensional restoration backbones with bidirectional closed-form continuous-time (Bi-CfC) modules for cross-slice modeling while retaining in-plane feature extraction. Slice-index intervals modulate gates determined by local features and hidden states, enabling propagation to respond to sampling variation...

### 3. Streaming-Aware Diffusion for Real-Time Video Super-Resolution via Cross-Step Attention

- 方向：底层视觉、视频处理
- 作者：Harris Partaourides, Sotirios Chatzis
- 日期：2026-10-08
- 分类：cs.CV
- 关键词：denoising、video super-resolution
- arXiv：2610.11746v1

摘要：

Real-time video super-resolution requires high spatio-temporal fidelity under strict latency constraints, challenging diffusion models due to their iterative sampling cost and limited temporal coordination. We propose a streaming-aware framework that adapts pretrained single-image latent diffusion models for efficient video super-resolution (VSR) by exploiting the sequential structure of video streams. Our Cross-Step Attention mechanism reuses intermediate denoising features across adjacent frames and diffusion ste...

### 4. DLC: A Metric-Guided Dynamic Loss Controller for Multi-Objective Training

- 方向：底层视觉
- 作者：Jaewan Ko, Janghoon Choi
- 日期：2026-10-08
- 分类：cs.CV
- 关键词：image restoration、image enhancement
- arXiv：2610.11433v1

摘要：

In this paper, we introduce a metric-guided dynamic loss controller (DLC) for multi-objective image restoration. Conventional image restoration pipelines usually train with a fixed weighted combination of multiple losses, without changing the relative importance of fidelity, perceptual similarity, and no-reference quality during optimization. DLC is an architecture- and loss-term-agnostic training-time controller: it does not modify the restoration architecture or introduce new differentiable loss terms, but dynami...

### 5. InscriptionOCR: A Dataset and Method for Understanding Inscriptions

- 方向：底层视觉
- 作者：Jaidev Sanjay Khalane, Akbar Ali, V. N. Prabhakar, Shanmuganathan Raman
- 日期：2026-10-07
- 分类：cs.CV
- 关键词：image restoration、image enhancement
- arXiv：2610.09439v1

摘要：

Ancient script image restoration is a fundamental problem in computer vision, as it directly affects the reliable analysis and interpretation of historical documents and inscriptions. Ashokan Brahmi is an ancient script extensively used during the reign of Emperor Ashoka in the 3rd century BC, primarily for inscriptions in Prakrit. These inscriptions, including major and minor rock and pillar edicts, constitute a valuable yet largely unexplored source of data for computational analysis. The degraded nature of inscr...

### 6. TSRN-RTVD: Real-Time Video Deblurring System

- 方向：底层视觉、视频处理
- 作者：Nikita Alutis, Danila Evsyukov, Egor Chistov, Mikhail Voronin, Evgeney Bogatyrev, Dmitriy Vatolin
- 日期：2026-10-06
- 分类：cs.CV
- 关键词：deblurring、video deblurring
- arXiv：2610.08230v1

摘要：

As video capture moves to handheld and edge devices, motion blur from camera shake has become a pervasive degradation that lowers perceptual quality and harms downstream vision tasks. The strongest deblurring networks recover impressive detail, yet they remain computationally heavy and overwhelmingly complex, so their quality comes at a cost that consumer hardware cannot pay in real time. This gap between restoration quality and on-device speed is exactly what makes real-time deblurring difficult. We developed and...

### 7. Frequency-Decoupled Diffusion Guidance for Non-Blind Image Deblurring

- 方向：底层视觉
- 作者：Sihan Wang, Jinshu Huang, Haibin Su, Yunhua Xue
- 日期：2026-10-05
- 分类：cs.CV
- 关键词：image restoration、deblurring
- arXiv：2610.06221v1

摘要：

Pretrained diffusion models provide powerful image priors for training-free posterior sampling in image restoration. To guide this sampling process, frequency-aware methods progressively incorporate measurement information across frequency bands, facilitating coarse-to-fine reconstruction. However, existing methods typically do not explicitly separate frequency activation from degradation-induced attenuation, leaving attenuation differences among inactive frequencies insufficiently modeled. In this work, we propose...

### 8. Decomposition-Guided Curvelet Thresholding for Sharp-to-Soft CT Kernel Conversion

- 方向：底层视觉
- 作者：Mahmoud Nasr, Jan K. Argasinski, Krzysztof Brzostowski, Adam Piorkowski
- 日期：2026-10-05
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2610.07067v1

摘要：

Image denoising is a crucial task in image processing, focused on improving image quality by minimizing noise while maintaining essential structural elements. This study presents a hybrid denoising framework that combines several decomposition techniques, including empirical mode decomposition (EMD), variational mode decomposition (VMD), multichannel EMD (MEMD), and bidimensional EMD (BEMD), with curvelet transform thresholding. Each decomposition mode undergoes processing through both soft and hard thresholding, a...

### 9. Gauss-Map Variation for Image Denoising: Geometric Analysis and an Anderson--Accelerated Majorization--Minimization Method

- 方向：底层视觉
- 作者：Haibin Su
- 日期：2026-10-05
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2610.05801v1

摘要：

We propose a Gauss-map variation (GMV) model for image denoising that measures the spatial variation of the tangent-plane projectors of the scaled image graph. We establish an equivalent representation of the regularizer in terms of the corresponding Gauss map and, using differential geometric tools including tubular coordinates and the Frenet frame, analyze its behavior across general $C^2$ and piecewise $C^2$ boundaries. The resulting estimates provide edge- and corner-contrast preservation properties. To solve t...

### 10. LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation

- 方向：底层视觉
- 作者：Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim
- 日期：2026-10-08
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.12442v1

摘要：

Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This deterministic mapping assigns each pixel to a single reprojected location, which preserves texture but transl...

### 11. GenIA: Generative Reconstruction with Test-Time Input Alignment

- 方向：底层视觉
- 作者：Stefano Esposito, Naama Pearl, Polina Karpikova, Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder, et al.
- 日期：2026-10-08
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.12388v1

摘要：

Reconstructing complete 3D object assets from monocular or sparse multi-view observations remains challenging. Generative 3D foundation models can complete object geometry beyond the observed views, but their predictions may not faithfully reproduce the observed geometry, appearance, or pose. We introduce GenIA, a framework for test-time input-aligned generation that grounds SAM3D's generative prior in geometric and photometric observations without retraining the foundation model. We improve object pose by deriving...

### 12. Just Weather Scoring: Efficient End-to-end Nowcasting with Distributional Diffusion

- 方向：底层视觉
- 作者：Jannik Wiese, Johannes Schusterbauer, Tommaso Martorella, Björn Ommer
- 日期：2026-10-08
- 分类：cs.LG, cs.CV
- 关键词：denoising
- arXiv：2610.12189v1

摘要：

Generative diffusion models are well-suited for probabilistic precipitation nowcasting, but existing approaches often rely on separately trained compression or deterministic forecasting components and remain costly at inference due to iterative denoising. We introduce Just Weather Scoring (JWS), a single-stage, end-to-end diffusion model which addresses both issues by forecasting directly in radar space and enabling few-step generation. Radar-space modeling greatly simplifies training and inference and eliminates u...

### 13. Healthy Counterfactual Generation via Diffusion Inpainting for Mammography Classification

- 方向：底层视觉
- 作者：Inês Cruchinho Garcia, Mariana Mourão, Francisco Maria Calisto, Carlos Santiago, Jacinto Nascimento
- 日期：2026-10-08
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.12147v1

摘要：

False negatives remain a critical limitation of computer-aided diagnosis (CAD) systems for breast cancer screening due to delayed detection and treatment. To address this issue, we propose a counterfactual data augmentation strategy that generates healthy mammograms by "erasing" lesions from anomalous images, thereby enriching the training distribution. We train a Denoising Diffusion Probabilistic Model on BI-RADS 1 (healthy) mammograms and use a RePaint-based sampling strategy to inpaint realistic normal tissue wi...

### 14. From Pixels to Structure: Lightweight Vision-Language Models for Document OCR and Structured JSON Extraction

- 方向：底层视觉
- 作者：Uddipan Basu Bir, Vincent Christlein, Andreas Maier, Mathias Zinnen
- 日期：2026-10-08
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2610.11818v1

摘要：

While massive, closed-source Vision-Language Models (VLMs) set strong benchmarks for document understanding, their dependence on commercial APIs limits adoption in institutional archives due to data autonomy concerns, recurring costs, and the environmental footprint of hyperscale computing. This is especially acute in heritage digitization, where documents include historical handwriting, domain-specific terminology (e.g., jewelry, prehistory, architecture), and non-standard layouts requiring high-dimensional struct...

### 15. Dino Forcing Flow Models: Do not denoise what you can predict

- 方向：底层视觉
- 作者：Arijit Ghosh, Lucas Degeorge, Paul Couairon, Alexei A Efros, Vicky Kalogeiton, David Picard
- 日期：2026-10-08
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.11751v1

摘要：

Co-denoising pretrained representations such as DINO can substantially improve the training speed and quality of flow matching models, but it introduces a second denoising trajectory and requires carefully designed schedules. We propose a simpler alternative: predict the pretrained representation directly, then condition the model on its own prediction. This removes the need for a second ODE and any representation-specific denoising schedules, while retaining the benefits of representation guidance. Our approach co...

### 16. iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity

- 方向：底层视觉
- 作者：Chengfeng Han, Baole Ai, Xianlu Bian, Jie Yao, Zilong Huang, Ang Wang, et al.
- 日期：2026-10-08
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.11302v1

摘要：

Training-free sparse attention offers a practical acceleration solution to Diffusion Transformers (DiTs) via reducing computations without fine-tuning. It typically involves estimating the importance of query-key regions and deriving sparse masks to compute only the important candidates, which inevitably introduces approximation errors that may degrade generation quality. To better balance the efficiency-quality trade-off, we propose iCATS, integrating improved importance estimation and sparse mask construction wit...

### 17. Attributing HOW, Not Just WHICH: Counterfactual Response Trajectories for Diffusion Models

- 方向：底层视觉
- 作者：Haoqian Zhang, Ziyuan Yang, Zerui Shao, Yi Zhang
- 日期：2026-10-08
- 分类：cs.CV, cs.GR
- 关键词：denoising
- arXiv：2610.11238v1

摘要：

Diffusion models have achieved remarkable success in image generation, yet tracing their outputs to individual training examples remains challenging. Existing attribution methods often compress factor-specific effects into scalar responses, making distinct internal changes indistinguishable. This is particularly limiting for diffusion models, where semantic factors emerge through evolving representation dynamics during denoising. We therefore reformulate diffusion data attribution as attributing factor-induced inte...

### 18. A Unified Score Matching Paradigm for Video Anomaly Detection and Anticipation

- 方向：底层视觉
- 作者：Congqi Cao, Zhenhe Liang, Hanwen Zhang, Yifan Zhao, Qinyi Lv, Lingtong Min, et al.
- 日期：2026-10-08
- 分类：cs.CV, eess.IV
- 关键词：denoising
- arXiv：2610.11149v1

摘要：

Video anomaly detection (VAD) is a fundamental and safety-critical task in computer vision. Recent generative approaches detect anomalies from a distributional perspective, but remain limited by local anomaly modes. Meanwhile, video anomaly anticipation (VAA), as a proactive extension beyond post-hoc detection, introduces additional challenges. In particular, the contrastive inference paradigm in VAD, which relies on ground-truth frames, is not applicable to VAA, hindering its development. To address these challeng...

### 19. Refine Connections, Close the Gap: A Reliable Enhancement Framework for Driving Scene Topology

- 方向：底层视觉
- 作者：Xiaoqi Wang, Dingyi Zhaung, David Paz, Wenbin He, Yucai Bai, Peng Zhou, et al.
- 日期：2026-10-08
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.11058v1

摘要：

In autonomous driving, understanding scene topology - the connectivity between lanes and traffic elements - is critical for safe path planning and motion control. While current methods excel at detecting individual map elements, their connectivity reasoning often falls short of its theoretical potential, leaving a significant performance gap relative to the theoretical upper-bound achievable given the underlying detections. Furthermore, the decision-ready topology graphs passed to downstream tasks often remain unre...

### 20. Fluid-Gen-Zero: Grounding Pretrained Video Generators in Physics without Training

- 方向：底层视觉
- 作者：Hong Huang, Yuqiu Liu, Chenyu You, Daniel Martin, Chuhang Zou, Wuyang Chen
- 日期：2026-10-07
- 分类：cs.CV, cs.GR
- 关键词：denoising
- arXiv：2610.10984v1

摘要：

We present Fluid-Gen-Zero, a training-free framework for physics-aware fluid-object interaction video generation that decouples physical reasoning from appearance synthesis. Our key insight is to delegate motion dynamics to a physics simulator while preserving the appearance modeling capacity of pretrained video generators. We bridge these two domains through a two-level agentic workflow: generation-time planning, where a vision-language model (VLM) agent interprets intent and the simulation rollout to organize gen...

### 21. Enabling Preference-driven Unlearning in Few-step Distilled Text-to-Image Diffusion Models

- 方向：底层视觉
- 作者：Gaurav Patel, Jun Fang, Greg Ver Steeg, Qiang Qiu, Sravan Sripada
- 日期：2026-10-07
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2610.10859v1

摘要：

Text-to-image diffusion models are increasingly distilled into few-step variants and being deployed to enable fast inference. However, their ability to generate harmful or undesired content poses significant safety risks. Data-driven unlearning methods suppress targeted generations by fine-tuning model weights using specialized unlearning objectives. Crucially, these objectives implicitly rely on multi-step denoising dynamics, an assumption that breaks down for few-step distilled (FSD) models, resulting in ineffect...

### 22. GRACE: Generation-aware latent compression for efficient video generation

- 方向：底层视觉
- 作者：Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam, Donghoon Lee, Hyunsung Go, Yeonkyeong Lee, et al.
- 日期：2026-10-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.10524v1

摘要：

Highly compressed video autoencoders offer an effective way to accelerate video diffusion models, as the Diffusion Transformer (DiT) operates on far fewer tokens. However, such autoencoders are challenging to train, since a higher compression ratio degrades reconstruction quality and recovering it requires more channels, which is known to slow the convergence of the DiT. The compressed latent also differs from the one the DiT was trained on, so the pretrained DiT must be either retrained from scratch or adapted at...

### 23. MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration

- 方向：底层视觉
- 作者：Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang, Teng Hu, Songhang Shen, Bohao Feng, et al.
- 日期：2026-10-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.10457v1

摘要：

Diffusion Transformers (DiTs) achieve remarkable performance in video synthesis, but their iterative denoising process suffers from high inference latency. To address this, caching has emerged as an effective acceleration strategy by capitalizing on inter-step redundancy during denoising. Existing dynamic caching methods typically estimate the error that cache reuse would introduce at each denoising step (step error) to guide cache decisions, whereas our concern is how much quality loss cache reuse would cause in t...

### 24. SGF+: Decoupling Gradient Flows for Autoregressive Video Generation

- 方向：底层视觉
- 作者：Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, et al.
- 日期：2026-10-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.10429v2

摘要：

Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus (SGF+), which assigns separate parameters to context writing and denoising while preserving their interac...

### 25. Position Forcing: Self-Conditioning 3D Generation

- 方向：底层视觉
- 作者：Ziheng Ouyang, Zeqiang Lai, Jiarui Chen, Jiangshan Wang, Yuhao Wan, Jingbo Gong, et al.
- 日期：2026-10-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.10342v1

摘要：

Recent single-stage 3D generative models commonly adopt VecSet representations, encoding 3D shapes as unordered sets of latent tokens. However, compared with two-stage methods that provide explicit positional guidance, these models must implicitly infer token positions throughout denoising, limiting their generation quality. We observe that, despite the absence of explicit positional conditioning, VecSet tokens retain recoverable spatial correspondences. Building on this observation, we propose Position Forcing, a...

### 26. HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration

- 方向：底层视觉
- 作者：Xiangtao Kong, Shuaizheng Liu, Rongyuan Wu, Lingchen Sun, Zhengqiang Zhang, Jinxin Zhao, et al.
- 日期：2026-10-07
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2610.10133v2

摘要：

Real-world low-quality images suffer from complex mixed degradations, including but not limited to noise, blur, atmospheric effects, etc. Recent agentic methods usually model real-world image restoration (Real-IR) as a sequential tool calling problem over task-specific single-degradation restoration models. This paradigm, however, is fundamentally limited because complex real-world degradations cannot be cleanly undone degradation by degradation, and the tool used for task-specific models caps the capability of the...

### 27. Do Generative Priors Align with Human Naturalness Perception?

- 方向：底层视觉
- 作者：Taiki Fukiage
- 日期：2026-10-07
- 分类：cs.CV, q-bio.NC
- 关键词：denoising
- arXiv：2610.09928v1

摘要：

Visual generative models are trained to capture the probability distributions of natural images, yet whether their native priors reflect the regularities governing human perception of image naturalness remains an open question. Here, we probe these priors through native prediction errors across 25 open image and video generators. Because raw single-image losses are dominated by scene content and visual complexity, we evaluate directional loss differences using content-preserving, paired relational interventions tha...

### 28. ORCA: Hunting Compositional Failures in Text-to-Image Diffusion

- 方向：底层视觉
- 作者：Arshia Hemmat, Amirhossein Vahidi, Amitis Shidani, Mohammad Vali Sanian, Hesam Asadollahzadeh, Aryan Yazdan Parast, et al.
- 日期：2026-10-07
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2610.09841v1

摘要：

Text-to-image diffusion models fail predictably on compositional prompts: attributes bind to the wrong objects, spatial relations invert, and multi-object scenes lose count. Recent architectures already augment CLIP with a T5 encoder precisely because CLIP's contrastive embedding loses compositional structure, yet these failures persist. We argue the binding problem is therefore not one of missing information but of misaligned information: a text encoder preserves compositional structure, but in a representation sp...

### 29. Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning

- 方向：底层视觉
- 作者：Hanqiu Li Cai, Chema Garabito
- 日期：2026-10-07
- 分类：cs.CV, cs.AI
- 关键词：image restoration
- arXiv：2610.09450v1

摘要：

Pixel-space diffusion models avoid the lossy VAE of latent models, which suggests an advantage on downstream tasks where fine-grained detail matters. We test this claim along both routes to a pixel-space backbone. We pretrain Iris-3B, a 3B-parameter pixel-space text-to-image transformer, from scratch through a $256\to512\to1024$ curriculum, after first ablating the prediction target and representation alignment at $256^2$ to decide what to scale. We also convert a pretrained latent model, FLUX.2 Klein base 4B, to p...

### 30. PhyDiCT: Plug-and-Play CT Reconstruction from Sparse X-Rays via Differentiable Rendering and Strong Priors

- 方向：底层视觉
- 作者：Weicheng Dai, Shantanu Ghosh, Kayhan Batmanghelich
- 日期：2026-10-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.09253v1

摘要：

Reconstructing 3D Computed Tomography (CT) images from a few X-ray projections is a highly ill-posed inverse problem due to the loss of volumetric information. We propose PhyDiCT, a training-free framework that integrates a differentiable Physics-based forward model, grounded in the Beer-Lambert law, with a text-conditioned Diffusion as a strong prior to reconstruct 3D lung CT images. We refer to our approach as training-free since the prior model is used without fine-tuning, and our goal is to steer the denoising...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-10-11-low-level-vision-video-papers.md`
