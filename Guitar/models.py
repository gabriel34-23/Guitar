# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Guitarra(models.Model):
	nome = models.CharField(max_length=100)
	img = models.ImageField(upload_to = "Guitar/instrumentos", blank=True , null= True)
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	descricao = models.TextField()
	estoque = models.PositiveIntegerField()
	def __str__(self):
		return self.nome

class Funcionario(models.Model):
	img = models.ImageField(upload_to = "Guitar/funcionarios", blank=True , null= True)
	nome = models.CharField(max_length=100)
	funcao = models.CharField(max_length=100)
	idade = models.IntegerField()
	salario = models.DecimalField(max_digits=10, decimal_places=2)
	cpf = models.CharField(max_length=16)
	rg = models.CharField(max_length=10)
	sexo = models.CharField(max_length=1)
	def __str__(self):
		return u'%s %s' % (self.nome, self.idade)

class Baixo(models.Model):
	nome = models.CharField(max_length=100)
	img = models.ImageField(upload_to = "Guitar/instrumentos", blank=True , null= True)
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	descricao = models.TextField()
	estoque = models.PositiveIntegerField()
	def __str__(self):
		return self.nome

class Bateria(models.Model):
	nome = models.CharField(max_length=100)
	img = models.ImageField(upload_to = "Guitar/instrumentos", blank=True , null= True)
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	descricao = models.TextField()
	estoque = models.PositiveIntegerField()
	def __str__(self):
		return self.nome

class ComprarGuitarra(models.Model):
	guitar = models.ForeignKey('Guitarra', on_delete=models.PROTECT)
	nome_comprador = models.CharField(max_length=100)
	quantidade_guitar = models.PositiveIntegerField()
	forma_pagamento = models.ForeignKey('Pagamento', on_delete=models.PROTECT)
	def __str__(self):
		return u'%s ' % (self.nome_comprador) 
	

class ComprarBaixo(models.Model):
	baixo = models.ForeignKey('Baixo', on_delete=models.PROTECT)
	nome_comprador = models.CharField(max_length=100)
	quantidade_baixo = models.PositiveIntegerField()
	forma_pagamento = models.ForeignKey('Pagamento', on_delete=models.PROTECT)
	def __str__(self):
		return u'%s ' % (self.nome_comprador) 
	

class ComprarBateria(models.Model):
	bateria = models.ForeignKey('Bateria', on_delete=models.PROTECT)
	nome_comprador = models.CharField(max_length=100)
	quantidade_drum = models.PositiveIntegerField()
	forma_pagamento = models.ForeignKey('Pagamento', on_delete=models.PROTECT)
	def __str__(self):
		return u'%s ' % (self.nome_comprador) 

class Cliente_Guitar(models.Model):
	nome_guitar = models.ForeignKey('ComprarGuitarra', on_delete=models.PROTECT)
	repeat = models.CharField(max_length=3)

class Cliente_Baixo(models.Model):
	nome_baixo = models.ForeignKey('ComprarBaixo', on_delete=models.PROTECT)
	repeat = models.CharField(max_length=3)

class Cliente_Bateria(models.Model):
	nome_drum = models.ForeignKey('ComprarBateria', on_delete=models.PROTECT)
	repeat = models.CharField(max_length=3)

class Pagamento(models.Model):
	forma_pagamento = models.CharField(max_length=100)
	descricao = models.TextField()
	def __str__(self):
		return u'%s ' % (self.forma_pagamento) 