#coding:utf-8
from django.db import models

# Create your models here.

TIPO_FILME = [
       ('1','Ação'),
       ('2','Aventura'),
       ('3','Comédia'),
       ('4','Drama'),
       ('5','Documentário'),
       ('6','Policial'),
       ('7','Romance'),
       ('8','Terror'),
       ('9','Suspense')
]

CATEGORIA = [
     ('1','Lançamento'),
     ('2','Promoção'),
     ('3','Normal')
]

class Precat(models.Model):
       Preco = models.DecimalField('Preço',max_digits=4,decimal_places=2,unique=True,null=True)
       Categ = models.CharField('Categoria',max_length=1,choices=CATEGORIA,unique=True,null=True)
       
       def __unicode__(self):
	      return self.Categ

class Cadfilme(models.Model):
         Nome = models.CharField('Nome',max_length=100,unique=True,null=True)
         DtLan = models.DateField('Data de Lançamento',null=True)
         Nomed = models.CharField('Nome Diretor',max_length=100,null=True)
         Gen = models.CharField('Gênero',max_length=1,choices=TIPO_FILME,null=True)
         Cat = models.CharField('Categoria',max_length=1,choices=CATEGORIA,null=True)

         def __unicode__(self):
	      return self.Nome
	

class Aluguel(models.Model):	
         PesAlg = models.ForeignKey("cliente.Pessoa",verbose_name="Pessoa do Aluguel")
         DtAlg = models.DateField('Data Aluguel',null=True)
         DtAlgd = models.DateField('Data Devolução',null=True)
         
         def __unicode__(self):
		return unicode(self.PesAlg)

class AlugelFlmes(models.Model):    
	AlugelFlmes = models.ForeignKey(Aluguel,null=True)
	FilAlg = models.ForeignKey(Cadfilme,verbose_name="Nome do Filme",null=True )
         
         
         
