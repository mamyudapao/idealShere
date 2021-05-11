from rest_framework import serializers
from users.models import CustomUser
from posts.models import Post
import posts.api.serializers as postsSerializers


class CustomUserSerializer(serializers.ModelSerializer):
    projects = postsSerializers.PostSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'skill', 'image', 'introduction', 'projects']


