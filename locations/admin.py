from django.contrib import admin

from locations.models import Location


class LocationAdmin(admin.ModelAdmin):
    ordering = ("location",)
    list_display = ("id", "location", "description",)
    list_display_links = ("id",)
    list_per_page = 20
    list_filter = ("description",)
    search_fields = ("location", "description", )
    fieldsets = [
        ("General", {
            "fields": ["id", "location", "description"],
        }),
    ]
    readonly_fields = ["id"]


admin.site.register(Location, LocationAdmin)
