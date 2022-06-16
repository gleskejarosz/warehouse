from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, DeleteView, UpdateView, DetailView

from items.forms import CompanyModelForm
from items.models import Company


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = "items/delete.html"
    success_url = reverse_lazy("items_app:companies-template-view")


class CompanyDetailView(DetailView):
    model = Company
    template_name = "items/my_company.html"


class CompanyListView(ListView):
    # permission_required =
    template_name = "items/list_view.html"
    model = Company


class CompanyModelFormView(FormView):
    template_name = "form.html"
    form_class = CompanyModelForm
    success_url = 'homepage'

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class CompanyTemplateView(TemplateView):
    template_name = "items/companies.html"
    extra_context = {"companies": Company.objects.all()}


class CompanyUpdateView(UpdateView):
    model = Company
    fields = "__all__"
    template_name = "form.html"
