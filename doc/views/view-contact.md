---
title: View · contact
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · contact

Função `contact` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        company = request.POST.get('company', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        area = request.POST.get('area', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            try:
                body_lines = [
                    f'Nome: {name}',
                    f'Empresa: {company}',
                    f'Email: {email}',
                    f'Telefone: {phone}',
                ]
                if subject:
                    body_lines.append(f'Assunto: {subject}')
                if area:
                    body_lines.append(f'Área de interesse: {area}')
                body_lines += ['', 'Mensagem:', message]
                send_mail(
                    subject=f'[PIE Angola] Contacto de {name} — {company or "sem empresa"}',
                    message='\n'.join(body_lines),
                    from_email='noreply@pieangola.com',
                    recipient_list=['info@pieangola.com'],
                    fail_silently=True,
                )
            except Exception:
                pass
            return redirect('contact_success')

        return render(request, 'contact.html', {
            'active_menu': 'contact',
            'error': 'Por favor preencha todos os campos obrigatórios.',
            'form_data': {
                'name': name, 'company': company, 'email': email,
                'phone': phone, 'subject': subject, 'area': area, 'message': message,
            },
        })

    return render(request, 'contact.html', {'active_menu': 'contact'})
```
