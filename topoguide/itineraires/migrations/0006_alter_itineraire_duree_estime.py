# Generated by Django 4.0.4 on 2022-04-20 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0005_alter_itineraire_altitude_de_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraire',
            name='duree_estime',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxLengthValidator(3)]),
        ),
    ]
