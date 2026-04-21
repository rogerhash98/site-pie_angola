---
title: Template · pingwin_bo
drawer: produtos
source: templates/products/pingwin_bo.html
updated: 2026-04-21T01:50:49
tags: [template, html]
---
# Template · pingwin_bo

Ficheiro: `templates/products/pingwin_bo.html` (5.9 KB)

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
  <title>PingWin BO | PIE Angola</title>
  <meta name="description" content="PingWin BO — backoffice multiempresa, multiloja e multi sistema fiscal para gestão centralizada de restaurantes e lojas em Angola.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Cabin:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/menu.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/help_chat.css' %}" />
</head>
<body class="product-page">
  {% include 'components/menu/menu.html' %}

  <main>
    <section class="page-hero product-hero">
      <div class="container product-hero__grid">
        <div class="product-hero__content">
          <div class="about-eyebrow"><span></span>Produto</div>
          <h1>PingWin BO</h1>
          <p>O backoffice multiempresa, multiloja e multi sistema fiscal para gestão centralizada de stocks, compras e preços em Angola. Funciona totalmente de forma local, sem dependência de internet.</p>
          <div class="hero__actions">
            <a href="{% url 'contact' %}" class="btn btn-red">Pedir Demonstração</a>
            <a href="{% url 'contact' %}" class="btn btn-soft">Falar com um especialista</a>
          </div>
        </div>
        <div class="product-hero__image">
          <img src="{% static 'images/product-pingwinfo-home21-4ca840.png' %}" alt="PingWin BO">
        </div>
      </div>
    </section>

    <section class="section product-overview">
      <div class="container">
        <div class="about-eyebrow about-eyebrow--dark"><span></span>Visão Geral</div>
        <h2>O que é o PingWin BO?</h2>
        <div class="product-overview__grid">
          <div class="product-overview__text">
            <p>O <strong>PingWin BO</strong> é a solução de backoffice de gestão desenvolvida pela GrupoPIE para empresas e cadeias com múltiplos estabelecimentos. Ideal para franchisings, cadeias de restauração e redes de lojas em Angola.</p>
            <p>Com operação <strong>totalmente local</strong>, o PingWin BO não depende de ligação à internet para funcionar, tornando-o ideal para o mercado angolano onde a conectividade pode ser variável. Toda a informação é gerida e armazenada localmente, com sincronização quando disponível.</p>
          </div>
          <div class="product-overview__highlights">
            <div class="product-highlight">
              <strong>Multi-loja</strong>
              <span>gestão centralizada</span>
            </div>
            <div class="product-highlight">
              <strong>Offline</strong>
              <span>funciona sem internet</span>
            </div>
            <div class="product-highlight">
              <strong>Multi-fiscal</strong>
              <span>conformidade AGT Angola</span>
            </div>
            <div class="product-highlight">
              <strong>Multi-empresa</strong>
              <span>gerir vários CNPJ</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section product-features">
      <div class="container">
        <h2>Funcionalidades principais</h2>
        <div class="features-grid">
          <article class="feature-card">
            <h3>Gestão de Stocks</h3>
            <p>Controlo de stocks em tempo real por loja, com alertas de stock mínimo e histórico completo de movimentos.</p>
          </article>
          <article class="feature-card">
            <h3>Central de Compras</h3>
            <p>Centralização das compras de toda a cadeia, com gestão de fornecedores e otimização de custos.</p>
          </article>
          <article class="feature-card">
            <h3>Gestão de Preços</h3>
            <p>Definição e atualização centralizada de preços e promoções em todas as lojas simultaneamente.</p>
          </article>
          <article class="feature-card">
            <h3>Relatórios Consolidados</h3>
            <p>Relatórios de vendas, stocks e compras consolidados para toda a rede ou por estabelecimento.</p>
          </article>
          <article class="feature-card">
            <h3>Integração WinRest</h3>
            <p>Integração nativa com o WinRest NX Angola para sincronização automática de dados de ponto de venda.</p>
          </article>
          <article class="feature-card">
            <h3>Operação Local</h3>
            <p>Funciona completamente offline, sem necessidade de internet. Dados armazenados localmente com segurança.</p>
          </article>
          <article class="feature-card">
            <h3>Multi-empresa</h3>
            <p>Gira múltiplas empresas e CNPJ a partir de uma única instância do backoffice.</p>
          </article>
          <article class="feature-card">
            <h3>Controlo de Produções</h3>
            <p>Fichas técnicas, controlo de produções e cálculo automático de custos de produto acabado.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section cta">
      <div class="overlay"></div>
      <div class="container cta__inner">
        <h2>Gira toda a sua cadeia de restauração em Angola a partir de um único backoffice.</h2>
        <a href="{% url 'contact' %}" class="btn btn-light">Agendar demonstração gratuita</a>
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
