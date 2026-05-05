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
.q247p-section {
  margin: 4rem 0 5rem;
  text-align: center;
  font-size: 0.85em;
}
.q247p-section .cipo-subline {
  font-size: 1.15em;
  color: var(--color-base-text);
  line-height: 1.6;
  text-align: center;
  margin: 0 auto;
  max-width: 620px;
  font-weight: 400;
}

.aa-stage {
  display: flex;
  align-items: stretch;
  justify-content: center;
  gap: 1.5rem;
  margin: 3rem auto;
  max-width: 640px;
  padding: 0 1rem;
}

.aa-card {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 0.45rem;
  padding: 1.5rem 0.5rem;
  min-width: 0;
}

.aa-tag {
  font-size: 0.62em;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--color-base-text-2);
}
.aa-tag.mut { color: #C2510A; }

.aa-letter {
  font-family: 'DM Mono', 'DM Sans', monospace;
  font-size: 5em;
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.03em;
  color: var(--color-base-text);
  margin: 0.4rem 0 0.25rem;
  position: relative;
  display: inline-block;
}
.aa-letter.mut { color: #C2510A; }

.aa-letter .yellow-stroke {
  position: absolute;
  left: -10%;
  right: -10%;
  bottom: -4px;
  width: 120%;
  height: 12px;
  pointer-events: none;
  overflow: visible;
}
.aa-letter .yellow-stroke path {
  stroke: #F5C842;
  stroke-width: 5;
  stroke-linecap: round;
  fill: none;
  stroke-dasharray: 130;
  stroke-dashoffset: 130;
  filter: drop-shadow(0 0 3px rgba(245, 200, 66, 0.5));
}

.aa-name {
  font-size: 0.92em;
  color: var(--color-base-text);
  font-weight: 500;
  margin-top: 0.5rem;
}

.aa-trait {
  font-size: 0.72em;
  color: var(--color-base-text-2);
  letter-spacing: 0.04em;
  font-weight: 400;
}

/* ── Lightning bolt zone ── */
.aa-bolt-zone {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0 0.4rem;
  min-width: 64px;
  flex-shrink: 0;
}

.bolt {
  width: 36px;
  height: 54px;
  filter: drop-shadow(0 0 6px rgba(245, 200, 66, 0.45));
}

.spark {
  position: absolute;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: #F5C842;
  box-shadow: 0 0 6px rgba(255, 224, 102, 0.9);
  opacity: 0;
  pointer-events: none;
}
.spark:nth-child(2) { top: 30%; left: 6%;  --tx: -18px; --ty: -16px; }
.spark:nth-child(3) { top: 38%; right: 6%; --tx:  18px; --ty: -12px; }
.spark:nth-child(4) { bottom: 30%; left: 8%; --tx: -16px; --ty: 14px; }
.spark:nth-child(5) { bottom: 28%; right: 6%; --tx: 16px; --ty: 16px; }

.bolt-label {
  font-family: 'DM Mono', 'DM Sans', monospace;
  font-size: 0.6em;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: #C2510A;
  margin-top: 0.55rem;
  white-space: nowrap;
  opacity: 0;
}

/* ── Animations triggered when section enters viewport ── */
.aa-stage.in-view .bolt {
  animation: boltStrike 0.7s 0.4s ease-out forwards,
             boltPulse 2.4s 1.2s ease-in-out infinite;
}
.aa-stage.in-view .spark {
  animation: sparkFly 2.4s ease-out infinite;
}
.aa-stage.in-view .spark:nth-child(2) { animation-delay: 1.0s; }
.aa-stage.in-view .spark:nth-child(3) { animation-delay: 1.4s; }
.aa-stage.in-view .spark:nth-child(4) { animation-delay: 1.8s; }
.aa-stage.in-view .spark:nth-child(5) { animation-delay: 2.2s; }
.aa-stage.in-view .bolt-label {
  animation: fadeIn 0.6s 0.9s ease-out forwards;
}

.aa-stage.in-view .aa-card.mut .aa-tag    { animation: fadeUp 0.55s 1.2s ease-out backwards; }
.aa-stage.in-view .aa-card.mut .aa-letter { animation: fadeUp 0.55s 1.35s ease-out backwards; }
.aa-stage.in-view .aa-card.mut .aa-name   { animation: fadeUp 0.55s 1.55s ease-out backwards; }
.aa-stage.in-view .aa-card.mut .aa-trait  { animation: fadeUp 0.55s 1.7s ease-out backwards; }
.aa-stage.in-view .aa-letter.mut .yellow-stroke path {
  animation: drawStroke 1s 1.7s ease-out forwards;
}

/* Pre-animation state (only when JS attaches the observer) */
.aa-stage.js-armed .aa-card.mut > * { opacity: 0; }
.aa-stage.js-armed .bolt           { opacity: 0; transform: scale(0.3); }
.aa-stage.js-armed .bolt-label     { opacity: 0; }

@keyframes boltStrike {
  0%   { opacity: 0; transform: scale(0.3); filter: drop-shadow(0 0 0 rgba(245,200,66,0)); }
  45%  { opacity: 1; transform: scale(1.45); filter: drop-shadow(0 0 26px rgba(255,215,0,1))
                                                       drop-shadow(0 0 50px rgba(255,200,80,0.55)); }
  100% { opacity: 1; transform: scale(1);   filter: drop-shadow(0 0 6px rgba(245,200,66,0.45)); }
}
@keyframes boltPulse {
  0%, 100% { filter: drop-shadow(0 0 6px rgba(245,200,66,0.4)); transform: scale(1); }
  50%      { filter: drop-shadow(0 0 16px rgba(245,200,66,0.85))
                     drop-shadow(0 0 30px rgba(255,215,0,0.5)); transform: scale(1.08); }
}
@keyframes sparkFly {
  0%   { opacity: 0; transform: translate(0,0) scale(1); }
  18%  { opacity: 1; }
  100% { opacity: 0; transform: translate(var(--tx), var(--ty)) scale(0.3); }
}
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes drawStroke {
  to { stroke-dashoffset: 0; }
}

/* ── Mobile: stack cards vertically, one panel at a time ── */
@media (max-width: 600px) {
  .aa-stage {
    flex-direction: column;
    gap: 0.5rem;
    max-width: 320px;
  }
  .aa-card { padding: 1rem 0.5rem; }
  .aa-letter { font-size: 4em; }
  .aa-bolt-zone {
    flex-direction: row;
    padding: 0.4rem 0;
    min-height: 60px;
    gap: 0.7rem;
  }
  .bolt-label { margin-top: 0; margin-left: 0.3rem; }
}
</style>

<div class="q247p-section">

  <p class="cipo-subline">A single substitution rewrites the protein.</p>

  <div class="aa-stage" id="aa-stage">

    <!-- Wild-type -->
    <div class="aa-card">
      <div class="aa-tag">Wild-type</div>
      <div class="aa-letter">Q</div>
      <div class="aa-name">Glutamine</div>
      <div class="aa-trait">flexible · polar</div>
    </div>

    <!-- Lightning -->
    <div class="aa-bolt-zone">
      <svg class="bolt" viewBox="0 0 24 36" fill="none" aria-hidden="true">
        <path d="M14 1.5L2.5 20.5h8L8.5 34.5l13-18h-8L14 1.5z"
              fill="#F5C842" stroke="#FFE066" stroke-width="0.5"
              stroke-linejoin="round"/>
      </svg>
      <span class="spark"></span>
      <span class="spark"></span>
      <span class="spark"></span>
      <span class="spark"></span>
      <div class="bolt-label">Q247P</div>
    </div>

    <!-- Mutant -->
    <div class="aa-card mut">
      <div class="aa-tag mut">Mutant</div>
      <div class="aa-letter mut">P<svg class="yellow-stroke" viewBox="0 0 100 12" preserveAspectRatio="none" aria-hidden="true"><path d="M3,7 Q22,3 48,5.5 T97,4.5"/></svg></div>
      <div class="aa-name">Proline</div>
      <div class="aa-trait">rigid · cyclic</div>
    </div>

  </div>

  <p class="cipo-subline">Disrupting γ-2 actin polymerization in intestinal smooth muscle.</p>

</div>

<script>
(function () {
  var stage = document.getElementById('aa-stage');
  if (!stage) return;
  stage.classList.add('js-armed');
  if (!('IntersectionObserver' in window)) {
    stage.classList.add('in-view');
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        stage.classList.add('in-view');
        io.unobserve(stage);
      }
    });
  }, { threshold: 0.35 });
  io.observe(stage);
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