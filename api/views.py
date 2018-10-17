#from django.shortcuts import render
from api.models import Gasto
from api.serializers import GastoSerializer
from rest_framework import generics

class GastoList(generics.ListCreateAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class GastoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer