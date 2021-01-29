from django.urls import path

from users.views import UserList


urlpatterns = [
    path('', UserList.as_view()),
]
