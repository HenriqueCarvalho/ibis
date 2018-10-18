from rest_framework import generics
from api.models import Gasto
from api.models import TipoGasto
from api.serializers import GastoSerializer
from api.serializers import TipoGastoSerializer

class GastoList(generics.ListCreateAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class GastoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class TipoGastoList(generics.ListCreateAPIView):
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer