---
layout: basic
title: "About"
date: 2026-04-04
permalink: "/about/"
---

<style>
.about-header {
  display: flex;
  align-items: flex-start;
  margin-bottom: 2rem;
  gap: 2.5rem;
}
.photo-wrapper {
  position: relative;
  width: 300px;
  min-width: 300px;
  height: 380px;
}
.blob-orange {
  position: absolute;
  width: 260px;
  height: 290px;
  background: linear-gradient(135deg, #fff451, #FF6B00);
  border-radius: 62% 38% 70% 30% / 45% 55% 45% 55%;
  bottom: -40px;
  left: -30px;
  z-index: 0;
  animation: morph-orange 8s ease-in-out infinite;
}
.blob-pink {
  position: absolute;
  width: 230px;
  height: 280px;
  background: linear-gradient(135deg, #FF4D8B, #FF8C42);
  border-radius: 38% 62% 30% 70% / 55% 45% 55% 45%;
  top: 30px;
  right: -20px;
  z-index: 0;
  animation: morph-pink 9s ease-in-out infinite;
}
@keyframes morph-orange {
  0%, 100% { border-radius: 62% 38% 70% 30% / 45% 55% 45% 55%; }
  33%       { border-radius: 50% 50% 30% 70% / 60% 40% 60% 40%; }
  66%       { border-radius: 30% 70% 55% 45% / 38% 62% 38% 62%; }
}
@keyframes morph-pink {
  0%, 100% { border-radius: 38% 62% 30% 70% / 55% 45% 55% 45%; }
  33%       { border-radius: 70% 30% 60% 40% / 45% 55% 35% 65%; }
  66%       { border-radius: 45% 55% 40% 60% / 62% 38% 62% 38%; }
}
.photo-wrapper img {
  position: absolute;
  z-index: 1;
  width: 240px;
  border-radius: 6px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}
</style>

<div class="about-header">
  <div class="photo-wrapper">
    <div class="blob-orange"></div>
    <div class="blob-pink"></div>
    <img src="/assets/images/Pro_linkedin.jpg" alt="Minh-Chau Ta, MD">
  </div>
  <div>
    <h1 style="margin-top: 0;">Minh-Chau Ta, MD</h1>
    <p>Born in 1995 in Vietnam, I moved to France at age 7. I earned my medical degree at Sorbonne University in Paris, then completed a residency in pathology with a focus on molecular genetics.</p>
    <p>During my full-time residency, I earned a Master of Arts in Philosophy at Sorbonne University, where I developed a way of thinking that helps me simplify complexity.</p>
    <p>I presented my research at international conferences in the U.S. and Europe and received several awards, including the 2023 research grant from the French Society of Pathology, the Bernard Beaufrère Research Prize, and the Best Medical Thesis Prize from the Rotary Club of Paris.</p>
  </div>
</div>

## Research Interests

- Brain-gut axis
- Clinical Nutrition
- Dermatopathology
- Tumoral clonal evolution

## Education

- **MD** — Sorbonne University, Paris, France
- **Residency in Pathology** — Paris, France
- **MA in Philosophy** — Sorbonne University, Paris, France

## Awards & Grants

- Annual Research Grant — French Society of Pathology
- Bernard Beaufrère Research Prize - French-speaking Society for Clinical Nutrition and Metabolism
- Best Medical Thesis Prize — Rotary Club of Paris