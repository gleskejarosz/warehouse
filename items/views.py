from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, DeleteView, UpdateView, DetailView, CreateView

from .forms import CompanyModelForm, ItemModelForm
from .models import Company, Item, Unit, Category
from .filters import ItemFilter


def items(request):
    items_list = Item.objects.all().order_by("name")
    return render(
        request,
        template_name='items/items.html',
        context={'items': items_list},
    )


# class ItemCreateView(LoginRequiredMixin, CreateView):
#     model = Item
#     template_name = "form.html"
#     fields = "__all__"
#     success_url = reverse_lazy("items_app:items-list-view")

class ItemCreateView(LoginRequiredMixin, FormView):
    template_name = "form.html"
    form_class = ItemModelForm
    success_url = reverse_lazy("items_app:items-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class CompanyUpdateView(UpdateView):
    model = Company
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("items_app:companies")


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = "__all__"
    exclude = ("registration_date", )
    template_name = "form.html"
    success_url = reverse_lazy("items_app:items-list-view")


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = "items/delete.html"
    success_url = reverse_lazy("items_app:companies")


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "items/delete.html"
    success_url = reverse_lazy("items_app:items-list-view")


class CompanyTemplateView(TemplateView):
    template_name = "items/companies.html"
    extra_context = {"object_list": Company.objects.all()}


class CompanyDetailView(DetailView):
    model = Company
    template_name = "items/my_company.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/my_item.html"


class CompanyListView(ListView):
    template_name = "items/companies.html"
    model = Company
    paginate_by = 3

    # def change_pagination(self, number):
    #     if isinstance(number, int):
    #         self.paginate_by = number


class ItemListView(ListView):
    template_name = "items/items.html"
    model = Item

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'name')
        return ordering


class CompanyModelFormView(FormView):
    template_name = "form.html"
    form_class = CompanyModelForm
    success_url = reverse_lazy('items_app:companies')

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


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


class UnitCreateView(LoginRequiredMixin, CreateView):
    model = Unit
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("items_app:units")


class UnitDeleteView(LoginRequiredMixin, DeleteView):
    model = Unit
    template_name = "units/delete_units.html"
    success_url = reverse_lazy("items_app:units-list-view")


class UnitDetailView(DetailView):
    model = Unit
    template_name = "units/my_units.html"


class UnitListView(ListView):
    model = Unit
    template_name = "units/list_view_units.html"


class UnitUpdateView(LoginRequiredMixin, UpdateView):
    model = Unit
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("items_app:units")


def category(request):
    return render(
        request,
        template_name="category/category.html",
        context={"category": Category.objects.all()}
    )


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("items_app:category-list-view")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "category/delete_category.html"
    success_url = reverse_lazy("items_app:category-list-view")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category/my_category.html"


class CategoryListView(ListView):
    model = Category
    template_name = "category/list_view_category.html"


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ("name", "description")
    template_name = "form.html"
    success_url = reverse_lazy("items_app:category-list-view")


class SearchResultsView(ListView):
    model = Item
    template_name = "items/items_search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Item.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) |
            Q(producer_no__icontains=query) | Q(supplier_no__icontains=query) |
            Q(producer__name__icontains=query) | Q(supplier__name__icontains=query) |
            Q(category__name__icontains=query) | Q(unit__name__icontains=query)
        ).order_by('name')
        return object_list


def above_minimum_stock(request):
    items_list = Item.objects.order_by('-quantity').exclude(quantity__lte=0)
    page = request.GET.get('page', 1)

    paginator = Paginator(items_list, 10)
    try:
        items_list = paginator.page(page)
    except PageNotAnInteger:
        items_list = paginator.page(1)
    except EmptyPage:
        items_list = paginator.page(paginator.num_pages)
    return render(
        request,
        template_name='items/items_above_min.html',
        context={'items': items_list},
    )


def search(request):
    items_list = Item.objects.all().order_by('name')
    items_filter = ItemFilter(request.GET, queryset=items_list)
    return render(request, 'items/filter_list.html', {'filter': items_filter})

