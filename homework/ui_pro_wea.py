# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pro_wea.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1027, 685)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 440, 811, 201))
        self.frame_wind = QFrame(self.widget)
        self.frame_wind.setObjectName(u"frame_wind")
        self.frame_wind.setGeometry(QRect(20, 10, 194, 36))
        self.frame_wind.setFrameShape(QFrame.StyledPanel)
        self.frame_wind.setFrameShadow(QFrame.Raised)
        self.wind_icon = QLabel(self.frame_wind)
        self.wind_icon.setObjectName(u"wind_icon")
        self.wind_icon.setGeometry(QRect(10, 6, 75, 21))
        self.wind = QLabel(self.frame_wind)
        self.wind.setObjectName(u"wind")
        self.wind.setGeometry(QRect(110, 10, 54, 16))
        self.frame_wind_pos = QFrame(self.widget)
        self.frame_wind_pos.setObjectName(u"frame_wind_pos")
        self.frame_wind_pos.setGeometry(QRect(20, 50, 194, 36))
        self.frame_wind_pos.setFrameShape(QFrame.StyledPanel)
        self.frame_wind_pos.setFrameShadow(QFrame.Raised)
        self.wind_pos_icon = QLabel(self.frame_wind_pos)
        self.wind_pos_icon.setObjectName(u"wind_pos_icon")
        self.wind_pos_icon.setGeometry(QRect(10, 5, 75, 21))
        self.wind_pos = QLabel(self.frame_wind_pos)
        self.wind_pos.setObjectName(u"wind_pos")
        self.wind_pos.setGeometry(QRect(110, 10, 54, 16))
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 90, 194, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.wet_icon = QLabel(self.frame_3)
        self.wet_icon.setObjectName(u"wet_icon")
        self.wet_icon.setGeometry(QRect(10, 6, 81, 51))
        self.wet = QLabel(self.frame_3)
        self.wet.setObjectName(u"wet")
        self.wet.setGeometry(QRect(110, 10, 54, 41))
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(260, 10, 531, 36))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(260, 50, 531, 36))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(260, 90, 531, 61))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.temp = QWebEngineView(Form)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(10, 10, 1011, 401))
        self.temp.setUrl(QUrl(u"about:blank"))
        self.frame_8 = QFrame(Form)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(30, 420, 791, 31))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(270, 10, 54, 16))
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(400, 10, 54, 16))
        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(530, 10, 54, 16))
        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(660, 10, 54, 16))
        self.label_21 = QLabel(self.frame_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(130, 10, 54, 16))
        self.frame_9 = QFrame(Form)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(840, 450, 151, 36))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 51, 16))
        self.PM25 = QLabel(self.frame_9)
        self.PM25.setObjectName(u"PM25")
        self.PM25.setGeometry(QRect(87, 10, 54, 16))
        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(930, 620, 91, 41))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(840, 490, 151, 36))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pm = QLabel(self.frame_2)
        self.pm.setObjectName(u"pm")

        self.horizontalLayout_3.addWidget(self.pm)

        self.pm_icon = QLabel(self.frame_2)
        self.pm_icon.setObjectName(u"pm_icon")

        self.horizontalLayout_3.addWidget(self.pm_icon)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.wind_icon.setText("")
        self.wind.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.wind_pos_icon.setText("")
        self.wind_pos.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.wet_icon.setText("")
        self.wet.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u65e5\u671f", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"PM2.5", None))
        self.PM25.setText("")
        self.back.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.pm.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pm_icon.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

