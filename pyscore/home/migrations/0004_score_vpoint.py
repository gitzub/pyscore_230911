# Generated by Django 4.0.10 on 2023-09-11 06:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_score_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='vpoint',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], verbose_name='포인트'),
        ),
    ]
