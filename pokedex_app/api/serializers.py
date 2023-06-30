from rest_framework import serializers
from pokedex_app.models import Pokemon

class PokemonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    type1 = serializers.CharField()
    type2 = serializers.CharField()
    abilities = serializers.DictField()
    stats = serializers.DictField()