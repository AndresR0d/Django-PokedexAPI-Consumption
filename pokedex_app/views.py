#from django.shortcuts import render
#from pokedex_app.models import Pokemon
#from django.http import JsonResponse
#
#def pokemon_list(request):
#    pokemons = Pokemon.objects.all()
#    data = {
#        'pokemons': list(pokemons.values())
#    }
#    return JsonResponse(data)
#
#def pokemon_details(request, pk):
#    pokemon = Pokemon.objects.get(pk=pk)
#    data = {
#        'name': pokemon.name,
#        'type1': pokemon.type1,
#        'type2': pokemon.type2,
#        'abilities': pokemon.abilities,
#        'stats': pokemon.stats
#    }
#    return JsonResponse(data)