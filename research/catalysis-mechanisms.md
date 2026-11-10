---
layout: research-guide
title: Inferring catalytic mechanisms from kinetic data
guide_order: 4
image: /images/Joule2017.jpg
topics: SPARK research project · Tafel analysis and thermal CO oxidation · CatScore for catalyst selectivity
question: How can we distinguish catalytic mechanisms that fit the same kinetic data?
description: Explore the ongoing SPARK project and how cyclic voltammetry, Tafel data, and thermal CO oxidation rates can distinguish competing catalytic mechanisms.
permalink: /research/catalysis-mechanisms/
reviewed: '2026-11-10'
---

Two reaction mechanisms can predict the same current or turnover rate. To distinguish them, look for a quantity on which their predictions diverge. For hydrogen evolution on platinum, that quantity can be the fraction of the surface occupied by hydrogen. For thermal CO oxidation, it can be how much CO remains adsorbed as the temperature rises.

## How does SPARK use kinetic data to plan the next experiment? {#spark}

We are developing SPARK (Simulation-based Posterior Amortization for Reaction Kinetics) to identify reaction pathways and rate constants that fit kinetic measurements. When several mechanisms fit the same data, we simulate each one under new conditions and look for a measurement that could distinguish them.

### Can Tafel data distinguish hydrogen evolution pathways on platinum? {#hydrogen-evolution-tafel}

Jung, Jackson, Bisbey, Kogan, and Surendranath measured the electrode potential needed to sustain a given current as they varied pH. In the SPARK analysis of these hydrogen evolution reaction (HER) data, a Volmer–Heyrovsky mechanism fits the potentials, and so does a mechanism that also allows Tafel recombination of two adsorbed hydrogen atoms. The models predict different hydrogen coverages. Measuring adsorbed hydrogen across pH while holding current fixed would test which pathway better explains the observations. [Jung et al., original Tafel measurements](https://doi.org/10.1016/j.joule.2022.01.007)

### Which measurement could distinguish oxygen activation routes in thermal CO oxidation? {#thermal-co-oxidation}

For thermal CO oxidation on platinum, two candidate pathways involve direct oxygen activation and CO-assisted oxygen activation. SPARK compares them using turnover rates and CO desorption measurements from Allian and colleagues, together with calculated energies. At 0.01 kPa CO and 10 kPa oxygen, the two routes predict similar CO coverage at 358 K, but their predictions diverge at 463 K. Measuring adsorbed CO at both temperatures would test that prediction. [Allian et al., original platinum CO oxidation study](https://doi.org/10.1021/ja110073u)

### What could explain a return peak in a cyclic voltammogram?

Sheng, Sun, and colleagues observed a return-scan peak in cyclic voltammetry of a cobalt porphyrin reacting with an organohalide. SPARK suggests that further reduction of the cobalt–alkyl product could contribute to the peak. Preparing that product independently and measuring its voltammogram would test the assignment. [Sheng et al., original voltammetry study](https://doi.org/10.1038/s41467-024-47210-x)

The SPARK manuscript is in preparation. You can explore the cyclic voltammetry model with a simulated electron-transfer example or upload current–potential curves at several scan rates to see which mechanisms reproduce them. [Try the SPARK demo](https://huggingface.co/spaces/bing-yan/spark) · [Demo documentation](https://huggingface.co/spaces/bing-yan/spark/blob/main/README.md)

## Which surface reduces oxygen on nickel sulfide?

Yan and colleagues studied oxygen reduction on heazlewoodite (Ni₃S₂) in a neutral aqueous electrolyte. Electrochemical measurements, surface spectroscopy, and microscopy showed that the crystallites developed a thin, disordered surface layer of nominal NiS composition. Density functional calculations suggested why the reconstructed surface could be active. Nickel sites with three sulfur neighbors had favorable oxygen-reduction energetics. The paper is a useful reference for the observed change in surface composition and the proposed relationship between local coordination and activity. [Joule study](https://doi.org/10.1016/j.joule.2017.08.020) · [Open manuscript at MIT](https://dspace.mit.edu/entities/publication/ecbf2c60-4b3d-4306-9681-9fafcdd2d60e)

Once an experiment identifies a candidate surface, a computational question follows. How will an adsorbed molecule bind to a particular arrangement of surface atoms? Chanussot and colleagues’ Open Catalyst 2020 (OC20) dataset benchmarks predictions of forces, relaxed structures, and energies against density functional calculations for adsorbates on specified surfaces. In the nickel sulfide study, identifying which surface formed under oxygen-reduction conditions required spectroscopy and microscopy. [OC20 dataset and benchmarks](https://doi.org/10.1021/acscatal.0c04525)

## Where do bond activation and charge transfer occur?

A membrane experiment makes the location of each step testable. Yan and colleagues placed a tungsten oxide membrane that conducts electrons and protons between platinum and an aqueous electrolyte. The electrode still oxidized hydrogen. Their mechanistic measurements placed hydrogen activation at the platinum–gas interface and electron–proton charge separation at the oxide–solution interface. Hydrogen diffusion through the oxide coupled the two processes. [JACS membrane study](https://doi.org/10.1021/jacs.9b03327)

Wesley, Román-Leshkov, and Surendranath explored the role of the interface in a thermal reaction, ethylene hydrogenation on carbon-supported platinum. They tracked the platinum potential during the reaction and changed it in two ways, by varying pH in water and by adding redox buffers in an organic solvent. Hydrogenation rates showed a similar dependence on open-circuit potential in both media. The comparison gives a reason to measure catalyst potential even in a reactor with no applied voltage. [Ethylene hydrogenation study](https://doi.org/10.1021/acscentsci.1c00293)

## How should a proposed asymmetric catalyst be scored?

For asymmetric olefin hydrogenation, the practical question is which catalyst to test first for a given substrate. CatScore predicts product selectivity from the reactants and the proposed catalyst. Yan and Cho reported a Spearman rank correlation of 0.84 between predicted and experimental selectivities in their instance-level evaluation. To adapt this test to another catalyst family, specify the selectivity to predict and reserve previously unseen ligand scaffolds for evaluation. [CatScore paper](https://doi.org/10.1039/D4DD00114A) · [CatScore code and data](https://github.com/bingyan4science/CatScore)
