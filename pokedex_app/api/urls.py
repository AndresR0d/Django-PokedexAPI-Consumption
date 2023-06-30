from django.urls import path, include
from pokedex_app.api.views import pokemon_list, pokemon_details
urlpatterns = [
    path('list/', pokemon_list, name='pokemon-list'),
    path('<int:pk>', pokemon_details, name='pokemon-detail'),
]
