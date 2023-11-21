# Generated by Django 4.2.7 on 2023-11-15 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dt_fim', models.DateTimeField(blank=True, null=True)),
                ('dt_inicio', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('valor_acumulado', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'jogo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loterica',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('saldo', models.FloatField(blank=True, null=True)),
                ('telefone', models.CharField(blank=True, max_length=255, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'loterica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('telefone', models.CharField(blank=True, max_length=255, null=True)),
                ('num_cadastro', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'funcionario',
                'managed': True,
            },
        ),
    ]
