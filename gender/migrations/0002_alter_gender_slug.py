# Generated by Django 5.0.3 on 2024-04-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
