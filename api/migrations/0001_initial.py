# Generated by Django 2.1.2 on 2018-10-18 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('quando', models.DateTimeField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('descricao', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('quando',),
            },
        ),
        migrations.CreateModel(
            name='TipoGasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('criado',),
            },
        ),
        migrations.AddField(
            model_name='gasto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TipoGasto'),
        ),
    ]
