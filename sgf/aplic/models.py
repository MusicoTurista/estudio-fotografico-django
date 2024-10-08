from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename