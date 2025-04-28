from django.db import models

# Create your models here.
class carros(models.Model):
    modelo = models.CharField(max_length=200)
    preco = models.FloatField(max_length=10)


def __str__(self):
    return self.modelo