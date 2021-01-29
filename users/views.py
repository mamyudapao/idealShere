from rest_framework import generics

from users.serializers import CustomUserSerializer
from users.models import CustomUser


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer