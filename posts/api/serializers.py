from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from posts.models import Comment, Post, Member, Notification, Chat
from users.models import CustomUser



class PostSerializer(serializers.ModelSerializer):
    count_participants = serializers.SerializerMethodField()
    user_has_participated = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    author_image = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["title", "detail", "invitation", "member_number", "user", "id", "created_at", 'count_participants', 'user_has_participated', 'author_name', 'author_image']
        read_only_fields = ['participants', 'user']

    def get_count_participants(self, instance):
        return instance.participants.count()

    def get_user_has_participated(self, instance):
        request = self.context.get("request")
        return instance.participants.filter(pk=request.user.pk).exists()

    def get_author_name(self, instance):
        return instance.user.username

    def get_author_image(self, instance):
        return instance.user.image.url



        
class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()
    author_image = serializers.SerializerMethodField()
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

    def get_author_image(self, instance):
        return instance.author.image.url
    
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


class ChatSerializer(serializers.ModelSerializer):

    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ["user", "message", "room", "id", "user_name", "created_at"]

    def get_user_name(self, instance):
        return instance.user.username
