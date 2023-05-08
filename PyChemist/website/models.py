from django.contrib.auth.models import User
from django.db import models

# Ideas for future system:
#   Ingredients could have fields of color and/or symbols, patterns
#   After we have a Recipe with 5 ingredients we create some logic
#   that calculate the color and patterns for creating a picture


MAXIMUM_AMOUNT_OF_INGREDIENT = 5


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe',
        blank=True,
    )

    def add_ingredient(self, ingredient):
        if self.ingredients.count() < MAXIMUM_AMOUNT_OF_INGREDIENT:
            self.ingredients.add(ingredient)


class Potion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='potions',
        blank=True,
    )

    def can_add_ingredients(self):
        return self.ingredients.count() < MAXIMUM_AMOUNT_OF_INGREDIENT

    def add_ingredient(self, ingredient):
        if self.can_add_ingredients():
            self.ingredients.add(ingredient)

    def ready_to_check_for_recipe(self):
        return self.ingredients.count() == MAXIMUM_AMOUNT_OF_INGREDIENT
