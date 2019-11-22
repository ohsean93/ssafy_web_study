from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:movie_pk>/', views.detail, name='detail'),
    path('detail/<int:movie_pk>/review/new/', views.review_new, name='review_new'),
    path('detail/<int:movie_pk>/review/<int:review_pk>/', views.review_delete, name='review_delete'),
    path('detail/<int:movie_pk>/like/', views.like, name='like'),
]