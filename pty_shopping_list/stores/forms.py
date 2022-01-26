from django import forms

from pty_shopping_list.stores.models import StoreChain


class StoreChainForm(forms.ModelForm):
    class Meta:
        model = StoreChain
        fields = ('id', 'name', 'closed_on')
        widgets = {'closed_on': forms.DateInput(attrs={'type': 'date'})}
