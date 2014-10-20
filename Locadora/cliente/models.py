#coding:utf-8
from django.db import models

# Create your models here.

class Pessoa(models.Model):
      Nome = models.CharField('Nome',max_length=100,null=True)
      DataNascimento = models.DateField('Data de Nascimento',null=True)
      Telefone = models.CharField('Telefone',max_length=15,null=True)
      Celular = models.CharField('Celular',max_length=15,null=True)
      Email = models.EmailField('Endereço de email',max_length=100)
      Bairro = models.CharField('Bairro', max_length=100,null=True)
      Cidade = models.CharField('Cidade', max_length=100,null=True)
