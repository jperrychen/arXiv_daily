---
title: 2026-08-09｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-08-09｜底层视觉与视频论文速览

生成时间：2026-08-09

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Flow-Map Distillation on Relation Manifolds for Image Restoration｜2026-08-06
2. 底层视觉｜LiteKD-Net: Lightweight Knowledge-Distilled Network for Mobile Image Denoising｜2026-08-06
3. 顶会论文｜The First EgoCross Challenge at EgoVis 2026: Cross-Domain Egocentric Video Question Answering｜2026-08-05
4. 底层视觉｜S$^3$-Diff: Structural Semantic Synergy Diffusion Model for High Fidelity Super Resolution of Pathological Images｜2026-08-04
5. 底层视觉｜EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation｜2026-08-06
6. 底层视觉｜Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training｜2026-08-06
7. 底层视觉｜Domain-Grounded Candidate Selection for Agentic Image Editing: A Shadow Removal Case｜2026-08-06
8. 底层视觉｜Iterate or Widen? When Test-Time Refinement Helps LiDAR Scene Completion: A Controlled Study of Evidence Geometry, Training Coverage, and Compute｜2026-08-06
9. 视频处理｜Diff-VF: Training-free High-quality Long Video Generation via Diffusion Model｜2026-08-06
10. 底层视觉｜Overcoming Attention Drift: Homogeneity-Heterogeneity Guided Feature Aggregation for Low-Light Remote Sensing Image Enhancement｜2026-08-06
11. 底层视觉｜Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification｜2026-08-06
12. 底层视觉｜PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models｜2026-08-06
13. 底层视觉｜SciQNet: Two-Stage Multimodal Adaptation for Scientific Image Quality Assessment｜2026-08-06
14. 底层视觉｜Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming｜2026-08-06
15. 视频处理｜A Multi-Layer System for Ultra-High-Resolution Static 360-Degree Telepresence｜2026-08-06
16. 底层视觉｜Hierarchical Flow Matching for 3D Point Cloud Generation｜2026-08-06
17. 底层视觉｜MOSAIK: Multi-Patch Content-Aware Spatial Allocation of Image Tokens for Efficient Generation｜2026-08-05
18. 底层视觉｜ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Context Routing｜2026-08-05
19. 底层视觉｜In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion｜2026-08-05
20. 顶会论文｜Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors｜2026-08-05
21. 底层视觉｜MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight｜2026-08-05
22. 底层视觉｜Visual Anchoring in Diffusion: Multimodal Zero-Shot Skeleton Action Recognition｜2026-08-05
23. 底层视觉｜StyleComposer: Training-Free Multi-Reference Style Composition｜2026-08-05
24. 底层视觉｜Coupled Continuous-Discrete Generation for Scene Text Image Super-Resolution｜2026-08-05
25. 底层视觉｜UBLLIE: Unified Backlight and Low-Light Image Enhancement｜2026-08-05
26. 底层视觉｜Faster-WAM: Efficient Inference-Time Future Conditioning for Robust World Action Models｜2026-08-05
27. 视频处理｜OmniVR: Joint Video-Audio Conditional Generation for Restoring Degraded Historical Films｜2026-08-04
28. 底层视觉｜Latent Reward Registers for Diffusion Preference Alignment｜2026-08-04
29. 底层视觉｜GVCCTurbo: Rate-Compute Quality Scheduling for Codebook Driven Generative Compression｜2026-08-04
30. 底层视觉｜3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment｜2026-08-04

## 论文摘要

### 1. Flow-Map Distillation on Relation Manifolds for Image Restoration

- 方向：底层视觉
- 作者：Zihao He, Songhua Liu
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：image restoration、denoising、deblurring、low-light enhancement
- arXiv：2608.05769v1

摘要：

Knowledge distillation for image restoration typically aligns intermediate features or relation matrices between teacher and student networks as static targets, ignoring the dynamic structure of the knowledge transfer process. In this paper, we propose Flow-Map Distillation on Relation Manifolds (FoRM), which reformulates relation-based knowledge transfer as a continuous flow mapping problem on the relation manifold. Rather than regressing a constant velocity field between student and teacher relation states, FoRM...

### 2. LiteKD-Net: Lightweight Knowledge-Distilled Network for Mobile Image Denoising

- 方向：底层视觉
- 作者：Zhou Zhiyi
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：image denoising、denoising
- arXiv：2608.05739v1

摘要：

Mobile image denoising requires both good restoration quality and low computational cost. In addition, it's annoying to collect large-scale LQ-GT clean pairs. As a result, we propose LiteKD-Net, a lightweight knowledge-distilled network for mobile image denoising. First, a physics-guided noise simulation pipeline generates paired training data by adding pixel crosstalk compared with pipelines applied to cameras. Next, we adapt the Real-ESRGAN to identity-resolution denoising and construct a lightweight Student usin...

### 3. The First EgoCross Challenge at EgoVis 2026: Cross-Domain Egocentric Video Question Answering

- 方向：顶会论文
- 作者：Yuqian Fu, Tianwen Qian, Yanjun Li, Yu Li, Kunyu Peng, Xu Zheng, et al.
- 日期：2026-08-05
- 分类：cs.CV, cs.AI
- 关键词：CVPR 2026、CVPR
- arXiv：2608.04589v1

摘要：

EgoCross is a cross-domain egocentric video question answering benchmark designed to evaluate whether multimodal large language models can generalize beyond common daily-life scenarios. The first EgoCross Challenge was hosted at the Third EgoVis Workshop at CVPR 2026 and evaluated models on first-person videos from four target domains: surgery, industrial assembly, extreme sports, and animal perspectives. Each test example consists of an egocentric video clip, a question, and four candidate answers, from which the...

### 4. S$^3$-Diff: Structural Semantic Synergy Diffusion Model for High Fidelity Super Resolution of Pathological Images

- 方向：底层视觉
- 作者：Jiaming Liang, QiHui Han, Guangye Ou, Jiawen Liu, Haolin Chen, Xi Zhong, et al.
- 日期：2026-08-04
- 分类：cs.CV
- 关键词：super resolution、denoising
- arXiv：2608.03540v1

摘要：

Digital pathology relies on high-resolution whole slide images for accurate diagnosis, yet limitations in imaging devices, storage, and transmission often make lower-resolution pathology images more common in clinical workflows. Current super-resolution techniques often tend to smooth diagnostically relevant morphology, leading to over-smoothed textures and semantic drift that compromise downstream clinical interpretation. To this end, we develop the Structural Semantic Synergy Diffusion Model (S3-Diff), a diffusio...

### 5. EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation

- 方向：底层视觉
- 作者：Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.06231v1

摘要：

Emotion shapes how viewers interpret a scene, yet existing video generators entangle global atmosphere, affect-bearing semantic cues, and temporal progression within a single text condition. We present EmoWorld, a framework that decouples these factors within a frozen flow-matching video diffusion transformer (Video DiT). A one-time preparation stage extracts layer-specific affect directions and a reusable cue library from geometry-preserving neutral and emotion-edited panoramas. At inference, Visual Atmosphere Ste...

### 6. Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training

- 方向：底层视觉
- 作者：Rui Li, Yuanzhi Liang, Ke Hao, Ziqiao Weng, Haibin Huang, Chi Zhang, et al.
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.06125v1

摘要：

Latent reward models can supervise visual diffusion models without decoding intermediate states into pixel space. This makes alignment with human preferences more efficient. However, existing latent reward models output only scalar scores. They do not estimate the uncertainty of each prediction. The generator therefore cannot determine which feedback is reliable. This can drive optimization in the wrong direction and lead to reward hacking. We propose \textsc{SURE}, a unified latent-space framework for image and vi...

### 7. Domain-Grounded Candidate Selection for Agentic Image Editing: A Shadow Removal Case

- 方向：底层视觉
- 作者：Shilin Hu, Jingyi Xu, Dimitris Samaras, Hieu Le
- 日期：2026-08-06
- 分类：cs.CV, cs.AI
- 关键词：low-level vision
- arXiv：2608.06075v1

摘要：

Commercial vision-language models are reshaping computer vision, with visual priors broad enough to rival task-specific systems. This raises a natural question: do they reduce the need for classic, physics-informed low-level vision? We study this through shadow removal, a problem shaped by scene geometry, illumination, materials, and occluders, where paired shadow and shadow-free data are hard to collect at scale. We find that a commercial generative editor, used directly, can produce clean shadow-free edits that p...

### 8. Iterate or Widen? When Test-Time Refinement Helps LiDAR Scene Completion: A Controlled Study of Evidence Geometry, Training Coverage, and Compute

- 方向：底层视觉
- 作者：Shijie Hao, Weining Zhang
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.06014v1

摘要：

Should a completion model spend extra test-time compute by iterating, or spend a similar parameter budget on a wider one-shot predictor? The answer is easily confounded by denoising curricula, corruption augmentation, capacity, and unpaired evaluation. We study this question in LiDAR semantic scene completion by comparing a one-shot predictor, a parameter-matched wider predictor, and a weight-tied multigrid refiner initialized from the same frozen predictor. The protocol separates coherent region removal, independe...

### 9. Diff-VF: Training-free High-quality Long Video Generation via Diffusion Model

- 方向：视频处理
- 作者：Haoning Yang, Xinyuan Chen, Yaohui Wang, Guo Lu
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：video enhancement
- arXiv：2608.05976v1

摘要：

Recently, diffusion models have made great progress in video generation. However, most existing video diffusion models are trained with short videos, and degrade when extrapolated to long videos, struggling to maintain long-range temporal coherence while retaining diverse motions. To generate consistent, high-quality and dynamic long videos, we propose Diff-VF, a training-free, plug-and-play and model-agnostic framework that converts existing short-video diffusion backbones into long-video generators without modify...

### 10. Overcoming Attention Drift: Homogeneity-Heterogeneity Guided Feature Aggregation for Low-Light Remote Sensing Image Enhancement

- 方向：底层视觉
- 作者：Yaozi Zhong, Xingxing Yang, Shaohui Mei, Mingyang Ma
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2608.05843v1

摘要：

Restoring high-fidelity remote sensing imagery from extreme low-light degradation is indispensable for reliable Earth observation and downstream machine vision. However, under severe noise and illumination corruption, existing methods suffer from attention drift, erroneously aggregating features across distinct physical boundaries and causing severe structural blurring and color distortion. To address this, we propose HALO, a dual-prior-driven enhancement framework that formulates enhancement as a guided feature ag...

### 11. Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification

- 方向：底层视觉
- 作者：Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, et al.
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.05776v1

摘要：

Autoregressive continuation provides a natural path toward minute-scale audio-visual generation by repeatedly extending a short-window generator conditioned on previously generated video and audio. However, models are trained on clean ground-truth histories, while inference relies on their own generated histories, where accumulated errors cause identity drift, over-smoothing, and audio-visual desynchronization. Recent methods reduce this mismatch by reusing prediction residuals as synthetic corruption, but we obser...

### 12. PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models

- 方向：底层视觉
- 作者：Xi Zeng, Haojie Ren, Ziying Song
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.05720v1

摘要：

We propose PhyLatent, a dynamics-relevant training objective for JointEmbedding Predictive Architecture (JEPA) world models. Our key observation is that preventing global latent collapse does not ensure that a representation preserves physical states and action consequences. We identify three failure modes in JEPA world models: physical invariance collapse, physical identifiability collapse, and counterfactual dynamics collapse. PhyLatent addresses them through three training pathways: physical invariance, physical...

### 13. SciQNet: Two-Stage Multimodal Adaptation for Scientific Image Quality Assessment

- 方向：底层视觉
- 作者：Yin-Loon Khor, Yi-Jie Wong, Jing Jie Tan, Ming Jie Lee
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2608.05691v1

摘要：

Scientific images are essential for communicating experimental observations, quantitative evidence and conceptual knowledge. Unlike natural images, their quality depends on both visual clarity and scientific informativeness, making assessment challenging. In this work, we present SciQNet, a two-stage multimodal adaptation framework for scientific image quality assessment. The first stage performs domain-adaptive pretraining on scientific document images and the second stage conducts task-specific fine-tuning with j...

### 14. Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming

- 方向：底层视觉
- 作者：Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, et al.
- 日期：2026-08-06
- 分类：cs.CV, cs.SD
- 关键词：denoising
- arXiv：2608.05663v1

摘要：

Real-time long-form avatar audio--video generation requires causal, continuous synthesis while maintaining audiovisual synchronization and visual consistency. Adapting a pretrained bidirectional model to this setting presents two key dilemmas. First, autoregressively reusing generated blocks as context creates exposure bias, causing errors and visual drift to accumulate over long rollouts. Second, a global speech utterance does not indicates a causal generator which portion should be spoken next when only limited l...

### 15. A Multi-Layer System for Ultra-High-Resolution Static 360-Degree Telepresence

- 方向：视频处理
- 作者：Jiapeng Chi, Gerd Bruder, Carsten Neumann, Carolina Cruz-Neira, Dirk Reiners
- 日期：2026-08-06
- 分类：cs.HC, cs.CV
- 关键词：video super-resolution
- arXiv：2608.05570v1

摘要：

360-degree video telepresence offers strong immersive potential but remains constrained by the limited resolution of current capture and display hardware. Many telepresence installations feature fixed viewpoints and largely static scenes, yet optimization strategies tailored to such setups have received limited attention. We present a multi-layer, ultra-high-resolution system for static 360-degree telepresence that combines an 8K panoramic camera with a rotatable 4K pan-tilt-zoom (PTZ) camera. Our approach builds a...

### 16. Hierarchical Flow Matching for 3D Point Cloud Generation

- 方向：底层视觉
- 作者：Linhao Wang, Qichang Zhang, Ye Su, Hao Wang
- 日期：2026-08-06
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.05557v1

摘要：

Generating high-quality 3D point clouds requires capturing both global shape topology and local geometric details. Existing flow-based methods rely on continuous normalizing flows (CNFs) that demand expensive ODE solving and trace estimation during training, while diffusion models require hundreds of iterative denoising steps. Moreover, most approaches adopt single-level generation directly in point space, disregarding the hierarchical structure natural to 3D shapes. We propose Hierarchical Flow Matching (HFM) that...

### 17. MOSAIK: Multi-Patch Content-Aware Spatial Allocation of Image Tokens for Efficient Generation

- 方向：底层视觉
- 作者：Mohammadreza Hami, Mohammadreza Samadi, Chao Gao, Negar Hassanpour
- 日期：2026-08-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.05450v1

摘要：

Pixel-space diffusion models avoid the reconstruction ceiling of latent diffusion models by generating directly in image space. However, their substantially higher token count makes generation expensive due to the quadratic complexity of self-attention. Several existing efficiency methods reduce this cost by using larger patches at selected denoising steps, thereby representing the image with fewer tokens. Yet, each step still uses a single patch size uniformly across the entire image, overlooking that different re...

### 18. ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Context Routing

- 方向：底层视觉
- 作者：Xu Guo, Zhengxuan Wei, Xinghui Li, Hanzhuo Huang, Xinyu Liu, Xiangyang Luo, et al.
- 日期：2026-08-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.04956v1

摘要：

Recent video models increasingly support generation, reference conditioning, and editing within a single model, yet typically expose them as separate operations over fixed inputs. Practical creation unfolds across multiple shots, requiring one model to generate from text, follow a reference, or edit source footage while maintaining shared history. We formalize this setting as interactive multi-shot video creation (IMVC) and introduce ContextMaster, a unified model with a role-aware context representation for these...

### 19. In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion

- 方向：底层视觉
- 作者：Lingxiao Yang, Liu Liu, Moran Li, Han Feng, Wenjian Cao, Jiangning Zhang, et al.
- 日期：2026-08-05
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2608.05237v1

摘要：

Current few-step autoregressive video diffusion models depend on previous fully denoised clean frames as context for all denoising steps of the current frame. However, these clean frames leak excessive local details, which causes the model to take shortcuts, resulting in compromised temporal semantics and dynamics. Inspired by the perspective of diffusion as masking, we explore the impact of noisy contexts on few-step autoregressive generation. Yet, simply applying contexts with the same noise levels provides insuf...

### 20. Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors

- 方向：顶会论文
- 作者：Hakyeong Kim, Ruicheng Wang, Chengtang Yao, Jiaolong Yang, Min H. Kim
- 日期：2026-08-05
- 分类：cs.CV, cs.GR
- 关键词：CVPR
- arXiv：2608.04737v1

摘要：

Direct Time-of-Flight (dToF) sensors provide highly accurate metric depth and are more robust than indirect ToF systems in challenging real-world conditions. However, their high manufacturing cost and limited photodiode array size produce depth maps that are extremely sparse, low-resolution, and noisy, making them unsuitable for VR/XR, robotics, and 3D perception tasks that require dense metric depth. Existing monocular and depth completion methods struggle to handle the unique sampling patterns and hardware artifa...

### 21. MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight

- 方向：底层视觉
- 作者：Zehua Fan, Junjie He, Wenxuan Song, Xi Wang, Wenqi Lyu, Linge Zhao, et al.
- 日期：2026-08-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.04657v2

摘要：

World action models (WAMs) built on video generation backbones are a rising recipe for robot learning, yet remain confined to tabletop manipulation. Mobile manipulation demands simultaneous locomotion and whole-body manipulation amid scene-scale dynamics, yet is still dominated by dynamics-blind visual encoders with hand-crafted coordination. We bridge this gap with MobileWAM, a mixture-of-transformers architecture that fuses a pretrained video diffusion transformer with a lightweight action expert through layerwis...

### 22. Visual Anchoring in Diffusion: Multimodal Zero-Shot Skeleton Action Recognition

- 方向：底层视觉
- 作者：Zehao Bao, Shujun Guo, Bruce X. B. Yu
- 日期：2026-08-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.04623v1

摘要：

Zero-shot Skeleton Action Recognition (ZSAR) remains ambiguous when unseen actions share similar skeleton joint dynamics but differ in objects or scene context. RGB provides these missing cues, yet existing multimodal methods typically maintain independent skeleton and RGB scoring branches and fuse their outputs. Without using unlabeled test data for adaptation or fusion calibration, a fixed fusion weight cannot capture class-pair-dependent modality reliability, while an adaptive rule lacks target-side feedback for...

### 23. StyleComposer: Training-Free Multi-Reference Style Composition

- 方向：底层视觉
- 作者：Sanghyeok Lee, Jihye Kang, Namhyuk Ahn
- 日期：2026-08-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.05213v1

摘要：

The style of a painting is not monolithic: color, texture, and structure may come from different sources. Existing reference-guided methods transfer them as one style signal, leaving each attribute's source and strength outside the user's control. We ask where in a diffusion model one attribute can change while the others hold, and find that no single representation isolates all three. The proposed StyleComposer therefore routes each style attribute through the representation where it separates best and coordinates...

### 24. Coupled Continuous-Discrete Generation for Scene Text Image Super-Resolution

- 方向：底层视觉
- 作者：Axi Niu, Knag Zhang, Qingsen Yan, Hao Jin, Jinqiu Sun, Yanning Zhang
- 日期：2026-08-05
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2608.04525v1

摘要：

Scene text image super-resolution (STISR) aims to recover visually plausible appearance while preserving character semantics from degraded inputs. Existing STISR systems often rely on externally generated priors or separate image and text models, resulting in error propagation and costly multi-stage inference. We present DualTSR, a unified framework that formulates STISR as coupled continuous-discrete generation. Conditional flow matching restores continuous image latents, while absorbing-state discrete diffusion r...

### 25. UBLLIE: Unified Backlight and Low-Light Image Enhancement

- 方向：底层视觉
- 作者：Yasmin Yasin, Muhammad Usman, Ibrahim Radwan, Saeed Anwar
- 日期：2026-08-05
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2608.04429v1

摘要：

Backlit and low-light images often suffer from severe exposure imbalance or global underexposure, presenting significant challenges for both visual perception and downstream computer vision tasks. In this paper, we propose a unified, unsupervised enhancement framework that addresses both types of degradation without relying on paired ground-truth data. Our approach builds on CLIP-guided prompt learning to semantically supervise enhancement using learned positive and negative textual prompts. To improve the quality...

### 26. Faster-WAM: Efficient Inference-Time Future Conditioning for Robust World Action Models

- 方向：底层视觉
- 作者：Weiheng Zhao, Haoyi Jiang, Xin Shi, Liu Liu, Fan Huang, Zhizhong Su, et al.
- 日期：2026-08-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2608.04404v1

摘要：

World Action Models (WAMs) improve robot manipulation by learning how the environment evolves beyond the current observation. However, existing approaches face a fundamental dilemma: Joint-WAMs preserve future-aware representations during inference but incur prohibitive computation costs, while efficient alternatives remove future modeling at inference time and may lose the robustness benefits of temporal reasoning. In this work, we revisit the role of future representations in WAMs and show that inference-time fut...

### 27. OmniVR: Joint Video-Audio Conditional Generation for Restoring Degraded Historical Films

- 方向：视频处理
- 作者：Xin Lu, Zihao Fan, Mingchen Zhong, Jie Huang, Xueyang Fu, Zheng-Jun Zha
- 日期：2026-08-04
- 分类：cs.CV
- 关键词：video restoration
- arXiv：2608.04224v1

摘要：

Historical films suffer from co-occurring visual and audio degradations---blur, noise, flicker, hiss, clipping, and dropout---yet existing methods restore each modality independently, leaving quality gaps and cross-modal inconsistency. We present OmniVR, the first joint audio-video generative restoration model. Built upon a 22B-parameter audio-video generation backbone, OmniVR formulates restoration as conditional generation within a unified multimodal DiT: the low-quality video and audio are encoded as latent cond...

### 28. Latent Reward Registers for Diffusion Preference Alignment

- 方向：底层视觉
- 作者：Yuanshen Guan, Zipeng Feng, Chengru Song, Zhiwei Xiong, Peiqin Sun
- 日期：2026-08-04
- 分类：cs.LG, cs.CV
- 关键词：denoising
- arXiv：2608.03929v2

摘要：

Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents by prepending learnable, position-free register tokens to the input sequence of a frozen Diffusion Transformer (DiT). This independent readout mechanism extracts la...

### 29. GVCCTurbo: Rate-Compute Quality Scheduling for Codebook Driven Generative Compression

- 方向：底层视觉
- 作者：Ziyue Zeng, Dingjie Peng, Xun Su, Hiroshi Watanabe
- 日期：2026-08-04
- 分类：cs.CV
- 关键词：image compression
- arXiv：2608.03517v1

摘要：

Codebook-driven generative compression uses a pretrained image or video generator as a zero-shot visual prior and transmits compact codebook indices to guide reconstruction at ultra-low bitrate. Current codecs tie each finite-rate correction to a fresh prior evaluation, so shortening the sampler also removes correction slots that carry target-dependent information. We propose GVCCTurbo, a BPP-driven scheduler that separates expensive prior refreshes from codebook corrections: after calibrating an atom-count operati...

### 30. 3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment

- 方向：底层视觉
- 作者：Yuke Xing, Jiarui Wang, William Gordon, Zhu Li, Guangtao Zhai, Yiling Xu
- 日期：2026-08-04
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2608.03279v1

摘要：

3D Gaussian Splatting (3DGS) has become a dominant representation for real-time novel view synthesis (NVS), yet its storage footprint makes compression indispensable for practical deployment. 3DGS training and compression introduce representation-specific distortions such as floating artifacts and surface scattering, which conventional image quality assessment (IQA) metrics fail to capture. Moreover, the independent compression of geometric and color attributes may lead to decoupled dimension-specific distortions t...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-08-09-low-level-vision-video-papers.md`
