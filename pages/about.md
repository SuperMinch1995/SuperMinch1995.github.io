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

/* ===== Photo 1 — Pro_linkedin (dans about-header, inchangé) ===== */
.photo-wrapper.pw-pro {
  position: relative;
  width: 300px;
  min-width: 300px;
  height: 380px;
}
.photo-wrapper.pw-pro img {
  position: absolute;
  z-index: 1;
  width: 240px;
  border-radius: 6px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 8px 30px rgba(0,0,0,0.15);
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
  33%      { border-radius: 50% 50% 30% 70% / 60% 40% 60% 40%; }
  66%      { border-radius: 30% 70% 55% 45% / 38% 62% 38% 62%; }
}
@keyframes morph-pink {
  0%, 100% { border-radius: 38% 62% 30% 70% / 55% 45% 55% 45%; }
  33%      { border-radius: 70% 30% 60% 40% / 45% 55% 35% 65%; }
  66%      { border-radius: 45% 55% 40% 60% / 62% 38% 62% 38%; }
}

/* ===== Photo 2 — ESPEN (pleine largeur, trio en cascade) ===== */
.photo-wrapper.pw-espen {
  position: relative;
  width: 500px;
  max-width: 100%;
  height: 640px;
  margin: 3rem auto;
}
.photo-wrapper.pw-espen img {
  position: absolute;
  z-index: 1;
  width: 400px;
  max-width: 80%;
  border-radius: 6px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}
.blob-espen-a {
  position: absolute;
  width: 38%;
  height: 34%;
  background: linear-gradient(135deg, #722F37, #B85042);
  top: 0;
  left: -5%;
  z-index: 0;
  border-radius: 60% 40% 50% 50% / 50% 60% 40% 50%;
  animation: morph-espen-a 8s ease-in-out infinite;
}
.blob-espen-b {
  position: absolute;
  width: 50%;
  height: 47%;
  background: linear-gradient(135deg, #D4923C, #F2D8A0);
  top: 32%;
  right: -7%;
  z-index: 0;
  border-radius: 50% 50% 30% 70% / 60% 40% 60% 40%;
  animation: morph-espen-b 10s ease-in-out infinite -2s;
}
.blob-espen-c {
  position: absolute;
  width: 40%;
  height: 35%;
  background: linear-gradient(135deg, #C88FA0, #E8A0B4);
  bottom: -4%;
  left: -3%;
  z-index: 0;
  border-radius: 45% 55% 60% 40% / 55% 45% 55% 45%;
  animation: morph-espen-c 9s ease-in-out infinite -1s;
}
@keyframes morph-espen-a {
  0%, 100% { border-radius: 60% 40% 50% 50% / 50% 60% 40% 50%; }
  50%      { border-radius: 40% 60% 60% 40% / 60% 40% 60% 40%; }
}
@keyframes morph-espen-b {
  0%, 100% { border-radius: 50% 50% 30% 70% / 60% 40% 60% 40%; }
  33%      { border-radius: 70% 30% 50% 50% / 40% 60% 40% 60%; }
  66%      { border-radius: 30% 70% 60% 40% / 50% 50% 70% 30%; }
}
@keyframes morph-espen-c {
  0%, 100% { border-radius: 45% 55% 60% 40% / 55% 45% 55% 45%; }
  50%      { border-radius: 65% 35% 40% 60% / 35% 65% 35% 65%; }
}

/* ===== Photo 3 — Beach (pleine largeur, vignette enveloppante) ===== */
.photo-wrapper.pw-beach {
  position: relative;
  width: 720px;
  max-width: 100%;
  height: 580px;
  margin: 3rem auto;
}
.photo-wrapper.pw-beach img {
  position: absolute;
  z-index: 1;
  width: 600px;
  max-width: 85%;
  border-radius: 6px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}
.blob-beach {
  position: absolute;
  width: 110%;
  height: 90%;
  background: linear-gradient(135deg, #82B6D6 0%, #FFB088 35%, #E8D5B7 65%, #E8A0B4 100%);
  bottom: -8%;
  left: -8%;
  z-index: 0;
  border-radius: 60% 40% 35% 65% / 50% 60% 40% 50%;
  animation: morph-beach 12s ease-in-out infinite;
}
@keyframes morph-beach {
  0%, 100% { border-radius: 60% 40% 35% 65% / 50% 60% 40% 50%; }
  33%      { border-radius: 40% 60% 60% 40% / 60% 40% 60% 40%; }
  66%      { border-radius: 55% 45% 50% 50% / 40% 60% 50% 50%; }
}

/* ===== Mobile responsive ===== */
@media (max-width: 768px) {
  .about-header {
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
  }
  .photo-wrapper.pw-pro {
    width: 100%;
    min-width: unset;
    height: 340px;
    padding-bottom: 1rem;
  }
  .about-header > div:last-child {
    width: 100%;
    margin-top: 2rem;
  }
  .photo-wrapper.pw-espen {
    width: 100%;
    height: 480px;
    margin: 2.5rem auto;
  }
  .photo-wrapper.pw-espen img {
    width: 70%;
    max-width: 280px;
  }
  .photo-wrapper.pw-beach {
    width: 100%;
    height: 320px;
    margin: 2.5rem auto;
  }
  .photo-wrapper.pw-beach img {
    width: 85%;
    max-width: 360px;
  }
}
</style>

<div class="about-header">
  <div class="photo-wrapper pw-pro">
    <div class="blob-orange"></div>
    <div class="blob-pink"></div>
    <img src="/assets/images/Pro_linkedin.jpg" alt="Minh-Chau Ta, MD">
  </div>
  <div>
    <h1 style="margin-top: 0;">Minh C. Thom, MD</h1>

    <br><p>I am a physician-scientist with training in pathology and molecular genetics.</p>
    <p>Born in Vietnam and raised in France, I earned my MD from Sorbonne University in Paris, where I also completed my residency.</p>

    <p>Alongside my medical training, I completed a Master’s degree in philosophy - an experience that deepened my reasoning and decision-making.</p>
  </div>
</div>

<br>
<p>My research has been presented internationally across the United States and Europe.</p>

<div class="photo-wrapper pw-espen">
  <div class="blob-espen-a"></div>
  <div class="blob-espen-b"></div>
  <div class="blob-espen-c"></div>
  <img src="/assets/images/espen-2025.webp" alt="Lecture at the 47th ESPEN Congress, 2025">
</div>

<br>
<p>I received multiple awards and competitive grants, including the 2023 Research Grant from the Society of Pathology, the Bernard Beaufrère Research Prize, and the Best Medical Thesis Prize from the Rotary Club of Paris.</p>

<p>Having lived and trained in diverse international settings, I see intellectual flexibility and interdisciplinary collaboration as drivers of innovation in medicine.</p>

<p>I currently live in San Diego with my husband and family.</p>

<p>Outside of medicine and research, I enjoy travel, pickleball, and exploring how different cultures, languages, and disciplines shape the way we understand health and science.</p>

<div class="photo-wrapper pw-beach">
  <div class="blob-beach"></div>
  <img src="/assets/images/Beach.webp" alt="Family in San Diego">
</div>