from rest_framework import serializers
from core.models import Chapa, Nota, Servico, Cliente

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
