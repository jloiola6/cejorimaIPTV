
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar-venda/', views.cadastrar_venda, name='cadastrar-venda'),
    path('visualizar-venda/', views.visualizar_venda, name='visualizar-venda'),
    path('cadastrar-dispositivos/', views.cadastrar_dispositivos, name='cadastrar-dispositivos'),
    path('cadastrar-box/', views.cadastrar_box, name='cadastrar-box'),
    path('listar-duplex/', views.listar_Duplex, name='listar-duplex'),
    path('listar-box/', views.listar_Box, name='listar-box'),
]