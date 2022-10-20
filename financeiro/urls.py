from django.urls import include, path

from .views import ServicoBackendAPIView, ServicoFrontendAPIView


urlpatterns = [
    path('', include("common.urls")),
    path('servicos/frontend', ServicoFrontendAPIView.as_view()),
    path('servicos/backend', ServicoBackendAPIView.as_view()),
]
