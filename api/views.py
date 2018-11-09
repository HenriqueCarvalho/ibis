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
        #queryset, entrada, saida
        queryset = self.get_queryset()
        
        total_entrada = 0
        total_saida = 0

        if queryset:
            total_entrada = queryset\
                        .filter(tipo_fluxo=tipo_fluxo.ENTRADA)\
                        .aggregate(Sum('valor'))\
                        ['valor__sum']          

        if queryset:
            total_saida = queryset\
                        .filter(tipo_fluxo=tipo_fluxo.SAIDA)\
                        .aggregate(Sum('valor'))\
                        ['valor__sum']
            
        saldo = total_entrada - total_saida

        data = {
            'total_entrada': valor_formatado(total_entrada),
            'total_saida': valor_formatado(total_saida),
            'saldo': valor_formatado(saldo),
            'gastos': AnnotationGastoSerializer(queryset, many=True).data
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