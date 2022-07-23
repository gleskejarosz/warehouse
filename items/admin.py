from django.contrib import admin

from items.models import Item, Unit, Company, Category


class CategoryAdmin(admin.ModelAdmin):
    ordering = ("name", )
    list_display = ("id", "name", "description", )
    list_display_links = ("id", )
    list_per_page = 20
    list_filter = ("name", )
    fieldsets = [
        ("General", {
            "fields": ["id", "name", "description"],
        }),
    ]
    readonly_fields = ["id"]


class ItemAdmin(admin.ModelAdmin):
    ordering = ("producer_no", )
    list_display = ("id", "name", "description", "category", "unit", "quantity", "location",
                    "bin", "producer", "supplier", )
    list_display_links = ("name", )
    list_per_page = 50
    list_filter = ("category", "location", "producer", "supplier", )
    search_fields = ("description", "bin", )
    fieldsets = [
        ("General", {
            "fields": ["id", "name", "description", "category", "registration_date", "unit", "quantity", "location",
                       "bin", "minimum_order"],
        }),
        ("Additional Information", {
            "fields": ["producer", "producer_no", "supplier", "supplier_no", "minimum_quantity"],
        })
    ]
    readonly_fields = ["id", "registration_date"]


class UnitAdmin(admin.ModelAdmin):
    ordering = ("name", )
    list_display = ("id", "name", "description", )
    list_display_links = ("id", )
    list_per_page = 20
    list_filter = ("name", )
    fieldsets = [
        ("General", {
            "fields": ["id", "name", "description"],
        }),
    ]
    readonly_fields = ["id"]


class CompanyAdmin(admin.ModelAdmin):
    ordering = ("name", )
    list_display = ("id", "name", "email", "phone_no", "contact_person", )
    list_display_links = ("name", )
    list_per_page = 30
    fieldsets = [
        ("General", {
            "fields": ["id", "name", "email", "phone_no", "contact_person", "website", "minimum_order_value"],
        }),
    ]
    readonly_fields = ["id"]


admin.site.register(Item, ItemAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
