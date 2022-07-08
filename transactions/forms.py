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
    amount = PositiveNumberValue()


class AmountTransactionFormInt(forms.Form):
    amount = PositiveNumberInt()


