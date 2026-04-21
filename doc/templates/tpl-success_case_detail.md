---
title: Template · success_case_detail
drawer: templates
source: templates/success_case_detail.html
updated: 2026-04-21T01:50:49
tags: [template, html]
---
# Template · success_case_detail

Ficheiro: `templates/success_case_detail.html` (4.8 KB)

## Dependências de template

- [[tpl-menu]]
- [[tpl-footer]]
- [[tpl-help_chat]]

## Conteúdo

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>H3 New Hamburgology — Casos de Sucesso | PIE Angola</title>
  <meta name="description" content="H3 com Quiosque de pedidos — caso de sucesso PIE.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cabin:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/menu.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/help_chat.css' %}" />
</head>
<body class="case-detail-page">
  {% include 'components/menu/menu.html' %}

  <main>

    <!-- Breadcrumb -->
    <section class="fdetail-breadcrumb-wrap">
      <div class="container">
        <nav class="contact-breadcrumb" aria-label="Breadcrumb">
          <span class="contact-breadcrumb__dot" aria-hidden="true"></span>
          <a href="{% url 'success_cases' %}">Casos de Sucesso</a>
          <span class="contact-breadcrumb__sep" aria-hidden="true">|</span>
          <strong>H3 New Hamburgology</strong>
        </nav>
      </div>
    </section>

    <!-- Big hero image -->
    <section class="fdetail-hero">
      <div class="container">
        <img src="{% static 'images/components/sd-hero.jpg' %}" alt="H3 New Hamburgology — Quiosque de pedidos" class="fdetail-hero__img">
      </div>
    </section>

    <!-- Content: sidebar + main text -->
    <section class="fdetail-content">
      <div class="container fdetail-content__inner">

        <aside class="fdetail-sidebar" aria-label="Detalhes do cliente">
          <div class="fdetail-sidebar__logo">
            <img src="{% static 'images/components/sd-logo.png' %}" alt="H3 New Hamburgology">
          </div>
          <p class="fdetail-sidebar__label">Cliente:</p>
          <p class="fdetail-sidebar__value">H3 New Hamburgology</p>
          <hr class="fdetail-sidebar__divider">
          <p class="fdetail-sidebar__label">Produtos utilizados:</p>
          <ul class="fdetail-sidebar__list">
            <li>WinRest NX</li>
            <li>Kiosk Digital</li>
            <li>Site de Pedidos</li>
            <li>myCloud PIE</li>
          </ul>
        </aside>

        <div class="fdetail-main">
          <h1 class="fdetail-main__title">H3 com Quiosque de pedidos</h1>

          <div class="fdetail-main__body">
            <p>A H3 New Hamburgology implementou quiosques de auto-atendimento integrados com a plataforma PIE para transformar a experiência do cliente em loja. O resultado foi uma redução significativa do tempo de espera e um aumento da rotatividade nos picos de afluência, mantendo a qualidade de serviço característica da marca.</p>
            <p>A solução combina o WinRest NX como motor de POS, o Kiosk Digital como interface de pedidos e o myCloud PIE para a gestão centralizada de toda a cadeia. Os pedidos fluem em tempo real para a cozinha, com KDS dedicado, eliminando erros de comunicação e acelerando a preparação.</p>
          </div>

          <ol class="fdetail-main__numlist">
            <li><span class="fdetail-num">01.</span> Redução de filas em horas de pico e maior rotatividade.</li>
            <li><span class="fdetail-num">02.</span> Pedidos centralizados em backoffice com indicadores em tempo real.</li>
            <li><span class="fdetail-num">03.</span> Experiência consistente em todas as unidades da marca.</li>
          </ol>
        </div>

      </div>
    </section>

    <!-- Quote with red top bar -->
    <section class="fdetail-quote-section" aria-label="Testemunho">
      <div class="container">
        <div class="fdetail-quote">
          <div class="fdetail-quote__bar" aria-hidden="true"></div>
          <blockquote class="fdetail-quote__text">
            “A integração com a PIE permitiu-nos repensar o atendimento em loja: mais rápido, mais simples e com a robustez de que precisamos para crescer com confiança.”
          </blockquote>
        </div>
      </div>
    </section>

    <!-- Red CTA banner -->
    <section class="fcta-banner" aria-label="Saiba mais">
      <div class="container fcta-banner__inner fcta-banner__inner--center">
        <p class="fcta-banner__text fcta-banner__text--center">A tecnologia certa para o seu negócio<br>completa, simples e integrada.</p>
        <a href="{% url 'contact' %}" class="fcta-banner__btn">Quero saber mais</a>
      </div>
    </section>

  </main>

  {% include 'components/footer/footer.html' %}
  {% include 'components/help_chat/help_chat.html' %}

  <script src="{% static 'js/main.js' %}"></script>
  <script src="{% static 'js/components/help_chat.js' %}"></script>
</body>
</html>
```

## Relacionados
- [[tpl-menu]]
- [[tpl-footer]]
- [[tpl-help_chat]]
