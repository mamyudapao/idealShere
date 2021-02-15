from rest_framework import serializers
from posts.models import Comment, Post

from users.serializers import CustomUserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Post
        fields = ["title", "detail", "category", "invitation", "member_number", "user", "id"]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'