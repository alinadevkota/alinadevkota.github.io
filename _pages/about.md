---
permalink: /
title: "About Me"
description: "Alina Devkota is a PhD student in Computer Science at West Virginia University in the Machine Intelligence Lab, researching multimodal out-of-distribution detection, foundation models and federated learning for healthcare."
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
  grid-template-columns: 5.2em 1fr;
  gap: 0 1em;
  padding: 0.65em 0;
  border-bottom: 1px solid var(--global-border-color);
}

.hp-news__item:last-child {
  border-bottom: 0;
}

.hp-news__date {
  font-size: 0.78em;
  font-weight: 700;
  letter-spacing: 0.06em;
  line-height: 1.9;
  text-transform: uppercase;
  color: var(--sec-text);
}

.hp-news__text {
  font-size: 0.95em;
  line-height: 1.6;
}

/* --- Collapsed news ------------------------------------------------- */

/* The row after the visible ones is rendered but faded out, so the list
   visibly continues rather than stopping dead above the button. It sits
   outside <details> because a closed <details> does not render its contents
   at all, leaving nothing to fade. A mask is used rather than a gradient
   overlay so it works on any background, light or dark. */
.hp-news__peek {
  -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,0.25) 55%, rgba(0,0,0,0) 100%);
  mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,0.25) 55%, rgba(0,0,0,0) 100%);
  border-bottom: 0;
  transition: opacity 0.2s ease;
}

/* :has() lets the peek react to the sibling <details> being opened, so the
   row returns to full strength once everything is shown. */
.hp-news:has(.hp-news__more[open]) .hp-news__peek {
  -webkit-mask-image: none;
  mask-image: none;
  border-bottom: 1px solid var(--global-border-color);
}

/* Pull the control up under the faded row so the two read as one unit. */
.hp-news__more:not([open]) .hp-news__toggle {
  margin-top: 0.1em;
}


/* <summary> must be the first child of <details>, which would put the button
   between the visible and revealed entries and break the list in two. Making
   the element a flex column and giving the summary order:2 renders it after
   the revealed entries instead, so the list reads as one continuous run. */
.hp-news__more {
  display: flex;
  flex-direction: column;
  margin: 0;
}

/* The last visible entry keeps its rule because <details> follows it; the
   last entry inside <details> is :last-child of its own parent, so the
   existing :last-child rule still removes the final border correctly. */
.hp-news__toggle {
  order: 2;                        /* below the entries it reveals */
  align-self: flex-start;
  margin: 0.9em 0 0.2em;
  padding: 0.3em 0.95em;
  border: 1px solid var(--global-dark-border-color);
  border-radius: 3px;
  font-size: 0.8em;
  font-weight: 600;
  cursor: pointer;
  color: var(--global-link-color);
  list-style: none;                /* drop the default disclosure triangle */
}

.hp-news__toggle::-webkit-details-marker {
  display: none;
}

.hp-news__toggle:hover {
  border-color: var(--global-link-color);
}

.hp-news__toggle-show::after,
.hp-news__toggle-hide::after {
  margin-left: 0.4em;
}

.hp-news__toggle-show::after { content: "\25BE"; }   /* down triangle */
.hp-news__toggle-hide::after { content: "\25B4"; }   /* up triangle */

/* Swap the label depending on open state. */
.hp-news__more .hp-news__toggle-hide,
.hp-news__more[open] .hp-news__toggle-show {
  display: none;
}

.hp-news__more[open] .hp-news__toggle-hide {
  display: inline;
}

@media (max-width: 520px) {
  .hp-news__item {
    grid-template-columns: 1fr;
    gap: 0.15em;
  }
  .hp-news__date {
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
    <span class="hp-news__date">Oct 2026</span>
    <div class="hp-news__text">Our paper, <em>When Medical VLMs Stop Understanding: MedTEC-Bench for Probing Semantic Specificity</em>, has been accepted to the <strong>NeurIPS 2026 Evaluations &amp; Datasets Track</strong>.</div>
  </div>
  <div class="hp-news__item">
    <span class="hp-news__date">Sep 2026</span>
    <div class="hp-news__text">Our paper, <em><a href="https://arxiv.org/pdf/2505.24108">Federated Foundation Model for GI Endoscopy Images</a></em>, has been accepted to <strong>npj Digital Medicine</strong>.</div>
  </div>
  <div class="hp-news__item">
    <span class="hp-news__date">Sep 2026</span>
    <div class="hp-news__text">Released <a href="https://alinadevkota.github.io/Paper2Video/">Paper2Video</a>, a project that generates narrated explainer videos from research papers and lectures. <a href="{{ '/videos/' | relative_url }}">Watch the videos for my papers</a>.</div>
  </div>
  <div class="hp-news__item">
    <span class="hp-news__date">2026</span>
    <div class="hp-news__text">Currently serving as the <strong>Web and Publicity Chair</strong> for the <a href="https://demi-workshop.github.io/">4th DEMI Workshop at MICCAI 2026</a>.</div>
  </div>

  {% comment %}
    Collapsed with <details> rather than JavaScript: the hidden entries stay
    in the DOM for search engines, and the control is keyboard-accessible and
    works with JS disabled.
  {% endcomment %}
  <div class="hp-news__item hp-news__peek">
    <span class="hp-news__date">Apr 2026</span>
    <div class="hp-news__text">Received <strong>2nd place</strong> in the Rapid Fire Presentation at <a href="{{ '/files/AlinaDevkota_RapidFire.pptx.pdf' | relative_url }}">Statler College Research Week</a>.</div>
  </div>
  <details class="hp-news__more">
    <summary class="hp-news__toggle">
      <span class="hp-news__toggle-show">See more</span>
      <span class="hp-news__toggle-hide">Show less</span>
    </summary>
  <div class="hp-news__item">
    <span class="hp-news__date">Feb 2026</span>
    <div class="hp-news__text">Our paper, <em><a href="https://openaccess.thecvf.com/content/CVPR2026F/papers/Devkota_FedVG_Gradient-Guided_Aggregation_for_Enhanced_Federated_Learning_CVPRF_2026_paper.pdf">FedVG: Gradient-Guided Aggregation for Enhanced Federated Learning</a></em>, has been accepted to <strong>CVPR Findings 2026</strong>.</div>
  </div>
  <div class="hp-news__item">
    <span class="hp-news__date">Aug 2025</span>
    <div class="hp-news__text">Our work on estimating heart ejection fraction from 12-lead ECG was featured by
      <a href="https://wvutoday.wvu.edu/stories/2025/08/28/wvu-researchers-train-ai-to-diagnose-heart-failure-in-rural-patients-using-low-tech-electrocardiograms">WVU Today</a> and
      <a href="https://www.wvnews.com/news/wvnews/ai-models-developed-at-wvu-to-aid-heart-failure-diagnosis-in-rural-appalachia/article_208742e7-81ef-4fba-8924-db9e22e6889b.html">WV News</a>.</div>
  </div>
  <div class="hp-news__item">
    <span class="hp-news__date">Jul 2025</span>
    <div class="hp-news__text">Served as the lecturer for the <a href="https://www.linkedin.com/posts/prashnna-k-gyawali_generativeai-reliableai-aieducation-activity-7349619059082084352-xlRh">WVU SURE Generative AI Workshop</a>.</div>
  </div>
  <div class="hp-news__item">
    <span class="hp-news__date">May 2025</span>
    <div class="hp-news__text">Received <strong>2nd place</strong> in the poster presentation at the <a href="https://hsc.wvu.edu/research-and-graduate-education/wvu-ai-symposium/">WVU AI Symposium</a>.</div>
  </div>
  <div class="hp-news__item">
    <span class="hp-news__date">Apr 2025</span>
    <div class="hp-news__text">Our paper, <em><a href="https://www.nature.com/articles/s41598-025-97113-0">AI Analysis for Ejection Fraction Estimation from 12-Lead ECG</a></em>, was published in <strong>Scientific Reports</strong>.</div>
  </div>
  </details>

</div>
