from .models import *
from ..usuarios.models import *

def save(form, request, editar, id):
    testDispositivo = testeCliente = False

    if len(request.POST.get('nome_dispositivo')) != 0:
        nome_dispositivo = request.POST.get('nome_dispositivo')
        device_ID = request.POST.get('Device ID')
        device_KEY = request.POST.get('Device KEY')
        situacao = request.POST.get('situacao')

        dispositivo = Dispositivos(nome=nome_dispositivo, device_ID=device_ID, device_KEY=device_KEY, situacao=situacao)
        dispositivo.save()
        dispositivo = Dispositivos.objects.last()
        testDispositivo = True

    if len(request.POST.get('nome_cliente')) != 0:
        nome_cliente = request.POST.get('nome_cliente')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')

        cliente = Cliente(nome=nome_cliente, telefone=telefone, endereco=endereco)
        cliente.save()
        cliente = Cliente.objects.last()
        testeCliente = True

    if testeCliente and testDispositivo:
        form.cleaned_data['cliente'] = cliente
        form.cleaned_data['produto'] = dispositivo
    elif testDispositivo:
        form.cleaned_data['produto'] = dispositivo
    elif testeCliente:
        form.cleaned_data['cliente'] = cliente

    if editar:
        print("editar")
        venda = Venda.objects.get(id= id)
        venda.cliente = form.cleaned_data['cliente']
        venda.produto = form.cleaned_data['produto']
        venda.tipo = form.cleaned_data['tipo']
        venda.pagamento = form.cleaned_data['pagamento']
        venda.aplicativo = form.cleaned_data['aplicativo']
        venda.save()
    else:
        print("novo")
        venda = Venda(cliente=form.cleaned_data['cliente'], produto=form.cleaned_data['produto'], tipo= form.cleaned_data['tipo'], pagamento = form.cleaned_data['pagamento'], aplicativo = form.cleaned_data['aplicativo'])
        venda.save()

    
