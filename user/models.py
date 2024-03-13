from django.db import models

class User (models.Model):
    name = models.CharField(max_lenght=50)
    email = models.CharField()
    password = models.CharField(max_length=50)
    