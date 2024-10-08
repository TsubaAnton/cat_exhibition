# Generated by Django 4.2 on 2024-10-01 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=255, verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Порода',
                'verbose_name_plural': 'Породы',
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('age_months', models.IntegerField(verbose_name='Возраст (полных месяцев')),
                ('description', models.TextField(verbose_name='Описание')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat.breed', verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Котенок',
                'verbose_name_plural': 'Котята',
            },
        ),
    ]
