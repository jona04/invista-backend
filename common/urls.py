
from django.urls import include, path

from common.views import LoginApiView, LogoutAPIView, ProfileInfoAPIView, ProfilePasswordAPIView, RegisterApiView, UserAPIView


urlpatterns = [
    path("register", RegisterApiView.as_view() ),
    path("login", LoginApiView.as_view() ),
    path("user", UserAPIView.as_view()),
    path("users/info", ProfileInfoAPIView.as_view()),
    path("users/password", ProfilePasswordAPIView.as_view()),
    path("logout", LogoutAPIView.as_view())
]