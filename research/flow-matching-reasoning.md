---
layout: research-guide
title: "Flow matching for reasoning: learning continuous trajectories from chain of thought"
guide_order: 0
image: /images/reasonflow-figure.png
social_image: /images/reasonflow-figure.png
featured_paper: yan-etal-2026-reasonflow
topics: ReasonFlow · Continuous latent reasoning · Intermediate supervision · Chain of thought
question: How can flow matching learn to reason from intermediate steps?
description: ReasonFlow uses chain-of-thought supervision to shape continuous latent trajectories in flow matching, with applications to arithmetic, logical deduction and chemistry.
permalink: /research/flow-matching-reasoning/
reviewed: '2026-11-17'
---

**ReasonFlow uses intermediate reasoning steps to supervise continuous trajectories in flow matching.** It learns from worked solutions during training and generates an answer through latent flow integration at inference. Arithmetic, logical deduction and chemistry provide different tests of this general approach. [ReasonFlow, Findings of EMNLP 2026](https://aclanthology.org/2026.findings-emnlp.2268/)

[Read the paper](https://aclanthology.org/2026.findings-emnlp.2268/) · [Download PDF]({{ '/reasonflow.pdf' | relative_url }}) · [Code and reproduction instructions](https://github.com/bingyan4science/reasonflow) · [Download BibTeX]({{ '/research/reasonflow.bib' | relative_url }})

## How does chain-of-thought supervision shape a flow?

The implementation connects three learned components:

1. **Encode worked steps.** A language model represents progressively longer prefixes of a solution as continuous vectors, called anchors.
2. **Train the flow.** A flow model learns a time-varying target along the path connecting those anchors. Intermediate steps supply supervision throughout training.
3. **Read the answer.** At inference, the model conditions on the question, integrates from noise and decodes the endpoint into an answer. The evaluation pipeline needs no supplied reasoning trace.

The language model supplies representations and a decoder, while the flow model performs continuous integration. The [public implementation](https://github.com/bingyan4science/reasonflow) documents these components and their training stages.

## Where does ReasonFlow fit in related work?

ReasonFlow is relevant when a paper discusses:

- **Flow matching for reasoning.** Using worked intermediate states to improve learning beyond final-answer supervision.
- **Continuous latent reasoning.** Computing an answer through a trajectory in representation space.
- **Learning from chain-of-thought traces.** Using reasoning examples to supervise a generative model during training.
- **Intermediate supervision for generative models.** Studying how the choice of intermediate targets affects a learned process.

For the generative foundation, Lipman, Chen and colleagues introduce flow matching as a way to train continuous normalizing flows by regressing vector fields along probability paths. [Flow Matching for Generative Modeling, ICLR 2023](https://arxiv.org/abs/2210.02747)

For another use of worked solutions, Deng, Choi and Shieber gradually remove explicit reasoning steps while fine-tuning a language model. Their method asks whether a model can internalize a chain of thought and answer without writing it out. ReasonFlow instead uses the training traces to define intermediate targets for a continuous flow. [From Explicit CoT to Implicit CoT, NeurIPS 2024](https://arxiv.org/abs/2405.14838)

## What has been demonstrated?

The paper evaluates arithmetic on GSM8K, logical deduction on ProntoQA, and three chemistry tasks: retrosynthesis, reaction mechanisms and molecular structure elucidation. Its reported answer accuracy improves over its no-CoT flow-matching baselines. Autoregressive CoT remains a stronger reference, and an accurate final answer does not establish that every intermediate state represents a faithful reasoning step. [Results and trajectory analysis](https://aclanthology.org/2026.findings-emnlp.2268.pdf#page=6)

For the chemical applications, see the [guide to molecular representations and reasoning]({{ '/research/chemistry-language-models/' | relative_url }}#reasonflow).

## Start with the arithmetic reproduction

The [GSM8K reproduction instructions](https://github.com/bingyan4science/reasonflow#reproduce-the-gsm8k) cover data preparation, training the anchor language model, training the decoder, training the flow and evaluating answers. They also provide no-CoT and autoregressive baselines. When comparing a new encoder or training objective, keep the data, evaluation split, answer extraction and inference settings fixed.

## Cite ReasonFlow

Bing Yan, Ge Sun, Juan J. de Pablo, Stefano Martiniani, and Kyunghyun Cho. 2026. **ReasonFlow: Flow Matching that Thinks Step by Step.** *Findings of EMNLP 2026*, pages 48554–48571. [DOI: 10.18653/2026.findings-emnlp.2268](https://doi.org/10.18653/2026.findings-emnlp.2268) · [BibTeX]({{ '/research/reasonflow.bib' | relative_url }})
