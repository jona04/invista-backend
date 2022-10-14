from django.shortcuts import render
from rest_framework.views import APIView, Response

class RegisterApiView(APIView):
    def post(self, request):
        return Response('Hello')