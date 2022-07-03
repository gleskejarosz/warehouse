import django_filters
from django.core.exceptions import ValidationError

from django import forms


from items.models import Item


def positive_number_validator(value: float):
    if value <= 0:
        raise ValidationError("Quantity has to be greater than 0!")


class PositiveNumberField(forms.IntegerField):
    def validate(self, value):
        super().validate(value)
        if value <= 0:
            raise ValidationError("Quantity has to be greater than 0!")


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
    amount = PositiveNumberField()


