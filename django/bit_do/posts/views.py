from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.
def index(request):
    # table 형태로 게시판을 보여줌
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == 'POST':
        Post.objects.create(
            title = request.POST.get('title'), 
            content = request.POST.get('content'), 
        )
        return redirect('home')
    else:
        return render(request, 'posts/new.html')


def detail(request, pk):
    # pk라는 id를 가진 글을 찾아와 보여줌
    post = Post.objects.get(pk=pk)

    comments = reversed(post.comment_set.all())
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)


def delete(request, pk):
    # pk라는 id를 가진 글을 삭제
    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect('home')


def update(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.image_url = request.POST.get('image_url')
        post.save()

        return redirect('posts:detail', pk)
    else:
        context = {
            'post': post,
        }
        return render(request, 'posts/update.html', context)


def create_comment(request, pk):
    Comment.objects.create(
        content=request.POST.get('content'),
        post=Post.objects.get(pk=pk),
    )
    return redirect('posts:detail', pk)