from django.urls import path

from . import views


urlpatterns = [
    path('', views.artii),
    path('artii_result/', views.artii_result),
]