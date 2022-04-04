from django.urls import path
from . import views

urlpatterns = [
    path('tags', views.TagListView.as_view(), name='tags'),
    path('categories', views.CategoryListView.as_view(), name='categories'),
    path('staff/tags', views.TagListView.as_view(), name='tags'),
    path('staff/categories', views.CategoryListView.as_view(), name='categories'),
    path('staff/tag/create/', views.CreateTagView.as_view(), name='tag-create'),
    path('staff/category/create/', views.CreateCategoryView.as_view(), name='category-create'),
    path('staff/tag/<str:pk>/update/', views.TagUpdateView.as_view(), name='tag-update'),
    path('staff/tag/<str:pk>/delete/', views.TagDeleteView.as_view(), name='tag-delete'),
    path('staff/category/<str:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('staff/category/<str:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    path('tag/<slug:slug>', views.TagPostList.as_view(), name='tag-posts-list'),
    path('category/<slug:slug>', views.CategoryPostList.as_view(), name='category-posts-list'),
]