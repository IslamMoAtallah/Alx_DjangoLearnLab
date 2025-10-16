from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login 
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Post, profile
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, f'Your account has been created! You are now logged in as {user.username}.')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'
@login_required
def profile_view(request):
    if request.method == 'post':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,   
        'p_form': p_form
    }
    return render(request, 'blog/profile.html', context)


# Create your views here.
