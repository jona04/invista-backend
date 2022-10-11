from django.urls import path

from . import views

urlpatterns = [
    path("busca_servico/", views.busca_servico, name="busca_servico"),
    path("busca_cliente/", views.busca_cliente, name="busca_cliente"),
    path("busca_nota/", views.busca_nota, name="busca_nota"),
    path(
        "lista_notas_cliente/<int:id>",
        views.lista_notas_cliente,
        name="lista_notas_cliente",
    ),
    path(
        "lista_servicos_cliente/<int:id>",
        views.lista_servicos_cliente,
        name="lista_servicos_cliente",
    ),
    path(
        "cliente_especifico/<int:id>",
        views.cliente_especifico,
        name="cliente_especifico",
    ),
    path("nota_especifica/<int:id>", views.nota_especifica, name="nota_especifica"),
    path("notas/", views.notas, name="notas"),
    path("chapas/", views.chapas, name="chapas"),
    path("servicos/", views.servicos, name="servicos"),
    path("clientes/", views.clientes, name="clientes"),
    path("", views.home, name="home"),
    path("oi/", views.index, name="index"),
]
