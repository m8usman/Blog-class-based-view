from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from django.contrib import messages

from posts.forms import PostForm
from posts.models import Post, Comment
from taxonomies.models import Category, Tag
from users.models import User


class Posts(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    paginate_by = 6


class PostView(DetailView):
    model = Post
    template_name = 'posts/single-post.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get('user_id'))
        text = request.POST.get('text')
        Comment(created_by=user, post=post, comment=text).save()
        messages.success(request, "Your comment has been added successfully.")

    return redirect('post', slug=slug)


class DashboardView(TemplateView):
    template_name = 'posts/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.count()
        comments = Comment.objects.count()
        tags = Tag.objects.count()
        categories = Category.objects.count()
        context = {'posts': posts, 'comments': comments, 'tags': tags, 'categories': categories}
        return context





