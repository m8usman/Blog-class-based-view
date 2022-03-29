from django.urls import path
from . import views

urlpatterns = [
    path('', views.Posts.as_view(), name="posts"),
    path('post/<slug:slug>', views.PostView.as_view(), name="post"),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
]