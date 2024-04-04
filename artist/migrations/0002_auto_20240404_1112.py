from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.CharField(max_length=100, unique=True, blank=True, null=True),
        ),
    ]