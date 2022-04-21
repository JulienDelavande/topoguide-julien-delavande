# Generated by Django 4.0.4 on 2022-04-20 19:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0007_alter_sortie_duree_reelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraire',
            name='duree_estime',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='duree_reelle',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
