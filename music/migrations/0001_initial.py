# Generated by Django 5.0.3 on 2024-05-13 16:41

import django.db.models.deletion
import django_jsonform.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0002_remove_album_gender_album_genders'),
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.FloatField()),
                ('album_info', django_jsonform.models.fields.JSONField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='album.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='artist.artist')),
            ],
        ),
    ]
