"""远程调用服务
"""

from xmlrpc.server import SimpleXMLRPCServer


class SimpleServer:

    # 默认功能
    methods = ["get", "set", "post"]

    def __init__(self, address):
        self._server = (SimpleXMLRPCServer(address,
                                           allow_none=True))
        for method in self.methods:
            self._server.register_function(getattr(self, method))

    def get(self, *args, **kwargs):
        print("SimpleServer get ...")

    def set(self, *args, **kwargs):
        print("SimpleServer set ...")

    def post(self, *args, **kwargs):
        print("SimpleServer post ...")

    def serve_forever(self):
        self._server.serve_forever()

    def add_function(self, method):
        """注册新功能
        """
        name = str(method)
        setattr(self, name, method)
        self._server.register_function(getattr(self, name))
