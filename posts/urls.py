from django.urls import path
from posts.views import PostList, PostDetail, CommentList,\
    CommentDetail,  PostCommentList, MemberList, PostMember, LikeList, PostLikeList,\
    LikeList, LikeRetrieveDestroy

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/<int:pk>/comments', PostCommentList.as_view()),
    # membersにするとなぜかCORSエラーが出る。
    path('posts/<int:pk>/list_members', PostMember.as_view()),
    path('posts/<int:pk>/likes', PostLikeList.as_view()),
    path('likes/', LikeList.as_view()),
    path('likes/<int:pk>', LikeRetrieveDestroy.as_view())
]
