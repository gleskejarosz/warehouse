import string

from django import forms
import django_filters
from django.forms import ModelChoiceField

from items.models import Item, Company
from locations.models import Location


class ItemModelForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = ["quantity"]


class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = []

    def clean_name(self):
        return string.capwords(self.cleaned_data["name"])

    def clean_contact_person(self):
        return string.capwords(self.cleaned_data["contact_person"])

    def clean_email(self):
        return self.cleaned_data["email"].lower()


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        exclude = (
            "registration_date",
            "image",
        )
