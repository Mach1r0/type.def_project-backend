# Generated by Django 5.0.3 on 2024-04-03 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gender',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='gender',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subgenres',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='subgenres',
            old_name='nome',
            new_name='name',
        ),
    ]
