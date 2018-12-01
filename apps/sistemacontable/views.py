# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponseRedirect

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
# Create your views here.


def main(request):
    return render(request, 'Main/main.html',{})

@login_required
def index(request):
    return render(request, 'Main/index.html',{})

@login_required
def transaccion(request):
    partida = Partida.objects.all()
    cuentas = Cuenta.objects.all()
    if request.method == 'GET':
        if "q" in request.GET:
            q = request.GET.get('q', '')

            partida = Partida.objects.filter(id__icontains=q)

    if request.method == 'POST':
        t = Transaccion()
        p = int(request.POST['par'])
        t.partida = Partida.objects.get(id=p)
        t.descripcion = request.POST['descri']
        t.monto = float(request.POST['monto'])

        if request.POST['carga2'] == "" and request.POST['mCargar2'] == "":
            if request.POST['carga1'] != "":
                cuenta = Cuenta()
                codigo = int(request.POST['carga1'])
                cuenta = Cuenta.objects.get(codigo=codigo)
                cuenta.debe = (cuenta.debe + float(request.POST['mCargar1']))
                if request.POST['cargarIva'] == "":
                    if t.monto == cuenta.debe:
                        cuenta.save()
                else:
                    if t.monto == (cuenta.debe + float(request.POST['cargarIva'])):
                        cuent = Cuenta()
                        cod = int(request.POST['iva'])
                        cuent = Cuenta.objects.get(codigo=cod)
                        cuent.debe = (cuent.debe + float(request.POST['cargarIva']))
                        cuent.save()
                        cuenta.save()

        else:
            if request.POST['carga3'] != "" and request.POST['mCargar3'] != "":
                cuenta = Cuenta()
                codigo = int(request.POST['carga2'])
                cuenta = Cuenta.objects.get(codigo=codigo)
                cuenta.debe = (cuenta.debe + float(request.POST['mCargar2']))
                codigo2 = int(request.POST['carga3'])
                cu = Cuenta()
                cu = Cuenta.objects.get(codigo=codigo2)
                cu.debe = (cu.debe + float(request.POST['mCargar3']))
                if request.POST['cargarIva'] == "":
                    if t.monto == (cuenta.debe + cu.debe):
                        cuenta.save()
                        cu.save()
                else:
                    if t.monto == (cu.debe + cuenta.debe + float(request.POST['cargarIva'])):
                        cuent = Cuenta()
                        cod = int(request.POST['iva'])
                        cuent = Cuenta.objects.get(codigo=cod)
                        cuent.debe = (cuent.debe + float(request.POST['cargarIva']))
                        cuent.save()
                        cuenta.save()
                        cu.save()
        if request.POST['carga4'] != "" and request.POST['carga5'] != "" and request.POST['carga6'] != "" and \
                        request.POST['mCargar4'] != "" and request.POST['mCargar5'] != "" and request.POST[
            'mCargar6'] != "":
            cuenta = Cuenta()
            codigo = int(request.POST['carga4'])
            cuenta = Cuenta.objects.get(codigo=codigo)
            cuenta.debe = (cuenta.debe + float(request.POST['mCargar4']))
            codigo2 = int(request.POST['carga5'])
            cu = Cuenta()
            cu = Cuenta.objects.get(codigo=codigo2)
            cu.debe = (cu.debe + float(request.POST['mCargar5']))
            codigo3 = int(request.POST['carga6'])
            c = Cuenta.objects.get(codigo=codigo3)
            c.debe = (c.debe + float(request.POST['mCargar6']))
            if request.POST['cargarIva'] == "":
                if t.monto == (cuenta.debe + cu.debe + c.debe):
                    cuenta.save()
                    cu.save()
                    c.save()
            else:
                if t.monto == (c.debe + cu.debe + cuenta.debe + float(request.POST['cargarIva'])):
                    cuent = Cuenta()
                    cod = int(request.POST['iva'])
                    cuent = Cuenta.objects.get(codigo=cod)
                    cuent.debe = (cuent.debe + float(request.POST['cargarIva']))
                    cuent.save()
                    cu.save()
                    c.save()
                    cuenta.save()

        if request.POST['carga7'] != "" and request.POST['carga8'] != "" and request.POST['carga9'] != "" and \
                        request.POST['carga10'] != "" and request.POST['mCargar7'] != "" and request.POST[
            'mCargar8'] != "" and request.POST['mCargar9'] != "" and request.POST['mCargar10'] != "":
            cuenta = Cuenta()
            codigo = int(request.POST['carga7'])
            cuenta = Cuenta.objects.get(codigo=codigo)
            cuenta.debe = (cuenta.debe + float(request.POST['mCargar7']))
            codigo2 = int(request.POST['carga8'])
            cu = Cuenta()
            cu = Cuenta.objects.get(codigo=codigo2)
            cu.debe = (cu.debe + float(request.POST['mCargar8']))
            codigo3 = int(request.POST['carga9'])
            c = Cuenta.objects.get(codigo=codigo3)
            c.debe = (c.debe + float(request.POST['mCargar9']))
            codigo4 = int(request.POST['carga10'])
            cue = Cuenta.objects.get(codigo=codigo4)
            cue.debe = (cue.debe + float(request.POST['mCargar10']))
            if request.POST['cargarIva'] == "":
                if t.monto == (cue.debe + cuenta.debe + cu.debe + c.debe):
                    cuenta.save()
                    cu.save()
                    c.save()
                    cue.save()
            else:
                if t.monto == (cue.debe + c.debe + cu.debe + cuenta.debe + float(request.POST['cargarIva'])):
                    cuent = Cuenta()
                    cod = int(request.POST['iva'])
                    cuent = Cuenta.objects.get(codigo=cod)
                    cuent.debe = (cuent.debe + float(request.POST['cargarIva']))
                    cuent.save()
                    cu.save()
                    c.save()
                    cue.save()
                    cuenta.save()

        if request.POST['carga11'] != "" and request.POST['carga12'] != "" and request.POST['carga13'] != "" and \
                        request.POST['carga14'] != "" and request.POST['carga15'] != "" and request.POST[
            'mCargar11'] != "" and request.POST['mCargar12'] != "" and request.POST['mCargar13'] != "" and request.POST[
            'mCargar14'] != "" and request.POST['mCargar15'] != "":
            cuenta = Cuenta()
            codigo = int(request.POST['carga11'])
            cuenta = Cuenta.objects.get(codigo=codigo)
            cuenta.debe = (cuenta.debe + float(request.POST['mCargar11']))
            codigo2 = int(request.POST['carga12'])
            cu = Cuenta()
            cu = Cuenta.objects.get(codigo=codigo2)
            cu.debe = (cu.debe + float(request.POST['mCargar12']))
            codigo3 = int(request.POST['carga13'])
            c = Cuenta.objects.get(codigo=codigo3)
            c.debe = (c.debe + float(request.POST['mCargar13']))
            codigo4 = int(request.POST['carga14'])
            cue = Cuenta.objects.get(codigo=codigo4)
            cue.debe = (cue.debe + float(request.POST['mCargar14']))
            codigo5 = int(request.POST['carga15'])
            cuen = Cuenta.objects.get(codigo=codigo5)
            cuen.debe = (cuen.debe + float(request.POST['mCargar15']))
            if request.POST['cargarIva'] == "":
                if t.monto == (cuen.debe + cue.debe + cuenta.debe + cu.debe + c.debe):
                    cuenta.save()
                    cuen.save()
                    cu.save()
                    c.save()
                    cue.save()
            else:
                if t.monto == (cuen.debe + cue.debe + c.debe + cu.debe + cuenta.debe + float(
                        request.POST['cargarIva'])):
                    cuent = Cuenta()
                    cod = int(request.POST['iva'])
                    cuent = Cuenta.objects.get(codigo=cod)
                    cuent.debe = (cuent.debe + float(request.POST['cargarIva']))
                    cuent.save()
                    cu.save()
                    c.save()
                    cue.save()
                    cuen.save()
                    cuenta.save()

        if request.POST['abo2'] == "" and request.POST['mAbo2'] == "":
            if request.POST['abo1'] != "":
                cuenta = Cuenta()
                cod = int(request.POST['abo1'])
                cuenta = Cuenta.objects.get(codigo=cod)
                cuenta.haber = (cuenta.haber + float(request.POST['mAbo1']))
                if request.POST['abonarIva'] == "":
                    if t.monto == cuenta.haber:
                        cuenta.save()
                else:
                    if t.monto == (cuenta.haber + float(request.POST['abonarIva'])):
                        cuent = Cuenta()
                        cod = int(request.POST['iva'])
                        cuent = Cuenta.objects.get(codigo=cod)
                        cuent.haber = (cuent.haber + float(request.POST['abonarIva']))
                        cuent.save()
                        cuenta.save()

        else:
            if request.POST['abo3'] != "" and request.POST['mAbo3'] != "":
                codigo = int(request.POST['abo2'])
                cuenta = Cuenta.objects.get(codigo=codigo)
                cuenta.haber = (cuenta.haber + float(request.POST['mAbo2']))
                codigo2 = int(request.POST['abo3'])
                cu = Cuenta.objects.get(codigo=codigo2)
                cu.haber = (cu.haber + float(request.POST['mAbo3']))
                if request.POST['abonarIva'] == "":
                    if t.monto == (cuenta.haber + cu.haber):
                        cuenta.save()
                        cu.save()
                else:
                    if t.monto == (cu.haber + cuenta.haber + float(request.POST['abonarIva'])):
                        cuent = Cuenta()
                        cod = int(request.POST['iva'])
                        cuent = Cuenta.objects.get(codigo=cod)
                        cuent.haber = (cuent.haber + float(request.POST['abonarIva']))
                        cuent.save()
                        cuenta.save()
                        cu.save()

        if request.POST['abo4'] != "" and request.POST['abo5'] != "" and request.POST['abo6'] != "" and request.POST[
            'mAbo4'] != "" and request.POST['mAbo5'] != "" and request.POST['mAbo6'] != "":
            cuenta = Cuenta()
            codigo = int(request.POST['abo4'])
            cuenta = Cuenta.objects.get(codigo=codigo)
            cuenta.haber = (cuenta.haber + float(request.POST['mAbo4']))
            codigo2 = int(request.POST['abo5'])
            cu = Cuenta()
            cu = Cuenta.objects.get(codigo=codigo2)
            cu.haber = (cu.haber + float(request.POST['mAbo5']))
            codigo3 = int(request.POST['abo6'])
            c = Cuenta.objects.get(codigo=codigo3)
            c.haber = (c.haber + float(request.POST['mAbo6']))
            if request.POST['abonarIva'] == "":
                if t.monto == (cuenta.haber + cu.haber + c.haber):
                    cuenta.save()
                    cu.save()
                    c.save()
            else:
                if t.monto == (c.haber + cu.haber + cuenta.haber + float(request.POST['abonarIva'])):
                    cuent = Cuenta()
                    cod = int(request.POST['iva'])
                    cuent = Cuenta.objects.get(codigo=cod)
                    cuent.haber = (cuent.haber + float(request.POST['abonarIva']))
                    cuent.save()
                    cu.save()
                    c.save()
                    cuenta.save()

        if request.POST['abo7'] != "" and request.POST['abo8'] != "" and request.POST['abo9'] != "" and request.POST[
            'abo10'] != "" and request.POST['mAbo7'] != "" and request.POST['mAbo8'] != "" and request.POST[
            'mAbo9'] != "" and request.POST['mAbo10'] != "":
            cuenta = Cuenta()
            codigo = int(request.POST['abo7'])
            cuenta = Cuenta.objects.get(codigo=codigo)
            cuenta.haber = (cuenta.haber + float(request.POST['mAbo7']))
            codigo2 = int(request.POST['abo8'])
            cu = Cuenta()
            cu = Cuenta.objects.get(codigo=codigo2)
            cu.haber = (cu.haber + float(request.POST['mAbo8']))
            codigo3 = int(request.POST['abo9'])
            c = Cuenta.objects.get(codigo=codigo3)
            c.haber = (c.haber + float(request.POST['mAbo9']))
            codigo4 = int(request.POST['abo10'])
            cue = Cuenta.objects.get(codigo=codigo4)
            cue.haber = (cue.haber + float(request.POST['mAbo10']))
            if request.POST['abonarIva'] == "":
                if t.monto == (cue.haber + cuenta.haber + cu.haber + c.haber):
                    cuenta.save()
                    cue.save()
                    cu.save()
                    c.save()
            else:
                if t.monto == (cue.haber + c.haber + cu.haber + cuenta.haber + float(request.POST['abonarIva'])):
                    cuent = Cuenta()
                    cod = int(request.POST['iva'])
                    cuent = Cuenta.objects.get(codigo=cod)
                    cuent.haber = (cuent.haber + float(request.POST['abonarIva']))
                    cuent.save()
                    cu.save()
                    cue.save()
                    c.save()
                    cuenta.save()

        if request.POST['abo11'] != "" and request.POST['abo12'] != "" and request.POST['abo13'] != "" and request.POST[
            'abo14'] != "" and request.POST['abo15'] != "" and request.POST['mAbo11'] != "" and request.POST[
            'mAbo12'] != "" and request.POST['mAbo13'] != "" and request.POST['mAbo14'] != "" and request.POST[
            'mAbo15'] != "":
            cuenta = Cuenta()
            codigo = int(request.POST['abo11'])
            cuenta = Cuenta.objects.get(codigo=codigo)
            cuenta.haber = (cuenta.haber + float(request.POST['mAbo11']))
            codigo2 = int(request.POST['abo12'])
            cu = Cuenta()
            cu = Cuenta.objects.get(codigo=codigo2)
            cu.haber = (cu.haber + float(request.POST['mAbo12']))
            codigo3 = int(request.POST['abo13'])
            c = Cuenta.objects.get(codigo=codigo3)
            c.haber = (c.haber + float(request.POST['mAbo13']))
            codigo4 = int(request.POST['abo14'])
            cue = Cuenta.objects.get(codigo=codigo4)
            cue.haber = (cue.haber + float(request.POST['mAbo14']))
            codigo5 = int(request.POST['abo15'])
            cuen = Cuenta.objects.get(codigo=codigo5)
            cuen.haber = (cuen.haber + float(request.POST['mAbo15']))
            if request.POST['abonarIva'] == "":
                if t.monto == (cuen.haber + cue.haber + cuenta.haber + cu.haber + c.haber):
                    cuenta.save()
                    cuen.save()
                    cue.save()
                    cu.save()
                    c.save()
            else:
                if t.monto == (cuen.haber + cue.haber + c.haber + cu.haber + cuenta.haber + float(
                        request.POST['abonarIva'])):
                    cuent = Cuenta()
                    cod = int(request.POST['iva'])
                    cuent = Cuenta.objects.get(codigo=cod)
                    cuent.haber = (cuent.haber + float(request.POST['abonarIva']))
                    cuent.save()
                    cu.save()
                    cuen.save()
                    cue.save()
                    c.save()
                    cuenta.save()
        return HttpResponseRedirect('/transaccion')
    return render(request, 'Main/transaccion.html',{'cuentas': cuentas, 'partida': partida})

@login_required
def preTransaccion(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/transaccion')
    return render(request, 'Main/preTransaccion',{})

@login_required
def saldoxMensual(request):
    cuentitas = Cuenta.objects.all()
    for c in cuentitas:
        cuentitas_codigo = c.codigo
        cuentitas_debe = c.debe
        cuentitas_haber = c.haber
        cuentitas_nombre = c.nombre
        for c in cuentitas:
            parti = Partida.objects.all()
            #pc= Cuenta.objects.get(nombre=c.nombre)
            #if pc.codigo == c.codigo:
            c.total = c.debe- c.haber
            if c.total < 0:
                c.haber = c.total
                c.debe =0
                c.save()
            if c.total > 0:
                c.debe = c.total
                c.haber = 0
                c.save()
            if c.total == 0:
                c.debe = 0
                c.haber = 0
                c.save()
        context={
        "cuentitas": cuentitas,
        "cuentitas_codigo": cuentitas_codigo,
        "cuentitas_nombre": cuentitas_nombre,
        "cuentitas_haber": cuentitas_haber,
        "cuentitas_debe": cuentitas_debe,
        #"pc": pc

        }
    return render (request, 'Main/saldoxMensual.html', context)