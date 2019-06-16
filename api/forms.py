from django import forms

from .models import QueryTest


class QueryTestForm(forms.ModelForm):
    class Meta:
        model = QueryTest
        fields = ('name', 'params', 'expected')
