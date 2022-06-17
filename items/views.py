from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, DeleteView, UpdateView, DetailView, CreateView

from items.forms import CompanyModelForm
from items.models import Company, Item


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


class CompanyUpdateView(UpdateView):
    model = Company
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("items_app:company-list-view")


class ItemUpdateView(UpdateView):
    model = Item
    fields = ("name", "description", "category",
              "unit", "quantity", "producer", "producer_no", "supplier", "supplier_no",
              "minimum_quantity", "minimum_order")
    template_name = "form.html"
    success_url = reverse_lazy("items_app:items-list-view")


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = "items/delete.html"
    success_url = reverse_lazy("items_app:companies-template-view")


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "items/delete.html"
    success_url = reverse_lazy("items_app:items-list-view")


class CompanyTemplateView(TemplateView):
    template_name = "items/companies.html"
    extra_context = {"companies": Company.objects.all()}


class CompanyDetailView(DetailView):
    model = Company
    template_name = "items/my_company.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/my_item.html"


class CompanyListView(ListView):
    # permission_required =
    template_name = "items/list_view.html"
    model = Company


class ItemListView(ListView):
    template_name = "items/list_view.html"
    model = Item


class CompanyModelFormView(FormView):
    template_name = "form.html"
    form_class = CompanyModelForm
    success_url = 'homepage'

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


def index(request):
    return render(
        request,
        template_name="items/index.html"
    )
