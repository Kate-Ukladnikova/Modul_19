# Домашнее задание по теме "Сайт администрирования".

from django.contrib import admin
from task1.models import Buyer, Game

# Register your models here.

# admin.site.register(Buyer)
# admin.site.register(Game)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    # fields = [('title', 'cost'), 'description', 'size',]
    search_fields = ('title',)
    list_filter = ('cost', 'size',)
    fieldsets = (
        ('info', {
            'fields':
                ('title', 'cost')
        }),
        ('footer', {
            'fields':
                ('description', 'size')
        }),
    )
    list_max_show_all = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    fields = [('name', 'balance'), 'age',]
    search_fields = ('name',)
    list_filter = ('balance', 'age',)
    readonly_fields = ('balance',)
    list_max_show_all = 30
