from item.views import index, itemlist
from django.urls import path
from item import views


urlpatterns = [
    path('',views.index,name='index'),
    path('itemlist/',views.itemlist,name='itemlist'),
    path('delete/<int:id>/',views.delete_item,name="delete_item"),
    path('<int:id>/', views.update_item, name="update_item"),
]