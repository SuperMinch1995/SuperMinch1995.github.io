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

/* Narration bridges between acts. Three variants:
   - default: standard transition phrase between acts
   - --first: opening hook at top of page
   - --caption: small italic subtitle under a figure
   - --closing: emotional landing at end of page */
.act-bridge {
  font-size: 0.98em;
  color: var(--color-base-text);
  line-height: 1.6;
  text-align: center;
  margin: 3.5rem auto;
  max-width: 620px;
  font-weight: 400;
  letter-spacing: 0.005em;
}
.act-bridge--first {
  margin: 2.5rem auto 1rem;
}
.act-bridge--caption {
  font-size: 0.78em;
  color: var(--color-base-text-2);
  font-style: italic;
  margin: -1.5rem auto 3rem;
  letter-spacing: 0.02em;
}
.act-bridge--closing {
  font-style: italic;
  color: var(--color-base-text-2);
  margin: 4rem auto 4.5rem;
}
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

<p class="act-bridge act-bridge--first">Your gut never stops moving.<br><br>It needs a protein called γ-2 actin.</p>

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

<p class="act-bridge">Proteins are made of amino acids.</p>

<p class="act-bridge">What if one amino acid was wrong?</p>

<p class="act-bridge">In this example, the Glutamine (Q) at the position 247</p>

<p class="act-bridge">is replaced by a proline (P, mutant).</p>

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
   posted by /assets/figures/actg2-wt-mutant.html.
   IMPORTANT: filter by e.source so messages from other iframes
   (e.g. act1-iframe = 3D viewer) don't accidentally resize this one. */
(function () {
  window.addEventListener('message', function (e) {
    if (!e.data || typeof e.data.q247pHeight !== 'number') return;
    var iframe = document.getElementById('act2-iframe');
    if (!iframe || e.source !== iframe.contentWindow) return;
    var h = Math.min(Math.max(e.data.q247pHeight, 400), 6000); // safety cap
    iframe.style.height = h + 'px';
  });
})();
</script>

<p class="act-bridge">This is what happens in real patients.</p>

<!-- ══════════════════════════════════════════════════
     ACT 3 — CIPO STORY
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
  <p class="cipo-subline">We explore it in 130 people.</p>

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

<p class="act-bridge">ACTG2 is the gene behind γ-2 actin.</p>

<!-- ══════════════════════════════════════════════════
     SUNBURST
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

<p class="act-bridge">ACTG2 wasn't the only suspect.</p>

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

<script>
/* Auto-adjust sunburst iframe height based on sunburstHeight messages
   posted by /assets/figures/cipo-sunburst.html.
   Filter by e.source so other iframes' messages don't leak in. */
(function () {
  window.addEventListener('message', function (e) {
    if (!e.data || typeof e.data.sunburstHeight !== 'number') return;
    var iframe = document.getElementById('sunburst-iframe');
    if (!iframe || e.source !== iframe.contentWindow) return;
    var h = Math.min(Math.max(e.data.sunburstHeight, 400), 6000); // safety cap
    iframe.style.height = h + 'px';
  });
})();
</script>

<p class="act-bridge act-bridge--closing">Behind every mutation, a person waiting.</p>