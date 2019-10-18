import json
import queue
import asyncio
import threading

from channels.generic.websocket import (WebsocketConsumer,
                                        AsyncWebsocketConsumer)


class ChatConsumer(AsyncWebsocketConsumer):
    """聊天：异步
    """

    async def connect(self):
        """开启连接
        """
        print("--- chat starting ---")

        self.uid = (self.scope["url_route"]
                    ["kwargs"]["service_name"])
        self.user = self.scope["user"].username
        self.group_name = 'chat_%s' % self.uid

        # channel layers副本：self.channel_layer
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        """关闭连接
        """
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        self.close()

    async def receive(self, text_data=None, bytes_data=None):
        """接收消息
        """
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'client.message',
                'group_id': self.uid,
                'user': self.user,
                'message': text_data
            }
        )

    async def client_message(self, event):
        """处理消息
        """
        await self.send(text_data=json.dumps({
             'group': event.get('group_id'),
             'user': event.get('user'),
             'message': 'nihao world!'
        }))

        # 清空channel_layer
        # await self.channel_layer.flush()

        # 发送完消息就从channel中丢弃group，与flush()函数类似
        # await self.channel_layer.group_discard(
        #     self.group_name,
        #     self.channel_name
        # )


class ChatConsumer01(WebsocketConsumer):
    """聊天：同步
    """

    def connect(self):
        """开启连接
        """
        print("--- chat01 starting ---")

        self.uid = (self.scope["url_route"]
                    ["kwargs"]["service_name"])
        self.user = self.scope["user"].username
        self.group_name = 'chat_%s' % self.uid

        self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """关闭连接
        """
        self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        self.close()

    def receive(self, text_data=None, bytes_data=None):
        """接收并处理消息
        """
        print("text data:", text_data)
        self.handle(text_data)

    def handle(self, text_data):
        """处理消息
        """
        self.send(text_data=json.dumps({
            'group': self.uid,
            'user': self.user,
            'message': text_data
        }))


class ChatConsumer02(AsyncWebsocketConsumer):
    """聊天：异步
    """

    async def connect(self):
        """开启连接
        """
        print("--- chat02 starting ---")

        self.uid = (self.scope["url_route"]
                    ["kwargs"]["service_name"])
        self.user = self.scope["user"].username
        self.group_name = 'chat_%s' % self.uid

        self.que = queue.Queue(maxsize=0)

        self.channel_layer.expiry = 300

        await self.build_thread(self.fetch_answer)

        await self.accept()

    async def build_thread(self, target):
        loop = asyncio.new_event_loop()
        t = threading.Thread(target=target, args=(loop,))
        t.setDaemon(True)
        t.start()

    async def disconnect(self, close_code):
        """关闭连接
        """
        self.close()

    async def receive(self, text_data=None, bytes_data=None):
        """接收并处理消息
        """
        self.que.put(text_data)

    def fetch_answer(self, loop):
        asyncio.set_event_loop(loop)

        async def sub():
            while True:
                data = self.que.get()

                if not data:
                    break

                await self.send(text_data=json.dumps({
                    'group': self.uid,
                    'user': self.user,
                    'message': data
                }))
        cro = asyncio.gather(sub())
        loop.run_until_complete(cro)
