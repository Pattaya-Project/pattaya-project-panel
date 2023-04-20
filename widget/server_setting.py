from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog,QDialogButtonBox
from designer.ui_pattaya_server_setting import Ui_ServerSettingWidget



class PattayaServerSetting(QDialog, Ui_ServerSettingWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.settings = QSettings("unknownclub.net", "Pattaya")

        # get current values for settings
        url = self.settings.value("url")
        token = self.settings.value("token")

        if url == None or token == None:
            pass
        else:
            # get current values for settings
            url = self.settings.value("url")
            token = self.settings.value("token")

        self.server_url_line_edit.setText(url)
        self.server_token_line_edit.setText(token)

        #Fields
        self.url = ""
        self.token = ""

        #Connections
        self.buttonBox.clicked.connect(self.button_box_clicked)

    def button_box_clicked(self,button):
        std_button = self.buttonBox.standardButton(button)
        if(std_button == QDialogButtonBox.Ok):
            self.ok()
        elif(std_button == QDialogButtonBox.Cancel):
            self.reject()

    def ok(self):
        if(not(self.server_url_line_edit.text()=='') and not(self.server_token_line_edit.text()=='')):
            self.url = self.server_url_line_edit.text()
            self.token = self.server_token_line_edit.text()

        self.accept()