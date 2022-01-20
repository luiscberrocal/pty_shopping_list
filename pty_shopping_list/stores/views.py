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


class StoreChainUpdateView(LoginRequiredMixin, UpdateView):
    model = StoreChain
    form_class = StoreChainForm
    success_url = reverse_lazy('stores:list-store-chain')


store_chain_update_view = StoreChainUpdateView.as_view()


class StoreChainListView(LoginRequiredMixin, ListView):
    model = StoreChain
    context_object_name = 'store_chain_list'
    paginate_by = 10


store_chain_list_view = StoreChainListView.as_view()


class StoreChainDeleteView(LoginRequiredMixin, DeleteView):
    model = StoreChain
    success_url = reverse_lazy('stores:list-store-chain')


store_chain_delete_view = StoreChainDeleteView.as_view()


class StoreChainDetailView(LoginRequiredMixin, DetailView):
    model = StoreChain


store_chain_detail_view = StoreChainDetailView.as_view()
