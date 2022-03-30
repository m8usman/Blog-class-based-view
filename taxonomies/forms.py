from django.forms import ModelForm
from taxonomies.models import Tag


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'description']
