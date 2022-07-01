from django.contrib import admin

from orders.models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    ordering = ("-id", )
    list_display = ("id", "user", "order_date_", "ordered",)
    list_display_links = ("id", )
    list_per_page = 20
    list_filter = ("ordered", "order_date", "user", )
    fieldsets = [
        ("General", {
            "fields": ["id", "ordered", "order_date"],
            "description": "General info"
        }),
        ("External Information", {
            "fields": ["user", "items"],
            "description": "Additional info"
        })
    ]
    readonly_fields = ["id", "order_date", "user", "items"]

    @staticmethod
    def order_date_(obj):
        return obj.order_date.strftime('%d %b %Y')


class OrderDetailsAdmin(admin.ModelAdmin):
    ordering = ("-id", )
    list_display = ("id", "user", "quantity", "ordered", "item")
    list_display_links = ("id", )
    list_per_page = 20
    list_filter = ("ordered", "user", )
    fieldsets = [
        ("General", {
            "fields": ["id", "ordered", "item", "quantity"],
            "description": "General info"
        }),
        ("External Information", {
            "fields": ["user"],
            "description": "Additional info"
        })
    ]
    readonly_fields = ["id"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailsAdmin)
