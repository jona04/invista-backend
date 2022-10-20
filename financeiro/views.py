import math
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Servico
from financeiro.serializers import ServicoSerializer
from django.core.cache import cache


class ServicoFrontendAPIView(APIView):
    @method_decorator(cache_page(60*60*2, key_prefix='servicos_backend'))
    def get(self, _):
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)


class ServicoBackendAPIView(APIView):
    def get(self, request):
        serializer = cache.get('servicos_backend')
        if not serializer:
            servicos = list(Servico.objects.all())
            
            serializer = ServicoSerializer(servicos, many=True).data
            cache.set('servicos_backend', serializer, timeout=60*30) #30min
        
        s = request.query_params.get('s', '')
        if s:
            serializer = list([
                p for p in serializer
                if (s.lower() in p['nome']) or 
                    (s.lower() in p['cliente']) or 
                    (s.lower() in p['chapa'])
            ])

        total = len(serializer)

        sort = request.query_params.get('sort', None)
        if sort == 'asc':
            serializer.sort(key=lambda p: p['created_at'])
        elif sort == 'desc':
            serializer.sort(key=lambda p: p['created_at'], reverse=True)

        per_page = 9
        page = int(request.query_params.get('page', 1))
        start = (page - 1) * per_page
        end = page * per_page

        data = serializer[start:end]
        return Response({
            'data': data,
            'meta': {
                'total': total,
                'page': page,
                'last_page': math.ceil(total / per_page)
            }
        })
