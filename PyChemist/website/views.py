from collections import Counter
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Potion, Ingredient, Recipe
from .forms import SignUpForm, AddPotionForm, RegisterRecipeForm, AddIngredientForm


def home(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('home')

@login_required
def add_potion(request):
    form = AddPotionForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                potion_name = form.cleaned_data['name']
                potion = Potion(name=potion_name, user=request.user)
                potion.save()
                messages.success(request, "Potion is created")
                return redirect('show_potion')
        return render(request, 'add_potion.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


def add_ingredient(request):
    form = AddIngredientForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                ingredient_name = form.cleaned_data['name']
                ingredient = Ingredient(name=ingredient_name)
                ingredient.save()
                messages.success(request, "Ingredient is added")
                return redirect('home')
        else:
            return render(request, 'add_ingredient.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


def show_potion(request):
    if request.user.is_authenticated:
        potions = Potion.objects.all()
        return render(request, 'show_potions.html', {'potions': potions})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


def show_ingredient(request):
    if request.user.is_authenticated:
        ingredients = Ingredient.objects.all()
        return render(request, 'show_ingredients.html', {'ingredients': ingredients})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


def brew_potion(request, potion_id):
    if request.user.is_authenticated:
        potion_to_brew = Potion.objects.get(pk=potion_id)
        ingredients = Ingredient.objects.all()
        return render(request, 'brew_potion.html', {"ingredients": ingredients, "potion": potion_to_brew})
    else:
        messages.success(request, "You must be logged in")
    return redirect('home')


def add_ingredient_to_potion(request, potion_id, ingredient_id):
    if request.user.is_authenticated:
        ingredient = Ingredient.objects.get(pk=ingredient_id)
        potion = Potion.objects.get(pk=potion_id)
        if potion.can_add_ingredients():
            potion.add_ingredient(ingredient)
            potion.save()
            if potion.ready_to_check_for_recipe():
                potion_ingredients = list(potion.ingredients.all())
                matching_recipes = Recipe.objects.filter(ingredients__in=potion_ingredients)
                distinct_recipes = set(matching_recipes)
                matching_recipe = None
                element_counter = Counter(matching_recipes)
                for recipe in distinct_recipes:
                    if element_counter[recipe] == 5:
                        matching_recipe = recipe
                if matching_recipe:
                    potion.recipe = matching_recipe
                    potion.save()
                    return redirect('show_potion')
                else:
                    return redirect('register_recipe', potion_id=potion_id)
            return redirect('brew_potion', potion_id=potion_id)
        else:
            messages.success(request, "Potion already Done!")
        return redirect('brew_potion', potion_id=potion_id)
    else:
        messages.success(request, "You must be logged in")
    return redirect('home')


def register_recipe(request, potion_id):
    if request.user.is_authenticated:
        form = RegisterRecipeForm(request.POST or None)
        potion = Potion.objects.get(pk=potion_id)
        ingredients = list(potion.ingredients.all())
        if request.user.is_authenticated:
            if request.method == 'POST':
                if form.is_valid():
                    recipe_name = form.cleaned_data['name']
                    recipe = Recipe(name=recipe_name)
                    recipe.save()
                    recipe.ingredients.set(ingredients)
                    recipe.save()
                    potion.recipe = recipe
                    potion.original = True
                    potion.save()
                    return redirect('show_potion')
            return render(request, 'register_recipe.html', {
                'form': form, 'ingredients': ingredients, 'potion_id': potion_id}
                          )
        else:
            messages.success(request, "You must be logged in")

        return redirect('home')
