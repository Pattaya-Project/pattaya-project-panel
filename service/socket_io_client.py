from PySide6.QtCore import QObject, Signal,QSettings
import socketio

from core.util import PattayaPanelUtil


class SocketIOClient(QObject):
    # define a custom signal that receives data from Socket.IO
    panel_received_bot_data = Signal(dict)
    panel_received_bot_count_data = Signal(int)

    connected_to_server = Signal()
    disconnected_to_server = Signal()
    panel_received_server_heartbeat = Signal(str)
    panel_received_username = Signal(str)
    panel_received_allow_command = Signal(str)

    

    def __init__(self, url = '', namespace = ''):
        super().__init__()
        self.url = url
        self.namespace = namespace
        self.panel_token = QSettings("unknownclub.net", "Pattaya").value('token')
        self._bot_len = 0
        self.socket_io = socketio.Client()
        self.socket_io.on('connect', self._on_connect)
        self.socket_io.on('disconnect', self._on_disconnect)
        if self.panel_token is not None:
            self.socket_io.on(f'{self.panel_token}_panel_received_bot_data', self._panel_received_bot_data)
            self.socket_io.on(f'{self.panel_token}_panel_received_username', self._panel_received_username)
        self.socket_io.on(f'all_panel_received_bot_data', self._panel_received_bot_data)
        self.socket_io.on(f'panel_received_server_heartbeat', self._panel_received_server_heartbeat)


    def start(self, url, token, namespace):
        self.url = url
        self.namespace = namespace
        try:
            self.socket_io.connect(self.url, headers={'Authorization': f'###### {token}', 'Content-Type': 'application/json'}, namespaces=self.namespace)
            PattayaPanelUtil.panel_log_info("Panel has been connected to Pattaya server!")
            self.connected_to_server.emit()
            if self.panel_token is None:
                PattayaPanelUtil.panel_log_info("Initialized panel token! ...Listening bot_data and username event")
                self.socket_io.on(f'{token}_panel_received_bot_data', self._panel_received_bot_data)
                self.socket_io.on(f'{token}_panel_received_username', self._panel_received_username)
                self.panel_token = token
            else:
                PattayaPanelUtil.panel_log_info("Found panel token! ...Listening bot_data and username event")
            
            self.socket_io.emit("panel_request_bot_data", {"token": self.panel_token})
        except Exception as e:
            PattayaPanelUtil.panel_log_error(f'{str(e)}')

        
        


    def send_command(self, event, data):
        try:
            self.socket_io.emit(event, data)
        except Exception as e:
            PattayaPanelUtil.panel_log_error(f'{str(e)}')

    def stop(self):
        try:
            self.socket_io.disconnect()
            PattayaPanelUtil.panel_log_info("Panel has been disconnected to Pattaya server!")
            self.disconnected_to_server.emit()
        except Exception as e:
            PattayaPanelUtil.panel_log_error(f'{str(e)}')

    def _on_connect(self):
        self.connected_to_server.emit()
        self.panel_received_bot_count_data.emit(self._bot_len)
        PattayaPanelUtil.panel_log_info('Connected to Socket.IO server.')

    def _on_disconnect(self):
        self.panel_received_bot_count_data.emit(0)
        self.disconnected_to_server.emit()
        PattayaPanelUtil.panel_log_info('Disconnected from Socket.IO server.')

    def _panel_received_bot_data(self, data):
       self.panel_received_bot_data.emit(data['data'])
       self._bot_len = len(data['data'])
       self.panel_received_bot_count_data.emit(self._bot_len)
       PattayaPanelUtil.panel_log_info(f"Server emit bot data to panel: {str(self._bot_len)} bots")


    def _panel_received_username(self, data):
       self.panel_received_username.emit(data['username'])
       self.panel_received_allow_command.emit(str(data['allow-commands']))
       PattayaPanelUtil.panel_log_info(f"Server emit credentials to panel: {data}")
        

    def _panel_received_server_heartbeat(self, data):
        PattayaPanelUtil.server_log_info(f"Server heartbeat: {data['message']}")


