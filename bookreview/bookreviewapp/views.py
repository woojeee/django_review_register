from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts' : posts })

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        form.save()
        return redirect('detail', post_pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'new.html', { 'form' : form })

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', { 'post' : post })