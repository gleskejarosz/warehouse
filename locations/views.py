from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView

from items.models import Item
from locations.models import Location


def location(request):
    return render(
        request,
        template_name="location/location.html",
        context={"location": Location.objects.all().order_by('location')}
    )


def index(request):
    return render(
        request,
        template_name="location/index.html"
    )


class LocationDetailView(DetailView):
    model = Location
    template_name = "location/my_location.html"


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("locations_app:location-list-view")


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    template_name = "location/delete_location.html"
    success_url = reverse_lazy("locations_app:location-list-view")


class LocationListView(ListView):
    model = Location
    template_name = "location/list_view_location.html"


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ("location", "description")
    template_name = "form.html"
    success_url = reverse_lazy("locations_app:location-list-view")


def location_with_stock(request):
    locations_list = Item.objects.order_by('location').exclude(location=None)
    page = request.GET.get('page', 1)

    paginator = Paginator(locations_list, 10)
    try:
        locations_list = paginator.page(page)
    except PageNotAnInteger:
        locations_list = paginator.page(1)
    except EmptyPage:
        locations_list = paginator.page(paginator.num_pages)
    return render(
        request,
        template_name='location/location_with_stock.html',
        context={'items': locations_list},
    )
