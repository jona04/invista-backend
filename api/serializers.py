from rest_framework import serializers
from core.models import Chapa, Nota, Servico, Cliente
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings


class ChapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapa
        fields = ('id', 'nome', 'valor', 'estoque', 'obs', 'created_at', 'uploaded_at')


class ServicoSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    chapa = ChapaSerializer(read_only=True)

    class Meta:
        model = Servico
        fields = ('id', 'nome', 'cliente', 'chapa', 'quantidade', 'created_at', 'uploaded_at')


class NotaSerializer(serializers.ModelSerializer):
    servico = ServicoSerializer(many=True)

    class Meta:
        model = Nota
        fields = ('id', 'desconto', 'numero', 'obs', 'servico', 'status', 'created_at', 'uploaded_at')


class ClienteSerializer(serializers.ModelSerializer):
    nota = NotaSerializer(many=True)

    class Meta:
        model = Cliente
        fields = (
            'id', 'nome', 'email', 'telefone', 'cnpj', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'estado', 'cep',
            'created_at', 'uploaded_at', 'nota')


class ListaClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id', 'nome', 'email', 'telefone', 'cnpj', 'cpf', 'rua', 'bairro', 'numero', 'cidade', 'estado', 'cep',
            'created_at', 'uploaded_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')
