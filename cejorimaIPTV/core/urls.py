
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_venda, name='cadastrar'),
    # path('produtos', views.produtos, name='produtos'),
    # path('listar-produtos', views.listarProdutos, name='listarProdutos'),
    # path('listar-compras', views.listarCompras, name='listarCompras'),
    # path('adicionarCarrinho/<int:idProduto>', views.adicionarCarrinho, name='carrinho')
]