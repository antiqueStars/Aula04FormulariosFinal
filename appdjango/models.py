from django.db import models

# Create your models here.
class Cantoras(models.Model):
  nome = models.CharField(max_length=30)
  instrumento = models.CharField(max_length=30)
  debut_date = models.DateField()

class NanoGames(models.Model):
  name = models.CharField(max_length = 50)
  release = models.DateField()
  platform = models.CharField(max_length = 20)