from .serializers import (
    ChapaSerializer,
    NotaSerializer,
    ClienteSerializer,
    ListaClienteSerializer,
    ServicoSerializer,
    SaidasSerializer,
)
from core.models import Chapa, Nota, Cliente, Servico, Saidas
from rest_framework import viewsets, filters

# pylint: disable=no-member
class ChapaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Chapa.objects.all()
    serializer_class = ChapaSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("nome", "obs")


class NotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("numero", "obs")


class ClienteViewSet(viewsets.ModelViewSet):
    #         return ClienteSerializer
    #     elif self.request.query_params.get('oi') == 2:
    #         serializer_class = ListaClienteSerializer
    #     else:
    #         serializer_class = ClienteSerializer
    #

    queryset = Cliente.objects.all()
    # serializer_class = ListaClienteSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("nome", "cidade")
    ordering = ("nome",)

    def get_serializer_class(self):
        tipo_serializer = self.request.query_params.get("tipo_serializer")
        if tipo_serializer == "lista":
            return ListaClienteSerializer
        else:
            return ClienteSerializer

    # def get_queryset(self):
    #     longitude = self.request.query_params.get('oi')
    #     print(longitude)
    #     return Cliente.objects.all()


class ListaClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Cliente.objects.all()
    serializer_class = ListaClienteSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("nome", "cidade")


class SaidasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Saidas.objects.all()
    serializer_class = SaidasSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("descricao", "valor")


class ServicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("nome", "cliente__nome")
