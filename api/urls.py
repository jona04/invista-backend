from django.urls import include,path

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'chapa', views.ChapaViewSet)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'servico', views.ServicoViewSet)
router.register(r'nota', views.NotaViewSet)


urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls))
]