# Generated by Django 3.2.13 on 2022-04-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_feladat_kiesz_alter_feladat_kie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feladat',
            name='kie',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feladat',
            name='kiesz',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
