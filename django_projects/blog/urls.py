from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',PostListView.as_view(),name="blog_home"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post_detail"),
    path('post/new/',PostCreateView.as_view(),name="post_create"),
    path('about/',views.about,name="blog_about"),
    path('register/',user_views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path('profile/',user_views.profile,name="profile"),
]
