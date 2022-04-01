from django.urls import path
from . import views

urlpatterns = [
    path('', views.Posts.as_view(), name="posts"),
    path('dashboard', views.DashboardView.as_view(), name="dashboard"),
    path('post/<slug:slug>', views.PostView.as_view(), name="post"),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<str:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<str:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('post/<slug:slug>/update-status/', views.StatusUpdateView.as_view(), name='status_updated_url'),
]