from item.models import Item
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import HttpResponse, request
from .forms import ItemForm
from .models import Item


# Create your views here.

def index(request):
    return render(request, 'item/index.html')


def additem(request):
    
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/itemlist')
    return render(request, 'item/additem.html', {'form': form})
    #return HttpResponseRedirect('/itemlist/')


def itemlist(request):
    all_items = Item.objects.all()
    return render(request, 'item/itemlist.html',{'all': all_items})

def update_item(request, id):
    if request.method == 'POST':
        pi = Item.objects.get(pk=id)
        fm = ItemForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/itemlist')
    else:
        pi = Item.objects.get(pk=id)
        fm = ItemForm(instance=pi)
    return render(request, 'item/update_item.html', {'form':fm})


def delete_item(request, id):
    if request.method == 'POST':
        pi = Item.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/itemlist')

def search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter(product_name__icontains = searched)
        return render(request, 'item/search_result.html', 
        {'searched':searched, 'items':items})
    else:
       return render(request, 'item/search_result.html') 