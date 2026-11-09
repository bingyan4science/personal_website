---
layout: research-guide
title: Chemistry literature synthesis
guide_order: 3
image: /images/askchem-figure.png
topics: AskChem · Citation recommendation · Chemical data extraction
question: Which experiment supports a claim in the chemistry literature?
description: Find chemistry papers through their references, trace claims to experiments with AskChem, and compare synthesis conditions extracted from the zeolite literature.
permalink: /research/chemistry-literature-synthesis/
reviewed: '2026-11-09'
---

Suppose a review says nickel sulfide restructures during oxygen reduction. To use that result in a paper, a chemist needs to know which nickel sulfide the authors tested, what electrolyte they used, and how they identified the new surface. Those details determine whether the experiment supports a claim about a particular material or a wider class of catalysts.

## Find a claim and follow it to the experiment

AskChem lets a reader search individual findings across chemistry papers. Each extracted claim carries a source DOI and either a quotation or a locator for the evidence. Try a query such as *nickel sulfide surface restructuring during oxygen reduction*. In the original study, spectroscopy and microscopy helped identify a surface film of nominal NiS composition on Ni₃S₂. The proposed coordination of the active nickel sites came from calculations. A review can cite the same paper for both points while identifying the evidence for each. [AskChem](https://askchem.org/) · [AskChem system paper](https://aclanthology.org/2026.emnlp-demos.69/) · [Nickel sulfide study](https://doi.org/10.1016/j.joule.2017.08.020) · [Guide to the mechanistic evidence]({{ '/research/catalysis-mechanisms/' | relative_url }})

## Follow references and compare experiments across papers

Nogueira, Jiang, Cho, and Lin studied how to recommend references for a draft paper. Their system uses the title and abstract to find an initial set of articles, follows references from promising candidates, and ranks the expanded set. A chemist can use the same approach to trace an observation back through a review to the group that made the measurement. [Citation recommendation study](https://doi.org/10.1007/s11192-020-03718-9)

Once several experiments are in hand, deciding which results can be compared takes chemical judgment. Jensen and colleagues extracted zeolite synthesis conditions from text and tables, then used the reported conditions to predict the framework density of germanium-containing zeolites. Their public dataset makes a useful reading exercise. Choose one synthesis and check its reported composition and crystallization conditions against the original article before comparing it with another preparation. [Zeolite literature extraction study](https://doi.org/10.1021/acscentsci.9b00193) · [Extracted synthesis data](https://synthesisproject.mit.edu/research-2)

## Work with the evidence programmatically

AskChem documents `GET /v1/search` for finding candidate claims and `GET /v1/claims/{claim_id}` for inspecting a claim and its provenance. Save the evidence locator together with the DOI. In the index evaluated in the AskChem paper, 70% of papers were processed from abstracts alone. When a conclusion depends on an instrument setting, control experiment, or numerical uncertainty, follow the DOI to the methods, figure, or supplement before citing it. [API reference](https://askchem.org/api/docs) · [Python and agent examples](https://github.com/bingyan4science/askchem)
