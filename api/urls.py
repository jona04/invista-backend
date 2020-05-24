from django.urls import include, path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


router = routers.DefaultRouter()
router.register(r'chapa', views.ChapaViewSet)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'servico', views.ServicoViewSet)
router.register(r'nota', views.NotaViewSet)
router.register(r'saidas', views.SaidasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
