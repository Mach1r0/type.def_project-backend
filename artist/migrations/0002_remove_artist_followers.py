# Generated by Django 5.0.3 on 2024-03-22 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='followers',
        ),
    ]
