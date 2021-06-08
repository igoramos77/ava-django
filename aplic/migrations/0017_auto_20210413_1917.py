# Generated by Django 2.2.19 on 2021-04-13 22:17

import aplic.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0016_auto_20210413_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d', validators=[aplic.models.validate_file_extension], verbose_name='Foto'),
        ),
        migrations.AddField(
            model_name='professor',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d', validators=[aplic.models.validate_file_extension], verbose_name='Foto'),
        ),
    ]
