# Generated by Django 3.0.5 on 2020-04-06 15:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_challenge', '0008_auto_20200406_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='avg_hr',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='result',
            name='max_hr',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(300)]),
        ),
    ]