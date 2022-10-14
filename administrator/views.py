from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from common.authentication import JWTAuthentication
from common.serializers import UserSerializer

from .serializers import ChapaSerializer, ClienteSerializer
from core.models import Chapa, Cliente, User


class FuncionarioAPIView(APIView):
    def get(self, _):
        funcionario = User.objects.filter(is_funcionario=True)
        serializer = UserSerializer(funcionario, many=True)
        return Response(serializer.data)


class ClienteGenericAPIView(generics.GenericAPIView, 
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        
        return self.list(request)

    def post(self, request):
        return self.create(request)


    def put(self, request, pk=None):
        return self.partial_update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)



class ChapaGenericAPIView(generics.GenericAPIView, 
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Chapa.objects.all()
    serializer_class = ChapaSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        
        return self.list(request)

    def post(self, request):
        return self.create(request)


    def put(self, request, pk=None):
        return self.partial_update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
