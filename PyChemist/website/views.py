from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Potion, Ingredient, Recipe
from .forms import SignUpForm, AddPotionForm


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


def add_potion(request):
    form = AddPotionForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                potion_name = form.cleaned_data['name']
                potion = Potion(name=potion_name, user=request.user)
                potion.save()
                messages.success(request, "Potion is created")
                return redirect('home')
        return render(request, 'add_potion.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


def show_potion(request):
    potions = Potion.objects.all()
    return render(request, 'show_potions.html', {'potions': potions})


def brew_potion(request, potion_id):
    potion_to_brew = Potion.objects.get(pk=potion_id)
    ingredients = Ingredient.objects.all()
    return render(request, 'brew_potion.html', {"ingredients": ingredients, "potion": potion_to_brew})


def add_ingredient_to_potion(request, potion_id, ingredient_id):
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    potion = Potion.objects.get(pk=potion_id)
    if potion.can_add_ingredients():
        potion.add_ingredient(ingredient)
        if potion.ready_to_check_for_recipe():
            potion_ingredients = list(potion.ingredients.all())
            matching_recipes = Recipe.objects.filter(ingredients__in=potion_ingredients)
            if matching_recipes.exists():
                potion = matching_recipes
                potion.save()
    else:
        messages.success(request, "Potion already Done!")
    return redirect('brew_potion', potion_id=potion_id)

