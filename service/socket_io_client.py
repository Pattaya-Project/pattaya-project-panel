from PySide6.QtCore import QObject, Signal
import socketio
import json


class SocketIOClient(QObject):
    # define a custom signal that receives data from Socket.IO
    received_data = Signal(str)
    panel_received_bot_data = Signal(dict)
    panel_received_online_bot_data = Signal(int)

    def __init__(self, url, namespace):
        super().__init__()
        self.url = url
        self.namespace = namespace
        self.socket_io = socketio.Client()
        self.socket_io.on('connect', self._on_connect)
        self.socket_io.on('disconnect', self._on_disconnect)
        self.socket_io.on('data', self._on_data)
        self.socket_io.on('panel_received_bot_data', self._panel_received_bot_data)
        self.socket_io.on('panel_received_online_bot_data', self._panel_received_online_bot_data)

    def start(self):
        self.socket_io.connect(self.url, namespaces=self.namespace)
        self.socket_io.emit("panel_request_bot_data")

    def stop(self):
        self.socket_io.disconnect()

    def _on_connect(self):
        print('Connected to Socket.IO server.')

    def _on_disconnect(self):
        print('Disconnected from Socket.IO server.')

    def _on_data(self, data):
        print(f'Received data: {data}')
        self.received_data.emit(data)

    def _panel_received_bot_data(self, data):
       self.panel_received_bot_data.emit(data['data'])

    def  _panel_received_online_bot_data(self, data):
        self.panel_received_online_bot_data.emit(data['data'])
        



