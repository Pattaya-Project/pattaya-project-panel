# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pattaya_server_setting.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ServerSettingWidget(object):
    def setupUi(self, ServerSettingWidget):
        if not ServerSettingWidget.objectName():
            ServerSettingWidget.setObjectName(u"ServerSettingWidget")
        ServerSettingWidget.resize(534, 125)
        ServerSettingWidget.setMinimumSize(QSize(534, 125))
        ServerSettingWidget.setMaximumSize(QSize(534, 125))
        self.verticalLayout_3 = QVBoxLayout(ServerSettingWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ServerSettingWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(ServerSettingWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.server_url_line_edit = QLineEdit(ServerSettingWidget)
        self.server_url_line_edit.setObjectName(u"server_url_line_edit")

        self.verticalLayout_2.addWidget(self.server_url_line_edit)

        self.server_token_line_edit = QLineEdit(ServerSettingWidget)
        self.server_token_line_edit.setObjectName(u"server_token_line_edit")

        self.verticalLayout_2.addWidget(self.server_token_line_edit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(ServerSettingWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(ServerSettingWidget)
        self.buttonBox.accepted.connect(ServerSettingWidget.accept)
        self.buttonBox.rejected.connect(ServerSettingWidget.reject)

        QMetaObject.connectSlotsByName(ServerSettingWidget)
    # setupUi

    def retranslateUi(self, ServerSettingWidget):
        ServerSettingWidget.setWindowTitle(QCoreApplication.translate("ServerSettingWidget", u"Pattaya server setting", None))
        self.label.setText(QCoreApplication.translate("ServerSettingWidget", u"Pattaya server URL : ", None))
        self.label_2.setText(QCoreApplication.translate("ServerSettingWidget", u"Token : ", None))
    # retranslateUi

