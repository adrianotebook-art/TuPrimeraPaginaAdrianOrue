from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.create_author, name='create_author'),
    path('post/', views.create_post, name='create_post'),
    path('comment/', views.create_comment, name='create_comment'),
    path('search/', views.search_post, name='search_post'),
]