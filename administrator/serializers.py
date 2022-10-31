from attr import fields
from rest_framework import serializers
# pylint: disable=import-error
from core.models import Chapa, GrupoNotaServico, Nota, Servico, Cliente


class ChapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapa
        fields = ("id", "nome", "valor", "estoque", "obs", "created_at", "uploaded_at")


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = (
            "id",
            "nome",
            "cliente",
            "chapa",
            "quantidade",
            "valor_total_servico",
            "created_at",
            "uploaded_at",
        )


class ServicoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = (
            "id",
            "nome",
            "quantidade",
            "valor_total_servico",
            "created_at"
        )


class NotaFullSerializer(serializers.ModelSerializer):
    servico = ServicoSerializer(many=True)
    class Meta:
        model = Nota
        fields = (
            "id",
            "desconto",
            "numero",
            "obs",
            "servico",
            "status",
            "valor_total_nota",
            "created_at"
        )


class NotaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = (
            "id",
            "desconto",
            "numero",
            "obs",
            "status",
            "valor_total_nota",
            "created_at"
        )


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = (
            "id",
            "desconto",
            "numero",
            "obs",
            "servico",
            "status",
            "valor_total_nota",
            "created_at",
            "uploaded_at",
        )


class GrupoNotaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model: GrupoNotaServico
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            "id",
            "nome",
            "email",
            "telefone",
            "cnpj",
            "cpf",
            "rua",
            "bairro",
            "numero",
            "cidade",
            "estado",
            "cep",
            "created_at",
            "uploaded_at"
        )
