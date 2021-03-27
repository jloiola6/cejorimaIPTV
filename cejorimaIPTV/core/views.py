from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import *
from .form import *
from ..usuarios.views import verification, logout


# from datetime import datetime

# Create your views here.

def index(request):
    if verification(request) == False:
        user = False
        return HttpResponseRedirect('usuarios/login')

    template_name = 'index.html'

    user = True
    venda = Venda.objects.all().order_by('-id')
    buscar = request.GET.get('pesquisa')
    if buscar:
        venda = Venda.objects.filter(cliente__icontains= buscar)
        if not venda:
            venda = Venda.objects.filter(id__icontains= buscar)
            if not venda:
                venda = Venda.objects.filter(marca__icontains= buscar)
                if not venda:
                    venda = Venda.objects.filter(device_ID__icontains= buscar)
                    if not venda:
                        venda = Venda.objects.filter(device_KEY__icontains= buscar)
                        if not venda:
                            venda = Venda.objects.filter(tipo__icontains= buscar)
                            if not venda:
                                venda = Venda.objects.filter(situacao__icontains= buscar)
                                if not venda:
                                    venda = Venda.objects.filter(pagamento__icontains= buscar)
                                    if not venda:
                                        venda = Venda.objects.filter(app__icontains= buscar)


        return TemplateResponse(request, template_name, locals())

    return TemplateResponse(request, template_name, locals())


def cadastrar_venda(request):

    if verification(request) == False:
        user = False
        return HttpResponseRedirect('/usuarios/login')

    template_name =  'venda.html'

    id = request.GET.get('id')
    user = True
    editar = False

    if id:
        venda = Venda.objects.get(id=int(id))
        form = FormVenda(instance=venda)
        editar = True
    else:
        form = FormVenda()

    if request.method == 'POST':
        if editar: 
            form = FormVenda(request.POST, instance=venda)
        else:
            form = FormVenda(request.POST)

        if form.is_valid():
            # form.updated_at = datetime.now()
            form.save()
            if editar: 
                return HttpResponseRedirect('/')
            form = FormVenda()

    return TemplateResponse(request, template_name, locals())