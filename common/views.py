from rest_framework.views import APIView, Response
import requests

from .services import UserService


class RegisterApiView(APIView):
    def post(self, request):
        data = request.data
        data['is_financeiro'] = 'api/financeiro' in request.path
        
        response = requests.post('http://172.17.0.1:8001/api/register', data)

        return Response(response.json())


class LoginApiView(APIView):
    def post(self, request):
        data = request.data
        data['scope'] = 'financeiro' if 'api/financeiro' in request.path else 'admin'


        res = UserService.post('login', data=data)

        response = Response()
        response.set_cookie(key='jwt', value=res['jwt'], httponly=True)
        response.data = {
            'message': 'Success'
        }

        return response


class UserAPIView(APIView):
    def get(self, request):
        return Response(request.user_ms)


class LogoutAPIView(APIView):
    def post(self, request):
        UserService.post('logout', headers=request.headers)

        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            'message': 'Success'
        }
        return response


class ProfileInfoAPIView(APIView):
    def put(self, request):
        return Response(UserService.put('users/info', data=request.data, headers=request.headers))


class ProfilePasswordAPIView(APIView):
    def put(self, request, pk=None):
        return Response(UserService.put('users/password', data=request.data, headers=request.headers))