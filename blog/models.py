from django.db import models

# Create your models here.
class Eu(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='eu', null=True, blank=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
class jogadores(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='jogadores', null=True, blank=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome

class times(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='times', null=True, blank=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    

    
