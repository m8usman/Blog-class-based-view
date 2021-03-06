from .models import Post, Tag
from django.db.models import Q


def searchPosts(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    posts = Post.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(created_by__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return posts, search_query
