# Домашнее задание по теме "MVT. Вывод объектов в
# шаблоны".
# Цель: закрепить навыки создания представлений, шаблонов и
# вызовов QuerySet запросов. Понять как работают эти инструменты
# вместе (паттерн MVT).
# Задача "Время объединять".

# Из Modul_18 task4 views

from django.shortcuts import render, get_object_or_404, redirect
from task1.models import Game, Buyer, News, Review
from task1.forms import UserRegister, ReviewForm
from django.db import models
from decimal import Decimal
from django.core.paginator import Paginator
# ----
from rest_framework.response import Response
from rest_framework.decorators import api_view
from task1.serializers import BuyerSerializer, GameSerializer, ReviewSerializer

# ----

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


# ------------------------------
# Домашнее задание по теме "Пагинация": добавить новую вкладку с
# пагинацией в главном меню.
def index(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'six_task/news.html', {'page_obj': page_obj})


# ---- Представления для API
@api_view(['GET'])
def buyer_list_api(request):
    buyers = Buyer.objects.all()
    serializer = BuyerSerializer(buyers, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def game_list_api(request):
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# ---- Функция для отображения и добавления отзывов
def game_reviews(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.all()  # Получаем отзывы для игры

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game  # Связываем отзыв с игрой
            review.save()
            return redirect('game_reviews',
                            game_id=game.id)  # Перенаправляем на ту же страницу
    else:
        form = ReviewForm()

    return render(request,
              'seven_task/game_reviews.html',
              {'game': game,
               'reviews': reviews,
               'form': form})

@api_view(['GET', 'POST'])
def review_list(request, game_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(game_id=game_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
