# Generated by Django 4.2.16 on 2024-11-19 03:52

import aplic.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_alter_entrega_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografo',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 420, 'width': 420}}, verbose_name='Foto'),
        ),
    ]
