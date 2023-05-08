from django.contrib import admin
from .models import Potion, Recipe, Ingredient

# Register your models here.

admin.site.register(Potion)
admin.site.register(Recipe)
admin.site.register(Ingredient)
