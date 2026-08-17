---
title: "The IgG4 Hypothesis: Investigating a Proposed Link Between mRNA Persistence, Antibody Class Switching, and Chronic Disease"
created: 2026-08-17
category: health
tags:
  - covid-19
  - mrna-vaccines
  - spike-protein
  - igg4
  - immune-tolerance
  - antibody-class-switching
  - post-vaccination-syndrome
  - chronic-disease
  - vaccine-safety
  - immunology
people:
  - Peter McCullough
  - Nicolas Hulscher
  - Akiko Iwasaki
  - Harlan Krumholz
  - Pascal Irrgang
  - Shiv Pillai
  - Vladimir Uversky
  - William Makis
organizations:
  - McCullough Foundation
  - Yale LISTEN Study
  - EMEI Grand Rounds
topics:
  - mRNA persistence
  - spike protein persistence
  - IgG4 class switching
  - immune tolerance
  - post-vaccination syndrome
  - chronic inflammation
  - cancer hypothesis
  - autoimmune disease
status: complete
---

# The IgG4 Hypothesis: Investigating a Proposed Link Between mRNA Persistence, Antibody Class Switching, and Chronic Disease

*Tracing a theory circulating through physician networks like the McCullough Foundation and EMEI Grand Rounds back to its primary sources*

The theory goes like this: mRNA vaccines don't fully clear from the body. The spike protein they encode keeps getting made, in small amounts, for months or years in some people. The immune system responds to this unusual persistence by shifting its antibody output toward IgG4 — a subclass built for tolerance rather than attack. And once that shift happens, the theory holds, spike and IgG4 may start reinforcing each other: less inflammatory clearance means the antigen lingers longer, and the longer it lingers, the further the antibody response drifts toward tolerance. Proponents argue this feedback loop could explain a subset of chronic post-vaccination illness, and — more speculatively — create tissue conditions that favor cancer or autoimmune disease.

The individual observations behind this are real, and some are well replicated. The chain connecting them into a disease mechanism is a hypothesis, built in public by named researchers who say so themselves. This piece traces both — the data and the reasoning laid on top of it — and spends most of its time on the part that gets glossed over in summaries: *how* the proposed mechanism is supposed to work, cell by cell.

---

## Part 1: How long do mRNA and spike protein actually stick around?

mRNA vaccines were originally described as transient: lipid nanoparticles deliver mRNA to cells near the injection site, those cells produce spike protein for days to a couple of weeks, the immune system learns from it, and everything degrades. Several studies have since pushed that timeline out further than expected — though how far, and in whom, varies a lot by study.

**Weeks, in normal tissue.** Katharina Röltgen's team at Stanford biopsied lymph nodes from vaccinated volunteers and found <cite index="20-1">robust germinal centers — the structures where B cells mature and refine antibodies — containing vaccine mRNA and spike antigen for up to eight weeks after vaccination in some cases</cite>. That's substantially longer than originally assumed, but it's a normal, expected site of immune activity doing exactly what germinal centers do: hold onto antigen so B cells can keep testing and improving their antibodies against it.

**About a month, by autopsy.** A follow-up study in *npj Vaccines* examined tissue from people who died at various intervals after vaccination. <cite index="21-1">Vaccine mRNA was found in axillary lymph nodes in most people who died within 30 days of vaccination but not in those who died later than that</cite>, and it <cite index="21-1">wasn't found in the mediastinal lymph nodes, spleen, or liver at all</cite> — though it <cite index="21-1">did turn up in heart tissue in a subset of recently vaccinated people</cite>, a finding relevant to the known, rare risk of vaccine-associated myocarditis.

**Up to two years, in a symptomatic minority.** The most consequential recent data point is Yale's LISTEN study, led by immunologist Akiko Iwasaki and cardiologist Harlan Krumholz, which examined people with "Post-Vaccination Syndrome" (PVS) — long-COVID-like symptoms that began after vaccination rather than infection. Comparing 42 PVS patients to 22 vaccinated controls, the team found <cite index="27-1">a subset of PVS participants had detectable spike protein in their bloodstream, with antigen persistence in some cases up to 709 days post-vaccination</cite>. <cite index="32-1">About half the PVS group (20 of 42) had measurable free spike in plasma, ranging from roughly 1 to 246 pg/mL</cite>, confirmed at an independent lab. Iwasaki called it unexpected: <cite index="34-1">"That was surprising, to find spike protein in circulation at such a late time point," she said, adding that it's not yet known whether the spike is causing the symptoms</cite> — some PVS patients had none detectable at all, and the study also flagged Epstein-Barr virus reactivation and altered T-cell profiles as other candidate contributors. It's a preprint, drawn from a self-selected symptomatic cohort rather than a population sample, so the ~50% detection rate describes that specific group, not vaccinated people generally.

**3.5 years, in one documented patient.** The outer edge of the persistence claims comes from a case report in the *Medical Research Archives* (2026) by Nicolas Hulscher, Vanessa Schmidt, Michael Mörz, Claire Rogers, Natalia von Ranke, Wei Zhang, John Catanzaro, and Peter A. McCullough. It describes a 55-year-old man, three doses of Pfizer-BioNTech, and a multi-system illness investigated over years. The reported findings, at their own stated timepoints: spike protein detected inside monocytes at day 852; <cite index="16-1">free spike protein by high-sensitivity ELISA in plasma (129.0 ± 4.1 fg/mL) and circulating exosomes (11.6 ± 0.1 fg/mL) at day 1,173</cite>; <cite index="16-1">spike mRNA detected by RT-PCR in circulating exosomes at day 1,284</cite>; and serial skin biopsies at days 1,160, 1,249, and 1,364 showing <cite index="16-1">persistent spike protein in endothelial cells, macrophages, and — by the final biopsy — nerve fibers, plus multiple plasmid DNA elements including spike gene sequences, bacterial origin-of-replication sequences, and an SV40 enhancer</cite>. Nucleocapsid antibodies stayed negative across five timepoints at three separate labs, which the authors use to argue against undiagnosed natural infection as the source. A whole-genome sequencing analysis at day 1,277 reportedly found <cite index="16-1">structural variants — large duplications and deletions — affecting cancer-associated genes including EGFR, MYC, ERBB2, and ETV6/RUNX1</cite>, which the authors frame as possible "genomic dysregulation" associated with the persistent material, without claiming to have established that link causally.

Read across these four data points, there's a real gradient: routine, expected persistence in lymphoid tissue for weeks; occasional detection in blood for up to two years in a minority of symptomatic people; and, in one closely instrumented case, detection past three years. What connects them mechanistically — and what the field is actually trying to work out — is *why* persistence would happen at all once a well-functioning immune response has formed. That's where the IgG4 mechanism comes in.

---

## Part 2: The proposed mechanism — how persistent antigen and IgG4 might reinforce each other

### Step one: what makes IgG4 different

Antibodies aren't interchangeable. The four IgG subclasses share the same basic Y-shape and the same ability to grab an antigen, but they differ enormously in what happens *after* they grab it:

- **IgG1 and IgG3** are the default antiviral workhorses. They activate complement — a cascade of blood proteins that can punch holes in pathogens or flag them for destruction — and they bind strongly to activating Fc receptors on macrophages and natural killer cells, triggering those cells to engulf or kill whatever the antibody is attached to.
- **IgG2** mostly handles certain bacterial polysaccharides and is a weaker activator of both complement and effector cells.
- **IgG4** is structurally the odd one out. <cite index="37-1">Making up only about 3–6% of total IgG in a healthy person</cite>, it undergoes a quirk called Fab-arm exchange: two IgG4 molecules can swap halves with each other mid-circulation, producing a hybrid, functionally one-armed antibody that can bind an antigen but generally can't cross-link two copies of it. <cite index="38-1">That kills its ability to form the large immune complexes that trigger strong inflammation, and it also binds poorly to complement's C1q protein while preferentially engaging FcγRIIb — an inhibitory receptor, rather than the activating ones IgG1 favors.</cite> The net effect, replicated across many contexts, is an antibody that can still recognize and even neutralize its target but is comparatively bad at recruiting the rest of the immune system to destroy it.

### Step two: what makes the body switch to it

Class switching — the process by which a B cell trades its default antibody type for IgG4 — happens inside germinal centers, the same lymph node structures Röltgen's team found still active weeks after vaccination. It's directed by two ingredients: contact with T follicular helper (Tfh) cells, and a specific cytokine signal. <cite index="60-1">IL-10 acts as the critical cytokine for IgG4-specific class-switch recombination, and it also promotes the germinal center response more broadly</cite> — B cells don't switch to IgG4 by default; they need repeated instruction to do so, largely via IL-10 exposure. That IL-10-driven signal is characteristic of chronic, repetitive antigen exposure rather than a single, resolved encounter. The clearest natural example is allergen immunotherapy: someone getting weekly allergy shots for years builds up IL-10-producing regulatory cells in their lymph nodes, and their B cells respond to the sustained, low-dose antigen drip by increasingly switching to IgG4 — which is exactly why allergists consider a strong IgG4 response a treatment success, not a failure. Beekeepers show the same pattern from years of repeated stings.

This is the biological logic proponents of the hypothesis are drawing on: **IgG4 switching is the immune system's readout of "this antigen keeps showing up, again and again, at a survivable dose."** A single vaccine dose, cleared within weeks, wouldn't be expected to drive much IgG4. Multiple doses, spaced months apart, delivering more spike protein into a system that may not have fully cleared the antigen from the previous round, plausibly look more like the repeated-exposure pattern that pushes B cells toward IL-10-mediated switching. This is consistent with — and offers a mechanistic explanation for — the empirical finding, discussed below, that IgG4 rises sharply after a third mRNA dose but is barely detectable after two.

### Step three: the proposed feedback loop

This is the part of the argument that goes beyond what's been directly measured, but it follows logically from steps one and two, and it's the mechanism proponents like Uversky, Redwan, Makis, and Rubio-Casillas explicitly propose. If IgG4 is less effective at complement activation and effector-cell recruitment, then a spike-specific response that has shifted heavily toward IgG4 would, in theory, be worse at flagging spike-expressing cells for destruction by macrophages and NK cells — even though the IgG4 antibodies can still bind spike and even neutralize free virus directly. Fewer spike-bearing cells get cleared. More antigen persists. And persistent antigen, per the same IL-10/Tfh biology, is exactly the condition that reinforces further IgG4 switching. In this model, the two processes aren't just correlated — they're a loop, each one feeding the other, with the balance drifting further toward tolerance the longer the exposure runs.

At the tissue level, the researchers proposing this model point to processes documented in other IgG4-dominant conditions and extrapolate them to spike-expressing tissue. In cancer immunology, tumors that shift the local antibody environment toward IgG4 are described as recruiting a specific type of macrophage: <cite index="36-1">chronic antigen stimulation under Th2-type conditions drives macrophages toward an "M2b-like" state, which secretes IL-10 and the chemokine CCL1</cite>, which in turn recruits regulatory T cells (Tregs) and further entrenches a tolerogenic, anti-inflammatory microenvironment around the antigen — essentially a self-sustaining local zone where the immune system has been told to stand down. <cite index="39-1">In several cancers, this IgG4-skewed state correlates with reduced effector-cell activity and worse outcomes</cite>, and separately, IgG4-related disease (a distinct, rare autoimmune condition unrelated to vaccination) shows <cite index="60-1">that IgG4 class-switch recombination is specifically upregulated in the affected organ tissue itself</cite>, not just in the blood, with local plasma cells producing IgG4 in place, surrounded by fibrotic tissue — evidence that the IgG4 program can become a persistent, tissue-resident state once established, not just a transient blood measurement.

Applying that template to the vaccine hypothesis, the argument runs: if spike protein is present at low levels in a tissue (endothelium, nerve fibers, or elsewhere, as in the case report above) for long enough to attract this kind of local, IgG4-dominant, macrophage-and-Treg-recruiting environment, the tissue could end up in a state that neither clears the antigen efficiently nor mounts a strong local inflammatory response — a kind of stalemate that persists rather than resolves. On the cancer side specifically, the mechanistic proposal is more targeted: <cite index="43-1">non-specific IgG4 elevated by this process could bind and block anti-tumor IgG1 antibodies from engaging killer immune cells, engage the inhibitory FcγRIIb receptor to dampen innate immune effector cells more broadly, and — depending on which epitopes it targets — help shape a tumor-permissive microenvironment</cite>, essentially borrowing a tolerance mechanism evolved for allergens or self-tissue and turning it into cover for a nearby malignant process.

### What's measured versus what's inferred, stated once

The load-bearing empirical claim — that repeated mRNA vaccination measurably shifts the spike-specific antibody response toward IgG4 — is genuinely well established. The feedback-loop mechanism connecting persistent antigen to IgG4 switching to further persistence, and the extension of that loop to cancer or chronic tissue disease, is a mechanistically coherent hypothesis built from adjacent, published immunology (allergen tolerance, cancer-associated IgG4, IgG4-related disease) but has not itself been directly demonstrated in vaccinated people. No study has yet shown that vaccinated individuals with a strong IgG4 shift go on to clear spike more slowly than those without one, or that local IgG4-dominant, macrophage/Treg-recruiting microenvironments actually form around residual vaccine antigen in human tissue. Both are plausible extrapolations, not observations.

---

## Part 3: The empirical evidence for the IgG4 shift itself

Here the ground is firm. In January 2023, Pascal Irrgang's team at Friedrich-Alexander-Universität Erlangen-Nürnberg published a longitudinal analysis in *Science Immunology* showing that <cite index="7-1">IgG4 as a share of total spike-specific IgG rose, on average, from about 0.04% shortly after the second dose to roughly 19% following a third dose</cite>. The shift was specific to the mRNA platform: <cite index="6-1">it appeared after repeated mRNA vaccination but not after an adenoviral-vector vaccine</cite>, and effector activity — antibody-dependent phagocytosis and complement deposition — <cite index="6-1">was measurably lower after the third dose than after the second</cite>, tracking the antibody shift.

This has been independently replicated several times over:

- A Spanish healthcare-worker cohort found <cite index="3-1">IgG4 and IgG2 rose markedly after the third mRNA dose, and elevated IgG4 was significantly associated with increased risk of breakthrough infection</cite> — a real-world clinical correlate, not just a lab measurement.
- A Hungarian cohort found the magnitude of the switch <cite index="8-1">depended on prior infection history</cite>, meaning it isn't uniform across everyone.
- Comparing vaccine brands, the <cite index="2-1">class switch toward IgG2 and IgG4 was more pronounced with Pfizer's BNT162b2 than Moderna's mRNA-1273</cite>, suggesting formulation or dosing details modulate the effect rather than it being an unavoidable property of mRNA vaccination as such.

What remains genuinely open is what this shift *does* functionally. Harvard immunologist Shiv Pillai, in an editorial pointedly titled "Is it bad, is it good, or is IgG4 just misunderstood?", ran follow-up experiments that complicate the simple "IgG4 = worse protection" reading. <cite index="52-1">Spike-specific IgG4 did show reduced effector-function activity — ADCC, complement deposition, phagocytosis — when isolated on its own, and was inhibitory when it competed directly with other IgG subclasses for the same binding site. But in polyclonal plasma — a realistic mixture of many antibody types, as exists in an actual vaccinated person's blood — adding high concentrations of spike-specific IgG4 didn't manage to suppress the overall antibody-dependent killing and phagocytosis activity of the mixture</cite>, and <cite index="52-1">IgG4 retained the ability to neutralize the virus directly</cite>. That's a real tension in the current data: IgG4 looks concerning in isolation, less so in the messier, more realistic context of a full antibody repertoire — which is exactly the setting relevant to a real infection or ongoing antigen exposure.

---

## Where the argument stands

Three tiers, briefly:

**Established, replicated science:** mRNA and spike protein persist in lymph nodes for weeks post-vaccination; repeated mRNA dosing drives a substantial, dose-dependent shift toward spike-specific IgG4; IL-10 and germinal center biology are the documented drivers of IgG4 class switching generally; IgG4's structural features genuinely reduce its complement- and effector-cell-recruiting ability compared with IgG1/IgG3.

**Preliminary but real findings, still being worked out:** spike protein detectable in blood up to two years post-vaccination in a symptomatic subset (Yale LISTEN); elevated IgG4 correlating with breakthrough infection risk in at least one cohort; conflicting data on whether IgG4's effector-suppressing effect actually holds up in realistic, polyclonal antibody mixtures.

**The proposed mechanism connecting them:** that persistent spike and IgG4 switching reinforce each other in a feedback loop, and that this loop can create local tissue environments — via IL-10, M2-like macrophages, and Treg recruitment — permissive to chronic illness or malignancy. This is a coherent, testable hypothesis, assembled from real immunology by researchers who describe it as a hypothesis. It has not yet been tested directly: no study has traced the loop in real time in vaccinated people, and no population-level data yet links IgG4 shift magnitude to cancer or chronic-disease incidence.

The research that would move any of this from hypothesis to established fact is already underway in pieces — Yale's LISTEN study continues to recruit and publish, and several European groups are tracking IgG4 dynamics longitudinally in specific patient populations. The mechanism is a live, testable scientific question, not a closed one.

---

## Sources cited

- Röltgen K, et al. "Immune imprinting, breadth of variant recognition, and germinal center response in human SARS-CoV-2 infection and vaccination." *Cell*, 2022.
- Röltgen K, Nielsen SCA, Silva O, et al. "Duration of SARS-CoV-2 mRNA vaccine persistence and factors associated with cardiac involvement in recently vaccinated patients." *npj Vaccines*, 2023;8(1):141.
- Bhattacharjee B, Lu P, Silva Monteiro V, et al. (Iwasaki, Krumholz, et al.) Yale LISTEN study preprint on Post-Vaccination Syndrome immunology. *medRxiv*, 2025.02.18.25322379.
- Hulscher N, Schmidt V, Mörz M, Rogers C, von Ranke N, Zhang W, Catanzaro JA, McCullough PA. "Persistence of Vaccine mRNA, Plasmid DNA, Spike Protein, and Genomic Dysregulation Over 3.5 Years Post-COVID-19 mRNA Vaccination." *Medical Research Archives*, 2026;14(6). DOI: 10.18103/mra.2026.0351.
- Irrgang P, Gerling J, Kocher K, et al. "Class switch toward noninflammatory, spike-specific IgG4 antibodies after repeated SARS-CoV-2 mRNA vaccination." *Science Immunology*, 2023;8(79):eade2798.
- Pillai S. "Is it bad, is it good, or is IgG4 just misunderstood?" *Science Immunology*, 2023;8(81).
- Uversky VN, Redwan EM, Makis W, Rubio-Casillas A. "IgG4 Antibodies Induced by Repeated Vaccination May Generate Immune Tolerance to the SARS-CoV-2 Spike Protein." *Vaccines*, 2023;11(5):991.
- Raszek M, Cowley D, Redwan EM, Uversky VN, Rubio-Casillas A. "Exploring the possible link between the spike protein immunoglobulin G4 antibodies and cancer progression." *Explorations of Immunology*, 2024;4:267–284.
- Buhre JS, et al. "Post-vaccination IgG4 and IgG2 class switch associates with increased risk of SARS-CoV-2 infections." *Journal of Infection*, 2025.
- Kiszel P, Sík P, Miklós J, et al. "Class switch towards spike protein-specific IgG4 antibodies after SARS-CoV-2 mRNA vaccination depends on prior infection history." *Scientific Reports*, 2023;13:1.
- "The Role of IgG4 in the Fine Tuning of Tolerance in IgE-Mediated Allergy and Cancer." Review, *PMC*.
- "Role of IgG4 Antibodies in Human Health and Disease." Review, *PMC*.
- "Immunological mechanism of IgG4-related disease." *Journal of Translational Autoimmunity* / ScienceDirect.
- "An immune evasion mechanism with IgG4 playing an essential role in cancer and implication for immunotherapy." *PubMed*.

*This synthesizes primary research literature, preprints, and hypothesis papers current as of August 2026. Several sources — notably the Yale LISTEN preprint and the 3.5-year case report — are recent enough that peer review, replication, or revision may still be in progress.*