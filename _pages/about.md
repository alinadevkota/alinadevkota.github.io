---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
/* Scoped to this page. Theme --global-* custom properties handle light/dark. */
:root { --sec-text: #696f75; }
html[data-theme="dark"] { --sec-text: #bcc0c4; }

/* "About Me" is the page h1 and keeps the theme's title styling. Research
   Interests and News are h2, and head/custom.html styles .page__content h2 as
   a small uppercase label for the publication pages - that is undone here so
   all three headings on this page look the same.
   1.563em is what .page__title actually resolves to - it sets no font-size of
   its own and inherits the theme's h1 rule. The theme's 1.953em / 2.441em
   title rules belong to .page__hero--overlay .page__title, which is not used
   here. Measured: both render at 28.134px against an 18px parent. */
.page__content h2 {
  margin-top: 1.6em;
  margin-bottom: 0.5rem;
  padding-bottom: 0;
  border-bottom: 0;
  font-size: 1.563em;
  font-weight: bold;
  letter-spacing: normal;
  line-height: 1;
  text-transform: none;
  color: var(--global-text-color);
}

/* Opening paragraph, set slightly larger so the page has an entry point. */
.hp-lead {
  font-size: 1.08em;
  line-height: 1.65;
}

/* Research areas as a typographic list rather than boxed tags. */
.hp-areas {
  margin: 0 0 1.1em;
  padding: 0;
  list-style: none;
  font-size: 0.95em;
  line-height: 1.9;
}

.hp-areas li {
  display: inline;
  margin: 0;
}

.hp-areas li + li::before {
  content: "\00b7";
  margin: 0 0.6em;
  color: var(--sec-text);
}

/* News: year in a fixed left column so the entries line up and the year is
   not repeated inline in every sentence. */
.hp-news {
  margin: 0;
}

.hp-news__item {
  display: grid;
  grid-template-columns: 3.6em 1fr;
  gap: 0 1em;
  padding: 0.65em 0;
  border-bottom: 1px solid var(--global-border-color);
}

.hp-news__item:last-child {
  border-bottom: 0;
}

.hp-news__year {
  font-size: 0.78em;
  font-weight: 700;
  letter-spacing: 0.06em;
  line-height: 1.9;
  color: var(--sec-text);
}

.hp-news__text {
  font-size: 0.95em;
  line-height: 1.6;
}

@media (max-width: 520px) {
  .hp-news__item {
    grid-template-columns: 1fr;
    gap: 0.15em;
  }
  .hp-news__year {
    line-height: 1.4;
  }
}
</style>

<p class="hp-lead">I am a Third-year Ph.D. student in Computer Science at West Virginia University, working with <a href="https://pkgyawali.com/">Dr. Prashnna K. Gyawali</a> at the <a href="https://sites.google.com/view/gyawalilab/">Machine Intelligence Lab</a>. Before starting my Ph.D., I worked as a Machine Learning Engineer for four years, where I developed and deployed machine learning models across various applications. I completed my Bachelor's degree in Computer Engineering from Pulchowk Campus (Institute of Engineering), Tribhuvan University, Nepal.</p>

I enjoy tackling challenging problems, learning new techniques, and applying them creatively to make an impact.
Outside of research, I enjoy playing chess and can be found on chess.com under the username [AlinaDevkota](https://www.chess.com/member/alinadevkota).

Please do not hesitate to reach out to me via [LinkedIn](https://www.linkedin.com/in/alina-devkota-47415413a/) or email at [devkota.alina@gmail.com](mailto:devkota.alina@gmail.com).

## Research Interests

{% comment %}
Research-area list, hidden for now. Remove this comment wrapper to restore it.
<ul class="hp-areas">
  <li>Multimodal Learning</li>
  <li>Out-of-Distribution Detection</li>
  <li>Vision-Language Models</li>
  <li>Foundation Models</li>
  <li>Federated Learning</li>
  <li>Medical Imaging</li>
</ul>
{% endcomment %}

My research is focused on applying Artificial Intelligence (AI) to healthcare. I am currently focusing my research on multimodal out-of-distribution (OOD) detection.
My earlier work has focused on foundation models and privacy-preserving techniques, such as federated learning for medical imaging, particularly in gastrointestinal endoscopy.
I am also passionate about exploring broader areas of computer vision, large language models, and other applications of deep learning and machine learning.

Looking ahead, I plan to concentrate future research at the intersection of advanced computer vision and language models for medical imaging, with the goal of enhancing diagnostic accuracy and improving patient outcomes.

## News

<div class="hp-news">

  <div class="hp-news__item">
    <span class="hp-news__year">2026</span>
    <div class="hp-news__text">Currently serving as the <strong>Web and Publicity Chair</strong> for the <a href="https://demi-workshop.github.io/">4th DEMI Workshop at MICCAI 2026</a>.</div>
  </div>

  <div class="hp-news__item">
    <span class="hp-news__year">2026</span>
    <div class="hp-news__text">Received <strong>2nd place</strong> in the Rapid Fire Presentation at <a href="{{ '/files/AlinaDevkota_RapidFire.pptx.pdf' | relative_url }}">Statler College Research Week</a>.</div>
  </div>

  <div class="hp-news__item">
    <span class="hp-news__year">2026</span>
    <div class="hp-news__text">Our paper, <em><a href="https://openaccess.thecvf.com/content/CVPR2026F/papers/Devkota_FedVG_Gradient-Guided_Aggregation_for_Enhanced_Federated_Learning_CVPRF_2026_paper.pdf">FedVG: Gradient-Guided Aggregation for Enhanced Federated Learning</a></em>, has been accepted to <strong>CVPR Findings 2026</strong>.</div>
  </div>

  <div class="hp-news__item">
    <span class="hp-news__year">2025</span>
    <div class="hp-news__text">Served as the lecturer for the <a href="https://www.linkedin.com/posts/prashnna-k-gyawali_generativeai-reliableai-aieducation-activity-7349619059082084352-xlRh">WVU SURE Generative AI Workshop</a>.</div>
  </div>

  <div class="hp-news__item">
    <span class="hp-news__year">2025</span>
    <div class="hp-news__text">Received <strong>2nd place</strong> in the poster presentation at the <a href="https://hsc.wvu.edu/research-and-graduate-education/wvu-ai-symposium/">WVU AI Symposium</a>.</div>
  </div>

  <div class="hp-news__item">
    <span class="hp-news__year">2025</span>
    <div class="hp-news__text">Our paper, <em><a href="https://www.nature.com/articles/s41598-025-97113-0">AI Analysis for Ejection Fraction Estimation from 12-Lead ECG</a></em>, was published in <strong>Scientific Reports</strong>.</div>
  </div>

</div>
