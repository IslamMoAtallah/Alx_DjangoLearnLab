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
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# List view - public
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # blog/post_list.html
    context_object_name = 'posts'
    paginate_by = 10

# Detail view - public
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # blog/post_detail.html
    context_object_name = 'post'

# Create view - authenticated users only
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # blog/post_form.html

    def form_valid(self, form):
        # Set the logged-in user as the author
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

# Update view - only author can edit
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        # default behaviour: redirect to login; raise 403 instead if you prefer
        return super().handle_no_permission()

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

# Delete view - only author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # blog/post_confirm_delete.html
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})
# Additional views can be added as needed



