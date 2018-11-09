from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Gasto
from api.utils.date import translate_date_en_to_pt
#from api.models import TipoGasto
    
class UserSerializer(serializers.ModelSerializer):
    gastos = serializers.PrimaryKeyRelatedField(many=True, queryset=Gasto.objects.all())
    #tipogastos = serializers.PrimaryKeyRelatedField(many=True, queryset=TipoGasto.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'gastos',
            #'tipogastos',
        )

"""
class TipoGastoSerializer(serializers.ModelSerializer):

    #usuario = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = TipoGasto
        fields = (
            'id',
            'nome',
            'fluxo',
        )
"""

class AnnotationGastoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    tipo_fluxo = serializers.ReadOnlyField()
    tipo_gasto = serializers.ReadOnlyField()
    usuario = serializers.CharField(source='usuario.username', read_only=True)
    descricao = serializers.ReadOnlyField()
    quando_formatado = serializers.ReadOnlyField()
    valor_formatado = serializers.ReadOnlyField()

class GastoSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.username', read_only=True)
    #tipo = TipoGastoSerializer(many=False, read_only=True) #By default nested serializers are read-only
    criado = serializers.DateTimeField(format="%A, %d %b %Y %H:%M", required=False, read_only=True)
    quando = serializers.DateField(format="%A %d %b %Y", required=False, read_only=False)
    quando_formatado = serializers.ReadOnlyField()
    valor_formatado = serializers.ReadOnlyField()

    class Meta:
        model = Gasto
        fields = (
            'id',
            'usuario',
            'tipo_fluxo',
            'tipo_gasto',
            'criado',
            'quando',
            'quando_formatado',
            'valor',
            'valor_formatado',
            'descricao',
        )

        """
        fields = (
            '__all__'
        )
        """

        #read_only_fields = ('tipo',)
        #extra_kwargs = {'password': {'write_only': True}}
    

    #def validate(self,data):
        #print(data)
        #return TipoGasto.objects.get(pk=data)
        #return data

    #def create(self, validated_data):
        #tipo_data = validated_data.pop('tipo')
        #gasto = Gasto.objects.create(**validated_data)
        #Gasto.objects.create(gasto=gasto, **tipo_data)
        #return gasto