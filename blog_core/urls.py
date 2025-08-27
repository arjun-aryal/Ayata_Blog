from django.urls import path
from .views import (
    CategoryAPIView,
    CategoryDetailAPIView,
    PostsAPIView,
    PostDetailAPIView,
    CommentAPIView,
    CommentDetailsAPIView
)

urlpatterns = [

    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),

    path('posts/<int:post_id>/comments/', CommentAPIView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentDetailsAPIView.as_view(), name='comment-detail'),

    path('posts/', PostsAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),



]


