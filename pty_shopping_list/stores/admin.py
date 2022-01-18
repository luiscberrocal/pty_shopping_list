from django.contrib import admin
from .models import StoreChain


# Register your models here.
@admin.register(StoreChain)
class ChainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'metadata', 'is_active', 'closed_on')
    list_editable = ('closed_on',)
