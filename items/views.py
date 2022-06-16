from django.views.generic import TemplateView, ListView, FormView

from items.forms import CompanyModelForm
from items.models import Company


class CompanyTemplateView(TemplateView):
    template_name = "items/companies.html"
    extra_context = {"companies": Company.objects.all()}


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
