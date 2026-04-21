---
title: Template · footer
drawer: componentes
source: templates/components/footer/footer.html
updated: 2026-04-21T01:50:49
tags: [template, html]
---
# Template · footer

Ficheiro: `templates/components/footer/footer.html` (6.6 KB)

## Conteúdo

```html
{% load static %}
<footer class="pie-footer">
  <div class="pie-footer__inner container">
    <!-- top header: logo | contacts | CTA button -->
    <div class="pie-footer__header">
      <a href="{% url 'home' %}" class="pie-footer__logo-link">
        <img src="{% static 'images/pie-diamond.png' %}" alt="" class="pie-footer__logo-diamond" />
        <img src="{% static 'images/footer-logo.png' %}" alt="GrupoPIE Portugal SA" class="pie-footer__logo-text" />
      </a>
      <div class="pie-footer__contact-cols">
        <div class="pie-footer__contact-col">
          <svg class="pie-footer__contact-icon" width="22" height="22" fill="none" viewBox="0 0 22 22">
            <path d="M4.25 2A2 2 0 0 0 2.5 3.07L1.75 6.5C1.75 13.4 7.6 19 14.5 19l3.43-.75A2 2 0 0 0 19.5 16.5l-1-3.5a2 2 0 0 0-1.9-1.45l-2 .5a1 1 0 0 1-.99-.25l-2.4-2.4a1 1 0 0 1-.25-.99l.5-2A2 2 0 0 0 9.5 4.5l-3.5-1A2 2 0 0 0 4.25 2Z" stroke="#37393F" stroke-width="1.4"/>
          </svg>
          <div class="pie-footer__contact-info">
            <span class="pie-footer__contact-label">Contactos</span>
            <a href="tel:+351252290600" class="pie-footer__contact-phone">(+351) 252 290 600</a>
            <span class="pie-footer__contact-small">chamada para a rede fixa nacional</span>
          </div>
        </div>
        <div class="pie-footer__contact-col">
          <svg class="pie-footer__contact-icon" width="22" height="22" fill="none" viewBox="0 0 22 22">
            <rect x="2" y="4" width="18" height="14" rx="2" stroke="#37393F" stroke-width="1.4"/>
            <path d="M2 7l9 6 9-6" stroke="#37393F" stroke-width="1.4" stroke-linejoin="round"/>
          </svg>
          <div class="pie-footer__contact-info">
            <span class="pie-footer__contact-label">Email</span>
            <a href="mailto:geral@grupopie.com" class="pie-footer__contact-email">geral@grupopie.com</a>
            <a href="mailto:comercial@grupopie.com" class="pie-footer__contact-email">comercial@grupopie.com</a>
          </div>
        </div>
      </div>
      <a href="{% url 'contact' %}" class="pie-footer__cta-btn">Pedido de Contacto</a>
    </div>

    <hr class="pie-footer__divider" />

    <!-- menus -->
    <div class="pie-footer__menus">
      <div class="pie-footer__col">
        <h4 class="pie-footer__col-title">GrupoPIE</h4>
        <a href="{% url 'about' %}" class="pie-footer__link">Sobre nós</a>
        <a href="{% url 'clients' %}" class="pie-footer__link">Clientes</a>
        <a href="#" class="pie-footer__link">Parceiros</a>
        <a href="{% url 'recruitment' %}" class="pie-footer__link">Recrutamento</a>
        <a href="{% url 'contact' %}" class="pie-footer__link">Contactos</a>
      </div>
      <div class="pie-footer__col">
        <h4 class="pie-footer__col-title">Soluções</h4>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Restauração</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Retalho</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Eventos</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Hotelaria</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Gestão Comercial</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Fidelização</a>
      </div>
      <div class="pie-footer__col">
        <h4 class="pie-footer__col-title">Produtos</h4>
        <a href="{% url 'product_winrest_nx' %}" class="pie-footer__link">WinRest</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Booking All</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">PingWin FO</a>
        <a href="{% url 'product_pingwin_bo' %}" class="pie-footer__link">PingWin BO</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">PingWin MBA</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">myClient</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">360City</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">360City FUN</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Kiosk digital</a>
        <a href="{% url 'solutions' %}" class="pie-footer__link">Apps Verticais</a>
      </div>
      <div class="pie-footer__col pie-footer__col--social">
        <h4 class="pie-footer__col-title">Siga-nos</h4>
        <div class="pie-footer__socials">
          <a href="https://www.facebook.com/grupopie" target="_blank" rel="noopener" class="pie-footer__social-icon pie-footer__social-icon--fb" aria-label="Facebook">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3V2Z" fill="#37393F"/></svg>
          </a>
          <a href="https://www.instagram.com/grupopie" target="_blank" rel="noopener" class="pie-footer__social-icon pie-footer__social-icon--ig" aria-label="Instagram">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><rect x="2" y="2" width="20" height="20" rx="5" stroke="#37393F" stroke-width="2"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37Z" stroke="#37393F" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.5" fill="#37393F"/></svg>
          </a>
          <a href="https://www.youtube.com/grupopie" target="_blank" rel="noopener" class="pie-footer__social-icon pie-footer__social-icon--yt" aria-label="YouTube">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M22.54 6.42A2.78 2.78 0 0 0 20.59 4.45C18.88 4 12 4 12 4S5.12 4 3.41 4.46A2.78 2.78 0 0 0 1.46 6.42 29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.41 19.1C5.12 19.56 12 19.56 12 19.56s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.95-1.97A29 29 0 0 0 23 11.75a29 29 0 0 0-.46-5.33Z" fill="#37393F"/><polygon points="9.75,15.02 15.5,11.75 9.75,8.48" fill="#F7F7F7"/></svg>
          </a>
          <a href="https://www.linkedin.com/company/grupopie" target="_blank" rel="noopener" class="pie-footer__social-icon pie-footer__social-icon--li" aria-label="LinkedIn">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6Z" fill="#37393F"/><rect x="2" y="9" width="4" height="12" fill="#37393F"/><circle cx="4" cy="4" r="2" fill="#37393F"/></svg>
          </a>
        </div>
      </div>
    </div>

    <hr class="pie-footer__divider" />

    <!-- copyright -->
    <div class="pie-footer__bottom">
      <p class="pie-footer__copy">© Copyright 2025 GrupoPIE Portugal SA. Todos os direitos reservados. <a href="#" class="pie-footer__copy-link">Política de Privacidade</a> · <a href="#" class="pie-footer__copy-link">Termos e Condições</a></p>
    </div>
  </div>
</footer>
```
