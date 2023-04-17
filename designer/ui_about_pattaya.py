# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_pattaya.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import designer.resource_rc

class Ui_AboutPattayaWidget(object):
    def setupUi(self, AboutPattayaWidget):
        if not AboutPattayaWidget.objectName():
            AboutPattayaWidget.setObjectName(u"AboutPattayaWidget")
        AboutPattayaWidget.setWindowModality(Qt.NonModal)
        AboutPattayaWidget.resize(490, 189)
        AboutPattayaWidget.setMinimumSize(QSize(490, 189))
        AboutPattayaWidget.setMaximumSize(QSize(490, 189))
        AboutPattayaWidget.setCursor(QCursor(Qt.CrossCursor))
        AboutPattayaWidget.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/assets/images/rat.png", QSize(), QIcon.Normal, QIcon.Off)
        AboutPattayaWidget.setWindowIcon(icon)
        self.label_7 = QLabel(AboutPattayaWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 150, 81, 16))
        self.layoutWidget = QWidget(AboutPattayaWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 291, 61))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(AboutPattayaWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 80, 121, 16))
        self.label_5 = QLabel(AboutPattayaWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 100, 161, 16))
        self.label_3 = QLabel(AboutPattayaWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 81, 16))
        self.label_8 = QLabel(AboutPattayaWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 150, 101, 16))
        self.label_8.setOpenExternalLinks(True)
        self.label_6 = QLabel(AboutPattayaWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 120, 161, 16))
        self.label_9 = QLabel(AboutPattayaWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 10, 171, 171))
        self.label_9.setPixmap(QPixmap(u":/assets/images/rat.png"))
        self.label_9.setScaledContents(True)

        self.retranslateUi(AboutPattayaWidget)

        QMetaObject.connectSlotsByName(AboutPattayaWidget)
    # setupUi

    def retranslateUi(self, AboutPattayaWidget):
        AboutPattayaWidget.setWindowTitle(QCoreApplication.translate("AboutPattayaWidget", u"About Pattaya Project", None))
        self.label_7.setText(QCoreApplication.translate("AboutPattayaWidget", u"Developer :", None))
        self.label.setText(QCoreApplication.translate("AboutPattayaWidget", u"Pattaya Project", None))
        self.label_2.setText(QCoreApplication.translate("AboutPattayaWidget", u"A Real-Time based Remote Administrator Tool", None))
        self.label_4.setText(QCoreApplication.translate("AboutPattayaWidget", u"Panel -> Pyside6", None))
        self.label_5.setText(QCoreApplication.translate("AboutPattayaWidget", u"Server -> Nestjs/Socket.io", None))
        self.label_3.setText(QCoreApplication.translate("AboutPattayaWidget", u"Tech stacks :", None))
        self.label_8.setText(QCoreApplication.translate("AboutPattayaWidget", u"<html><head/><body><p><a href=\"https://github.com/un4ckn0wl3z\"><span style=\" font-size:10pt; font-weight:700; color:#0000ff;\">un4ckn0wl3z</span></a></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("AboutPattayaWidget", u"Client ->C# (.Net)", None))
        self.label_9.setText("")
    # retranslateUi

