from rest_framework import generics, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from posts.api.serializers import CommentSerializer, PostSerializer, MemberSerializer, NotificationSerializer
from posts.models import Post, Comment, Member, Notification
from users.models import CustomUser
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        request_user = self.request.user
        custom_user = get_object_or_404(CustomUser, id=request_user.id)
        serializer.save(user=custom_user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostParticipateAPIView(APIView):
    serializer_class = PostSerializer

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user.id

        post.participants.remove(user)
        post.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        post.participants.add(user)
        post.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PostCommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        queryset = Comment.objects.filter(
            post_id=self.kwargs['pk']).order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(request ,serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, request, serializer):
        request_user = self.request.user
        kwargs_pk = self.kwargs.get('pk')
        custom_user = get_object_or_404(CustomUser, id=request_user.id)
        post = get_object_or_404(Post, pk=request.data.get('post_id'))
        notification = Notification(sender_id=self.request.user, receiver_id=custom_user,
                                    post_id=post, action="Comment")
        notification.save()
        user = request.user
        post = get_object_or_404(Post, id=kwargs_pk)
        serializer.save(author=custom_user, post=post)


class PostMember(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request, *args, **kwargs):
        queryset = Member.objects.filter(post=self.kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentLikeAPIView(APIView):
    serializer_class = CommentSerializer

    def patch(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user.id

        comment.voters.remove(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        post = get_object_or_404(Post, pk=request.data.get('post_id'))
        notification = Notification(sender_id=self.request.user, receiver_id=comment.author,
                                    post_id=post, action="Like")
        user = request.user
        notification.save()
        comment.voters.add(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# TODO: 自分のアカウントのやつだけが帰ってくるようにlistをオーバーライドする
class NotificationList(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def list(self, request, *args, **kwargs):
        queryset = Notification.objects.filter(
            receiver_id=self.request.user.id).order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# TODO: checkedを変更できるようにする
