---
title: 2026-10-18｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-10-18｜底层视觉与视频论文速览

生成时间：2026-10-18

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Denoising Textures is a Different Ballgame Altogether!｜2026-10-15
2. 底层视觉、视频处理｜FilterFusion: Prior-Guided Adaptive Filter Fusion for Efficient Video Denoising｜2026-10-15
3. 底层视觉、视频处理｜OLiVES: An Outdoor Low-Light Video Benchmark for Enhancement and Segmentation｜2026-10-14
4. 底层视觉｜$\mathrm{S}^3$-PnP: Plug-and-Play Denoising for Scientific Imaging with Self-Supervised Score Priors｜2026-10-13
5. 底层视觉｜Gen4P: Video Generators are 4D Perceivers｜2026-10-15
6. 底层视觉｜Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation｜2026-10-15
7. 底层视觉｜Speculative Forcing for Efficient Autoregressive Video Generation｜2026-10-15
8. 底层视觉｜Velox: Spatial Memory Makes World Models Efficient｜2026-10-15
9. 底层视觉｜Routing Policy Optimization for Online Diffusion Reinforcement Learning｜2026-10-15
10. 底层视觉｜WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression｜2026-10-15
11. 底层视觉｜VesperMUSE: Multi-Modal Fusion Vision Transformer for Image Semantic Segmentation Under Diverse Light Conditions｜2026-10-15
12. 视频处理｜Beyond Source Prompts: Towards Visually Grounded AI-Generated Video Quality Assessment｜2026-10-15
13. 底层视觉｜ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space｜2026-10-15
14. 底层视觉｜FocusOPD: Structure-Guided On-Policy Distillation for Diffusion Models｜2026-10-15
15. 底层视觉｜Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search｜2026-10-15
16. 底层视觉｜EigDiff: Eigensample Diffusion - or how to significantly reduce training dataset size with marginal performance variation?｜2026-10-14
17. 底层视觉｜Temporal Specification Guidance for Text-to-Video Generation｜2026-10-14
18. 底层视觉｜VITAL: From Visual Motion to Precise Action｜2026-10-14
19. 底层视觉｜Look Before You Restore: Learning to Predict Before Acting for Agentic Image Restoration｜2026-10-14
20. 底层视觉｜Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance｜2026-10-14
21. 底层视觉｜Complementary Future Token Pruning for World Action Models｜2026-10-14
22. 底层视觉｜BluePixel: Toward Native 4K Agentic Image Editing｜2026-10-14
23. 底层视觉｜Physics-Shaped, Not Physical: Auditing Physics-Guided Underwater Image Restoration｜2026-10-14
24. 底层视觉｜SaTPO: Text-to-Image Safety Alignment via Transition Preference Optimization｜2026-10-14
25. 底层视觉｜LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts｜2026-10-13
26. 底层视觉｜Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs｜2026-10-13
27. 底层视觉｜PixelMoE: Scaling Pixel-Space Diffusion with LLM-Style Mixture-of-Experts｜2026-10-13
28. 底层视觉｜Recasting DiT for Extreme Image Compression with Hierarchical Visual Priors｜2026-10-13
29. 底层视觉｜Denoise X: Self-Supervised U-Net for Quantum Mottle Suppression in Chest Radiography｜2026-10-13
30. 视频处理｜MFVSR: A Multi-Style and Fine-Grained Benchmark for Video Subtitle Removal｜2026-10-13

## 论文摘要

### 1. Denoising Textures is a Different Ballgame Altogether!

- 方向：底层视觉
- 作者：Saptarshi Mandal, Oindrila Haldar, Chirayata Bhattacharya, Chandra Sekhar Seelamantula, Zhiwei Xu, Thrasyvoulos N. Pappas, et al.
- 日期：2026-10-15
- 分类：eess.IV, cs.CV
- 关键词：image denoising、denoising
- arXiv：2610.22258v1

摘要：

The human brain effortlessly deciphers colors and textures from visual stimuli and reconstructs the world around us, yet preserving such details remains challenging in image denoising. While significant progress has been made in generic image denoising, the problem of texture denoising has remained relatively under-explored. Fine details, such as intricate patterns and repetitive structures, often suffer from over-smoothing even in deep learning based approaches for denoising. In this paper, we analyze the behavior...

### 2. FilterFusion: Prior-Guided Adaptive Filter Fusion for Efficient Video Denoising

- 方向：底层视觉、视频处理
- 作者：Wenlong Yang, Weihang Yuan, Canran Jin, Jiahao Li, Henrik Turbell, Lifeng Sun
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：denoising、video denoising
- arXiv：2610.21505v1

摘要：

Real-world video denoising for communication systems must handle mixed degradations such as sensor noise, compression artifacts, and motion-induced inconsistency while remaining deployable under tight latency budgets. Purely deep models often achieve high accuracy but come with significant computational cost, whereas classical filters are robust and efficient but insufficiently adaptive. We present FilterFusion, a prior-guided multi-frame denoising framework that combines temporally-aware learned features with an i...

### 3. OLiVES: An Outdoor Low-Light Video Benchmark for Enhancement and Segmentation

- 方向：底层视觉、视频处理
- 作者：Yini Li, Joanne Lin, David Blackham, David Bull, Nantheera Anantrasirichai
- 日期：2026-10-14
- 分类：cs.CV
- 关键词：low-light enhancement、video enhancement
- arXiv：2610.20501v1

摘要：

Low-light video processing remains an underexplored problem in computer vision, primarily due to the scarcity of high-quality ground-truth data. Existing public datasets exhibit several limitations, including restricted motion diversity, limited scene coverage, weak degradations, reliance on auxiliary modalities such as event data, and misalignment between low-light inputs and ground truth. Furthermore, current datasets typically address either low-light enhancement or scene understanding, whereas these tasks shoul...

### 4. $\mathrm{S}^3$-PnP: Plug-and-Play Denoising for Scientific Imaging with Self-Supervised Score Priors

- 方向：底层视觉
- 作者：Yukun Cui, Jiangshe Zhang, Shuang Xu, Lilun Deng, Haowen Bai, Tao Feng, et al.
- 日期：2026-10-13
- 分类：cs.CV
- 关键词：image restoration、denoising
- arXiv：2610.18458v1

摘要：

Modern image restoration methods increasingly rely on large-scale supervised training, yet clean targets are often prohibitively difficult to obtain in scientific imaging modalities such as hyperspectral imaging (HSI) and magnetic resonance imaging (MRI). Plug-and-play ADMM (PnP-ADMM) with pretrained diffusion priors offers a promising alternative, but the learned prior distribution can mismatch both the target scientific image distribution and the distribution of ADMM denoiser inputs induced by dual feedback. To m...

### 5. Gen4P: Video Generators are 4D Perceivers

- 方向：底层视觉
- 作者：Yitong Xia, Zeren Jiang, Chuanxia Zheng
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.22371v1

摘要：

We introduce Gen4P, a unified framework for recovering 4D geometry and motion from monocular video. We show that a pretrained video generator can be repurposed into a feed-forward 4D perceiver without iterative denoising. Building on on-demand querying, Gen4P processes clean video latents in a single encoder pass and predicts the requested 4D attributes through a lightweight cross-attention decoder. The on-demand query formulation enables flexible spatial sampling, and our proposed continuous-time queries further p...

### 6. Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation

- 方向：底层视觉
- 作者：SeungJu Cha, Ye-Chan Kim, HyunGee Kim, Sungho Koh, Dong-Jin Kim
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.22370v1

摘要：

Token merging has emerged as an effective training-free strategy for accelerating diffusion models by reducing redundant token computation while minimizing generation degradation. A key challenge is determining which tokens can be safely merged and which should be preserved for subsequent computation. Existing method addresses this by preserving prompt-aligned foreground regions, thereby protecting semantically relevant structures. However, this text-relevance criterion overlooks background objects, local details t...

### 7. Speculative Forcing for Efficient Autoregressive Video Generation

- 方向：底层视觉
- 作者：Hyunwook Choi, Seungryong Kim, Dongyoon Han, Sangdoo Yun
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.22347v1

摘要：

Few-step autoregressive video generators enable streaming generation, yet they run every token through the final denoising step, regardless of how much refinement it needs. We find this uniform computation is often unnecessary: many tokens already closely match their eventual full-step outputs in the initial steps, while others require refinement until the end. We introduce Speculative Forcing, a framework that treats intermediate clean estimates as drafts and predicts when individual tokens can be safely accepted...

### 8. Velox: Spatial Memory Makes World Models Efficient

- 方向：底层视觉
- 作者：Qiuhong Shen, Shizun Wang, Xinchao Wang
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.22311v1

摘要：

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation. Such interaction requires responsive generation, yet coherent rollouts must retain visual memory of what has already been generated. Chunked video diffusion models usually keep this context in growing KV caches, so later chunks become progressively slower. To address this bottleneck, we introduce Velox, a training-free attention router for region-level context selection using fru...

### 9. Routing Policy Optimization for Online Diffusion Reinforcement Learning

- 方向：底层视觉
- 作者：Qiuhong Shen, Yiding Yang, Yuxin Zhang, Xinwei Huang, Minxuan Lin, Bo Liu, et al.
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.22282v1

摘要：

Reinforcement learning can align visual generators with reward signals beyond their pretraining objectives, but existing score-function methods typically introduce stochasticity by perturbing the reverse denoising trajectory, leading to costly rollout-based optimization. We instead ask whether stochastic exploration can be introduced inside the generator while preserving its original sampler. Routing Policy Optimization (RPO) answers this question by turning attention routing into a stochastic exploration action. A...

### 10. WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression

- 方向：底层视觉
- 作者：Yue Yu, Bowei Kang, Changsheng Gao, Dong Liu, Xiaoyan Sun
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：image compression
- arXiv：2610.22232v1

摘要：

Lossless image compression fundamentally relies on accurate entropy modeling, driving a recent shift toward large language model (LLM)-based methods. However, existing approaches mainly emphasize the modeling capacity of LLMs while directly serializing images into pixel or residual sequences, leaving heterogeneous signal patterns entangled within a single prediction stream. In this paper, we argue that effective entropy modeling depends not only on model capacity, but also on the predictability of the input represe...

### 11. VesperMUSE: Multi-Modal Fusion Vision Transformer for Image Semantic Segmentation Under Diverse Light Conditions

- 方向：底层视觉
- 作者：Raul Balmez
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2610.21990v1

摘要：

Semantic segmentation is critical for the reliable navigation and scene understanding of autonomous systems, yet its performance degrades severely in low-light environments due to noise, artifacts, colour distortion, and the loss of structural details. To address this challenge, this work introduces VesperMUSE, a unified multi-modal framework designed to achieve robust image semantic segmentation across diverse illumination conditions. The architecture addresses the light deficiency problem on multiple levels: prop...

### 12. Beyond Source Prompts: Towards Visually Grounded AI-Generated Video Quality Assessment

- 方向：视频处理
- 作者：Kehao Zhou, Yixuan Li, Yuxuan Jiang, Fan Zhang
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：video quality assessment
- arXiv：2610.21758v1

摘要：

Recent advances in generative artificial intelligence have accelerated video generation technologies. However, AI-generated videos (AIGVs) remain susceptible to various distortions, highlighting the need for dedicated video quality assessment methods. Content semantics play an important role in AIGV quality assessment, with source prompts typically used as textual references. However, these prompts may not accurately reflect the generated video content, resulting in a discrepancy between the intended textual descri...

### 13. ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space

- 方向：底层视觉
- 作者：Minkyu Kim, Baekseung Kim, Junhoo Lee, Jangho Kim, Nojun Kwak
- 日期：2026-10-15
- 分类：cs.CV, cs.LG
- 关键词：denoising
- arXiv：2610.21433v1

摘要：

Diffusion models achieve high-quality image generation but remain computationally expensive due to iterative denoising across many timesteps. Existing acceleration methods mainly reduce per-sample latency, but gains along this axis are becoming saturated. We instead explore an orthogonal throughput-oriented direction by processing multiple samples within a single denoising evaluation. To this end, we propose ManiFusion, a backbone-agnostic framework for multi-sample generation through fused-space computation. ManiF...

### 14. FocusOPD: Structure-Guided On-Policy Distillation for Diffusion Models

- 方向：底层视觉
- 作者：Xinrui Lin, Shumin Wang, Suqi Song, Fan Li, Yanyong Zhang
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.21250v1

摘要：

Multi-teacher on-policy distillation enables rectified-flow models with diffusion-transformer architectures to combine task-specific capabilities within a single student. However, matching model outputs does not guarantee that their internal representations are aligned, and it remains unclear where and when additional feature supervision is most useful. We analyze the teacher-student feature mismatch across Transformer blocks and denoising timesteps, and find that the mismatch is concentrated in deeper Transformer...

### 15. Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search

- 方向：底层视觉
- 作者：Yun Dai, Yuyun Chen, Jiarui Wen, Huiping Zhuang, Cen Chen, Ziqian Zeng
- 日期：2026-10-15
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.21129v1

摘要：

Diffusion Transformers (DiTs) dominate video generation but suffer from high inference cost due to the quadratic complexity of self-attention. Sparse attention mitigates this by skipping unnecessary computation in the attention matrix, but existing methods apply a fixed sparsity ratio throughout denoising and struggle to accurately determine which computations to skip. To address these limitations, we analyze attention dynamics through attention entropy and mean attention distance, and find that attention becomes i...

### 16. EigDiff: Eigensample Diffusion - or how to significantly reduce training dataset size with marginal performance variation?

- 方向：底层视觉
- 作者：Andrei Jarca, Vlad Hondru, Florinel-Alin Croitoru, Radu Tudor Ionescu
- 日期：2026-10-14
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- arXiv：2610.20999v1

摘要：

Diffusion models are notoriously expensive to train, requiring large-scale datasets to learn how to gradually reverse the noise from images over multiple small denoising steps. Current approaches focus on distilling the number of diffusion steps, neglecting potential redundancies of the training data. In this paper, we explore the potential of harnessing eigensamples to train diffusion models on significantly smaller datasets, while preserving model performance. To mitigate the sensitivity to affine transformations...

### 17. Temporal Specification Guidance for Text-to-Video Generation

- 方向：底层视觉
- 作者：Avishree Khare, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Rajeev Alur
- 日期：2026-10-14
- 分类：cs.AI, cs.CV
- 关键词：denoising
- arXiv：2610.20822v1

摘要：

Text-to-video models often generate the visual concepts requested in natural language prompts but fail to satisfy their intended ordering, timing, and persistence requirements. We propose representing these requirements as specifications in a formal Temporal Logic, and introduce Temporal Specification Guidance (TSG), a training-free inference-time framework that turns temporal specifications into executable objectives for guiding video generation during sampling. TSG scores traces of visual concept evidence using d...

### 18. VITAL: From Visual Motion to Precise Action

- 方向：底层视觉
- 作者：Ao Liang, Youquan Liu, Mingxiao Li, Wei Chow, Lingdong Kong, Yue Liao, et al.
- 日期：2026-10-14
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.20604v1

摘要：

World-action models aim to turn visual anticipation into driving decisions, yet typically train action experts on trajectory representations defined independently of visual dynamics. This motivates deriving action targets directly from visual motion. We first examine a simpler setting in which trajectories are reconstructed from recorded future images. Even without the need for future prediction, reconstruction captures the dominant maneuver but leaves centimeter-scale errors. We therefore introduce VITAL (Vision-I...

### 19. Look Before You Restore: Learning to Predict Before Acting for Agentic Image Restoration

- 方向：底层视觉
- 作者：Xu Zhang, Jun Wan, Lefei Zhang, Liangpei Zhang
- 日期：2026-10-14
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2610.20384v1

摘要：

Agents for mixed-degradation image restoration typically learn what a tool does to an image only after running it: failed calls waste computation and harmful outputs go unnoticed until too late. We propose PreActIR, an agentic restoration framework that predicts tool consequences before execution. For each candidate tool, a tool-conditioned world model forecasts changes in residual degradation, image quality, and fidelity, together with the risk of harm and the uncertainty of the prediction. The agent executes the...

### 20. Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance

- 方向：底层视觉
- 作者：Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao, Alex Jinpeng Wang
- 日期：2026-10-14
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.20220v1

摘要：

Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models. Today's dominant approach distills a bidirectional diffusion model into a causal few-step student, but existing pipelines make this conversion prohibitively expensive, requiring offline Probability Flow ODE} (PF-ODE) trajectories that cost tens of thousands of GPU-hours and terabytes of storage. We show it can be made dramatically more efficient. Pushing this efficiency to its extreme, we reduce trajecto...

### 21. Complementary Future Token Pruning for World Action Models

- 方向：底层视觉
- 作者：Baekseung Kim, Junhoo Lee, Sohyeon Hong, Suhyun Jeon, Minkyu Kim, Seungyeon Kim, et al.
- 日期：2026-10-14
- 分类：cs.RO, cs.CV
- 关键词：denoising
- arXiv：2610.19957v1

摘要：

World action models (WAMs) jointly predict future visual states and robot actions, but processing dense future-frame tokens incurs substantial inference latency. We propose CF-Prune, a training-free framework for pruning future-frame tokens in pretrained WAMs. Our key insight is that future visual predictions support action generation and therefore need not preserve every visual detail required for high-fidelity video synthesis. CF-Prune combines instruction and action attention to identify task-relevant tokens dur...

### 22. BluePixel: Toward Native 4K Agentic Image Editing

- 方向：底层视觉
- 作者：Shanyan Guan, Shiyu Li, Xin Li, Zhizhou Chen, Yunzhe Xu, Yuehao Liu, et al.
- 日期：2026-10-14
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.19882v1

摘要：

Instruction-driven image editing has reached native 4K, yet how such editors are trained remains undisclosed, and pretraining one from scratch is beyond most teams. The task itself compounds the difficulty: a single end-to-end editor cannot make precise parametric adjustments, match specialized experts, or interpret the vague instructions users actually write. We argue that 4K editing is a system problem rather than a single-model problem, and present BluePixel, which couples a native-4K editing model with an agent...

### 23. Physics-Shaped, Not Physical: Auditing Physics-Guided Underwater Image Restoration

- 方向：底层视觉
- 作者：Mochamad Rizal Fauzan, Irgi Surya
- 日期：2026-10-14
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2610.19763v1

摘要：

Physics-guided networks for underwater image restoration predict transmission and backscatter and invert the image-formation model, yet rarely test whether this physics does any work. We audit one representative design, PhysGuide-Net, with four controlled experiments: five-seed ablations on UIEB with zero-shot evaluation on the complete LSUI (4279 pairs) and AUIED3K (3000 pairs) sets; a data-efficiency study with a capacity-matched control that removes the formation model; and a validation of the predicted maps aga...

### 24. SaTPO: Text-to-Image Safety Alignment via Transition Preference Optimization

- 方向：底层视觉
- 作者：Ziyi Fang, Jingzhi Li, Xiaojun Jia, Xingxing Wei, Wenqi Ren, Haijun Zhang
- 日期：2026-10-14
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.19563v1

摘要：

Safety alignment of text-to-image diffusion models aims to suppress harmful content without compromising useful generation capabilities. However, preferences over completed images compress multidimensional generation factors into a coarse signal, potentially driving changes beyond those required for safety. To address this, we propose Safety Transition Preference Optimization (SaTPO), which enforces step-wise alignment during denoising. SaTPO leverages the insight that an unsafe prompt and its safe rewrite naturall...

### 25. LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts

- 方向：底层视觉
- 作者：Wenxuan Guo, Yingping Liang, Zhaoguo Wang, Ziyuan Li, Angyuan Ma, Zhenyu Wu, et al.
- 日期：2026-10-13
- 分类：cs.RO, cs.CV
- 关键词：denoising
- arXiv：2610.18873v2

摘要：

Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment. Real-world rollouts contain successes, suboptimal behavior, and failures: imitating every recorded action can reinforce poor behavior, while filtering out failures discards evidence of physical interactions and their consequences. We introduce LoopWAM, a closed-loop world-action model that learns directly from this full quality spectrum, using rollouts from both itself and other deployed policies. Source-depend...

### 26. Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs

- 方向：底层视觉
- 作者：Aimon Rahman, Joymallya Chakraborty, Vidit Bansal, Abhishek Dan
- 日期：2026-10-13
- 分类：cs.CV
- 关键词：image compression
- arXiv：2610.18858v1

摘要：

Multimodal large language models have advanced rapidly, but most remain optimized for single-image inputs. Multi-image reasoning is costly because each image adds many visual tokens, increasing encoding and attention demands. Existing techniques that address the above issue, including visual token pruning, token merging, visual token compression, learned resampling, hierarchical compression, retrieval-augmented visual reasoning, and memory-based architectures, have largely been designed for single-image scenarios,...

### 27. PixelMoE: Scaling Pixel-Space Diffusion with LLM-Style Mixture-of-Experts

- 方向：底层视觉
- 作者：Ruixiao Dong, Jianmin Bao, Bozhi Luan, Zijie Meng, Xin Tao, Pengfei Wan, et al.
- 日期：2026-10-13
- 分类：cs.CV
- 关键词：denoising
- arXiv：2610.18857v1

摘要：

Pixel-space diffusion models provide an appealing alternative to latent-space diffusion models by directly modeling raw images without relying on a learned tokenizer. However, scaling pixel-space models has predominantly followed dense strategies, tightly coupling model capacity with active computation. In this work, we show that standard LLM-style Mixture-of-Experts (MoE) architectures can be effectively transferred to pixel-space diffusion. Building on this finding, we introduce PixelMoE, a pixel-space generative...

### 28. Recasting DiT for Extreme Image Compression with Hierarchical Visual Priors

- 方向：底层视觉
- 作者：Yunuo Chen, Jingnan Gao, Bing He, Jinjing Zhao, Chuqin Zhou, Xiaoyue Ling, et al.
- 日期：2026-10-13
- 分类：cs.CV
- 关键词：image compression
- arXiv：2610.18607v1

摘要：

Pretrained diffusion models provide powerful generative priors for extreme image compression, but their stochastic, iterative generation processes are not designed to decode compressed representations directly. We present PrismCodec, which recasts a pretrained Diffusion Transformer (DiT) as a bitstream-grounded one-step generative decoder. PrismCodec uses the decoded representation in two complementary roles: a projected codec state defines the starting state for generation, while hierarchical visual priors derived...

### 29. Denoise X: Self-Supervised U-Net for Quantum Mottle Suppression in Chest Radiography

- 方向：底层视觉
- 作者：Parth Giramkar, Aryan Patle, Vanita Kshirsagar
- 日期：2026-10-13
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2610.18556v1

摘要：

Deep learning for medical image restoration is often constrained by the need for paired training data. Acquiring perfectly registered clean-noisy radiographs in vivo is impractical due to patient motion and radiation-dose limits. To address this, we employ a self-supervised Noise2Noise paradigm that trains on independently corrupted observations without paired clean images. We propose Denoise X, a lightweight self-supervised U-Net model (7.79M parameters) for suppressing quantum mottle and electronic readout noise...

### 30. MFVSR: A Multi-Style and Fine-Grained Benchmark for Video Subtitle Removal

- 方向：视频处理
- 作者：Xiyan Huang, Qingdong He, Peng Tang, Bo Yin, Chaoyi Wang, Xiaobin Hu
- 日期：2026-10-13
- 分类：cs.CV
- 关键词：video restoration
- arXiv：2610.18461v1

摘要：

Video subtitle removal (VSR) is an important video restoration task, yet existing evaluation remains limited by low-resolution datasets, fragmented test sets, and generic video-inpainting protocols that fail to adequately capture localized restoration errors, unintended modifications, temporal instability, and incomplete outputs. In this paper, we introduce MFVSR, a large-scale multi-style benchmark for fine-grained and reliability-aware video subtitle removal evaluation. MFVSR distinguishes itself through three ke...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-10-18-low-level-vision-video-papers.md`
