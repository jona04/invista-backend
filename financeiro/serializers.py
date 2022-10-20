from rest_framework import serializers

from core.models import Chapa, Servico


class ChapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapa
        fields = ("id", "nome", "valor", "estoque", "obs", "created_at", "uploaded_at")


class ServicoSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    chapa = ChapaSerializer(read_only=True)

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


