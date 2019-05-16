from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, UserForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    posts = Post.objects.all()
    # 모든 포스트 오브젝트 할당
    return render(request, 'home.html', {'posts': posts})

@login_required
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user.get_username()
        post.save()
        return redirect('detail', post_pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})


def detail(request, post_pk):

    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        return redirect('detail', post.pk)

    else:
        post = Post.objects.get(pk=post_pk)
        form = CommentForm()
        return render(request, 'detail.html', {'post': post, 'form': form})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('detail', post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')


def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect('detail', post_pk)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
    
    else:
        form = UserForm()
        error = '장난치지 마라'
        return render(request, 'registration/signup.html', { 'form': form, 'error': error })