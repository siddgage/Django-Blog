from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic  import ListView, DetailView, CreateView, UpdateView
from .models import Post

# render return a httpResponse and is a shortcut method used here.
def index(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html', context) 


class PostListView(ListView):
    # all the names should be as follows
    model = Post
    template_name= 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    # all the names should be as follows
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    # all the names should be as follows
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    # all the names should be as follows
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request,'blog/about.html', {'title':'BLOG | ABOUT'})