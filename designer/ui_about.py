# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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

class Ui_AboutWidget(object):
    def setupUi(self, AboutWidget):
        if not AboutWidget.objectName():
            AboutWidget.setObjectName(u"AboutWidget")
        AboutWidget.setWindowModality(Qt.ApplicationModal)
        AboutWidget.resize(352, 188)
        AboutWidget.setMinimumSize(QSize(352, 188))
        AboutWidget.setMaximumSize(QSize(352, 188))
        AboutWidget.setMouseTracking(True)
        self.label_3 = QLabel(AboutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 80, 81, 16))
        self.label_4 = QLabel(AboutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 80, 121, 16))
        self.label_5 = QLabel(AboutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 100, 161, 16))
        self.label_6 = QLabel(AboutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 120, 161, 16))
        self.label_7 = QLabel(AboutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 150, 81, 16))
        self.label_8 = QLabel(AboutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 150, 101, 16))
        self.label_8.setOpenExternalLinks(True)
        self.layoutWidget = QWidget(AboutWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 10, 291, 61))
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


        self.retranslateUi(AboutWidget)

        QMetaObject.connectSlotsByName(AboutWidget)
    # setupUi

    def retranslateUi(self, AboutWidget):
        AboutWidget.setWindowTitle(QCoreApplication.translate("AboutWidget", u"About Pattaya Project", None))
        self.label_3.setText(QCoreApplication.translate("AboutWidget", u"Tech stacks :", None))
        self.label_4.setText(QCoreApplication.translate("AboutWidget", u"Panel -> Pyside6", None))
        self.label_5.setText(QCoreApplication.translate("AboutWidget", u"Server -> Nestjs/Socket.io", None))
        self.label_6.setText(QCoreApplication.translate("AboutWidget", u"Client ->C# (.Net)", None))
        self.label_7.setText(QCoreApplication.translate("AboutWidget", u"Developer :", None))
        self.label_8.setText(QCoreApplication.translate("AboutWidget", u"<html><head/><body><p><a href=\"https://github.com/un4ckn0wl3z\"><span style=\" font-size:10pt; font-weight:700; color:#0000ff;\">un4ckn0wl3z</span></a></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("AboutWidget", u"Pattaya Project", None))
        self.label_2.setText(QCoreApplication.translate("AboutWidget", u"A Real-Time based Remote Administrator Tool", None))
    # retranslateUi

