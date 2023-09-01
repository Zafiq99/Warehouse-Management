from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, Inbound, Outbound, AddItem, EditItem, DeleteItem, EditInbound, EditOutbound, completeInbound
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('inbound/', Inbound.as_view(), name='inbound'),
    path('outbound/', Outbound.as_view(), name='outbound'),
    path('add_item/', AddItem.as_view(), name='add_item'),
    path('edit_item/<int:pk>', EditItem.as_view(), name='edit_item'),
    path('edit_inbound/<int:pk>', EditInbound.as_view(), name='edit_inbound'),
    path('edit_outbound/<int:pk>', EditOutbound.as_view(), name='edit_outbound'),
    path('delete_item/<int:pk>', DeleteItem.as_view(), name='delete_item'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='WInventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='WInventory/logout.html'), name='logout'),

    #problem
    path('completeInbound/<int:id>', completeInbound, name='completeInbound'),
]