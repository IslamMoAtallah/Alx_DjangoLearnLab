from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post , Profile, comment
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['bio', 'avatar']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        content = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your comment here...'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5 , 'placeholder': 'Write your post here...'}),
        }
     def clean_tag_names(self):
        data = self.cleaned_data.get('tag_names', '')
        names = [n.strip() for n in data.split(',') if n.strip()]
        seen = set()
        uniq=[]
        for n in names:
            key = n.lower()
            if key not in seen:
                seen.add(key)
                uniq.append(n)
        return uniq
