---
layout: basic
title: "Research"
permalink: /research/
---

<style>
.research-timeline {
  position: relative;
  padding-left: 2rem;
  margin: 2rem 0;
}
.research-timeline::before {
  content: '';
  position: absolute;
  left: 6px;
  top: 4px;
  bottom: 4px;
  width: 0.5px;
  background: var(--color-base-border, #ddd);
}
.rt-section-title {
  font-size: 0.72em;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #C2510A;
  margin: 2rem 0 1rem;
}
.rt-section-title:first-child { margin-top: 0; }
.rt-item {
  position: relative;
  margin-bottom: 1.5rem;
}
.rt-item:has(.rt-thumb) {
  padding-right: 140px;
  min-height: 84px;
}
.rt-dot {
  position: absolute;
  left: -2rem;
  top: 4px;
  width: 13px;
  height: 13px;
  border-radius: 50%;
  border: 0.5px solid #ccc;
  background: var(--color-base-bg);
  display: flex;
  align-items: center;
  justify-content: center;
}
.rt-dot-inner {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #C2510A;
}
.rt-dot-inner.grey { background: #bbb; }
html[data-bs-theme="dark"] .rt-dot-inner.grey { background: #555; }
.rt-thumb {
  position: absolute;
  top: 4px;
  right: 0;
  width: 120px;
  height: 80px;
  object-fit: cover;
  border-radius: 3px;
  border: 0.5px solid var(--color-base-border, #ddd);
  background: var(--color-base-bg);
}
html[data-bs-theme="dark"] .rt-thumb {
  border-color: rgba(255,255,255,0.1);
}
.rt-title {
  font-size: 1em;
  font-weight: 600;
  color: var(--color-base-text);
  line-height: 1.4;
  margin: 0 0 0.25rem;
}
.rt-meta {
  font-size: 0.82em;
  color: var(--color-base-text);
  opacity: 0.55;
  margin: 0 0 0.35rem;
}
.rt-abstract {
  font-size: 0.83em;
  color: var(--color-base-text);
  opacity: 0.7;
  line-height: 1.6;
  margin: 0 0 0.4rem;
}
.rt-citation {
  font-size: 0.82em;
  color: var(--color-base-text);
  opacity: 0.65;
  font-style: italic;
  line-height: 1.5;
  margin: 0 0 0.4rem;
}
.rt-links {
  display: flex;
  gap: 0.6rem;
  flex-wrap: wrap;
}
.rt-link {
  font-size: 0.75em;
  font-weight: 500;
  color: #C2510A;
  text-decoration: none;
  border: 0.5px solid #C2510A;
  border-radius: 3px;
  padding: 0.15em 0.55em;
  transition: opacity 0.15s;
}
.rt-link:hover { opacity: 0.7; }
html[data-bs-theme="dark"] .rt-link {
  color: #E8845A;
  border-color: #E8845A;
}
.rt-divider {
  border: none;
  border-top: 0.5px solid var(--color-base-border, #ddd);
  margin: 0 0 1.5rem;
}
@media (max-width: 600px) {
  .rt-item:has(.rt-thumb) {
    padding-right: 0;
    min-height: 0;
  }
  .rt-thumb {
    position: static;
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 3 / 2;
    margin: 0 0 0.6rem;
  }
}
</style>

<div class="research-timeline">

  <div class="rt-section-title">In progress</div>

  <div class="rt-item">
    <div class="rt-dot"><div class="rt-dot-inner grey"></div></div>
    <img class="rt-thumb" src="/assets/images/MF-hero.webp" alt="Phylogenetic divergence between skin and nodal mycosis fungoides clones">
    <p class="rt-title">Mycosis fungoides with nodal progression harbors recurrent SOCS1 mutations and JAK2 rearrangements</p>
    <p class="rt-meta">Ta MC, … · In reviewing</p>
    <p class="rt-abstract">Mutations in skin and lymph node samples indicated intratumoral heterogeneity and branched evolution between the skin and the lymph node.</p>
  </div>

  <div class="rt-item">
    <div class="rt-dot"><div class="rt-dot-inner grey"></div></div>
    <img class="rt-thumb" src="/assets/images/Clock-hero.webp" alt="Clock gene expression in NOS1+ enteric nitrergic neurons">
    <p class="rt-title">Clock gene expression in NOS1+ nitrergic neurons in intestinal dysmotility</p>
    <p class="rt-meta">Ta MC, … · In preparation</p>
    <p class="rt-abstract">snRNA-seq analysis of the Drokhlyansky 2020 human enteric nervous system dataset (GSE148822). Central hypothesis: circadian misalignment of nitrergic neurons as a driver of enteric dysmotility.</p>
  </div>

  <hr class="rt-divider">
  <div class="rt-section-title">Publications</div>

  <div class="rt-item">
    <div class="rt-dot"><div class="rt-dot-inner"></div></div>
    <img class="rt-thumb" src="/assets/images/AJG-2026-hero.webp" alt="Histogenetic classification predicts outcomes in 130 adults with chronic intestinal pseudo-obstruction - CIPO">
    <p class="rt-title">Histogenetic Classification Predicts Outcomes in 130 Adults With Chronic Intestinal Pseudo-Obstruction</p>
    <p class="rt-meta">First author · Am J Gastroenterol · 2026</p>
    <p class="rt-citation">Ta MC, et al. <em>Am J Gastroenterol.</em> 2026. doi:10.14309/…</p>
    <div class="rt-links">
      <a class="rt-link" href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener">↗ PubMed</a>
      <a class="rt-link" href="https://doi.org/10.14309/" target="_blank" rel="noopener">↗ DOI</a>
      <a class="rt-link" href="/publications/cipo-2026/">About the project</a>
    </div>
  </div>

  <div class="rt-item">
    <div class="rt-dot"><div class="rt-dot-inner"></div></div>
    <img class="rt-thumb" src="/assets/images/NR1D1-hero.webp" alt="NR1D1::MAML3 fusion structure with breakpoints in mesenchymal neoplasm">
    <p class="rt-title">NR1D1::MAML3 Fusion in an Aggressive Mesenchymal Neoplasm</p>
    <p class="rt-meta">First author · Genes Chromosomes Cancer · 2025</p>
    <p class="rt-citation">Ta MC, et al. <em>Genes Chromosomes Cancer.</em> 2025. doi:10.1002/…</p>
    <div class="rt-links">
      <a class="rt-link" href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener">↗ PubMed</a>
      <a class="rt-link" href="https://doi.org/10.1002/" target="_blank" rel="noopener">↗ DOI</a>
      <a class="rt-link" href="/publications/NR1D1-2025/">About the project</a>
    </div>
  </div>

  <div class="rt-item">
    <div class="rt-dot"><div class="rt-dot-inner"></div></div>
    <img class="rt-thumb" src="/assets/images/Lancet-hero.webp" alt="National framework for genomic medicine integration in France">
    <p class="rt-title">PFMG2025 — Integrating Genomic Medicine into the National Healthcare System in France</p>
    <p class="rt-meta">Co-author · Lancet Reg Health Eur · 2025</p>
    <p class="rt-citation">… Ta MC, et al. <em>Lancet Reg Health Eur.</em> 2025. doi:10.1016/…</p>
    <div class="rt-links">
      <a class="rt-link" href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener">↗ PubMed</a>
      <a class="rt-link" href="https://doi.org/10.1016/" target="_blank" rel="noopener">↗ DOI</a>
    </div>
  </div>

  <div class="rt-item">
    <div class="rt-dot"><div class="rt-dot-inner"></div></div>
    <img class="rt-thumb" src="/assets/images/neurology-hero.webp" alt="Leptomeningeal angioma with GNA11 pathogenic variation">
    <p class="rt-title">Late-Onset Status Epilepticus Associated With Isolated Leptomeningeal Angioma and Sturge-Weber Syndrome-Related GNA11 Pathogenic Variation</p>
    <p class="rt-meta">Co-author · Neurology · 2023</p>
    <p class="rt-citation">… Ta MC, et al. <em>Neurology.</em> 2023. doi:10.1212/…</p>
    <div class="rt-links">
      <a class="rt-link" href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener">↗ PubMed</a>
      <a class="rt-link" href="https://doi.org/10.1212/" target="_blank" rel="noopener">↗ DOI</a>
    </div>
  </div>

  <div class="rt-item">
    <div class="rt-dot"><div class="rt-dot-inner"></div></div>
    <img class="rt-thumb" src="/assets/images/SOCS1-hero.webp" alt="Intestinal phenotypic spectrum of SOCS1 haploinsufficiency">
    <p class="rt-title">Insights Into the Expanding Intestinal Phenotypic Spectrum of SOCS1 Haploinsufficiency and Therapeutic Options</p>
    <p class="rt-meta">Co-author · J Clin Immunol · 2023</p>
    <p class="rt-citation">… Ta MC, et al. <em>J Clin Immunol.</em> 2023. doi:10.1007/…</p>
    <div class="rt-links">
      <a class="rt-link" href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener">↗ PubMed</a>
      <a class="rt-link" href="https://doi.org/10.1007/" target="_blank" rel="noopener">↗ DOI</a>
    </div>
  </div>

</div>