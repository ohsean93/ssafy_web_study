from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context=context)


# @login_required(login_url='accounts/login')
@login_required
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
        

def detail(request, article_pk, comment_pk=None):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    commentform = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'commentform': commentform,
        'comment_pk': comment_pk
    }
    if comment_pk:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.article = article
                new_form.save()
                return redirect(article)
        else:
            form = CommentForm(instance=comment)
            context['form'] = form

    return render(request, 'articles/detail.html', context)


@login_required
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
@login_required
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.method == 'POST':
            article.delete()
            return redirect('articles:index')
        else:
            return redirect(article)
    else:
        return HttpResponse('검증되지 않은 유저정보입니다.', status=401)


@require_POST
@login_required
def new_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.article = Article.objects.get(pk=article_pk)
            new_form.save()
            return redirect(article)
    else:
        return redirect(article)
        

@require_POST
@login_required
def delete_comment(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        if comment.article == article:
            comment.delete()
    return redirect(article)