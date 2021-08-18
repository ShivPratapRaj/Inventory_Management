from item.models import Item
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import HttpResponse, request
from .forms import ItemForm
from .models import Item
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.

def index(request):
    labels = []
    data = []
    sss = []
    lll = []

    #queryset = Item.objects.order_by('-quantity')[:5]
    queryset = Item.objects.all()
    #if request.user.is_authenticated:
    for i in queryset:
        labels.append(i.product_name)
        data.append(i.quantity)
        sss.append(i.sold)
        lll.append(i.left)
            
    return render(request, 'item/index.html',
                            {'labels': labels,
                            'data': data,
                            'sss':sss,
                            'lll':lll,
                            'name':request.user.username,
                            })
    # else:
    #     return HttpResponseRedirect('/account/login/')

def leftitems(request):
    labels = []
    data = []
    sss = []
    lll = []

    #queryset = Item.objects.order_by('-quantity')[:5]
    queryset = Item.objects.all()
    for i in queryset:
        labels.append(i.product_name)
        data.append(i.quantity)
        sss.append(i.sold)
        lll.append(i.left)
    return render(request, 'item/leftitems.html',
                  {'labels': labels,
                   'data': data,
                   'sss':sss,
                   'lll':lll,
                  })

def solditems(request):
    labels = []
    data = []
    sss = []
    lll = []

    #queryset = Item.objects.order_by('-quantity')[:5]
    queryset = Item.objects.all()
    for i in queryset:
        labels.append(i.product_name)
        data.append(i.quantity)
        sss.append(i.sold)
        lll.append(i.left)
    return render(request, 'item/solditems.html',
                  {'labels': labels,
                   'data': data,
                   'sss':sss,
                   'lll':lll,
                  })

def itemlist(request):
    all_items = Item.objects.all()
    return render(request, 'item/itemlist.html', {'all': all_items})

@login_required(login_url='/account/login/')
def additem(request):

    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/itemlist')
    return render(request, 'item/additem.html', {'form': form})
    #return HttpResponseRedirect('/itemlist/')


def update_item(request, id):
    if request.method == 'POST':
        pi = Item.objects.get(pk=id)
        fm = ItemForm(request.POST, instance=pi)
        # sold = request.POST["soldd"]
        # left = request.POST["leftt"]
        if fm.is_valid():
            fm.save()
            return redirect('/itemlist')
    else:
        pi = Item.objects.get(pk=id)
        fm = ItemForm(instance=pi)
    return render(request, 'item/update_item.html', {'form': fm})

@login_required
#@user_passes_test(lambda u: u.is_superuser)
@staff_member_required
def delete_item(request, id):
    if request.method == 'POST':
        pi = Item.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/itemlist')


def search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter(product_name__icontains=searched)
        return render(request, 'item/search_result.html',
                      {'searched': searched, 'items': items})
    else:
       return render(request, 'item/search_result.html')
