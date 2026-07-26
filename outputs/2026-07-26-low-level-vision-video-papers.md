---
title: 2026-07-26｜底层视觉与视频论文速览
author: AI论文助手
digest: 每周自动抓取 arXiv 计算机视觉方向论文，筛选底层视觉与视频处理相关工作，并汇总摘要、链接与关键词。
cover: ../images/cover.png
---

# 2026-07-26｜底层视觉与视频论文速览

生成时间：2026-07-26

本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 30 篇，排序优先考虑关键词命中数量，其次参考提交时间。

## 快速列表

1. 底层视觉｜Decoupling Cross-Modality Manifold Discrepancy: Leveraging Visible Diffusion Priors for Infrared Super-Resolution｜2026-07-23
2. 底层视觉｜The Second LoViF 2026 Challenge on Real-World All-in-One Image Restoration: Methods and Results｜2026-07-23
3. 底层视觉｜The RealDefocus Benchmark for Defocus Deblurring｜2026-07-23
4. 底层视觉、视频处理｜RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring｜2026-07-22
5. 底层视觉、视频处理｜Group-of-Latents: Perceptual Video Compression at Extreme Bitrates via Masked Latent Generative Modeling｜2026-07-21
6. 底层视觉｜Rarity-Aware Discrete Diffusion with Spatially Consistent Decoding for Photo-Realistic Image Super-Resolution｜2026-07-20
7. 底层视觉｜Towards Robust Iris Recognition Through Occlusion Identification and Conditional Diffusion-Based Reconstruction｜2026-07-23
8. 底层视觉｜CLUIE: Clustering-Aware Recurrent Propagation with Local Structural Compensation for Underwater Image Enhancement｜2026-07-23
9. 底层视觉｜KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers｜2026-07-23
10. 底层视觉｜PC-Edit: Prompt-Contrastive Region Discovery and Region-Guided Editing｜2026-07-23
11. 视频处理｜DART: A Degradation-Aware Recurrent Transformer for Archival Film Restoration｜2026-07-23
12. 底层视觉｜Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents｜2026-07-23
13. 底层视觉｜Ms. Forcing: Efficient Streaming Video Generation with Multi-Scale Patchification and Attention｜2026-07-23
14. 底层视觉｜Self Gradient Forcing: Native Long Video Extrapolation｜2026-07-22
15. 底层视觉｜Evolving Cache Schedules for Fast Diffusion Policy Inference｜2026-07-22
16. 视频处理｜BLUE: Semantics-Preserving Video Compression for Efficient Vision-Language Surveillance Analytics｜2026-07-21
17. 底层视觉｜ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling｜2026-07-21
18. 底层视觉｜ERank in Latent Space as an Image-Complexity and Richness Measure｜2026-07-21
19. 底层视觉｜Text Template Tokens Are Implicit Semantic Registers in Diffusion Transformers｜2026-07-21
20. 底层视觉｜Wavefront Parallelization for Efficient Learned Image Compression｜2026-07-21
21. 底层视觉｜SynGallery: A Synthetic Gallery of Real Paintings for Instance-Level Artwork Recognition｜2026-07-21
22. 底层视觉｜Think Sparse, Predict Dense: Continuous Thought Machines for Image Super-Resolution｜2026-07-21
23. 底层视觉｜Surprise Forcing: What to Remember, When to Skip in Long Video Generation｜2026-07-20
24. 底层视觉｜Luminosity-Adaptive Contrast Enhancement Using CLAHE for Retinal Fundus Images with Quantitative Validation and Comparative Analysis｜2026-07-20
25. 底层视觉｜MixDiffusion: Mixing Diffusion-based Uni-condition Text-to-Image Generation Models for Multi-condition Image Synthesis｜2026-07-20
26. 底层视觉｜Pixel-Space Diffusion Transformers｜2026-07-20
27. 视频处理｜Generative Transmission: Rethinking Computation, Bandwidth, and Memory in Communication｜2026-07-20
28. 底层视觉｜Denoising Models Develop Human-Like Perceptual Illusion Representations Across Architectures｜2026-07-19
29. 底层视觉｜HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis｜2026-07-19
30. 底层视觉｜Splat-based 3D Scene Reconstruction with Extreme Motion-blur｜2026-07-18

## 论文摘要

### 1. Decoupling Cross-Modality Manifold Discrepancy: Leveraging Visible Diffusion Priors for Infrared Super-Resolution

- 方向：底层视觉
- 作者：Yunpeng Hua, Hongwei Yu, Jiawei Li, Qiankun Liu, Huimin Ma, Jiansheng Chen
- 日期：2026-07-23
- 分类：cs.CV
- 关键词：image super-resolution、denoising
- arXiv：2607.21174v1

摘要：

Infrared image super-resolution (IISR) mitigates the limitations imposed by low spatial resolution. Existing methods have recognized that IISR should preserve consistency in global distribution and structural information while enhancing image clarity. However, these methods are either insufficient or overly intrusive, a problem that becomes even more pronounced in diffusion-based models. To address these issues, we propose a dual-path diffusion-based framework for IISR, termed Shift-IISR. The proposed method is des...

### 2. The Second LoViF 2026 Challenge on Real-World All-in-One Image Restoration: Methods and Results

- 方向：底层视觉
- 作者：Xiang Chen, Hao Li, Jiangxin Dong, Jinshan Pan, Xin Li, Hongbo Ding, et al.
- 日期：2026-07-23
- 分类：cs.CV
- 关键词：image restoration、low-level vision
- arXiv：2607.21118v1

摘要：

This paper presents a review of the second LoViF Challenge on Real-World All-in-One Image Restoration. The challenge aims to advance unified image restoration under diverse real-world degradation conditions, including blur, low-light, haze, rain, and snow. It provides a common benchmark for evaluating the restoration accuracy, robustness, and generalization capability of models across multiple degradation categories within a unified framework. The competition attracted 158 registered participants, and 20 teams were...

### 3. The RealDefocus Benchmark for Defocus Deblurring

- 方向：底层视觉
- 作者：Tim Seizinger, Zhuyun Zhou, Radu Timofte
- 日期：2026-07-23
- 分类：cs.CV
- 关键词：image restoration、deblurring
- arXiv：2607.21078v1

摘要：

Single-Image Defocus Deblurring (SIDD) aims to recover an all-in-focus image from a single defocused observation, but rigorous and reproducible evaluation remains challenging due to the scarcity of realistic, high-resolution datasets with well-aligned defocused/sharp pairs and standardized protocols. We build on RealDefocus, a benchmark derived from the real-world RealBokeh dataset originally proposed for Bokeh Rendering. RealDefocus provides paired defocused inputs and sharp ground truth images, predefined trainin...

### 4. RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring

- 方向：底层视觉、视频处理
- 作者：Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, et al.
- 日期：2026-07-22
- 分类：cs.CV, cs.AI
- 关键词：deblurring、video deblurring
- arXiv：2607.20628v1

摘要：

Real-world video deblurring remains challenging due to diverse motion patterns, complex degradations, and the scarcity of realistic training data, yet robust restoration is critical for downstream pipelines such as mobile imaging and 3D reconstruction. This work presents \textbf{RealVDeblur}, an efficient generative framework designed to improve in-the-wild robustness under diverse real capture conditions. First, a large-scale, physically grounded blur synthesis pipeline is constructed from scene-level 3D Gaussian...

### 5. Group-of-Latents: Perceptual Video Compression at Extreme Bitrates via Masked Latent Generative Modeling

- 方向：底层视觉、视频处理
- 作者：Shaokang Wang, Jinchang Xu, Peidong Jia, Zhijian Hao, Siyuan Qian, Fei Zhao, et al.
- 日期：2026-07-21
- 分类：eess.IV, cs.CV, cs.MM
- 关键词：denoising、video compression
- arXiv：2607.19437v1

摘要：

Most existing video compression algorithms follow a paradigm of transformation and quantization, optimizing the trade-off between distortion and bitrate. However, extremely low-bitrate compression remains an underexplored frontier where perceptual quality optimization under severely constrained coding resources has not been adequately addressed. In this paper, we propose a unified generative framework that leverages pre-trained Diffusion Transformer (DiT) priors to achieve high perceptual quality at extremely low b...

### 6. Rarity-Aware Discrete Diffusion with Spatially Consistent Decoding for Photo-Realistic Image Super-Resolution

- 方向：底层视觉
- 作者：Ao Li, Yapeng Du, Yi Xin, Lei Zhu, Le Zhang, Guangtao Zhai, et al.
- 日期：2026-07-20
- 分类：cs.CV
- 关键词：image super-resolution、denoising
- arXiv：2607.17612v2

摘要：

Continuous diffusion models have become the dominant paradigm for photo-realistic image Super-Resolution (SR), but they typically formulate reconstruction as continuous signal-level denoising and incorporate semantic priors through external conditioning modules. This makes it less direct to exploit the unified token-based scaling paradigm of modern multimodal models. Autoregressive models provide a more native semantic representation by modeling images as discrete visual tokens, yet their causal decoding is ineffic...

### 7. Towards Robust Iris Recognition Through Occlusion Identification and Conditional Diffusion-Based Reconstruction

- 方向：底层视觉
- 作者：Kamrul Hasan, Mylene C. Q. Farias, Oleg V. Komogortsev
- 日期：2026-07-23
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.21545v1

摘要：

Iris recognition is a reliable biometric approach that identifies individuals using the distinctive and stable texture of the iris. However, recognition performance can degrade when discriminative iris texture is partially occluded by eyelids, eyelashes, specular reflections, or other acquisition artifacts. Existing approaches often perform recognition directly on degraded samples or rely only on the remaining visible iris region, which may be inadequate when substantial texture is corrupted. To address this limita...

### 8. CLUIE: Clustering-Aware Recurrent Propagation with Local Structural Compensation for Underwater Image Enhancement

- 方向：底层视觉
- 作者：Kui Jiang, Zefan Feng, Laibin Chang, Yan Luo, Junjun Jiang, Xiaopeng Fan
- 日期：2026-07-23
- 分类：cs.CV
- 关键词：image enhancement
- arXiv：2607.21467v1

摘要：

Underwater image enhancement remains challenging due to wavelength-dependent light absorption, scattering, and backscattering, which jointly cause color distortion, contrast degradation, and detail loss. Since these degradations vary with scene depth and imaging conditions, different regions within the same image often exhibit heterogeneous degradation patterns and thus require region-adaptive restoration. Although visual RWKV models offer an efficient linear-complexity solution for long-range dependency modeling,...

### 9. KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers

- 方向：底层视觉
- 作者：Yann Bouquet, Alireza Khodamoradi, Kristof Denolf, Mathieu Salzmann
- 日期：2026-07-23
- 分类：cs.LG, cs.CV
- 关键词：denoising
- arXiv：2607.21446v1

摘要：

Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot represent. The standard fix applies an invertible linear transform to the activations and its inverse to the weights before quantizing both. Normalization layers between blocks force this transform to run online at every denoising step, making its inference computation cost the binding design constraint. Existing options...

### 10. PC-Edit: Prompt-Contrastive Region Discovery and Region-Guided Editing

- 方向：底层视觉
- 作者：Jian Zhang, Zhijun Zhang
- 日期：2026-07-23
- 分类：cs.CV, cs.AI
- 关键词：denoising
- arXiv：2607.21318v1

摘要：

Replacing an object with one that differs in category or shape requires complete source removal, natural target formation unconstrained by the source silhouette, and preservation of unrelated content. Existing training-free editors either localize edits from terminal predictions under source and target prompts or preserve unrelated content through spatially unselective source-feature reuse without explicit region discovery. Before reaching the terminal predictions, prompt-induced semantic differences undergo additi...

### 11. DART: A Degradation-Aware Recurrent Transformer for Archival Film Restoration

- 方向：视频处理
- 作者：Mikołaj Jastrzębski, Wojciech Kozłowski, Kamil Adamczewski
- 日期：2026-07-23
- 分类：cs.CV, cs.LG
- 关键词：video restoration
- arXiv：2607.21219v1

摘要：

Archival film restoration is a challenging problem because historical footage contains compound degradations such as scratches, dust, blur, noise, flicker, and photometric aging, while clean reference videos are unavailable. Existing video restoration methods largely treat these degradations implicitly, reconstructing frames without explicit knowledge of where damage occurs or how severe it is. We propose DART, a degradation-aware recurrent transformer for archival film restoration. DART predicts and propagates a s...

### 12. Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents

- 方向：底层视觉
- 作者：Hu Gao, Yulong Chen, Lizhuang Ma
- 日期：2026-07-23
- 分类：cs.CV
- 关键词：image restoration
- arXiv：2607.21125v1

摘要：

Image restoration agents have recently emerged as a flexible paradigm for handling diverse and unpredictable degradations in real-world scenarios. Existing agents typically formulate restoration as a tool-using process, where the agent perceives degradations, searches candidate tools, executes restoration operations, and revises the plan through reflection or rollback. However, their knowledge is often stored as static tool descriptions, manually defined degradation priors, or unstructured textual summaries, which...

### 13. Ms. Forcing: Efficient Streaming Video Generation with Multi-Scale Patchification and Attention

- 方向：底层视觉
- 作者：Zekun Li, Xiaoyan Cong, Hongyu Li, Zhiyang Dou, Chuan Guo, Abhay Mittal, et al.
- 日期：2026-07-23
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.20940v1

摘要：

Streaming video diffusion models have made substantial progress toward interactive and dynamic world simulation, but the nested autoregressive and denoising loops of conventional next-frame generation hinder real-time deployment. Recent rolling-window methods pipeline denoising across multiple consecutive frames at different noise levels, improving throughput and long-horizon stability. However, they tokenize every state at the same fine spatial granularity, leaving substantial noise-dependent redundancy in the joi...

### 14. Self Gradient Forcing: Native Long Video Extrapolation

- 方向：底层视觉
- 作者：Junhao Zhuang, Shiyi Zhang, Yuxuan Bian, Yaowei Li, Yawen Luo, Yijun Liu, et al.
- 日期：2026-07-22
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.20368v1

摘要：

Recent autoregressive video diffusion methods are increasingly built upon Self Forcing, where the student is trained on histories produced by its own rollout rather than ground-truth video contexts. This reduces exposure bias, but the historical key-value cache is still used by future frames only as frozen rollout state. As a result, future losses cannot supervise how earlier generated latents should be written into more useful keys and values for later video-latent generation. We call this the historical context-g...

### 15. Evolving Cache Schedules for Fast Diffusion Policy Inference

- 方向：底层视觉
- 作者：Siying Wang, Kangye Ji, Di Wang, Fei Cheng
- 日期：2026-07-22
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.20293v1

摘要：

Diffusion policies achieve strong visuomotor control by iteratively denoising action chunks, but repeated denoising makes real-time deployment computationally demanding. Cache-based methods reduce inference cost by reusing intermediate activations, but existing training-free schedules typically allocate computation uniformly across blocks, ignoring heterogeneous redundancy across blocks and leading to a suboptimal performance-efficiency trade-off. To bridge this gap, we introduce Evolving Cache Schedules (EVO), a t...

### 16. BLUE: Semantics-Preserving Video Compression for Efficient Vision-Language Surveillance Analytics

- 方向：视频处理
- 作者：Shubham Baid, Akash James, Sahil Chachra, Nishant Sinha, Kunal Kislay
- 日期：2026-07-21
- 分类：eess.IV, cs.CV
- 关键词：video compression
- arXiv：2607.19515v1

摘要：

Continuous surveillance video creates a growing storage, transmission, and inference burden for enterprise video analytics systems. While modern codecs such as H.265 reduce bitrate for human-viewable video, aggressive compression can degrade downstream computer-vision performance and does not necessarily reduce the number of vision-language model (VLM) inference calls required for semantic video understanding. This paper evaluates BLUE, a fixed-camera surveillance compression approach that suppresses static-backgro...

### 17. ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling

- 方向：底层视觉
- 作者：Chirag Vashist, Ke Li
- 日期：2026-07-21
- 分类：cs.LG, cs.CV
- 关键词：denoising
- arXiv：2607.19332v1

摘要：

Generative models have undergone many generations of evolution, from VAEs/GANs to diffusion/flow matching. Along the way, the underlying techniques have become more complicated and various beliefs about what drives strong empirical performance have taken hold. Due to the success of diffusion models and flow matching, one of the more common beliefs is the importance of transforming the noise distribution to the data distribution gradually through many small transformations. We ask whether this is truly necessary, an...

### 18. ERank in Latent Space as an Image-Complexity and Richness Measure

- 方向：底层视觉
- 作者：Maksim Smirnov, Grigory Kononov, Anastasiia Linich, Egor Surkov, Egor Shvetsov
- 日期：2026-07-21
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.19315v2

摘要：

We propose the effective rank (ERank) of the channel covariance of an image's deep feature map as a per-sample, label-free measure of visual richness, computed from a single forward pass through a frozen pretrained encoder. ERank counts how many decorrelated channel directions an image activates, and we characterize its properties, including its behavior under noise. Empirically, ERank orders images from plain to visually rich, correlates with codec bitrate, sharpness, and edge density, and correlates with human co...

### 19. Text Template Tokens Are Implicit Semantic Registers in Diffusion Transformers

- 方向：底层视觉
- 作者：Maohua Li, Qirui Li, Yanke Zhou, Yiduo Li, Zhaosheng Chi, Chao Xu, et al.
- 日期：2026-07-21
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.19139v1

摘要：

Text-to-image diffusion transformers (DiTs) jointly process text and image tokens, yet their internal computation during denoising remains poorly understood. We introduce a causal interpretability framework for modern large-scale DiTs that combines attention decomposition with targeted interventions across token spans, heads, and layers. Using it to separate prompt-content tokens from structural template tokens, we find that the structural tokens carry little prompt-specific information at the encoder output. Yet s...

### 20. Wavefront Parallelization for Efficient Learned Image Compression

- 方向：底层视觉
- 作者：Shimon Murai, Fangzheng Lin, Kasidis Arunruangsirilert, Jiro Katto
- 日期：2026-07-21
- 分类：eess.IV, cs.CV
- 关键词：image compression
- arXiv：2607.19082v1

摘要：

Autoregressive context models are foundational for learned image compression,but they suffer from slow serial inference. Existing acceleration methods such as checkerboard context require architectural changes and retraining, thus are inapplicable to pre-trained models. We propose a completely training-free inference-time acceleration algorithm inspired by wavefront parallelism in video coding standards. Our method reorganizes inference into an optimal ``staggered'' wavefront order, minimizing sequential steps whil...

### 21. SynGallery: A Synthetic Gallery of Real Paintings for Instance-Level Artwork Recognition

- 方向：底层视觉
- 作者：Patryk Bartkowiak, Jakub Markil, Bartosz Kotrys, Dominik Michels, Sören Pirk, Wojtek Palubicki
- 日期：2026-07-21
- 分类：cs.CV
- 关键词：image compression
- arXiv：2607.18907v1

摘要：

Instance-level artwork recognition requires matching a handheld visitor photograph to a specific work in a large museum collection. This is challenging because painting datasets typically provide clean catalog images for training, while test queries are captured under oblique viewpoints, gallery lighting, reflections, frames, and other scene-level variations. We present SynGallery, a synthetic gallery dataset for artwork retrieval that addresses this gap without collecting additional real photographs. Starting from...

### 22. Think Sparse, Predict Dense: Continuous Thought Machines for Image Super-Resolution

- 方向：底层视觉
- 作者：Zekai Shi
- 日期：2026-07-21
- 分类：cs.CV, eess.IV
- 关键词：image super-resolution
- arXiv：2607.18856v1

摘要：

Continuous Thought Machines introduce an internal temporal dimension in which neuron-level histories and synchronization-derived representations evolve over a sequence of thought ticks. Extending this mechanism to dense visual prediction is non-trivial, because tasks such as image super-resolution require spatial evidence to remain available at every output location rather than being compressed into a single global representation. In the proposed window-level use of CTM, the thought dynamics produce a compact summa...

### 23. Surprise Forcing: What to Remember, When to Skip in Long Video Generation

- 方向：底层视觉
- 作者：Shuwei Shi, Zhen Li, Muyao Niu, Chuanhao Li, Bo Zheng, Kaipeng Zhang, et al.
- 日期：2026-07-20
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.18436v1

摘要：

Streaming autoregressive diffusion makes minute-scale video synthesis practical, but its bounded context and fixed denoising schedule allocate resources uniformly across a highly non-stationary sequence. A rolling key-value cache forgets distant visual evidence even when that evidence remains important, while every generated chunk receives the same number of denoising passes irrespective of its actual difficulty. We introduce Surprise Forcing, a training-free framework that treats both limitations as online resourc...

### 24. Luminosity-Adaptive Contrast Enhancement Using CLAHE for Retinal Fundus Images with Quantitative Validation and Comparative Analysis

- 方向：底层视觉
- 作者：K. Mithra, Prem Kumar Santhanam
- 日期：2026-07-20
- 分类：eess.IV, cs.CV, cs.ET
- 关键词：image enhancement
- arXiv：2607.17691v1

摘要：

Background: Retinal fundus imaging is central to the early diagnosis of sight-threatening conditions including diabetic retinopathy, glaucoma, and retinal vein occlusion. Clinical utility of fundus images is routinely compromised by non-uniform illumination, motion blur, and low contrast - artefacts that increase the risk of diagnostic error. Effective image enhancement is therefore a prerequisite for reliable computer-aided ophthalmic diagnosis. Methods: This study proposes a two-stage image enhancement pipeline c...

### 25. MixDiffusion: Mixing Diffusion-based Uni-condition Text-to-Image Generation Models for Multi-condition Image Synthesis

- 方向：底层视觉
- 作者：Pengcheng Wan, Liang Han, Lin Xu, Bowen Xiao, Liqiang Nie
- 日期：2026-07-20
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.17634v1

摘要：

Recent advances in text-to-image (T2I) generation have enabled controllable image synthesis by incorporating conditions beyond text. However, most existing diffusion-based methods are limited to a single type of control condition (e.g., bounding boxes or keypoints), which restricts their flexibility. To address this limitation, we propose MixDiffusion, a training-free diffusion framework for multi-condition T2I generation. MixDiffusion theoretically supports an arbitrary number of control conditions, including boun...

### 26. Pixel-Space Diffusion Transformers

- 方向：底层视觉
- 作者：Renye Yan, Jikang Cheng, You Wu, Ling Liang, Wei Peng, Athanasios V. Vasilakos, et al.
- 日期：2026-07-20
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.17585v2

摘要：

Latent diffusion models (LDMs) enable efficient high-resolution image synthesis by denoising in a VAE-compressed latent space. However, fixed visual tokenizers can discard fine textures and structural details, while separate representation and diffusion training creates a mismatch between reconstruction and generation objectives. These limitations have renewed interest in pixel-space diffusion, which models raw pixels directly, removes the VAE bottleneck, and supports end-to-end optimization. This formulation bette...

### 27. Generative Transmission: Rethinking Computation, Bandwidth, and Memory in Communication

- 方向：视频处理
- 作者：Xiangyu Chen, Jixiang Luo, Yuankai Fan, Haibin Huang, Chi Zhang, Xuelong Li
- 日期：2026-07-20
- 分类：cs.CV
- 关键词：video compression
- arXiv：2607.17482v1

摘要：

Under the AI Flow framework, communication is shifting from transmitting fidelity-oriented information flows toward delivering task-oriented and perception-oriented token flows across heterogeneous network resources. Video communication is a fundamental component of modern information networks. However, under ultra-low-bandwidth and weak-network conditions, conventional video coding and transmission methods, which are primarily optimized for pixel-level fidelity, often struggle to balance visual usability, transmis...

### 28. Denoising Models Develop Human-Like Perceptual Illusion Representations Across Architectures

- 方向：底层视觉
- 作者：Gautam Ranka, Paras Chopra
- 日期：2026-07-19
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.17138v1

摘要：

Deep neural networks trained on natural images are shown to produce outputs consistent with human observers for brightness illusions. While this phenomenon has been documented across architectures, all evidence, to date, is measured at the output level: restored pixels, decoded trajectories, or classification decisions. Whether these models actually represent illusions internally, and if so where and how, remains unknown. We show that denoising models develop illusion-sensitive representations at specific internal...

### 29. HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis

- 方向：底层视觉
- 作者：Lingwei Dang, Juntong Li, Zonghan Li, Hongwen Zhang, Liang An, Wei Min, et al.
- 日期：2026-07-19
- 分类：cs.CV
- 关键词：denoising
- arXiv：2607.17097v1

摘要：

Hand-Object Interaction (HOI) synthesis is a cornerstone for animation production and embodied AI. Despite the strong priors of video foundation models, multi-view consistent HOI synthesis remains challenging due to complex hand motions and occlusions. We present HarmoHOI, a unified diffusion framework that jointly and harmoniously generates synchronized multi-view HOI videos and globally aligned 3D point tracks. Our core insight is that robust multi-view consistency fundamentally requires globally aligned 3D geome...

### 30. Splat-based 3D Scene Reconstruction with Extreme Motion-blur

- 方向：底层视觉
- 作者：Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim
- 日期：2026-07-18
- 分类：cs.CV
- 关键词：deblurring
- arXiv：2607.16926v1

摘要：

We propose a splat-based 3D scene reconstruction method from RGB-D input that effectively handles extreme motion blur, a frequent challenge in low-light environments. Under dim illumination, RGB frames often suffer from severe motion blur due to extended exposure times, causing traditional camera pose estimation methods, such as COLMAP, to fail. This results in inaccurate camera pose and blurry color input, compromising the quality of 3D reconstructions. Although recent 3D reconstruction techniques like Neural Radi...

## 关键词配置

本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。

Markdown 文件：`2026-07-26-low-level-vision-video-papers.md`
