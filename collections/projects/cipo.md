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
[data-bs-theme="dark"] .cipo-stat-num { color: #E8845A; }
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
</style>

<div class="cipo-section">


  <p class="cipo-subline">CIPO is a disorder where the <span class="pencil-mark">bowels fail to move food<img src="/assets/images/underlines/underline-bowels.svg" class="pencil-underline" aria-hidden="true" alt=""></span> despite <span class="pencil-mark">no physical blockage<img src="/assets/images/underlines/underline-blockage.svg" class="pencil-underline" aria-hidden="true" alt=""></span>.</p>

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


<script>
(function() {
  function isDark() {
    var t = document.documentElement.getAttribute('data-bs-theme');
    return t === 'dark';
  }

  function sendTheme() {
    var iframe = document.querySelector('.cipo-map-frame iframe');
    if (!iframe || !iframe.contentWindow) return;
    try { iframe.contentWindow.postMessage({ dark: isDark() }, '*'); } catch(e) {}
  }

  window.addEventListener('load', function() {
    var iframe = document.querySelector('.cipo-map-frame iframe');
    if (iframe) {
      iframe.addEventListener('load', function() {
        sendTheme();
        setTimeout(sendTheme, 300);
      });
    }
  });

  window.addEventListener('message', function(e) {
    if (e.data && e.data.requestTheme) sendTheme();
  });

  // Observe data-bs-theme sur <html>
  new MutationObserver(sendTheme).observe(
    document.documentElement,
    { attributes: true, attributeFilter: ['data-bs-theme'] }
  );
})();
</script>

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

<script>
(function() {
  function sendThemeToSunburst() {
    var iframe = document.getElementById('sunburst-iframe');
    if (!iframe || !iframe.contentWindow) return;
    var dark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
    try { iframe.contentWindow.postMessage({ dark: dark }, '*'); } catch(e) {}
  }
  // Envois multiples pour garantir la réception
  window.addEventListener('load', function() {
    var iframe = document.getElementById('sunburst-iframe');
    if (iframe) {
      iframe.addEventListener('load', function() {
        [100, 400, 800, 1500].forEach(function(d) {
          setTimeout(sendThemeToSunburst, d);
        });
      });
    }
  });
  window.addEventListener('message', function(e) {
    if (e.data && e.data.requestTheme) sendThemeToSunburst();
  });
  new MutationObserver(sendThemeToSunburst).observe(
    document.documentElement, { attributes: true, attributeFilter: ['data-bs-theme'] }
  );
})();
</script>

<script>
(function() {
  var iframe = document.getElementById('sunburst-iframe');
  if (!iframe) return;
  function resizeIframe() {
    try {
      var h = iframe.contentDocument.body.scrollHeight;
      iframe.style.height = Math.max(580, h + 20) + 'px';
    } catch(e) {}
  }
  iframe.addEventListener('load', function() {
    resizeIframe();
    // Observer les mutations dans l'iframe pour resize dynamique
    try {
      var mo = new MutationObserver(resizeIframe);
      mo.observe(iframe.contentDocument.body, { childList: true, subtree: true, attributes: true });
    } catch(e) {}
  });
  window.addEventListener('message', function(e) {
    if (e.data && e.data.requestTheme) resizeIframe();
  });
})();
</script>
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
[data-bs-theme="dark"] .q247p-see-ex { color: #E8845A; }
.q247p-caption-line {
  width: 32px;
  height: 1px;
  background: #C2510A;
  opacity: .4;
  margin: 0 auto .75rem;
}
[data-bs-theme="dark"] .q247p-caption-line { background: #E8845A; }
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
  height: 1320px;
  border: none;
  background: transparent;
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

<script>
(function() {
  function sendTheme() {
    var iframe = document.querySelector('.q247p-frame iframe');
    if (!iframe || !iframe.contentWindow) return;
    var dark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
    try { iframe.contentWindow.postMessage({ dark: dark }, '*'); } catch(e) {}
  }
  window.addEventListener('load', function() {
    var iframe = document.querySelector('.q247p-frame iframe');
    if (iframe) {
      iframe.addEventListener('load', function() {
        [100, 400, 800, 1500].forEach(function(d) { setTimeout(sendTheme, d); });
      });
    }
  });
  window.addEventListener('message', function(e) {
    if (e.data && e.data.requestTheme) sendTheme();
    if (e.data && e.data.q247pHeight) {
      var iframe = document.querySelector('.q247p-frame iframe');
      if (iframe) iframe.style.height = (e.data.q247pHeight + 40) + 'px';
    }
  });
  new MutationObserver(sendTheme).observe(
    document.documentElement, { attributes: true, attributeFilter: ['data-bs-theme'] }
  );
})();
</script>
<!-- ── END ACTG2 Q247P SECTION ──────────────────────────────────────── -->