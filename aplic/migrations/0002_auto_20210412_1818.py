# Generated by Django 2.2.19 on 2021-04-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='dia_da_semana',
            field=models.CharField(choices=[('Segunda-feira', 'Segunda-feira'), ('Terça-feira', 'Terça-feira'), ('Quarta-feira', 'Quarta-feira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], default='', max_length=13, verbose_name='Dia da Semana'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='horario_de_inicio',
            field=models.TimeField(blank=True, null=True, verbose_name='horário de início'),
        ),
        migrations.AddField(
            model_name='turma',
            name='horario_de_termino',
            field=models.TimeField(blank=True, null=True, verbose_name='horário de término'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='turma',
            field=models.CharField(max_length=10, verbose_name='Nome da Turma'),
        ),
    ]
