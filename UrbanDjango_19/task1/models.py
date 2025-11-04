# Домашнее задание по теме "Модели баз данных в Django."
# Цель: реализовать собственные ORM модели и научиться мигрировать их в базу данных.
# Задача "Модели игрового магазина":
# Студентка: Укладникова Екатерина
# Дата: 24.09.2025г.
#------------------------------
# Домашнее задание по теме "QuerySet запросы в
# базу данных"
# Цель: сделать первые записи в БД при помощи QuerySet запросов,
# закрепив знания о них.
# Задача "Я буду устанавливать все игры!":
# список QuerySet запросов в порядке вызовов, которые
# я использовала для внесения изменений в БД
# (Команда для запуска в терминале QuerySet запросов: python manage.py shell):

# from task1.models import Buyer

# Добавляю покупателей:
# Buyer.objects.create(name='Ilya', balance=1500.05, age=24)
# Buyer.objects.create(name='Terminator2000', balance=42.15, age=52)
# Buyer.objects.create(name='Ubivator432', balance=0.5, age=16)

# from task1.models import Game

# Добавляю игры в каталог:
# Game.objects.create(title='Cyberpunk 2077', cost=31, size=46.2, description='Game of year', age_limited=1)
# Game.objects.create(title='Mario', cost=5, size=0.5, description='Old Game', age_limited=0)
# Game.objects.create(title='Hitman', cost=12, size=36.6, description='Who kills Mark?', age_limited=1)

# Продаю игры с учетом возраста покупателей:
# first_buyer = Buyer.objects.get(age__lt=18)
# second_buyer, third_buyer = Buyer.objects.filter(age__gte=18)
# Game.objects.get(id=1).buyer.set((second_buyer, third_buyer))
# Game.objects.get(id=2).buyer.set([third_buyer])
# Game.objects.get(id=3).buyer.set((second_buyer, first_buyer, third_buyer))

# Выводим список покупателей
# buyer = Buyer.objects.all()
# print(buyer)

# Выводим список игр
# game = Game.objects.all()
# print(game)

from decimal import Decimal
from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100)  # имя покупателя (username аккаунта)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # баланс
    age = models.IntegerField()  # возраст

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)  # название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # размер файлов игры
    description = models.TextField()  # описание (неограниченное кол-во текста, поле необязательно для заполнения в формах и админке Django (может быть пустым))
    age_limited = models.BooleanField(default=False) # Поле, которое вычисляется автоматически на основе возраста
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

#------------------------------
# Домашнее задание по теме "Пагинация": добавить новую вкладку с
# пагинацией в главном меню.

class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#------------------------------
# Домашнее задание по теме Django REST Framework (DRF) и Debug

class Review(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE,
                             related_name='reviews')
    author = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Оценка от 1 до 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.author} для ({self.rating})"
