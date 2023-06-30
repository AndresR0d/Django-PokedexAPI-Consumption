from pokedex_app.models import Pokemon
from pokedex_app.api.serializers import PokemonSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons)
    return Response(serializer.data)

@api_view()
def pokemon_details(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    serializer = PokemonSerializer(pokemon)
    return Response(serializer.data)