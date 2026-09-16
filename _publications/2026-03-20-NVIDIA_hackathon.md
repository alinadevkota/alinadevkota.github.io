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
videoslug: 'nvidia_hackathon'
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
  {% if page.projecturl %}<a href="{{ page.projecturl }}">Project</a>{% endif %}
  {% if page.codeurl %}<a href="{{ page.codeurl }}">Code</a>{% endif %}
  {% if page.modelsurl %}<a href="{{ page.modelsurl }}">Models</a>{% endif %}
  {% include video-url.html doc=page %}
  {% if video_src %}<a href="{{ video_src }}" data-video-probe="{{ video_src }}" hidden>Video</a>{% endif %}
  {% if page.slidesurl %}<a href="{{ page.slidesurl }}">Slides</a>{% endif %}
  {% if page.citation %}<a href="#cite">Cite</a>{% endif %}
</p>

<div class="pub-body{% if video_src %} pub-body--split{% endif %}">

{% assign pub_figure = page.figure | default: page.teaser %}
{% if pub_figure %}
<p class="pub-teaser">
  <img src="{{ pub_figure | relative_url }}" alt="{{ page.figure_alt | default: page.title | escape }}">
  {% if page.figure_caption %}<span class="pub-teaser__caption">{{ page.figure_caption }}</span>{% endif %}
</p>
{% endif %}

<div class="pub-body__text" markdown="1">

## Abstract

The Carnegie Mellon University-NVIDIA Federated Learning Hackathon for Biomedical Applications (January 7-9, 2026) convened researchers from academia, government, and industry to implement federated frameworks for disease subtyping, genetic association studies, and multimodal clinical prediction using NVIDIA FLARE. This preprint presents ten projects spanning genome-wide association analyses, histopathology harmonization, pangenome construction, ancestry deconvolution, rare disease stratification, cancer subtyping, polygenic risk score aggregation, and multimodal fusion. These proofs of principle collectively demonstrate both the versatility of federated learning for biomedical applications and the technical considerations required for successful deployment.

</div>

</div>

{% comment %}
  Narrated explainer video (Paper2Video). Set `videoslug:` in the front matter
  (the filename in videos/mine without .mp4), or `videourl:` for a full URL.
  The block stays hidden until the browser confirms the file exists, so a paper
  whose video has not been uploaded yet simply shows nothing.
{% endcomment %}
{% include video-url.html doc=page %}
{% if video_src %}
<div class="pub-video" data-video-probe="{{ video_src }}" hidden>
  <div class="pub-video__player">
    <video controls preload="metadata"{% if video_poster %} poster="{{ video_poster }}"{% endif %}>
      <source src="{{ video_src }}" type="video/mp4">
      Your browser does not support embedded video.
      <a href="{{ video_src }}">Download the video</a> instead.
    </video>
  </div>
  <aside class="pub-video__note">
    <p class="pub-video__note-label">Explainer video</p>
    <p>Made with <a href="{{ site.paper2video_base }}/">Paper2Video</a>, a project of mine.</p>
    <p><a class="pub-video__note-more" href="{{ site.paper2video_base }}/">More videos and details</a></p>
  </aside>
</div>
{% endif %}
