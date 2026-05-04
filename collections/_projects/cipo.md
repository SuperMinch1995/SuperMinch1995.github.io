---
layout: home
title: "Chronic Intestinal Pseudo-Obstruction (CIPO)"
description: ""
date: 2024-01-01
weight: 1
thumbnail: "/assets/images/cipo_distension.jpg"
client: "Greater Paris University Hospitals"
categories: ["Neurogastroenterology"]
role: "Physician-Researcher"
---

<!-- ── CIPO SECTION ─────────────────────────────────────────────────── -->
<style>
h1 { text-align: center; }
.cipo-section {
  margin: 60px 0 3rem;
  font-size: 0.85em;
  text-align: center;
}
.cipo-headline {
  font-size: 1.55em;
  font-weight: 700;
  color: var(--color-base-text);
  line-height: 1.25;
  margin: 0 0 2.5rem;
  letter-spacing: -0.01em;
}
.cipo-map-frame {
  width: 100%;
  overflow: hidden;
  background: transparent;
}
.cipo-map-frame iframe {
  display: block;
  width: 100%;
  height: 540px;
  border: none;
  background: transparent;
}
.cipo-stats-row {
  display: flex;
  justify-content: center;
  gap: 3rem;
  margin: 2.5rem 0 3.75rem;
  flex-wrap: wrap;
}
.cipo-stat {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}
.cipo-stat-num {
  font-size: 2em;
  font-weight: 700;
  color: #C2510A;
  line-height: 1;
}
.cipo-stat-label {
  font-size: 0.88em;
  color: var(--color-base-text-2);
  letter-spacing: 0.04em;
}
.cipo-subline {
  font-size: 1.15em;
  color: var(--color-base-text);
  line-height: 1.6;
  text-align: center;
  margin: 0.8rem auto 3.75rem;
  max-width: 620px;
  font-weight: 400;
}
.pencil-mark {
  position: relative;
  display: inline;
  white-space: nowrap;
  padding-bottom: 4px;
}
.pencil-mark img.pencil-underline {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -5px;
  width: 100%;
  height: 8px;
  pointer-events: none;
  object-fit: fill;
}
.brain-gut-img-wrap {
  margin: -1.5rem auto 2rem;
  max-width: 200px;
}
.brain-gut-img {
  display: block;
  width: 100%;
  height: auto;
  mix-blend-mode: multiply;
}

</style>

<div class="cipo-section">


  <p class="cipo-subline">CIPO is a disorder where the <span class="pencil-mark">bowels fail to move food<img src="/assets/images/underlines/underline-bowels.svg" class="pencil-underline" aria-hidden="true" alt=""></span> despite <span class="pencil-mark">no physical blockage<img src="/assets/images/underlines/underline-blockage.svg" class="pencil-underline" aria-hidden="true" alt=""></span>.</p>
  <p class="cipo-subline">Lesions may arise anywhere along the brain-gut axis.</p>
  <div class="brain-gut-img-wrap">
    <img src="/assets/images/brain-gut.png"
         alt="Brain-gut axis — bidirectional communication diagram"
         class="brain-gut-img">
  </div>
  <p class="cipo-subline">We studied the <span class="pencil-mark">largest patient cohort<img src="/assets/images/underlines/underline-largest-patient-cohort.svg" class="pencil-underline" aria-hidden="true" alt=""></span> to date.</p>

  <div class="cipo-stats-row">
    <div class="cipo-stat">
      <span class="cipo-stat-num">130</span>
      <span class="cipo-stat-label">Patients</span>
    </div>
    <div class="cipo-stat">
      <span class="cipo-stat-num">15+</span>
      <span class="cipo-stat-label">Countries of birth</span>
    </div>
    <div class="cipo-stat">
      <span class="cipo-stat-num">19–74</span>
      <span class="cipo-stat-label">Age range (years)</span>
    </div>
  </div>

  <div class="cipo-map-frame">
    <iframe src="/assets/figures/cipo-map.html"
            title="Where Patients Were Born — CIPO cohort"
            loading="lazy"
            scrolling="no">
    </iframe>
  </div>
</div>


<!-- ── END CIPO SECTION ──────────────────────────────────────────────── -->

<!-- ── SUNBURST SECTION ─────────────────────────────────────────────── -->
<style>
.sunburst-section {
  margin: 3rem 0 2.5rem;
  text-align: center;
}
.sunburst-frame {
  width: 100%;
  overflow: hidden;
  background: transparent;
}
.sunburst-frame iframe {
  display: block;
  width: 100%;
  height: 620px;
  border: none;
  background: transparent;
}
</style>

<div class="sunburst-section">
  <div class="sunburst-frame">
    <iframe id="sunburst-iframe"
            src="/assets/figures/cipo-sunburst.html"
            title="CIPO — Genetic diagnosis sunburst"
            loading="lazy"
            scrolling="no">
    </iframe>
  </div>
</div>

<!-- ── END SUNBURST SECTION ─────────────────────────────────────────── -->

<!-- ── ACTG2 Q247P SECTION ──────────────────────────────────────────── -->
<style>
.q247p-section {
  text-align: center;
  margin: 3rem 0 2.5rem;
  border-top: none;
}
.q247p-headline {
  font-size: 1.15em;
  font-weight: 400;
  color: var(--color-base-text);
  margin: 0 0 0.35rem;
}
.q247p-subline {
  font-size: 0.85em;
  color: var(--color-base-text-2);
  margin: 0 0 1.2rem;
  line-height: 1.6;
}
.q247p-subline-italic {
  font-style: italic;
  margin: 0;
}
.q247p-see-ex {
  font-size: 0.78em;
  font-weight: 500;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: #C2510A;
  margin: 0 0 .5rem;
}
.q247p-caption-line {
  width: 32px;
  height: 1px;
  background: #C2510A;
  opacity: .4;
  margin: 0 auto .75rem;
}
.q247p-caption-toggle {
  transition: opacity .15s ease;
}
.q247p-caption-toggle:hover { opacity: .75; }
.q247p-frame-collapsible {
  display: none;
  margin-top: 2rem;
}
.q247p-caption-toggle.open ~ .q247p-frame-collapsible {
  display: block;
}
.q247p-frame {
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  overflow: hidden;
  background: transparent;
}
.q247p-frame iframe {
  zoom: 0.82;
  display: block;
  width: 100%;
  min-height: 600px;
  border: none;
  background: transparent;
}
@media (max-width: 768px) {
  .q247p-frame iframe {
    zoom: 1;
    min-height: 600px;
  }
}
</style>

<div class="q247p-section">
  <h3 class="q247p-headline">We found mutations with distinct mechanisms.</h3>
  <img src="/assets/images/allvariants.gif"
       alt="All ACTG2 variants — structural overview"
       style="display:block;margin:1.5rem auto 0;max-width:680px;width:100%;height:auto;">
  <div class="q247p-caption-toggle" onclick="this.classList.toggle('open')" role="button" aria-expanded="false" style="margin-top:60px;cursor:pointer;text-align:center;max-width:560px;margin-left:auto;margin-right:auto;">
    <p class="q247p-see-ex">See an example</p>
    <div class="q247p-caption-line"></div>
    <p class="q247p-subline q247p-subline-italic">A single amino acid substitution replaces a flexible glutamine with a rigid proline, disrupting γ-2 actin polymerization in intestinal smooth muscle.</p>
  </div>
  <div class="q247p-frame q247p-frame-collapsible">
    <iframe src="/assets/figures/actg2-q247p.html"
            title="ACTG2 Q247P — structural impact on γ-2 actin"
            loading="lazy"
            scrolling="no">
    </iframe>
  </div>
</div>

<!-- ── END ACTG2 Q247P SECTION ──────────────────────────────────────── -->