from django.views.generic import ListView
from django.views.generic.edit import FormMixin, CreateView

from .forms import TagForm, CategoryForm
from .models import Tag, Category


class TagListView(CreateView, ListView):
    model = Tag
    form_class = TagForm
    template_name = 'taxonomies/tags.html'
    context_object_name = 'tags'
    success_url = 'tags'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CategoryListView(CreateView, ListView):
    model = Category
    form_class = CategoryForm
    template_name = 'taxonomies/categories.html'
    context_object_name = 'categories'
    success_url = 'categories'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

