from django.db import models
from django.core.serializers import serialize

class Pokemon(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    base_experience = models.IntegerField()
    height = models.IntegerField()
    order = models.IntegerField()
    weight = models.IntegerField()
    abilities = models.ManyToManyField('Ability', related_name='pokemons')

class Ability(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='abilitites')
    name = models.CharField(max_length=100)
    is_hidden = models.BooleanField(default=False)
    slot = models.IntegerField()

class Type(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='types')
    slot = models.IntegerField()
    name = models.CharField(max_length=50)
    url = models.URLField()

class Stat(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='stats')
    base_stat = models.IntegerField()
    effort = models.IntegerField()
    name = models.CharField(max_length=50)
    url = models.URLField()