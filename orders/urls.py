from django.urls import path

from . import views

app_name = "orders_app"


urlpatterns = [
    path("orders/index/", views.index, name="orders-index"),
    path("orders-update-view/<pk>/", views.OrderUpdateView.as_view(), name="orders-update-view"),
    path("orders-delete-view/<pk>/", views.OrderDeleteView.as_view(), name="orders-delete-view"),
    path("orders-detail-view/<pk>/", views.OrderDetailView.as_view(), name="orders-detail-view"),
    path("active-orders-detail-view/<pk>/", views.ActiveOrderDetailView.as_view(), name="active-orders-detail-view"),
    path("orders-list-view/", views.OrderListView.as_view(), name="orders-list-view"),
    path("orders/", views.orders, name="orders"),
    path("order-details", views.order_details, name="order-details"),
    path("add-to-cart/<pk>/", views.add_to_cart, name="add-to-cart"),
    path("order-summary", views.OrderSummary.as_view(), name="order-summary"),
    path("remove-single-item-from-cart/<pk>/", views.remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path("complete-order", views.complete_order, name="complete-order"),
    path("active-orders", views.active_orders, name="active-orders"),
    path("completed-orders", views.completed_orders, name="completed-orders"),
    path("items-below-minimum-stock", views.below_minimum_stock, name="items-below-minimum-stock"),
    path("frequently-ordered", views.frequently_ordered, name="frequently-ordered"),
    ]
