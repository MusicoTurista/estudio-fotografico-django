# Generated by Django 4.2.16 on 2024-11-19 16:10

import aplic.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='data',
            field=models.DateField(blank=True, verbose_name='Data da entrega'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fotografo',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 420, 'width': 420}}, verbose_name='Foto'),
        ),
    ]
