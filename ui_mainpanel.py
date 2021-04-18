# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpanelLHXibB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainPanel(object):
    def setupUi(self, MainPanel):
        if not MainPanel.objectName():
            MainPanel.setObjectName(u"MainPanel")
        MainPanel.resize(669, 537)
        self.centralwidget = QWidget(MainPanel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 500))
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setStyleSheet(u"background-color: rgb(45, 46, 45);\n"
"")
        self.centralframe.setFrameShape(QFrame.NoFrame)
        self.centralframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centralframe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QFrame(self.centralframe)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 50))
        self.title.setStyleSheet(u"background-color: rgb(39, 40, 39);")
        self.title.setFrameShape(QFrame.Panel)
        self.title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_toogle = QFrame(self.title)
        self.title_toogle.setObjectName(u"title_toogle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_toogle.sizePolicy().hasHeightForWidth())
        self.title_toogle.setSizePolicy(sizePolicy)
        self.title_toogle.setMinimumSize(QSize(70, 0))
        self.title_toogle.setMaximumSize(QSize(70, 16777215))
        self.title_toogle.setStyleSheet(u"background-color: rgb(39, 40, 39);")
        self.title_toogle.setFrameShape(QFrame.StyledPanel)
        self.title_toogle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.title_toogle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pb_toggle = QPushButton(self.title_toogle)
        self.pb_toggle.setObjectName(u"pb_toggle")
        self.pb_toggle.setMinimumSize(QSize(70, 50))
        self.pb_toggle.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(39, 40, 39);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	\n"
"	background-color: rgb(85, 85, 127);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8_menu_32px_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_toggle.setIcon(icon)
        self.pb_toggle.setIconSize(QSize(32, 32))
        self.pb_toggle.setFlat(True)

        self.verticalLayout_3.addWidget(self.pb_toggle)


        self.horizontalLayout.addWidget(self.title_toogle)

        self.title_brand = QFrame(self.title)
        self.title_brand.setObjectName(u"title_brand")
        self.title_brand.setFrameShape(QFrame.StyledPanel)
        self.title_brand.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_brand)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, 0, 0, 0)
        self.lbl_title = QLabel(self.title_brand)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(13)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet(u"color: rgb(177, 177, 177);")
        self.lbl_title.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_5.addWidget(self.lbl_title)


        self.horizontalLayout.addWidget(self.title_brand)

        self.title_buttons = QFrame(self.title)
        self.title_buttons.setObjectName(u"title_buttons")
        self.title_buttons.setMinimumSize(QSize(100, 0))
        self.title_buttons.setMaximumSize(QSize(100, 16777215))
        self.title_buttons.setFrameShape(QFrame.StyledPanel)
        self.title_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.title_buttons)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.pb_minimize = QPushButton(self.title_buttons)
        self.pb_minimize.setObjectName(u"pb_minimize")
        self.pb_minimize.setMaximumSize(QSize(24, 24))
        self.pb_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(121, 124, 121);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8_minimize_window_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_minimize.setIcon(icon1)
        self.pb_minimize.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pb_minimize)

        self.pb_maximize = QPushButton(self.title_buttons)
        self.pb_maximize.setObjectName(u"pb_maximize")
        self.pb_maximize.setMaximumSize(QSize(24, 24))
        self.pb_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(121, 124, 121);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color:rgb(85, 255, 0)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8_maximize_window_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_maximize.setIcon(icon2)
        self.pb_maximize.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pb_maximize)

        self.pb_exit = QPushButton(self.title_buttons)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setMaximumSize(QSize(24, 24))
        self.pb_exit.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(121, 124, 121);\n"
"}\n"
"\n"
"\n"
"QPushButton::hover {\n"
"	background-color:rgb(255, 0, 0)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8_close_window_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_exit.setIcon(icon3)
        self.pb_exit.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pb_exit)


        self.horizontalLayout.addWidget(self.title_buttons)


        self.verticalLayout_2.addWidget(self.title)

        self.content = QFrame(self.centralframe)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color:None;")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.content)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.content)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(70, 0))
        self.left_menu.setMaximumSize(QSize(75, 16777215))
        self.left_menu.setStyleSheet(u"background-color: rgb(39, 40, 39);\n"
"")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.left_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(39, 40, 39);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(85, 85, 127);\n"
"}")
        self.frame_top_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pb_home = QPushButton(self.frame_top_menus)
        self.pb_home.setObjectName(u"pb_home")
        self.pb_home.setMinimumSize(QSize(0, 30))
        self.pb_home.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8_home_32px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_home.setIcon(icon4)
        self.pb_home.setIconSize(QSize(32, 32))
        self.pb_home.setFlat(True)

        self.verticalLayout_6.addWidget(self.pb_home)

        self.pb_form = QPushButton(self.frame_top_menus)
        self.pb_form.setObjectName(u"pb_form")
        self.pb_form.setMinimumSize(QSize(0, 30))
        self.pb_form.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icons8_new_document_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_form.setIcon(icon5)
        self.pb_form.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pb_form)

        self.pb_settings = QPushButton(self.frame_top_menus)
        self.pb_settings.setObjectName(u"pb_settings")
        self.pb_settings.setMinimumSize(QSize(0, 30))
        self.pb_settings.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icons8_settings_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_settings.setIcon(icon6)
        self.pb_settings.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pb_settings)


        self.verticalLayout_5.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_6.addWidget(self.left_menu)

        self.content_pages = QFrame(self.content)
        self.content_pages.setObjectName(u"content_pages")
        self.content_pages.setFrameShape(QFrame.StyledPanel)
        self.content_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.content_pages)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pages_widget = QStackedWidget(self.content_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.pages_widget.setFrameShape(QFrame.NoFrame)
        self.pages_widget.setLineWidth(0)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 170, 51, 21))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pages_widget.addWidget(self.page_home)
        self.page_form = QWidget()
        self.page_form.setObjectName(u"page_form")
        self.label_4 = QLabel(self.page_form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 180, 91, 21))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pages_widget.addWidget(self.page_form)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.label_5 = QLabel(self.page_settings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 160, 47, 13))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pages_widget.addWidget(self.page_settings)

        self.verticalLayout_7.addWidget(self.pages_widget)


        self.horizontalLayout_6.addWidget(self.content_pages)


        self.verticalLayout_2.addWidget(self.content)

        self.footer = QFrame(self.centralframe)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 30))
        self.footer.setMaximumSize(QSize(16777215, 50))
        self.footer.setStyleSheet(u"")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.footer_author = QFrame(self.footer)
        self.footer_author.setObjectName(u"footer_author")
        self.footer_author.setFrameShape(QFrame.StyledPanel)
        self.footer_author.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.footer_author)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 0, 0, 0)
        self.label = QLabel(self.footer_author)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Monotype Corsiva")
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(218, 218, 218);")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.footer_author)

        self.footer_expand = QFrame(self.footer)
        self.footer_expand.setObjectName(u"footer_expand")
        self.footer_expand.setMinimumSize(QSize(15, 30))
        self.footer_expand.setMaximumSize(QSize(30, 30))
        self.footer_expand.setFrameShape(QFrame.NoFrame)
        self.footer_expand.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.footer_expand)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.footer_expand)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/skateboard_grip_tape_32px.png"))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.footer_expand)


        self.verticalLayout_2.addWidget(self.footer)


        self.horizontalLayout_2.addWidget(self.centralframe)

        MainPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainPanel)

        self.pages_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPanel)
    # setupUi

    def retranslateUi(self, MainPanel):
        MainPanel.setWindowTitle(QCoreApplication.translate("MainPanel", u"MainWindow", None))
        self.pb_toggle.setText("")
        self.lbl_title.setText(QCoreApplication.translate("MainPanel", u"LOGO AND NAME", None))
        self.pb_minimize.setText("")
        self.pb_maximize.setText("")
        self.pb_exit.setText("")
        self.pb_home.setText("")
        self.pb_form.setText("")
        self.pb_settings.setText("")
        self.label_3.setText(QCoreApplication.translate("MainPanel", u"Homepage", None))
        self.label_4.setText(QCoreApplication.translate("MainPanel", u"Teklif Formu", None))
        self.label_5.setText(QCoreApplication.translate("MainPanel", u"Raporlar", None))
        self.label.setText(QCoreApplication.translate("MainPanel", u"Designed by Who", None))
        self.label_2.setText("")
    # retranslateUi

