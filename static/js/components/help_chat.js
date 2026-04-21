(function () {
  'use strict';
  const trigger = document.getElementById('helpChatTrigger');
  const panel = document.getElementById('helpChatPanel');
  const form = document.getElementById('helpChatForm');
  const input = document.getElementById('helpChatInput');
  const body = document.getElementById('helpChatBody');
  if (!trigger || !panel) return;

  function openPanel() {
    panel.hidden = false;
    trigger.setAttribute('aria-expanded', 'true');
    setTimeout(() => input && input.focus(), 50);
  }
  function closePanel() {
    panel.hidden = true;
    trigger.setAttribute('aria-expanded', 'false');
  }
  function togglePanel() {
    panel.hidden ? openPanel() : closePanel();
  }

  trigger.addEventListener('click', togglePanel);
  document.querySelectorAll('[data-help-chat-close]').forEach(btn => {
    btn.addEventListener('click', closePanel);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !panel.hidden) closePanel();
  });

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const txt = (input.value || '').trim();
      if (!txt) return;
      const msg = document.createElement('div');
      msg.className = 'help-chat__msg help-chat__msg--out';
      msg.innerHTML = '<div class="help-chat__bubble"></div>';
      msg.querySelector('.help-chat__bubble').textContent = txt;
      body.appendChild(msg);
      input.value = '';
      body.scrollTop = body.scrollHeight;
    });
  }
})();
