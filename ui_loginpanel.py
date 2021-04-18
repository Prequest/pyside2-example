# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginpanelClxqta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        if not UserWindow.objectName():
            UserWindow.setObjectName(u"UserWindow")
        UserWindow.resize(493, 392)
        self.centralwidget = QWidget(UserWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.mainFrame.setFont(font)
        self.mainFrame.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(56,58,89);\n"
"	color:rgb(100, 100, 149);\n"
"	border-radius:10px\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.mainFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 270, 391, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color:rgb(98, 114, 164);\n"
"	color:rgb(0, 0, 127);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:0.682, y2:0.0170455, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(85, 255, 255, 255));\n"
"	\n"
"}\n"
"#background-color: qlineargradient(spread:pad, x1:0, y1:0.465909, x2:0.903409, y2:0.943, stop:0 rgba(255, 114, 233, 255), stop:0.9375 rgba(170, 85, 255, 255));")
        self.progressBar.setValue(50)
        self.lbl_credit = QLabel(self.mainFrame)
        self.lbl_credit.setObjectName(u"lbl_credit")
        self.lbl_credit.setGeometry(QRect(310, 340, 161, 21))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.lbl_credit.setFont(font1)
        self.lbl_credit.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:0.682, y2:0.0170455, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(85, 255, 255, 255));")
        self.lbl_credit.setAlignment(Qt.AlignCenter)
        self.loginFrame = QFrame(self.mainFrame)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setGeometry(QRect(110, 90, 261, 151))
        self.loginFrame.setStyleSheet(u"QLabel {\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:0.682, y2:0.0170455, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(85, 255, 255, 255));\n"
"	font: 87 10pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius:6px;\n"
"	background-color: rgb(122, 127, 194);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	background-color:rgb(77, 80, 122);\n"
"	border:2px solid qlineargradient(spread:pad, x1:0, y1:0.653, x2:0.682, y2:0.0170455, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(85, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius:6px;\n"
"	background-color: rgb(122, 127, 194);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:0.682, y2:0.0170455, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(85, 255, 255, 255));\n"
"	color: rgb(85, 0, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.loginFrame.setFrameShape(QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.loginFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(24)
        self.lbl_username = QLabel(self.loginFrame)
        self.lbl_username.setObjectName(u"lbl_username")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_username)

        self.le_username = QLineEdit(self.loginFrame)
        self.le_username.setObjectName(u"le_username")
        self.le_username.setMinimumSize(QSize(0, 25))
        self.le_username.setStyleSheet(u"")
        self.le_username.setCursorPosition(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_username)

        self.lbl_password = QLabel(self.loginFrame)
        self.lbl_password.setObjectName(u"lbl_password")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_password)

        self.le_password = QLineEdit(self.loginFrame)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setMinimumSize(QSize(0, 25))
        self.le_password.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_password)

        self.pb_login = QPushButton(self.loginFrame)
        self.pb_login.setObjectName(u"pb_login")
        self.pb_login.setMinimumSize(QSize(120, 30))
        self.pb_login.setMaximumSize(QSize(16777215, 16777215))
        self.pb_login.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.pb_login)

        self.pb_forgot = QPushButton(self.loginFrame)
        self.pb_forgot.setObjectName(u"pb_forgot")
        self.pb_forgot.setMinimumSize(QSize(120, 30))
        self.pb_forgot.setMaximumSize(QSize(120, 16777215))
        self.pb_forgot.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pb_forgot)

        self.lbl_brand = QLabel(self.mainFrame)
        self.lbl_brand.setObjectName(u"lbl_brand")
        self.lbl_brand.setGeometry(QRect(200, 20, 81, 48))
        self.lbl_brand.setStyleSheet(u"QLabel {\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:0.682, y2:0.0170455, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(85, 255, 255, 255));\n"
"	font: 75 32pt \"Berlin Sans FB\";\n"
"}")

        self.verticalLayout.addWidget(self.mainFrame)

        UserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserWindow)

        QMetaObject.connectSlotsByName(UserWindow)
    # setupUi

    def retranslateUi(self, UserWindow):
        UserWindow.setWindowTitle(QCoreApplication.translate("UserWindow", u"MainWindow", None))
        self.progressBar.setFormat(QCoreApplication.translate("UserWindow", u"%p%", None))
        self.lbl_credit.setText(QCoreApplication.translate("UserWindow", u"Designed: OTA", None))
        self.lbl_username.setText(QCoreApplication.translate("UserWindow", u"Username:", None))
        self.le_username.setInputMask("")
        self.le_username.setText("")
        self.le_username.setPlaceholderText("")
        self.lbl_password.setText(QCoreApplication.translate("UserWindow", u"Passsword:", None))
        self.pb_login.setText(QCoreApplication.translate("UserWindow", u"Login", None))
        self.pb_forgot.setText(QCoreApplication.translate("UserWindow", u"Forgot Password", None))
        self.lbl_brand.setText(QCoreApplication.translate("UserWindow", u"OTA", None))
    # retranslateUi

