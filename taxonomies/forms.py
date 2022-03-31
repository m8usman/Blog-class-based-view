from django import forms
from django.forms import ModelForm
from taxonomies.models import Tag, Category


class TagForm(ModelForm):

    # name = forms.CharField(required=True)

    class Meta:
        model = Tag
        fields = ['name', 'description']


class CategoryForm(ModelForm):

    # name = forms.CharField(attrs={'required': True})

    class Meta:
        model = Category
        fields = ['name', 'description']



