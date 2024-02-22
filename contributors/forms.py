from django import forms
from .models import Contributor


class ContributorModelForm(forms.ModelForm):
    class Meta:
        model = Contributor
        fields = (
            "name",
            "editor",
            "email",
        )