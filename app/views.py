from django.core.mail import send_mail
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'home.html', {'active_menu': 'solutions'})


def about(request):
    return render(request, 'about.html', {'active_menu': 'about'})


def solutions(request):
    return render(request, 'solutions.html', {'active_menu': 'solutions'})


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


def contact_success(request):
    return render(request, 'contact_success.html', {'active_menu': 'contact'})


def clients(request):
    return render(request, 'clients.html', {'active_menu': 'clients'})


def success_cases(request):
    return render(request, 'success_cases.html', {'active_menu': 'success_cases'})


def product_winrest_nx(request):
    return render(request, 'products/winrest_nx.html', {'active_menu': 'solutions'})


def product_pingwin_bo(request):
    return render(request, 'products/pingwin_bo.html', {'active_menu': 'solutions'})
