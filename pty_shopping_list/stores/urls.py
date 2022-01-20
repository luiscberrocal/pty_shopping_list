from django.urls import path

from pty_shopping_list.stores.views import store_chain_create_view

app_name = 'stores'

urlpatterns = [
    #ChainStore CRUD urls
    path(r'chain-store/list/', chain_store_list_view, name='list-chain-store'),
    path(r'chain-store/create/', chain_store_create_view, name='create-chain-store'),
    path(r'chain-store/update/<int:pk>/', chain_store_update_view, name='update-chain-store'),
    path(r'chain-store/delete/<int:pk>/', chain_store_delete_view, name='delete-chain-store'),
    path(r'chain-store/<int:pk>/', chain_store_detail_view, name='detail-chain-store'),

]
