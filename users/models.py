from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    senha = models.CharField(max_length=8)

    def __str__(self):
        return self.nome
    