---
title: 本周底层视觉与视频处理论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 本周底层视觉与视频处理论文速览

生成时间：2026-05-29

本期选取 10 篇近期 arXiv cs.CV 论文，聚焦底层视觉、视频处理和 CVPR 相关方向。为适配公众号发布，正文保留摘要要点和 arXiv 编号，完整论文可按编号到 arXiv 检索。

## 本期论文

### 1. Internally Referenced Low-Light Enhancement

- 方向：底层视觉
- 作者：Peiyuan He, Hainuo Wang, Hengxing Liu, Mingjia Li, Xiaojie Guo
- 日期：2026-05-27
- 关键词：denoising、low-light enhancement、image enhancement
- arXiv：2605.28605v1

摘要：

Self-supervised low-light image enhancement (LLIE) is highly appealing as it eliminates the reliance on external paired data. However, the lack of external references causes networks to struggle with decoupling entangled illumination, delicate textures, and amplified noise. To resolve this challenge, we propose an Internally Referenced LLIE framework that extracts reliable physical and structural references from the degraded input image itself. First, we introduce a local exposure-simulated scheme to extract a low-...

### 2. Bridging the Generalization Gap in Adverse Weather Segmentation: A Training Recipe Perspective

- 方向：顶会论文
- 作者：Cong Xu, Pu Luo, Yumei Li, Boyou Xue
- 日期：2026-05-27
- 关键词：CVPR 2026、CVPR
- arXiv：2605.27962v1

摘要：

This paper describes our approach for the 8th UG2+ Workshop (CVPR 2026) Track~2, which targets semantic segmentation of outdoor scenes degraded by five weather conditions: blur, darkness, snow, haze, and glare. A central challenge we observe is a severe generalization gap -- models that perform well on the validation set often collapse on the test set. For instance, SegFormer-B5 drops 16.1 mIoU points from validation to test, suggesting that model capacity alone is insufficient for robustness. We investigate whethe...

### 3. Reflective Dialogue between Teacher and Solver Agents for Video Question Answering

- 方向：顶会论文
- 作者：Takuya Murakawa, Toru Tamaki
- 日期：2026-05-27
- 关键词：CVPR 2026、CVPR
- arXiv：2605.27885v1

摘要：

Various approaches have been proposed to adapt Vision-Language Models (VLMs) to specialized domains for Video Question Answering, including fine-tuning and in-context learning. However, acquiring task-specific knowledge at the inference phase from only a small labeled support set without fine-tuning remains a challenge. In this paper, we propose a method that achieves adaptation solely through inference-time context injection. Our method first constructs a Reflective Dialogue (RD) -- a multi-turn conversation betwe...

### 4. StreamChar: Long-Horizon Streaming Character Audio-Video Generation with Decoupled Orchestration

- 方向：底层视觉、视频处理
- 作者：Linrui Tian, Qi Wang, Bang Zhang
- 日期：2026-05-25
- 关键词：denoising、video denoising
- arXiv：2605.25659v1

摘要：

Real-time streaming joint audio-video generation for character animation requires a generator to speak the requested transcript, maintain visual identity across chunks, and run within a strict playback budget. These requirements are difficult to satisfy simultaneously: chunk-wise autoregressive generation can accumulate transcript-audio misalignment and visual drift, while the few-step distillation needed for low latency often degrades spatial diversity and temporal quality. We present StreamChar, a streaming frame...

### 5. Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation

- 方向：底层视觉、视频处理
- 作者：Shuyuan Tu, Qi Tian, Zihan Yang, Yue Wu, Xintong Han, Weijie Kong, et al.
- 日期：2026-05-24
- 关键词：denoising、video denoising
- arXiv：2605.25195v1

摘要：

Current open-source diffusion models struggle to generate stable and synchronized audio-visual content, particularly in scenarios demanding complex semantic reasoning. The root cause is that existing methods rely on coarse text embeddings from off-the-shelf encoders to guide audio-video denoising, which discards fine-grained semantics and, critically, lacks a shared long-horizon plan, leading to uncoordinated denoising trajectories and fragile cross-modal alignment. We propose Baton, the first framework that introd...

### 6. From Affect to Complex Behavior: Advancing Multimodal Human-Centered AI at the 10th ABAW Workshop & Competition

- 方向：顶会论文
- 作者：Dimitrios Kollias, Panagiotis Tzirakis, Alan Cowen, Stefanos Zafeiriou, Irene Kotsia, Eric Granger, et al.
- 日期：2026-05-24
- 关键词：CVPR 2026、CVPR
- arXiv：2605.27451v1

摘要：

The 10th Affective & Behavior Analysis in-the-Wild (ABAW) Workshop and Competition, held at CVPR 2026, continues to advance research on modelling, analysis, understanding of human affect and behavior in real-world, unconstrained environments. The workshop maintains its dual structure, comprising both a competition and a paper track. The ABAW Competition introduces a diverse set of challenges targeting key aspects of affective and behavioral understanding, including continuous affect (valence-arousal) estimation, di...

### 7. Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling

- 方向：底层视觉
- 作者：Xinyu Wang, Mingze Li, Sicheng Lyu, Dongxiu Liu, Kaicheng Yang, Ziyu Zhao, et al.
- 日期：2026-05-27
- 关键词：denoising
- arXiv：2605.28803v1

摘要：

Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We challenge this assump...

### 8. Diffusion Large Language Models for Visual Speech Recognition

- 方向：底层视觉
- 作者：Jeong Hun Yeo, Chae Won Kim, Hyeongseop Rha, Yong Man Ro
- 日期：2026-05-27
- 关键词：denoising
- arXiv：2605.28456v1

摘要：

Existing Visual Speech Recognition (VSR) systems commonly rely on left-to-right autoregressive decoding, which can force premature decisions on visually ambiguous tokens before sufficient context is available. We propose DLLM-VSR, to the best of our knowledge, the first Diffusion Large Language Model (DLLM)-based VSR framework, formulating transcription as iterative masked denoising with flexible-order decoding. With confidence-based unmasking, DLLM-VSR commits high-confidence positions early and uses the committed...

### 9. Inpainting-Style Conditional Diffusion for Multivariable Time Series Forecasting

- 方向：底层视觉
- 作者：Kourosh Kiani, S. M. Muyeen
- 日期：2026-05-27
- 关键词：denoising
- arXiv：2605.28324v1

摘要：

In this paper, we propose a novel conditional diffusion-based framework for multivariable time-series solar power forecasting. The proposed method reformulates temporal PV data as structured two-dimensional representations (images) using a sliding-window patch construction, enabling the application of Denoising Diffusion Probabilistic Models (DDPM) within a unified spatiotemporal learning paradigm. A key contribution of this work is the formulation of solar forecasting as an inpainting problem, where future time st...

### 10. DebFilter: Eradicating Biases Stashed in Value

- 方向：底层视觉
- 作者：Seung Hyuk Lee, Songkuk Kim
- 日期：2026-05-27
- 关键词：denoising
- arXiv：2605.28167v1

摘要：

Text-to-image diffusion models, which are theoretically equivalent to score-based generative models, generate images through a multi-step denoising process guided by text embeddings extracted from pretrained vision-language models such as CLIP. However, these text embeddings inherently encode social and semantic biases -- such as those related to gender and age -- that are subsequently propagated and amplified through the guidance mechanism, along with the model's training on large-scale datasets that are imbalance...

## 说明

本内容由自动脚本按关键词筛选生成。筛选关键词包括 image restoration、super-resolution、denoising、deblurring、video compression、frame interpolation、CVPR 等。
