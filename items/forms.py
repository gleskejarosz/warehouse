import string

from django import forms

from items.models import Company


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

