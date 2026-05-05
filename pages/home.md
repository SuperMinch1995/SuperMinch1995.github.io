---
layout: home
permalink: "/"
title: "Minh-Chau Ta, MD"
description: ""
meta_description: "Minh-Chau Ta, MD — Physician-researcher at the interface of pathology, internal medicine, gastroenterology, oncology and dermatology."
meta_title: "Minh-Chau Ta, MD"
subscribe: false

posts:
  heading: "Blog"
  sub_heading: ""
  limit: 3
  sort: date
  view_more_button_text: "Read more"
  view_more_button_link: "/blog"
  columns: 3
---

<style>
.kw {
  color: #C2510A;
  text-decoration: none;
}
.kw:hover {
  text-decoration: underline;
}
.conf-section {
  margin: 2.5rem 0 1.5rem;
  margin-left: 12px;
  font-size: 0.85em;
}
.conf-row {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
}
.conf-photo {
  flex-shrink: 0;
  margin-top: 0;
}
.conf-photo img {
  height: 193px;
  width: auto;
  border-radius: 6px;
  display: block;
}
.conf-panels {
  display: flex;
  gap: 1.5rem;
  align-items: stretch;
}
.pub-fieldset, .conf-fieldset {
  border: 1px dashed #ccc;
  border-radius: 4px;
  padding: 0.6rem 1rem 0.8rem;
  margin: 0;
  box-sizing: border-box;
}
.pub-fieldset {
  flex: 1;
  min-width: 0;
}
.conf-fieldset {
  flex-shrink: 0;
  width: fit-content;
  white-space: nowrap;
}
.conf-legend, .pub-legend {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  padding: 0 0.3rem;
  font-size: 0.78em;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-base-text);
  font-weight: 500;
  background: var(--color-base-bg);
}
.pub-legend a {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.88em;
  font-weight: 500;
  letter-spacing: 0.01em;
  text-transform: none;
  color: var(--color-base-text);
  text-decoration: none;
  opacity: 0.45;
  transition: opacity 0.15s;
}
.pub-legend a:hover {
  opacity: 1;
}
.conf-list, .pub-list {
  list-style: none;
  padding: 0;
  margin: 0.4rem 0 0;
  display: flex;
  flex-direction: column;
  gap: 5.6px;
  font-size: 15.3px;
  line-height: 22.95px;
}
.conf-list li::before, .pub-list li::before {
  content: "— ";
  color: var(--color-base-text);
}
.conf-list a {
  color: #C2510A;
  text-decoration: none;
  font-weight: 500;
}
.conf-list a:hover {
  text-decoration: underline;
}
.conf-list span {
  color: var(--color-base-text);
}
.pub-list li {
  color: var(--color-base-text);
}
.pub-journal {
  color: #C2510A;
  font-weight: 500;
}
.pub-list a {
  color: #C2510A;
  text-decoration: none;
  font-weight: 500;
}
.pub-list a:hover {
  text-decoration: underline;
}
.pub-year {
  color: var(--color-base-text);
}
.sep {
  font-size: 1.2em;
  opacity: 0.4;
  font-weight: 300;
  margin: 0 0.3rem;
  vertical-align: middle;
}
.tagline-row {
  display: flex;
  align-items: center;
  gap: 1.2rem;
  margin: -0.8rem 0 2rem;
}
.badge {
  font-size: 0.72em;
  font-weight: 500;
  letter-spacing: 0.06em;
  color: #C2510A;
  border: 1px solid #C2510A;
  border-radius: 3px;
  padding: 0.2em 0.65em;
  text-transform: uppercase;
}
.pub-card-cta:hover {
  text-decoration: none !important;
  opacity: 0.7;
}
.pub-card-title {
  font-size: 1.1em;
  font-weight: 600;
  color: var(--color-base-text);
  line-height: 1.4;
  margin: 0.4rem 0 0;
}
.home-intro { text-align: center; }
.conf-section { text-align: center; }
.conf-panels { justify-content: center; }
.pub-list, .conf-list { text-align: left; }
.pub-legend, .conf-legend { text-align: left; }

/* ── Contact to collaborate ── */
.contact-wrap {
  max-width: 836px;
  margin: 20px auto 0;
  text-align: left;
}
.contact-inline {
  font-size: 15px;
  font-weight: 600;
  color: #C2510A;
  background: none;
  border: none;
  border-bottom: 1.5px solid #C2510A;
  padding: 0 0 2px 0;
  cursor: pointer;
  font-family: inherit;
  display: inline-block;
  white-space: nowrap;
  transition: opacity 0.15s;
  line-height: 1.2;
}
.contact-inline:hover { opacity: 0.7; }

/* ── Scroll transition ── */
.scroll-transition {
  max-width: 836px;
  margin: 1.8rem auto 28px;  /* negatif = remonte pour aligner avec contact-wrap */
  text-align: left;
  padding-left: 0px;
}
.scroll-transition p {
  font-size: 18px;
  line-height: 1.5;
  color: var(--color-base-text);
  opacity: 0.9;
  font-weight: 400;
  margin: 0;
}
.scroll-transition .arrow {
  font-size: 17px;
  margin-top: 10px;
  color: var(--color-base-text);
  opacity: 0.5;
  animation: float 2.2s ease-in-out infinite;
  display: block;
}
@keyframes float {
  0%, 100% { transform: translateY(0); opacity: 0.5; }
  50% { transform: translateY(6px); opacity: 0.8; }
}

/* ── Latest publication ── */
.pub-section {
  max-width: 836px;
  margin: 18px auto 0;
}
.pub-card {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  text-decoration: none;
  color: inherit;
  align-items: center
}
.pub-pill {
  display: inline-block;
  font-size: 0.68em;
  font-weight: 500;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: #7a3208;
  background: #f5ddd0;
  border-radius: 20px;
  padding: 0.2em 0.7em;
  align-self: flex-start;
}
.pub-image {
  width: 100%;
  height: auto;
  border-radius: 6px;
  display: block;
  margin: 0;
}
.pub-stats {
  display: flex;
  gap: 1.8rem;
  align-items: baseline;
  margin: 14px 0 0 0;
}
.stat-block { display: flex; flex-direction: column; }
.stat-sep {
  width: 0.5px;
  background: var(--color-base-border, #ddd);
  align-self: stretch;
}
.stat-num {
  font-size: 1.6em;
  font-weight: 600;
  color: #C2510A;
  line-height: 1;
}
.stat-label {
  font-size: 0.72em;
  color: var(--color-base-text);
  opacity: 0.45;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-weight: 500;
  margin-top: 2px;
}
.pub-card-desc {
  font-size: 18px;
  color: var(--color-base-text);
  opacity: 0.7;
  line-height: 1.55;
  margin: 20px 0 0 0;
  text-align: center
}
.pub-card-cta {
  font-size: 24px;
  color: #C2510A;
  font-weight: 700;
  border-bottom: 1.5px solid #C2510A;
  margin-top: 14px;
  padding-bottom: 1px;
  align-self: center;
  transition: opacity 0.15s;
}

/* ── Modal ── */
.contact-modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.35);
  z-index: 1000;
  align-items: center;
  justify-content: center;
}
.contact-modal-overlay.open { display: flex; }
.contact-modal {
  background: var(--color-base-bg);
  border-radius: 8px;
  padding: 2rem 2.2rem;
  max-width: 480px;
  width: 90%;
  box-shadow: 0 12px 48px rgba(0,0,0,0.18);
  position: relative;
}
.contact-modal h3 { margin: 0 0 1.2rem; font-size: 1.1em; color: var(--color-base-text); }
.contact-modal label {
  display: block;
  font-size: 0.82em;
  font-weight: 500;
  text-transform: uppercase;
  color: var(--color-base-text);
  opacity: 0.6;
  margin-bottom: 0.3rem;
}
.contact-modal input,
.contact-modal textarea {
  width: 100%;
  box-sizing: border-box;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 0.55rem 0.75rem;
  font-size: 0.93em;
  background: var(--color-base-bg);
  color: var(--color-base-text);
  margin-bottom: 1rem;
  font-family: inherit;
}
.contact-modal input:focus,
.contact-modal textarea:focus { outline: none; border-color: #C2510A; }
.contact-modal textarea { resize: vertical; min-height: 90px; }
.modal-footer { display: flex; justify-content: flex-end; gap: 0.8rem; margin-top: 0.5rem; }
.btn-cancel {
  background: none; border: 1px solid #ccc; border-radius: 4px;
  padding: 0.5em 1.2em; cursor: pointer; font-size: 0.88em;
  color: var(--color-base-text);
}
.btn-submit {
  background: #C2510A; color: #fff; border: none; border-radius: 4px;
  padding: 0.5em 1.4em; cursor: pointer; font-size: 0.88em; font-weight: 600;
}
.modal-close {
  position: absolute; top: 0.9rem; right: 1rem;
  background: none; border: none; font-size: 1.3em;
  cursor: pointer; opacity: 0.4; color: var(--color-base-text);
}
.modal-close:hover { opacity: 1; }
</style>

<div class="tagline-row">
  <a href="/research/" class="badge">Translational Research</a>
</div>

<p>Hi, I'm Minh. I'm based in San Diego, CA.<br>I'm exploring opportunities to join projects with people who value excellence and results.
</p>

<div class="conf-section">
  <div class="conf-row">
    <div class="conf-photo">
      <img src="/assets/images/Pro_linkedin.jpg" alt="Minh-Chau Ta, MD" width="auto" height="193" loading="eager">
    </div>
    <div class="conf-panels">

      <fieldset class="pub-fieldset">
        <legend class="pub-legend">
          Publications
          <a href="https://orcid.org/0009-0001-8503-9574" target="_blank" rel="noopener">
            <svg width="13" height="13" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg"><path d="M128 0C57.3 0 0 57.3 0 128s57.3 128 128 128 128-57.3 128-128S198.7 0 128 0z" fill="#A6CE39"/><path d="M86.3 186.2H70.9V79.1h15.4v107.1zM108.9 79.1h41.6c39.6 0 57 28.3 57 53.6 0 27.5-21.5 53.6-56.8 53.6h-41.8V79.1zm15.4 93.3h24.5c34.9 0 42.9-26.5 42.9-39.7C191.7 111.2 178 93 148 93h-23.7v79.4zM88.7 56.8c0 5.5-4.5 9.9-10 9.9s-10-4.4-10-9.9 4.5-9.9 10-9.9 10 4.4 10 9.9z" fill="#fff"/></svg>
            ORCID
          </a>
          <a href="https://www.ncbi.nlm.nih.gov/myncbi/minh-chau.ta.1/bibliography/public/" target="_blank" rel="noopener">
            <svg width="13" height="13" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" rx="8" fill="#205493"/><text x="50" y="68" font-size="52" font-family="sans-serif" font-weight="bold" fill="white" text-anchor="middle">PM</text></svg>
            PubMed
          </a>
        </legend>
        <ul class="pub-list">
          <li><a href="/publications/cipo-2026/">Am J Gastroenterol</a><span class="sep">·</span><span class="pub-year">2026</span></li>
          <li><a href="/publications/NR1D1-2025/">Genes Chromosomes Cancer</a><span class="sep">·</span><span class="pub-year">2025</span></li>
          <li><a href="/publications/PFMG-2025/">Lancet Reg Health Eur</a><span class="sep">·</span><span class="pub-year">2025</span></li>
          <li><a href="/publications/neurology-2023/">Neurology</a><span class="sep">·</span><span class="pub-year">2023</span></li>
          <li><a href="/publications/SOCS1-2023/">J Clin Immunol</a><span class="sep">·</span><span class="pub-year">2023</span></li>
        </ul>
      </fieldset>

      <fieldset class="conf-fieldset">
        <legend class="conf-legend">Speaker</legend>
        <ul class="conf-list">
          <li><a href="/conferences/ddw-2025/">DDW 2025</a><span class="sep">·</span><span>San Diego, USA</span></li>
          <li><a href="/conferences/espghan-2025/">ESPGHAN 2025</a><span class="sep">·</span><span>Helsinki, Finland</span></li>
          <li><a href="/conferences/ciirta-2025/">CIIRTA 2025</a><span class="sep">·</span><span>Gothenburg, Sweden</span></li>
          <li><a href="/conferences/espen-2025/">ESPEN 2025</a><span class="sep">·</span><span>Prague, Czech Republic</span></li>
          <li><a href="/conferences/eortc-cltg-2025/">EORTC CLTG 2025</a><span class="sep">·</span><span>Athens, Greece</span></li>
        </ul>
      </fieldset>

    </div>
  </div>
</div>

<div class="contact-wrap">
  <button class="contact-inline" onclick="document.getElementById('contactModal').classList.add('open')">Contact to collaborate &rarr;</button>
</div>

<div class="scroll-transition">
  <p>Behind every dataset is a story of patient care and discovery.<br>Explore the work below.</p>
  <span class="arrow">↓</span>
</div>

<!-- Latest publication -->
<div class="pub-section">
  <div class="pub-card">
    <img class="pub-image" src="/assets/images/ACTG2.jpeg" alt="ACTG2 immunohistochemistry panel" loading="lazy" decoding="async">
    <span class="pub-pill">Latest publication</span>
    <p class="pub-card-title">Histogenetic Classification Predicts Outcomes in Chronic Intestinal Pseudo-Obstruction · First author · American Journal of Gastroenterology · 2026</p>
    <div class="pub-stats">
      <div class="stat-block">
        <span class="stat-num">130</span>
        <span class="stat-label">Unsolved Cases</span>
      </div>
      <div class="stat-sep"></div>
      <div class="stat-block">
        <span class="stat-num">82%</span>
        <span class="stat-label">Characterized</span>
      </div>
      <div class="stat-sep"></div>
      <div class="stat-block">
        <span class="stat-num">13</span>
        <span class="stat-label">Genes</span>
      </div>
    </div>
    <p class="pub-card-desc">We found mutations with distinct mechanisms.</p>
    <img src="/assets/images/allvariants.gif"
         alt="All ACTG2 variants — structural overview"
         style="display:block;width:100%;height:auto;border-radius:4px;">
    <p class="pub-card-desc">I modeled this protein in Python.</p>
    <a href="/projects/cipo/" class="pub-card-cta">Interact with it in 3D &rarr;</a>
  </div>
</div>

<!-- Modal -->
<!-- Modal -->
<div class="contact-modal-overlay" id="contactModal">
  <div class="contact-modal">
    <button class="modal-close" onclick="document.getElementById('contactModal').classList.remove('open')">&times;</button>
    <h3>Contact to collaborate</h3>

    <form action="https://formspree.io/f/mvzlapbv" method="POST">
      <label>Name</label>
      <input type="text" name="name" placeholder="">
      <label>Email</label>
      <input type="email" name="email" placeholder="">
      <label>Message</label>
      <textarea name="message" placeholder=""></textarea>
      <div class="modal-footer">
        <button type="button" class="btn-cancel" onclick="document.getElementById('contactModal').classList.remove('open')">Cancel</button>
        <button type="submit" class="btn-submit">Send</button>
      </div>
    </form>

  </div>
</div>

<script>
document.getElementById('contactModal').addEventListener('click', function(e) {
  if (e.target === this) this.classList.remove('open');
});
</script>