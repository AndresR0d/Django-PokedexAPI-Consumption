from django.shortcuts import render
from pokedex_app.models import Pokemon
from django.http import JsonResponse

def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    data = {
        'pokemons': list(pokemons.values())
    }
    return JsonResponse(data)
