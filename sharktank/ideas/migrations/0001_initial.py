# Generated by Django 4.1.7 on 2023-04-03 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game_date", models.DateTimeField(verbose_name="game date")),
            ],
        ),
        migrations.CreateModel(
            name="Idea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("submitter_name", models.CharField(max_length=200)),
                ("deck_url", models.URLField()),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ideas.game"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Presenter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="presenter name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("entertainment_score", models.IntegerField()),
                ("creativity_score", models.IntegerField()),
                (
                    "idea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ideas.idea"
                    ),
                ),
                (
                    "presenter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="ideas.presenter",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="idea",
            name="presenter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="ideas.presenter"
            ),
        ),
    ]
