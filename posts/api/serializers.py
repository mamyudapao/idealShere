from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from posts.models import Comment, Post, Member, Like

from users.serializers import CustomUserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["title", "detail", "category", "invitation", "member_number", "user", "id", "created_at", "image"]


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    post = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['content',  'user', 'post', 'created_at', 'id']
        
class LikeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    post = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Like
        fields = ['user', 'comment', 'post', 'id']  
        


class MemberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    class Meta:
        model = Member
        fields = ['user', 'post', 'created_at']