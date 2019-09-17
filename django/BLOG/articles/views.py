from django.shortcuts import render, redirect
from datetime import datetime
from .models import ORM_Article

blog_articles = []
blog_dict_articles = []
blog_class_articles = []

class Article:
    def __init__(self, title, content, created_at):
        self.title = title
        self.content = content
        self.created_at = created_at

    def __str__(self):
        return f'제목 : {self.title} 내용 : {self.content} 작성시간 : {self.created_at}'





# Create your views here.
def new(request):
    return render(request,'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    img_url = request.GET.get('img_url')

    now = datetime.now

    blog_articles.append((title, content))
    blog_dict_articles.append({'title':title, 'content':content, 'created_at':now})
    blog_class_articles.append(Article(title,content,now))

    article = ORM_Article()
    article.title = title
    article.content = content
    article.img_url = img_url
    article.save()


    context = {
        'title' : title,
        'content' : content,
    }

    return redirect('index')
    # render(request, 'articles/create.html', context)


def index(request):
    articles = ORM_Article.objects.all()
    context = {
        'blog_articles' : blog_articles,
        'blog_dict_articles' : blog_dict_articles,
        'blog_class_articles' : blog_class_articles,
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)