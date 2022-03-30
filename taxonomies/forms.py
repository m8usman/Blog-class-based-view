from django.forms import ModelForm
from taxonomies.models import Tag, Category


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'description']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
