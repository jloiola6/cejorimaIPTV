from .models import *
from ..usuarios.models import *

def save(form, request, id):
    testDispositivo = testeCliente = False

    if len(request.POST.get('device_ID')) != 0 and len(request.POST.get('device_KEY')) != 0:
        print("1")
        # nome_dispositivo = request.POST.get('nome_dispositivo')
        device_ID = request.POST.get('device_ID')
        device_KEY = request.POST.get('device_KEY')
        situacao = request.POST.get('situacao')

        dispositivo = Dispositivos(device_ID=device_ID, device_KEY=device_KEY, situacao= situacao)
        dispositivo.save()
        dispositivo = Dispositivos.objects.last()
        testDispositivo = True

    if len(request.POST.get('nome_cliente')) != 0:
        print("1")
        nome_cliente = request.POST.get('nome_cliente')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')

        cliente = Cliente(nome=nome_cliente, telefone=telefone, email=email ,endereco=endereco)
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
    else:
        print("Teste")
        box = form.cleaned_data['box']
        produto = Dispositivos.objects.get(box= box)
        print(produto.situacao)
        produto.situacao = "Vendido"
        produto.save()

    if form.cleaned_data['box']:
        venda = Venda(cliente=form.cleaned_data['cliente'], box=form.cleaned_data['box'], produto=produto, tipo= form.cleaned_data['tipo'], pagamento = form.cleaned_data['pagamento'], aplicativo = form.cleaned_data['aplicativo'])
    else:
        venda = Venda(cliente=form.cleaned_data['cliente'], produto=dispositivo, tipo= form.cleaned_data['tipo'], pagamento = form.cleaned_data['pagamento'], aplicativo = form.cleaned_data['aplicativo'])
    
    venda.save()

    
