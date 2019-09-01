from django.urls import path

from .apis.views_crud import (Login,
                              Logout,
                              CreateUser,
                              DeletionUser)
from .apis.views import UserList, UserExport


urlpatterns = [
    path('login/user',
         Login.as_view()),
    path('logout/user',
         Logout.as_view()),
    path('create/user',
         CreateUser.as_view()),
    path('delete/user',
         DeletionUser.as_view()),
    path('list/user',
         UserList.as_view()),
    path('export/user',
         UserExport.as_view()),
]
