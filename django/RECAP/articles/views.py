from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
from itertools import chain
from IPython import embed



# Create your views here.
# @login_required
def index(request):
    # embed()
    if request.user.is_authenticated:
        # visits_num = request.session.get('visits', 0)
        # request.session['visits'] = visits_num + 1
        request.session.modified = True
        followings_and_me = chain(request.user.followings.all(), [request.user])
        articles = Article.objects.filter(user__in=followings_and_me)
    else:
        articles = Article.objects.all()

    context = {
        'articles': articles,
        # 'visits': visits_num,
    }
    return render(request, 'articles/index.html', context=context)



def explore(request):
    # embed()
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/explore.html', context=context)


def tags(request):
    # embed()
    tags = Hashtag.objects.filter()
    context = {
        'tags': tags,
    }
    return render(request, 'articles/tags.html', context=context)


def hashtag(request, hashtag_pk):
    # embed()
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    articles = hashtag.article_set.all()
    context = {
        'articles': articles,
        'hashtag': hashtag,
    }
    return render(request, 'articles/hashtag.html', context=context)


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
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            for word in article.content.split():
                if word.startswith('#'):
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag)

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
    # visits_num = request.session.get('visits', 0)
    # request.session['visits'] = visits_num + 1
    # request.session.modified = True
    context = {
        'article': article,
        'comments': comments,
        'commentform': commentform,
        'comment_pk': comment_pk,
    }
    if comment_pk:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user != request.user():
            return redirect(article)
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.article = article
                new_form.user = request.user
                new_form.save()
                return redirect(article)
        else:
            form = CommentForm(instance=comment)
            context['form'] = form

    return render(request, 'articles/detail.html', context)


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if article.user != request.user:
        return redirect(article)

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
        if article.user != request.user:
            return redirect(article)

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
            new_form.user = request.user
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


def send_cookie(request):
    res = HttpResponse('과자 받아라')
    res.set_cookie('mycookie', 'oreo')
    return res


@login_required
def like(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    user = request.user

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        liked = False

    else:
        article.like_users.add(user)
        liked = True
    # return redirect(article)
    context = {
        'liked': liked,
        'count': article.like_users.count(),
        # 'users': article.like_users.all(),
    }

    return JsonResponse(context)