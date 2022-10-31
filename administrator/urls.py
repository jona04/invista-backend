from django.urls import include, path

from administrator.views import ChapaGenericAPIView, ClienteGenericAPIView, FinanceiroAPIView, NotaGenericAPIView, ServicoGenericAPIView, ServicoListGenericAPIView, NotaListGenericAPIView, NotaFullGenericAPIView

urlpatterns = [
    path('', include("common.urls")),
    path('financeiros', FinanceiroAPIView.as_view()),
    path('chapas', ChapaGenericAPIView.as_view()),
    path('chapas/<str:pk>', ChapaGenericAPIView.as_view()),
    path('clientes', ClienteGenericAPIView.as_view()),
    path('clientes/<str:pk>', ClienteGenericAPIView.as_view()),
    path('servicos', ServicoGenericAPIView.as_view()),
    path('servicos/list', ServicoListGenericAPIView.as_view()),
    path('servicos/<str:pk>', ServicoGenericAPIView.as_view()),
    path('notas', NotaGenericAPIView.as_view()),
    path('notas/list', NotaListGenericAPIView.as_view()),
    path('notas/<str:pk>', NotaGenericAPIView.as_view()),
    path('notas/full/<str:pk>', NotaFullGenericAPIView.as_view()),
]
