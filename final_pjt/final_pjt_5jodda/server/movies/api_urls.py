from django.urls import path
from . import api_views

app_name = 'api_movies'

urlpatterns = [
    path('', api_views.movie_index, name='index'),
    path('<int:movie_pk>/', api_views.movie_detail, name='detail'),
    path('<int:movie_pk>/<int:review_pk>/', api_views.review_detail, name='detail'),
]