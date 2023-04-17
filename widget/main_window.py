from PySide6.QtCore import Qt,QModelIndex
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox,QTableView,QMenu
from PySide6.QtGui import QIcon,QAction
from core.info import PATTAYA_PANEL_VERSION
from core.util import PattayaPanelUtil
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
        
        PattayaPanelUtil.setup(self.panel_log_text_browser, self.server_log_text_browser)
        self.socket_io_client = socket_io_client
        self.bot_table_view.setShowGrid(False)

        self.bots_table_model = BotTableModel(self.socket_io_client)
        self.bot_table_view.setSelectionBehavior(QTableView.SelectRows)
        self.bot_table_view.setSelectionMode(QTableView.SingleSelection)
        self.bot_table_view.setModel(self.bots_table_model)
        self.bot_table_view.setAlternatingRowColors(True)


        self.actionExit.triggered.connect(self.app_exit)
        self.actionDark.triggered.connect(self.enable_dark_theme)
        self.actionLight.triggered.connect(self.enable_light_theme)
        self.actionAbout_Pattaya_Project.triggered.connect(self.about_pattaya_project)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

        self.actionStart.triggered.connect(self.start)
        self.actionStop.triggered.connect(self.stop)

        self.actionStop.setDisabled(True)

        self.socket_io_client.connected_to_server.connect(self.disable_start_action)
        self.socket_io_client.disconnected_to_server.connect(self.disable_stop_action)


        self.socket_io_client.panel_received_bot_count_data.connect(self.update_online_bot)

        # Create a context menu with an action to print the selected row data
        self.context_menu = QMenu(self.bot_table_view)

        self.action_ping_bot = QAction("Ping", self.context_menu)
        self.action_ping_bot.setIcon(QIcon(":/assets/images/cross.png"))
        self.action_ping_bot.triggered.connect(self.ping_bot)
        self.context_menu.addAction(self.action_ping_bot)


        # Connect the context menu to the table widget
        self.bot_table_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.bot_table_view.customContextMenuRequested.connect(lambda pos:  self.context_menu.exec(self.bot_table_view.mapToGlobal(pos)))


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


    def ping_bot(self):
        item = self.pick_bot()
        print(item['wanIp'])


    def pick_bot(self):
        # Get the currently selected model item data
        selected_indexes = self.bot_table_view.selectionModel().selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            data = selected_index.data()
            item = self.bots_table_model.internal_data[int(data)-1]
            return item
        else:
            return None


    def start(self):
        self.socket_io_client.start()
        


    def stop(self):
        self.socket_io_client.stop()
        self.bots_table_model.refresh([])
    

    def disable_start_action(self):
        self.actionStart.setDisabled(True)
        self.actionStop.setDisabled(False)



    def disable_stop_action(self):
        self.actionStart.setDisabled(False)
        self.actionStop.setDisabled(True)