# Generated by Django 4.0.4 on 2022-05-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_auto_20220422_1228'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Diak',
        ),
        migrations.AddField(
            model_name='feladat',
            name='egyezzik',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feladat',
            name='kie',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feladat',
            name='kiesz',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
