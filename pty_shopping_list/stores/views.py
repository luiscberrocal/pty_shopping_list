from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from pty_shopping_list.stores.forms import StoreChainForm
from pty_shopping_list.stores.models import StoreChain


class StoreChainCreateView(CreateView):
    model = StoreChain
    form_class = StoreChainForm
    success_url = '/'


store_chain_create_view = StoreChainCreateView.as_view()
