# Generated by Django 3.0.5 on 2020-04-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_challenge', '0010_auto_20200407_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='time',
            field=models.DurationField(),
        ),
    ]
