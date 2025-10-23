"""
URL configuration for UrbanDjango_19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from task1.views import *
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', info, name='Информационная страница'),
    path('games/', games, name='Игры'),  # Подключение маршрута task4: игры
    path('basket/', basket, name='Корзина'),  # Подключение маршрута task4: корзина
    path('django_sign_up/', sign_up_by_django),  # Подключение маршрутов task5
    path('menu/', get_menu, name='Главная страница'),
    path('platform/news/', index), # Подключение маршрута task1 из Modul_19: вкладка с пагинацией
]
