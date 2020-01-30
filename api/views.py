
from .serializers import ChapaSerializer,NotaSerializer,ClienteSerializer,ServicoSerializer
from core.models import Chapa,Nota,Cliente,Servico
from rest_framework import viewsets, filters

class ChapaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Chapa.objects.all()
    serializer_class = ChapaSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome','obs')

class NotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('numero','obs')

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'cidade')


class ServicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'cliente__nome')