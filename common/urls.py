
from django.urls import include, path

from common.views import RegisterApiView


urlpatterns = [
    path("register", RegisterApiView.as_view() )
]