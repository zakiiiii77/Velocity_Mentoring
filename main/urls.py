from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_location, name='add'),
    # path('like/', views.like, name='like'),
    # path('dislike/', views.dislike, name='dislike'),
    path('like/<int:location_id>/', views.like_location, name='like_location'),
    path('dislike/<int:location_id>/', views.dislike_location, name='dislike_location'),
    path('add_comment/<int:location_id>/', views.add_comment, name='add_comment'),

    # path('comment/', views.comment, name='comment'),

]