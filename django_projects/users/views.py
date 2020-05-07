from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdatationForm, UserUpdatationForm

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm(request.POST)


    return render(request, 'users/register.html',{'form': form})
@login_required
def profile(request):
    if request.method =='POST':
        update_form = UserUpdatationForm(request.POST,instance=request.user)
        profile_update_form = ProfileUpdatationForm(request.POST,request.FILES,instance=request.user.profile)
    else:
        update_form = UserUpdatationForm(request.POST,instance=request.user)
        profile_update_form = ProfileUpdatationForm(request.POST,instance=request.user.profile)


    context = {
        'update_form': update_form,
        'profile_update_form': profile_update_form,
    }
    return render(request,'users/profile.html', context)