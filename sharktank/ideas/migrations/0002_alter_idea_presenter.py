# Generated by Django 4.1.7 on 2023-04-03 03:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ideas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="idea",
            name="presenter",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ideas.presenter",
            ),
        ),
    ]
