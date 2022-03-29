from django.urls import path
from . import views

urlpatterns = [
    path('', views.Posts.as_view(), name="posts"),
    path('post/<str:pk>/', views.Post.as_view(), name="post"),
]