from django.forms import ModelForm
from django import forms


from .models import Comment, Post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        labels = {
            'body': 'Add your comment'
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'featured_image', 'tags', 'categories', 'is_published']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'categories': forms.CheckboxSelectMultiple(),
            'publish_from': forms.SelectDateWidget(),
            'publish_to': forms.SelectDateWidget(),
        }



