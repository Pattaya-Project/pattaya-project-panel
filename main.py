import sys

from PySide6 import QtWidgets
from widget.main_window import MainWindow
from service.socket_io_client import SocketIOClient
import qdarktheme


def on_exit():
    socket_io_client.stop()
    #print("Exiting the application...")


import win32event
import win32api
import winerror

app = QtWidgets.QApplication(sys.argv)
qdarktheme.setup_theme()
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

