from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from model_utils.models import TimeStampedModel


class StoreChain(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=80)
    # is_active = models.BooleanField(_('Is active'), default=True)
    metadata = models.JSONField(_('Metadata'), null=True, blank=True)
    closed_on = models.DateField(_('Closed on'), null=True, blank=True)

    @property
    def is_active(self):
        return self.closed_on is None

    def __str__(self):
        return f'{self.name} -  {self.is_active}'


class Location(TimeStampedModel):
    store_chain = models.ForeignKey(StoreChain, verbose_name=_('Store chain'), on_delete=models.PROTECT)
    name = models.CharField(_('Name'), max_length=80)
    address = models.TextField(_('Address'), null=True, blank=True)
    store_chain = models.ForeignKey(StoreChain, verbose_name=_('Store chain'), )
