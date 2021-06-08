# Generated by Django 2.2.19 on 2021-04-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0019_auto_20210413_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='facebook',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='instagram',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='lattes',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Curriculo Lattes'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='linkedin',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Linkedin'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='twitter',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='professor',
            name='facebook',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='professor',
            name='instagram',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='professor',
            name='lattes',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Curriculo Lattes'),
        ),
        migrations.AddField(
            model_name='professor',
            name='linkedin',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Linkedin'),
        ),
        migrations.AddField(
            model_name='professor',
            name='twitter',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Twitter'),
        ),
    ]