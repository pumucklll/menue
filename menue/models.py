from django.db import models

class Book(models.Model):
    Name = models.CharField(max_length=100)
    Kategorie = models.CharField(max_length=100)
    Verkaufspreis = models.CharField(max_length=100)
    Allergene = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Kategorie} {self.Name} {self.Verkaufspreis} Euro {self.Allergene}"
