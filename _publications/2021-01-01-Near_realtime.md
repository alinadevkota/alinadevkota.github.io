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
videoslug: 'nasco'
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

## Summary

We present a methodology using GPS-enabled mobile sensors to collect and model fine-scale environmental proxies (e.g., temperature, CO₂, PM₂.₅) along major roadways in Nepal, demonstrating the effectiveness of ARIMA and RNNs for real-time and historical climate modeling.

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
