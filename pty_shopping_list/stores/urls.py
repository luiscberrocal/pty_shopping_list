from django.urls import path

from pty_shopping_list.stores.views import store_chain_create_view

app_name = 'stores'

urlpatterns = [
    path(r'chain/create', store_chain_create_view, name='create-chain-store')
]
