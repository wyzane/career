from django.views import View
from django.shortcuts import render


class ChatRoom(View):

    def get(self, request):
        """返回聊天页面
        """

        return render(request, 'index.html')


class ChatRoom01(View):

    def get(self, request):
        """返回聊天页面
        """

        return render(request, 'chat01.html')


class ChatRoom02(View):

    def get(self, request):
        """返回聊天页面
        """

        return render(request, 'chat02.html')
