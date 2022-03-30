from django.urls import path
from . import views

urlpatterns = [
    path('tag_create', views.CreateTagView.as_view(), name='tag_create'),
]