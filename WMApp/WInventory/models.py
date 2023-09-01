from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    sku = models.CharField(max_length=20, unique=True)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.sku
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class InboundItem(models.Model):
    reference = models.CharField(max_length=25)
    date_received = models.DateTimeField(blank=True, null=True)
    sku = models.ForeignKey('InventoryItem', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.reference

class OutboundItem(models.Model):
    reference = models.CharField(max_length=25)
    date_shipped = models.DateTimeField(blank=True, null=True)
    sku = models.ForeignKey('InventoryItem', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    destination = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.reference