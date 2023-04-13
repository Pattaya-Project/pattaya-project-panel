from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from designer.ui_about import Ui_AboutWidget


class AboutWidget(QWidget, Ui_AboutWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)