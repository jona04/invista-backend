
from django.urls import include, path

from administrator.views import ChapaGenericAPIView, ClienteGenericAPIView, FuncionarioAPIView

urlpatterns = [
    path('', include("common.urls")),
    path('funcionarios', FuncionarioAPIView.as_view()),
    path('chapas', ChapaGenericAPIView.as_view()),
    path('chapas/<str:pk>', ChapaGenericAPIView.as_view()),
    path('clientes', ClienteGenericAPIView.as_view()),
    path('clientes/<str:pk>', ClienteGenericAPIView.as_view()),
]