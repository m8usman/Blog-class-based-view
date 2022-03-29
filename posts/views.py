from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from posts.models import Post, Comment
from users.models import User


class Posts(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'


class PostView(DetailView):
    model = Post
    template_name = 'posts/single-post.html'


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get('user_id'))
        text = request.POST.get('text')
        Comment(created_by=user, post=post, comment=text).save()
        messages.success(request, "Your comment has been added successfully.")

    return redirect('post', slug=slug)




