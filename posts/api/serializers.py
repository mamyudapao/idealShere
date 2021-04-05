from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from posts.models import Comment, Post, Member, Notification

from users.serializers import CustomUserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    count_participants = serializers.SerializerMethodField()
    user_has_participated = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["title", "detail", "invitation", "member_number", "author", "id", "created_at", 'count_participants', 'user_has_participated',]

    def get_count_participants(self, instance):
        return instance.participants.count()

    def get_user_has_participated(self, instance):
        request = self.context.get("request")
        return instance.participants.filter(pk=request.user.pk).exists()

    def get_author(self, instance):
        return instance.user.username


        
class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ['post', 'voters']

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()
    
class MemberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    class Meta:
        model = Member
        fields = ['user', 'post', 'created_at']


class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields = "__all__"