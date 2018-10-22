from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', views.obtain_auth_token),
]