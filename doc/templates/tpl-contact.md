---
title: Template · contact
drawer: templates
source: templates/contact.html
updated: 2026-04-21T01:50:49
tags: [template, html]
---
# Template · contact

Ficheiro: `templates/contact.html` (7.4 KB)

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
  <title>Contactos | PIE Angola</title>
  <meta name="description" content="Entre em contacto com a equipa PIE Angola. Estamos em Luanda, Bairro Militar, Município de Belas.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Cabin:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/menu.css' %}" />
  <link rel="stylesheet" href="{% static 'css/components/help_chat.css' %}" />
</head>
<body class="contact-page">
  {% include 'components/menu/menu.html' %}

  <main>

    <!-- ══════════════════════════════════════
         HERO — Fale connosco
    ══════════════════════════════════════ -->
    <section class="contact-hero" aria-label="Contactos">
      <div class="contact-hero__bg"></div>
      <div class="container contact-hero__inner">
        <div class="contact-hero__content">
          <nav class="contact-breadcrumb" aria-label="Breadcrumb">
            <span class="contact-breadcrumb__dot" aria-hidden="true"></span>
            <a href="{% url 'home' %}">O GrupoPIE</a>
            <span class="contact-breadcrumb__sep" aria-hidden="true">|</span>
            <strong>Contactos</strong>
          </nav>
          <h1>Fale connosco</h1>
          <p>Estamos disponíveis para esclarecer dúvidas e encontrar a melhor solução para o seu negócio</p>
        </div>
        <div class="contact-hero__image-wrap" aria-hidden="true">
          <img src="{% static 'images/components/contact-hero-phone.jpg' %}" alt="" class="contact-hero__image" />
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════
         OFFICES — Escritórios
    ══════════════════════════════════════ -->
    <section class="offices-section" aria-labelledby="offices-heading">
      <div class="container offices-grid">

        <div class="office-card">
          <h3 class="office-card__title">Lisboa</h3>
          <address class="office-card__address">
            Rua das Marinhas do Tejo, nº121<br>
            2690-370 Santa Iria de Azóia
          </address>
          <div class="office-card__map">
            <iframe
              src="https://www.google.com/maps?q=Rua+das+Marinhas+do+Tejo+121,+Santa+Iria+de+Azoia,+Portugal&output=embed"
              width="100%" height="224" style="border:0;" allowfullscreen="" loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              title="GrupoPIE — Lisboa, Santa Iria de Azóia"></iframe>
          </div>
        </div>

        <div class="office-card">
          <h3 class="office-card__title">Póvoa de Varzim <span class="office-card__title-suffix">(Sede)</span></h3>
          <address class="office-card__address">
            Edifício GrupoPIE<br>
            Rua Artur Aires, 100<br>
            4490-144 Póvoa de Varzim
          </address>
          <div class="office-card__map">
            <iframe
              src="https://www.google.com/maps?q=Rua+Artur+Aires+100,+Povoa+de+Varzim,+Portugal&output=embed"
              width="100%" height="224" style="border:0;" allowfullscreen="" loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              title="GrupoPIE — Sede, Póvoa de Varzim"></iframe>
          </div>
        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════
         FORM — Envie-nos uma mensagem
    ══════════════════════════════════════ -->
    <section class="cform-section" aria-labelledby="cform-heading">
      <div class="container">

        <div class="cform-header">
          <h2 id="cform-heading">Envie-nos uma mensagem</h2>
          <p>Respondemos com a maior brevidade possível</p>
        </div>

        {% if error %}
          <div class="form-error cform-error" role="alert">{{ error }}</div>
        {% endif %}

        <form class="cform" method="POST" action="{% url 'contact' %}" novalidate>
          {% csrf_token %}

          <div class="cform__grid">

            <div class="cform__cell">
              <input type="text" name="name" id="name" placeholder="Nome"
                value="{{ form_data.name|default:'' }}" required>
            </div>
            <div class="cform__cell">
              <input type="text" name="company" id="company" placeholder="Empresa"
                value="{{ form_data.company|default:'' }}">
            </div>

            <div class="cform__cell">
              <input type="tel" name="phone" id="phone" placeholder="Telefone/telemóvel"
                value="{{ form_data.phone|default:'' }}">
            </div>
            <div class="cform__cell">
              <input type="email" name="email" id="email" placeholder="Email"
                value="{{ form_data.email|default:'' }}" required>
            </div>

            <div class="cform__cell">
              <input type="text" name="subject" id="subject" placeholder="Assunto"
                value="{{ form_data.subject|default:'' }}">
            </div>
            <div class="cform__cell">
              <select name="area" id="area">
                <option value="" disabled {% if not form_data.area %}selected{% endif %}>Área de interesse</option>
                <option value="winrest-nx" {% if form_data.area == 'winrest-nx' %}selected{% endif %}>WinRest NX Angola</option>
                <option value="pingwin-bo" {% if form_data.area == 'pingwin-bo' %}selected{% endif %}>PingWin BO</option>
                <option value="winrest-360" {% if form_data.area == 'winrest-360' %}selected{% endif %}>WinRest 360</option>
                <option value="demo" {% if form_data.area == 'demo' %}selected{% endif %}>Pedido de demonstração</option>
                <option value="outro" {% if form_data.area == 'outro' %}selected{% endif %}>Outro</option>
              </select>
            </div>

            <div class="cform__cell cform__cell--full">
              <textarea name="message" id="message" rows="5" placeholder="Mensagem" required>{{ form_data.message|default:'' }}</textarea>
            </div>

          </div><!-- /.cform__grid -->

          <div class="cform__footer">
            <label class="cform__privacy">
              <input type="checkbox" name="privacy" required>
              <span>Li e aceito a <a href="/politica-de-privacidade/">Política de Privacidade</a></span>
            </label>
            <button type="submit" class="cform__submit">Enviar mensagem</button>
          </div>

        </form>

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
