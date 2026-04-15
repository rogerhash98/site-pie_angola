"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import (
    about,
    clients,
    contact,
    contact_success,
    home,
    product_pingwin_bo,
    product_winrest_nx,
    solutions,
    success_cases,
)

urlpatterns = [
    path('', home, name='home'),
    path('sobre-nos/', about, name='about'),
    path('solucoes/', solutions, name='solutions'),
    path('contacto/', contact, name='contact'),
    path('clientes/', clients, name='clients'),
    path('casos-de-sucesso/', success_cases, name='success_cases'),
    path('produtos/winrest-nx/', product_winrest_nx, name='product_winrest_nx'),
    path('contacto/obrigado/', contact_success, name='contact_success'),
    path('produtos/pingwin-bo/', product_pingwin_bo, name='product_pingwin_bo'),
    path('admin/', admin.site.urls),
]
