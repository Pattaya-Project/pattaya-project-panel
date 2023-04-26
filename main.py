import sys

from PySide6 import QtWidgets
from core.util import PattayaPanelUtil
from widget.main_window import MainWindow
from service.socket_io_client import SocketIOClient
from PySide6.QtCore import QSettings
import qdarktheme
import win32event
import win32api
import winerror


def on_exit():
    del PattayaPanelUtil.terminals
    socket_io_client.stop()
    #print("Exiting the application...")


app = QtWidgets.QApplication(sys.argv)
settings = QSettings("unknownclub.net", "Pattaya")

match settings.value("themes"):
    case 0:
        qdarktheme.setup_theme(custom_colors={"primary": "#FB00FF"})
    case 1:
        qdarktheme.setup_theme(theme="light",custom_colors={"primary": "#FB00FF"})

del settings

app.aboutToQuit.connect(on_exit)

socket_io_client = SocketIOClient()
window = MainWindow(app, socket_io_client)

mutex = win32event.CreateMutex(None, False, "PattayaPanelSingleInstanceMutex")
if not mutex:
    QtWidgets.QMessageBox.warning(window,
    "Pattaya Panel Alert",
    "Cannot create Mutex",
    QtWidgets.QMessageBox.Ok)
    sys.exit(0)

if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    QtWidgets.QMessageBox.warning(window, 
    "Pattaya Panel Alert",
    "One Instance only",
    QtWidgets.QMessageBox.Ok)
    sys.exit(0)
window.show()
app.exec()

