from django.urls import path
from users.views import UserList, UserEditView


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>', UserEditView.as_view())
]
