from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="homepage"),
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
]
