from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import datetime, jwt
from core.models import User
from invista import settings

class JWTAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('nao autenticado')

        user = User.objects.get(pk=payload['user_id'])

        if user is None:
            raise exceptions.AuthenticationFailed('usuario nao encontrado')
        
        return (user, None)


    @staticmethod
    def generate_jwt(id):
        payload = {
            'user_id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow()
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    