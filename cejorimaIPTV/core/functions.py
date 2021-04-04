from .models import Venda

def pesquisarVenda(buscar):
    venda = Venda.objects.filter(cliente__icontains= buscar)
    if not venda:
        venda = Venda.objects.filter(id__icontains= buscar)
        if not venda:
            venda = Venda.objects.filter(produto__icontains= buscar)
            if not venda:
                venda = Venda.objects.filter(pagamento__icontains= buscar)
                if not venda:
                    venda = Venda.objects.filter(app__icontains= buscar)
    return venda