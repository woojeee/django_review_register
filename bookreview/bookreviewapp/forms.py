from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'img', 'price', 'point', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'content', )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {'password': forms.PasswordInput()}
