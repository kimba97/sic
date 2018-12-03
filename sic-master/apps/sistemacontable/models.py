# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cuenta(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField()
    naturaleza = models.CharField(max_length=30)
    debe = models.FloatField()
    haber = models.FloatField()

    class Meta:
        verbose_name='Cuenta'
        verbose_name_plural='Cuentas'
    def __str__(self):
        return '%s' %(self.nombre)


class Partida(models.Model):
    fecha = models.DateField()
    cuenta = models.ManyToManyField(Cuenta)
    descripcion = models.TextField(max_length=500)
    def get_cuenta(self):
        return "\n".join([i.id for i in self.cuenta.all()])
    class Meta:
        verbose_name='Partida'
        verbose_name_plural='Partidas'
    def __str__(self):
        return '%s' %(self.id)

class Periodo(models.Model):
    partidas = models.ManyToManyField(Partida)
    def get_partidas(self):
        return "\n".join([i.id for i in self.partidas.all()])
    class Meta:
        verbose_name='Periodo'
        verbose_name_plural='Periodos'
    def __str__(self):
        return '%s' %(self.id)

class Catalogo(models.Model):
    cuentas = models.ManyToManyField(Cuenta)
    def get_cuentas(self):
        return "\n".join([i.codigo for i in self.cuentas.all()])
    class Meta:
        verbose_name='Catalogo'
        verbose_name_plural='Catalogos'
    def __str__(self):
        return '%s' %(self.id)

class Transaccion(models.Model):
    partida = models.ForeignKey(Partida)
    descripcion = models.TextField(max_length=500)
    monto = models.FloatField()
    class Meta:
        verbose_name='Transaccion'
        verbose_name_plural='Transacciones'
    def __str__(self):
        return '%s' %(self.id)