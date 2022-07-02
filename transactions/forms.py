import django_filters

from django import forms


from items.models import Item


class ItemTransactionFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = [
            "name",
            "producer_no",
            "description",
            "category",
            "producer",
            "supplier",
        ]


class AmountTransactionForm(forms.Form):
    amount = forms.IntegerField()


