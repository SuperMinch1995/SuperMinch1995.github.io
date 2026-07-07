---
layout: post
title: "How does the gut change from fetus to adult?"
subtitle: "A walkthrough of Elmentaite et al., Nature 2021"
date: 2026-05-21
author: Minh-Chau Ta
categories: [literature, single-cell, neurogastroenterology]
tags: [gut-cell-atlas, single-cell-RNA-seq, enteric-nervous-system, IBD]
description: "A cell-by-cell journey through space and time in the developing intestine."
image: "/assets/images/elmentaite-2021/Gut_space_time_hero.webp"
related_posts: true
---

{% comment %}
================================================================================
LIGHTBOX STYLES + JAVASCRIPT (load once)
================================================================================
These should ideally live in _includes/elmentaite-lightbox-assets.html and
be included once at the top of the post. For portability, they are inlined
here. If you put them in an include, replace this whole block with:
{% raw %}{% include elmentaite-lightbox-assets.html %}{% endraw %}
================================================================================
{% endcomment %}

<style>
  /* ── Hero image full-bleed ── */
  .heading-image img {
    width: 100% !important;
    display: block !important;
    height: auto;
  }

  /* ── Figure gallery grid ── */
  .figure-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0 2.5rem 0;
  }
  .figure-gallery-label {
    font-size: 0.75rem;
    color: #888780;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.6rem;
    font-weight: 500;
  }
  .figure-card {
    border: 1px solid #e8e4d8;
    border-radius: 6px;
    overflow: hidden;
    background: #faf9f7;
    cursor: zoom-in;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    font-family: 'DM Sans', system-ui, sans-serif;
  }
  .figure-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(58, 48, 40, 0.12);
  }
  .figure-card img {
    width: 100%;
    height: 140px;
    object-fit: cover;
    object-position: center;
    display: block;
    background: #fff;
  }
  .figure-card-label {
    padding: 0.5rem 0.75rem;
    font-size: 0.78rem;
    color: #3a3028;
    line-height: 1.3;
  }
  .figure-card-label strong {
    display: block;
    font-weight: 600;
    color: #AF3A3A;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 0.15rem;
  }

  /* ── Lightbox overlay ── */
  .lightbox {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(20, 14, 8, 0.92);
    z-index: 9999;
    overflow-y: auto;
    cursor: zoom-out;
    font-family: 'DM Sans', system-ui, sans-serif;
  }
  .lightbox.is-open {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
  }
  .lightbox-content {
    max-width: 1100px;
    width: 100%;
    cursor: default;
    text-align: center;
  }
  .lightbox img {
    max-width: 100%;
    max-height: 75vh;
    height: auto;
    background: #fff;
    border-radius: 4px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
  }
  .lightbox-caption {
    margin-top: 1.25rem;
    color: #faf9f7;
    font-size: 0.95rem;
    line-height: 1.55;
    max-width: 720px;
    margin-left: auto;
    margin-right: auto;
    text-align: left;
  }
  .lightbox-caption strong {
    color: #FFFFFF;
    display: block;
    margin-bottom: 0.3rem;
    font-weight: 600;
  }
  .lightbox-caption .source {
    margin-top: 0.7rem;
    font-size: 0.8rem;
    color: #b5a98e;
    font-style: italic;
  }
  .lightbox-caption .source a {
    color: #d4c7a4;
    text-decoration: underline;
  }
  .lightbox-close {
    position: fixed;
    top: 1rem;
    right: 1.5rem;
    background: none;
    border: none;
    color: #faf9f7;
    font-size: 2rem;
    cursor: pointer;
    line-height: 1;
    padding: 0.5rem;
    border-radius: 50%;
    width: 3rem;
    height: 3rem;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s;
  }
  .lightbox-close:hover {
    background: rgba(255, 255, 255, 0.15);
  }

  /* ── Interactive figure placeholders ── */
  .interactive-figure {
    background: #f5f1e8;
    border: 1px dashed #C2510A;
    border-radius: 8px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
    font-family: 'DM Sans', system-ui, sans-serif;
  }
  .interactive-figure-label {
    display: inline-block;
    background: #AF3A3A;
    color: #FFFFFF;
    padding: 0.2rem 0.6rem;
    border-radius: 3px;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 500;
    margin-bottom: 0.75rem;
  }
  .interactive-figure-title {
    font-size: 1rem;
    font-weight: 500;
    color: #3a3028;
    margin: 0 0 0.4rem 0;
  }
  .interactive-figure-desc {
    font-size: 0.85rem;
    color: #5F5E5A;
    line-height: 1.5;
    max-width: 540px;
    margin: 0 auto;
  }

  /* ── Pull-quote / hero stats ── */
  .stat-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
    padding: 1.5rem 1rem;
    background: linear-gradient(135deg, rgba(27, 112, 146, 0.07), rgba(175, 58, 58, 0.05));
    border-radius: 8px;
    font-family: 'DM Sans', system-ui, sans-serif;
  }
  .stat-item {
    text-align: center;
  }
  .stat-value {
    font-size: 1.6rem;
    font-weight: 500;
    color: #1B7092;
    line-height: 1;
    margin-bottom: 0.3rem;
  }
  .stat-label {
    font-size: 0.78rem;
    color: #5F5E5A;
    line-height: 1.3;
  }

  /* ── Act / Finding dividers ── */
  .act-divider {
    margin: 4rem 0 2rem 0;
    text-align: center;
    position: relative;
  }
  .act-divider::before {
    content: '';
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    border-top: 0.5px solid #e8e4d8;
    z-index: 0;
  }
  .act-divider-label {
    display: inline-block;
    position: relative;
    z-index: 1;
    color: #ffffff;
    background: #3a3028;
    font-family: 'DM Sans', system-ui, sans-serif;
    font-size: 0.84rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    padding: 0.42rem 1.15rem;
    border-radius: 999px;
  }
.pub-reading-badge {
  display: inline-block;
  font-size: 0.72em;
  font-weight: 500;
  letter-spacing: 0.06em;
  color: #1B7092;
  border: 1px solid #1B7092;
  border-radius: 3px;
  padding: 0.2em 0.65em;
  text-transform: uppercase;
  margin-bottom: 1.8rem;
}
</style>

<span class="pub-reading-badge">15 min read</span>

The human gut is a series of distinct compartments: duodenum, jejunum, ileum, colon, rectum. Each segment has a distinct cellular composition that evolves differently from fetal life through adulthood.

In 2021, Elmentaite and colleagues at the Wellcome Sanger Institute published a single-cell atlas of the human intestinal tract, from 6 post-conception weeks to 75 years of age. This page walks through five of their main findings.

<div class="act-divider"><span class="act-divider-label">Finding #1</span></div>

## From structure to immunity

Previous studies profiled fetal, adult, and diseased intestines separately, but no comprehensive atlas existed across space and lifespan.

The authors generated a single-cell atlas of ~428,000 cells from the small intestine, colon, and mesenteric lymph nodes, spanning fetal development to adulthood.

133 cell types and states were identified, revealing dynamic changes in intestinal cellular composition over development.

<div class="stat-row">
  <div class="stat-item">
    <div class="stat-value">~428,000</div>
    <div class="stat-label">single cells profiled</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">5</div>
    <div class="stat-label">anatomical regions (fetus)</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">11</div>
    <div class="stat-label">anatomical regions (adult)</div>
  </div>
  <div class="stat-item">
    <div class="stat-value">133</div>
    <div class="stat-label">cell types and states</div>
  </div>
</div>


During development, early fetal gut is enriched in **mesenchymal** and **neural** cells, while **immune** cells progressively accumulate from the second trimester onward.

{% comment %} ── FIGURE 1 — blueprint ribbon ── {% endcomment %}
<iframe id="fig1b-blueprint-frame"
        src="{{ site.baseurl }}/assets/figures/elmentaite-2021/widget_fig1_blueprint.html"
        title="Figure 1 — Shifting cell composition over development"
        loading="lazy" scrolling="no"
        style="width:100%;border:0;display:block;margin:2rem 0;min-height:560px;"></iframe>
<script>
(function(){
  window.addEventListener('message', function(e){
    if (e.data && e.data.type === 'fig1b-height') {
      var f = document.getElementById('fig1b-blueprint-frame');
      if (f) f.style.height = e.data.height + 'px';
    }
  });
})();
</script>

<div style="background:linear-gradient(135deg,rgba(27,112,146,0.07),rgba(175,58,58,0.05));border:none;border-radius:10px;padding:1.2rem 1.3rem;margin:2rem 0;display:flex;gap:0.9rem;align-items:flex-start;font-family:'DM Sans',system-ui,sans-serif;">
  <div style="flex-shrink:0;width:34px;height:34px;border-radius:50%;background:#1B7092;display:flex;align-items:center;justify-content:center;margin-top:0.1rem;">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.4 1 2.3h6c0-.9.4-1.8 1-2.3A7 7 0 0 0 12 2z"/></svg>
  </div>
  <div>
    <p style="font-size:0.95rem;font-weight:600;text-transform:uppercase;letter-spacing:0.04em;color:#1B7092;margin:0 0 0.4rem 0;">Question</p>
    <p style="font-size:19px;color:#3a3028;line-height:1.6;margin:0;">Which intestinal cell populations emerge, expand, or disappear during human development?</p>
  </div>
</div>



<div class="act-divider"><span class="act-divider-label">Finding #2</span></div>

## BEST4 epithelial cells exhibit region-specific functions

BEST4 enterocytes are a small, recently identified epithelial population found across the entire intestinal tract. The authors showed that these cells are not the same everywhere: BEST4 cells in the small intestine and BEST4 cells in the colon express very different genes.

In the small intestine, BEST4 cells strongly express *CFTR*, the chloride channel mutated in cystic fibrosis. They also express genes involved in lipid metabolism and digestion. Their close proximity to goblet cells suggests a role in mucus production.

In the colon, the same cell type expresses carbonic anhydrases (*CA1*, *CA4*, *CA7*) and aquaporins, pointing to a role in ion and water transport.


{% comment %} ── FIGURE 2 — BEST4 regional signature ── {% endcomment %}
<!--
  Figure 2 — BEST4 regional signature comparator
  Data     : assets/figures/elmentaite-2021/fig4_best4_marker_expression.json
  Gene info : assets/figures/elmentaite-2021/fig4_best4_gene_info.json  (built by build_gene_info.py)

  Click a gene name (left column) to open a MODAL with its MedlinePlus Genetics
  summary: Normal Function, Health Conditions, Other Names, source link.
  Close with the x, a click on the backdrop, or the Escape key.
-->
<style>
#fig4-best4-widget .gene-row{cursor:pointer;}
.g4-overlay{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;padding:1.5rem;background:rgba(40,33,27,0.5);opacity:0;transition:opacity .18s ease;font-family:'DM Sans',system-ui,sans-serif;-webkit-tap-highlight-color:transparent;}
.g4-overlay.open{opacity:1;}
.g4-modal{background:#fff;border:1px solid #e8e4d8;border-radius:10px;width:100%;max-width:560px;max-height:85vh;display:flex;flex-direction:column;overflow:hidden;color:#3a3028;box-shadow:0 14px 44px rgba(40,33,27,0.24);transform:translateY(10px) scale(.985);transition:transform .18s ease;}
.g4-overlay.open .g4-modal{transform:none;}
.g4-head{position:relative;flex:0 0 auto;padding:1.2rem 1.5rem 0.9rem;border-bottom:1px solid #f0ebe0;}
.g4-symbol{font-size:1.2rem;font-weight:500;line-height:1.2;}
.g4-fullname{font-size:0.85rem;color:#5F5E5A;margin-top:0.15rem;}
.g4-region{display:flex;align-items:center;gap:7px;margin-top:0.6rem;font-size:0.8rem;color:#5F5E5A;}
.g4-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
.g4-close{position:absolute;top:0.7rem;right:0.85rem;background:none;border:none;font-size:1.7rem;line-height:1;color:#b8b0a3;cursor:pointer;padding:0 0.2rem;border-radius:6px;}
.g4-close:hover{color:#6b5f52;}
.g4-close:focus-visible{outline:2px solid var(--g4-accent,#8a7f72);outline-offset:2px;}
.g4-body{overflow-y:auto;padding:0.3rem 1.5rem 1.4rem;font-size:0.85rem;line-height:1.62;}
.g4-body p{margin:0 0 0.6rem 0;}
.g4-sec{margin-top:1rem;}
.g4-sec-h{font-size:0.7rem;text-transform:uppercase;letter-spacing:0.07em;color:#a89e8d;font-weight:600;margin-bottom:0.35rem;}
.g4-sec-h a{color:inherit;text-decoration:none;}
.g4-cond{position:relative;padding-left:17px;margin-bottom:0.7rem;}
.g4-cond::before{content:'';position:absolute;left:0;top:6px;width:8px;height:8px;border-radius:50%;background:var(--g4-accent,#8a7f72);}
.g4-cond-name{font-weight:500;color:#3a3028;margin-bottom:0.2rem;}
.g4-chips{display:flex;flex-wrap:wrap;gap:0.35rem;}
.g4-chip{display:inline-block;background:#EEE8E0;color:#5F5E5A;font-size:0.75rem;padding:0.2rem 0.55rem;border-radius:4px;}
.g4-link{display:inline-block;font-size:0.78rem;border:1px solid;border-radius:5px;padding:0.25rem 0.6rem;text-decoration:none;}
.g4-foot{margin-top:1.1rem;padding-top:0.7rem;border-top:1px solid #f0ebe0;font-size:0.72rem;color:#888780;}
@media (max-width:520px){.g4-overlay{padding:0;align-items:flex-end;}.g4-modal{max-width:none;max-height:92vh;border-radius:14px 14px 0 0;}}
@media (prefers-reduced-motion:reduce){.g4-overlay,.g4-modal{transition:none;}}
</style>

<div id="fig4-best4-widget" style="background:#f5f1e8;border:1px solid #e8e4d8;border-radius:8px;padding:1.5rem;margin:2rem 0;font-family:'DM Sans',system-ui,sans-serif;color:#3a3028;">
<div style="display:flex;align-items:baseline;gap:0.6rem;margin-bottom:0.4rem;">
<span style="font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:#888780;">FIGURE 2</span>
</div>
<h4 style="font-size:1.3rem;font-weight:500;margin:0 0 0.3rem 0;">BEST4 enterocytes — small intestine vs colon</h4>
<p style="font-size:1rem;color:#5F5E5A;line-height:1.5;margin:0 0 1rem 0;">Each dot's <strong>size</strong> shows the % of cells expressing the gene; its <strong>opacity</strong> shows mean expression.</p>
<div id="fig4-content" style="min-height:400px;"><p style="text-align:center;color:#888780;padding:3rem 0;">Loading…</p></div>
<p style="font-size:0.72rem;color:#888780;font-style:italic;margin-top:1.5rem;line-height:1.4;">Computed from the epithelium lineage object (4,555 BEST4+ cells: 1,176 small intestine, 3,379 large intestine). Data: Elmentaite et al., <em>Nature</em> 2021, used under CC BY 4.0. Figure &copy; Minh Chau Thom.</p>
</div>

<script>
(function(){
const DATA_URL = '{{ site.baseurl }}/assets/figures/elmentaite-2021/fig4_best4_marker_expression.json';
const INFO_URL = '{{ site.baseurl }}/assets/figures/elmentaite-2021/fig4_best4_gene_info.json';
const SMALL_COLOR='#D8472F', LARGE_COLOR='#1E8FA0', NEUTRAL='#8a7f72', NEUTRAL_BG='#EEE8E0';

const content = document.getElementById('fig4-content');
let GENE_INFO = {};
let GENE_SIDE = {};
let overlay = null;
let lastFocused = null;
let prevOverflow = '';

Promise.all([
  fetch(DATA_URL).then(r=>{ if(!r.ok) throw new Error('JSON not found at '+DATA_URL); return r.json(); }),
  fetch(INFO_URL).then(r=> r.ok ? r.json() : {}).catch(()=>({}))
]).then(([data, info])=>{
  for(const k in info){ if(k!=='_meta') GENE_INFO[k.toUpperCase()] = info[k]; }
  render(data);
}).catch(err=>{
  content.innerHTML='<p style="text-align:center;color:#D8472F;padding:2rem;">Could not load: '+err.message+'</p>';
});

/* ---------------------------------------------------------------- render */
function render(data){
  const genes=Object.keys(data).map(g=>{
    const s=data[g].small_intestine||{mean_expression:0,fraction_expressing:0};
    const l=data[g].large_intestine||{mean_expression:0,fraction_expressing:0};
    return{name:g,small:s,large:l,logRatio:Math.log2((s.mean_expression+0.01)/(l.mean_expression+0.01))};
  });
  genes.sort((a,b)=>b.logRatio-a.logRatio);
  const maxExpr=Math.max(...genes.flatMap(g=>[g.small.mean_expression,g.large.mean_expression]));
  const rowH=26,headerH=50,padding={top:10,left:130,right:30,bottom:30},colW=130;
  const totalH=headerH+genes.length*rowH+padding.top+padding.bottom;
  const totalW=padding.left+2*colW+padding.right;

  // Genes that have Health Conditions get a pulsing halo; the halos light up in
  // sequence (top -> bottom) so the glow appears to travel between them.
  const condCount=genes.filter(g=>{const gi=GENE_INFO[g.name.toUpperCase()];return gi&&gi.conditions&&gi.conditions.length;}).length;
  const PER_GENE=1.8;                 // seconds each gene stays lit (slower = larger)
  const haloDur=Math.max(condCount,1)*PER_GENE;
  let condSeen=0;                     // running index among condition-genes
  let haloCSS='';
  if(condCount>0){
    const slot=100/condCount;         // each gene owns one slot of the cycle
    haloCSS=`
    @keyframes g4HaloPulse{0%{opacity:0;transform:scale(.82);}${(slot*0.5).toFixed(2)}%{opacity:.9;transform:scale(1.18);}${slot.toFixed(2)}%{opacity:0;transform:scale(.82);}100%{opacity:0;transform:scale(.82);}}
    .gene-halo{pointer-events:none;transform-box:fill-box;transform-origin:center;animation:g4HaloPulse ${haloDur.toFixed(1)}s ease-in-out infinite;}
    @media (prefers-reduced-motion:reduce){.gene-halo{animation:none;opacity:.5;transform:none;}}`;
  }

  let svg=`<svg viewBox="0 0 ${totalW} ${totalH}" style="width:100%;max-width:580px;display:block;margin:0 auto;" role="img">`;
  svg+=`<style>
    .gene-row .gene-label{transition:fill .12s;}
    .gene-row .gene-hl{fill:transparent;transition:fill .12s;}
    .gene-row:hover .gene-hl,.gene-row:focus .gene-hl{fill:rgba(58,48,40,0.07);}
    .gene-row:hover .gene-label,.gene-row:focus .gene-label{fill:#1a1410;}
    .gene-row:focus{outline:none;}${haloCSS}
  </style>`;
  svg+=`<defs><filter id="g4halo" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="3.5"/></filter></defs>`;
  svg+=`<rect x="${padding.left}" y="${padding.top}" width="${colW}" height="${headerH-10}" rx="6" fill="${SMALL_COLOR}" opacity="0.1"/>`;
  svg+=`<rect x="${padding.left+colW}" y="${padding.top}" width="${colW}" height="${headerH-10}" rx="6" fill="${LARGE_COLOR}" opacity="0.1"/>`;
  svg+=`<text x="${padding.left+colW/2}" y="${padding.top+18}" text-anchor="middle" font-size="13" font-weight="600" fill="${SMALL_COLOR}">Small intestine</text>`;
  svg+=`<text x="${padding.left+colW/2}" y="${padding.top+33}" text-anchor="middle" font-size="11" fill="${SMALL_COLOR}" opacity="0.8">n = ${genes[0].small.n_cells} cells</text>`;
  svg+=`<text x="${padding.left+colW+colW/2}" y="${padding.top+18}" text-anchor="middle" font-size="13" font-weight="600" fill="${LARGE_COLOR}">Large intestine</text>`;
  svg+=`<text x="${padding.left+colW+colW/2}" y="${padding.top+33}" text-anchor="middle" font-size="11" fill="${LARGE_COLOR}" opacity="0.8">n = ${genes[0].large.n_cells} cells</text>`;

  let _mctx=null;
  try{ _mctx=document.createElement('canvas').getContext('2d'); if(_mctx) _mctx.font="italic 12px 'DM Sans', system-ui, sans-serif"; }catch(e){ _mctx=null; }
  const labelW=s=> _mctx ? _mctx.measureText(s).width : s.length*6.6;

  genes.forEach((g,i)=>{
    const y=padding.top+headerH+i*rowH+rowH/2;
    if(i%2===0)svg+=`<rect x="${padding.left}" y="${y-rowH/2}" width="${2*colW}" height="${rowH}" fill="${NEUTRAL_BG}" opacity="0.4"/>`;

    const side=g.logRatio>1?'small':g.logRatio<-1?'large':'neutral';
    GENE_SIDE[g.name]=side;

    svg+=`<g class="gene-row" data-gene="${g.name}" tabindex="0" role="button" aria-haspopup="dialog" aria-label="Show information for ${g.name}">`;
    svg+=`<rect x="0" y="${y-rowH/2}" width="${padding.left-2}" height="${rowH}" fill="transparent"/>`;
    const _tw=labelW(g.name);
    const _gi=GENE_INFO[g.name.toUpperCase()];
    if(_gi && _gi.conditions && _gi.conditions.length){
      const _haloH=22,_haloPadX=11,_haloW=_tw+2*_haloPadX,_haloX=((padding.left-12)-_tw/2)-_haloW/2;
      svg+=`<rect class="gene-halo" x="${_haloX.toFixed(1)}" y="${(y-_haloH/2).toFixed(1)}" width="${_haloW.toFixed(1)}" height="${_haloH}" rx="${_haloH/2}" fill="rgba(245,200,66,0.7)" filter="url(#g4halo)" style="animation-delay:${(-condSeen*PER_GENE).toFixed(2)}s"/>`;
      condSeen++;
    }
    const _hlH=20,_padX=8,_hlW=_tw+2*_padX,_hlR=(padding.left-8)-_hlW;
    svg+=`<rect class="gene-hl" x="${_hlR.toFixed(1)}" y="${(y-_hlH/2).toFixed(1)}" width="${_hlW.toFixed(1)}" height="${_hlH}" rx="5"/>`;
    svg+=`<text class="gene-label" x="${padding.left-12}" y="${y+4}" text-anchor="end" font-size="13" font-style="italic" fill="#3a3028">${g.name}</text>`;
    svg+=`</g>`;

    const arrow=g.logRatio>1?'\u25C0':g.logRatio<-1?'\u25B6':'\u2022';
    const arrowColor=side==='small'?SMALL_COLOR:side==='large'?LARGE_COLOR:'#cccccc';
    svg+=`<text x="${padding.left+colW}" y="${y+4}" text-anchor="middle" font-size="10" fill="${arrowColor}" opacity="0.5">${arrow}</text>`;

    const sX=padding.left+colW/2;
    const sR=3+g.small.fraction_expressing*10;
    const sOp=0.15+(g.small.mean_expression/maxExpr)*0.85;
    svg+=`<circle cx="${sX}" cy="${y}" r="${sR.toFixed(1)}" fill="${SMALL_COLOR}" opacity="${sOp.toFixed(2)}" style="pointer-events:none;"><title>${g.name} (small): mean ${g.small.mean_expression.toFixed(2)}, ${(g.small.fraction_expressing*100).toFixed(1)}% cells</title></circle>`;
    const lX=padding.left+colW+colW/2;
    const lR=3+g.large.fraction_expressing*10;
    const lOp=0.15+(g.large.mean_expression/maxExpr)*0.85;
    svg+=`<circle cx="${lX}" cy="${y}" r="${lR.toFixed(1)}" fill="${LARGE_COLOR}" opacity="${lOp.toFixed(2)}" style="pointer-events:none;"><title>${g.name} (large): mean ${g.large.mean_expression.toFixed(2)}, ${(g.large.fraction_expressing*100).toFixed(1)}% cells</title></circle>`;
  });
  svg+=`</svg>`;

  const topSmall=genes.slice(0,3).map(g=>g.name).join(', ');
  const topLarge=genes.slice(-3).reverse().map(g=>g.name).join(', ');
  const summary=`<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.2rem;padding:0.8rem 1rem;background:${NEUTRAL_BG};border-radius:6px;font-size:13px;"><div><div style="color:${SMALL_COLOR};font-weight:600;margin-bottom:0.2rem;">Most enriched in small intestine</div><div><em>${topSmall}</em></div><div style="color:#888780;margin-top:0.3rem;font-size:13px;">Lipid metabolism, digestion, chloride transport (CFTR)</div></div><div><div style="color:${LARGE_COLOR};font-weight:600;margin-bottom:0.2rem;">Most enriched in large intestine</div><div><em>${topLarge}</em></div><div style="color:#888780;margin-top:0.3rem;font-size:13px;">Carbonic anhydrases, ion / water transport</div></div></div>`;

  content.innerHTML=svg+summary;
  content.querySelectorAll('.gene-row').forEach(row=>{
    const gene=row.getAttribute('data-gene');
    row.addEventListener('click',()=>openModal(gene));
    row.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); openModal(gene); } });
  });
}

/* ---------------------------------------------------------------- modal */
function openModal(gene){
  if(overlay) destroyOverlay();
  const side=GENE_SIDE[gene]||'neutral';
  const accent=side==='large'?LARGE_COLOR:side==='small'?SMALL_COLOR:NEUTRAL;
  lastFocused=[...content.querySelectorAll('.gene-row')].find(r=>r.dataset.gene===gene)||null;

  overlay=document.createElement('div');
  overlay.className='g4-overlay';
  overlay.style.setProperty('--g4-accent',accent);
  overlay.innerHTML=buildModal(gene,accent);

  document.body.appendChild(overlay);
  prevOverflow=document.body.style.overflow;
  document.body.style.overflow='hidden';

  overlay.querySelectorAll('a[href^="http"]').forEach(a=>{ a.target='_blank'; a.rel='noopener noreferrer'; });
  overlay.addEventListener('click',e=>{ if(e.target===overlay) closeModal(); });
  overlay.querySelector('.g4-close').addEventListener('click',closeModal);
  overlay.addEventListener('keydown',onKeydown);

  requestAnimationFrame(()=>{ if(overlay) overlay.classList.add('open'); });
  const close=overlay.querySelector('.g4-close');
  if(close) close.focus();
}

function onKeydown(e){
  if(e.key==='Escape'){ e.preventDefault(); closeModal(); }
  else if(e.key==='Tab'){ trapFocus(e); }
}

function trapFocus(e){
  if(!overlay) return;
  const f=overlay.querySelectorAll('button,a[href],[tabindex]:not([tabindex="-1"])');
  if(!f.length) return;
  const first=f[0], last=f[f.length-1];
  if(e.shiftKey && document.activeElement===first){ e.preventDefault(); last.focus(); }
  else if(!e.shiftKey && document.activeElement===last){ e.preventDefault(); first.focus(); }
}

function closeModal(){
  if(!overlay) return;
  const o=overlay; overlay=null;
  o.classList.remove('open');
  let done=false;
  const finish=()=>{ if(done) return; done=true; o.remove(); document.body.style.overflow=prevOverflow||''; if(lastFocused&&lastFocused.focus) lastFocused.focus(); };
  o.addEventListener('transitionend',finish);
  setTimeout(finish,260);
}

function destroyOverlay(){ if(overlay){ overlay.remove(); overlay=null; document.body.style.overflow=prevOverflow||''; } }

/* ---------------------------------------------------------------- content */
function esc(s){ return String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

function buildModal(gene,accent){
  const info=GENE_INFO[gene.toUpperCase()];
  const closeBtn=`<button class="g4-close" aria-label="Close panel">&times;</button>`;

  if(!info || info.found===false){
    return `<div class="g4-modal" role="dialog" aria-modal="true" aria-labelledby="g4-modal-title">
      <div class="g4-head">${closeBtn}<div class="g4-symbol" id="g4-modal-title"><em>${esc(gene)}</em></div></div>
      <div class="g4-body">
        <p style="color:#5F5E5A;">A consumer summary for <em>${esc(gene)}</em> isn't available in MedlinePlus Genetics (which covers ~1,475 genes). You can look it up here:</p>
        <div class="g4-chips" style="gap:0.5rem;">
          ${link('MedlinePlus Genetics &#8599;','https://medlineplus.gov/genetics/gene/'+encodeURIComponent(gene.toLowerCase())+'/',accent)}
          ${link('NCBI Gene &#8599;','https://www.ncbi.nlm.nih.gov/gene/?term='+encodeURIComponent(gene)+'%5Bsym%5D+AND+human%5Borgn%5D',accent)}
          ${link('GeneCards &#8599;','https://www.genecards.org/cgi-bin/carddisp.pl?gene='+encodeURIComponent(gene),accent)}
        </div>
      </div>
    </div>`;
  }

  const side=GENE_SIDE[gene]||'neutral';
  const regionLabel=side==='small'?'Enriched in small intestine'
                   :side==='large'?'Enriched in large intestine'
                   :'Comparable in both regions';

  let head=`<div class="g4-head">${closeBtn}
    <div class="g4-symbol" id="g4-modal-title"><em>${esc(info.symbol||gene)}</em> gene</div>
    ${info.full_name?`<div class="g4-fullname">${esc(info.full_name)}</div>`:''}
    <div class="g4-region"><span class="g4-dot" style="background:${accent};"></span><span>${regionLabel}</span></div>
  </div>`;

  let body=`<div class="g4-body">`;

  if(info.function_html){
    body+=section('Normal Function', `<div>${info.function_html}</div>`);
  }
  if(info.conditions && info.conditions.length){
    const isNcbi=info.source==='ncbi';
    const condTitle=isNcbi?'Associated conditions (NCBI MedGen)':'Health Conditions Related to Genetic Changes';
    let inner='';
    info.conditions.forEach(c=>{
      inner+=`<div class="g4-cond">
        <div class="g4-cond-name">${esc(c.name)}</div>
        ${c.html?`<div>${c.html}</div>`:''}
      </div>`;
    });
    body+=section(condTitle, inner);
  }
  if(info.source==='ncbi' && !(info.conditions&&info.conditions.length)){
    body+=section('No disease associations have been reported','');
  }
  if(info.synonyms && info.synonyms.length){
    const chips=info.synonyms.map(s=>`<span class="g4-chip">${esc(s)}</span>`).join('');
    const anchor=info.source==='ncbi' ? (info.url||'') : (info.url||'')+'#synonyms';
    body+=section(`<a href="${esc(anchor)}">Other Names for This Gene</a>`, `<div class="g4-chips">${chips}</div>`);
  }
  body+=`</div>`;

  return `<div class="g4-modal" role="dialog" aria-modal="true" aria-labelledby="g4-modal-title">${head}${body}</div>`;
}

function section(title, inner){
  return `<div class="g4-sec"><div class="g4-sec-h">${title}</div>${inner}</div>`;
}
function link(label, href, accent){
  return `<a class="g4-link" href="${esc(href)}" style="color:${accent};border-color:${accent}55;">${label}</a>`;
}
})();
</script>
<p class="figure-gallery-label">Original figures from the article</p>
<div class="figure-gallery">

  <figure class="figure-card" data-caption-id="cap-1c">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig1c_best4_proportions.png"
         alt="BEST4 cell proportions across intestinal regions" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 1c</strong>
      BEST4 % by region
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-1d">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig1d_best4_histology.png"
         alt="BEST4 immunohistochemistry across gut regions" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 1d</strong>
      BEST4 histology (IHC)
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-1e">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig1e_best4_dotplot.png"
         alt="Regional gene signature of BEST4 enterocytes" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 1e</strong>
      Regional BEST4 markers
    </div>
  </figure>

</div>

<div class="act-divider"><span class="act-divider-label">Finding #3</span></div>

## Tuft cells may be able to sense IgG

Tuft cells are a rare epithelial population usually associated with parasite sensing. One of the surprising findings is that tuft cells express *PLCG2*, a phospholipase normally found in immune cells.

Looking upstream, the authors found that about 3% of tuft cells express *FCGR2A*, a receptor that binds the Fc fragment of IgG antibodies. They confirmed in mice that around 5% of small-intestinal tuft cells carry the equivalent receptor (FCGR3) on their surface. 

Downstream of PLCG2, tuft cells express the signalling molecules needed to convert that signal into a calcium response and an ionic current: *ITPR2*, *PRKCA*, and *TRPM5*.

This potential PLCG2 signaling cascade suggests tuft cells may be functionally equipped for IgG sensing - a role that has not previously been attributed to intestinal epithelium. 

Two missense variants of *PLCG2* have been linked to early-onset inflammatory bowel disease, hinting at a possible clinical relevance.

{% comment %} ── FIGURE 3 — what tuft cells sense (sensory fan) ── {% endcomment %}
<iframe id="tuft-fan-frame"
        src="{{ site.baseurl }}/assets/figures/elmentaite-2021/widget_fig3_tuft_sensory_fan.html"
        title="What a tuft cell listens for"
        loading="lazy" scrolling="no"
        style="width:100%;border:0;display:block;margin:2rem 0;min-height:460px;"></iframe>
<script>
(function(){
  window.addEventListener('message', function(e){
    if (e.data && e.data.type === 'tuft-fan-height') {
      var f = document.getElementById('tuft-fan-frame');
      if (f) f.style.height = e.data.height + 'px';
    }
  });
})();
</script>

The Fc receptors are only the newest input. Placed beside the tuft cell's established chemosensory wiring, the proposed IgG route feeds the *same* downstream machinery — receptor to phospholipase to a shared calcium/TRPM5 hub — rather than a parallel one. Whether the Fc signal genuinely drives *PLCG2* remains open: the canonical taste cascade runs through PLCβ2, and receptor tyrosine kinases usually couple to PLCG1.

{% comment %} ── FIGURE 4 — converging pathways (established vs proposed) ── {% endcomment %}
<iframe id="tuft-converge-frame"
        src="{{ site.baseurl }}/assets/figures/elmentaite-2021/widget_fig4_tuft_pathways.html"
        title="A new wire in a known circuit — converging tuft-cell pathways"
        loading="lazy" scrolling="no"
        style="width:100%;border:0;display:block;margin:2rem 0;min-height:500px;"></iframe>
<script>
(function(){
  window.addEventListener('message', function(e){
    if (e.data && e.data.type === 'tuft-converge-height') {
      var f = document.getElementById('tuft-converge-frame');
      if (f) f.style.height = e.data.height + 'px';
    }
  });
})();
</script>

<p class="figure-gallery-label">Original figures from the article</p>
<div class="figure-gallery">

  <figure class="figure-card" data-caption-id="cap-2f">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig2f_tuft_pathway_dotplot.png"
         alt="FCGR2A and PLCG2 pathway expression in tuft cells" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 2f</strong>
      FCGR2A pathway expression
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-2g">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig2g_flow_cytometry_tuft.png"
         alt="Flow cytometry validation of Fcγ receptors on mouse tuft cells" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 2g</strong>
      Flow cytometry validation
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-2h">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig2h_tuft_pathway_schematic.png"
         alt="Schematic of tuft cell IgG sensing pathway" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 2h</strong>
      Tuft signalling schematic
    </div>
  </figure>

</div>

<div class="act-divider"><span class="act-divider-label">Finding #4</span></div>

## Building the enteric nervous system

The enteric nervous system develops from enteric neural crest cells (ENCC), which the authors detected in the gut as early as 6.5 post-conception weeks. From this progenitor pool, two main neuronal lineages emerge, defined by expression of *ETV1* (branch A) and *BNC2* (branch B), alongside three glial subtypes.

Branch A gives rise to inhibitory motor neurons and a subset of intrinsic primary afferent neurons / interneurons. Branch B gives rise to excitatory motor neurons and a second IPAN subtype. Both branches mature over the second trimester, while glial cells become more abundant later in development.

{% comment %} ── FIGURE 5 — ENS lineage river ── {% endcomment %}
<!--
  Figure 5 — ENS lineage river (landing medallions)
  © Minh Chau Thom — original representation
  Data: assets/figures/elmentaite-2021/fig1_ens_cell_counts.json
-->
<div id="fig1-ens-widget" style="background:#f5f1e8;border:1px solid #e8e4d8;border-radius:8px;padding:1.5rem;margin:2rem 0;font-family:'DM Sans',system-ui,sans-serif;color:#3a3028;">

<div style="margin-bottom:0.35rem;">
  <span style="font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:#888780;">FIGURE 5</span>
</div>
<h4 style="font-size:1.5rem;font-weight:600;margin:0 0 0.35rem 0;color:#3a3028;">One origin, two fates — the enteric nervous system</h4>
<p style="font-size:16px;color:#5F5E5A;line-height:1.55;margin:0 0 1rem 0;">A single ENCC progenitor flows into inhibitory (branch A) and excitatory (branch B) neurons, plus the glial lineage. Ribbon width tracks cell count — switch developmental stage to watch the river re-flow as glia become enriched.</p>

<div style="display:flex;gap:0.5rem;margin-bottom:1rem;flex-wrap:wrap;">
<button onclick="fig1Filter('all')" id="fig1-btn-all" style="padding:5px 12px;border-radius:4px;border:1px solid #e8e4d8;background:#3a3028;color:#f5f1e8;font-size:13px;cursor:pointer;font-family:inherit;">All stages</button>
<button onclick="fig1Filter('W6-11')" id="fig1-btn-W6-11" style="padding:5px 12px;border-radius:4px;border:1px solid #e8e4d8;background:transparent;color:#3a3028;font-size:13px;cursor:pointer;font-family:inherit;">6–11 PCW</button>
<button onclick="fig1Filter('W12-17')" id="fig1-btn-W12-17" style="padding:5px 12px;border-radius:4px;border:1px solid #e8e4d8;background:transparent;color:#3a3028;font-size:13px;cursor:pointer;font-family:inherit;">12–17 PCW</button>
</div>

<div id="fig1-content" style="min-height:420px;"><p style="text-align:center;color:#888780;padding:3rem 0;">Loading…</p></div>
<p id="fig1-caption" style="font-size:14px;color:#5F5E5A;text-align:center;line-height:1.55;margin:0.4rem 0 0 0;">&nbsp;</p>

<p style="font-size:13px;color:#888780;font-style:italic;margin-top:1.2rem;line-height:1.6;border-top:1px solid #ddd6cc;padding-top:0.75rem;margin-bottom:0.6rem;">Ribbon width and medallion size &prop; cell count. Computed from the ENS lineage object (16,870 fetal enteric neural cells, 6–17 PCW). Data: Elmentaite <em>et al.</em>, <em>Nature</em> 597, 250–255 (2021), used under CC BY 4.0. Figure &copy; Minh Chau Thom.</p>
</div>

<script>
let fig1Data = null;
let fig1Stage = 'all';

(function(){
  const DATA_URL = '{{ site.baseurl }}/assets/figures/elmentaite-2021/fig1_ens_cell_counts.json';

  const GROUPS = {
    progenitor: ['ENCC/glia Progenitor','cycling ENCC/glia'],
    neuroblast: ['Neuroblast','cycling neuroblast'],
    branchA:    ['Branch A1 (iMN)','Branch A2 (IPAN/IN)','Branch A3 (IPAN/IN)','Branch A4 (IN)'],
    branchB:    ['Branch B1 (eMN)','Branch B2 (eMN)','Branch B3 (IPAN)'],
    glia:       ['Glia 1 (DHH+)','Glia 2 (ELN+)','Glia 3 (BCAN+)','Differentiating glia']
  };
  const STAGE_LABELS = {
    'all':    'all stages · 6–17 PCW',
    'W6-11':  '6–11 PCW · first trimester',
    'W12-17': '12–17 PCW · second trimester'
  };

  let gMaxFlow = 1, gMaxDest = 1;

  function flow(group, st){
    let t = 0;
    GROUPS[group].forEach(function(ct){
      const node = fig1Data[ct];
      if(!node) return;
      for(const s in node){
        if(st !== 'all' && s !== st) continue;
        for(const r in node[s]) t += node[s][r];
      }
    });
    return t;
  }
  function neuronal(st){ return flow('neuroblast',st) + flow('branchA',st) + flow('branchB',st); }

  function widthFor(c){ return Math.max(8, (c / gMaxFlow) * 56); }
  function radiusFor(c){ return 20 + (c / gMaxDest) * 14; }
  function fmt(n){ return Math.round(n).toLocaleString('en-US'); }

  function computeGlobals(){
    const flows = [], dests = [];
    ['all','W6-11','W12-17'].forEach(function(st){
      flows.push(neuronal(st), flow('branchA',st), flow('branchB',st), flow('glia',st));
      dests.push(flow('branchA',st), flow('branchB',st), flow('glia',st));
    });
    gMaxFlow = Math.max.apply(null, flows.concat([1]));
    gMaxDest = Math.max.apply(null, dests.concat([1]));
  }

  function el(id){ return document.getElementById(id); }
  function setAttr(id, attr, val){ const e = el(id); if(e) e.setAttribute(attr, val); }
  function setText(id, t){ const e = el(id); if(e) e.textContent = t; }

  function skeleton(){
    const rib = 'fill:none;stroke-linecap:round;transition:stroke-width .55s cubic-bezier(.4,0,.2,1);';
    const med = 'transition:r .55s cubic-bezier(.4,0,.2,1);';
    return ''
    + '<svg width="100%" viewBox="0 0 680 510" role="img" style="max-width:640px;display:block;margin:0 auto;overflow:visible;" xmlns="http://www.w3.org/2000/svg">'
    + '<title>Enteric nervous system differentiation as a lineage river</title>'
    + '<desc>A single ENCC progenitor splits into branch A inhibitory neurons, branch B excitatory neurons, and glia. Ribbon width and medallion size are proportional to cell count.</desc>'

    + '<path id="fig1-r-g"     d="M340,128 C430,170 510,255 540,330 C552,370 552,408 549,430" style="' + rib + '" stroke="#3DAEA3" stroke-width="2" opacity="0.80"><title id="fig1-tt-g"></title></path>'
    + '<path id="fig1-r-trunk" d="M340,122 C320,165 290,205 270,240" style="' + rib + '" stroke="#534AB7" stroke-width="2" opacity="0.22"><title id="fig1-tt-n"></title></path>'
    + '<path id="fig1-r-a"     d="M270,248 C220,330 175,388 142,428" style="' + rib + '" stroke="#AF3A3A" stroke-width="2" opacity="0.82"><title id="fig1-tt-a"></title></path>'
    + '<path id="fig1-r-b"     d="M270,248 C300,330 332,390 347,428" style="' + rib + '" stroke="#C2510A" stroke-width="2" opacity="0.82"><title id="fig1-tt-b"></title></path>'

    + '<circle cx="340" cy="118" r="22" fill="#3a3028"/>'
    + '<text x="340" y="122" text-anchor="middle" font-size="11" fill="#f5f1e8" font-weight="600">ENCC</text>'
    + '<text x="370" y="114" font-size="13" fill="#3a3028" font-weight="600">ENCC / glia progenitor</text>'
    + '<text x="370" y="131" font-size="12" fill="#888780">proliferates · keeps reserve</text>'

    + '<circle cx="270" cy="245" r="16" fill="#534AB7"/>'
    + '<text x="270" y="249" text-anchor="middle" font-size="11" fill="#f5f1e8" font-weight="600">NB</text>'
    + '<text x="270" y="219" text-anchor="middle" font-size="12" fill="#534AB7" font-weight="600">Neuroblast</text>'

    + '<circle id="fig1-m-a" cx="142" cy="432" r="20" fill="#AF3A3A" style="' + med + '"/>'
    + '<text x="142" y="427" text-anchor="middle" font-size="15" fill="#FFFFFF" font-weight="600">A</text>'
    + '<text id="fig1-c-a" x="142" y="444" text-anchor="middle" font-size="12" fill="#FFFFFF" opacity="0.92"></text>'
    + '<text x="142" y="481" text-anchor="middle" font-size="15" fill="#AF3A3A" font-weight="600">Inhibitory motor neurons</text>'
    + '<text x="142" y="498" text-anchor="middle" font-size="12" fill="#888780">ETV1⁺ · IPAN / interneurons · A1–A4</text>'

    + '<circle id="fig1-m-b" cx="347" cy="432" r="20" fill="#C2510A" style="' + med + '"/>'
    + '<text x="347" y="427" text-anchor="middle" font-size="15" fill="#FFFFFF" font-weight="600">B</text>'
    + '<text id="fig1-c-b" x="347" y="444" text-anchor="middle" font-size="12" fill="#FFFFFF" opacity="0.92"></text>'
    + '<text x="347" y="481" text-anchor="middle" font-size="15" fill="#C2510A" font-weight="600">Excitatory motor neurons</text>'
    + '<text x="347" y="498" text-anchor="middle" font-size="12" fill="#888780">BNC2⁺ · + late IPAN · B1–B3</text>'

    + '<circle id="fig1-m-g" cx="549" cy="432" r="20" fill="#3DAEA3" style="' + med + '"/>'
    + '<text x="549" y="427" text-anchor="middle" font-size="15" fill="#FFFFFF" font-weight="600">G</text>'
    + '<text id="fig1-c-g" x="549" y="444" text-anchor="middle" font-size="12" fill="#FFFFFF" opacity="0.92"></text>'
    + '<text x="549" y="481" text-anchor="middle" font-size="15" fill="#2C8C82" font-weight="600">Glial support &amp; niche</text>'
    + '<text x="549" y="498" text-anchor="middle" font-size="12" fill="#888780">DHH⁺ · ELN⁺ · BCAN⁺</text>'

    + '</svg>';
  }

  function updateRiver(){
    const nA = flow('branchA', fig1Stage),
          nB = flow('branchB', fig1Stage),
          nG = flow('glia', fig1Stage),
          nN = neuronal(fig1Stage),
          nP = flow('progenitor', fig1Stage);

    setAttr('fig1-r-trunk', 'stroke-width', widthFor(nN));
    setAttr('fig1-r-a',     'stroke-width', widthFor(nA));
    setAttr('fig1-r-b',     'stroke-width', widthFor(nB));
    setAttr('fig1-r-g',     'stroke-width', widthFor(nG));

    setAttr('fig1-m-a', 'r', radiusFor(nA));
    setAttr('fig1-m-b', 'r', radiusFor(nB));
    setAttr('fig1-m-g', 'r', radiusFor(nG));

    setText('fig1-c-a', fmt(nA));
    setText('fig1-c-b', fmt(nB));
    setText('fig1-c-g', fmt(nG));

    setText('fig1-tt-a', 'Branch A · ' + fmt(nA) + ' cells');
    setText('fig1-tt-b', 'Branch B · ' + fmt(nB) + ' cells');
    setText('fig1-tt-g', 'Glia · ' + fmt(nG) + ' cells');
    setText('fig1-tt-n', 'Neuronal stream · ' + fmt(nN) + ' cells');

    const total = nP + nN + nG;
    setText('fig1-caption', 'Showing ' + fmt(total) + ' cells · ' + STAGE_LABELS[fig1Stage]);
  }

  window.fig1Filter = function(st){
    fig1Stage = st;
    ['all','W6-11','W12-17'].forEach(function(s){
      const b = document.getElementById('fig1-btn-' + s);
      if(!b) return;
      if(s === st){ b.style.background = '#3a3028'; b.style.color = '#f5f1e8'; }
      else { b.style.background = 'transparent'; b.style.color = '#3a3028'; }
    });
    if(fig1Data) updateRiver();
  };

  fetch(DATA_URL)
    .then(function(r){ if(!r.ok) throw new Error('JSON not found'); return r.json(); })
    .then(function(d){
      fig1Data = d;
      computeGlobals();
      document.getElementById('fig1-content').innerHTML = skeleton();
      requestAnimationFrame(updateRiver);
    })
    .catch(function(e){
      document.getElementById('fig1-content').innerHTML =
        '<p style="text-align:center;color:#AF3A3A;padding:2rem;">Could not load: ' + e.message + '</p>';
    });
})();
</script>
The same dataset makes it possible to ask which cell types express genes linked to Hirschsprung disease, a congenital disorder where enteric neurons fail to colonise part of the bowel. The authors found that HSCR-associated genes are expressed across many cell types, but with clear differences. *RET*, for example, is strongly expressed by branch A neurons but not branch B. *ZEB2* and *EDNRB* are higher in colonic glia and neuroblasts than in their small-intestinal counterparts.

{% comment %} ── FIGURE 6 — HSCR gene spotlight ── {% endcomment %}
<!--
  Figure 6 — HSCR gene spotlight (bipartite arcs)
  © Minh Chau Thom — original representation
  Data: assets/figures/elmentaite-2021/fig2_hscr_expression.json
-->
<div id="fig2-hscr-widget" style="background:#f5f1e8;border:1px solid #e8e4d8;border-radius:8px;padding:1.5rem;margin:2rem 0;font-family:'DM Sans',system-ui,sans-serif;color:#3a3028;">

<div style="margin-bottom:0.35rem;">
  <span style="font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:#888780;">FIGURE 6</span>
</div>
<h4 style="font-size:1.5rem;font-weight:600;margin:0 0 0.35rem 0;color:#3a3028;">Two signatures, two territories — Hirschsprung genes</h4>
<p style="font-size:16px;color:#5F5E5A;line-height:1.55;margin:0 0 1rem 0;">Arcs link each HSCR-associated gene to the cell groups where it is expressed; thickness tracks mean expression. <em>RET</em> lights up branch A neurons, while <em>ZEB2</em> and <em>EDNRB</em> light up colonic glia. Hover any gene or cell group to spotlight its connections.</p>

<div id="fig2-content" style="min-height:380px;overflow-x:auto;"><p style="text-align:center;color:#888780;padding:3rem 0;">Loading…</p></div>

<p style="font-size:13px;color:#888780;font-style:italic;margin-top:1.2rem;line-height:1.6;border-top:1px solid #ddd6cc;padding-top:0.75rem;margin-bottom:0.6rem;">Arc width &prop; mean log-normalised expression, n-cell weighted across stages; colonic and small-intestinal glia are shown separately. Data: Elmentaite <em>et al.</em>, <em>Nature</em> 597, 250–255 (2021), used under CC BY 4.0. Figure &copy; Minh Chau Thom.</p>
</div>

<script>
let fig2Data = null;

(function(){
  const DATA_URL = '{{ site.baseurl }}/assets/figures/elmentaite-2021/fig2_hscr_expression.json';

  const GLIA = ['Glia 1 (DHH+)','Glia 2 (ELN+)','Glia 3 (BCAN+)','Differentiating glia'];
  const NODES = [
    { id:'NB', label:'Neuroblast',     x:108, hue:'#534AB7', cells:['Neuroblast','cycling neuroblast'], region:null },
    { id:'A',  label:'Branch A',        x:229, hue:'#AF3A3A', cells:['Branch A1 (iMN)','Branch A2 (IPAN/IN)','Branch A3 (IPAN/IN)','Branch A4 (IN)'], region:null },
    { id:'B',  label:'Branch B',        x:350, hue:'#C2510A', cells:['Branch B1 (eMN)','Branch B2 (eMN)','Branch B3 (IPAN)'], region:null },
    { id:'GC', label:'Colonic glia',    x:471, hue:'#2C8C82', cells:GLIA, region:'LargeInt' },
    { id:'GS', label:'Small-int. glia', x:592, hue:'#4FA89E', cells:GLIA, region:'SmallInt' }
  ];
  const STORY = { 'RET|A':1, 'ZEB2|GC':1, 'EDNRB|GC':1 };

  function expr(gene, node){
    const obj = fig2Data[gene];
    if(!obj) return 0;
    let num = 0, den = 0;
    for(const key in obj){
      const parts = key.split('__');
      const cell = parts[0], region = parts[1];
      if(node.cells.indexOf(cell) === -1) continue;
      if(node.region && region !== node.region) continue;
      const e = obj[key];
      num += e.mean_expression * e.n_cells;
      den += e.n_cells;
    }
    return den > 0 ? num / den : 0;
  }

  let arcEls = null;

  function reset(){
    if(!arcEls) return;
    arcEls.forEach(function(a){
      if(a.dataset.story === '1'){
        a.setAttribute('stroke', a.dataset.hue);
        a.setAttribute('opacity', '0.9');
        a.setAttribute('stroke-width', (4 + parseFloat(a.dataset.norm) * 4).toFixed(1));
      } else {
        a.setAttribute('stroke', '#b9b3a6');
        a.setAttribute('opacity', '0.16');
        a.setAttribute('stroke-width', '1.3');
      }
    });
  }
  function highlight(pred){
    arcEls.forEach(function(a){
      if(pred(a)){
        a.setAttribute('stroke', a.dataset.hue);
        a.setAttribute('opacity', '0.92');
        a.setAttribute('stroke-width', (2.5 + parseFloat(a.dataset.norm) * 5).toFixed(1));
      } else {
        a.setAttribute('stroke', '#b9b3a6');
        a.setAttribute('opacity', '0.05');
        a.setAttribute('stroke-width', '1');
      }
    });
  }

  function build(){
    const genes = Object.keys(fig2Data);
    const N = genes.length;
    const xL = 68, xR = 612;
    const gx = function(i){ return N > 1 ? xL + i * (xR - xL) / (N - 1) : 340; };

    const arcs = [];
    genes.forEach(function(g, i){
      const es = NODES.map(function(n){ return expr(g, n); });
      const geneMax = Math.max.apply(null, es.concat([0])) || 1;
      NODES.forEach(function(n, ni){
        const norm = es[ni] / geneMax;
        const story = STORY[g + '|' + n.id] ? 1 : 0;
        if(story || norm >= 0.35){
          arcs.push({ gene:g, node:n.id, x1:gx(i), x2:n.x, hue:n.hue, norm:norm, story:story });
        }
      });
    });

    const aStyle = 'transition:stroke-width .25s ease, opacity .25s ease;';
    let s = '<svg width="100%" viewBox="0 0 680 470" role="img" style="max-width:640px;min-width:560px;display:block;margin:0 auto;overflow:visible;" xmlns="http://www.w3.org/2000/svg">'
      + '<title>Hirschsprung-associated genes connected to enteric neural cell groups</title>'
      + '<desc>RET connects strongly to branch A neurons; ZEB2 and EDNRB connect strongly to colonic glia; other connections are faint until hovered.</desc>';

    arcs.forEach(function(a){
      s += '<path class="fig2-arc" data-gene="' + a.gene + '" data-node="' + a.node + '" data-norm="'
        + a.norm.toFixed(3) + '" data-hue="' + a.hue + '" data-story="' + a.story
        + '" d="M' + a.x1.toFixed(1) + ',124 C' + a.x1.toFixed(1) + ',215 ' + a.x2 + ',255 ' + a.x2
        + ',332" fill="none" stroke-linecap="round" style="' + aStyle + '"></path>';
    });

    s += '<text x="70" y="249" font-size="13" font-weight="600" fill="#AF3A3A">RET ↑↑</text>'
      + '<text x="70" y="265" font-size="12" fill="#AF3A3A">branch A neurons</text>'
      + '<text x="612" y="249" text-anchor="end" font-size="13" font-weight="600" fill="#2C8C82">ZEB2 · EDNRB ↑↑</text>'
      + '<text x="612" y="265" text-anchor="end" font-size="12" fill="#2C8C82">colonic glia</text>';

    genes.forEach(function(g, i){
      const x = gx(i), ly = (i % 2 === 0) ? 96 : 110;
      s += '<g class="fig2-gene" data-gene="' + g + '" style="cursor:pointer;">'
        + '<text x="' + x.toFixed(1) + '" y="' + ly + '" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#3a3028">' + g + '</text>'
        + '<circle cx="' + x.toFixed(1) + '" cy="120" r="3.4" fill="#3a3028"/></g>';
    });

    NODES.forEach(function(n){
      s += '<g class="fig2-node" data-node="' + n.id + '" style="cursor:pointer;">'
        + '<rect x="' + (n.x - 49) + '" y="334" width="98" height="32" rx="16" fill="#FFFFFF" stroke="' + n.hue + '"/>'
        + '<text x="' + n.x + '" y="354" text-anchor="middle" font-size="12" font-weight="600" fill="' + n.hue + '">' + n.label + '</text></g>';
    });

    s += '</svg>';

    const container = document.getElementById('fig2-content');
    container.innerHTML = s;
    arcEls = container.querySelectorAll('.fig2-arc');

    container.querySelectorAll('.fig2-gene').forEach(function(el){
      el.addEventListener('mouseenter', function(){ highlight(function(a){ return a.dataset.gene === el.dataset.gene; }); });
      el.addEventListener('mouseleave', reset);
    });
    container.querySelectorAll('.fig2-node').forEach(function(el){
      el.addEventListener('mouseenter', function(){ highlight(function(a){ return a.dataset.node === el.dataset.node; }); });
      el.addEventListener('mouseleave', reset);
    });
    reset();
  }

  fetch(DATA_URL)
    .then(function(r){ if(!r.ok) throw new Error('JSON not found'); return r.json(); })
    .then(function(d){ fig2Data = d; build(); })
    .catch(function(e){
      document.getElementById('fig2-content').innerHTML =
        '<p style="text-align:center;color:#AF3A3A;padding:2rem;">Could not load: ' + e.message + '</p>';
    });
})();
</script>
<p class="figure-gallery-label">Original figures from the article</p>
<div class="figure-gallery">

  <figure class="figure-card" data-caption-id="cap-3a">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig3a_umap_ens_early.png"
         alt="UMAP of enteric neurons at 6-11 PCW" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 3a</strong>
      ENS at 6–11 PCW
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-3b">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig3b_umap_ens_late.png"
         alt="UMAP of enteric neurons at 12-17 PCW" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 3b</strong>
      ENS at 12–17 PCW
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-3c">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig3c_smfish_neurons.png"
         alt="smFISH of SCGN, BNC2, GRP enteric neurons" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 3c</strong>
      smFISH — branch A/B neurons
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-3d">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig3d_smfish_glia.png"
         alt="smFISH of DHH-expressing glia" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 3d</strong>
      smFISH — DHH glia
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-3e">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig3e_hscr_heatmap.png"
         alt="HSCR-associated gene expression across neural cells" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 3e</strong>
      HSCR gene expression
    </div>
  </figure>

</div>

<div class="act-divider"><span class="act-divider-label">Finding #5</span></div>

## Lymphoid organs in the making — and in disease

Mesenteric lymph nodes start to appear around 12 post-conception weeks in this dataset. Their formation depends on three cell populations working together: lymphoid tissue inducer cells (LTi), mesenchymal lymphoid tissue organisers (mLTo), and endothelial lymphoid tissue organisers (a subset of lymphatic endothelial cells the authors call LEC2, marked by *MADCAM1*).

The authors found that innate lymphoid cell progenitors (ILCPs) are the earliest LTi-like cells in the developing gut, and that they give rise to NCR+ and NCR− ILC3 subsets. The mLTo cells they identified express the chemokines *CCL19*, *CCL21* and *CXCL13* — the same signals known to attract naive lymphocytes into developing lymph nodes.

{% comment %} ── FIGURE 7 — lymphoid composition stream ── {% endcomment %}
<!--
  Figure 7 — Lymphoid organogenesis composition stream (normalised to 100% per stage)
  © Minh Chau Thom — original representation
  Data: assets/figures/elmentaite-2021/fig6_lymphoid_timeline.json
-->
<div id="fig6-lymphoid-widget" style="background:#f5f1e8;border:1px solid #e8e4d8;border-radius:8px;padding:1.5rem;margin:2rem 0;font-family:'DM Sans',system-ui,sans-serif;color:#3a3028;">

<div style="margin-bottom:0.35rem;">
  <span style="font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:#888780;">FIGURE 7</span>
</div>
<h4 style="font-size:1.5rem;font-weight:600;margin:0 0 0.35rem 0;color:#3a3028;">Building a lymphoid organ — composition over time</h4>
<p style="font-size:16px;color:#5F5E5A;line-height:1.55;margin:0 0 1rem 0;">Composition of the gut T / innate lymphoid compartment across development, normalised so each stage sums to 100%. The innate LTi-like pioneers (magenta + red) appear only in the fetus — seeding lymphoid tissue before disappearing — while the adaptive T compartment (teal) comes to dominate. Hover a lineage for its share and count at each stage.</p>

<div id="fig6-content" style="min-height:360px;"><p style="text-align:center;color:#888780;padding:3rem 0;">Loading…</p></div>
<p id="fig6-caption" style="font-size:14px;color:#5F5E5A;text-align:center;line-height:1.55;margin:0.4rem 0 0 0;">Innate pioneers (ILCP, LTi-like ILC3) seed lymphoid tissue in the fetus, then vanish; the adaptive T compartment dominates from childhood on.</p>

<p style="font-size:13px;color:#888780;font-style:italic;margin-top:1.2rem;line-height:1.6;border-top:1px solid #ddd6cc;padding-top:0.75rem;margin-bottom:0.6rem;">Bands show composition (% of cells per stage), normalised so every stage totals 100% — removing the fetal over-sampling that skews raw counts. Computed from the T/innate lineage object (38,633 cells, fetal to adult). Data: Elmentaite <em>et al.</em>, <em>Nature</em> 597, 250–255 (2021), used under CC BY 4.0. Figure &copy; Minh Chau Thom.</p>
</div>

<script>
let fig6Data = null;

(function(){
  const DATA_URL = '{{ site.baseurl }}/assets/figures/elmentaite-2021/fig6_lymphoid_timeline.json';

  const STAGES = [
    { key:'Second trim',   label:'2nd trim.' },
    { key:'Pediatric',     label:'Paediatric' },
    { key:'Pediatric_IBD', label:'Paed. IBD' },
    { key:'Adult',         label:'Adult' }
  ];
  const BANDS = [
    { id:'ILCP', label:'ILCP',          color:'#D449AA', cells:['ILCP'] },
    { id:'LTI',  label:'LTi-like ILC3', color:'#AF3A3A', cells:['LTi-like NCR+ ILC3','LTi-like NCR- ILC3'] },
    { id:'ILC3', label:'ILC3',          color:'#C2510A', cells:['ILC3'] },
    { id:'NK',   label:'NK',            color:'#534AB7', cells:['NK cell'] },
    { id:'T',    label:'Lymphocytes T', color:'#3DAEA3', cells:['SELL+ CD4 T','SELL+ CD8 T','Treg','fetal T cell'] }
  ];
  const X  = [85, 270, 455, 610];
  const MX = [177.5, 362.5, 532.5];
  const Y_TOP = 30, H = 246;
  const DEFAULT_CAP = 'Innate pioneers (ILCP, LTi-like ILC3) seed lymphoid tissue in the fetus, then vanish; the adaptive T compartment dominates from childhood on.';

  function count(band, sKey){
    let t = 0;
    band.cells.forEach(function(c){
      const node = fig6Data[c];
      if(!node || !node[sKey]) return;
      for(const r in node[sKey]) t += node[sKey][r];
    });
    return t;
  }
  function fmt(n){ return Math.round(n).toLocaleString('en-US'); }
  function r1(n){ return n.toFixed(1); }

  let bandEls = null;

  function setBands(activeBi){
    if(!bandEls) return;
    bandEls.forEach(function(el){
      const bi = parseInt(el.dataset.bi, 10);
      if(activeBi === null) el.setAttribute('opacity', '0.9');
      else el.setAttribute('opacity', bi === activeBi ? '0.98' : '0.28');
    });
  }

  function build(){
    const counts = BANDS.map(function(b){ return STAGES.map(function(s){ return count(b, s.key); }); });
    const totals = STAGES.map(function(s, si){ return BANDS.reduce(function(a, _, bi){ return a + counts[bi][si]; }, 0); });
    const frac = BANDS.map(function(b, bi){ return STAGES.map(function(s, si){ return totals[si] > 0 ? counts[bi][si] / totals[si] : 0; }); });

    const edges = BANDS.map(function(){ return { top:[], bot:[] }; });
    STAGES.forEach(function(s, si){
      let cum = 0;
      BANDS.forEach(function(b, bi){
        const f = frac[bi][si];
        edges[bi].top[si] = Y_TOP + cum * H;
        edges[bi].bot[si] = Y_TOP + (cum + f) * H;
        cum += f;
      });
    });

    function bandPath(bi){
      const t = edges[bi].top, b = edges[bi].bot;
      return 'M' + r1(X[0]) + ',' + r1(t[0])
        + ' C' + r1(MX[0]) + ',' + r1(t[0]) + ' ' + r1(MX[0]) + ',' + r1(t[1]) + ' ' + r1(X[1]) + ',' + r1(t[1])
        + ' C' + r1(MX[1]) + ',' + r1(t[1]) + ' ' + r1(MX[1]) + ',' + r1(t[2]) + ' ' + r1(X[2]) + ',' + r1(t[2])
        + ' C' + r1(MX[2]) + ',' + r1(t[2]) + ' ' + r1(MX[2]) + ',' + r1(t[3]) + ' ' + r1(X[3]) + ',' + r1(t[3])
        + ' L' + r1(X[3]) + ',' + r1(b[3])
        + ' C' + r1(MX[2]) + ',' + r1(b[3]) + ' ' + r1(MX[2]) + ',' + r1(b[2]) + ' ' + r1(X[2]) + ',' + r1(b[2])
        + ' C' + r1(MX[1]) + ',' + r1(b[2]) + ' ' + r1(MX[1]) + ',' + r1(b[1]) + ' ' + r1(X[1]) + ',' + r1(b[1])
        + ' C' + r1(MX[0]) + ',' + r1(b[1]) + ' ' + r1(MX[0]) + ',' + r1(b[0]) + ' ' + r1(X[0]) + ',' + r1(b[0]) + ' Z';
    }

    const ltiMid0 = (edges[1].top[0] + edges[1].bot[0]) / 2;
    const tMid3   = (edges[4].top[3] + edges[4].bot[3]) / 2;

    let s = '<svg width="100%" viewBox="0 0 680 352" role="img" style="max-width:680px;display:block;margin:0 auto;overflow:visible;" xmlns="http://www.w3.org/2000/svg">'
      + '<title>Composition of the gut T and innate lymphoid compartment from fetus to adult</title>'
      + '<desc>Each stage is normalised to 100 percent. Innate LTi-like pioneers occupy about a fifth of the fetal compartment then disappear; the adaptive T compartment rises to around 90 percent.</desc>';

    s += '<line x1="' + r1(X[0]) + '" y1="' + r1(Y_TOP) + '" x2="' + r1(X[3]) + '" y2="' + r1(Y_TOP) + '" stroke="#e8e4d8" stroke-width="1"/>';
    s += '<line x1="' + r1(X[0]) + '" y1="' + r1(Y_TOP + H) + '" x2="' + r1(X[3]) + '" y2="' + r1(Y_TOP + H) + '" stroke="#e8e4d8" stroke-width="1"/>';

    BANDS.forEach(function(b, bi){
      s += '<path class="fig6-band" data-bi="' + bi + '" d="' + bandPath(bi) + '" fill="' + b.color
        + '" opacity="0.9" style="cursor:pointer;transition:opacity .25s ease;"><title>' + b.label + '</title></path>';
    });

    s += '<text x="92" y="' + r1(ltiMid0 - 3) + '" font-size="14" font-weight="600" fill="#FFFFFF">Innate pioneers</text>';
    s += '<text x="92" y="' + r1(ltiMid0 + 13) + '" font-size="12" fill="#FFFFFF">fetal-only wave</text>';
    s += '<text x="452" y="' + r1(tMid3 - 4) + '" text-anchor="middle" font-size="14" font-weight="600" fill="#FFFFFF">Adaptive T compartment</text>';
    s += '<text x="452" y="' + r1(tMid3 + 13) + '" text-anchor="middle" font-size="12" fill="#FFFFFF">dominant from birth on</text>';

    STAGES.forEach(function(st, si){
      s += '<text x="' + r1(X[si]) + '" y="' + r1(Y_TOP + H + 24) + '" text-anchor="middle" font-size="15" fill="#3a3028">' + st.label + '</text>';
    });
    s += '<text x="' + r1(X[2]) + '" y="' + r1(Y_TOP + H + 40) + '" text-anchor="middle" font-size="12" font-style="italic" fill="#888780">T &amp; Treg counts \u22482\u00d7 age-matched</text>';

    let lx = 70;
    BANDS.forEach(function(b, bi){
      s += '<g class="fig6-leg" data-bi="' + bi + '" style="cursor:pointer;">'
        + '<circle cx="' + lx + '" cy="' + r1(Y_TOP + H + 60) + '" r="5" fill="' + b.color + '"/>'
        + '<text x="' + (lx + 9) + '" y="' + r1(Y_TOP + H + 64) + '" font-size="12" fill="#5F5E5A">' + b.label + '</text></g>';
      lx += 14 + b.label.length * 7 + 20;
    });

    s += '</svg>';

    const container = document.getElementById('fig6-content');
    container.innerHTML = s;
    bandEls = container.querySelectorAll('.fig6-band');

    const caption = document.getElementById('fig6-caption');
    function hover(bi){
      setBands(bi);
      caption.textContent = BANDS[bi].label + ' \u2014 '
        + STAGES.map(function(st, si){ return st.label + ' ' + (frac[bi][si] * 100).toFixed(1) + '% (' + fmt(counts[bi][si]) + ')'; }).join(' \u00b7 ');
    }
    function leave(){ setBands(null); caption.textContent = DEFAULT_CAP; }

    container.querySelectorAll('.fig6-band').forEach(function(el){
      el.addEventListener('mouseenter', function(){ hover(parseInt(el.dataset.bi, 10)); });
      el.addEventListener('mouseleave', leave);
    });
    container.querySelectorAll('.fig6-leg').forEach(function(el){
      el.addEventListener('mouseenter', function(){ hover(parseInt(el.dataset.bi, 10)); });
      el.addEventListener('mouseleave', leave);
    });
  }

  fetch(DATA_URL)
    .then(function(r){ if(!r.ok) throw new Error('JSON not found'); return r.json(); })
    .then(function(d){ fig6Data = d; build(); })
    .catch(function(e){
      document.getElementById('fig6-content').innerHTML =
        '<p style="text-align:center;color:#AF3A3A;padding:2rem;">Could not load: ' + e.message + '</p>';
    });
})();
</script>
Using spatial transcriptomics (10x Genomics Visium) on fetal ileum sections, the authors mapped these cell types onto tissue and showed that mLTo, LTi-like ILC3, and LEC2 cells co-localise in the same tissue zones, surrounded by naive T and B cells. These zones are the architectural precursors of secondary lymphoid organs.


Crucially, the authors then compared this fetal programme to tissue from paediatric Crohn's disease. They found that ILC3s, T reticular cells, and stromal subsets from Crohn's biopsies transcriptionally resemble their fetal counterparts. In other words, the same developmental programme that builds lymph nodes during pregnancy appears to be reactivated to form ectopic lymphoid structures at sites of intestinal inflammation.

<p class="figure-gallery-label">Original figures from the article</p>
<div class="figure-gallery">

  <figure class="figure-card" data-caption-id="cap-4a">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig4a_umap_tcells.png"
         alt="UMAP of T and innate lymphoid cells" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 4a</strong>
      T/innate lymphoid cells
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-4b">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig4b_lti_schematic.png"
         alt="Schematic of LTi-like cell states" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 4b</strong>
      LTi-like cell states
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-4c">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig4c_smfish_lti_mlto.png"
         alt="smFISH of RORC CXCR5 LTi cells next to CXCL13 mLTo cells" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 4c</strong>
      smFISH — LTi adjacent to mLTo
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-4d">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig4d_umap_stromal.png"
         alt="UMAP of stromal cell types" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 4d</strong>
      Stromal cell types
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-4e">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig4e_visium_spatial.png"
         alt="Spatial transcriptomics of fetal ileum showing LEC2, LTi, M cells" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 4e</strong>
      Visium spatial mapping
    </div>
  </figure>

  <figure class="figure-card" data-caption-id="cap-4f">
    <img src="{{ site.baseurl }}/assets/images/elmentaite-2021/thumbs/fig4f_gwas_enrichment.png"
         alt="GWAS enrichment for Crohn's disease and ulcerative colitis" loading="lazy">
    <div class="figure-card-label">
      <strong>Fig. 4f</strong>
      Crohn's / UC GWAS enrichment
    </div>
  </figure>

</div>

<div class="act-divider"><span class="act-divider-label">Epilogue</span></div>

## From atlas to clinic

The complete dataset is browsable at [gutcellatlas.org](https://www.gutcellatlas.org/). All raw sequencing data are available at ArrayExpress (E-MTAB-9543, E-MTAB-9536, E-MTAB-9532, E-MTAB-9533, E-MTAB-10386), and the code is on GitHub at [Teichlab/SpaceTimeGut](https://github.com/Teichlab/SpaceTimeGut).

While this atlas focuses on Hirschsprung disease as the canonical enteric neuropathy, the same cell taxonomy is increasingly being used to understand acquired motility disorders such as chronic intestinal pseudo-obstruction (CIPO) — work I have been developing in parallel.

---

**Citation.** Elmentaite, R., Kumasaka, N., Roberts, K. *et al.* Cells of the human intestinal tract mapped across space and time. *Nature* **597**, 250–255 (2021). [doi:10.1038/s41586-021-03852-1](https://doi.org/10.1038/s41586-021-03852-1)

All figure panels reproduced here are used under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Panels from Fig. 1d additionally credit the [Human Protein Atlas](https://www.proteinatlas.org/) as the original image source.

{% comment %}
================================================================================
LIGHTBOX OVERLAY (single instance, used by all galleries above)
================================================================================
{% endcomment %}

<div class="lightbox" id="lightbox" aria-hidden="true">
  <button class="lightbox-close" id="lightbox-close" aria-label="Close">×</button>
  <div class="lightbox-content">
    <img src="" id="lightbox-img" alt="">
    <div class="lightbox-caption" id="lightbox-caption"></div>
  </div>
</div>

<script type="application/json" id="figure-captions">
{
  "cap-1a": {
    "title": "Fig. 1a — Schematic of human gut tissue sampling",
    "text": "Sampling diagram showing the anatomical regions analysed: first and second trimester fetal donors (n = 16), and paediatric / adult donors with up to 11 distinct intestinal regions (paediatric n = 8, Crohn's disease n = 7, adult n = 6). The mesenteric lymph nodes (mLN) and the appendix are also sampled."
  },
  "cap-1b": {
    "title": "Fig. 1b — Cell lineage proportions across life",
    "text": "Stacked bars showing how the major cell lineages — epithelial, mesenchymal, endothelial, neural, B / plasma / T / NK / myeloid cells, and red blood cells — shift in relative abundance from the first trimester through adulthood, in both gut tissue and lymph nodes."
  },
  "cap-1c": {
    "title": "Fig. 1c — BEST4 cell abundance by region",
    "text": "Bar chart showing the percentage of BEST4-expressing enterocytes within the total epithelial compartment of each region, in fetal, paediatric and adult samples. BEST4 cells are most abundant in adult colon."
  },
  "cap-1d": {
    "title": "Fig. 1d — Histological validation of BEST4",
    "text": "Immunohistochemistry of BEST4 protein in four intestinal regions (duodenum, ileum, colon, rectum). Images sourced from the Human Protein Atlas (proteinatlas.org), n = 2 biologically independent samples per region. Scale bars: 50 µm."
  },
  "cap-1e": {
    "title": "Fig. 1e — Regional gene signature of BEST4 cells",
    "text": "Dot plot showing differentially expressed genes between BEST4 enterocytes from small versus large intestine, in both fetal and postnatal donors. Small-intestinal BEST4 cells are marked by CFTR, CPA2 and ADGRG4; colonic BEST4 cells by CA4, CA7, OTOP2 and metallothionein genes (MT1G, MT2A)."
  },
  "cap-2f": {
    "title": "Fig. 2f — FCGR2A and PLCG2 pathway in tuft cells",
    "text": "Dot plot of expression of upstream and downstream molecules of the PLCG2 pathway in tuft cells, compared with pooled absorptive (transit-amplifying + enterocytes) and secretory (Paneth + goblet + EECs) cells. FCGR2A, PLCG2, ITPR2, PRKCA and TRPM5 are markedly enriched in tuft cells."
  },
  "cap-2g": {
    "title": "Fig. 2g — Flow cytometry validation in mice",
    "text": "Percentage expression of Fcγ receptors on EpCAM⁺SiglecF⁺ tuft cells (blue) and EpCAM⁺SiglecF⁻ non-tuft epithelial cells (grey) from wild-type mice. Tuft cells show significantly higher FcγRIIB and FcγRIIB/III expression. **** P_adj < 0.0001 (two-way ANOVA with Tukey's correction). n = 4 biological replicates."
  },
  "cap-2h": {
    "title": "Fig. 2h — Schematic of proposed tuft cell signalling",
    "text": "Proposed model of IgG sensing in tuft cells: IgG Fc binds FCGR2A on the cell surface, which signals through SYK to activate PLCG2. PLCG2 generates IP₃ (activating ITPR2 and intracellular Ca²⁺ release) and DAG (activating PRKCA / PKC). TRPM5 mediates Na⁺ influx, completing the response."
  },
  "cap-3a": {
    "title": "Fig. 3a — Enteric nervous system at 6–11 PCW",
    "text": "UMAP of enteric neural crest cells (ENCC) and their progeny at 6–11 post-conception weeks. RNA velocity arrows show two major differentiation branches: branch A (ETV1+, giving inhibitory motor neurons and intrinsic primary afferent / interneurons) and branch B (BNC2+, giving excitatory motor neurons)."
  },
  "cap-3b": {
    "title": "Fig. 3b — Enteric nervous system at 12–17 PCW",
    "text": "UMAP at 12–17 PCW shows enrichment of glial cell types (DHH+ glia 1, ELN+ glia 2, BCAN+ glia 3, and a COL20A1+ differentiating glia population), in addition to the maturing neuronal branches."
  },
  "cap-3c": {
    "title": "Fig. 3c — smFISH of enteric neurons at 15 PCW",
    "text": "Multiplex smFISH staining showing SCGN-expressing branch A1 neurons (green), GRP-expressing branch A2/A3 neurons (yellow), and BNC2-expressing branch B1/B2 neurons (red) in the 15 PCW ileum. ELAVL4 is a pan-neuronal marker. Scale bar: 100 µm. n = 2 biological replicates."
  },
  "cap-3d": {
    "title": "Fig. 3d — smFISH of enteric glia",
    "text": "Multiplex smFISH of glia 1 cells expressing DHH, MPZ and SOX10 in the mesentery. Main panel scale bar: 100 µm; expansion: 30 µm. n = 2 biological replicates."
  },
  "cap-3e": {
    "title": "Fig. 3e — HSCR-associated gene expression across neural cells",
    "text": "Heatmap of mean expression of Hirschsprung's disease-associated genes across enteric neural cell types, separated by intestinal region (small vs large) and developmental stage (6–11 vs 12–17 PCW). RET is high in branch A; ZEB2 and EDNRB are higher in colonic glia and neuroblasts than in small-intestinal counterparts."
  },
  "cap-4a": {
    "title": "Fig. 4a — T and innate lymphoid cells",
    "text": "UMAP of T and innate cells across fetal, paediatric and adult samples. The dashed line marks the three LTi-like cell clusters (ILCP, NCR+ ILC3, NCR- ILC3) characterised by high RORC, KIT, IL7R, LTA and LTB expression."
  },
  "cap-4b": {
    "title": "Fig. 4b — LTi-like cell expression signatures",
    "text": "Schematic showing the distinctive expression signatures of the three LTi-like states: ILCP (SCN1B, HPN, CXCR5), NCR+ ILC3 (NCR2, IL2, JAG1, CD40LG), and NCR- ILC3 (IL17A, granzyme A, CCR9). The shared upstream RORγ and transcription factor programme is shown above."
  },
  "cap-4c": {
    "title": "Fig. 4c — LTi cells adjacent to mLTo cells",
    "text": "Multiplex smFISH of 15 PCW ileum showing RORC+ and CXCR5+ LTi-like cells positioned next to CXCL13-expressing mesenchymal lymphoid tissue organiser (mLTo) cells. White arrows highlight cells of interest. Scale bars: main 100 µm, expansion 50 µm. n = 2 biological replicates. This is the spatial evidence that LTi and mLTo cells congregate to seed lymphoid tissue."
  },
  "cap-4d": {
    "title": "Fig. 4d — Stromal cell types across development",
    "text": "UMAP of stromal cell populations across fetal, paediatric and adult samples. Key fetal lineages include mesothelium, smooth muscle, myofibroblasts, interstitial cells of Cajal, several stromal subtypes (1-4), and the mLTo cells central to lymphoid organogenesis. T reticular cells (TRCs) and follicular dendritic cells (FDCs) are also annotated."
  },
  "cap-4e": {
    "title": "Fig. 4e — Spatial transcriptomics of fetal ileum (Visium)",
    "text": "Spatial mapping of three cell types onto a 17 PCW fetal terminal ileum section using cell2location. Each dot represents a Visium capture spot, coloured by estimated abundance. LEC2 cells (MADCAM1+ lymphatic endothelium, left) and LTi-like NCR+ ILC3 (middle) map to the same tissue zone, while Microfold cells (right) appear in an adjacent zone — the architectural precursors of secondary lymphoid organs."
  },
  "cap-4f": {
    "title": "Fig. 4f — Gene enrichment for Crohn's disease and ulcerative colitis",
    "text": "Forest plot of cell types enriched for genes associated with Crohn's disease (left) or ulcerative colitis (right). Each point is the log odds ratio estimated by an fGWAS approach. Cell types in red have false-discovery rate < 10%. Adult ILC3, fetal ILCP and NCR+ ILC3 are among the top cells for Crohn's-associated gene expression."
  }
}
</script>

<script>
(function() {
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const closeBtn = document.getElementById('lightbox-close');
  const captionsData = JSON.parse(document.getElementById('figure-captions').textContent);

  const attribution = '<div class="source">' +
    'From Elmentaite et al., Nature 597, 250–255 (2021). Reproduced under ' +
    '<a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a>. ' +
    '<a href="https://www.nature.com/articles/s41586-021-03852-1" target="_blank" rel="noopener">View original article →</a>' +
    '</div>';

  function openLightbox(card) {
    const img = card.querySelector('img');
    const capId = card.dataset.captionId;
    const cap = captionsData[capId] || { title: '', text: '' };
    const fullSrc = img.src.replace('/thumbs/', '/full/');
    lightboxImg.src = fullSrc;
    lightboxImg.alt = img.alt;
    lightboxCaption.innerHTML =
      '<strong>' + cap.title + '</strong>' +
      cap.text +
      attribution;
    lightbox.classList.add('is-open');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('is-open');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.figure-card').forEach(function(card) {
    card.addEventListener('click', function() { openLightbox(card); });
  });

  closeBtn.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', function(e) {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && lightbox.classList.contains('is-open')) {
      closeLightbox();
    }
  });
})();
</script>
