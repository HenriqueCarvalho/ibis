from django.db import models
#from datetime import datetime

class Gasto(models.Model):
    
    criado = models.DateTimeField(auto_now_add=True)
    quando = models.DateTimeField(auto_now_add=True)
    #quando = models.DateTimeField(default=datetime.now)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)     #procurar melhor representação da moeda brasileira
    categoria = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    class Meta:
        #ordenação dos gastos
        ordering = ('quando',)

    # Depois de criar o model roda as linhas de comando
    # python manage.py makemigrations [NOME DO APP]
    # python manage.py migrate
