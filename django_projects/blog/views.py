from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic  import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# render return a httpResponse and is a shortcut method used here.
def index(request):
    context={
        'posts':Post.objects.all() #ignore error
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
    #prefined method
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # all the names should be as follows
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # all the names should be as follows
    model = Post
    success_url = 'blog_home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request,'blog/about.html', {'title':'BLOG | ABOUT'})