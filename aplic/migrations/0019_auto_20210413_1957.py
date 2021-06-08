# Generated by Django 2.2.19 on 2021-04-13 22:57

import aplic.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0018_auto_20210413_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path),
        ),
        migrations.AlterField(
            model_name='professor',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path),
        ),
    ]
