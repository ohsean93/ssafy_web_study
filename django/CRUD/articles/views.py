from django.shortcuts import render, redirect
from .models import Article
from datetime import datetime


# Create your views here.
def new(request):
    return render(request,'articles/new.html')


def create(request):
    now = datetime.now()
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    # article.created_at = now
    article.img_url = request.GET.get('img_url')
    article.save()

    return redirect(index)


def index(request):
    all_article = reversed(Article.objects.all())
    context = {
        'articles': all_article,
    }
    return render(request,'articles/index.html',context = context)