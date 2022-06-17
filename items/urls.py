from django.urls import path

from . import views

app_name = "items_app"

urlpatterns = [
    path("items-create-view/", views.ItemCreateView.as_view(), name="items-create-view"),
    path("items-detail-view/<pk>/", views.ItemDetailView.as_view(), name="items-detail-view"),
    path("items-update-view/<pk>/", views.ItemUpdateView.as_view(), name="items-update-view"),
    path("items-delete-view/<pk>/", views.ItemDeleteView.as_view(),
         name="items-delete-view"),
    path('items-list-view/', views.ItemListView.as_view(), name="items-list-view"),
    path('items/index/', views.index, name="index"),
    path('items/', views.items, name="items"),
    path('units-create-view/', views.UnitCreateView.as_view(), name="units-create-view"),
    path('units-detail-view/<pk>/', views.UnitDetailView.as_view(), name="units-detail-view"),
    path('units-update-view/<pk>/', views.UnitUpdateView.as_view(), name="units-update-view"),
    path('units-delete-view/<pk>/', views.UnitDeleteView.as_view(),
         name="units-delete-view"),
    path('units-list-view/', views.UnitListView.as_view(), name="units-list-view"),
    path('units/index/', views.index, name="index"),
    path('units/', views.units, name="units"),
]
