from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('gastos/', views.GastoList.as_view()),
    path('gastos/<int:pk>', views.GastoDetail.as_view()),
    path('tipogastos/', views.TipoGastoList.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)