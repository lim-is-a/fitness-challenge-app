# Generated by Django 3.0.5 on 2020-04-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_challenge', '0005_auto_20200403_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.CharField(max_length=700),
        ),
    ]