---
title: 2026-11-08｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-11-08｜底层视觉与视频论文速览

生成时间：2026-11-08

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉、视频处理｜CoGenRec: A Unified Generative Framework for Complementary Vision Reconstruction｜2026-11-05
2. 底层视觉｜Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop｜2026-11-03
3. 底层视觉｜Adaptive Low-Light Enhancement for Road Anomaly Detection: A Multi-Architecture Benchmark and Edge Deployment Study｜2026-11-05
4. 底层视觉｜Unaligned Image Guided Denoising via Cross-modal Conditional Flow Matching｜2026-11-04
5. 底层视觉｜CHROMA-MILL: Joint Low-Light Enhancement and White Balance under Colored Illumination｜2026-11-03
6. 底层视觉｜Local-Global Joint Modeling for Point Cloud Super-Resolution Guided by Multi-Scale Spatial Priors｜2026-11-02
7. 底层视觉｜Efficient Image Denoising on Smartphone GPUs: Mobile AI 2026 Challenge Report｜2026-10-31
8. 视频处理｜Towards Practical 20 kbps Generative Video Compression via Adaptive Tokenization and Entropy Modeling｜2026-11-05
9. 底层视觉｜Flux as a Codec: Zero-Shot Lossy Compression with Flux｜2026-11-05
10. 底层视觉｜StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing｜2026-11-05
11. 底层视觉｜ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation｜2026-11-05
12. 底层视觉｜Neural Image Compression with Internal-External Prior Fusion and Alignment｜2026-11-05
13. 底层视觉｜Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion｜2026-11-05
14. 底层视觉｜OptIMerge: Optimization-Based Merging of Diffusion Models｜2026-11-05
15. 底层视觉｜Compact Motion Embeddings for Feed-forward Unified Human Animation｜2026-11-05
16. 视频处理｜ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation｜2026-11-05
17. 视频处理｜PixelSpline: Continuous Space-Time Video Super-Resolution via Endpoint-Anchored Shared Pixel Trajectories｜2026-11-04
18. 底层视觉｜VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation｜2026-11-04
19. 底层视觉｜TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing｜2026-11-04
20. 底层视觉｜MonoLaDN: Language-Guided DeNoising for Monocular 3D Object Detection｜2026-11-04
21. 底层视觉｜BiCG-Net: Target-Specific Image Quality Assessment via Observation Modeling and In-Image Differencing｜2026-11-04
22. 底层视觉｜UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity Degradation Modeling｜2026-11-04
23. 底层视觉｜DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion｜2026-11-04
24. 底层视觉｜Dual Flow: Joint Image-Measurement Flow for Inverse Problems｜2026-11-04
25. 视频处理｜GSCV++: Lightweight 3D Gaussian Splatting Sequence Compression via Standard Video Codecs｜2026-11-03
26. 视频处理｜Diffusion Plug-in Priors for Self-Supervised Ultrasound Video Restoration｜2026-11-03
27. 底层视觉｜VIGOR: Visual Gain Ordering for Hallucination Mitigation in Multimodal Discrete Diffusion Language Models｜2026-11-03
28. 底层视觉｜An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression｜2026-11-03
29. 底层视觉｜NightIQA: A Comprehensive Dataset and Benchmark for MLLM-Based Nighttime Image Quality Assessment｜2026-11-03
30. 底层视觉｜E2I-Flow: EEG-to-Image Reconstruction via Wavelet-Temporal Cross-Attention and Conditional Flow Matching｜2026-11-03

## 论文摘要

### 1. CoGenRec: A Unified Generative Framework for Complementary Vision Reconstruction

- 方向：底层视觉、视频处理
- 作者：Yapeng Meng, Yuguo Chen, Xiangru Chen, Shaojun Xu, Xuezhen Wang, Lijian Wang, et al.
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：deblurring、video deblurring、frame interpolation
- arXiv：2611.07665v1

摘要：

Capturing scenes with extreme motion and high dynamic range is fundamentally constrained by trade-offs among temporal resolution, spatial detail, signal-to-noise ratio, and dynamic range under practical bandwidth, power, and quantum-efficiency limits. Conventional frame-based cameras therefore suffer from temporal undersampling, exposure-induced motion blur, and sensor saturation. The Complementary Vision Sensor (CVS) addresses these limitations by decomposing visual information across two complementary pathways, a...

### 2. Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop

- 方向：底层视觉
- 作者：Zhuoran Zheng, Doubao
- 日期：2026-11-03
- 分类：cs.CV
- 关键词：image restoration、denoising、deblurring
- arXiv：2611.04268v1

摘要：

Can an LLM directly edit the weights of a diffusion-based image-restoration model to \emph{improve} restoration quality---without gradients, paired data, or fine-tuning? Recent experiments show frontier LLMs can fix structural bugs by modifying as little as \(0.016%\) of parameters, but cannot instill new capabilities. We ask whether weight-space programming (WSP) can move from \emph{debugging} to \emph{improvement} in the precise-regression setting of image restoration (deblurring, super-resolution, denoising, inp...

### 3. Adaptive Low-Light Enhancement for Road Anomaly Detection: A Multi-Architecture Benchmark and Edge Deployment Study

- 方向：底层视觉
- 作者：Obed Honour Eje, Oluwatosin Kolade, Glory Bagai, Taliha Abiodun Folorunso
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：denoising、low-light enhancement
- arXiv：2611.08393v1

摘要：

Road anomaly detection systems on autonomous vehicles must function reliably under degraded visual conditions including darkness, rain, and Harmattan dust haze. This paper benchmarks four object detection architectures, YOLOv8n, YOLOv12n, RT-DETR, and Faster R-CNN, under physically grounded lighting and weather degradation, and shows that uniform application of the SCI low-light enhancement network is actively harmful at dusk-level lighting (-16.1% to -30.7% mAP@50). We propose a lightweight, training-free luminanc...

### 4. Unaligned Image Guided Denoising via Cross-modal Conditional Flow Matching

- 方向：底层视觉
- 作者：Runmin Zhang, Linshan Li, Si-Yuan Cao, Zhu Yu, Lingyu Zhu, Huaqi Zhang, et al.
- 日期：2026-11-04
- 分类：cs.CV
- 关键词：image restoration、denoising
- arXiv：2611.06422v1

摘要：

This work presents UGD-FM, a novel unaligned image guided denoising framework based on cross-modal conditional flow matching. Unlike previous approaches that assume spatially aligned inputs or only handle small-baseline rectified pairs, we address a more challenging setting where severe target noise and large-range two-dimensional cross-modal misalignment coexist. Specifically, we formulate guided denoising as a progressive flow matching process, allowing image restoration and aligned guidance aggregation to mutual...

### 5. CHROMA-MILL: Joint Low-Light Enhancement and White Balance under Colored Illumination

- 方向：底层视觉
- 作者：Pol Riubrogent-Comas, David Serrano-Lozano, Maria Pilligua, Michael S. Brown, Ramon Baldrich, Javier Vazquez-Corral
- 日期：2026-11-03
- 分类：cs.CV
- 关键词：low-light enhancement、image enhancement
- arXiv：2611.04092v1

摘要：

Capturing an image in a low-light environment produces a weak, noisy sensor signal. Low-light image enhancement (LLIE) aims to restore it. Auto white balance (AWB) is also required for every image, and the same noisy signal degrades its ability to infer the scene illuminant. LLIE is typically performed first, followed by AWB, but this strategy remains largely unexamined because existing low-light datasets span a narrow range of illuminants and lack illuminant ground truth for evaluating AWB. We address this with CH...

### 6. Local-Global Joint Modeling for Point Cloud Super-Resolution Guided by Multi-Scale Spatial Priors

- 方向：底层视觉
- 作者：Wang Yang, Wenyi Ge
- 日期：2026-11-02
- 分类：cs.CV
- 关键词：image super-resolution、denoising
- arXiv：2611.02786v1

摘要：

Range-image-based point cloud super-resolution provides an effective way to reconstruct sparse outdoor point clouds by projecting low-resolution LiDAR scans into a regular 2D representation. However, current methods still face three challenges. First, range images exhibit pronounced vertical nonuniformity, with sparse observations in distant regions and denser observations in nearby regions. Some cross-scale fusion mechanisms do not account for the varying reliability of features at different vertical positions, al...

### 7. Efficient Image Denoising on Smartphone GPUs: Mobile AI 2026 Challenge Report

- 方向：底层视觉
- 作者：Andrey Ignatov, Georgy Perevozchikov, Radu Timofte, HaoDong Wu, Desheng Cai, Nikolay Falaleev, et al.
- 日期：2026-10-31
- 分类：cs.CV, cs.AI
- 关键词：image denoising、denoising
- arXiv：2611.00974v1

摘要：

Image denoising is a fundamental problem in mobile photography. Despite a large number of solutions proposed for this task, the majority of them are trained on synthetically produced noisy images, and are additionally too computationally heavy for processing full-resolution images on mobile devices. This creates a need for efficient deep learning-based models that are not only performant but can also be deployed on constrained mobile hardware. In this Mobile AI challenge, we address this problem and propose the par...

### 8. Towards Practical 20 kbps Generative Video Compression via Adaptive Tokenization and Entropy Modeling

- 方向：视频处理
- 作者：Jiancheng Zhao, Jixiang Luo, Haibin Huang, Chi Zhang, Xuelong Li
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：video compression
- arXiv：2611.08099v1

摘要：

Video compression at ultra-low bitrates remains challenging due to the loss of perceptually important details under limited bit budgets. Recent generative video compression methods leverage pretrained video priors to improve perceptual quality and temporal coherence, but many follow a compress-then-generate paradigm, where generative priors are primarily exploited during reconstruction. Moreover, representations learned for generation and reconstruction are not inherently optimized for entropy coding. In this work,...

### 9. Flux as a Codec: Zero-Shot Lossy Compression with Flux

- 方向：底层视觉
- 作者：Fuma Kimishima, Jinjia Zhou
- 日期：2026-11-05
- 分类：cs.LG, cs.CV
- 关键词：image compression
- arXiv：2611.07929v1

摘要：

We propose FluxC, a zero-shot codec that uses Flux as a compression prior. Although DiffC has shown that pretrained diffusion models can serve as zero-shot codecs, we ask how the choice of coding path and reconstruction method affects rate--distortion--perception behavior. We analyze FluxC along three axes: coding cost and bit allocation, reconstruction method, and low rate distortion. At matched signal-to-noise ratio (SNR), we show that the path choice does not affect the ideal information rate, but changes how bi...

### 10. StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing

- 方向：底层视觉
- 作者：Qin Guo, Dan Xu
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.07922v1

摘要：

Text-guided image editing with diffusion models struggles with spatial edits (e.g. manipulating objects, changing viewpoints, manipulating occlusions) that depend on the 3D structure understanding of a scene. Marigold and follow-up work demonstrate that a pretrained diffusion backbone already harbors strong geometric priors that can be activated for depth estimation, yet how to redirect these priors toward editing remains unresolved. Through per-layer gradient probing, we discover that the editing and depth objecti...

### 11. ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation

- 方向：底层视觉
- 作者：Minh Canh Tu, Quang-Binh Nguyen, Khoi Nguyen
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.07658v1

摘要：

Articulated 3D assets are essential for robotic simulation and training, yet their generation from casual images poses a key challenge: recovering part geometry and kinematics that remain mutually consistent. We present ArtCrafter, a novel feed-forward generative model for controllable generation of articulated 3D objects from a pair of images, one depicting the object in the rest state and the other in the open state. At the core of ArtCrafter is a DiT-based generative model that jointly produces part-level meshes...

### 12. Neural Image Compression with Internal-External Prior Fusion and Alignment

- 方向：底层视觉
- 作者：Tiancheng Si, Wenlong Xu, Dahua Gao
- 日期：2026-11-05
- 分类：cs.CV, cs.AI
- 关键词：image compression
- arXiv：2611.07644v1

摘要：

Existing context models for learned image com- pression rely primarily on internal priors from the current image, overlooking common patterns and typical textures shared across natural images. To address this limitation, we propose an Internal-External Prior Fusion-Alignment (IE-PFA) context model built upon quadtree spatial-channel joint modeling, where a learnable dictionary shared by the encoder and decoder serves as an external prior. Specifically, an RWKV-based Spatial- Channel Prior Fusion (RSCPF) module effi...

### 13. Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion

- 方向：底层视觉
- 作者：Jia Li, Xurui Peng, Xing Wang, Hayden Kwok-Hay So
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.07551v1

摘要：

Few-step autoregressive (AR) video diffusion models generate videos chunk by chunk and have made efficient video generation practical. However, further accelerating these models toward real-time generation remains challenging, as few-step distillation leaves little cross-step redundancy for existing training-free caching methods to exploit. We revisit this regime and identify two token-level redundancy patterns: cross-frame redundancy from static content shared across adjacent frames, and cross-step redundancy from...

### 14. OptIMerge: Optimization-Based Merging of Diffusion Models

- 方向：底层视觉
- 作者：Viraj Shah, Ashwini Pokle, Peyman Milanfar, Mauricio Delbracio, Hossein Talebi
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2611.07543v1

摘要：

The arithmetic merging of weights from multiple task-specific models fine-tuned from a shared base model, commonly known as model souping, has emerged as a popular strategy for multi-task learning without the computational overhead of joint retraining. However, naive scalar weight averaging frequently leads to severe performance degradation when the constituent models learn structurally divergent feature representations, leading to destructive parameter interference. We study this problem in a largely unexplored se...

### 15. Compact Motion Embeddings for Feed-forward Unified Human Animation

- 方向：底层视觉
- 作者：Seonwook Park, Hyunsoo Cha, Amrita Mazumdar, Shengze Wang, Tianye Li, Hanbyul Joo, et al.
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.07481v1

摘要：

Animating a reference image with a driver's motion requires a motion representation that captures face, hand, and body articulation but excludes the driver's appearance. Most body animation methods take motion from external pose estimators and render it with many denoising steps; compact learned motion representations mostly cover the face. We present FUHA, a real-time-capable feed-forward transformer that learns a compact motion embedding of the whole human and uses it for face, upper-body, and full-body animation...

### 16. ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation

- 方向：视频处理
- 作者：Caorui Li, Yangguang Ji, Shuxia Lin, Yu Chen, YiCheng Xiao, Yongliang Wu, et al.
- 日期：2026-11-05
- 分类：cs.CV
- 关键词：video quality assessment
- arXiv：2611.07301v1

摘要：

Reinforcement learning has become an effective approach for improving video generation, but its success depends heavily on reliable reward models. Existing methods either map videos directly to opaque scalar scores or generate free-form rationales that are not explicitly optimized as the basis of the final judgment. We propose ArtiVidRM, a verifiable, artifact-as-rubrics video reward model that follows an observe-then-score paradigm. It first identifies visible generation artifacts and organizes them into a structu...

### 17. PixelSpline: Continuous Space-Time Video Super-Resolution via Endpoint-Anchored Shared Pixel Trajectories

- 方向：视频处理
- 作者：Wanqi Yuan, Nianyi Li
- 日期：2026-11-04
- 分类：cs.CV
- 关键词：video super-resolution
- arXiv：2611.06870v1

摘要：

Existing continuous space-time video super-resolution methods often infer motion from only two endpoint frames and model the two motion directions independently, making them vulnerable to ambiguous correspondence and inconsistent trajectories. We introduce a continuous STVSR framework that combines long-context encoding, continuous HR feature lifting, and an endpoint-anchored PixelSpline. Long-range observations provide more reliable endpoint representations, while continuous upsampling constructs detailed appearan...

### 18. VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation

- 方向：底层视觉
- 作者：Yihong Luo, Tianyu Pang, Tianyang Hu
- 日期：2026-11-04
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.06796v1

摘要：

Few-step distillation offers efficient generation with diffusion and flow models, but preserving quality with only a few sampling steps remains challenging. Distribution-matching methods via score distillation provide a strong foundation, yet they rely on accurately tracking the student's changing distribution. At intermediate generation steps in few-step sampling, student-score estimation can be difficult, and commonly used estimators may describe a different distribution from the one used to update the student. F...

### 19. TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing

- 方向：底层视觉
- 作者：Ruikang Li, Zixuan Chen, Jiarui Wu, Mingde Yao, Yiyuan Zhang, Yujin Wang, et al.
- 日期：2026-11-04
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2611.06741v1

摘要：

Strong single-turn editing performance does not guarantee reliable multi-turn interaction: as edited outputs are repeatedly reused, small unintended changes can accumulate into severe visual drift. This long-term drift is often mitigated through training on multi-turn data or cross-turn rollouts, potentially altering pretrained priors, or through specialized inference-time mechanisms that are difficult to scale to foundation models. We introduce TailSteer, a final-stage training framework that improves multi-turn r...

### 20. MonoLaDN: Language-Guided DeNoising for Monocular 3D Object Detection

- 方向：底层视觉
- 作者：Kiet Dang Vu, Cao Le Minh Khoa, Nguyen Viet Tri Pham, An Nguyen Gia, Tam Le Thuc Ho, Duc Dung Nguyen
- 日期：2026-11-04
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2611.06282v1

摘要：

Monocular 3D object detection offers a low-cost route to 3D perception, but it remains fundamentally ill-posed, since depth must be inferred from a single view. Recent transformer-based detectors learn geometry purely from image features and 3D box annotations, lacking the high-level semantic priors that vision-language models (VLMs) acquire from large-scale pretraining. VLMs offer such priors, but deploying one directly as a detector is impractical due to its heavy inference cost. We propose MonoLaDN, a language-g...

### 21. BiCG-Net: Target-Specific Image Quality Assessment via Observation Modeling and In-Image Differencing

- 方向：底层视觉
- 作者：Yibu Yang, Tingqiong Cui, Liming Lei, Hao Xiong, Jun Xu, Siyuan Liu, et al.
- 日期：2026-11-04
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2611.06203v1

摘要：

We estimate the quality of a specific target region (e.g., a train body) in an image, rather than the whole image. This differs fundamentally from whole-image No-Reference Image Quality Assessment (NR-IQA): when the target occupies a small fraction of the frame, the whole-image score is dominated by background, and no public benchmark provides target-level human Mean Opinion Score (MOS). We estimate target quality via nested sampling - a sequence of patches expanding outward from the target box - and infer quality...

### 22. UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity Degradation Modeling

- 方向：底层视觉
- 作者：Jingbo Lin, Zhilu Zhang, Fan Li, Renjing Pei, Wenbo Li, Hang Xu, et al.
- 日期：2026-11-04
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2611.06042v1

摘要：

Universal image restoration aims to handle diverse degradations within a single model, but a reliable scaling strategy remains underexplored. Increasing backbone depth and width can lead to performance saturation, while degradation-aware specialization depends on accurate degradation estimation and is vulnerable to errors on out-of-distribution and real-world inputs. We propose UniRestorer++, a scalable framework based on multi-granularity degradation modeling. It progressively refines degradation groups and introd...

### 23. DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion

- 方向：底层视觉
- 作者：Yanjin Li, Bingbing Qiu, Qiang Huang, Rui Qian, Yanfeng Li, Jian Wang, et al.
- 日期：2026-11-04
- 分类：cs.CV
- 关键词：denoising
- arXiv：2611.05917v1

摘要：

Sparse attention accelerates few-step video diffusion transformers by computing a few key blocks exactly and compensating for the rest. However, existing sparse attention still faces key challenges, including identification overhead from finding critical blocks at every denoising step, suboptimal budget allocation that sets sparsity budgets uniformly or by local metrics, and cross-step error accumulation as reused masks or clusters go stale. Observing that the errors left on skipped blocks cancel each other once ev...

### 24. Dual Flow: Joint Image-Measurement Flow for Inverse Problems

- 方向：底层视觉
- 作者：Sevket Ege Yesilyurt, Figen S. Oktem
- 日期：2026-11-04
- 分类：eess.IV, cs.CV
- 关键词：denoising
- arXiv：2611.05843v1

摘要：

Existing generative model-based approaches to linear inverse problems typically use the acquired noisy measurement to condition or guide sampling in the image domain. In this work, we introduce Dual Flow, a novel joint flow model for solving linear inverse problems by jointly estimating the clean image and its corresponding noise-free measurement from the observation. Specifically, Dual Flow formulates image reconstruction and measurement denoising as a coupled estimation problem, using coupled flows in the image a...

### 25. GSCV++: Lightweight 3D Gaussian Splatting Sequence Compression via Standard Video Codecs

- 方向：视频处理
- 作者：Qi Yang, Yingzhan Xu, Kai Zhang, Li Zhang
- 日期：2026-11-03
- 分类：cs.CV
- 关键词：video compression
- arXiv：2611.05359v2

摘要：

This paper presents GSCV++, a lightweight pipeline for 3D {G}aussian {S}platting (GS) sequences {C}ompression with standard {V}ideo codecs. To meet the requirements of low-complexity and hardware compatibility from the industry, GSCV++ jointly improves preprocessing, 3D-to-2D mapping, and practical video compression configuration of GS compression. First, for preprocessing, energy-adaptive inter-frame spherical harmonic (SH) alternative current (AC) dimensionality reduction (EA-SHDR) is proposed to produces a compa...

### 26. Diffusion Plug-in Priors for Self-Supervised Ultrasound Video Restoration

- 方向：视频处理
- 作者：Chu Chen, Mingduo He, Yining Li, Yinhao Wu, Wei Tang, Yiwen Luo, et al.
- 日期：2026-11-03
- 分类：cs.CV
- 关键词：video restoration
- arXiv：2611.05206v2

摘要：

Ultrasound videos are limited by hardware-constrained spatial resolution and signal-dependent speckle, while paired low- and high-resolution acquisitions for supervised restoration are rarely available. We aim to jointly super-resolve and despeckle ultrasound videos without paired training data or network retraining. We propose UltraDiff, which uses a frozen pre-trained diffusion model (DM) as a plug-in prior and restores each frame by optimizing the latent seed of the DM sampler under a range-constrained maximum a...

### 27. VIGOR: Visual Gain Ordering for Hallucination Mitigation in Multimodal Discrete Diffusion Language Models

- 方向：底层视觉
- 作者：Junzhe Chen, Tian Qin, Eugenie Shi, Tianshu Zhang, Qiang Ju, Lijie Wen
- 日期：2026-11-03
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2611.05066v1

摘要：

Multimodal discrete diffusion language models (dLLMs) generate responses through iterative mask prediction and offer a promising alternative to autoregressive large vision-language models. However, they still suffer from hallucination, producing outputs that are plausible under language priors but insufficiently grounded in the image. We argue that hallucination in multimodal dLLMs is not only a token prediction problem, but also a premature commitment problem: during iterative denoising, some masked positions are...

### 28. An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression

- 方向：底层视觉
- 作者：Zhenghao Chen, Lebin Zhou, Zicong Chen, Naifu Xue, Jiahao Li, Bin Li, et al.
- 日期：2026-11-03
- 分类：cs.CV
- 关键词：image compression
- arXiv：2611.04960v1

摘要：

Despite decades of progress, image codecs remain difficult to adapt to diverse real-world compression scenarios for two main reasons. First, most image codecs are optimized for a specific objective and require substantial redevelopment when the compression goal changes. Second, they typically assume clean inputs, whereas sensor-captured images often contain degradations that alter rate-quality behavior. To address these challenges, we propose Practical Image Coding Agents (PICA), a multi-agent framework that adapts...

### 29. NightIQA: A Comprehensive Dataset and Benchmark for MLLM-Based Nighttime Image Quality Assessment

- 方向：底层视觉
- 作者：Yiding Tian, Jiaojiao Yi, Jiayuan Lu, Pufan Xu, Jinlin Wu, Changyuan Wen, et al.
- 日期：2026-11-03
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2611.04811v1

摘要：

Nighttime images are inherently susceptible to complex, compound degradations, making accurate quality assessment exceptionally challenging. Score-based IQA methods condense quality into a single number, lacking the multi-dimensional, language-grounded reasoning required for nighttime evaluation. Multimodal Large Language Models (MLLMs) offer a more comprehensive alternative, yet remain constrained by a critical data gap: existing real-world IQA datasets are overwhelmingly daytime-centric and often built from outda...

### 30. E2I-Flow: EEG-to-Image Reconstruction via Wavelet-Temporal Cross-Attention and Conditional Flow Matching

- 方向：底层视觉
- 作者：Haowei Pan, Hwa Hui Tew, Junn Yong Loo, Fuad Noman, Hernando Ombao, Chee-Ming Ting
- 日期：2026-11-03
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2611.04524v1

摘要：

Electroencephalography (EEG)-based visual decoding and reconstruction aims to recover visual information from non-invasive brain signals. But there are challenges due to the complex temporal-frequency characteristics of EEG signals and the difficulty of discrete denoising framework in mapping neural activity to meaningful visual representations. Here, we propose E2I-Flow, an EEG-to-image decoding and reconstruction framework that combines a novel EEG encoder for time-frequency representation learning from EEG featu...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`latest.md`
