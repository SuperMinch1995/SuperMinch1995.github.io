---
layout: home
title: "This is an interactive scientific journey built from my research project"
description: ""
date: 2024-01-01
weight: 1
thumbnail: ""
client: ""
categories: ["Neurogastroenterology"]
role: "Physician-scientist"
---

<!-- ══════════════════════════════════════════════════
     NARRATION STYLE
═══════════════════════════════════════════════════ -->

<style>
h1 {
  text-align: center;
  animation: titleSettle 0.7s ease-out 0.15s both;
}
@keyframes titleSettle {
  from { opacity: 0; transform: translateY(-6px); }
  to   { opacity: 1; transform: translateY(0); }
}
.opening-section {
  margin-top: 3.5rem;
}

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
.reveal-cta {
  display: flex;
  justify-content: center;
  margin: 0.5rem auto 4rem;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.7s ease, transform 0.7s ease;
  pointer-events: none;
}
.reveal-cta.visible {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}
.reveal-cta.hiding {
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s ease;
}
.cta-arrow {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: none;
  background: var(--color-base-bg, #FBF6EC);
  color: #C2510A;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  position: relative;
  transition: transform 0.2s ease, background 0.25s ease, color 0.25s ease;
}
.cta-arrow:hover {
  transform: translateY(3px);
  background: #C2510A;
  color: var(--color-base-bg, #FBF6EC);
}
.cta-arrow svg {
  width: 22px;
  height: 22px;
  display: block;
}

@keyframes ctaPulse {
  0%, 100% {
    box-shadow: 0 0 0 0 rgba(245, 200, 66, 0),
                0 0 0 0 rgba(245, 200, 66, 0);
  }
  50% {
    box-shadow: 0 0 0 6px rgba(245, 200, 66, 0.7),
                0 0 24px 4px rgba(245, 200, 66, 0.55),
                0 0 48px 8px rgba(245, 200, 66, 0.3);
  }
}
.cta-halo {
  animation: ctaPulse 1.6s ease-in-out infinite;
}

.reveal-target {
  display: none;
}
.reveal-target.revealed {
  display: block;
  animation: revealFade 0.9s ease-out;
}
@keyframes revealFade {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
</style>

<noscript>
<style>
  .reveal-target { display: block !important; }
  .reveal-cta { display: none !important; }
</style>
</noscript>

<!-- ══════════════════════════════════════════════════
     OPENING — SILENCE TO MOTION
═══════════════════════════════════════════════════ -->
<style>
.opening-section {
  margin: 2.5rem auto 4rem;
}
.opening-frame {
  width: 100%;
  background: transparent;
}
.opening-frame iframe {
  display: block;
  width: 100%;
  height: 360px;
  border: none;
  background: transparent;
}
@media (max-width: 768px) {
  .opening-frame iframe { height: 280px; }
}
</style>

<div class="opening-section">
  <div class="opening-frame">
    <iframe src="/assets/figures/cipo-opening.html"
            title="Opening — silence to motion"
            loading="eager"
            scrolling="no"
            allowtransparency="true">
    </iframe>
  </div>
</div>

<div class="reveal-cta" id="reveal-cta">
  <button class="cta-arrow cta-halo" id="reveal-button" aria-label="Continue the journey">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <polyline points="6 9 12 15 18 9"/>
    </svg>
  </button>
</div>

<div class="reveal-target" id="reveal-target">

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
    <iframe data-src="/assets/figures/actg2-q247p-v3-pedagogique.html"
            title="ACTG2 Q247P — interactive 3D viewer"
            loading="eager"
            scrolling="no"
            allowtransparency="true">
    </iframe>
  </div>
</div>

<p class="act-bridge">At first glance, the mutation looks subtle.

<br><br>The mutation did not simply change an amino acid.

<br><br>One amino acid.

<br><br>One surface residue.

<br><br>But proteins are mechanical systems.

<br><br>To understand why Q247P matters, we need to zoom in further.</p>

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
  <p class="cipo-subline">Dysfunction may emerge from any point along the brain–gut axis</p>
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

<p class="act-bridge">We genotyped hundred of unsolved cases.</p>

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

<p class="act-bridge">Sometimes, the mutation is invisible.</p>

<p class="act-bridge">Behind every mutation is a person waiting.</p>

<p class="act-bridge act-bridge--closing">Discover our patients' stories.</p>

</div>

<script>
(function () {
  var ctaEl = document.getElementById('reveal-cta');
  var targetEl = document.getElementById('reveal-target');
  var btn = document.getElementById('reveal-button');
  var arrowShown = false;
  var revealed = false;

  function showArrow() {
    if (arrowShown) return;
    arrowShown = true;
    ctaEl.classList.add('visible');
  }

  /* Listen specifically to the opening iframe — filter by source
     so other iframes' messages (sunburst, wt-mutant) don't trigger this. */
  window.addEventListener('message', function (e) {
    var openingFrame = document.querySelector('.opening-frame iframe');
    if (!openingFrame || e.source !== openingFrame.contentWindow) return;
    if (e.data && e.data.cipoOpeningTextReady) {
      setTimeout(showArrow, 1500);
    }
  });

  /* Fallback: if the message is ever missed (iframe load failure, etc.),
     show the arrow at 10s so the page never gets stuck. */
  setTimeout(showArrow, 10000);

  function reveal() {
    if (revealed) return;
    revealed = true;

    /* Lazy-load any iframe with data-src. This is what keeps actg2-q247p
       from auto-playing its narrative until the user is ready. */
    var lazyIframes = targetEl.querySelectorAll('iframe[data-src]');
    Array.prototype.forEach.call(lazyIframes, function (iframe) {
      iframe.src = iframe.getAttribute('data-src');
      iframe.removeAttribute('data-src');
    });

    targetEl.classList.add('revealed');
    ctaEl.classList.add('hiding');

    /* Smooth scroll to the protein viewer once the reveal has begun. */
    setTimeout(function () {
      var act1 = document.querySelector('.act1-section');
      if (act1) {
        act1.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 400);
  }

  btn.addEventListener('click', reveal);
})();
</script>