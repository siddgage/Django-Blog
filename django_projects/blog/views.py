from django.shortcuts import render
from .models import Post

# render return a httpResponse and is a shortcut method used here.
def index(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html', context) 


def about(request):
    return render(request,'blog/about.html', {'title':'BLOG | ABOUT'})
