---
title: Template · help_chat
drawer: componentes
source: templates/components/help_chat/help_chat.html
updated: 2026-04-21T01:50:49
tags: [template, html]
---
# Template · help_chat

Ficheiro: `templates/components/help_chat/help_chat.html` (5.1 KB)

## Conteúdo

```html
{% load static %}
<!-- ══════════════════════════════════════
     Floating Help / Chat widget
     (Figma 14:756 button + 14:2028 chat)
══════════════════════════════════════ -->
<div class="help-chat" id="helpChat" aria-live="polite">

  <!-- Chat panel (initially hidden) -->
  <div class="help-chat__panel" id="helpChatPanel" role="dialog"
       aria-label="Fale connosco" aria-modal="false" hidden>

    <header class="help-chat__header">
      <img src="{% static 'images/menu-logo.svg' %}" alt="GrupoPIE" class="help-chat__logo" />
      <button type="button" class="help-chat__hbtn" aria-label="Abrir noutra janela">
        <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="#fff" stroke-width="1.6"><path d="M5 11l6-6M6 5h5v5"/></svg>
      </button>
      <button type="button" class="help-chat__hbtn help-chat__close" aria-label="Fechar" data-help-chat-close>
        <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="#fff" stroke-width="1.8"><path d="M3 8h10"/></svg>
      </button>
    </header>

    <div class="help-chat__intro">
      <span class="help-chat__avatar" aria-hidden="true">
        <img src="{% static 'images/menu-logo.svg' %}" alt="" />
      </span>
      <div class="help-chat__intro-text">
        <strong>Fale Connosco!</strong>
        <span>Normalmente respondemos em poucos minutos.</span>
      </div>
    </div>

    <div class="help-chat__body" id="helpChatBody">
      <p class="help-chat__sep"><span>Chat iniciado</span></p>

      <div class="help-chat__msg help-chat__msg--in">
        <span class="help-chat__avatar help-chat__avatar--sm" aria-hidden="true">
          <img src="{% static 'images/menu-logo.svg' %}" alt="" />
        </span>
        <div class="help-chat__bubble">Em que podemos ajudar?</div>
      </div>
    </div>

    <form class="help-chat__form" id="helpChatForm" autocomplete="off">
      <div class="help-chat__input-wrap">
        <input type="text" class="help-chat__input" id="helpChatInput"
               placeholder="Escreva aqui uma mensagem ..." aria-label="Escreva aqui uma mensagem" />
        <button type="submit" class="help-chat__send" aria-label="Enviar">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#9ea0a5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/></svg>
        </button>
      </div>
      <div class="help-chat__bottom">
        <button type="button" class="help-chat__icon-btn" aria-label="Anexar ficheiro">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#9ea0a5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>
        </button>
        <button type="button" class="help-chat__icon-btn" aria-label="Mais opções">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="#9ea0a5"><circle cx="5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="12" r="2"/></svg>
        </button>
      </div>
    </form>

  </div>

  <!-- Floating trigger button -->
  <button type="button" class="help-chat__trigger" id="helpChatTrigger"
          aria-label="Precisa de ajuda? Abrir chat" aria-controls="helpChatPanel" aria-expanded="false">
    <svg class="help-chat__trigger-icon" viewBox="0 0 27 24" fill="#fff" aria-hidden="true">
      <path d="M11.21 16.29c-.55-.03-1.1-.07-1.66-.09-.08 0-.18.05-.25.11-1.44 1.22-3.01 2.22-4.81 2.88-.29.1-.59.16-.89.22-.27.06-.51-.03-.67-.25-.16-.22-.14-.45 0-.69.45-.73.89-1.48 1.15-2.3.1-.31.15-.63.21-.95.03-.13-.03-.21-.16-.28C1.78 13.66.5 11.67.09 9.13c-.42-2.64.59-4.74 2.64-6.43 1.58-1.3 3.44-2.06 5.46-2.43 2.68-.49 5.31-.32 7.87.62 1.72.64 3.21 1.6 4.37 3.01 2.17 2.62 1.81 6.22-.03 8.55-1.27 1.6-2.97 2.59-4.94 3.19-1.39.43-2.82.6-4.27.65zm-5.82.8c.31-.21.58-.37.82-.56.8-.63 1.58-1.27 2.37-1.91.07-.06.17-.11.26-.11.26 0 .52.02.78.05 1.93.21 3.82.07 5.66-.57 1.67-.59 3.09-1.51 4.04-2.99 1.39-2.17 1.32-4.81-.84-6.81-.91-.84-1.97-1.43-3.15-1.85-2.06-.72-4.18-.88-6.33-.57-1.72.25-3.34.8-4.75 1.81-1.92 1.38-2.91 3.16-2.44 5.53.4 2.01 1.46 3.57 3.4 4.52.22.11.44.21.66.33.06.03.13.12.12.17-.07.59-.13 1.19-.24 1.78-.07.37-.22.74-.35 1.17z"/>
      <path d="M9.64 17.96c.87 0 1.69.04 2.5 0 2.65-.16 5.16-.76 7.41-2.19 1.81-1.16 3.12-2.73 3.92-4.68.22-.54.31-1.12.48-1.74.39.28.81.55 1.18.87 1.18.99 1.76 2.26 1.86 3.74.1 1.54-.23 2.96-1.27 4.18-.61.71-1.36 1.24-2.19 1.67-.16.08-.2.16-.19.33.09 1.06.38 2.07.84 3.03.1.21.13.41-.01.61-.15.19-.36.24-.6.21-.77-.13-1.44-.47-2.08-.87-.86-.54-1.65-1.16-2.36-1.88-.1-.11-.19-.1-.32-.1-2.76.18-5.39-.19-7.69-1.82-.47-.34-.88-.76-1.31-1.15-.05-.05-.09-.11-.17-.21z"/>
      <circle cx="6.48" cy="8.31" r="1.87"/>
      <circle cx="11.4" cy="8.31" r="1.81"/>
      <circle cx="16.25" cy="8.31" r="1.81"/>
    </svg>
    <span class="help-chat__trigger-label">Precisa de Ajuda?</span>
  </button>

</div>
```
