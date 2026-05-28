---
title: 本周底层视觉与视频处理论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 本周底层视觉与视频处理论文速览

生成时间：2026-05-29

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

| # | 方向 | 标题 | 日期 |
|---|---|---|---|
| 1 | 底层视觉 | [Internally Referenced Low-Light Enhancement](#1) | 2026-05-27 |
| 2 | 顶会论文 | [Bridging the Generalization Gap in Adverse Weather Segmentation: A Training Recipe Perspective](#2) | 2026-05-27 |
| 3 | 顶会论文 | [Reflective Dialogue between Teacher and Solver Agents for Video Question Answering](#3) | 2026-05-27 |
| 4 | 底层视觉、视频处理 | [StreamChar: Long-Horizon Streaming Character Audio-Video Generation with Decoupled Orchestration](#4) | 2026-05-25 |
| 5 | 底层视觉、视频处理 | [Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation](#5) | 2026-05-24 |
| 6 | 顶会论文 | [From Affect to Complex Behavior: Advancing Multimodal Human-Centered AI at the 10th ABAW Workshop & Competition](#6) | 2026-05-24 |
| 7 | 底层视觉 | [Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling](#7) | 2026-05-27 |
| 8 | 底层视觉 | [Diffusion Large Language Models for Visual Speech Recognition](#8) | 2026-05-27 |
| 9 | 底层视觉 | [Inpainting-Style Conditional Diffusion for Multivariable Time Series Forecasting](#9) | 2026-05-27 |
| 10 | 底层视觉 | [DebFilter: Eradicating Biases Stashed in Value](#10) | 2026-05-27 |
| 11 | 底层视觉 | [Residualized Temporal Sparse Autoencoders for Interpreting Diffusion Models](#11) | 2026-05-27 |
| 12 | 底层视觉 | [Explicit Critic Guidance for Aligning Diffusion Models](#12) | 2026-05-26 |
| 13 | 底层视觉 | [Asynchronous Remote Sensing Time-Series Fusion for Cloud Removal and Anytime Reconstruction](#13) | 2026-05-26 |
| 14 | 底层视觉 | [PARE: Pruning and Adaptive Routing for Efficient Video Generation](#14) | 2026-05-26 |
| 15 | 底层视觉 | [SoftCap: Soft-Budget Control for Diffusion Transformer Acceleration](#15) | 2026-05-26 |
| 16 | 视频处理 | [NeR-SC: Adapting Neural Video Representation to Screen Content](#16) | 2026-05-26 |
| 17 | 底层视觉 | [Timestep-Aware SVDQuant-GPTQ for W4A4 Quantization of Wan2.2-I2V](#17) | 2026-05-26 |
| 18 | 底层视觉 | [SIMPC: Learning Self-Induced Mirror-Point Consistency for Unsupervised Point Cloud Denoising](#18) | 2026-05-26 |
| 19 | 底层视觉 | [Scheduled Style Injection: Expanding the Style-Content Pareto Frontier in Training-Free Diffusion-based Style Transfer](#19) | 2026-05-26 |
| 20 | 底层视觉 | [Beyond Pairwise Preferences: Listwise Reward-Aware Alignment for Diffusion Models](#20) | 2026-05-26 |
| 21 | 底层视觉 | [D$^2$Turb: Depth-Aware Simulation and Decoupled Learning for Single-Frame Atmospheric Turbulence Mitigation](#21) | 2026-05-25 |
| 22 | 底层视觉 | [Geometry-Aware Representation Denoising for Robust Multi-view 3D Reconstruction](#22) | 2026-05-25 |
| 23 | 底层视觉 | [Squeezing Capacity from Multimodal Large Language Models for Subject-driven Generation](#23) | 2026-05-25 |
| 24 | 底层视觉 | [On-Policy Adversarial Flow Distillation for Autoregressive Video Generation](#24) | 2026-05-25 |
| 25 | 底层视觉 | [A Multimodal 3D Foundation Model for Light Sheet Fluorescence Microscopy Enables Few-Shot Segmentation, Classification, and Deblurring](#25) | 2026-05-25 |
| 26 | 视频处理 | [How Accurate are Video Quality Models for Diffusion-Based Video Super-Resolution?](#26) | 2026-05-25 |
| 27 | 底层视觉 | [SP-MoMamba: Superpixel-driven Mixture of State Space Experts for Efficient Image Super-Resolution](#27) | 2026-05-25 |
| 28 | 底层视觉 | [Concept Unlearning via Cross-Attention Activation Projection for Diffusion Models](#28) | 2026-05-25 |
| 29 | 底层视觉 | [AI-T2I: Aggregating-and-Isolating Cross-Attention to Diffusion Models for Text-to-Image Synthesis](#29) | 2026-05-25 |
| 30 | 底层视觉 | [ControlLight: Towards Controllable, Consistent, and Generalizable Low-Light Enhancement](#30) | 2026-05-25 |

## 论文摘要

### 1. Internally Referenced Low-Light Enhancement

- 方向：底层视觉
- 作者：Peiyuan He, Hainuo Wang, Hengxing Liu, Mingjia Li, Xiaojie Guo
- 日期：2026-05-27
- 分类：cs.CV
- 关键词：denoising、low-light enhancement、image enhancement
- 链接：[Abstract](http://arxiv.org/abs/2605.28605v1) / [PDF](http://arxiv.org/pdf/2605.28605v1)

摘要：

> Self-supervised low-light image enhancement (LLIE) is highly appealing as it eliminates the reliance on external paired data. However, the lack of external references causes networks to struggle with decoupling entangled illumination, delicate textures, and amplified noise. To resolve this challenge, we propose an Internally Referenced LLIE framework that extracts reliable physical and structural references from the degraded input image itself. First, we introduce a local exposure-simulated scheme to extract a low-frequency pseudo ground-truth. This serves as an internal physical reference to guide global illumination estimation and correct color casts. Second, we propose a dual-domain preservation strategy with spatial and spectral constraints to construct internal structural references. Specifically, an Illumination-Aligned Perceptual loss preserves global structures under illumination shifts, while a Shift-Invariant Spectral Correlation loss captures fine-grained local structures and suppresses high-frequency noise. Finally, we propose a Gain-Adaptive Feature Modulation (GAFM) mechanism to address highly spatially-variant residual noise. By transforming the self-estimated illumination map into an internal spatial gain prior, GAFM dynamically guides a blind-spot network for spatially-aware denoising. Extensive experiments demonstrate that our method achieves state-of-the-art performance, delivering superior noise suppression and textural fidelity. Code will be publicly released at https://visonj.github.io/IRLE/.

### 2. Bridging the Generalization Gap in Adverse Weather Segmentation: A Training Recipe Perspective

- 方向：顶会论文
- 作者：Cong Xu, Pu Luo, Yumei Li, Boyou Xue
- 日期：2026-05-27
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- 链接：[Abstract](http://arxiv.org/abs/2605.27962v1) / [PDF](http://arxiv.org/pdf/2605.27962v1)

摘要：

> This paper describes our approach for the 8th UG2+ Workshop (CVPR 2026) Track~2, which targets semantic segmentation of outdoor scenes degraded by five weather conditions: blur, darkness, snow, haze, and glare. A central challenge we observe is a severe generalization gap -- models that perform well on the validation set often collapse on the test set. For instance, SegFormer-B5 drops 16.1 mIoU points from validation to test, suggesting that model capacity alone is insufficient for robustness. We investigate whether a carefully designed training recipe, rather than architectural complexity, can address this gap. Starting from a pre-trained SegMAN-S backbone, we systematically study the effects of domain-adaptive fine-tuning, multi-source data mixing, scene-balanced sampling, and synthetic degradation augmentation. Our final system achieves 59.9\% mIoU on the official test set while maintaining a validation-test gap of only 6.5 points -- less than half that of larger models. We analyze negative results from architectural modifications, loss function variants, and model scaling to provide practical insights for weather-robust segmentation under limited data.

### 3. Reflective Dialogue between Teacher and Solver Agents for Video Question Answering

- 方向：顶会论文
- 作者：Takuya Murakawa, Toru Tamaki
- 日期：2026-05-27
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- 链接：[Abstract](http://arxiv.org/abs/2605.27885v1) / [PDF](http://arxiv.org/pdf/2605.27885v1)

摘要：

> Various approaches have been proposed to adapt Vision-Language Models (VLMs) to specialized domains for Video Question Answering, including fine-tuning and in-context learning. However, acquiring task-specific knowledge at the inference phase from only a small labeled support set without fine-tuning remains a challenge. In this paper, we propose a method that achieves adaptation solely through inference-time context injection. Our method first constructs a Reflective Dialogue (RD) -- a multi-turn conversation between two agents, in which Teacher poses each support question and delivers correctness feedback, and Solver answers and provides visual grounding explanations (or reflections) for both correct and incorrect answers. This dialogue history is then used as context at the inference phase. Experiments on the EgoCross benchmark demonstrate that our method outperforms both a baseline zero-shot setting and a standard in-context learning approach that passes support set examples directly, achieving 3rd place in the Open-source Track of the 1st Cross-Domain EgoCross Challenge at the CVPR 2026 EgoVis Workshop, for which this paper also serves as a technical report.

### 4. StreamChar: Long-Horizon Streaming Character Audio-Video Generation with Decoupled Orchestration

- 方向：底层视觉、视频处理
- 作者：Linrui Tian, Qi Wang, Bang Zhang
- 日期：2026-05-25
- 分类：cs.CV
- 关键词：denoising、video denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.25659v1) / [PDF](http://arxiv.org/pdf/2605.25659v1)

摘要：

> Real-time streaming joint audio-video generation for character animation requires a generator to speak the requested transcript, maintain visual identity across chunks, and run within a strict playback budget. These requirements are difficult to satisfy simultaneously: chunk-wise autoregressive generation can accumulate transcript-audio misalignment and visual drift, while the few-step distillation needed for low latency often degrades spatial diversity and temporal quality. We present StreamChar, a streaming framework that separates long-horizon orchestration from short-window audio-video denoising. An LLM-based orchestrator uses the transcript and historical context to produce frame-aligned audio conditions, and a joint audio-video DiT performs local bidirectional denoising with reference and motion-frame conditioning. For efficient deployment, we use a two-stage distillation pipeline that first compresses the sampler and then fine-tunes the student under online chunk rollouts. A progress-aware pointer aligns partial transcripts with generated audio during rollout training, and a sink-chunk memory provides a persistent visual anchor for reducing long-horizon drift. Experiments on short-clip and long-horizon protocols show that StreamChar runs in real time on a single H100 GPU and provides a favorable system-level trade-off among transcript fidelity, audio-visual synchronization, visual quality, and streaming stability compared with recent joint and audio-driven baselines.

### 5. Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation

- 方向：底层视觉、视频处理
- 作者：Shuyuan Tu, Qi Tian, Zihan Yang, Yue Wu, Xintong Han, Weijie Kong, et al.
- 日期：2026-05-24
- 分类：cs.CV
- 关键词：denoising、video denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.25195v1) / [PDF](http://arxiv.org/pdf/2605.25195v1)

摘要：

> Current open-source diffusion models struggle to generate stable and synchronized audio-visual content, particularly in scenarios demanding complex semantic reasoning. The root cause is that existing methods rely on coarse text embeddings from off-the-shelf encoders to guide audio-video denoising, which discards fine-grained semantics and, critically, lacks a shared long-horizon plan, leading to uncoordinated denoising trajectories and fragile cross-modal alignment. We propose Baton, the first framework that introduces explicit semantic planning into joint video-audio generation. Our key insight is that complementing coarse text guidance with semantically rich, modality-aware planned tokens, jointly reasoned and mutually aligned before denoising, can simultaneously restore fine-grained semantic detail and establish a shared blueprint that coordinates both audio and video denoising trajectories. Concretely, Baton first introduces the VA-Planner, a multimodal language model equipped with dual semantic alignment towers, where learnable queries cross-attend to both video and audio features to produce a pair of semantically aligned video and audio planned tokens as keyframe-level blueprints. These planned tokens are injected into the diffusion backbone via cross-attention layers, providing temporally grounded guidance complementary to coarse text embeddings. Since planned tokens do not share one-to-one spatial-temporal correspondence with diffusion latents, we further propose Relative Semantic RoPE, a relative positional encoding that maps planned tokens and latents into a shared spatial-temporal coordinate frame, enabling each latent to accurately attend to its positionally corresponding semantic cues. Experiments on benchmarks show the effectiveness of Baton both qualitatively and quantitatively.

### 6. From Affect to Complex Behavior: Advancing Multimodal Human-Centered AI at the 10th ABAW Workshop & Competition

- 方向：顶会论文
- 作者：Dimitrios Kollias, Panagiotis Tzirakis, Alan Cowen, Stefanos Zafeiriou, Irene Kotsia, Eric Granger, et al.
- 日期：2026-05-24
- 分类：cs.CV
- 关键词：CVPR 2026、CVPR
- 链接：[Abstract](http://arxiv.org/abs/2605.27451v1) / [PDF](http://arxiv.org/pdf/2605.27451v1)

摘要：

> The 10th Affective & Behavior Analysis in-the-Wild (ABAW) Workshop and Competition, held at CVPR 2026, continues to advance research on modelling, analysis, understanding of human affect and behavior in real-world, unconstrained environments. The workshop maintains its dual structure, comprising both a competition and a paper track. The ABAW Competition introduces a diverse set of challenges targeting key aspects of affective and behavioral understanding, including continuous affect (valence-arousal) estimation, discrete affect (expression and action unit) recognition, as well as more complex behavior analysis tasks, such as emotional mimicry intensity estimation, ambivalence/hesitancy recognition and fine-grained violence detection. These challenges are built upon large-scale in-the-wild datasets, providing comprehensive benchmarks for state-of-the-art approaches. In parallel, the paper track presents a wide range of contributions spanning pose, motion & behavior estimation, affect modelling & multimodal learning, benchmarks, datasets & evaluation protocols, fairness, robustness & deployment. Overall, the 10th ABAW Workshop and Competition continues to serve as a key platform for benchmarking, collaboration and innovation, shaping the development of next-generation multimodal, human-centered AI systems.

### 7. Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling

- 方向：底层视觉
- 作者：Xinyu Wang, Mingze Li, Sicheng Lyu, Dongxiu Liu, Kaicheng Yang, Ziyu Zhao, et al.
- 日期：2026-05-27
- 分类：cs.CV, cs.LG
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.28803v1) / [PDF](http://arxiv.org/pdf/2605.28803v1)

摘要：

> Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We challenge this assumption with Omega-QVLA, the first training-free post-training quantization framework that compresses both the language backbone and the entire diffusion action head of a VLA model to a uniform W4A4 precision, eliminating the need for mixed-precision allocation. Omega-QVLA combines a composite SVD-Hadamard rotation that equalizes per-channel weight energy while diffusing residual activation outliers with per-step DiT activation scaling quantization that absorbs dynamic-range drift across denoising steps. On LIBERO, Omega-QVLA compresses Pi 0.5 and GR00T N1.5 to W4A4 with 98.0% and 87.8% task success rates, matching or exceeding their FP16 references of 97.1% and 87.0%, while reducing the static memory footprint by 71.3%. Real-world manipulation experiments further confirm smooth, accurate manipulation where prior methods fail. Code is available at https://github.com/UCMP13753/Omega-QVLA.

### 8. Diffusion Large Language Models for Visual Speech Recognition

- 方向：底层视觉
- 作者：Jeong Hun Yeo, Chae Won Kim, Hyeongseop Rha, Yong Man Ro
- 日期：2026-05-27
- 分类：cs.AI, cs.CV, eess.AS
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.28456v1) / [PDF](http://arxiv.org/pdf/2605.28456v1)

摘要：

> Existing Visual Speech Recognition (VSR) systems commonly rely on left-to-right autoregressive decoding, which can force premature decisions on visually ambiguous tokens before sufficient context is available. We propose DLLM-VSR, to the best of our knowledge, the first Diffusion Large Language Model (DLLM)-based VSR framework, formulating transcription as iterative masked denoising with flexible-order decoding. With confidence-based unmasking, DLLM-VSR commits high-confidence positions early and uses the committed tokens as bidirectional context to refine ambiguous ones. To adapt DLLMs to VSR, we introduce a two-stage masked-denoising training strategy that separates visual-to-text content alignment from length modeling. We further observe a performance gap with oracle-length decoding, which assumes access to the true transcript length, indicating that reducing target-length uncertainty can improve DLLM-based VSR. To reduce this gap, we develop length-guided candidate decoding, which uses video duration to construct plausible transcript-length hypotheses, decodes under multiple hypotheses, and reranks candidates using length plausibility and decoding confidence. The proposed method achieves a state-of-the-art WER of 19.5\% on LRS3 using only its labeled training data.

### 9. Inpainting-Style Conditional Diffusion for Multivariable Time Series Forecasting

- 方向：底层视觉
- 作者：Kourosh Kiani, S. M. Muyeen
- 日期：2026-05-27
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.28324v1) / [PDF](http://arxiv.org/pdf/2605.28324v1)

摘要：

> In this paper, we propose a novel conditional diffusion-based framework for multivariable time-series solar power forecasting. The proposed method reformulates temporal PV data as structured two-dimensional representations (images) using a sliding-window patch construction, enabling the application of Denoising Diffusion Probabilistic Models (DDPM) within a unified spatiotemporal learning paradigm. A key contribution of this work is the formulation of solar forecasting as an inpainting problem, where future time steps are treated as missing regions to be reconstructed. This is achieved through a mask-based conditional diffusion mechanism, in which historical observations are preserved as conditioning context while the target (future) region is progressively corrupted and subsequently recovered via reverse diffusion. The model learns to generate coherent future sequences conditioned on observed data, effectively performing time-series inpainting. To fully utilize all available features and ensure compatibility with U-Net architectural constraints, a zero-padding strategy is introduced to construct fixed-size inputs. The model is trained using a supervised denoising objective to predict injected noise, enabling accurate iterative reconstruction during the reverse process. Extensive experiments conducted on benchmark PV dataset, including GEFCom2014, demonstrate that the proposed approach achieves high forecasting accuracy, particularly for short-term horizons. The results highlight the effectiveness of integrating diffusion-based generative modeling with an inpainting formulation for robust, flexible, and high-fidelity solar power forecasting.

### 10. DebFilter: Eradicating Biases Stashed in Value

- 方向：底层视觉
- 作者：Seung Hyuk Lee, Songkuk Kim
- 日期：2026-05-27
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.28167v1) / [PDF](http://arxiv.org/pdf/2605.28167v1)

摘要：

> Text-to-image diffusion models, which are theoretically equivalent to score-based generative models, generate images through a multi-step denoising process guided by text embeddings extracted from pretrained vision-language models such as CLIP. However, these text embeddings inherently encode social and semantic biases -- such as those related to gender and age -- that are subsequently propagated and amplified through the guidance mechanism, along with the model's training on large-scale datasets that are imbalanced with respect to these bias-related concepts, often leading to skewed outputs in text-to-image generation. We propose DebFilter, a lightweight and training-free framework for mitigating such biases in text-to-image diffusion models. Observing that the model's error prediction at each denoising step is primarily influenced by cross-attention dynamics, we introduce a bias-correction strategy that adjusts the value components within cross-attention. Specifically, we apply a fixed offset to the slice of guidance embedding, effectively steering the semantic direction of cross-attention values toward unbiased representations. This adjustment reconfigures the score landscape to produce balanced outputs while maintaining alignment with the intended text semantics. Unlike prior approaches that rely on fine-tuning or retraining, DebFilter operates entirely at inference time, requiring no additional data or model updates. Our results demonstrate that this method effectively mitigates social biases in generated images, offering an efficient and scalable pathway toward fairer and more inclusive text-to-image generation.

### 11. Residualized Temporal Sparse Autoencoders for Interpreting Diffusion Models

- 方向：底层视觉
- 作者：Calvin Yeung, Prathyush Poduval, Ali Zakeri, Zhuowen Zou, Mohsen Imani
- 日期：2026-05-27
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.27813v1) / [PDF](http://arxiv.org/pdf/2605.27813v1)

摘要：

> Text-to-image diffusion models generate images through an iterative denoising process, so internal neural layers produce trajectories of activations rather than single static representations. Sparse autoencoders (SAEs) have recently been used to decompose diffusion activations into interpretable feature directions, but most approaches analyze activations at individual timesteps or condition on time rather than learning directly from full activation trajectories. In this work, we introduce residualized temporal SAEs for diffusion activation trajectories. We collect activations across denoising time, fit linear predictors between neighboring timesteps, and represent each trajectory using an initial activation together with residual components not explained by these linear dynamics. Training an SAE on this residualized representation encourages sparse latents to capture structure beyond what is linearly predictable. The residualized decoder directions can be mapped back into activation space, allowing each latent to be analyzed as a feature trajectory over denoising time. Through reconstruction and ablation studies, spatiotemporal feature analysis, and qualitative steering experiments on Stable Diffusion~1.5, we show that residualized temporal SAEs provide a useful framework for studying temporally structured diffusion activations.

### 12. Explicit Critic Guidance for Aligning Diffusion Models

- 方向：底层视觉
- 作者：Zhengyang Liang, Qihang Zhang, Ceyuan Yang
- 日期：2026-05-26
- 分类：cs.LG, cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.27736v1) / [PDF](http://arxiv.org/pdf/2605.27736v1)

摘要：

> Online reinforcement learning is becoming increasingly important for aligning diffusion models with non-differentiable objectives. However, existing methods still face limitations in assigning fine-grained credit along denoising trajectories and in realizing stable value-based optimization. We propose a state-aligned latent actor-critic framework for diffusion post-training, in which the diffusion model serves as its own timestep-conditioned value function and predicts values directly on noisy latent states. This enables trajectory-level PPO training, supports stable actor-critic optimization with simple conditioning and value pretraining strategies, and naturally allows the learned critic to be reused for inference-time steering. We further extend the framework to multi-reward optimization, where joint training with complementary rewards helps alleviate reward hacking. Across both UNet- and DiT-based backbones, our method consistently outperforms prior group-relative RL and actor-critic baselines on single-reward and multi-reward benchmarks, while test-time steering provides additional gains in generation quality.

### 13. Asynchronous Remote Sensing Time-Series Fusion for Cloud Removal and Anytime Reconstruction

- 方向：底层视觉
- 作者：Forouzan Fallah, Chia Yu Hsu, Wenwen Li, Anna Liljedahl, Yezhou Yang
- 日期：2026-05-26
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.27726v1) / [PDF](http://arxiv.org/pdf/2605.27726v1)

摘要：

> Frequent cloud cover severely limits the usability of Sentinel-2 (S2) optical time series for Earth surface monitoring. Sentinel-1 (S1) SAR provides all-weather complementary observations, but practical S1/S2 fusion remains difficult because acquisitions are irregular and asynchronous. Many existing approaches assume temporally aligned inputs (or require external nearest-date matching) and typically restore only observed timestamps, limiting reconstruction under long gaps and preventing on-demand synthesis. We propose AGFlow (Time Aligned Generative Flow Matching), a spatiotemporal flow-matching model for S1/S2 cloud removal and time-series reconstruction with three capabilities: (1) timestamp-conditioned internal alignment that fuses asynchronous S1 and cloudy S2 observations without preprocessing-based pairing; (2) spatiotemporal, context-aware denoising that models spatial structure jointly with temporal dynamics (rather than independent per-pixel time series); and (3) anytime querying, enabling generation of cloud-free S2 frames at both observed and user-specified timestamps within the monitoring window. We evaluate on the RESTORE-DiT benchmark protocol with quantitative metrics, qualitative comparisons, and component ablations. AGFlow notably improves fully missing-frame reconstruction (MAE and RMSE reduce by 16-19% over RESTORE-DiT) and provides reliable reconstructions under persistent gaps, while also yielding competitive cloud removal performance and flexible temporal querying for downstream tasks such as dense vegetation monitoring.

### 14. PARE: Pruning and Adaptive Routing for Efficient Video Generation

- 方向：底层视觉
- 作者：Yutong Wang, Yunke Wang, Tianfan Xue, Yu Qiao, Yaohui Wang, Xinyuan Chen, et al.
- 日期：2026-05-26
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.27336v1) / [PDF](http://arxiv.org/pdf/2605.27336v1)

摘要：

> Video Diffusion Transformers (DiTs) generate high-quality videos but demand substantial compute due to wide blocks, deep architectures, and iterative sampling. Recent methods reduce cost by compressing width, depth, or sampling steps, but typically commit to a fixed architecture that cannot adapt to individual inputs or denoising stages. We propose PARE (Pruning and Adaptive Routing for Efficient video generation), which jointly compresses width and depth with structure-aware pruning and input-adaptive routing. For width, we observe that attention heads specialize into spatial and temporal roles, and design importance scoring that accounts for this distinction to prevent motion-critical temporal heads from being pruned prematurely. For depth, we train a lightweight router conditioned on denoising timestep and visual content to dynamically select which blocks to execute at each step, enabling per-input compute adaptation rather than static block removal. A progressive pipeline first recovers width-pruned quality via distillation, then jointly optimizes the student and router to decouple the two learning objectives. Experiments on Wan2.1-14B for both image-to-video and text-to-video generation show that PARE substantially reduces per-step computation while preserving quality across VBench dimensions, and composes with step distillation for further acceleration.

### 15. SoftCap: Soft-Budget Control for Diffusion Transformer Acceleration

- 方向：底层视觉
- 作者：Yuhang Zhang, Junxiang Qiu, Huixia Ben, Zhenhua Tang, Shuo Wang, Yanbin Hao
- 日期：2026-05-26
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.27075v1) / [PDF](http://arxiv.org/pdf/2605.27075v1)

摘要：

> Diffusion Transformers (DiTs) achieve strong visual quality, but their iterative denoising process requires many costly Transformer evaluations. Training-free acceleration methods reduce this cost by caching, forecasting, or verifying intermediate features, yet the runtime decision of when to execute a Full step is often driven by fixed schedules or hand-tuned thresholds. We propose \textbf{SoftCap}, a training-free control layer for cache-based DiT inference. SoftCap couples a Trajectory Drift Observer, which estimates local cache risk from lightweight hidden-state statistics, with a Soft-Budget PI Controller, which adjusts the Full-triggering threshold from realized compute relative to a fixed reference profile. The budget is a soft ceiling: it shapes the threshold but does not require a run to spend a prescribed number of Full evaluations. On FLUX.1-dev, SoftCap improves over SpeCa at a comparable middle-compute operating point, raising ImageReward from 0.967 to 0.981 and reducing LPIPS-Full from 0.518 to 0.498 at nearly identical FLOPs, while target-sweep diagnostics show the intended soft-ceiling behavior as the budget is relaxed.

### 16. NeR-SC: Adapting Neural Video Representation to Screen Content

- 方向：视频处理
- 作者：Ruohan Shi, Jiaoyan Zhao, Haogang Feng
- 日期：2026-05-26
- 分类：cs.CV, cs.MM
- 关键词：video compression
- 链接：[Abstract](http://arxiv.org/abs/2605.27024v1) / [PDF](http://arxiv.org/pdf/2605.27024v1)

摘要：

> Implicit neural representations have emerged as a promising paradigm for video compression, with recent methods achieving competitive performance on natural video. However, screen content video -- common in remote desktop, online education, and cloud gaming -- exhibits distinct statistics: sharp edges, limited color palettes, and strong temporal redundancy. Existing neural representation methods, designed for natural scenes, lack mechanisms to exploit these properties, leaving substantial room for improvement. In this paper, we propose NeR-SC, a neural representation framework tailored for screen content video. Building on the SNeRV backbone, NeR-SC introduces three screen-content-specific modules: (i) a learnable color palette that models the discrete color structure of screen content by restricting the low-frequency sub-band to a learned color set; (ii) a multi-gate dense fusion module that replaces sequential feature fusion with dense, attention-gated cross-stage interaction; and (iii) an embedding-level frame skip strategy that bypasses redundant decoder invocations for static frames, with zero training overhead. Experiments on DSCVC and VCD show that NeR-SC achieves 40.32~dB and 41.73~dB average PSNR, outperforming representative neural video representation methods and, at low bitrates, surpassing H.264 and H.265. The skip strategy enables real-time decoding with no loss in quality.

### 17. Timestep-Aware SVDQuant-GPTQ for W4A4 Quantization of Wan2.2-I2V

- 方向：底层视觉
- 作者：Junhao Wu, Dezhong Yao, Hai Jin
- 日期：2026-05-26
- 分类：cs.CV, cs.AI
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.27003v1) / [PDF](http://arxiv.org/pdf/2605.27003v1)

摘要：

> W4A4 quantization of large video diffusion Transformers offers substantial memory savings but is hindered by two main challenges: sparse large-magnitude activation outliers, and strongly timestep-dependent activation distributions across the multi-step denoising trajectory. These difficulties are compounded by Wan2.2-I2V's two-expert Mixture-of-Experts DiT design, whose high-noise and low-noise experts exhibit distinct quantization sensitivities that a single global calibration policy cannot capture. We propose a post-training quantization framework combining SVDQuant-based low-rank outlier compensation, GPTQ-based reconstruction-aware residual weight quantization, and timestep-bin-wise per-layer activation clipping-ratio search conducted independently for each expert. On the OpenS2V-Eval benchmark, our method reduces peak GPU memory by 59.3\% relative to the BF16 baseline while incurring only a 0.9\% drop in VBench average score and a 2.3\% drop in Imaging Quality, demonstrating that expert- and timestep-aware calibration is essential for high-fidelity W4A4 inference on MoE video DiTs.

### 18. SIMPC: Learning Self-Induced Mirror-Point Consistency for Unsupervised Point Cloud Denoising

- 方向：底层视觉
- 作者：Chengwei Zhang, Xueyi Zhang, Tao Jiang, Xinhao Xu, Wenjie Li, Fubo Zhang, et al.
- 日期：2026-05-26
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.26894v1) / [PDF](http://arxiv.org/pdf/2605.26894v1)

摘要：

> In point clouds, noise directly perturbs point coordinates that encode both spatial location and geometry, making one-to-one correspondence construction more challenging than in images. Existing methods impose statistical mappings across noisy variants via noise or optimal transport, but suffer from correspondence ambiguity. In this work, we propose Self-Induced Mirror-Point Consistency (SIMPC) to learn deterministic correspondences between points and the underlying surface in an unsupervised manner. For each noisy point, SIMPC generates a mirror-point on the opposite side of the underlying surface, guided by geometric priors during the denoising process. By encouraging consistency between the denoising targets of the original point and its mirror counterpart, SIMPC effectively localizes the position of underlying surface. Extensive experiments on synthetic and real-world datasets demonstrate that SIMPC significantly outperforms state-of-the-art unsupervised methods and surpasses several strong supervised counterparts.

### 19. Scheduled Style Injection: Expanding the Style-Content Pareto Frontier in Training-Free Diffusion-based Style Transfer

- 方向：底层视觉
- 作者：Amey Sunil Kulkarni
- 日期：2026-05-26
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.26538v1) / [PDF](http://arxiv.org/pdf/2605.26538v1)

摘要：

> Style transfer with pre-trained diffusion models has advanced rapidly, but a core question remains underexplored: where in the model should style injection be strongest? StyleID, the leading training-free method, uses a single global parameter (gamma) uniformly across all layers and timesteps, which forces a fixed tradeoff between style quality and content preservation. We show this tradeoff is unnecessarily rigid. We systematically explore four dimensions of control: varying style injection strength across decoder layers, across denoising timesteps, and scheduling ControlNet geometric conditioning along both axes. The pattern is consistent everywhere: decreasing schedules, with stronger structural signal injection in shallower layers and earlier timesteps, reliably outperform the reverse. Beyond direction, schedule shape matters: cosine and square-root timestep schedules outperform linear. Most importantly, we find that gamma scheduling and ControlNet conditioning are nearly independent. The resulting combined configurations expand the Pareto frontier, offering superior tradeoffs between style fidelity and content preservation compared to any single baseline setting. Our best balanced configuration achieves ArtFID of 27.036 versus StyleID's 28.801 - a 6.1% relative improvement, with consistent gains across the full style-content tradeoff frontier. Results are validated across 35 configurations totaling over 28,000 stylized images using four complementary metrics. These findings generalize across SD backbones with identical rank ordering. All modifications are training-free, parameter-free, and require only a few lines of scheduling code; code is available at https://github.com/ameyskulkarni/scheduled_style_injection.

### 20. Beyond Pairwise Preferences: Listwise Reward-Aware Alignment for Diffusion Models

- 方向：底层视觉
- 作者：Austin Wang, Jiaqi Han, Stefano Ermon, Yisong Yue
- 日期：2026-05-26
- 分类：cs.LG, cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.26491v1) / [PDF](http://arxiv.org/pdf/2605.26491v1)

摘要：

> Preference optimization has emerged as an efficient alternative to online reinforcement learning from human feedback (RLHF) for aligning text-to-image diffusion models. However, existing methods largely reduce supervision to binary pairwise comparisons. This pairwise reduction is limiting when training data naturally contains multiple candidate images for the same prompt, and when continuous reward scores can provide richer information than a single winner-loser label. To address these limitations, we propose Diffusion LAIR, a reward-aware listwise preference optimization method for diffusion models. For each prompt, LAIR converts reward scores across a group of candidate images into centered advantage weights, then optimizes an advantage-weighted regression objective on the implicit reward, defined as the denoising-loss improvement of the current model over a fixed reference model, with a quadratic penalty that regularizes the magnitude of the implicit reward. The resulting objective uses all candidates simultaneously rather than selecting pairs, and remains conservative by explicitly controlling the magnitude of the implicit reward. The LAIR objective admits a bounded closed-form optimum in implicit-reward space, clarifying how the regularization strength controls the magnitude of the preference update. Experiments show that Diffusion LAIR outperforms strong preference optimization baselines on SD1.5 and SDXL across text-to-image generation, compositional generation, and image editing benchmarks.

### 21. D$^2$Turb: Depth-Aware Simulation and Decoupled Learning for Single-Frame Atmospheric Turbulence Mitigation

- 方向：底层视觉
- 作者：Zixiao Hu, Tianyu Li, Guoqing Wang, Wei Li, Guoguo Xin, Xun Liu, et al.
- 日期：2026-05-25
- 分类：cs.CV
- 关键词：deblurring
- 链接：[Abstract](http://arxiv.org/abs/2605.27460v1) / [PDF](http://arxiv.org/pdf/2605.27460v1)

摘要：

> Single-frame atmospheric turbulence mitigation is inherently ill-posed due to spatially varying blur coupled with non-rigid geometric distortion. Existing end-to-end approaches trained on flat-field simulations often struggle to balance texture recovery with geometric rectification. To overcome this limitation, we propose D$^2$Turb, a unified framework that bridges physics-grounded simulation with explicitly decoupled restoration. First, we introduce a Depth-Aware Turbulence Synthesis protocol that incorporates scene depth into the phase-to-space formulation. This generates physically consistent, depth-dependent degradations and provides a crucial intermediate tilt supervision signal for disentangled learning. Building upon this simulation engine, D$^2$Turb decomposes restoration into two interactive stages: texture deblurring and geometric rectification. The texture deblurring stage employs a deblurring backbone to recover fine-grained details while preserving geometric distortion for the subsequent rectification stage. To mitigate the information fragmentation commonly observed in cascaded designs, we further propose an Adaptive Structural Prior Injection (ASPI) mechanism that dynamically transfers deep structural representations from the deblurring module to guide dense flow prediction for spatial unwarping. Extensive experiments demonstrate that D$^2$Turb achieves state-of-the-art performance on both synthetic and real-world datasets, with consistent improvements in both texture recovery and geometric fidelity. Our code and pre-trained models are publicly available at https://github.com/HertzDot222/D2Turb.

### 22. Geometry-Aware Representation Denoising for Robust Multi-view 3D Reconstruction

- 方向：底层视觉
- 作者：Jin Hyeon Kim, Jaeeun Lee, Claire Kim, Kyoungjin Oh, Paul Hyunbin Cho, Jaewon Min, et al.
- 日期：2026-05-25
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.26230v1) / [PDF](http://arxiv.org/pdf/2605.26230v1)

摘要：

> Multi-view 3D reconstruction has achieved remarkable progress with the advent of feed-forward 3D reconstruction models. However, these models are typically trained and evaluated under ideal, degradation-free imaging conditions, whereas real-world observations often contain degradations that differ significantly from such settings. Improving robustness for multi-view 3D reconstruction under degraded conditions therefore remains an important challenge. We present Geometry-Aware Representation Denoising (GARD), a novel framework that performs diffusion-based multi-view restoration directly in the feature space of a feed-forward 3D reconstruction model. This design exploits the geometry-aware feature representations of the 3D reconstructor to effectively recover accurate scene geometry. Furthermore, by employing an additional RGB image decoder, the refined representations can also be used to restore high-quality RGB images, thereby enabling the simultaneous recovery of 3D scene geometry and high-quality imagery. Comprehensive experiments on the Depth Anything 3 (DA3) benchmark demonstrate the effectiveness of the proposed GARD framework.

### 23. Squeezing Capacity from Multimodal Large Language Models for Subject-driven Generation

- 方向：底层视觉
- 作者：Shuhong Zheng, Aashish Kumar Misraa, Yu-Teng Li, Yu-Jhe Li, Igor Gilitschenski
- 日期：2026-05-25
- 分类：cs.CV, cs.AI, cs.GR, cs.LG, cs.MM
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.26111v1) / [PDF](http://arxiv.org/pdf/2605.26111v1)

摘要：

> Subject-driven image generation aims to synthesize new images that preserve the identity of the given subject while following textual instructions. Existing approaches often encode text and reference images separately. This limits cross-modal reasoning abilities and causes copy-paste artifacts. Recent frameworks that connect multimodal models and diffusion models improve instruction following, but largely overlook identity preservation. To address these limitations, we condition diffusion models on Multimodal Large Language Models (MLLMs) that jointly encode text and reference images, and augment it with VAE-based identity conditioning. A novel Dual Layer Aggregation (DLA) module is designed to aggregate multi-level MLLM features for optimal conditioning, and a multi-stage denoising strategy is applied to progressively balance the semantic information from MLLM and fine-detail identity from VAE during inference. Extensive experiments demonstrate that our approach harmonizes multimodal understanding with identity preservation, mitigates copy-paste issues, and achieves superior performance regarding human preference on subject-driven image generation. Our project website is available at https://zsh2000.github.io/squeeze-mllm-subject-gen/.

### 24. On-Policy Adversarial Flow Distillation for Autoregressive Video Generation

- 方向：底层视觉
- 作者：Yang Luo, Shengju Qian, Xiaohang Tang, Zirui Zhu, Yong Liu, Xin Wang, et al.
- 日期：2026-05-25
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.26105v1) / [PDF](http://arxiv.org/pdf/2605.26105v1)

摘要：

> Autoregressive video generators are attractive for streaming, long-horizon, and interactive applications, but distilling strong black-box teachers into causal students remains difficult. The student must learn under its own rollout distribution, whereas practical teachers may expose only prompt-conditioned completed videos and may differ in architecture, capacity, temporal design, and sampling schedule. This interface makes supervised fine-tuning off-policy, score-based distillation inapplicable, and direct adversarial imitation too sparse for denoising-time credit assignment. We propose Adversarial Flow Distillation (AFD), an on-policy framework for heterogeneous black-box video distillation. AFD queries the teacher and rolls out the current student on the same prompts, trains a prompt-paired Bradley-Terry discriminator to estimate clean-sample teacher-student discrepancy, and converts the resulting on-policy advantage into forward-process flow-matching updates on the student's own noised states. Thus, AFD provides dense velocity-field supervision while requiring no teacher scores, latents, denoising trajectories, step alignment, or reverse-chain reinforcement learning. Experiments across two causal AR student families show that AFD consistently improves motion- and physics-sensitive generation while preserving general video quality, and ablations validate the importance of adaptive on-policy feedback and forward-process credit assignment. The method requires only clean teacher videos and student rollouts, providing a practical route for distilling proprietary or heterogeneous video generators into efficient autoregressive students.

### 25. A Multimodal 3D Foundation Model for Light Sheet Fluorescence Microscopy Enables Few-Shot Segmentation, Classification, and Deblurring

- 方向：底层视觉
- 作者：Adina Scheinfeld, Haotan Zhang, Shang Mu, Rudolf L. M. van Herten, Lucas Stoffl, Ali Erturk, et al.
- 日期：2026-05-25
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：deblurring
- 链接：[Abstract](http://arxiv.org/abs/2605.26026v1) / [PDF](http://arxiv.org/pdf/2605.26026v1)

摘要：

> Light sheet fluorescence microscopy (LSM) enables high-resolution, three-dimensional (3D) imaging of biological specimens, providing rich volumetric data for studying cellular organization, pathology, and vascular networks. However, the size, dimensionality, and annotation burden of LSM data make supervised deep learning approaches costly and difficult to scale. Additionally, despite the abundance of unannotated LSM volumes, foundation models for this modality remain underexplored due to computational challenges and the complexity of volumetric representation learning. In this work, we introduce a 3D foundation model for LSM data, pretrained on a large curated collection of 3D images spanning multiple organisms, stains, and imaging protocols. We learn transferable volumetric representations by jointly optimizing for masked reconstruction and image-text alignment. The pretrained backbone drastically reduces the annotation burden, enabling efficient, few-shot adaptation for varied downstream tasks. We evaluate this approach on downstream segmentation, classification, and deblurring. Our results demonstrate consistent improvements over baselines, (1) when measured using standard evaluation metrics and (2) when rigorously assessed by domain experts. This highlights the potential of foundation model pretraining to reduce annotation requirements while improving performance across diverse LSM analysis tasks. Pretrained model weights and code for pretraining and finetuning are publicly available: https://github.com/AdinaScheinfeld/lsm_fm_public_repo.git.

### 26. How Accurate are Video Quality Models for Diffusion-Based Video Super-Resolution?

- 方向：视频处理
- 作者：Benjamin Herb, Steve Göring, Alexander Raake, Rakesh Rao Ramachandra Rao
- 日期：2026-05-25
- 分类：eess.IV, cs.CV
- 关键词：video super-resolution
- 链接：[Abstract](http://arxiv.org/abs/2605.25940v1) / [PDF](http://arxiv.org/pdf/2605.25940v1)

摘要：

> Recent video super-resolution (VSR) approaches use deep neural networks to enhance low-quality input videos and recover visual detail, with diffusion-based methods in particular showing promising results. In this paper, we investigate whether existing video quality models can be used to assess the performance of these diffusion-based VSR methods, by comparing model predictions with results from a subjective test. The study compares six upscaling methods (Lanczos, Rhea, SCST, DOVE, SeedVR2, Starlight Mini) applied to both compressed (AV1 and DCVC-RT) and uncompressed low-resolution videos considering the play-out on a UHD-1/4K screen. A range of full- and no-reference quality models are used to assess their applicability to this new type of quality degradation, focusing on within-sequence performance. The results highlight that CNN-based full-reference models, such as LPIPS, DISTS, and CVQA-FR show significantly higher correlation coefficients than both conventional full- as well as the tested no-reference models. Most overestimate the overly sharp results of SCST, with VMAF mainly failing due to spatial inconsistencies introduced by Starlight Mini. None of the tested video quality models reach sufficient accuracy so as to replace complementary subjective testing. The reference, degraded and upscaled videos, as well as the user ratings and model scores are made available with the paper at https://github.com/Telecommunication-Telemedia-Assessment/AVT-VQDB-UHD-1-VSR as open data.

### 27. SP-MoMamba: Superpixel-driven Mixture of State Space Experts for Efficient Image Super-Resolution

- 方向：底层视觉
- 作者：Wenbin Zou, Yawen Cui, Yi Wang, Lap-Pui Chau, Liang Chen, Jinshan Pan, et al.
- 日期：2026-05-25
- 分类：cs.CV
- 关键词：image super-resolution
- 链接：[Abstract](http://arxiv.org/abs/2605.25892v1) / [PDF](http://arxiv.org/pdf/2605.25892v1)

摘要：

> State space models (SSMs) have emerged as a powerful paradigm for efficient single-image super-resolution (SR) due to their linear complexity and long-range modeling capabilities. However, existing Mamba-based methods typically rely on data-agnostic rigid scanning, which reshapes 2D images into 1D sequences over a fixed grid, inevitably disrupting spatial-semantic topology and introducing artifacts. Inspired by the \textbf{Gestalt perceptual grouping theory}, we propose \textbf{SP-MoMamba}, a superpixel-driven mixture of state space experts designed for content-aware SR. Our core idea is to transform the traditional rigid scanning into a \textbf{semantic-level interaction} by treating superpixels as fundamental units. Specifically, we introduce the \textbf{Superpixel-driven State Space Model (SP-SSM)}, which compresses semantically homogeneous regions into high-order tokens to preserve global topological consistency. To address the conflict between fixed scanning scales and diverse semantic granularities, we develop the \textbf{Multi-Scale Superpixel Mixture of State Space Experts (MSS-MoE)}. This module utilizes a dynamic routing mechanism to adaptively assign scale-specific experts, effectively capturing multi-scale textures while reducing computational redundancy. Furthermore, to prevent the loss of high-frequency details during global abstraction, we introduce a \textbf{Local Spatial Modulation Expert (LSME)} to complement the global modeling, ensuring a precise reconstruction of sharp edges and fine structures. Extensive experiments on standard benchmarks demonstrate that SP-MoMamba achieves superior reconstruction fidelity and a more favorable efficiency-performance trade-off compared to state-of-the-art efficient SR methods.

### 28. Concept Unlearning via Cross-Attention Activation Projection for Diffusion Models

- 方向：底层视觉
- 作者：Saemi Moon, Suhyeon Jun, Seoyeon Lee, Dongwoo Kim
- 日期：2026-05-25
- 分类：cs.CV, cs.AI, cs.LG
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.25765v1) / [PDF](http://arxiv.org/pdf/2605.25765v1)

摘要：

> Concept unlearning aims to erase a target concept from a pretrained text-to-image diffusion model without retraining. Closed-form methods are attractive in this setting because they apply a single deterministic edit to the cross-attention weights and add no inference-time cost. Existing closed-form methods, however, represent the target concept through the text encoder's response to a few short anchor prompts that name it, and paraphrased prompts that evoke the concept without naming it consistently bypass the edit. We argue that the target should instead be represented in the cross-attention activation space. Text embeddings describe the user's prompt, while cross-attention activations describe what the model is about to render, and the latter generalize to paraphrase the anchor templates do not cover. Building on this observation, we propose PURE (Projection in U-Net Rendering for Erasure), a closed-form method that builds the forget and retain bases from per-layer cross-attention activations captured along a short denoising trajectory and applies a single linear projector to the cross-attention key and value weights. On a recent holistic concept-unlearning benchmark covering ten concepts across artistic style, intellectual property, celebrity, and NSFW categories, PURE significantly reduces target leakage under paraphrased and adversarial prompts while preserving retain concepts close to the unedited model, yielding the best overall forget-retain trade-off among evaluated methods.

### 29. AI-T2I: Aggregating-and-Isolating Cross-Attention to Diffusion Models for Text-to-Image Synthesis

- 方向：底层视觉
- 作者：Shipeng Cao, Biao Qian, Haipeng Liu, Yang Wang, Meng Wang
- 日期：2026-05-25
- 分类：cs.CV
- 关键词：denoising
- 链接：[Abstract](http://arxiv.org/abs/2605.25763v3) / [PDF](http://arxiv.org/pdf/2605.25763v3)

摘要：

> Text-to-image synthesis has made significant progress, benefiting from the strong generative capabilities of diffusion models. However, these models struggle to achieve precise text-to-image alignment within cross-attention maps during the denoising process. Existing works primarily focus on inter-subject-token activations (i.e., cross-attention scores) overlap for different subjects, overlooking the intra-subject-token activations scattering issue for identical subjects. In this paper, we propose an Aggregating-and-Isolating cross-attention approach to diffusion models for Text-to-Image synthesis, dubbed AI-T2I. Technically, to address the scattering issue, we devise an aggregation loss to identify and consolidate the scattered intra-token activations, which implicitly helps mitigate the potential overlap issue. Upon that, an isolation loss is further introduced to push the inter-token activations apart, thus fulfilling precise text-to-image alignment. Extensive experiments on various benchmarks demonstrate the superiority of AI-T2I over the state-of-the-art works for text-to-image synthesis. Furthermore, our AI-T2I exhibits excellent generalization across other tasks, e.g., controllable layout generation and personalized generation. Our code is available at https://github.com/Hatter77/AI-T2I.

### 30. ControlLight: Towards Controllable, Consistent, and Generalizable Low-Light Enhancement

- 方向：底层视觉
- 作者：Yufeng Yang, Jianzhuang Liu, Jisheng Chu, Yuqi Peng, Xianfang Zeng, Jiancheng Huang, et al.
- 日期：2026-05-25
- 分类：cs.CV
- 关键词：low-light enhancement
- 链接：[Abstract](http://arxiv.org/abs/2605.25569v2) / [PDF](http://arxiv.org/pdf/2605.25569v2)

摘要：

> Existing deep learning-based low-light enhancement methods are typically trained on limited datasets with single enhancement targets, which restricts their generalization ability and controllability in real-world applications. To overcome these limitations, we propose ControlLight, a controllable, consistent, and generalizable framework for low-light enhancement. We first construct a large-scale dataset of real-world degraded images with continuous illumination-strength supervision. To further ensure consistent outputs under different control strengths, we introduce a misalignment-aware weighted flow matching loss that preserves image structure across continuous enhancement strengths. ControlLight allows users to edit real-world degraded low-light images toward satisfactory enhancement results by flexibly controlling the strength while preserving visual consistency and realism. Extensive experiments show that ControlLight achieves state-of-the-art performance against existing low-light enhancement approaches while demonstrating strong continuous controllability and generalization to real-world scenarios.

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`latest.md`
