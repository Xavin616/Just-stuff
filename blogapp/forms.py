from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Blog, CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email') 

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('author', 'topic', 'body')