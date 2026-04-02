from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'active_menu': 'solutions'})


def about(request):
    return render(request, 'about.html', {'active_menu': 'about'})
