from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context=context)

def create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:home')

    else:
        return render(request, 'posts/create.html')

def detail(request, pk):
    post = Post.objects.get(id = pk)
    context = {
        'post': post,
    }

    return render(request, 'posts/detail.html', context=context)

def update(request, pk):
    post = Post.objects.get(id = pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:home')

    else:
        context = {
            'post': post,
        }
        return render(request, 'posts/update.html', context=context)

def delete(request, pk):
    todo = get_object_or_404(Post, id = pk)
    todo.delete()

    return redirect('posts:home')