# Generated by Django 5.1.1 on 2024-10-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0007_categoriaevento_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='hora',
            field=models.TimeField(blank=True, default='00:00:00', verbose_name='Hora'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateField(blank=True, help_text='Formato DD/MM/AAAA', verbose_name='Data'),
        ),
    ]