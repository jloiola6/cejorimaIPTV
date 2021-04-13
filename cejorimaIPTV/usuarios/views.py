from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import *
from .form import *

# Create your views here.

def verification(request):
    try:
       if request.session['id']:
           return True
    except KeyError:
        return False


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponseRedirect('/')


def cadastroCliente(request):

    try:
        adm = Usuario.objects.get(id= request.session['id'])
    except:
        user = False
        return HttpResponseRedirect('login')

    template_name = 'cliente.html'

    id = request.GET.get('id')
    user = True
    editar = False

    if id:
        cliente = Cliente.objects.get(id=int(id))
        form = FormCliente(instance=cliente)
        editar = True
    else:
        form = FormCliente()

    if request.method == 'POST':
        if editar: 
            form = FormCliente(request.POST, instance=cliente)
        else:
            form = FormCliente(request.POST)

        if form.is_valid():
            form.save()
            if editar: 
                return HttpResponseRedirect('listar-clientes')
            form = FormCliente()

    return TemplateResponse(request, template_name, locals())


def login(request):

    if verification(request):
        user = False
        return HttpResponseRedirect('/')
    
    
    template_name = 'login.html'

    erro = None
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')
    
        try:
            user = Usuario.objects.get(usuario= login, senha= senha)
            if user:
                request.session['id'] = user.id
                return HttpResponseRedirect('/')
        except:
            erro = 'Usuário ou senha inválidos'
            
    return TemplateResponse(request, template_name, locals())


def listarClientes(request):
    try:
        adm = Usuario.objects.get(id= request.session['id'])
    except:
        user = False
        return HttpResponseRedirect('login')

    template_name = 'listarClientes.html'

    user = True
    cliente = Cliente.objects.all().order_by('-id')
    # buscar = request.GET.get('pesquisa')
    # if buscar:
    #     cliente = Cliente.objects.filter(nome__icontains= buscar)
    #     if not cliente:
    #         cliente = Cliente.objects.filter(id__icontains= buscar)
    #         if not cliente:
    #             cliente = Cliente.objects.filter(telefone__icontains= buscar)
    #             if not cliente:
    #                 cliente = Cliente.objects.filter(endereco__icontains= buscar)


        # return TemplateResponse(request, template_name, locals())

    return TemplateResponse(request, template_name, locals())