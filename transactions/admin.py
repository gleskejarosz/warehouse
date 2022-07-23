from django.contrib import admin

from transactions.models import TransactionType, TransactionArchive


class TransactionTypeAdmin(admin.ModelAdmin):
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


class TransactionArchiveAdmin(admin.ModelAdmin):
    ordering = ("-when", )
    list_display = ("id", "transaction", "item", "who", "quantity", "quantity_after", "when", )
    list_per_page = 30
    list_filter = ("transaction", "who", )
    fieldsets = [
        ("General", {
            "fields": ["id", "transaction", "item", "who", "quantity", "quantity_after", "when"],
        }),
    ]
    readonly_fields = ["id", "transaction", "item", "who", "quantity", "quantity_after", "when"]


admin.site.register(TransactionType, TransactionTypeAdmin)
admin.site.register(TransactionArchive, TransactionArchiveAdmin)
