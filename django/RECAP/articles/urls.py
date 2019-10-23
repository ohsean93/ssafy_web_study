from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comment/', views.new_comment, name='new_comment'),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.detail, name='update_comment'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete', views.delete_comment, name='delete_comment'),
    path('send_cookie/', views.send_cookie, name='send'),
    path('<int:article_pk>/like/', views.like, name='like'),
]
