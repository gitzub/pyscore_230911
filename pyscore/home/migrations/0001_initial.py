# Generated by Django 4.0.10 on 2023-09-04 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rankname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=20, unique=True, verbose_name='순위')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='날짜')),
                ('rank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appliers_Score_rank', to='home.rankname', verbose_name='순위')),
                ('username', models.ForeignKey(limit_choices_to={'groups__name': 'onlyholdem'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appliers_Score_username', to=settings.AUTH_USER_MODEL, verbose_name='이름')),
            ],
        ),
    ]
