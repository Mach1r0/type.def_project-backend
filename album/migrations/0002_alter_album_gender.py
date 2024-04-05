# Generated by Django 5.0.3 on 2024-04-04 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('gender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='gender.gender'),
        ),
    ]
