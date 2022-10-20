from django.urls import include, path

from .views import ServicoBackendAPIView, ServicoFrontendAPIView


urlpatterns = [
    path('', include("common.urls")),
    path('servicos/frontend', ServicoFrontendAPIView),
    path('servicos/backend', ServicoBackendAPIView),
]
