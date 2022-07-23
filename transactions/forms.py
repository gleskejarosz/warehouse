import django_filters
from django.core.exceptions import ValidationError

from django import forms


from items.models import Item


def positive_number_validator(value: float):

    if value <= 0:
        raise ValidationError("Amount has to be greater than 0!")


class PositiveNumberValue(forms.FloatField):

    def validate(self, value):
        super().validate(value)
        if value <= 0:
            raise ValidationError("Amount has to be greater than 0!")


class PositiveNumberInt(forms.FloatField):

    def validate(self, value):
        super().validate(value)

        print(type(value))
        if value <= 0:
            raise ValidationError("Amount has to be greater than 0!")

        if not value.is_integer():
            raise ValidationError("Amount has to be Integer")


class ItemTransactionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="contains", label="Name")
    description = django_filters.CharFilter(lookup_expr="contains", label="Description")
    producer_no = django_filters.CharFilter(lookup_expr="contains", label="Producer No")
    supplier_no = django_filters.CharFilter(lookup_expr="contains", label="Supplier No")
    bin = django_filters.CharFilter(lookup_expr="contains", label="Bin")

    class Meta:
        model = Item
        fields = [
            "name",
            "producer_no",
            "description",
            "category",
            "producer",
            "supplier",
            "supplier_no",
            "location",
            "bin"
        ]


class AmountTransactionForm(forms.Form):
    amount = PositiveNumberValue()


class AmountTransactionFormInt(forms.Form):
    amount = PositiveNumberInt()


