from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import *
from ..usuarios.models import Usuario
from .form import *
from ..usuarios.views import verification, logout
from .functions import pesquisarVenda
from .save import save


# from datetime import datetime

# Create your views here.
def cadastrar_venda(request):

    if verification(request) == False:
        user = False
        return HttpResponseRedirect('/usuarios/login')

    template_name = 'venda.html'

    id = request.GET.get('id')
    user = True
    editar = False

    form = FormVenda()

    if request.method == 'POST':
        form = FormVenda(request.POST)
        if form.is_valid():
            save(form, request, editar, id)
            form = FormVenda()

    return TemplateResponse(request, template_name, locals())


def visualizar_venda(request):
    if verification(request) == False:
        user = False
        return HttpResponseRedirect('/usuarios/login')

    template_name = 'visualizarVenda.html'

    editar = True
    user = True
    id = request.GET.get('id')

    venda = Venda.objects.get(id=int(id))
    form = FormVenda(instance=venda)

    if request.method == 'POST':
        form = FormVenda(request.POST, instance=venda)
        if form.is_valid():
            save(form, request, editar, id)
            return HttpResponseRedirect('/')

    return TemplateResponse(request, template_name, locals())


def index(request):
    if verification(request) == False:
        user = False
        return HttpResponseRedirect('usuarios/login')

    template_name = 'index.html'

    user = True
    venda = Venda.objects.all().order_by('-id')

    return TemplateResponse(request, template_name, locals())


def listar_dispositivos(request):

    try:
        adm = Usuario.objects.get(id= request.session['id'])
    except:
        user = False
        return HttpResponseRedirect('/usuarios/login')

    template_name = 'listarDispositivos.html'

    user = True
    dispositivos = Dispositivos.objects.all().order_by('-id')
    # buscar = request.GET.get('pesquisa')
    # if buscar:
    #     dispositivos = Dispositivos.objects.filter(nome__icontains= buscar)
    #     if not dispositivos:
    #         dispositivos = Dispositivos.objects.filter(device_ID__icontains= buscar)
    #         if not dispositivos:
    #             dispositivos = Dispositivos.objects.filter(device_KEY= buscar)
    #             if not dispositivos:
    #                 dispositivos = Dispositivos.objects.filter(situacao__icontains= buscar)


        # return TemplateResponse(request, template_name, locals())

    return TemplateResponse(request, template_name, locals())


def cadastrar_dispositivos(request):

    if verification(request) == False:
        user = False
        return HttpResponseRedirect('/usuarios/login')

    template_name =  'dispositivos.html'

    id = request.GET.get('id')
    user = True
    editar = False

    if id:
        dispositivos = Dispositivos.objects.get(id=int(id))
        form = FormDispositivos(instance=dispositivos)
        editar = True
    else:
        form = FormDispositivos()

    if request.method == 'POST':
        if editar: 
            form = FormDispositivos(request.POST, instance=dispositivos)
        else:
            form = FormDispositivos(request.POST)

        if form.is_valid():
            form.save()
            if editar: 
                return HttpResponseRedirect('/')
            form = FormDispositivos()

    return TemplateResponse(request, template_name, locals())