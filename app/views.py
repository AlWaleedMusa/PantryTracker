from django.shortcuts import render, redirect
from .models import Items
from django.shortcuts import get_object_or_404
from .forms import AddNewItem


# Create your views here.
def home(request):
    items = Items.objects.all()

    context = {"items": items}

    return render(request, "home.html", context)


def add_new_item(request):
    if request.method == "POST":
        form = AddNewItem(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    form = AddNewItem()

    context = {"form": form}

    return render(request, "add_new_item.html", context)


def edit_item(request, pk):
    item = get_object_or_404(Items, id=pk)
    if request.method == "POST":
        form = AddNewItem(request.POST, instance=item)
        if form.is_valid:
            form.save()
            return redirect("home")

    form = AddNewItem(instance=item)

    context = {"form": form}

    return render(request, "edit_item.html", context)

def delete_item(request, pk):
    item = get_object_or_404(Items, id=pk)
    item.delete()
    return redirect('home')


def add_item(request, pk):
    item = get_object_or_404(Items, id=pk)
    if item.item_count >= 0:
        item.item_count += 1
        item.save()

    return redirect("home")


def remove_item(request, pk):
    item = get_object_or_404(Items, id=pk)
    if item.item_count >= 1:
        item.item_count -= 1
        item.save()

    return redirect("home")
