from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="blog_home"),
    path('about/',views.about,name="blog_about"),
    path('register/',user_views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logput"),
]
