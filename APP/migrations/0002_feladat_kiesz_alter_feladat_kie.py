# Generated by Django 4.0.4 on 2022-04-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feladat',
            name='kiesz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feladat',
            name='kie',
            field=models.CharField(max_length=255, null=True),
        ),
    ]