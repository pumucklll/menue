from django.db import models

class Book(models.Model):
    Name = models.CharField(max_length=100)
    Kategorie = models.CharField(max_length=100)
    Verkaufspreis = models.CharField(max_length=100)
