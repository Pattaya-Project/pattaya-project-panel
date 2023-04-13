# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QTableView, QTextBrowser, QToolBar, QVBoxLayout,
    QWidget)
import designer.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1117, 700)
        MainWindow.setMinimumSize(QSize(1049, 610))
        MainWindow.setMaximumSize(QSize(16777215, 700))
        self.actionStart = QAction(MainWindow)
        self.actionStart.setObjectName(u"actionStart")
        icon = QIcon()
        icon.addFile(u":/assets/images/plug-connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStart.setIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/assets/images/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionServer_setting = QAction(MainWindow)
        self.actionServer_setting.setObjectName(u"actionServer_setting")
        icon2 = QIcon()
        icon2.addFile(u":/assets/images/server--pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionServer_setting.setIcon(icon2)
        self.actionAbout_Pattaya_Project = QAction(MainWindow)
        self.actionAbout_Pattaya_Project.setObjectName(u"actionAbout_Pattaya_Project")
        icon3 = QIcon()
        icon3.addFile(u":/assets/images/information-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_Pattaya_Project.setIcon(icon3)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        icon4 = QIcon()
        icon4.addFile(u":/assets/images/qt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_Qt.setIcon(icon4)
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        icon5 = QIcon()
        icon5.addFile(u":/assets/images/plug-disconnect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStop.setIcon(icon5)
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        icon6 = QIcon()
        icon6.addFile(u":/assets/images/monitor-off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDark.setIcon(icon6)
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        icon7 = QIcon()
        icon7.addFile(u":/assets/images/monitor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLight.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bot_table_view = QTableView(self.centralwidget)
        self.bot_table_view.setObjectName(u"bot_table_view")
        self.bot_table_view.setMinimumSize(QSize(991, 371))
        self.bot_table_view.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.bot_table_view)

        self.control_tab = QTabWidget(self.centralwidget)
        self.control_tab.setObjectName(u"control_tab")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.panel_log_text_browser = QTextBrowser(self.tab)
        self.panel_log_text_browser.setObjectName(u"panel_log_text_browser")

        self.verticalLayout_2.addWidget(self.panel_log_text_browser)

        self.control_tab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.server_log_text_browser = QTextBrowser(self.tab_2)
        self.server_log_text_browser.setObjectName(u"server_log_text_browser")

        self.verticalLayout_3.addWidget(self.server_log_text_browser)

        self.control_tab.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.control_tab)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1117, 22))
        self.menuPattaya = QMenu(self.menubar)
        self.menuPattaya.setObjectName(u"menuPattaya")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuTheme = QMenu(self.menubar)
        self.menuTheme.setObjectName(u"menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuPattaya.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuPattaya.addAction(self.actionStart)
        self.menuPattaya.addAction(self.actionStop)
        self.menuPattaya.addAction(self.actionExit)
        self.menuSetting.addAction(self.actionServer_setting)
        self.menuAbout.addAction(self.actionAbout_Pattaya_Project)
        self.menuAbout.addAction(self.actionAbout_Qt)
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addSeparator()
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionServer_setting)

        self.retranslateUi(MainWindow)

        self.control_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pattaya Project Panel - $VERSION [ Online bots: $ONLINE_BOT ]", None))
        self.actionStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionServer_setting.setText(QCoreApplication.translate("MainWindow", u"Server setting", None))
        self.actionAbout_Pattaya_Project.setText(QCoreApplication.translate("MainWindow", u"About Pattaya Project", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.control_tab.setTabText(self.control_tab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Panel log viewer", None))
        self.control_tab.setTabText(self.control_tab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Server log viewer", None))
        self.menuPattaya.setTitle(QCoreApplication.translate("MainWindow", u"Pattaya", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

