from rest_framework import serializers
from posts.models import Comment, Post

from users.serializers import CustomUserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ["title", "detail", "category", "invitation", "member_number", "user", "id"]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['content',  'user', 'post']