from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox,QTableView
from PySide6.QtGui import QIcon
from core.info import PATTAYA_PANEL_VERSION
from designer.ui_main_window import Ui_MainWindow
from model.bot_table_model import BotTableModel
import qdarktheme

from widget.about import AboutWidget



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app, socket_io_client):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.backup_title = self.windowTitle()
        self.old_title = self.windowTitle()
        self.update_title = self.old_title.replace('$VERSION', PATTAYA_PANEL_VERSION).replace('$ONLINE_BOT', str(0))
        self.setWindowTitle(self.update_title)

        self.about_dialog = AboutWidget()
        

        self.socket_io_client = socket_io_client
        self.bot_table_view.setShowGrid(False)

        self.bots_table_model = BotTableModel(self.socket_io_client)
        self.bot_table_view.setSelectionBehavior(QTableView.SelectRows)
        self.bot_table_view.setSelectionMode(QTableView.SingleSelection)
        self.bot_table_view.setModel(self.bots_table_model)

        self.actionExit.triggered.connect(self.app_exit)
        self.actionDark.triggered.connect(self.enable_dark_theme)
        self.actionLight.triggered.connect(self.enable_light_theme)
        self.actionAbout_Pattaya_Project.triggered.connect(self.about_pattaya_project)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

        self.socket_io_client.panel_received_online_bot_data.connect(self.update_online_bot)


    def app_exit(self):
        self.app.exit()

    def enable_dark_theme(self):
        qdarktheme.setup_theme()

    def enable_light_theme(self):
        qdarktheme.setup_theme(theme="light")

    def about_pattaya_project(self):
        self.about_dialog.show()

    def about_qt(self):
        QApplication.aboutQt()


    def update_online_bot(self, data):
        self.update_title = self.backup_title.replace('$VERSION', PATTAYA_PANEL_VERSION).replace('$ONLINE_BOT', str(data))
        self.setWindowTitle(self.update_title)
