from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

user = get_user_model()
class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Post
        fields = '__all_'
class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        

