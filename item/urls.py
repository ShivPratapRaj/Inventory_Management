from item.views import additem, index, itemlist, leftitems, solditems
from django.urls import path
from item import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('additem/', views.additem, name='additem'),
    path('itemlist/', views.itemlist, name='itemlist'),
    path('delete/<int:id>/', views.delete_item, name="delete_item"),
    path('<int:id>/', views.update_item, name="update_item"),
    path('search_result', views.search_result, name="search_result"),
    path('leftitems/', views.leftitems, name="leftitems"),
    path('solditems/', views.solditems, name="solditems"),

]
