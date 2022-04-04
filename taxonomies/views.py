from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from posts.models import Post
from .forms import TagForm, CategoryForm
from .models import Tag, Category
from django.http import JsonResponse


class TagListView(LoginRequiredMixin, CreateView, ListView):
    model = Tag
    form_class = TagForm
    template_name = 'taxonomies/tags.html'
    context_object_name = 'tags'
    success_url = '/staff/tags'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.filter(created_by=self.request.user)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CategoryListView(LoginRequiredMixin, CreateView, ListView):
    model = Category
    form_class = CategoryForm
    template_name = 'taxonomies/categories.html'
    context_object_name = 'categories'
    success_url = '/staff/categories'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.filter(created_by=self.request.user)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CreateCategoryView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)

    def post(self, request):
        if request.POST.get('action') == 'create-category':
            name = request.POST.get('name')
            description = request.POST.get('description')

            new_category = Category.objects.create(
                name=name,
                description=description,
                created_by=request.user,
            )

        return JsonResponse({'categoryId': new_category.id}, status=200)


class CreateTagView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)

    def post(self, request):
        if request.POST.get('action') == 'create-tag':
            name = request.POST.get('name')
            description = request.POST.get('description')

            new_tag = Tag.objects.create(
                name=name,
                description=description,
                created_by=request.user,
            )

        return JsonResponse({'tagId': new_tag.id}, status=200)


class TagUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'taxonomies/tag_form.html'

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)

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
    success_url = '/staff/tags'

    def test_func(self):
        tag = self.get_object()
        if self.request.user == tag.created_by:
            return True
        return False


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'taxonomies/tag_form.html'

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)

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
    success_url = '/staff/categories'

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.created_by:
            return True
        return False


class TagPostList(ListView):
    model = Post
    template_name = 'taxonomies/tag_post_list.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.all().filter(tags__slug=slug)


class CategoryPostList(ListView):
    model = Post
    template_name = 'taxonomies/category_post_list.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.all().filter(categories__slug=slug)

