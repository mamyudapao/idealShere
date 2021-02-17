from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.api.serializers import CommentSerializer, PostSerializer
from posts.models import Post, Comment
from users.models import CustomUser
from rest_framework.response import Response



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        request_user = self.request.user
        custom_user = get_object_or_404(CustomUser, id=request_user.id)
        serializer.save(user=custom_user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        queryset = Comment.objects.filter(post_id=self.kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        request_user = self.request.user
        kwargs_pk = self.kwargs.get('pk')
        custom_user = get_object_or_404(CustomUser, id=request_user.id)
        post = get_object_or_404(Post, id=kwargs_pk)

        serializer.save(user=custom_user, post=post)
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

