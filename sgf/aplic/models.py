from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Fotografo(models.Model):
    Sexos = (
        ('Masculino', _('Masculino')),
        ('Feminino', _('Feminino')),
        ('Outro', _('Outro')),
    )
    cpf = models.CharField(_('CPF'), max_length=14, null=False)
    telefone = models.CharField(_('Telefone'), max_length=14)
    nome = models.CharField(_('Nome'), max_length=100, null=False)
    sexo = models.CharField(_('Sexo'), blank=True, null=False, choices=Sexos)
    imagem = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 420, 'crop': True}})
    class Meta:
        verbose_name = _('Fotografo')
        verbose_name_plural = _('Fotografos')

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    Tipos = (
        ('Camera', _('Camera')),
        ('Lente', _('Lente')),
        ('Flash', _('Flash')),
        ('Iluminacao', _('Iluminação')),
        ('Memoria', _('Memória')),
        ('Outros', _('Outros')),
    )
    Estados = (
        ('Funcional', _('Funcional')),
        ('Defeituoso', _('Defeituoso')),
        ('Em Conserto', _('Em Conserto')),
    )
    modelo = models.CharField(_('Modelo'), max_length=100, null=False)
    tipo = models.CharField(_('Tipo'), blank=True, null=False, choices=Tipos)
    estado = models.CharField(_('Estado'), blank=True, null=False, choices=Estados)
    data_fabric = models.DateField(_('Data de Fabricação'), blank=True, null=True, help_text=_('Formato DD/MM/AAAA'))
    fotografo = models.ForeignKey(Fotografo, related_name='Equipamentos', on_delete=models.CASCADE)
    class Meta:
        verbose_name = _('Equipamento')
        verbose_name_plural = _('Equipamentos')

    def __str__(self):
        return self.modelo

class Departamento(models.Model):
    tipo = models.CharField(_('Tipo'), max_length=100, null=False)
    descricao = models.CharField(_('Descrição'), max_length=500)
    fotografos = models.ManyToManyField(Fotografo)
    class Meta:
        verbose_name = _('Departamento')
        verbose_name_plural = _('Departamentos')

    def __str__(self):
        return self.tipo

class CategoriaEvento(models.Model):
    tipo = models.CharField(_('Tipo'), max_length=100, null=False)
    descricao = models.CharField(_('Descrição'), max_length=500)
    valor_foto = models.FloatField(_('Valor Foto'), null=False,)
    valor_hora = models.FloatField(_('Valor Hora'), null=False,)
    class Meta:
        verbose_name = _('Categoria de evento')
        verbose_name_plural = _('Categorias de evento')

    def __str__(self):
        return self.tipo

class Evento(models.Model):
    Pacotes = (
        ('Quantidade de fotos', _('Quantidade de fotos')),
        ('Tempo de serviço', _('Tempo de serviço')),
    )
    cliente = models.ForeignKey(User, related_name='Cliente', on_delete=models.CASCADE)
    data = models.DateTimeField('Data/Hora', blank=True, null=False)
    categoria = models.ForeignKey(CategoriaEvento, related_name='Categoria', on_delete=models.RESTRICT)
    pacote_tipo = models.CharField(_('Pacote'), blank=True, null=False, choices=Pacotes)
    fotografos = models.ManyToManyField(Fotografo, blank=True)

    class Meta:
        verbose_name = _('Evento')
        verbose_name_plural = _('Eventos')

    def __str__(self):
        return f'{self.cliente} - {self.data}'


class Entrega(models.Model):
    evento = models.ForeignKey(Evento, related_name='Evento', on_delete=models.CASCADE)
    data = models.DateField('Data da entrega', blank=True, null=False)
    class Meta:
        verbose_name = _('Entrega')
        verbose_name_plural = _('Entregas')

    def __str__(self):
        return f'{self.evento} - {self.data}'

class Foto(models.Model):
    Entregas = (
        ('Digital', _('Digital')),
        ('Revelada 20x30', _('Revelada 20x30')),
        ('Revelada 30x40', _('Revelada 30x40')),
        ('Revelada 40x60', _('Revelada 40x60')),
        ('Revelada 60x90', _('Revelada 60x90')),
    )
    imagem = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path)
    entrega_tipo = models.CharField(_('Tipo de entrega'), blank=True, null=False, choices=Entregas)
    entrega = models.ForeignKey(Entrega, related_name='Entrega', on_delete=models.CASCADE)
    class Meta:
        verbose_name = _('Foto')
        verbose_name_plural = _('Fotos')

    def __str__(self):
        return f'{self.entrega_tipo}'