from .serializers import UserSerializer, UserSerializerWithToken, ChapaSerializer, NotaSerializer, ClienteSerializer, \
    ListaClienteSerializer, ServicoSerializer
from core.models import Chapa, Nota, Cliente, Servico
from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChapaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Chapa.objects.all()
    serializer_class = ChapaSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'obs')


class NotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('numero', 'obs')


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
    search_fields = ('nome', 'cidade')
    ordering = ('nome',)

    def get_serializer_class(self):
        tipo_serializer = self.request.query_params.get('tipo_serializer')
        if tipo_serializer == 'lista':
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
    search_fields = ('nome', 'cidade')


class ServicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'cliente__nome')
