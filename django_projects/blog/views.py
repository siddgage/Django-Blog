from django.shortcuts import render

posts = [
    {
        'author':'sidd',
        'title':'post no 1',
        'content':'some content',
        'date':'todays date'
    },
    {
        'author':'sidd 1',
        'title':'post no 2',
        'content':'some content again',
        'date':'todays date again'
    },
    {
        'author':'sidd 2',
        'title':'post no 3',
        'content':'some content and again',
        'date':'todays date and again'
    },
]
# render return a httpResponse and is a shortcut method used here.
def index(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html', context) 


def about(request):
    return render(request,'blog/about.html', {'title':'BLOG | ABOUT'})
