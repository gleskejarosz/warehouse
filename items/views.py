from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from items.models import Item, Unit


def items(request):
    return render(
        request,
        template_name="items/items.html",
        context={"items": Item.objects.all()}
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


def units(request):
    return render(
        request,
        template_name="units/units.html",
        context={"units": Unit.objects.all()}
    )


class UnitCreateView(CreateView):
    model = Unit
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("items_app:units-list-view")


class UnitDeleteView(DeleteView):
    model = Unit
    template_name = "units/delete_units.html"
    success_url = reverse_lazy("items_app:units-list-view")


class UnitDetailView(DetailView):
    model = Unit
    template_name = "units/my_units.html"


class UnitListView(ListView):
    model = Unit
    template_name = "units/list_view_units.html"


class UnitUpdateView(UpdateView):
    model = Unit
    fields = ("unit", "description")
    template_name = "form.html"
    success_url = reverse_lazy("items_app:units-list-view")
