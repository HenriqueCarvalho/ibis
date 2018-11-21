from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from api.utils import tipo_fluxo, tipo_gasto
from api.utils.date import translate_date_en_to_pt
from api.utils.string import *
from django.core.validators import MinValueValidator, RegexValidator
from decimal import Decimal

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

"""
class endereco(models.Model):
    criado = models.DateTimeField(auto_now_add=True) #VER COMO QUE DEIXA ISSO SEGURO QUE NAO POSSA SER ALTERADO
    usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    cep = models.CharField(
            max_length=8,
            validators=[
                    RegexValidator(
                        regex='^.{8}$',
                        message='CEP precisa ser 8 digitos.',
                        code='nomatch'
                    )
                ]
        ) #89026-385 8 Dig
    cidade = 
    estado =
    bairro =
    logradouro =
    numero = 
    complemento(opcional)
"""

"""
class Filiado(models.Model):

    #Campos obrigatorios: cnpj, razao_social, email, presidente_nome
    
    criado = models.DateTimeField(auto_now_add=True) #VER COMO QUE DEIXA ISSO SEGURO QUE NAO POSSA SER ALTERADO
    usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    cnpj = models.CharField(
        max_length=14,
        unique=True,
        validators=[
            RegexValidator(
                regex='^.{14}$',
                message='cnpj precisa ser 14 digitos.',
                code='nomatch'
            )
        ]
    )
    razao_social = models.CharField(verbose_name='Razão Social', max_length=100)
    sigla = models.CharField(max_length=100, blank=True) #opcional
    site = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=60)
    telefone_fixo = models.CharField(
        max_length=11,
        blank=True,
        validators=[
            RegexValidator(
                regex='^.{10}$',
                message='Telefone fixo precisa ser 10 digitos. Ex:(12) 1234-1234',
                code='nomatch'
            )
        ]
    ) #(86)3300-0123 #opcional 11 Dig
    celular = models.CharField(
        max_length=11,
        blank=True,
        validators=[
            RegexValidator(
                regex='^.{11}$',
                message='Celular precisa ser 11 digitos. Ex:(12) 91234-1234',
                code='nomatch'
            )
        ]
    ) #(86)93300-0123 #opcional 11 Dig
    presidente_nome = models.CharField(max_length=80)
    presidente_celular = models.CharField(
        max_length=11,
        blank=True,
        validators=[
            RegexValidator(
                regex='^.{11}$',
                message='Celular precisa ser 11 digitos. Ex:(12) 91234-1234',
                code='nomatch'
            )
        ]
    ) #(86)93300-0123 #opcional 11 Dig
"""


class Gasto(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    #categoria = models.ForeignKey(TipoGasto, on_delete=models.CASCADE)
    tipo_gasto = models.IntegerField(choices=tipo_gasto.CHOICES, default=tipo_gasto.OUTROS)
    tipo_fluxo = models.IntegerField(choices=tipo_fluxo.CHOICES)
    usuario = models.ForeignKey('auth.User', related_name='gastos', on_delete=models.PROTECT) 
    quando = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2, validators = [MinValueValidator(Decimal('0.01'))])
    descricao = models.TextField(blank=True)
    
    class Meta:
        ordering = ('-quando','-id')

    @property
    def criado_formatado(self):
        date = self.criado.strftime("%A, %d %b %Y")
        return date.replace(' Feira', '')

    @property
    def quando_formatado(self):
        date = self.quando.strftime("%A, %d %b %Y")
        return date.replace(' Feira', '')
 
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