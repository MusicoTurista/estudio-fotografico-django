# Generated by Django 5.1.1 on 2024-10-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_alter_fotografo_cpf_alter_fotografo_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografo',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')], verbose_name='Sexo'),
        ),
    ]