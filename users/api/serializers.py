from rest_framework import serializers
from users.models import CustomUser
from posts.models import Post
import posts.api.serializers as postsSerializers


class CustomUserSerializer(serializers.ModelSerializer):
    projects = postsSerializers.PostSerializer(many=True, read_only=True)
    made_projects = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'skill', 'image', 'introduction', 'projects', 'made_projects']

    def get_made_projects(self, instance):
        made_projects = Post.objects.filter(user=instance.id)
        return made_projects.count()


