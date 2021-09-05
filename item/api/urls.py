from django.urls import path, include
from item.api import views


urlpatterns = [
    path('', views.itemList, name='item-list'),
    path('item-detail/<str:pk>/', views.itemDetail, name="item-detail"),
    path('item-create/', views.itemCreate, name="item-create"),
    path('item-update/<str:pk>/', views.itemUpdate, name="item-update"),
    path('item-delete/<str:pk>/', views.itemDelete, name="item-delete"),
]