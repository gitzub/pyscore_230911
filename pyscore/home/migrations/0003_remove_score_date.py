# Generated by Django 4.0.10 on 2023-09-04 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_gamelist_alter_score_username_score_foreignkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='date',
        ),
    ]
