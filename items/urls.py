from django.urls import path

from items import views

app_name = "items_app"


urlpatterns = [
    path('items/index/', views.index, name="index"),
    path("items-create-view/", views.ItemCreateView.as_view(), name="items-create-view"),
    path("items-detail-view/<pk>/", views.ItemDetailView.as_view(), name="items-detail-view"),
    path("items-update-view/<pk>/", views.ItemUpdateView.as_view(), name="items-update-view"),
    path("items-delete-view/<pk>/", views.ItemDeleteView.as_view(), name="items-delete-view"),
    path("items-list-view/", views.ItemListView.as_view(), name="items-list-view"),
    path('items/index/', views.index, name="items-index"),
    path('items/', views.items, name="items"),
    path('search/', views.SearchResultsView.as_view(), name="search-result"),
    path("company-delete-view/<pk>/", views.CompanyDeleteView.as_view(), name="company-delete-view"),
    path("company-detail-view/<pk>/", views.CompanyDetailView.as_view(), name="company-detail-view"),
    path("company-list-view/", views.CompanyListView.as_view(), name="company-list-view"),
    path("company-model-form-view/", views.CompanyModelFormView.as_view(), name="company-model-form-view"),
    path("company-template-view/", views.CompanyTemplateView.as_view(), name="company-template-view"),
    path("company-update-view/<pk>/", views.CompanyUpdateView.as_view(), name="company-update-view"),
    path('units-create-view/', views.UnitCreateView.as_view(), name="units-create-view"),
    path('units-detail-view/<pk>/', views.UnitDetailView.as_view(), name="units-detail-view"),
    path('units-update-view/<pk>/', views.UnitUpdateView.as_view(), name="units-update-view"),
    path('units-delete-view/<pk>/', views.UnitDeleteView.as_view(),
         name="units-delete-view"),
    path('units-list-view/', views.UnitListView.as_view(), name="units-list-view"),
    path('units/index/', views.index, name="units-index"),
    path('units/', views.units, name="units"),
    path('category-create-view/', views.CategoryCreateView.as_view(), name="category-create-view"),
    path('category-detail-view/<pk>/', views.CategoryDetailView.as_view(), name="category-detail-view"),
    path('category-update-view/<pk>/', views.CategoryUpdateView.as_view(), name="category-update-view"),
    path('category-delete-view/<pk>/', views.CategoryDeleteView.as_view(),
         name="category-delete-view"),
    path('category-list-view/', views.CategoryListView.as_view(), name="category-list-view"),
    path('category/index/', views.index, name="index"),
    path('category/', views.category, name="category"),
]
