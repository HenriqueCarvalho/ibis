# Generated by Django 2.1.2 on 2018-10-29 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('tipo_gasto', models.IntegerField(choices=[(0, 'Água'), (1, 'Comida'), (2, 'Energia'), (3, 'Internet'), (4, 'Mensalidade'), (5, 'Telefone'), (6, 'Transporte'), (7, 'Viagem'), (8, 'Outros')], default=8)),
                ('tipo_fluxo', models.IntegerField(choices=[(0, 0), (1, 1)])),
                ('quando', models.DateTimeField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('descricao', models.TextField(blank=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gastos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('quando',),
            },
        ),
    ]
