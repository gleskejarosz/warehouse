from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from items.models import Item


def items(request):
    return render(
        request,
        template_name='items/items.html',
        context={'items': Item.objects.all()}
    )


class ItemCreateView(CreateView):
    model = Item
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("items_app:items-list-view")


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "items/delete.html"
    success_url = reverse_lazy("items_app:items-list-view")


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/my_item.html"


class ItemListView(ListView):
    template_name = "items/list_view.html"
    model = Item


class ItemUpdateView(UpdateView):
    model = Item
    fields = ("name", "description", "category",
              "unit", "quantity", "producer", "producer_no", "supplier", "supplier_no",
              "minimum_quantity", "minimum_order")
    template_name = "form.html"
    success_url = reverse_lazy("items_app:items-list-view")


def index(request):
    return render(
        request,
        template_name="items/index.html"
    )

