from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }

    return render(request,'posts/index.html', context)

def new(request):
    return render(request,'posts/new.html')

def create(request):
    # post = Post()
    # post.title = request.GET.get('title')
    # post.content = request.GET.get('content')
    # post.image_url = request.GET.get('image_url')
    # post.save()

    Post.objects.create(
        title = request.GET.get('title'),
        content = request.GET.get('content'),
        image_url = request.GET.get('image_url'),
    )
    return redirect('home')


def detail(request, pk):
    # id == pk
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }

    return render(request, 'posts/detail.html', context)
    
def delete(request, pk):
    # id == pk
    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect('home')

    
def edit(request, pk):
    # id == pk
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }

    return render(request, 'posts/edit.html', context)
    
def update(request, pk):
    # id == pk
    post = Post.objects.get(pk=pk)

    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.image_url = request.GET.get('image_url')
    post.save()

    return redirect('posts:detail', pk)
    