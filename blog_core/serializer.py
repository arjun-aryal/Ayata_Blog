from rest_framework import serializers
from .models import Category, Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author_name', 'content', 'created_at']
        read_only_fields = ["id"]


class PostSerializer(serializers.ModelSerializer):
#    comments = CommentSerializer(many=True, read_only=True)
    author_name = serializers.CharField(source='author.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'category', 'category_name', 'title', 'content', 'author_name', 'status', 'created_at', 'updated_at'] #, 'comments'
        read_only_fields = ["id"]


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'posts']
        read_only_fields = ["id"]
