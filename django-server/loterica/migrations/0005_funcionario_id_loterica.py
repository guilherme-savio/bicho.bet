# Generated by Django 4.2.7 on 2023-11-16 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loterica', '0004_alter_funcionario_num_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='id_loterica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='loterica.loterica', verbose_name='Lotérica'),
        ),
    ]
