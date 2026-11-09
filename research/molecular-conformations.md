---
layout: research-guide
title: Molecular conformation generation
guide_order: 2
image: /images/eva-flow-figure.svg
topics: EVA-Flow · Protein-bound conformers · Energy-based sampling
question: How does a molecule's 3D shape change between vacuum, water, a protein pocket and a crystal?
description: A reading guide to environment-aware conformer generation, ligand docking, energy-based sampling, and how to compare molecular conformation benchmarks.
permalink: /research/molecular-conformations/
reviewed: '2026-11-09'
---

A rotatable bond gives a molecule several possible shapes. Which ones appear can depend on neighboring water molecules, the shape of a protein pocket or contacts in a crystal. For modeling, two decisions follow. What information about the surroundings will be available at inference? Do you need the molecule's internal geometry, its position relative to a receptor, or samples from a specified energy distribution? [EVA-Flow, problem formulation and environment inputs](https://arxiv.org/html/2610.36280v1#S3.SS1)

## What does each method predict?

- **Conformers from a molecular graph.** Mansimov, Mahmood, Kang and Cho trained a generative graph neural network to predict sets of 3D atomic coordinates from molecular connectivity. Torsional Diffusion takes a different approach to the same task. It samples rotations around flexible bonds while keeping the local bond geometry fixed. These papers offer two starting points when the molecular graph is known and the environment is unspecified. [Mansimov et al., *Scientific Reports* (2019)](https://doi.org/10.1038/s41598-019-56773-5) · [Jing et al., NeurIPS 2022](https://papers.nips.cc/paper_files/paper/2022/hash/994545b2308bbbbc97e3e687ea9e464f-Abstract-Conference.html)
- **Conformers in a known environment.** EVA-Flow generates centered molecular coordinates using a shared model. Its conditioning inputs include a protein pocket for the bound ligand, solvent descriptors for water, and lattice parameters and space group for crystal packing. The largest gains from cross-environment training occurred in the three settings with less data. [Yan et al., EVA-Flow, TMLR 2026](https://openreview.net/forum?id=pD4Smou3Xp)
- **A ligand pose relative to a protein.** DiffDock samples the ligand's translation, orientation and torsions given the protein and ligand. It is a relevant comparison when a prediction must locate a binding site and place the molecule in the receptor's coordinate frame. [Corso et al., DiffDock](https://arxiv.org/abs/2210.01776)
- **Atomistic conformations from coarse coordinates.** A coarse-grained simulation supplies a 3D position for each group of atoms. Several atomistic configurations can fit those same positions. Wang and colleagues model this ambiguity by sampling fine-grained coordinates conditioned on the coarse structure, a task called backmapping. [Wang et al., ICML 2022](https://proceedings.mlr.press/v162/wang22ag.html)
- **Samples from a specified energy function.** Adjoint Sampling trains a diffusion sampler using an unnormalized target density. The molecular experiments use a neural energy model across many molecules. The authors provide code and benchmarks for testing energy-based conformer generation. [Havens et al., ICML 2025](https://proceedings.mlr.press/v267/havens25a.html) · [Code and benchmarks](https://github.com/facebookresearch/adjoint_sampling)

## How should you compare conformer sets?

Count coverage in both directions. **Recall coverage** asks what fraction of reference conformers have a generated neighbor within a chosen root-mean-square deviation (RMSD). **Precision coverage** reverses the question and checks what fraction of generated conformers have a nearby reference. Report the threshold, alignment procedure, reference set and number of generated conformers per molecule. Sampling more candidates gives a method more chances to recover a reference shape. [EVA-Flow, evaluation metrics](https://arxiv.org/html/2610.36280v1#A4)

For a vacuum comparison, EVA-Flow Table 3 uses GEOM-DRUGS and generates twice as many conformers as there are references for each molecule. Table 2 uses four generated conformers per molecule across environments. For a question about *changes in shape*, Appendix G follows molecules that occur in more than one environment, holding molecular identity fixed. [Experimental results and shared-molecule controls](https://arxiv.org/html/2610.36280v1)

To repeat the comparison, the EVA-Flow model card lists an evaluation command for each environment. Use one unified checkpoint across the four runs and record which environment configuration you used. Access to the release requires a request through Hugging Face. [EVA-Flow model card and evaluation instructions](https://huggingface.co/facebook/eva-flow)
