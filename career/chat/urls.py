from django.urls import path

from .views import ChatRoom, ChatRoom01, ChatRoom02


urlpatterns = [
    path('chat', ChatRoom.as_view()),
    path('chat01', ChatRoom01.as_view()),
    path('chat02', ChatRoom02.as_view())
]
