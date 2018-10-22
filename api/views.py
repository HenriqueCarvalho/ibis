from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from api.models import Gasto
from api.models import TipoGasto
from api.serializers import UserSerializer
from api.serializers import GastoSerializer
from api.serializers import TipoGastoSerializer

class UserList(generics.ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    #permission_classes = (permissions.IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GastoList(generics.ListCreateAPIView):
    #aceitar apenas usuarios que criou podem editar
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,) 
    #permission_classes = (permissions.IsAuthenticated,) 
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

    #perform_create() allows us to modify how the instance save is managed
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class GastoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class TipoGastoList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,) 
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer

    #perform_create() allows us to modify how the instance save is managed
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class TipoGastoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer