---
layout: research-guide
title: Molecular representations and latent reasoning in chemistry
guide_order: 1
image: /images/consistency.png
topics: SMILES and IUPAC consistency · Chain-of-thought supervision · Flow matching
question: How do molecular notation and reasoning steps affect chemical predictions?
description: Study SMILES and IUPAC consistency, then see how ReasonFlow uses chain-of-thought supervision in latent flow matching to predict molecular structures from spectra.
permalink: /research/chemistry-language-models/
reviewed: '2026-11-10'
---

A chemist identifying a molecule from spectra may recognize several substructures before writing the final SMILES string. Those intermediate assignments can serve as training targets for a model learning to read spectra. Once a molecule is known, its notation raises a different question. If the same molecule is given as a SMILES string or an IUPAC name, does the model make the same prediction?

<span id="when-does-step-by-step-reasoning-help"></span>

## How can flow matching learn from a chain of thought? {#reasonflow}

ReasonFlow uses worked solutions to train a continuous generative model. A language model encodes progressively longer prefixes of each solution as vectors. These vectors act as anchors along a path that the flow model learns to follow. At inference, given only the question, the model starts from noise, follows its learned flow, and decodes the answer at the endpoint. This is one way to use chain-of-thought supervision for latent reasoning when a reasoning trace is available only during training. [Yan et al., *ReasonFlow: Flow Matching that Thinks Step by Step*, Findings of EMNLP 2026](https://aclanthology.org/2026.findings-emnlp.2268/)

On **MolPuzzle**, the task is to infer a molecular structure from spectra, and the training traces identify substructures. ReasonFlow recovered the reference SMILES on 19.5% of test examples in the reported single-seed comparison. A flow model trained on questions and final answers reached 14.0%, and a language model trained to generate the reasoning steps reached 24.6%. Those scores measure the final structure. To evaluate the chemical explanation itself, one would also need to check the substructure assignments. The paper also evaluates retrosynthesis, reaction mechanisms, arithmetic, and logical deduction. [ReasonFlow, Table 1](https://aclanthology.org/2026.findings-emnlp.2268.pdf#page=6) · [Code and GSM8K reproduction instructions](https://github.com/bingyan4science/reasonflow)

Two related methods illustrate different uses of worked steps. **StructChem** prompts a language model to choose formulas, carry out a calculation, and check its answer to a quantitative chemistry problem. In **implicit chain-of-thought reasoning**, Deng, Choi and Shieber fine-tune a language model while gradually removing written steps from its training examples. Their arithmetic experiments test whether the model can still give the final answer once those steps are removed. [Ouyang et al., StructChem, ICML 2024](https://proceedings.mlr.press/v235/ouyang24a.html) · [Deng et al., NeurIPS 2024](https://arxiv.org/abs/2405.14838)

## Does a model give the same answer for SMILES and IUPAC names? {#which-evidence-answers-your-question}

Imagine predicting a reaction product twice, first with SMILES strings for the reactants and then with IUPAC names. The predictions can disagree, agree on the correct product, or agree on the same wrong product. Reporting agreement alongside accuracy distinguishes those outcomes. [Yan, Chen and Cho, *Digital Discovery* (2025)](https://doi.org/10.1039/D5DD00176E)

- **Does the prediction change for the same molecule?** Yan, Chen and Cho paired SMILES and IUPAC inputs for reaction and property prediction. Their consistency regularizer improved agreement in their fine-tuning experiments without improving accuracy. [Paper and results](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00176e)
- **Can a model handle different SMILES for the same reactant?** In Graph2SMILES, Tu and Coley encode reactants as molecular graphs and decode the predicted products as a SMILES sequence. The graph encoder is invariant to atom ordering. This gives a baseline for studying why two valid SMILES strings for the same input molecule can yield different predictions from a text model. [Tu and Coley, *Journal of Chemical Information and Modeling* (2022)](https://doi.org/10.1021/acs.jcim.2c00321)
- **What can a model learn about molecules from reaction equations?** MolR learns molecular embeddings by bringing the sum of the reactant vectors close to the sum of the product vectors. Given reactants from a held-out reaction, Wang and colleagues use that distance to rank candidate products. They also evaluate the learned representations on molecular property prediction. [Wang et al., ICLR 2022](https://openreview.net/forum?id=6sh3pIzKS-)

## Repeat the paired-input test

The public dataset contains matched SMILES and IUPAC examples for forward reaction prediction, retrosynthesis and property prediction. Start with the forward-reaction test split. Keep the model, instructions and decoding settings fixed across each pair. Check whether the predictions identify the same chemical product, then score each prediction against the reference. The repository includes an evaluation script and a consistency calculation. [Paired data on Zenodo](https://doi.org/10.5281/zenodo.14430369) · [Code and evaluation instructions](https://github.com/bingyan4science/consistency)
