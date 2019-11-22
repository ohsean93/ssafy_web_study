from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'form': review_form,
        'reviews': movie.review_set.all(),
    }
    return render(request, 'movies/detail.html', context)


@login_required
@require_POST
def review_new(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
    return redirect(movie)


@login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:detail', movie_pk)


@login_required
def like(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    # 만약 좋아요 리스트에 현재 접속중인 유저가 있다면, Unlike 처리
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect(movie)