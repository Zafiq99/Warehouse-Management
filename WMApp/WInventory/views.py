from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, InventoryItemForm, InboundItemForm, OutboundItemForm, AddItemForm
from .models import InventoryItem, Category, InboundItem, OutboundItem

class Index(TemplateView):
    template_name = "WInventory/index.html"

class Dashboard(LoginRequiredMixin, View):
    def get(self,request):
        items = InventoryItem.objects.all().order_by('id')

        return render(request, 'WInventory/dashboard.html', {'items' : items})
    
class Inbound(LoginRequiredMixin, View):
    def get(self,request):
        items = InboundItem.objects.all().order_by('id')

        return render(request, 'WInventory/inbound.html', {'items' : items})
    
class Outbound(LoginRequiredMixin, View):
    def get(self,request):
        items = OutboundItem.objects.all().order_by('id')

        return render(request, 'WInventory/outbound.html', {'items' : items})

class SignUpView(View):
    def get(self,request):
        form = UserRegisterForm()
        return render(request, 'WInventory/signup.html', {'form' : form})

    def post(self,request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
                )
            login(request,user)
            return redirect('index')
        
        return render(request, 'WInventory/signup.html', {'form' : form})

class AddItem(LoginRequiredMixin, CreateView):
    model = InventoryItem
    form_class = AddItemForm
    template_name = 'WInventory/add_item.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'WInventory/edit_item.html'
    success_url = reverse_lazy('dashboard')

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = 'WInventory/delete_item.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'items'

class EditInbound(LoginRequiredMixin, UpdateView):
    model = InboundItem
    form_class = InboundItemForm
    template_name = 'WInventory/edit_inbound.html'
    success_url = reverse_lazy('inbound')

class EditOutbound(LoginRequiredMixin, UpdateView):
    model = OutboundItem
    form_class = OutboundItemForm
    template_name = 'WInventory/edit_outbound.html'
    success_url = reverse_lazy('outbound')

#problem
def completeInbound(request, id):
    sku = request.GET.get('sku')

    inv_item = InventoryItem.objects.get(sku=sku)
    inb_item = InboundItem.objects.get(id=id)
    total = inv_item.quantity + inb_item.quantity
    inv_item.quantity = total
    inv_item.save()

    return redirect('inv_item')
