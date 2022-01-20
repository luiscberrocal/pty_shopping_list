from django.urls import path

from pty_shopping_list.stores.views import store_chain_create_view, store_chain_list_view, store_chain_update_view, \
    store_chain_delete_view, store_chain_detail_view

app_name = 'stores'

urlpatterns = [
   #StoreChain CRUD urls
   path(r'store-chain/list/', store_chain_list_view, name='list-store-chain'),
   path(r'store-chain/create/', store_chain_create_view, name='create-store-chain'),
   path(r'store-chain/update/<int:pk>/', store_chain_update_view, name='update-store-chain'),
   path(r'store-chain/delete/<int:pk>/', store_chain_delete_view, name='delete-store-chain'),
   path(r'store-chain/<int:pk>/', store_chain_detail_view, name='detail-store-chain'),
]
