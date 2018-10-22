from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Gasto
from api.models import TipoGasto

class UserSerializer(serializers.ModelSerializer):

    gastos = serializers.PrimaryKeyRelatedField(many=True, queryset=Gasto.objects.all())
    tipogastos = serializers.PrimaryKeyRelatedField(many=True, queryset=TipoGasto.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'gastos',
            'tipogastos',
        )

class GastoSerializer(serializers.ModelSerializer):

    usuario = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Gasto
        fields = (
            'id',
            'usuario',
            'criado',
            'tipo',
            'quando',
            'valor',
            'descricao',
        )
    
    #def create(self, validated_data):
        #return Gasto.objects.create(**validated_data)

class TipoGastoSerializer(serializers.ModelSerializer):

    #usuario = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = TipoGasto
        fields = (
            'id',
            'nome',
        )