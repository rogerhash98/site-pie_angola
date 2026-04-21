---
title: Template · home
drawer: templates
source: templates/home.html
updated: 2026-04-21T01:50:49
tags: [template, html]
---
# Template · home

Ficheiro: `templates/home.html` (14.6 KB)

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
  <title>GrupoPIE — Software líder em restauração e gestão</title>
  <meta name="description" content="GrupoPIE — Software de faturação e gestão para restaurantes, fast food e comércio. WinRest, PingWin, Booking All e muito mais.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Cabin:wght@600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  <link rel="stylesheet" href="{% static 'css/home.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/menu.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/help_chat.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/help_chat.css' %}" />
</head>
<body>
  {% include 'components/menu/menu.html' %}

  <!-- 1. HERO CAROUSEL -->
  <section class="pie-hero-carousel" aria-roledescription="carousel" aria-label="Soluções em destaque">
    <div class="pie-hero-carousel__viewport">
      <div class="pie-hero-carousel__track" data-track>

        <article class="pie-hero pie-hero--winrest is-active" data-slide aria-roledescription="slide" aria-label="1 de 2">
          <div class="pie-hero__overlay"></div>
          <div class="pie-hero__content container">
            <p class="pie-hero__sub">+31.000 restaurantes escolhem WinRest</p>
            <h1 class="pie-hero__title">O software escolhido pelas marcas líderes da restauração</h1>
            <p class="pie-hero__subtitle">Faturação, pedidos, pagamentos e controlo operacional num único sistema.</p>
            <a href="{% url 'product_winrest_nx' %}" class="pie-hero__btn">Explorar soluções WinRest</a>
          </div>
        </article>

        <article class="pie-hero pie-hero--fun" data-slide aria-roledescription="slide" aria-label="2 de 2" hidden>
          <div class="pie-hero__overlay"></div>
          <div class="pie-hero__content container">
            <p class="pie-hero__sub">Controlo total de acessos · 360City FUN</p>
            <h1 class="pie-hero__title">A solução cashless que transforma festivais e eventos</h1>
            <p class="pie-hero__subtitle">Tudo o que precisa para eventos rápidos, seguros e sem dinheiro.</p>
            <a href="{% url 'solutions' %}" class="pie-hero__btn">Explorar soluções 360City FUN</a>
          </div>
        </article>

      </div>
    </div>

    <div class="pie-hero-carousel__dots" role="tablist" aria-label="Selecionar slide">
      <button type="button" class="pie-hero-carousel__dot is-active" data-dot="0" role="tab" aria-selected="true" aria-label="Ir para slide 1"></button>
      <button type="button" class="pie-hero-carousel__dot" data-dot="1" role="tab" aria-selected="false" aria-label="Ir para slide 2"></button>
    </div>
  </section>

  <script>
    (function () {
      var root = document.querySelector('.pie-hero-carousel');
      if (!root) return;
      var slides = root.querySelectorAll('[data-slide]');
      var dots = root.querySelectorAll('[data-dot]');
      var current = 0;
      var timer = null;
      var INTERVAL = 6000;

      function show(idx) {
        idx = ((idx % slides.length) + slides.length) % slides.length;
        slides.forEach(function (s, i) {
          var active = i === idx;
          s.classList.toggle('is-active', active);
          if (active) { s.removeAttribute('hidden'); }
          else { s.setAttribute('hidden', ''); }
        });
        dots.forEach(function (d, i) {
          var active = i === idx;
          d.classList.toggle('is-active', active);
          d.setAttribute('aria-selected', active ? 'true' : 'false');
        });
        current = idx;
      }

      function start() { stop(); timer = setInterval(function () { show(current + 1); }, INTERVAL); }
      function stop() { if (timer) { clearInterval(timer); timer = null; } }

      dots.forEach(function (d, i) {
        d.addEventListener('click', function () { show(i); start(); });
      });

      root.addEventListener('mouseenter', stop);
      root.addEventListener('mouseleave', start);

      start();
    })();
  </script>

  <!-- 2. SOLUÇÕES -->
  <section class="pie-sol">
    <div class="container">
      <h2 class="pie-sec-title">As soluções certas para cada tipo de negócio</h2>
      <div class="pie-sol__grid">
        <div class="pie-sol__card">
          <img src="{% static 'images/sol-restauracao.svg' %}" alt="" class="pie-sol__icon" />
          <h3 class="pie-sol__name">Restauração &amp; Similares</h3>
          <p class="pie-sol__desc">Solução completa para gestão e faturação</p>
        </div>
        <div class="pie-sol__card">
          <img src="{% static 'images/sol-comercio.svg' %}" alt="" class="pie-sol__icon" />
          <h3 class="pie-sol__name">Comércio &amp; Serviços</h3>
          <p class="pie-sol__desc">Software adaptado ao retalho e serviços</p>
        </div>
        <div class="pie-sol__card">
          <img src="{% static 'images/sol-gestao.svg' %}" alt="" class="pie-sol__icon" />
          <h3 class="pie-sol__name">Gestão Comercial</h3>
          <p class="pie-sol__desc">Controlo do negócio<br>em tempo real</p>
        </div>
        <div class="pie-sol__card">
          <img src="{% static 'images/sol-agregador.svg' %}" alt="" class="pie-sol__icon" />
          <h3 class="pie-sol__name">Agregador de Entregas</h3>
          <p class="pie-sol__desc">Pedidos online centralizados num só lugar</p>
        </div>
        <div class="pie-sol__card">
          <img src="{% static 'images/sol-fidelizacao.svg' %}" alt="" class="pie-sol__icon" />
          <h3 class="pie-sol__name">Fidelização de Clientes</h3>
          <p class="pie-sol__desc">Programas que aumentam retenção e vendas</p>
        </div>
        <div class="pie-sol__card">
          <img src="{% static 'images/sol-faturacao.svg' %}" alt="" class="pie-sol__icon" />
          <h3 class="pie-sol__name">Faturação em Mobilidade</h3>
          <p class="pie-sol__desc">Faturação rápida e ágil<br>no PDA</p>
        </div>
        <div class="pie-sol__card">
          <img src="{% static 'images/sol-digitalizacao.svg' %}" alt="" class="pie-sol__icon" />
          <h3 class="pie-sol__name">Digitalização no Atendimento</h3>
          <p class="pie-sol__desc">Pedidos e pagamentos feitos pelo cliente</p>
        </div>
        <div class="pie-sol__card">
          <img src="{% static 'images/sol-cashless.svg' %}" alt="" class="pie-sol__icon" />
          <h3 class="pie-sol__name">Sistema Cashless para Eventos</h3>
          <p class="pie-sol__desc">Pagamentos e consumos totalmente digitais</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 3. PRODUTOS -->
  <section class="pie-prod">
    <div class="container">
      <h2 class="pie-sec-title">Produtos especializados para cada tipo de operação</h2>
    </div>
    <div class="pie-prod__scroll-outer">
      <div class="pie-prod__track">
        <div class="pie-prod__card">
          <div class="pie-prod__img-wrap">
            <img src="{% static 'images/prod-winrest.png' %}" alt="WinRest" class="pie-prod__img" />
          </div>
          <div class="pie-prod__body">
            <h3 class="pie-prod__name">WinRest</h3>
            <p class="pie-prod__sub">O POS mais completo para restauração</p>
            <p class="pie-prod__desc">Faturação, gestão, pedidos, pagamentos e relatórios - totalmente integrado</p>
            <a href="{% url 'product_winrest_nx' %}" class="pie-prod__link">Saber mais</a>
          </div>
        </div>
        <div class="pie-prod__card">
          <div class="pie-prod__img-wrap">
            <img src="{% static 'images/prod-bookingall.png' %}" alt="Booking All" class="pie-prod__img" />
          </div>
          <div class="pie-prod__body">
            <h3 class="pie-prod__name">Booking All</h3>
            <p class="pie-prod__sub">Pedidos take-away e delivery no POS</p>
            <p class="pie-prod__desc">Receba, organize e centralize pedidos de todas as plataformas</p>
            <a href="{% url 'solutions' %}" class="pie-prod__link">Saber mais</a>
          </div>
        </div>
        <div class="pie-prod__card">
          <div class="pie-prod__img-wrap">
            <img src="{% static 'images/prod-360fun.png' %}" alt="360City FUN" class="pie-prod__img" />
          </div>
          <div class="pie-prod__body">
            <h3 class="pie-prod__name">360City FUN</h3>
            <p class="pie-prod__sub">Pagamentos cashless para eventos</p>
            <p class="pie-prod__desc">Pagamentos, acessos e consumos - tudo digital e simplificado.</p>
            <a href="{% url 'solutions' %}" class="pie-prod__link">Saber mais</a>
          </div>
        </div>
        <div class="pie-prod__card">
          <div class="pie-prod__img-wrap">
            <img src="{% static 'images/prod-pingwinmba.png' %}" alt="PingWin MBA" class="pie-prod__img" />
          </div>
          <div class="pie-prod__body">
            <h3 class="pie-prod__name">PingWin MBA</h3>
            <p class="pie-prod__sub">Faturação e gestão simples e completa</p>
            <p class="pie-prod__desc">Dashboard, documentos e controlo administrativo num só sistema</p>
            <a href="{% url 'solutions' %}" class="pie-prod__link">Saber mais</a>
          </div>
        </div>
        <div class="pie-prod__card">
          <div class="pie-prod__img-wrap">
            <img src="{% static 'images/prod-pingwin.png' %}" alt="PingWin" class="pie-prod__img" />
          </div>
          <div class="pie-prod__body">
            <h3 class="pie-prod__name">PingWin</h3>
            <p class="pie-prod__sub">Gestão para comércio e retalho</p>
            <p class="pie-prod__desc">Ideal para lojas, pastelarias, papelarias e outros negócios especializados.</p>
            <a href="{% url 'product_pingwin_bo' %}" class="pie-prod__link">Saber mais</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. CLIENTES -->
  <section class="pie-clients">
    <div class="container">
      <h2 class="pie-sec-title">+31.000 empresas confiam nas nossas soluções</h2>
      <div class="pie-clients__logos">
        <img src="{% static 'images/client-logo-1.png' %}" alt="Cliente 1" />
        <img src="{% static 'images/client-logo-2.png' %}" alt="Cliente 2" />
        <img src="{% static 'images/client-logo-3.png' %}" alt="Cliente 3" />
        <img src="{% static 'images/client-logo-4.png' %}" alt="Cliente 4" />
        <img src="{% static 'images/client-logo-5.png' %}" alt="Cliente 5" />
        <img src="{% static 'images/client-logo-6.png' %}" alt="Cliente 6" />
        <img src="{% static 'images/client-logo-7.png' %}" alt="Cliente 7" />
        <img src="{% static 'images/client-logo-8.png' %}" alt="Cliente 8" />
        <img src="{% static 'images/client-logo-9.png' %}" alt="Cliente 9" />
      </div>
    </div>
  </section>

  <!-- 5. CTA -->
  <section class="pie-cta">
    <div class="pie-cta__overlay"></div>
    <div class="pie-cta__content container">
      <h2 class="pie-cta__title">A tecnologia certa para o seu negócio<br>completa, simples e integrada.</h2>
      <a href="{% url 'contact' %}" class="pie-cta__btn">Quero saber mais</a>
    </div>
  </section>

  <!-- 6. ESTATÍSTICAS -->
  <section class="pie-stats">
    <div class="container">
      <h2 class="pie-sec-title">Números que traduzem o nosso sucesso</h2>
      <div class="pie-stats__grid">
        <div class="pie-stats__item">
          <img src="{% static 'images/stats-icon-globe.svg' %}" alt="" class="pie-stats__icon" />
          <span class="pie-stats__num">+15</span>
          <span class="pie-stats__label">Países</span>
        </div>
        <div class="pie-stats__item">
          <img src="{% static 'images/stats-icon-units.svg' %}" alt="" class="pie-stats__icon" />
          <span class="pie-stats__num">+31.000</span>
          <span class="pie-stats__label">unidades ativas</span>
        </div>
        <div class="pie-stats__item">
          <img src="{% static 'images/stats-icon-pos.svg' %}" alt="" class="pie-stats__icon" />
          <span class="pie-stats__num">+60.000</span>
          <span class="pie-stats__label">instalações POS</span>
        </div>
        <div class="pie-stats__item">
          <img src="{% static 'images/stats-icon-tickets.svg' %}" alt="" class="pie-stats__icon" />
          <span class="pie-stats__num">+10 Milhões</span>
          <span class="pie-stats__label">de tickets/dia</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 7. NOVIDADES -->
  <section class="pie-news">
    <div class="container">
      <h2 class="pie-sec-title">Mantenha-se atualizado</h2>
      <div class="pie-news__grid">
        <article class="pie-news__card">
          <div class="pie-news__img-wrap">
            <img src="{% static 'images/news-1.png' %}" alt="Booking All" class="pie-news__img" />
          </div>
          <div class="pie-news__body">
            <h3 class="pie-news__title">Booking All - Pedidos integrados</h3>
            <p class="pie-news__desc">Solução completa e única para a integração de plataformas de delivery e gestão de entregas.</p>
            <a href="#" class="pie-news__link">Ler mais</a>
          </div>
        </article>
        <article class="pie-news__card">
          <div class="pie-news__img-wrap">
            <img src="{% static 'images/news-2.png' %}" alt="Backoffice" class="pie-news__img" />
          </div>
          <div class="pie-news__body">
            <h3 class="pie-news__title">Backoffice de Gestão</h3>
            <p class="pie-news__desc">Gestão do negócio de forma segura e com ferramentas para tomar as decisões.</p>
            <a href="#" class="pie-news__link">Ler mais</a>
          </div>
        </article>
        <article class="pie-news__card">
          <div class="pie-news__img-wrap">
            <img src="{% static 'images/news-3.png' %}" alt="Backoffice" class="pie-news__img" />
          </div>
          <div class="pie-news__body">
            <h3 class="pie-news__title">Backoffice de Gestão</h3>
            <p class="pie-news__desc">Gestão do negócio de forma segura e com ferramentas para tomar as decisões.</p>
            <a href="#" class="pie-news__link">Ler mais</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  {% include 'components/footer/footer.html' %}
  {% include 'components/help_chat/help_chat.html' %}
  <script src="{% static 'js/components/help_chat.js' %}"></script>
</body>
</html>
```

## Relacionados
- [[tpl-menu]]
- [[tpl-footer]]
- [[tpl-help_chat]]
