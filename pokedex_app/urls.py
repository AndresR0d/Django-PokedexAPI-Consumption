from django.urls import path, include
from pokedex_app.views import pokemon_list
urlpatterns = [
    path('list/', pokemon_list, name='pokemon-list'),

]
