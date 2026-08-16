---
title: "Near Real-Time Mobile Profiling and Modeling of Fine-Scale Environmental Proxies Along Major Road Lines of Nepal"
authors: 'N. B. Adhikari, S. Gautam, A. Devkota, S. Shikha, S. Pyakurel, M. P. Adhikari'
collection: publications
category: manuscripts
permalink: /publication/2021-01-01-Near_realtime
excerpt: 'We present a methodology using GPS-enabled mobile sensors to collect and model fine-scale environmental proxies (e.g., temperature, CO₂, PM₂.₅) along major roadways in Nepal, demonstrating the effectiveness of ARIMA and RNNs for real-time and historical climate modeling.'
date: 2021-01-01
venue: 'ICMSI'
paperurl: 'https://www.researchgate.net/profile/Nanda-Adhikari/publication/353701660_Near_Real-Time_Mobile_Profiling_and_Modeling_of_Fine-Scale_Environmental_Proxies_Along_Major_Road_Lines_of_Nepal/links/610b76a4169a1a0103dde797/Near-Real-Time-Mobile-Profiling-and-Modeling-of-Fine-Scale-Environmental-Proxies-Along-Major-Road-Lines-of-Nepal.pdf'
citation: 'Adhikari, N.B., Gautam, S., Devkota, A., Shikha, S., Pyakurel, S. and Adhikari, M.P., 2020, January. Near Real-Time Mobile Profiling and Modeling of Fine-Scale Environmental Proxies Along Major Road Lines of Nepal. In International Conference on Mobile Computing and Sustainable Informatics (pp. 605-617). Cham: Springer International Publishing.'
teaser: images/publications/nasco_teaser.png
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

We present a methodology using GPS-enabled mobile sensors to collect and model fine-scale environmental proxies (e.g., temperature, CO₂, PM₂.₅) along major roadways in Nepal, demonstrating the effectiveness of ARIMA and RNNs for real-time and historical climate modeling.
