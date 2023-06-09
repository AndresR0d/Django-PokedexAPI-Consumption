from django.db import models
from django.core.serializers import serialize

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=50, default=None, null=False)
    type2 = models.CharField(max_length=50, blank=True, null=True)
    abilities = models.TextField(blank=False, null=True)
    stats = models.TextField(blank=False, null=True)

    def set_abilities(self, abilities):
        self.abilities = serialize('json', abilities)

    def get_abilities(self):
        return list(serialize('json', self.abilities))

    def set_stats(self, stats):
        self.stats = serialize('json', stats)

    def get_stats(self):
        return list(serialize('json'),self.stats)

    def __str__(self):
        return self.name