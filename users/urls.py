from django.urls import path
from . import views
import uuid

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', views.LogoutUser.as_view(), name="logout"),
    path('register/', views.RegisterUser.as_view(), name="register"),

    path('profiles', views.Profiles.as_view(), name="profiles"),
    path('profile/<str:pk>/', views.UserProfile.as_view(), name="user-profile"),
    path('staff/account/', views.UserAccount.as_view(), name="account"),

    path('staff/edit-account/<str:pk>/', views.EditAccount.as_view(), name="edit-account"),

    # path('reset/<str:pk>/', views.ResetPassword.as_view(template_name="reset.html"),
    #      name="password_reset_confirm"),
]