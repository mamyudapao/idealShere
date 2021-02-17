from django.urls import path
from posts.views import  PostList, PostDetail, CommentList, CommentDetail,  PostCommentList, MemberList, PostMember

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/<int:pk>/comments', PostCommentList.as_view()),
    path('posts/<int:pk>/list_members', PostMember.as_view()), #membersにするとなぜかCORSエラーが出る。
]
