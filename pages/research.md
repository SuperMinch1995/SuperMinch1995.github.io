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

.rt-section-title:first-child {
  margin-top: 0;
}

.rt-item {
  position: relative;
  margin-bottom: 1.5rem;
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

.rt-dot-inner.grey {
  background: #bbb;
}

html[data-bs-theme="dark"] .rt-dot-inner.grey {
  background: #555;
}

.rt-thumb {
  display: block;
  width: 100%;
  height: 110px;
  object-fit: cover;
  border-radius: 3px;
  border: 0.5px solid var(--color-base-border, #ddd);
  background: var(--color-base-bg);
  margin-bottom: 0.6rem;
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

.rt-link:hover {
  opacity: 0.7;
}

html[data-bs-theme="dark"] .rt-link {
  color: #E8845A;
  border-color: #E8845A;
}

.rt-thumb-link {
  display: block;
  text-decoration: none;
  color: inherit;
}

.rt-thumb-link:hover,
.rt-thumb-link:focus,
.rt-thumb-link:active {
  text-decoration: none !important;
  opacity: 1;
  color: inherit;
}

.rt-divider {
  border: none;
  border-top: 0.5px solid var(--color-base-border, #ddd);
  margin: 0 0 1.5rem;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .research-timeline {
    padding-left: 1.5rem;
  }

  .rt-dot {
    left: -1.5rem;
  }

  .rt-thumb {
    height: 90px;
  }

  .rt-title {
    font-size: 0.95em;
  }

  .rt-abstract {
    font-size: 0.8em;
  }
}
</style>

<div class="research-timeline">

  <div class="rt-section-title">In progress</div>

  <div class="rt-item">
    <div class="rt-dot">
      <div class="rt-dot-inner grey"></div>
    </div>

    <img class="rt-thumb"
         src="/assets/images/MF-hero.webp"
         alt="Phylogenetic divergence between skin and nodal mycosis fungoides clones">

    <p class="rt-title">
      Mycosis fungoides with nodal progression harbors recurrent SOCS1 mutations and JAK2 rearrangements
    </p>

    <p class="rt-meta">
      In preparation
    </p>

    <p class="rt-abstract">
      In advanced Mycosis fungoides with nodal progression (ISCL-EORTC N3 stage), paired skin and lymph node analyses revealed marked intratumoral heterogeneity and branched evolution, while recurrent SOCS1 mutations and JAK2 fusions highlighted a central role for JAK/STAT pathway dysregulation.
    </p>

  </div>

  <div class="rt-item">
    <div class="rt-dot">
      <div class="rt-dot-inner grey"></div>
    </div>

    <img class="rt-thumb"
         src="/assets/images/Clock-hero.webp"
         alt="Clock gene expression in NOS1+ enteric nitrergic neurons">

    <p class="rt-title">
      Clock gene expression in NOS1+ nitrergic neurons in intestinal dysmotility
    </p>

    <p class="rt-meta">
      In preparation
    </p>

    <p class="rt-abstract">
      snRNA-seq analysis of the Drokhlyansky 2020 human enteric nervous system dataset. Hypothesis: circadian misalignment of nitrergic neurons as a driver of enteric dysmotility.
    </p>

  </div>

  <hr class="rt-divider">

  <div class="rt-section-title">Publications</div>

  <div class="rt-item">
    <div class="rt-dot">
      <div class="rt-dot-inner"></div>
    </div>

    <a href="https://superminch1995.github.io/projects/cipo/" class="rt-thumb-link">
    <img class="rt-thumb"
         src="/assets/images/AJG-2026-hero.webp"
         alt="Histogenetic classification predicts outcomes in 130 adults with chronic intestinal pseudo-obstruction">

    <p class="rt-title">
      Histogenetic Classification Predicts Outcomes in 130 Adults With Chronic Intestinal Pseudo-Obstruction
    </p>

    <p class="rt-meta">
      First author · American Journal of Gastroenterology · 2026
    </p>

    <p class="rt-abstract">
      Integrating genomic and histopathological data resolved 82% of idiopathic cases. Monogenic myopathy emerged as an independent predictor of favorable long-term survival.
    </p>
    </a>

    <div class="rt-links">
      <a class="rt-link" href="/publications/cipo-2026/">
        About the project
      </a>

      <a class="rt-link"
         href="https://pubmed.ncbi.nlm.nih.gov/41744400/"
         target="_blank"
         rel="noopener">
        PubMed
      </a>

      <a class="rt-link"
         href="https://journals.lww.com/ajg/fulltext/9900/histogenetic_classification_predicts_outcomes_in.2123.aspx"
         target="_blank"
         rel="noopener">
        DOI
      </a>
    </div>
  </div>

  <div class="rt-item">
    <div class="rt-dot">
      <div class="rt-dot-inner"></div>
    </div>

    <img class="rt-thumb"
         src="/assets/images/NR1D1-hero.webp"
         alt="NR1D1::MAML3 fusion structure with breakpoints in mesenchymal neoplasm">

    <p class="rt-title">
      NR1D1::MAML3 Fusion in an Aggressive Mesenchymal Neoplasm
    </p>

    <p class="rt-meta">
      First author · Genes Chromosomes Cancer · 2025
    </p>

    <p class="rt-abstract">
      NR1D1-rearranged tumors are emerging aggressive mesenchymal neoplasms.
    </p>

    <div class="rt-links">
      <a class="rt-link" href="/publications/NR1D1-2025/">
        About the project
      </a>

      <a class="rt-link"
         href="https://pubmed.ncbi.nlm.nih.gov/40249078/"
         target="_blank"
         rel="noopener">
        PubMed
      </a>

      <a class="rt-link"
         href="https://onlinelibrary.wiley.com/doi/10.1002/gcc.70049"
         target="_blank"
         rel="noopener">
        DOI
      </a>
    </div>
  </div>

  <div class="rt-item">
    <div class="rt-dot">
      <div class="rt-dot-inner"></div>
    </div>

    <img class="rt-thumb"
         src="/assets/images/Lancet-hero.webp"
         alt="National framework for genomic medicine integration in France">

    <p class="rt-title">
      PFMG2025 — Integrating Genomic Medicine into the National Healthcare System in France
    </p>

    <p class="rt-meta">
      Co-author · Lancet Reg Health Eur · 2025
    </p>

    <p class="rt-abstract">
      The 2025 French Genomic Medicine Initiative represents one of the first nationwide efforts to integrate whole genome sequencing into routine clinical care.
    </p>

    <div class="rt-links">
      <a class="rt-link" href="/publications/PFMG-2025/">
        About the project
      </a>

      <a class="rt-link"
         href="https://pubmed.ncbi.nlm.nih.gov/40093400/"
         target="_blank"
         rel="noopener">
        PubMed
      </a>

      <a class="rt-link"
         href="https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(24)00352-1/fulltext"
         target="_blank"
         rel="noopener">
        DOI
      </a>
    </div>
  </div>

  <div class="rt-item">
    <div class="rt-dot">
      <div class="rt-dot-inner"></div>
    </div>

    <img class="rt-thumb"
         src="/assets/images/neurology-hero.webp"
         alt="Leptomeningeal angioma with GNA11 pathogenic variation">

    <p class="rt-title">
      Late-Onset Status Epilepticus Associated With Isolated Leptomeningeal Angioma and Sturge-Weber Syndrome-Related GNA11 Pathogenic Variation
    </p>

    <p class="rt-meta">
      Co-author · Neurology · 2023
    </p>

    <p class="rt-abstract">
      Some unexplained adult-onset epilepsies may have an underlying vascular-genetic origin.
    </p>

    <div class="rt-links">
      <a class="rt-link" href="/publications/neurology-2023/">
        About the project
      </a>

      <a class="rt-link"
         href="https://pubmed.ncbi.nlm.nih.gov/37813580/"
         target="_blank"
         rel="noopener">
        PubMed
      </a>

      <a class="rt-link"
         href="https://www.neurology.org/doi/10.1212/WNL.0000000000207839"
         target="_blank"
         rel="noopener">
        DOI
      </a>
    </div>
  </div>

  <div class="rt-item">
    <div class="rt-dot">
      <div class="rt-dot-inner"></div>
    </div>

    <img class="rt-thumb"
         src="/assets/images/SOCS1-hero.webp"
         alt="Intestinal phenotypic spectrum of SOCS1 haploinsufficiency">

    <p class="rt-title">
      Insights Into the Expanding Intestinal Phenotypic Spectrum of SOCS1 Haploinsufficiency and Therapeutic Options
    </p>

    <p class="rt-meta">
      Co-author · Journal of Clinical Immunology · 2023
    </p>

    <p class="rt-abstract">
      SOCS1 haploinsufficiency can cause severe intestinal diseases, including Crohn’s disease and chronic intestinal pseudo-obstruction.
    </p>

    <div class="rt-links">
      <a class="rt-link" href="/publications/SOCS1-2023/">
        About the project
      </a>

      <a class="rt-link"
         href="https://pubmed.ncbi.nlm.nih.gov/37156989/"
         target="_blank"
         rel="noopener">
        PubMed
      </a>

      <a class="rt-link"
         href="https://link.springer.com/article/10.1007/s10875-023-01495-7"
         target="_blank"
         rel="noopener">
        DOI
      </a>
    </div>
  </div>

</div>