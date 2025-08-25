from rest_framework.response import Response
from rest_framework import status
from .serializer import PostSerializer,CommentSerializer,CategorySerializer
from .models import Comment,Category,Post
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,IsAuthenticated
from .permission import IsOwnerOrReadOnly,IsAdminorOwner
from .pagination import BlogPagination


class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminorOwner]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminorOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    pagination_class = BlogPagination

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly,IsAdminUser]
    queryset = Post.objects.all().prefetch_related("comments")
    serializer_class = PostSerializer
    pagination_class = BlogPagination







