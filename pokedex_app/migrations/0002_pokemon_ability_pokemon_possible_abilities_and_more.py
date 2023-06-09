# Generated by Django 4.2.2 on 2023-06-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokedex_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="ability",
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name="pokemon",
            name="possible_abilities",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="pokemon",
            name="type1",
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name="pokemon",
            name="type2",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
