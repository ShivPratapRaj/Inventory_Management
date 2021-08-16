from django.contrib import admin
from django.http import request
from django.urls import path
from django.urls.conf import include
from item import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('item.urls')),
    path('account/', include(('account.urls', 'account'), namespace='account')),
]
