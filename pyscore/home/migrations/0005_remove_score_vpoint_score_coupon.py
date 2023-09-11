# Generated by Django 4.0.10 on 2023-09-11 06:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_score_vpoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='vpoint',
        ),
        migrations.AddField(
            model_name='score',
            name='coupon',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], verbose_name='쿠폰'),
        ),
    ]
