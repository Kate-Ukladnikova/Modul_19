from django.contrib import admin

# Register your models here.

from task1.models import Buyer, Game

admin.site.register(Buyer)
admin.site.register(Game)