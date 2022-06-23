import string

from django import forms
import django_filters

from items.models import Item, Company


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
        fields = "__all__"
        exclude = ("registration_date", "image", )
