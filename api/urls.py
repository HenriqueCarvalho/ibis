from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('usuarios/', views.UserList.as_view()),
    path('usuarios/<int:pk>', views.UserDetail.as_view()),
    path('gastos/', views.GastoList.as_view()),
    path('gastos/<int:pk>', views.GastoDetail.as_view()),
    #path('tipogastos/', views.TipoGastoList.as_view()),
    #path('tipogastos/<int:pk>', views.TipoGastoDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)