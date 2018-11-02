# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Cuenta, Partida, Periodo, Catalogo

# Register your models here.
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre','codigo','naturaleza','debe','haber')
admin.site.register(Cuenta,CuentaAdmin)

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('fecha','cuenta','descripcion','monto')
admin.site.register(Partida,PartidaAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('get_partidas',)
admin.site.register(Periodo,PeriodoAdmin)

class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('get_cuentas',)
admin.site.register(Catalogo,CatalogoAdmin)

admin.site.site_header = 'Sistema Contable'