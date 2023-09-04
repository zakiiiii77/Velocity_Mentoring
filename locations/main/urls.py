from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_location, name='add'),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('comment/', views.comment, name='comment'),
]