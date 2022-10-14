from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from .authentication import JWTAuthentication

from core.models import User

from .serializers import UserSerializer

class RegisterApiView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions .APIException('Senha nao iguais')
        
        data['is_funcionario'] = 0
        
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginApiView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed('Usuario nao encontrado')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Senha incorreta')
        
        token = JWTAuthentication.generate_jwt(user.id)

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'Success'
        }

        return response

class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            'message': 'Success'
        }
        return response

class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions .APIException('Senha nao iguais')

        user.set_password(data['password'])
        user.save()
        return Response(UserSerializer(user).data)