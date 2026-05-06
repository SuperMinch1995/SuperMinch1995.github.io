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

<style>
h1 { text-align: center; }
</style>

<!-- ══════════════════════════════════════════════════
     ACT 1 — 3D PROTEIN VIEWER
═══════════════════════════════════════════════════ -->
<style>
.act1-section {
  margin: 2.5rem auto 4rem;
  text-align: center;
}
.act1-frame {
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
  overflow: hidden;
  background: transparent;
}
.act1-frame iframe {
  display: block;
  width: 100%;
  height: 580px;
  border: none;
  background: transparent;
}
@media (max-width: 768px) {
  .act1-frame iframe { height: 460px; }
}
</style>

<div class="act1-section">
  <div class="act1-frame">
    <iframe src="/assets/figures/actg2-q247p.html"
            title="ACTG2 Q247P — interactive 3D viewer"
            loading="lazy"
            scrolling="no"
            allowtransparency="true">
    </iframe>
  </div>
</div>

<!-- ══════════════════════════════════════════════════
     ACT 2 — WILD-TYPE → MUTANT TRANSITION
═══════════════════════════════════════════════════ -->
<style>
.act2-section {
  margin: 4rem auto 5rem;
  text-align: center;
}
.act2-frame {
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
  overflow: hidden;
  background: transparent;
}
.act2-frame iframe {
  display: block;
  width: 100%;
  height: 1200px;
  border: none;
  background: transparent;
}
</style>

<div class="act2-section">
  <div class="act2-frame">
    <iframe id="act2-iframe"
            src="/assets/figures/actg2-wt-mutant.html"
            title="ACTG2 Q247P — wild-type vs mutant"
            loading="lazy"
            scrolling="no"
            allowtransparency="true">
    </iframe>
  </div>
</div>

<script>
/* Auto-adjust iframe height based on q247pHeight messages
   posted by /assets/figures/actg2-wt-mutant.html */
(function () {
  window.addEventListener('message', function (e) {
    if (e.data && typeof e.data.q247pHeight === 'number') {
      var iframe = document.getElementById('act2-iframe');
      if (iframe) iframe.style.height = e.data.q247pHeight + 'px';
    }
  });
})();
</script>

<!-- ══════════════════════════════════════════════════
     ACT 3 — CIPO STORY  (UNCHANGED)
═══════════════════════════════════════════════════ -->
<style>
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
            scrolling="no"
            allowtransparency="true">
    </iframe>
  </div>
</div>

<!-- ══════════════════════════════════════════════════
     SUNBURST  (UNCHANGED)
═══════════════════════════════════════════════════ -->
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
            scrolling="no"
            allowtransparency="true">
    </iframe>
  </div>
</div>