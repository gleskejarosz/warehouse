from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DeleteView, DetailView, ListView, UpdateView, View

from items.models import Item
from .models import Order, OrderDetail


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ("ordered",)
    template_name = "form.html"
    success_url = reverse_lazy("orders_app:active-orders")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.ordered = False
        order_items = self.object.items.all()
        order_items.update(ordered=False)
        for item in order_items:
            item.save()
        return super().post(request, *args, **kwargs)


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "items/delete.html"
    success_url = reverse_lazy("orders_app:orders-list-view")


class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/my_order.html"


class ActiveOrderDetailView(DetailView):
    model = Order
    template_name = "orders/my_active_order.html"


class OrderListView(ListView):
    template_name = "orders/orders.html"
    model = Order

    def get_ordering(self):
        ordering = self.request.GET.get("ordering", "-order_date")
        return ordering


@login_required
def orders(request):
    return render(
        request,
        template_name="orders/orders.html",
        context={"object_list": Order.objects.all().order_by("-order_date")},
    )


def order_details(request):
    return render(
        request,
        template_name="orders/order_details.html",
        context={"object_list": OrderDetail.objects.all().order_by("-item")},
    )


def index(request):
    return render(
        request,
        template_name="orders/index.html"
    )


class OrderSummary(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return render(self.request,
                          template_name='orders/order_summary.html',
                          context={
                              "order_summary": order,
                          },
                          )
        except ObjectDoesNotExist:
            return render(self.request,
                          template_name='orders/order_summary.html',
                          )


@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_item, created = OrderDetail.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print(order_qs)
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("orders_app:order-summary")
        else:
            order.items.add(order_item)
            return redirect("orders_app:order-summary")

    else:
        order = Order.objects.create(user=request.user, order_date=timezone.now())
        order.items.add(order_item)
        return redirect("orders_app:order-summary")


@login_required
def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderDetail.objects.filter(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
            else:
                order_item.quantity -= 1
                order.items.remove(order_item)
                order_item.ordered = True
            order_item.save()

            return redirect("orders_app:order-summary")
        else:
            return redirect("items_app:items-detail-view", pk=pk)
    else:
        return redirect("items_app:items-detail-view", pk=pk)


@login_required
def complete_order(request):
    order = Order.objects.get(user=request.user, ordered=False)
    order_items = order.items.all()
    order_items.update(ordered=True)
    for item in order_items:
        item.save()

    order.ordered = True
    order.save()

    return redirect("homepage")


@login_required
def active_orders(request):
    return render(
        request,
        template_name="orders/active_orders.html",
        context={"object_list": Order.objects.filter(ordered=False).order_by("-order_date")},
    )


def completed_orders(request):
    return render(
        request,
        template_name="orders/completed_orders.html",
        context={"object_list": Order.objects.filter(ordered=True).order_by("-order_date")},
    )


def below_minimum_stock(request):
    items_list = Item.objects.order_by('name').exclude(quantity__gte=F('minimum_quantity'))
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
        template_name='orders/items_below_min.html',
        context={'items': items_list},
    )


def frequently_ordered(request):
    from django.db.models import Sum
    object_list = OrderDetail.objects.filter(ordered="True").values(
        "item__producer_no").annotate(total_quantity=Sum("quantity")).order_by("-total_quantity")[:10]
    return render(
        request,
        template_name="orders/frequently_ordered.html",
        context={
            "object_list": object_list,
        },
    )
