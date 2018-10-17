from rest_framework import serializers
from api.models import Gasto

class GastoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gasto
        fields = (
            'id',
            'criado',
            'categoria',
            'quando',
            'valor',
            'descricao',
        )