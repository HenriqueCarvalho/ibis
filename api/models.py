from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class TipoGasto(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey('auth.User', related_name='tipogastos', on_delete=models.CASCADE) 
         
    class Meta:
        ordering = ('nome',)

class Gasto(models.Model):
    criado = models.DateTimeField(auto_now_add=True) #VER COMO QUE DEIXA ISSO SEGURO QUE NAO POSSA SER ALTERADO
    tipo = models.ForeignKey(TipoGasto, on_delete=models.CASCADE)
    usuario = models.ForeignKey('auth.User', related_name='gastos', on_delete=models.CASCADE) 
    quando = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)  #MELHOR MANEIRA DE REPRESTENTAR A MOEDA BRASILEIRA
    descricao = models.TextField(blank=True)

    class Meta:
        ordering = ('quando',)

# Depois de criar o model roda as linhas de comando

##### python manage.py makemigrations [NOME DO APP]
##### python manage.py migrate

# Populando no shell

##### python manage.py shell
##### from api.models import Gasto
##### from api.models import Gasto

# Delete a table and start over
##### rm -f db.sqlite3
##### rm -r snippets/migrations
##### python manage.py makemigrations [NOME DO APP]
##### python manage.py migrate

#new user
#python manage.py createsuperuser