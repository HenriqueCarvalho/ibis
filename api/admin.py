from django.contrib import admin
from .models import Gasto
from .models import TipoGasto

# Register your models here.
admin.site.register(Gasto)
admin.site.register(TipoGasto)