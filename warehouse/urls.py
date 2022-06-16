from django.contrib import admin
from django.urls import include, path
import warehouse.views

urlpatterns = [
    path('homepage/', warehouse.views.HomePage.as_view(), name="homepage"),
    path('admin/', admin.site.urls),
    path('items/', include('items.urls'))

]
