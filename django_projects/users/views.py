from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method =='POST':
        form.save()
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog_home')
    else:
        form = UserRegisterForm(request.POST)


    return render(request, 'users/register.html', {'form': form})