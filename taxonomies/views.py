from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import TagForm
from .models import Tag


class CreateTagView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'taxonomies/tag-form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save
        return HttpResponse('<script type="text/javascript">window.close()</script>')
