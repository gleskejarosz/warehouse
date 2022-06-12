from django.contrib import admin

from items.models import Item, Unit, Company, Category

admin.site.register(Item)
admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(Company)
