from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateTimeInput
from .models import InventoryItem, Category, InboundItem, OutboundItem

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class InventoryItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0, disabled=True)
    name = forms.CharField(disabled=True)
    sku = forms.CharField(disabled=True)

    class Meta:
        model = InventoryItem
        fields = ['name','category','sku','quantity','location','supplier']

class AddItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)

    class Meta:
        model = InventoryItem
        fields = ['name','category','sku','quantity','location','supplier']

class InboundItemForm(forms.ModelForm):
    reference = forms.CharField(disabled=True)
    date_received = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    sku = forms.ModelChoiceField(queryset=InventoryItem.objects.all(), initial=0,disabled=True)
    quantity = forms.IntegerField(disabled=True)

    class Meta:
        model = InboundItem
        fields = ['reference','date_received','sku','quantity','location','remarks']
        
class OutboundItemForm(forms.ModelForm):
    reference = forms.CharField(disabled=True) 
    date_shipped = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    sku = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0, disabled=True)
    quantity = forms.IntegerField(disabled=True)
    class Meta:
        model = OutboundItem
        fields = ['reference','date_shipped','sku','quantity','destination','remarks']
        