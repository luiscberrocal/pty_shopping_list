from django.contrib import admin
from .models import Chain


# Register your models here.
@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'metadata')
