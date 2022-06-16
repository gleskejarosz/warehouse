from django.contrib import admin
from django.urls import path
import warehouse.views

urlpatterns = [
    path('homepage/', warehouse.views.HomePage.as_view(), name="homepage"),
    path('admin/', admin.site.urls),

]
