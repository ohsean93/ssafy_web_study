from django.urls import path
from . import views

app_name = 'crud_test'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('add/', views.add, name='add'),
]
