
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro-cliente', views.cadastroCliente, name='cadastroCliente'),
    path('listar-clientes', views.listarClientes, name='listarClientes'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]