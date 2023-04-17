from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from designer.ui_about_pattaya import Ui_AboutPattayaWidget


class AboutPattayaWidget(QWidget, Ui_AboutPattayaWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)