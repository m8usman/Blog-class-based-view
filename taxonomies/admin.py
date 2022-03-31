from django.contrib import admin

# Register your models here.
from taxonomies.models import Tag, Category

admin.site.register(Category)
admin.site.register(Tag)


