from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from api.utils import tipo_fluxo, tipo_gasto
from api.utils.date import translate_date_en_to_pt
from api.utils.string import *

"""
from django.contrib.auth.models import User

class PessoaFisica(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, null=True, blank=False, unique=True) #329.614.663-69 | 32961466369 11 Dig
    nome_completo = models.CharField(
        verbose_name='Nome Completo', 
        max_length=100, blank=True, null=True
    )

class PessoaJuridica(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14, null=True, blank=False, unique=True) #59.684.473/0001-07 | 59684473000107 14 Dig
    nome_fantasia = models.CharField(
        verbose_name='Nome Fantasia', 
        max_length=100, blank=True, null=True
    )
    razao_social = models.CharField(
        verbose_name='Razão Social', 
        max_length=100, blank=True, null=True
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

"""
class CategoriaGasto(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey('auth.User', related_name='tipogastos', on_delete=models.CASCADE) 
         
    class Meta:
        ordering = ('nome',)
"""

class Gasto(models.Model):
    criado = models.DateTimeField(auto_now_add=True) #VER COMO QUE DEIXA ISSO SEGURO QUE NAO POSSA SER ALTERADO
    #categoria = models.ForeignKey(TipoGasto, on_delete=models.CASCADE)
    tipo_gasto = models.IntegerField(choices=tipo_gasto.CHOICES, default=tipo_gasto.OUTROS)
    tipo_fluxo = models.IntegerField(choices=tipo_fluxo.CHOICES)
    usuario = models.ForeignKey('auth.User', related_name='gastos', on_delete=models.CASCADE) 
    quando = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)  #MELHOR MANEIRA DE REPRESTENTAR A MOEDA BRASILEIRA
    descricao = models.TextField(blank=True)
    
    class Meta:
        ordering = ('-quando',)

    @property
    def quando_formatado(self):
        return translate_date_en_to_pt(self.quando.strftime("%A %d %b %Y"))
 
    @property
    def valor_formatado(self):
        return valor_formatado(self.valor, self.tipo_fluxo )

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