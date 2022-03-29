from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from posts.forms import CommentForm
from posts.models import Post


class Posts(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'


class Post(DetailView, FormMixin):
    model = Post
    form_class = CommentForm
    template_name = 'posts/single-post.html'

    def form_valid(self, form, request):
        comment = form.save(commit=False)
        comment.post = self.get_object()
        comment.created_by = request.user
        comment.save()

        messages.success(request, 'Your comment was successfully submitted!')

        return super().form_valid(form)



