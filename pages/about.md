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
@media (max-width: 768px) {
  .about-header {
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
  }

  .photo-wrapper {
    width: 100%;
    min-width: unset;
    height: 340px;
    padding-bottom: 3rem; /* espace sous la photo */
  }

  .about-header > div:last-child {
    width: 100%;
    margin-top: 2rem; /* espace supplémentaire avant le texte */
  }
}

</style>

<div class="about-header">
  <div class="photo-wrapper">
    <div class="blob-orange"></div>
    <div class="blob-pink"></div>
    <img src="/assets/images/Pro_linkedin.jpg" alt="Minh-Chau Ta, MD">
  </div>
  <div>
    <h1 style="margin-top: 0;">Minh C. Thom, MD</h1>
    <p>I am a physician-scientist with training in pathology, molecular genetics, and translational research.</p>
    <p>Born in Vietnam and raised in France, I earned my MD from Sorbonne University in Paris, where I also completed my residency.</p>
    <p>Alongside my medical training, I completed a Master’s degree in philosophy, an experience that shaped my approach to complex reasoning and decision-making.</p>
    <p>My work has been presented at international conferences across the United States and Europe. It has been recognized through competitive awards and grants, including the 2023 Research Grant from the Society of Pathology, the Bernard Beaufrère Research Prize, and the Best Medical Thesis Prize from the Rotary Club of Paris.</p>
    <p>Having lived and trained in diverse international settings, I see intellectual flexibility, adaptability, and interdisciplinary collaboration as drivers of innovation in medicine.</p>
    <p>I currently live in San Diego with my husband and family. Outside of medicine and research, I enjoy travel, pickleball, philosophy, and exploring how different cultures, languages, and disciplines shape the way we understand health and science.</p>
  </div>
</div>