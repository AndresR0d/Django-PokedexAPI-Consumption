from django.shortcuts import render
from pokedex_app.models import Pokemon

# Create your views here.
def pokemon_list(request):
    pokemon_list = Pokemon.objects.all()
    print(pokemon_list)