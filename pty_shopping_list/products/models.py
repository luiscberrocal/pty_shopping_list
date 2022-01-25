from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class Brand(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=80, unique=True)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    brand = models.ForeignKey(Brand, related_name='products', verbose_name=_('Brand'),
                              on_delete=models.PROTECT)
    name = models.CharField(_("Name"), max_length=80)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=8)
