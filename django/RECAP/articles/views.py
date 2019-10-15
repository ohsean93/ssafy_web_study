from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.http import Http404
from django.views.decorators.http import require_http_methods, require_POST


# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context=context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        # 데이터 유효성 검사
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            article = form.save()
            return redirect(article)
        else:
            return redirect('articles:create')
    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
        

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    commentform = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'commentform': commentform,
    }
    return render(request, 'articles/detail.html', context)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        
        # 데이터 유효성 검사
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            form.save()
            return redirect(article)

    data = {
        'title': article.title,
        'content': article.content,
    }
    form = ArticleForm(instance=article)
    # form = ArticleForm(initial=data) # initial, data 사용 가능하나 data는 유저 정보를 위해 사용하자
    # form.is_valid()

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)


def new_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        form = CommentForm(request.POST)
        embed()
        if form.is_valid():
            # article = form.cleaned_data.get('article')
            # content = form.cleaned_data.get('content')
            form.save()
            # comment.article = Article.objects.get(pk=article_pk)
            # comment.save()
            return redirect(article)
    else:
        return redirect(article)

