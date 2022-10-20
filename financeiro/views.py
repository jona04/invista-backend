from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Servico
from financeiro.serializers import ServicoSerializer


class ServicoFrontendAPIView(APIView):
    def get(self, _):
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)


class ServicoBackendAPIView(APIView):
    def get(self, _):
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)