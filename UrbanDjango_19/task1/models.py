# Домашнее задание по теме "Модели баз данных в Django."
# Цель: реализовать собственные ORM модели и научиться мигрировать их в базу данных.
# Задача "Модели игрового магазина":
# Студентка: Укладникова Екатерина
# Дата: 24.09.2025г.

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