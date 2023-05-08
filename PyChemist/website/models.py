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

    def add_ingredient(self, ingredient):
        if self.ingredients.count() < 5:
            if self.ingredients.count() == 4:
                # run your function here
                print("The fifth ingredient has been added!")
            self.ingredients.add(ingredient)
