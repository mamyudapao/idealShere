from django.urls import path
from posts.views import PostList, PostDetail, CommentList,\
    CommentDetail,  PostCommentList, MemberList, PostMember, CommentLikeAPIView, PostParticipateAPIView,\
        NotificationList

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/<int:pk>/comments', PostCommentList.as_view()),
    # membersにするとなぜかCORSエラーが出る。
    path('posts/<int:pk>/list_members', PostMember.as_view()),
    path('posts/<int:pk>/participants', PostParticipateAPIView.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('comments/<int:pk>/likes', CommentLikeAPIView.as_view()),
    path('notification/', NotificationList.as_view()),
]
