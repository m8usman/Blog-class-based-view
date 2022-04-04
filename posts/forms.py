from django.forms import ModelForm
from django import forms
from .models import Comment, Post
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        labels = {
            'body': 'Add your comment'
        }


class PostForm(ModelForm):
    publish_from = forms.SplitDateTimeField(required=False, widget=AdminSplitDateTime())
    publish_to = forms.SplitDateTimeField(required=False, widget=AdminSplitDateTime())

    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'featured_image', 'tags', 'categories', 'publish_from', 'publish_to', 'is_published' ]

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'categories': forms.CheckboxSelectMultiple(),
            'publish_from': AdminSplitDateTime(),
            'publish_to': AdminSplitDateTime(),
        }



