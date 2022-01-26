from django import forms
from django.utils.translation import ugettext_lazy as _

from pty_shopping_list.stores.models import StoreChain


class StoreChainForm(forms.ModelForm):
    SUPER_MARKET_TYPE = 'SUPER_MARKET'
    DRUG_STORE_TYPE = 'DRUG_STORE'
    OTHER_TYPE = 'OTHER'
    TYPE_CHOICES = (
        (SUPER_MARKET_TYPE, _('Supermarket')),
        (DRUG_STORE_TYPE, _('Drug store')),
        (OTHER_TYPE, _('Other')),
    )
    chain_type = forms.ChoiceField(label=_('Chain type'), choices=TYPE_CHOICES,)

    class Meta:
        model = StoreChain
        fields = ('id', 'name', 'closed_on', 'metadata')
        widgets = {'closed_on': forms.DateInput(attrs={'type': 'date'}),
                   'metadata': forms.HiddenInput()}

    def clean(self):
        cleaned_data =super(StoreChainForm, self).clean()
        cleaned_data['metatadata'] = {'chain_type': cleaned_data['chain_type']}
        return cleaned_data

    #def save(self, force_insert=False, force_update=False):
