from django.contrib import admin
from .models import InventoryItem, Category, InboundItem, OutboundItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['name','category','sku','quantity','location','supplier']
    list_filter = ['category']
    search_fields = ['name']

admin.site.register(Category)
admin.site.register(InboundItem)
admin.site.register(OutboundItem)

