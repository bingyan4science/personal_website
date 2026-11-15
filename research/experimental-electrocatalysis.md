---
layout: research-guide
title: "Experimental electrocatalysis: active sites, surface area, and selective bond activation"
guide_order: 5
image: /images/Joule2017.jpg
topics: Electrochemical surface area · Nickel sulfide oxygen reduction · Membrane-free fuel cells · Mediated C–C bond cleavage
question: How do we measure active surfaces and control bond activation in electrocatalysis?
description: A reading guide to experimental electrocatalysis, from measuring electrochemical surface area and identifying nickel sulfide active sites to membrane-free fuel cells and mediated C–C bond cleavage.
permalink: /research/experimental-electrocatalysis/
reviewed: '2026-11-14'
---

An electrode's current depends on how much surface is exposed, which sites are present during the reaction, and how reactants reach those sites. Understanding these contributions makes it possible to compare catalysts and design interfaces that favor a desired reaction.

This guide connects six papers from my experimental work with Yogesh Surendranath during my PhD and Yuriy Román-Leshkov during my postdoc at MIT. The questions range from measuring electrochemical surface area to using selective catalysts and redox mediators to control chemical transformations.

## How can electrochemical surface area be measured without ion-transfer interference? {#ecsa}

A larger catalytic current can reflect a larger exposed surface rather than a more active material. Double-layer capacitance offers a way to estimate electrochemically active surface area (ECSA), but ion adsorption, insertion, and other ion-transfer processes can add current that complicates the measurement.

Youngmin Yoon, Bing Yan, and Yogesh Surendranath examined 17 materials spanning metals, conductive oxides, and chalcogenides. Measuring capacitance in weakly coordinating potassium hexafluorophosphate in acetonitrile, KPF₆/MeCN, produced substantially more consistent capacitance per unit of real surface area than measurements in aqueous electrolytes. The method reduces ion-transfer interference and provides a basis for estimating ECSA across these materials.

This paper is useful when choosing a capacitance-based surface-area measurement or explaining how activity normalization depends on the electrolyte. The reported calibration applies to the tested materials and conditions. Capacitance-based ECSA estimates area, while counting catalytic sites requires additional evidence. [ECSA measurement paper, JACS 2018](https://doi.org/10.1021/jacs.7b10966)

## How can mediated hydrogen atom transfer enable electrochemical C–C bond cleavage? {#mediated-hat}

Oxidizing a redox mediator can initiate a reaction at a lower electrode potential than oxidizing the substrate directly. Bing Yan, Changxia Shi, Gregg T. Beckham, Eugene Y.-X. Chen, and Yuriy Román-Leshkov used N-hydroxyphthalimide (NHPI) as the mediator. Electrochemical oxidation forms the phthalimide-N-oxyl (PINO) radical, which removes a hydrogen atom from a benzylic C–H bond. Oxygen captures the resulting carbon radical, leading to peroxide intermediates and oxygenated C–C cleavage products.

The study connects experiments on model compounds to the conversion of styrene oligomers and polystyrene into oxygenated monomers, dimers, and oligomers. It is a reference for mediated electrochemical bond activation, the relationship between bond strength and cleavage selectivity, and oxidative polystyrene deconstruction. The demonstrated chemistry depends on the substrate and its benzylic sites. [Mediated hydrogen atom transfer paper, ChemSusChem 2022](https://doi.org/10.1002/cssc.202102317)

## Which surface is active during oxygen reduction on nickel sulfide? {#nickel-sulfide-surface}

The composition of a catalyst before a reaction need not describe the surface that carries out the reaction. Bing Yan, Dilip Krishnamurthy, Christopher H. Hendon, Siddharth Deshpande, Yogesh Surendranath, and Venkatasubramanian Viswanathan combined electrochemical measurements, surface spectroscopy, microscopy, and density functional theory to investigate nickel sulfide under oxygen-reduction conditions.

The crystalline Ni₃S₂ developed an approximately 2 nm disordered surface layer with nominal NiS composition. Calculations suggested that the local sulfur coordination of exposed nickel sites helps explain oxygen-reduction activity, with three sulfur neighbors providing favorable energetics. The experiments establish the surface transformation, while the calculations propose a connection between local structure and activity.

Use this paper when discussing catalyst reconstruction, amorphous active surfaces, or why bulk composition alone can be insufficient to identify active sites. [Surface restructuring paper, Joule 2017](https://doi.org/10.1016/j.joule.2017.08.020) · [Open manuscript at MIT](https://dspace.mit.edu/entities/publication/ecbf2c60-4b3d-4306-9681-9fafcdd2d60e)

## Can bond activation and charge transfer occur at different interfaces? {#separated-interfaces}

Bing Yan, Ryan P. Bisbey, Alexander Alabugin, and Yogesh Surendranath placed a mixed electron–proton conducting tungsten oxide membrane between platinum and an aqueous electrolyte. The composite electrode oxidized hydrogen even though the platinum catalyst was separated from the solution.

Mechanistic measurements supported hydrogen activation at the platinum–gas interface and electron–proton charge separation at the tungsten oxide–solution interface, coupled by hydrogen transport through the oxide. This architecture also reduced the catalyst's exposure to electrolyte poisons and impurities. The paper provides an experimental example of separating the environments for substrate activation and charge transfer, with hydrogen oxidation as the demonstrated reaction. [Mixed electron–proton conductor paper, JACS 2019](https://doi.org/10.1021/jacs.9b03327)

## How can catalyst selectivity enable a membrane-free formate fuel cell at neutral pH? {#membrane-free-fuel-cell}

A fuel-cell membrane helps keep fuel and oxidant from reacting at the wrong electrode. A different design strategy is to choose catalysts that remain selective even when both reactants are present.

Bing Yan, Nolan M. Concannon, Jarrod D. Milshtein, Fikile R. Brushett, and Yogesh Surendranath combined a Ni₃S₂ oxygen-reduction cathode with a carbon-supported palladium formate-oxidation anode. The nickel sulfide retained oxygen-reduction selectivity in the presence of concentrated formate, enabling a membrane-free, room-temperature fuel cell in a neutral aqueous electrolyte.

This proof of concept is useful when discussing how electrode selectivity can simplify device architecture. Its demonstrated scope is the nickel-sulfide/palladium formate cell under the reported conditions. [Membrane-free formate fuel-cell paper, Angewandte Chemie 2017](https://doi.org/10.1002/anie.201702578) · [Open manuscript at MIT](https://dspace.mit.edu/entities/publication/2043743c-ac99-43e2-be93-84c05d162fea)

## Which nickel sulfide catalysts reduce oxygen to water in a neutral electrolyte? {#heazlewoodite}

Joseph M. Falkowski, Nolan M. Concannon, Bing Yan, and Yogesh Surendranath showed that heazlewoodite, Ni₃S₂, supports oxygen reduction to water in neutral aqueous electrolyte. Electrodeposited films and nanoparticles were tested in pH 7 phosphate buffer, where the catalyst combined oxygen-reduction activity with resistance to poisoning and corrosion.

The paper establishes the catalyst's performance in this electrolyte and is the starting point for the later studies of surface reconstruction and membrane-free fuel cells. Cite it for the original Ni₃S₂ oxygen-reduction demonstration. The later Joule paper addresses the separate question of which surface forms during operation. [Heazlewoodite paper, JACS 2015](https://doi.org/10.1021/jacs.5b03426) · [Open manuscript at MIT](https://dspace.mit.edu/entities/publication/175f0a89-3c65-4ed9-ba14-1a898c6cbcb9)

## What experiment should follow a proposed mechanism?

These studies use complementary measurements to test different parts of a catalytic explanation, including surface area, surface composition, reaction selectivity, and the location of bond activation. When several mechanisms remain consistent with the measured rates, the next task is to choose a measurement on which their predictions differ. The [guide to inferring catalytic mechanisms from kinetic data]({{ '/research/catalysis-mechanisms/' | relative_url }}) explores this question through SPARK, an unpublished research project with a public manuscript draft.
