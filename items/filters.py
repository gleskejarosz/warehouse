import django_filters
from items.models import Item


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="contains", label="Name")
    description = django_filters.CharFilter(lookup_expr="contains", label="Description")
    producer_no = django_filters.CharFilter(lookup_expr="contains", label="Producer No")
    supplier_no = django_filters.CharFilter(lookup_expr="contains", label="Supplier No")
    bin = django_filters.CharFilter(lookup_expr="contains", label="Bin")

    class Meta:
        model = Item
        exclude = ("registration_date", "image", )
