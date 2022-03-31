from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView

from .forms import TagForm, CategoryForm
from .models import Tag, Category


class TagListView(CreateView, ListView):
    model = Tag
    form_class = TagForm
    template_name = 'taxonomies/tags.html'
    context_object_name = 'tags'
    success_url = 'tags'
    paginate_by = 6

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CategoryListView(CreateView, ListView):
    model = Category
    form_class = CategoryForm
    template_name = 'taxonomies/categories.html'
    context_object_name = 'categories'
    success_url = 'categories'
    paginate_by = 6

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TagUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'taxonomies/tag_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tag = self.get_object()
        if self.request.user == tag.created_by:
            return True
        return False


class TagDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tag
    success_url = '/tags'

    def test_func(self):
        tag = self.get_object()
        if self.request.user == tag.created_by:
            return True
        return False


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'taxonomies/tag_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.created_by:
            return True
        return False


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = '/tags'

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.created_by:
            return True
        return False



