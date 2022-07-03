from django.urls import path
from locations import views


app_name = "locations_app"


urlpatterns = [
    path('location/index/', views.index, name="location-index"),
    path('location-detail-view/<pk>/', views.LocationDetailView.as_view(), name="location-detail-view"),
    path('location-create-view/', views.LocationCreateView.as_view(), name="location-create-view"),
    path('location-update-view/<pk>/', views.LocationUpdateView.as_view(), name="location-update-view"),
    path('location-delete-view/<pk>/', views.LocationDeleteView.as_view(),
         name="location-delete-view"),
    path('location-list-view/', views.LocationListView.as_view(), name="location-list-view"),
    path('location/', views.location, name="location"),
    path('location-with-stock', views.location_with_stock, name="location-with-stock"),

]
