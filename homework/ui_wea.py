# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wea.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)
import res_rc

class Ui_MainWindow01(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 609)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sta = QStackedWidget(self.centralwidget)
        self.sta.setObjectName(u"sta")
        self.sta.setGeometry(QRect(0, 0, 805, 1000))
        self.sta.setMaximumSize(QSize(16777215, 1000))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.background = QGroupBox(self.page)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 280, 801, 301))
        self.pushButton_4 = QPushButton(self.background)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(270, 90, 51, 31))
        icon = QIcon()
        icon.addFile(u":/image/res/ChengDuIcon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(30, 35))
        self.pushButton_3 = QPushButton(self.background)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(450, 120, 41, 41))
        icon1 = QIcon()
        icon1.addFile(u":/image/res/GuangZhouIcon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(30, 40))
        self.pushButton_2 = QPushButton(self.background)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(540, 120, 41, 51))
        icon2 = QIcon()
        icon2.addFile(u":/image/res/ShangHaiIcon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(60, 40))
        self.pushButton = QPushButton(self.background)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 100, 61, 24))
        icon3 = QIcon()
        icon3.addFile(u":/image/res/BeiJingIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(50, 50))
        self.back = QPushButton(self.background)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 30, 50, 40))
        self.back.setIconSize(QSize(50, 40))
        self.sta.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.sta.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.sta.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.sta.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.background.setTitle("")
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.back.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
    # retranslateUi

