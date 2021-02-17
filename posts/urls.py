from django.urls import path
from posts.views import  PostList, PostDetail, CommentList, CommentDetail,  PostCommentList

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/<int:pk>/comments', PostCommentList.as_view()),
]
