from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Fotografo(models.Model):
    cpf = models.IntegerField(_('CPF'), null=False)
    telefone = models.IntegerField(_('Telefone'), max_length=15)
    nome = models.CharField(_('Nome'), max_length=100, null=False)
    sexo = models.CharField(_('Sexo'), max_length=20)
    imagem = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    class Meta:
        verbose_name = _('Fotografo')
        verbose_name_plural = _('Fotografos')

    def __str__(self):
        return self.nome