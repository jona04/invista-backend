from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from common.authentication import JWTAuthentication
from common.serializers import UserSerializer
from django.core.cache import cache

from .serializers import ChapaSerializer, ClienteSerializer, NotaSerializer, ServicoSerializer
from core.models import Chapa, Cliente, GrupoNotaServico, Nota, Servico, User


class FinanceiroAPIView(APIView):
    def get(self, _):
        financeiro = User.objects.all()
        serializer = UserSerializer(financeiro, many=True)
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
    

class ServicoGenericAPIView(generics.GenericAPIView, 
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        
        return self.list(request)

    def post(self, request):
        chapa = Chapa.objects.get(pk=request.data['chapa'])
        cliente = Cliente.objects.get(pk=request.data['cliente'])
        request.data['valor_total_servico'] = request.data['quantidade'] * chapa.valor
        response = self.create(request, chapa=chapa, cliente=cliente)
        
        for key in cache.keys('*'):
            if 'servicos_frontend' in key:
                cache.delete(key)
        cache.delete('servicos_backend')
        return response


    def put(self, request, pk=None):
        response = self.partial_update(request, pk)
        for key in cache.keys('*'):
            if 'servicos_frontend' in key:
                cache.delete(key)
        cache.delete('servicos_backend')
        return response

    def delete(self, request, pk=None):
        response = self.destroy(request, pk)
        for key in cache.keys('*'):
            if 'servicos_frontend' in key:
                cache.delete(key)
        cache.delete('servicos_backend')
        return response


class NotaGenericAPIView(generics.GenericAPIView, 
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        
        return self.list(request)

    def post(self, request):
        servico_id_list = request.data.pop('servico')
        servicos_list = []
        valor_total = 0.0
        for servico_id in servico_id_list:
            servico_obj = Servico.objects.get(pk=servico_id)
            valor_total = valor_total + servico_obj.valor_total_servico
            servicos_list.append(servico_obj)

        request.data['valor_total_nota'] = valor_total
        nota = self.create(request)
        nota_instance = Nota.objects.get(pk=nota.data['id'])
        for servico in servicos_list:
            GrupoNotaServico.objects.create(nota=nota_instance, servico=servico)
        nota = Nota.objects.get(pk=nota.data['id'])
        return Response(NotaSerializer(nota).data)

    def put(self, request, pk=None):
        return self.partial_update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
