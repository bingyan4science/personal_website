---
layout: research-guide
title: Molecular representations and chemical reasoning
guide_order: 1
image: /images/consistency.png
topics: SMILES and IUPAC names · StructChem · ReasonFlow
question: How do molecular notation and intermediate reasoning steps affect a model’s predictions?
description: A reading guide to SMILES and IUPAC consistency in language models, structured prompting with StructChem, and latent flow matching with ReasonFlow.
permalink: /research/chemistry-language-models/
reviewed: '2026-11-09'
---

Imagine asking a model to predict a reaction product twice. In the first prompt, the reactants are SMILES strings. In the second, the same reactants appear as IUPAC names. Three outcomes matter. The predictions can disagree, agree on the correct product, or agree on the same wrong product. Reporting agreement alongside accuracy distinguishes those outcomes. [Yan, Chen and Cho, *Digital Discovery* (2025)](https://doi.org/10.1039/D5DD00176E)

## Which evidence answers your question?

- **Does the prediction change for the same molecule?** Yan, Chen and Cho paired SMILES and IUPAC inputs for reaction and property prediction. Their consistency regularizer improved agreement in their fine-tuning experiments without improving accuracy. [Paper and results](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00176e)
- **Can a model handle different SMILES for the same reactant?** In Graph2SMILES, Tu and Coley encode reactants as molecular graphs and decode the predicted products as a SMILES sequence. The graph encoder is invariant to atom ordering. This gives a baseline for studying why two valid SMILES strings for the same input molecule can yield different predictions from a text model. [Tu and Coley, *Journal of Chemical Information and Modeling* (2022)](https://doi.org/10.1021/acs.jcim.2c00321)
- **What can a model learn about molecules from reaction equations?** MolR learns molecular embeddings by bringing the sum of the reactant vectors close to the sum of the product vectors. Given reactants from a held-out reaction, Wang and colleagues use that distance to rank candidate products. They also evaluate the learned representations on molecular property prediction. [Wang et al., ICLR 2022](https://openreview.net/forum?id=6sh3pIzKS-)

## Repeat the paired-input test

The public dataset contains matched SMILES and IUPAC examples for forward reaction prediction, retrosynthesis and property prediction. Start with the forward-reaction test split. Keep the model, instructions and decoding settings fixed across each pair. Check whether the predictions identify the same chemical product, then score each prediction against the reference. The repository includes an evaluation script and a consistency calculation. [Paired data on Zenodo](https://doi.org/10.5281/zenodo.14430369) · [Code and evaluation instructions](https://github.com/bingyan4science/consistency)

## When does step-by-step reasoning help?

StructChem guides a language model through a quantitative chemistry problem with prompts for selecting formulas, applying them, and checking the calculation. [StructChem, ICML 2024](https://proceedings.mlr.press/v235/ouyang24a.html)

ReasonFlow is a **latent flow-matching method**. During training, a Qwen language model encodes intermediate solution steps as points along a continuous path. At inference, the flow follows a learned trajectory from noise, and a decoder reads out the final answer. On the spectroscopy-to-structure task, adding intermediate supervision increased exact-match accuracy from 14.0% to 19.5% in the paper’s single-seed comparison. [ReasonFlow, architecture and Table 1](https://aclanthology.org/2026.findings-emnlp.2268.pdf#page=5)
