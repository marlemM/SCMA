from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def list_item(request):
    item = Item.objects.all()
    return render(request, 'item.html', {'item': item})


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_item')

    return render(request, 'item-form.html', {'form': form})


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('list_item')

    return render(request, 'item-form.html', {'form': form, 'item': item})


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('list_item')

    return render(request, 'item-delete-confirm.html', {'item': item})
