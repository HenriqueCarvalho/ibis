from django.db import models

class Gasto(models.Model):
    
    criado = models.DateTimeField(auto_now_add=True) #VER COMO QUE DEIXA ISSO SEGURO QUE NAO POSSA SER ALTERADO
    categoria = models.CharField(max_length=100)
    quando = models.DateTimeField(auto_now_add=True)
    #quando = models.DateTimeField(default=datetime.now)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)  #MELHOR MANEIRA DE REPRESTENTAR A MOEDA BRASILEIRA
    descricao = models.TextField(blank=True)

    class Meta:
        #ordenação dos gastos
        ordering = ('quando',)

    # Depois de criar o model roda as linhas de comando
    # python manage.py makemigrations [NOME DO APP]
    # python manage.py migrate