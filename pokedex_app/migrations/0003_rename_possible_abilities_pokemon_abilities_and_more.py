# Generated by Django 4.2.2 on 2023-06-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokedex_app", "0002_pokemon_ability_pokemon_possible_abilities_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pokemon", old_name="possible_abilities", new_name="abilities",
        ),
        migrations.RemoveField(model_name="pokemon", name="ability",),
        migrations.AddField(
            model_name="pokemon", name="stats", field=models.TextField(null=True),
        ),
    ]