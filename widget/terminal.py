from PySide6.QtWidgets import QWidget,QCompleter
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from core.util import PattayaPanelUtil
from designer.ui_terminal import Ui_BotTerminalWidget
import json


class BotTerminalWidget(QWidget, Ui_BotTerminalWidget):
    def __init__(self, bot, socket_io_client):
        super().__init__()        
        self.setupUi(self)
        self.bot = bot
        self.socket_io_client = socket_io_client
        self.setWindowIcon(QIcon(":/assets/images/rat.png"))
        self.task_result_text_browser.setStyleSheet("background-color: #000000;")
        self.bot_send_task_line_edit.setStyleSheet("background-color: #000000;")
        self.bot_send_task_line_edit.setStyleSheet("color: #FB00FF;")


        command = ['help', 'cd', 'pwd', 'mkdir', 'start']
        completer = QCompleter(command)
        self.bot_send_task_line_edit.setCompleter(completer)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.bot_send_task_line_edit.returnPressed.connect(self.handle_bot_comamnd)

        self.bot_event = f'panel_terminal_bot_task_result_{self.bot["hwid"]}'
        print(self.bot_event)

        self.socket_io_client.socket_io.on(self.bot_event, self.update_bot_terminal)
    

    def handle_bot_comamnd(self):
        command = self.bot_send_task_line_edit.text()
        PattayaPanelUtil.panel_log_info(f"Enter {command} command")
        bot_task = {
            "socketId": self.bot['socketId'],
            "hwid": self.bot['hwid'],
            "command": command,
            "arguments": [],
            "file": "" 
        }
        json_object = json.dumps(bot_task)
        self.socket_io_client.socket_io.emit('panel_send_bot_task', json_object)
        self.bot_send_task_line_edit.clear()


    def update_bot_terminal(self, data):
        print(data)


    def closeEvent(self, event):
        # self.socket_io_client.socket_io.off(self.bot_event)
        PattayaPanelUtil.terminals.pop(self.bot['hwid'])
        PattayaPanelUtil.panel_log_info(f"Closed {self.bot['username']} terminal")


