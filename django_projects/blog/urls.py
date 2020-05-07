from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('',views.index,name="blog_home"),
    path('about/',views.about,name="blog_about"),
    path('register/',user_views.register,name="register"),
]
