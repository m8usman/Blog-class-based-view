from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.Posts.as_view(), name="posts_guest"),
    path('', views.PostsStaff.as_view(), name="posts"),
    path('staff/dashboard', views.DashboardView.as_view(), name="dashboard"),
    path('post/<slug:slug>', views.PostView.as_view(), name="post"),
    path('staff/post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('staff/postnew/', views.PostCreateView.as_view(), name='post_create'),
    path('staff/post/<str:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('staff/post/<str:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('staff/post/<slug:slug>/update-status/', views.StatusUpdateView.as_view(), name='status_updated_url'),
]