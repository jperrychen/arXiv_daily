---
title: 2026-07-12｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-07-12｜底层视觉与视频论文速览

生成时间：2026-07-12

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜DICT: Data Injection and Contrastive Trajectory Refinement for Conditional Image Generation with Diffusion Models｜2026-07-04
2. 顶会论文｜AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding｜2026-07-09
3. 底层视觉、视频处理｜DiffCVE: Diffusion-based Compressed Video Enhancement｜2026-07-08
4. 底层视觉、视频处理｜UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation｜2026-07-06
5. 视频处理｜LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models｜2026-07-09
6. 底层视觉｜OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators｜2026-07-09
7. 底层视觉｜OpenCoF: Learning to Reason Through Video Generation｜2026-07-09
8. 底层视觉｜WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving｜2026-07-09
9. 底层视觉｜Enhancing the KidSat Model: Integrating Geographical Encoding and Data Quality Assessment for Childhood Poverty Prediction｜2026-07-09
10. 底层视觉｜LUMI: Tokenizer-Agnostic LLM-Based Lossless Image Compression｜2026-07-09
11. 底层视觉｜Unpaired Joint Distribution Modeling via Multi-Scale Image Representations｜2026-07-09
12. 底层视觉｜Leveraging Color Naming for Image Enhancement｜2026-07-09
13. 底层视觉｜LDFE: Laplacian Decoupled Feature Enhancement Block for Dual-Stream CNN-based RGB-IR Object Detection｜2026-07-09
14. 底层视觉｜Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF｜2026-07-08
15. 底层视觉｜Automatic Echocardiography Segmentation via Transition Probability Correlation for Stable Semantic Extraction｜2026-07-08
16. 底层视觉｜Stage-Aware Adaptation and Distribution Calibration for Subject-Driven Personalized Text-to-Image Generation｜2026-07-08
17. 底层视觉｜Retrieving and Refining Winning Noise Tickets for Diffusion-Based Motion Generation｜2026-07-07
18. 底层视觉｜Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement｜2026-07-07
19. 底层视觉｜Bridging Diffusion Pruning and Step Distillation with Teacher-Aligned Repair｜2026-07-07
20. 底层视觉｜Straight-Path Flow Matching for Incomplete Multi-View Clustering｜2026-07-07
21. 底层视觉｜Dynamic-in-Few-Step: Unifying Dynamic Computation and Few-Step Distillation for Efficient Video Generation｜2026-07-07
22. 底层视觉｜PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution｜2026-07-07
23. 视频处理｜EeveeDark: A Binary Neural Framework for Low-Light Video Enhancement via Event-Guided Sensor-Level Fusion｜2026-07-07
24. 底层视觉｜MoWorld: A Flash World Model｜2026-07-07
25. 底层视觉｜Tuning-Free Latent Diffusion Models for Ultrahigh-Resolution Image Editing｜2026-07-07
26. 底层视觉｜Realistic Compound-Lens Defocus Blur Synthesis｜2026-07-07
27. 底层视觉｜Clustered Codebook Quantization for 2D Gaussian-based Image Compression｜2026-07-06
28. 底层视觉｜Patch Knowledge Transfer for Efficient AI-Generated Image Quality Assessment｜2026-07-06
29. 底层视觉｜MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing｜2026-07-06
30. 底层视觉｜RADIANCE: Relative Adaptive Denoising with IP-Adapter for Novel Concept Enhancement｜2026-07-06

## 论文摘要

### 1. DICT: Data Injection and Contrastive Trajectory Refinement for Conditional Image Generation with Diffusion Models

- 方向：底层视觉
- 作者：Chunnan Shang, Xin Zhang, Zhizhong Wang, Hongwei Wang
- 日期：2026-07-04
- 分类：cs.CV
- 关键词：image super-resolution、denoising、deblurring
- arXiv：2607.03899v1

摘要：

Diffusion models have become a dominant paradigm for conditional image generation, yet existing approaches generally follow two directions: task-specific designs that can improve performance but limit generalization, and training-free loss guidance that compresses rich conditions into scalar objectives and applies stepwise guidance, leading to information bottlenecks and error accumulation along the sampling trajectory. Given the urgent need for an effective unified framework across diverse conditional image genera...

### 2. AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding

- 方向：顶会论文
- 作者：Siddharth Damodharan, Radhika Gupta, Ali Alshami, Ryan Rabinowitz, Jugal Kalita
- 日期：2026-07-09
- 分类：cs.AI, cs.CV
- 关键词：CVPR 2026、CVPR
- arXiv：2607.08745v1

摘要：

Recent advances in Vision-Language Models, Large Language Models, and Multimodal Large Language Models have improved autonomous driving tasks such as scene understanding, decision making, trajectory prediction, and visual question answering. However, evaluating whether these models can reliably reason about safety-critical incidents remains challenging. To address this gap, we present AUTOPILOT-VQA, an incident-centric visual question answering benchmark for dashcam video understanding. The dataset evaluates differ...

### 3. DiffCVE: Diffusion-based Compressed Video Enhancement

- 方向：底层视觉、视频处理
- 作者：Wenqiang Xiao, Wenzhuo Ma, Junxi Zhang, Zhenzhong Chen
- 日期：2026-07-08
- 分类：cs.CV
- 关键词：denoising、video enhancement
- arXiv：2607.07195v1

摘要：

Perceptual quality enhancement of severely compressed videos remains challenging due to complex artifact patterns and substantial information loss. Recent diffusion models have demonstrated strong generative capability for visual restoration, but directly applying them to compressed video often ignores compression degradation characteristics and may introduce structure-inconsistent hallucinations. To address this issue, this paper presents a diffusion-based compressed video enhancement method, named DiffCVE. Coding...

### 4. UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation

- 方向：底层视觉、视频处理
- 作者：Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, et al.
- 日期：2026-07-06
- 分类：cs.CV
- 关键词：denoising、video denoising
- arXiv：2607.05133v1

摘要：

World Action Models (WAMs) have shown strong potential for improving action generalization in autonomous driving by using future video prediction as dense supervision for scene dynamics and temporal causality. However, it remains unclear which architecture better transfers video-modeling benefits to trajectory generation. Existing cascaded or dual-DiT designs separate video imagination from action prediction, weakening the transfer of video-learned world dynamics to the trajectory branch: the action model may still...

### 5. LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models

- 方向：视频处理
- 作者：Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, et al.
- 日期：2026-07-09
- 分类：cs.CV
- 关键词：frame interpolation
- arXiv：2607.08770v1

摘要：

Recovering high-quality video from sparse event streams is a challenging task. Regression methods often blur textures, while existing generative models struggle with long-term stability. We propose LongE2V, a novel approach that leverages pre-trained video diffusion priors to jointly handle event-based video reconstruction, prediction, and frame interpolation. By fine-tuning a foundational video model, our approach achieves high data efficiency and superior perceptual quality. We introduce Autoregressive Unrolling...

### 6. OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators

- 方向：底层视觉
- 作者：Hongyu Liu, Chun Wang, Feng Gao, Xuanhua He, Yue Ma, Ziyu Wan, et al.
- 日期：2026-07-09
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.08766v1

摘要：

We propose OPSD-V, an on-policy self-distillation paradigm for post-training few-step autoregressive (AR) video diffusion models. Existing few-step AR video generators can produce long videos with low latency, but still suffer from error accumulation and weakened motion dynamics during long autoregressive rollout. OPSD-V reduces long-horizon degradation while preserving the original few-step inference path. The key idea is to introduce real long-video data as temporal context during training and use it to provide d...

### 7. OpenCoF: Learning to Reason Through Video Generation

- 方向：底层视觉
- 作者：Xinyan Chen, Ziyu Guo, Renrui Zhang, Dongzhi Jiang, Hongsheng Li
- 日期：2026-07-09
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2607.08763v1

摘要：

Reasoning has become a core capability for large models, especially when reliable decisions require understanding logical consequences. Recent video generation models offer a reasoning path distinct from previous Chain-of-Thought (CoT): reasoning can unfold through temporally connected frames, known as Chain-of-Frame (CoF) reasoning. However, existing video generators are primarily trained on general video corpora, still lacking diverse supervision and dedicated designs for CoF reasoning. To address this gap, we in...

### 8. WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving

- 方向：底层视觉
- 作者：Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, et al.
- 日期：2026-07-09
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2607.08375v1

摘要：

Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-VLA unifies world cog...

### 9. Enhancing the KidSat Model: Integrating Geographical Encoding and Data Quality Assessment for Childhood Poverty Prediction

- 方向：底层视觉
- 作者：Hou Hin Ip, Ka Nam Lam, Joshua Man Yu Ng, Makkunda Sharma, Seth Flaxman, Codie Gerlach-Wood, et al.
- 日期：2026-07-09
- 分类：cs.CV, stat.AP
- 关键词：image quality assessment
- arXiv：2607.08281v1

摘要：

Accurate poverty mapping using satellite imagery is often hindered by (i) noisy and sparse survey-derived supervision, (ii) image quality issues such as cloud cover and image corruption, and (iii) lack of explicit spatial structure in image-only models. Building on the KidSat framework, we develop an enhanced pipeline that improves predictive accuracy via refined data preprocessing, systematic image quality assessment, and mathematically defined geographic encoding. First, we refine the fine-tuning target matrix by...

### 10. LUMI: Tokenizer-Agnostic LLM-Based Lossless Image Compression

- 方向：底层视觉
- 作者：Chris Xing Tian, Chengkai Wu, Ziyu Wang, Rongqun Lin, Kecheng Chen, Xiandong Meng, et al.
- 日期：2026-07-09
- 分类：cs.CV
- 关键词：image compression
- arXiv：2607.08221v1

摘要：

Large language model (LLM)-based lossless image compression methods typically represent pixel data through the native text interface of a pretrained model, converting pixel values into token sequences that the LLM processes through its vocabulary head. This design shows that pretrained language models can provide probability estimates for image coding, but it also couples compression to tokenizer behavior, vocabulary-specific numeric tokens, and model-family-specific adaptation. In this paper, we present LUMI (LLM-...

### 11. Unpaired Joint Distribution Modeling via Multi-Scale Image Representations

- 方向：底层视觉
- 作者：Yihang Zou, Hui Zhang, Zuowei Shen, Chenglong Bao
- 日期：2026-07-09
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.08198v1

摘要：

This paper studies the problem of learning a joint distribution from marginal observations, which is inherently ill-posed due to the ambiguity of feasible couplings. We propose LUD-MSR, a latent-variable probabilistic framework that models the joint distribution via auxiliary representations and optimizes evidence lower bounds using only marginal data. Under mild assumptions, we establish an upper bound on the distribution approximation error. This analysis reveals a trade-off in representation learning between dom...

### 12. Leveraging Color Naming for Image Enhancement

- 方向：底层视觉
- 作者：David Serrano-Lozano, Luis Herranz, Michael S. Brown, Javier Vazquez-Corral
- 日期：2026-07-09
- 分类：cs.CV, cs.AI
- 关键词：image enhancement
- arXiv：2607.08185v1

摘要：

Enhancing images to make them visually appealing is a persistent challenge in computer vision. Many deep-learning methods train models on paired datasets to replicate expert editing styles. However, these approaches struggle with two key issues: (1) interpretability and (2) a parametrization suitable for user adjustments. To address these challenges, we present NamedCurves+, an approach inspired by the concept of Color Naming, a universal set of familiar colors widely used in software tools for intuitive editing. O...

### 13. LDFE: Laplacian Decoupled Feature Enhancement Block for Dual-Stream CNN-based RGB-IR Object Detection

- 方向：底层视觉
- 作者：Wenhao Dong, Xiaoyan Luo, Linlin Yang, Haodong Zhu, Xiaorong Shi, Guodong Guo, et al.
- 日期：2026-07-09
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2607.08076v1

摘要：

The complementary information between RGB and IR images can significantly enhance object detection performance under extreme conditions. Existing methods prefer dual-stream CNN backbones built upon YOLO for feature extraction and focus on the design of feature fusion. In this paper, we introduce the Laplacian Decoupled Feature Enhancement block (LDFE) to fuse features from different stages of the dual-stream CNN backbone. By design, LDFE simultaneously considers the characteristics of modalities and structures for...

### 14. Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF

- 方向：底层视觉
- 作者：Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay
- 日期：2026-07-08
- 分类：cs.LG, cs.AI, cs.CV
- 关键词：denoising
- arXiv：2607.07693v1

摘要：

Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that substantially improve th...

### 15. Automatic Echocardiography Segmentation via Transition Probability Correlation for Stable Semantic Extraction

- 方向：底层视觉
- 作者：Xinran Chen, Xiyuan Wang, Guangquan Zhou, Chuan Chen
- 日期：2026-07-08
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.07580v1

摘要：

While echocardiography is essential for cardiovascular diagnosis, inherent speckle noise and low signal-to-noise ratio often lead to ambiguous semantic features and fragmented boundaries. These limitations significantly hinder the segmentation accuracy of deep learning models in complex clinical cases. Moreover, temporal motion of the heart plays a critical role in recognizing anatomical structures. To address these challenges, we designed a STLSF module which comprises a window-matching-based semantic correction c...

### 16. Stage-Aware Adaptation and Distribution Calibration for Subject-Driven Personalized Text-to-Image Generation

- 方向：底层视觉
- 作者：Wenyan Xu, Alizer Wong
- 日期：2026-07-08
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.07173v1

摘要：

Subject-driven personalized text-to-image generation requires a pretrained diffusion model to acquire a specific subject from a few reference images while preserving subject identity, following novel text prompts, and maintaining sample diversity. Existing optimization-based methods instantiate subject adaptation through full fine-tuning, textual embedding optimization, or low-rank parameter updates; PaRa further constrains personalization from the perspective of parameter rank reduction. However, a uniform low-ran...

### 17. Retrieving and Refining Winning Noise Tickets for Diffusion-Based Motion Generation

- 方向：底层视觉
- 作者：Sakuya Ota, Qing Yu, Kent Fujiwara, Satoshi Ikehata, Ikuro Sato
- 日期：2026-07-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.06843v1

摘要：

Diffusion-based text-to-motion models synthesize realistic human motions but often exhibit semantic drift from the input text. Motion is inherently temporal, especially in compositional and long-duration sequences that require semantic consistency across multiple action segments and smooth kinematic transitions throughout the trajectory. We posit that the initial noise is central to this consistency: within the Gaussian noise space, certain instances, i.e. winning noise tickets, carry latent structure that biases d...

### 18. Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement

- 方向：底层视觉
- 作者：Ryuji Oi, Hikari Otsuka, Kosuke Matsushima, Yuki Ichikawa, Masato Motomura, Tatsuya Kaneko, et al.
- 日期：2026-07-07
- 分类：cs.RO, cs.CV, cs.LG
- 关键词：denoising
- arXiv：2607.06370v1

摘要：

Vision-Language-Action (VLA) models have emerged as a promising approach for generalizable robotic manipulations. In particular, flow matching-based VLA models have shown remarkable success due to their capability to generate precise and smooth action sequences and capture multimodal distributions. However, the iterative denoising process in the action head acts as a major computational bottleneck, posing a critical challenge for real-time deployment. To address this challenge, we propose ActionCache, a plug-and-pl...

### 19. Bridging Diffusion Pruning and Step Distillation with Teacher-Aligned Repair

- 方向：底层视觉
- 作者：Jincheng Ying, Li Wenlin, Minghui Xu, Yinhao Xiao
- 日期：2026-07-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.06335v1

摘要：

Diffusion models generate high-quality images, but their inference cost comes from two sources: large denoising networks and repeated denoising steps. Existing compression pipelines usually attack these costs separately. Pruning reduces the network, but most pruning methods still rely on a long post-pruning retraining stage to recover a many-step sampler. Step distillation reduces the number of denoising steps, but it usually assumes a student that can already follow the teacher well enough to receive useful distil...

### 20. Straight-Path Flow Matching for Incomplete Multi-View Clustering

- 方向：底层视觉
- 作者：Yiteng Yuan, Junyan Wang, Zheyuan Liu, Hong Jia, Lei Fan, Zhulin Tao, et al.
- 日期：2026-07-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.06281v1

摘要：

Incomplete Multi-View Clustering addresses the problem of clustering multi-modal data when certain views are missing. Recent end-to-end generative approaches leverage diffusion models to recover missing views via stochastic noise-to-data trajectories. While expressive, such mechanisms are not explicitly designed for clustering, as they initialize from cluster-agnostic noise and rely on stochastic denoising dynamics. In this work, we revisit probability path design in end-to-end generative IMVC. We introduce a flow-...

### 21. Dynamic-in-Few-Step: Unifying Dynamic Computation and Few-Step Distillation for Efficient Video Generation

- 方向：底层视觉
- 作者：Yu Cheng, Siyue Yao, Zhongang Qi, Shanyan Guan, Wei Li, Fajie Yuan
- 日期：2026-07-07
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- arXiv：2607.06631v1

摘要：

Video Diffusion Models (VDMs) have demonstrated superior generation quality but suffer from prohibitive computational costs. While recent few-step distillation techniques significantly accelerate inference, they typically enforce a static model architecture across all denoising stages, ignoring the varying computational demands inherent to different noise levels. In this work, we propose a novel post-training acceleration framework that exploits this redundancy by integrating dynamic structural sparsification direc...

### 22. PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution

- 方向：底层视觉
- 作者：Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, et al.
- 日期：2026-07-07
- 分类：cs.CV
- 关键词：image super-resolution
- arXiv：2607.06238v1

摘要：

Magnetic resonance imaging (MRI) super-resolution is vital for improving diagnostic accessibility, yet most methods treat it as a deterministic mapping from a fixed low-resolution input to a high-resolution target. This overlooks a key property of MRI acquisition physics: spatial resolution and signal-to-noise ratio (SNR) are inherently coupled, making any given low-resolution scan merely one of many possible realizations under varying acquisition trade-offs. We rethink MRI super-resolution as a physics-aware recon...

### 23. EeveeDark: A Binary Neural Framework for Low-Light Video Enhancement via Event-Guided Sensor-Level Fusion

- 方向：视频处理
- 作者：Onur Eker, Erkut Erdem, Aykut Erdem
- 日期：2026-07-07
- 分类：cs.CV
- 关键词：video enhancement
- arXiv：2607.06217v1

摘要：

Enhancing videos under extreme low-light conditions remains challenging due to the difficulty of balancing restoration quality and computational efficiency in resource-constrained settings. This paper introduces EeveeDark, a low-light video enhancement framework that combines the spatial richness of sensor-level RAW data with the temporal precision of event streams. Central to our model is a Binary Neural Network (BNN) architecture that reduces computational overhead by quantizing weights and activations while pres...

### 24. MoWorld: A Flash World Model

- 方向：底层视觉
- 作者：Team Moxin, Deyi Ji, Tianrun Chen, Xin Zhang, Jiale Yang, Qi Zhu, et al.
- 日期：2026-07-07
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.06216v1

摘要：

The future of World Models depends not only on scaling model capability, but also on scaling practicality and inference efficiency. High-frame-rate inference enables responsive perception, planning, and control in real-world autonomous systems. To this end, we present MoWorld, a cost-effective yet high-performance Flash World Model with an end-to-end framework spanning data generation, pre-training, distillation, and efficient inference, enabling up to 50 FPS real-time interaction with cinematic visual quality with...

### 25. Tuning-Free Latent Diffusion Models for Ultrahigh-Resolution Image Editing

- 方向：底层视觉
- 作者：Wanglong Lu, Lingming Su, Kaijie Shi, Minglun Gong, Xiaogang Jin, Hanli Zhao, et al.
- 日期：2026-07-07
- 分类：cs.CV, cs.MM
- 关键词：denoising
- arXiv：2607.06136v1

摘要：

Recent diffusion-based generative models have shown impressive performance in image generation and editing. However, due to memory limitations and the high cost of collecting high-resolution training images, existing methods are typically restricted to inputs with linear resolutions below 1K. In contrast, photos captured by modern mobile devices often reach linear resolutions up to 8K, revealing a significant gap between current capabilities and real-world demands. Simply upscaling low-resolution edited results oft...

### 26. Realistic Compound-Lens Defocus Blur Synthesis

- 方向：底层视觉
- 作者：Yunkyu Lee, Woohyeok Kim, Sunghyun Cho
- 日期：2026-07-07
- 分类：cs.CV
- 关键词：deblurring
- arXiv：2607.05837v1

摘要：

Defocus blur degrades fine image structures and limits visual perception, which can adversely affect downstream vision tasks. Although recent deep learning deblurring methods have achieved strong performance, their effectiveness depends on training data and often degrades across cameras and lenses due to limited optical diversity and realism in existing datasets. In this paper, we propose a pipeline for synthesizing realistic defocus deblurring datasets for diverse compound lenses. It integrates efficient wave-opti...

### 27. Clustered Codebook Quantization for 2D Gaussian-based Image Compression

- 方向：底层视觉
- 作者：Runze Cheng, Yicheng Zhan, Josef Spjut, Kaan Akşit
- 日期：2026-07-06
- 分类：cs.CV, cs.GR
- 关键词：image compression
- arXiv：2607.05667v1

摘要：

Gaussian-based image representations effectively model image content using compact parametric primitives while preserving high visual fidelity, yet storing a large number of floating-point parameters per primitive degrades rate-distortion efficiency at higher fidelity targets. To improve the rate-distortion performance in Gaussian representation, we present our Cluster-Guided Vector Quantization (CGVQ), a Gaussian primitive based image compression method. Our key idea is to partition Gaussian parameters further int...

### 28. Patch Knowledge Transfer for Efficient AI-Generated Image Quality Assessment

- 方向：底层视觉
- 作者：Jiquan Yuan
- 日期：2026-07-06
- 分类：cs.CV
- 关键词：image quality assessment
- arXiv：2607.05605v1

摘要：

With the rapid advancement of image generation technologies, perceptual quality assessment of AI-generated images has emerged as a crucial research direction in computer vision. The core challenge of this task lies in achieving efficient quality assessment for massive generated images. Current mainstream approaches exhibit two key limitations: 1) Methods employing complex feature extraction strategies, while improving performance, incur prohibitive computational costs that hinder real-time inference; 2) Simple imag...

### 29. MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing

- 方向：底层视觉
- 作者：Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim
- 日期：2026-07-06
- 分类：cs.CV, cs.GR
- 关键词：denoising
- arXiv：2607.05376v1

摘要：

Recent advances in video diffusion models have enabled either long single-view generation through temporal autoregression, or short multi-view synthesis through bidirectional attention. However, generating long, multi-view consistent videos of dynamic scenes remains unsolved. In this work, we present MV-Forcing, a framework that composes temporal and view-wise autoregression within a single diffusion model by introducing a 4D geometric bridge between sequentially generated views. Our key insight is that an autoregr...

### 30. RADIANCE: Relative Adaptive Denoising with IP-Adapter for Novel Concept Enhancement

- 方向：底层视觉
- 作者：Zi-Xiang Ni, Bo-Lun Huang, Teng-Fang Hsiao, Bo-Kai Ruan, Hong-Han Shuai
- 日期：2026-07-06
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.05088v1

摘要：

Text-to-image (T2I) diffusion models have achieved striking progress but still struggle to synthesize rare concepts involving unusual attribute-object pairings, often resulting in concept omission or semantic drift where a dominant entity overwhelms the generation. Tracing these failures to a lack of compositional balance during the denoising trajectory, we propose RADIANCE, a training-free framework that treats inference as a closed-loop feedback process. RADIANCE augments pretrained backbones with three modular c...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-07-12-low-level-vision-video-papers.md`
