from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from model_utils.models import TimeStampedModel


class Chain(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=80)
    is_active = models.BooleanField(_('Is active'), default=True)
    metadata = models.JSONField(_('Metadata'), null=True, blank=True)

    def __str__(self):
        return f'{self.name} -  {self.is_active}'

