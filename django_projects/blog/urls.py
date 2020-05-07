from django.contrib import admin
from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="blog_home"),
    path('admin/', admin.site.urls),
    path('about/',views.about,name="blog_about"),
    path('register/',user_views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logput"),
]
