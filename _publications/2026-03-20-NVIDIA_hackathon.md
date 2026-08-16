---
title: "Towards Federated Learning Across Biobanks: Prototype Software from the 2026 Carnegie Mellon University–NVIDIA Hackathon"
authors: 'J. Mu et al.'
collection: publications
category: manuscripts
permalink: /publication/2026-03-20-FL_Biobanks_Hackathon
excerpt: 'This preprint presents prototype federated learning software developed during the 2026 Carnegie Mellon University–NVIDIA Federated Learning Hackathon for Biomedical Applications. The work demonstrates federated frameworks across biomedical tasks including disease subtyping, genetic association studies, histopathology harmonization, rare disease stratification, cancer subtyping, polygenic risk score aggregation, and multimodal clinical prediction.'
date: 2026-03-20
venue: 'BioHackrXiv'
paperurl: 'https://osf.io/preprints/biohackrxiv/5psfj'
citation: 'Mu, J., et al., 2026. Towards Federated Learning Across Biobanks: Prototype Software from the 2026 Carnegie Mellon University–NVIDIA Hackathon. BioHackrXiv. https://doi.org/10.37044/osf.io/5psfj_v1.'
teaser: /images/publications/nvidia_hackathon_teaser.png
---

{% comment %}
  Paper-page header: authors, venue, action links, then the figure.
  `figure:` overrides `teaser:` when present; `teaser:` is the fallback.
{% endcomment %}
{% if page.authors %}
<p class="pub-authors">{{ page.authors | replace: 'A. Devkota', '<strong>A. Devkota</strong>' }}</p>
{% endif %}

{% if page.venue %}
{% assign pub_year = page.date | date: "%Y" %}
<p class="pub-venue">{{ page.venue }}{% unless page.venue contains pub_year %} &middot; {{ pub_year }}{% endunless %}</p>
{% endif %}

<p class="pub-actions">
  {% if page.paperurl %}<a href="{{ page.paperurl }}">Paper</a>{% endif %}
  {% if page.codeurl %}<a href="{{ page.codeurl }}">Code</a>{% endif %}
  {% if page.slidesurl %}<a href="{{ page.slidesurl }}">Slides</a>{% endif %}
  {% if page.citation %}<a href="#cite">Cite</a>{% endif %}
</p>

{% assign pub_figure = page.figure | default: page.teaser %}
{% if pub_figure %}
<p class="pub-teaser">
  <img src="{{ pub_figure | relative_url }}" alt="{{ page.figure_alt | default: page.title | escape }}">
  {% if page.figure_caption %}<span class="pub-teaser__caption">{{ page.figure_caption }}</span>{% endif %}
</p>
{% endif %}

## Abstract

The Carnegie Mellon University-NVIDIA Federated Learning Hackathon for Biomedical Applications (January 7-9, 2026) convened researchers from academia, government, and industry to implement federated frameworks for disease subtyping, genetic association studies, and multimodal clinical prediction using NVIDIA FLARE. This preprint presents ten projects spanning genome-wide association analyses, histopathology harmonization, pangenome construction, ancestry deconvolution, rare disease stratification, cancer subtyping, polygenic risk score aggregation, and multimodal fusion. These proofs of principle collectively demonstrate both the versatility of federated learning for biomedical applications and the technical considerations required for successful deployment.
