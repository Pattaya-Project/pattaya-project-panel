import sys

from PySide6 import QtWidgets
from widget.main_window import MainWindow
from service.socket_io_client import SocketIOClient
import qdarktheme


def on_exit():
    socket_io_client.stop()
    print("Exiting the application...")

app = QtWidgets.QApplication(sys.argv)
qdarktheme.setup_theme()
app.aboutToQuit.connect(on_exit)

socket_io_client = SocketIOClient()
window = MainWindow(app, socket_io_client)
window.show()

app.exec()

