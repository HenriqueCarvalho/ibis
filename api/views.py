from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from api.models import Gasto
#from api.models import TipoGasto
from api.serializers import UserSerializer, GastoSerializer, AnnotationGastoSerializer
from rest_framework.response import Response
#from api.serializers import TipoGastoSerializer
from datetime import date
from django.db.models import Avg, Max, Min, Sum
from api.utils import tipo_fluxo
from api.utils.string import *

class UserList(generics.ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    #permission_classes = (permissions.IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AnoMes:
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes

class GastoList(generics.ListCreateAPIView): 

    serializer_class = GastoSerializer
    
    def get_queryset(self):
        """
        Por default a url /gastos/ ira retornar todos os gastos. 
        Pode ser acrescentado 'mes' e 'ano' no parametro para ser filtrado.
        Ex: /gastos/?mes=11&ano=2018
        """
        queryset = Gasto.objects.all()

        mes = self.request.GET.get('mes', '')
        ano = self.request.GET.get('ano', '')

        #checa se a str eh numero
        if mes.isdigit():
            queryset = queryset.filter(quando__month=mes)

        #checa se a str eh um numero
        if ano.isdigit():
            queryset = queryset.filter(quando__year=ano)

        return queryset

    def get(self, request, *args, **kwargs):
        #queryset filtrada pelos parametros
        queryset_filtrada = self.get_queryset()
        #queryset sem parametros 
        queryset = Gasto.objects.all()
        
        entrada = queryset_filtrada\
                    .filter(tipo_fluxo=tipo_fluxo.ENTRADA)\
                    .aggregate(Sum('valor'))\
                    ['valor__sum']

        #Checando se a entrada filtrada pelos parametros é um Nonetype
        if entrada is None: entrada = 0

        saida = queryset_filtrada\
                    .filter(tipo_fluxo=tipo_fluxo.SAIDA)\
                    .aggregate(Sum('valor'))\
                    ['valor__sum']

        #Checando se a saida filtrada pelos parametros é um Nonetype
        if saida is None: saida = 0

        entrada_total = queryset\
                    .filter(tipo_fluxo=tipo_fluxo.ENTRADA)\
                    .aggregate(Sum('valor'))\
                    ['valor__sum']       
        
        if entrada_total is None: entrada_total = 0

        saida_total = queryset\
                    .filter(tipo_fluxo=tipo_fluxo.SAIDA)\
                    .aggregate(Sum('valor'))\
                    ['valor__sum']

        if saida_total is None: saida_total = 0

        # Calculado o saldo que a diferenca de todas as entradas menos a saida
        saldo = entrada_total - saida_total
        
        data = {
            'entrada': valor_formatado(entrada),
            'saida': valor_formatado(saida),
            'saldo': valor_formatado(saldo),
            'gastos': AnnotationGastoSerializer(queryset_filtrada, many=True).data
        }

        return Response(data)

    #perform_create() allows us to modify how the instance save is managed
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class GastoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

"""
class TipoGastoList(generics.ListCreateAPIView):
    #aceitar apenas usuarios que criou podem editar
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,) 
    #permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.IsAuthenticated,) 
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer

    #perform_create() allows us to modify how the instance save is managed
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
    #def post(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()

class TipoGastoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer
"""