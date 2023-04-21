# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'terminal.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_BotTerminalWidget(object):
    def setupUi(self, BotTerminalWidget):
        if not BotTerminalWidget.objectName():
            BotTerminalWidget.setObjectName(u"BotTerminalWidget")
        BotTerminalWidget.resize(1072, 689)
        self.verticalLayout_2 = QVBoxLayout(BotTerminalWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.task_result_text_browser = QTextBrowser(BotTerminalWidget)
        self.task_result_text_browser.setObjectName(u"task_result_text_browser")
        self.task_result_text_browser.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.task_result_text_browser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mark_bar_label = QLabel(BotTerminalWidget)
        self.mark_bar_label.setObjectName(u"mark_bar_label")
        font = QFont()
        font.setPointSize(11)
        self.mark_bar_label.setFont(font)

        self.horizontalLayout.addWidget(self.mark_bar_label)

        self.bot_send_task_line_edit = QLineEdit(BotTerminalWidget)
        self.bot_send_task_line_edit.setObjectName(u"bot_send_task_line_edit")

        self.horizontalLayout.addWidget(self.bot_send_task_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(BotTerminalWidget)

        QMetaObject.connectSlotsByName(BotTerminalWidget)
    # setupUi

    def retranslateUi(self, BotTerminalWidget):
        BotTerminalWidget.setWindowTitle(QCoreApplication.translate("BotTerminalWidget", u"[ Terminal ] - [ $USERNAME ] / $LAN/$WAN / $INTEGR / $PN", None))
        self.mark_bar_label.setText(QCoreApplication.translate("BotTerminalWidget", u">>>", None))
    # retranslateUi

