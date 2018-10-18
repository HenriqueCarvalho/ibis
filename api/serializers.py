from rest_framework import serializers
from api.models import Gasto
from api.models import TipoGasto

class GastoSerializer(serializers.ModelSerializer):

    #tipogasto = serializers.IntegerField(source='tipo.id', read_only=True)

    class Meta:
        model = Gasto
        # 'categoria',
        fields = (
            'id',
            'criado',
            'tipo',
            'quando',
            'valor',
            'descricao',
        )

class TipoGastoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoGasto
        fields = (
            'id',
            'nome',
        )