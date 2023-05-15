from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Potion, Recipe, Ingredient


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        "placeholder": "Username", "class": "form-control"}), label="")
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={
        "placeholder": "Password", "class": "form-control"}), label="",
                                help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too ' \
                                          'similar to your other personal information.</li><li>Your password must ' \
                                          'contain at least 8 characters.</li><li>Your password can\'t be a ' \
                                          'commonly used password.</li><li>Your password can\'t be entirely ' \
                                          'numeric.</li></ul>')
    password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={
        "placeholder": "Confirm Password", "class": "form-control"}), label="",
                                help_text='<span class="form-text text-muted"><small>Enter the same password as ' \
                                          'before, for verification.</small></span>')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AddPotionForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        "placeholder": "Choose a name for your Potion", "class": "form-control"}), label="")

    class Meta:
        model = Potion
        fields = ('name',)


class AddIngredientForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        "placeholder": "Choose a name for your Ingredient", "class": "form-control"}), label="")

    class Meta:
        model = Ingredient
        fields = ('name',)


class RegisterRecipeForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        "placeholder": "Choose a name for your Recipe", "class": "form-control"}), label="")

    class Meta:
        model = Recipe
        fields = ('name',)
