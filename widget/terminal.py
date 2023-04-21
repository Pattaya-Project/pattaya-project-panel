from PySide6.QtWidgets import QWidget,QCompleter
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from core.util import PattayaPanelUtil
from designer.ui_terminal import Ui_BotTerminalWidget

class BotTerminalWidget(QWidget, Ui_BotTerminalWidget):
    def __init__(self, bot):
        super().__init__()        
        self.setupUi(self)
        self.bot = bot
        self.setWindowIcon(QIcon(":/assets/images/rat.png"))
        self.task_result_text_browser.setStyleSheet("background-color: #000000;")
        self.bot_send_task_line_edit.setStyleSheet("background-color: #000000;")
        self.bot_send_task_line_edit.setStyleSheet("color: #FB00FF;")


        command = ['help', 'cd', 'pwd', 'mkdir', 'start']
        completer = QCompleter(command)
        self.bot_send_task_line_edit.setCompleter(completer)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.bot_send_task_line_edit.returnPressed.connect(self.handle_bot_comamnd)
    

    def handle_bot_comamnd(self):
        command = self.bot_send_task_line_edit.text()
        PattayaPanelUtil.panel_log_info(f"Enter {command} command")
        self.bot_send_task_line_edit.clear()



    def closeEvent(self, event):
        PattayaPanelUtil.terminals.pop(self.bot['hwid'])
        PattayaPanelUtil.panel_log_info(f"Closed {self.bot['username']} terminal")


