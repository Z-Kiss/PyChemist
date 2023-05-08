from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_potion/', views.add_potion, name='add_potion'),
    path('show_potion/', views.show_potion, name='show_potion'),
    path('add_ingredient_to_potion/<potion_id>/<ingredient_id>',
         views.add_ingredient_to_potion,
         name='add_ingredient_to_potion'),
    path('brew_potion/<potion_id>/', views.brew_potion, name='brew_potion'),
]
