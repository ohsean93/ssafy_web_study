from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new),
    path('create/', views.create),
    path('', views.index, name='index'),
]
