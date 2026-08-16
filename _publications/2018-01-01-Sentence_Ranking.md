---
title: "Sentence Ranking and Answer Pinpointing in Online Discussion Forums Utilizing User-generated Metrics and Highlights"
authors: 'S. Gautam, S. Shikha, A. Devkota, S. Pyakurel'
collection: publications
category: manuscripts
permalink: /publication/2018-01-01-Sentence_Ranking
excerpt: 'This work presents a framework for extracting precise answers from online discussion forums by combining sentence ranking with user-generated metrics and highlights. The approach enables accurate answer pinpointing, improving search relevance and supporting better question-answering in forums.'
date: 2018-01-01
venue: 'NASCOIT'
paperurl: 'https://www.researchgate.net/profile/Sushant-Gautam/publication/330041750_Sentence_Ranking_and_Answer_Pinpointing_in_Online_Discussion_Forums_Utilising_User-generated_Metrics_and_Highlights/links/5c2b76e3a6fdccfc70761dd3/Sentence-Ranking-and-Answer-Pinpointing-in-Online-Discussion-Forums-Utilising-User-generated-Metrics-and-Highlights.pdf'
citation: 'Gautam, S., Shikha, S., Devkota, A. and Pyakurel, S., 2018. Sentence Ranking and Answer Pinpointing in Online Discussion Forums Utilising User-generated Metrics and Highlights. Proceedings of the NaSCoIT.'
teaser: images/publications/sranking_teaser.png
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

## Summary

This work presents a framework for extracting precise answers from online discussion forums by combining sentence ranking with user-generated metrics and highlights. The approach enables accurate answer pinpointing, improving search relevance and supporting better question-answering in forums.
