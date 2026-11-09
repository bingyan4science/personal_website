---
layout: research-guide
title: Catalytic mechanisms and selectivity
guide_order: 4
image: /images/Joule2017.jpg
topics: Electrochemical and thermal catalysis · SPARK for reaction kinetics · CatScore for catalyst design
question: What evidence identifies an active catalyst or explains its selectivity?
description: Explore how SPARK uses voltammetry, Tafel data, and thermal catalytic rates to test mechanisms and plan experiments, and how CatScore evaluates catalyst selectivity.
permalink: /research/catalysis-mechanisms/
reviewed: '2026-11-09'
---

A catalyst can change composition during a reaction. Even when its structure is known, the current measured at an electrode can reflect events at different interfaces. When reading a mechanistic study, ask what the authors measured under reaction conditions and which part of their explanation depends on a model.

## Which surface reduces oxygen on nickel sulfide?

Yan and colleagues studied oxygen reduction on heazlewoodite (Ni₃S₂) in a neutral aqueous electrolyte. Electrochemical measurements, surface spectroscopy, and microscopy showed that the crystallites developed a thin, disordered surface layer of nominal NiS composition. Density functional calculations suggested why the reconstructed surface could be active. Nickel sites with three sulfur neighbors had favorable oxygen-reduction energetics. The paper is a useful reference for the observed change in surface composition and the proposed relationship between local coordination and activity. [Joule study](https://doi.org/10.1016/j.joule.2017.08.020) · [Open manuscript at MIT](https://dspace.mit.edu/entities/publication/ecbf2c60-4b3d-4306-9681-9fafcdd2d60e)

Once an experiment identifies a candidate surface, a computational question follows. How will an adsorbed molecule bind to a particular arrangement of surface atoms? Chanussot and colleagues’ Open Catalyst 2020 (OC20) dataset benchmarks predictions of forces, relaxed structures, and energies against density functional calculations for adsorbates on specified surfaces. In the nickel sulfide study, identifying which surface formed under oxygen-reduction conditions required spectroscopy and microscopy. [OC20 dataset and benchmarks](https://doi.org/10.1021/acscatal.0c04525)

## Where do bond activation and charge transfer occur?

A membrane experiment makes the location of each step testable. Yan and colleagues placed a tungsten oxide membrane that conducts electrons and protons between platinum and an aqueous electrolyte. The electrode still oxidized hydrogen. Their mechanistic measurements placed hydrogen activation at the platinum–gas interface and electron–proton charge separation at the oxide–solution interface. Hydrogen diffusion through the oxide coupled the two processes. [JACS membrane study](https://doi.org/10.1021/jacs.9b03327)

Wesley, Román-Leshkov, and Surendranath explored the role of the interface in a thermal reaction, ethylene hydrogenation on carbon-supported platinum. They tracked the platinum potential during the reaction and changed it in two ways, by varying pH in water and by adding redox buffers in an organic solvent. Hydrogenation rates showed a similar dependence on open-circuit potential in both media. The comparison gives a reason to measure catalyst potential even in a reactor with no applied voltage. [Ethylene hydrogenation study](https://doi.org/10.1021/acscentsci.1c00293)

## How can SPARK use kinetic measurements to choose the next experiment? {#spark}

Two mechanisms can reproduce the same reaction rate yet predict different amounts of adsorbed hydrogen or CO on a catalyst. SPARK (Simulation-based Posterior Amortization for Reaction Kinetics) uses simulations of each reaction system to infer which pathways and kinetic parameters are consistent with the measurements. The manuscript revisits three published experiments and proposes a measurement for each.

- **Cyclic voltammetry of a cobalt porphyrin.** Sheng, Sun, and colleagues observed a peak on the return scan. SPARK’s analysis suggests that further reduction can account for that peak. Preparing the cobalt–alkyl product independently and measuring its voltammogram would test its contribution. [Sheng et al., original voltammetry study](https://doi.org/10.1038/s41467-024-47210-x)
- **Tafel data for hydrogen evolution on platinum.** Jung, Jackson, Bisbey, Kogan, and Surendranath measured the potential required to sustain a given current across pH. A Volmer–Heyrovsky pathway and one that also includes Tafel recombination both fit the potentials. Measuring adsorbed hydrogen across pH at fixed current would test their different predictions for surface coverage. [Jung et al., original hydrogen evolution study](https://doi.org/10.1016/j.joule.2022.01.007)
- **Thermal CO oxidation on platinum.** SPARK combines Allian and colleagues’ turnover rates and CO desorption measurements with calculated energies to compare direct and CO-assisted oxygen activation. At 0.01 kPa CO and 10 kPa oxygen, the two routes predict similar CO coverage at 358 K and a larger difference at 463 K. Measuring adsorbed CO at both temperatures would test that prediction. [Allian et al., original thermal catalysis study](https://doi.org/10.1021/ja110073u)

The public demo runs the cyclic voltammetry model. Try the simulated electron-transfer example to see which mechanisms reproduce the current at several scan rates. The manuscript, *SPARK: Learning unseen chemistry to plan experiments*, is in preparation. [Try the CV demo](https://huggingface.co/spaces/bing-yan/spark) · [Demo documentation](https://huggingface.co/spaces/bing-yan/spark/blob/main/README.md) · [Manuscript listing in Bing Yan’s CV]({{ '/cv/Bing_Yan_CV.pdf' | relative_url }}#page=2)

## How should a proposed asymmetric catalyst be scored?

For asymmetric olefin hydrogenation, the practical question is which catalyst to test first for a given substrate. CatScore predicts product selectivity from the reactants and the proposed catalyst. Yan and Cho reported a Spearman rank correlation of 0.84 between predicted and experimental selectivities in their instance-level evaluation. To adapt this test to another catalyst family, specify the selectivity to predict and reserve previously unseen ligand scaffolds for evaluation. [CatScore paper](https://doi.org/10.1039/D4DD00114A) · [CatScore code and data](https://github.com/bingyan4science/CatScore)
