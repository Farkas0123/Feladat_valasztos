# Generated by Django 4.0.4 on 2022-04-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=255)),
                ('jelszo', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Diák',
                'verbose_name_plural': 'Diákok',
            },
        ),
        migrations.CreateModel(
            name='Feladat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feladat', models.CharField(max_length=255)),
                ('kie', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Feladat',
                'verbose_name_plural': 'Feladatok',
            },
        ),
    ]