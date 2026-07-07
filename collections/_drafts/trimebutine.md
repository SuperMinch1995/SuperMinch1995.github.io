---
layout: post
title: "A drug prescribed to millions — and why it's invisible in America"
subtitle: "Trimebutine, chronic intestinal pseudo-obstruction, and what the FDA–EMA divide looks like from inside a rare-disease cohort."
date: 2026-06-06
image: "/assets/images/trimebutine-hero.webp"
---

### Opening

While preparing our cohort of 130 patients with chronic intestinal pseudo-obstruction (CIPO) for the [*American Journal of Gastroenterology*](https://doi.org/10.14309/ajg.0000000000003980), I ran a set of survival analyses I expected to be unremarkable. One result was not. In both univariable and multivariable Cox proportional hazards models, trimebutine use was associated with better survival (univariable HR 0.24, 95% CI 0.07–0.79, p = 0.020; multivariable HR 0.15, 95% CI 0.03–0.72, p = 0.018).

I want to be precise about what that number is and is not. It comes from an observational cohort, not a trial. The confidence intervals are wide, the event count is small, and the analysis was exploratory — generating hypotheses rather than being definitive evidence. Patients who tolerate and stay on a motility-modulating drug may differ in ways no model fully captures, and residual confounding is real. But because there is currently no effective treatment for this disease, I started reading much more carefully about this molecule: if the hypothesis were true, the impact for patients could be real.

And the more I read, the stranger the situation became. Trimebutine is prescribed daily to millions of people across Europe, Latin America, and Asia. It has a four-decade safety record and a mechanism that is, on paper, almost tailor-made for a disease defined by the loss of organized gut motility. And it is entirely unavailable in the United States — not because the FDA rejected it, but because no one ever asked.

This piece is about why trimebutine is mechanistically interesting in CIPO, why a surprising survival signal in a rare disease deserves more than a footnote, and what the drug's absence in the US reveals about the wider divergence between how Europe and the United States decide what counts as a drug.

---

### Section 1 — An unusual opioid

<iframe class="mt-fig" src="{{ '/assets/figures/trimebutine/fig1-radar.html' | relative_url }}" title="Receptor-affinity profile of trimebutine" loading="lazy" scrolling="no" style="width:100%;border:0;display:block;margin:1.6rem 0;"></iframe>

Before asking whether a drug could matter in a disease, it helps to know what makes the drug itself unusual. And trimebutine is unusual.

Most molecules that act on opioid receptors are sharply selective. Morphine targets μ. Loperamide targets peripheral μ. Fedotozine targets κ. Trimebutine does something almost no other clinically used opioid does: it binds μ, κ, and δ receptors with no meaningful preference for any of them ([Delvaux & Wingate, 1997](https://pubmed.ncbi.nlm.nih.gov/9364286/)).

That flat, non-selective profile is the key to its clinical behavior. Pure μ-agonists slow the gut and constipate. Pure κ-agonists alter visceral perception but do little for motor function. Trimebutine, by engaging all three subtypes at low affinity, *modulates* rather than *blocks* — and as we'll see, a disease that sits at the extreme silent end of the motility spectrum is exactly where that distinction might matter most.

---

### Section 2 — At the synapse, and back to the survival signal

<iframe class="mt-fig" src="{{ '/assets/figures/trimebutine/fig2a-mechanism.html' | relative_url }}" title="What is known: opioid modulation of the phase III rhythm" loading="lazy" scrolling="no" style="width:100%;border:0;display:block;margin:1.6rem 0;"></iframe>

The survival association I found has no proven mechanism. But it does have a plausible one, and it lives at the synapse.

The cholinergic neurons of the myenteric plexus drive smooth muscle contraction. Enkephalin-containing neurons modulate that drive, hyperpolarizing the cholinergic terminal and damping acetylcholine release. Trimebutine binds the same opioid receptors as endogenous enkephalin, but more weakly — a partial agonist that nudges the system rather than silencing it.

This is the part that matters for CIPO. The motor pattern of the small intestine — the migrating motor complex, or MMC — depends on a balance between cholinergic excitation and opioidergic inhibition. In CIPO, that balance collapses: the MMC disappears or fragments. What manometry shows is not too much inhibition, but the loss of organized rhythm itself.

A drug that *re-engages* the modulatory system rather than blocking it is therefore mechanistically appealing — and this is not only theory. In 1986–1987, Boige and colleagues at Hôpital Bretonneau in Paris recorded duodenal manometry in five infants with severe dysmotility (two with confirmed pseudo-obstruction) before and after intravenous trimebutine. Baseline tracings showed a complete absence of MMC. After trimebutine, four of the five developed phase III–like activity within minutes, and two showed clinical signs of peristalsis that had been absent before injection ([Boige et al., *J Pediatr Gastroenterol Nutr*, 1987](https://pubmed.ncbi.nlm.nih.gov/3430262/)). The same phase III–inducing effect has been documented in adults with idiopathic pseudo-obstruction ([Delvaux & Wingate, 1997](https://pubmed.ncbi.nlm.nih.gov/9364286/)).

<iframe class="mt-fig" src="{{ '/assets/figures/trimebutine/fig2b-manometry.html' | relative_url }}" title="What was observed: manometry after intravenous trimebutine" loading="lazy" scrolling="no" style="width:100%;border:0;display:block;margin:1.6rem 0;"></iframe>



This is a single, small, uncontrolled study, three of whose five patients did not have CIPO. It is the kind of result that, in 1987, was enough to write trimebutine into European pediatric practice — and not the kind the FDA would accept as evidence of anything. Both responses are defensible. They reflect different beliefs about what to do when evidence is thin and patients are suffering. My survival signal sits in exactly the same uncomfortable space: suggestive, mechanistically coherent, and nowhere near proof.

<iframe class="mt-fig" src="{{ '/assets/figures/trimebutine/fig2c-evidence.html' | relative_url }}" title="What remains unknown: the evidence, to scale" loading="lazy" scrolling="no" style="width:100%;border:0;display:block;margin:1.6rem 0;"></iframe>



---

### Section 3 — A drug that goes both ways

<iframe class="mt-fig" src="{{ '/assets/figures/trimebutine/fig3-transit.html' | relative_url }}" title="Direction of effect across drugs" loading="lazy" scrolling="no" style="width:100%;border:0;display:block;margin:1.6rem 0;"></iframe>

There is one more feature of trimebutine that makes it an odd fit for conventional drug development — and a surprisingly good fit for CIPO.

The non-selective receptor binding produces something unusual in pharmacology: in randomized IBS studies, trimebutine accelerated colonic transit in constipated patients and slowed it in diarrhea-predominant patients. Same dose, same molecule, opposite directions — toward normal in both cases ([Delvaux & Wingate, 1997](https://pubmed.ncbi.nlm.nih.gov/9364286/)).

For most functional GI drugs, we have to pick a direction: loperamide for diarrhea, laxatives for constipation, prokinetics for stasis. Bidirectional normalization fits none of these categories — which may be part of why no one has built a clean registration trial around it. There is no tidy primary endpoint when the drug is meant to do different things to different patients.

For CIPO, that ambiguity is the point. CIPO patients don't have one motility problem; they have an unpredictable one, swinging between obstructive episodes and stasis, often with bacterial overgrowth and diarrhea in between. A drug that pushes the system back toward whatever the normal pattern would have been is, conceptually, well-matched to a disease defined by the loss of normal patterning. It is the kind of pharmacology that is easy to use at the bedside and hard to license — a tension that turns out to explain a great deal about where this drug is, and isn't, available.

---

### Section 4 — A world map of availability

<iframe class="mt-fig" src="{{ '/assets/figures/trimebutine/fig4-map.html' | relative_url }}" title="World map of trimebutine marketing authorisation" loading="lazy" scrolling="no" style="width:100%;border:0;display:block;margin:1.6rem 0;"></iframe>

If the molecule is this interesting, the obvious question is why an American physician has likely never heard of it.

Trimebutine is sold as Débridat — and as a dozen generic equivalents — across France, Germany, Italy, Spain, much of Latin America, Canada, Japan, Korea, and South-East Asia. It is not available in the United States ([Drugs.com, 2025](https://www.drugs.com/medical-answers/trimebutine-3571789/)).

The reason is not what a US clinician might assume. The FDA never rejected trimebutine; no sponsor has ever filed a New Drug Application for it. The molecule was developed by Jouveinal Laboratoires in France in the late 1960s; [Warner-Lambert took a controlling stake in 1993](https://insights.citeline.com/PS022109/), and [Pfizer absorbed it through its acquisition of Warner-Lambert in 2000](https://en.wikipedia.org/wiki/Warner%E2%80%93Lambert). Trimebutine therefore sits today inside a US pharmaceutical giant's portfolio — and was still never brought to the US market. By the time it was clinically mature, the US gastrointestinal market had already settled on dicyclomine and hyoscyamine for antispasmodic indications and on serotonergic agents for more complex motility cases. There was no commercial incentive to spend tens of millions of dollars on a full FDA dossier for an old, unpatentable molecule entering an occupied market.

The result is a strange asymmetry. A drug written on prescriptions across dozens of countries is, to a US physician, a drug that does not exist — and one that never had the chance to be tested in the disease where my own data hint it might matter most.

---

### Section 5 — Two philosophies of approval

<iframe class="mt-fig" src="{{ '/assets/figures/trimebutine/fig5a-table.html' | relative_url }}" title="United States (FDA) vs Europe: two systems, one drug" loading="lazy" scrolling="no" style="width:100%;border:0;display:block;margin:1.6rem 0;"></iframe>

The trimebutine story is a small instance of a much larger structural divergence between the two agencies that decide what counts as a drug.

The FDA and EMA differ less in *what* they require than in *how* they decide. Both demand evidence of safety, efficacy, and manufacturing quality; both run independent statistical reviews. The differences sit in approval pathways, jurisdictional scope, and the handling of uncertainty.

The FDA is a single federal agency issuing one binding decision for one market. The EMA coordinates decisions across 27 member states, often through national regulators that can also approve drugs independently via decentralized or mutual-recognition routes. This has a downstream effect: drugs authorized in one European country in the 1960s — trimebutine in France among them — were carried into the European system as it formalized in the 1990s. The US has no comparable pathway. A drug that is not FDA-approved is simply unavailable, regardless of how long it has been used safely elsewhere.

<iframe class="mt-fig" src="{{ '/assets/figures/trimebutine/fig5b-timeline.html' | relative_url }}" title="A drug's two timelines, 1969–2000" loading="lazy" scrolling="no" style="width:100%;border:0;display:block;margin:1.6rem 0;"></iframe>



A second difference, much discussed in oncology and rare disease, is how each agency handles thin evidence. The FDA's expedited pathways (Accelerated Approval, Breakthrough Therapy, RMAT) allow market entry on surrogate endpoints and limited data, with confirmatory trials required afterward. The EMA's Conditional Marketing Authorization is similar in principle but has historically been more willing to accept single-arm confirmatory studies ([Salcher-Konrad et al., Milbank Quarterly, 2020](https://doi.org/10.1111/1468-0009.12476)). The net effect: the FDA approves a steady stream of novel drugs each year ([50 in 2024](https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2024) and [46 in 2025](https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2025)), while the European portfolio retains more drugs of older continental origin that never crossed the Atlantic.

Trimebutine belongs to that second group. It is not a casualty of the FDA's evidentiary standards. It is a casualty of a structural mismatch — a market with no route for legacy drugs, and a sponsor with no commercial reason to build one.

---

### Closing

This brings me back to that survival curve.

I am not arguing that trimebutine treats CIPO. My data cannot carry that weight, and I have tried to be honest about exactly how much they can carry. What the analysis did was send me looking — and what I found was a molecule with a coherent mechanism, decades of safety data, and a tantalizing signal in the one disease where almost nothing works, sitting just out of reach of the patients and the research system that might benefit from testing it properly.

There is a real conversation to be had about whether the FDA should create a mechanism for legacy drugs with substantial international experience but no NDA sponsor. There is an equally real conversation about whether European practice leans too readily on small, uncontrolled studies. Both are worth having. What I am increasingly convinced of, as a French physician training in the American system, is that the divergence is not a failure of either agency. It is the price of two different answers to the same hard question: *what do you do when patients suffer and the evidence is thin?*

For now, the most useful thing I can do is the smallest and the slowest — turn an exploratory hazard ratio into a hypothesis worth testing, and write it down clearly enough that someone, somewhere with the means to run the trial, might decide it is worth the trouble.

---


<script>
window.addEventListener('message',function(e){
  if(e.data && e.data.type==='mtFigHeight'){
    document.querySelectorAll('iframe.mt-fig').forEach(function(f){
      if(f.contentWindow===e.source){ f.style.height=(e.data.h+8)+'px'; }
    });
  }
});
</script>
