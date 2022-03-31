from django.urls import path
from . import views

urlpatterns = [
    path('tags', views.TagListView.as_view(), name='tags'),
    path('categories', views.CategoryListView.as_view(), name='categories'),
    path('tag/<str:pk>/update/', views.TagUpdateView.as_view(), name='tag-update'),
    path('tag/<str:pk>/delete/', views.TagDeleteView.as_view(), name='tag-delete'),
    path('category/<str:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<str:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]