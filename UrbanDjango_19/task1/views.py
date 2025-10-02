# Домашнее задание по теме "MVT. Вывод объектов в
# шаблоны".
# Цель: закрепить навыки создания представлений, шаблонов и
# вызовов QuerySet запросов. Понять как работают эти инструменты
# вместе (паттерн MVT).
# Задача "Время объединять".

# Из Modul_18 task4 views

from django.shortcuts import render
from task1.models import Game, Buyer
from task1.forms import UserRegister
from django.db import models
from decimal import Decimal


menu = {'Навигационная страница': ["/"], 'Магазин': ["/games/"],
         'Корзина': ["/basket/"]}

context = {}

def info(request):
    context = {'base_name': 'Модуль 19. Django в Python.',
               'base_student': 'Студентка: Укладникова Екатерина',
               'base_title': 'Навигационная страница'
               }
    return render(request, 'info/info.html', context)

def get_menu(request):
    context['base_title'] = 'Главная'
    context['menu'] = menu
    return render(request, 'fourth_task/menu.html', context)

def games(request):
    pagename = 'Игры'
    context['pagename'] = pagename
    context['base_title'] = 'Игры'
    context['menu'] = menu

    content = Game.objects.all()
    # print(game)
    # content = {'games': game}
    # # print(content)
    context['games'] = content
    # # context['description'] = game.description
    print(context)
    return render(request, 'fourth_task/games.html', context)

def basket(request):
    context['base_title'] = 'Корзина'
    context['base_basket'] = 'Извините, ваша корзина пуста'
    context['menu'] = menu
    return render(request, 'fourth_task/basket.html', context)

def sign_up_by_django(request):
    context = {}
    form = UserRegister(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Обработка данных формы:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            set_user = Buyer.objects.values_list('name', flat=True)

            context["username"] = username
            context["password"] = password
            context["repeat_password"] = repeat_password
            context["age"] = age
            if username in set_user:
                context['message'] = f'Пользователь {username} уже зарегистрирован в системе'
                print(f"Пользователь {username} уже зарегистрирован в системе")
            elif password != repeat_password:
                context['message'] = 'Пароли не совпадают'
                print("Пароли не совпадают.")
            elif age <= 17:
                context['message'] = "Вы должны быть старше 18."
                print(f"Ваш возраст {age}, вы должны быть старше 18.")
            else:
                Buyer.objects.create(name=username, age=age, balance=1000)
                context['message'] = f'Пользователь {username} успешно зарегистрирован!'

        context['form'] = form
    return render(request, 'fifth_task/registration_page.html', context)


