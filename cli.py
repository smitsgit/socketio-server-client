from socketIO_client import SocketIO, BaseNamespace


class ChatNamespace(BaseNamespace):

    # Name of the method starts with on_{channel_name}
    # Server does emit('my_response', {'data': 'Connected'})
    # hence the name on_my_response
    @staticmethod
    def on_my_response(data):
        print(data)
        print('[Connected]')


socketIO = SocketIO('localhost', 5002)
chat_namespace = socketIO.define(ChatNamespace, '/test')

chat_namespace.emit('my_event', {'data': 20})
chat_namespace.emit('my_broadcast_event', {'data': 40})
socketIO.wait(seconds=20)
