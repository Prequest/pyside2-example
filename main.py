from PySide2.QtCore import QPropertyAnimation, QTimer
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_loginpanel import Ui_UserWindow
from ui_mainpanel import Ui_MainPanel
import sys


COUNTER = 0
CHECK_STATE = 0


class MainPanel(QMainWindow, Ui_MainPanel):
    def __init__(self, *args, **kwargs):
        super(MainPanel, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pb_exit.setToolTip("Exit")
        self.pb_maximize.setToolTip("Full Screen")
        self.pb_minimize.setToolTip("Minimize")

        ##Hide Window Title##
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        ##Click Events##
        self.pb_maximize.clicked.connect(self.maximize_restore)
        self.pb_exit.clicked.connect(lambda: self.close())
        self.pb_minimize.clicked.connect(lambda: self.showMinimized())
        self.pb_toggle.clicked.connect(self.toggle)
        self.pb_home.clicked.connect(self.button_click)
        self.pb_form.clicked.connect(self.button_click)
        self.pb_settings.clicked.connect(self.button_click)

        ##Resize Event##
        self.resize_window = QSizeGrip(self.footer_expand)

        ##Double-Click Expand Event##
        def expand_window(event):
            if event.buttons() == Qt.LeftButton:
                self.maximize_restore()

        ##Move Event##
        def move_window(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos()+event.globalPos()-self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.title.mouseMoveEvent = move_window
        self.title.mouseDoubleClickEvent = expand_window

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ##Events##
    def maximize_restore(self):
        global CHECK_STATE

        if CHECK_STATE == 0:
            CHECK_STATE = 1
            self.showMaximized()
            self.pb_maximize.setToolTip("Restore")
        else:
            CHECK_STATE = 0
            self.showNormal()
            self.resize(self.width(), self.height())
            self.pb_maximize.setToolTip("Maximize")

    def toggle(self, maxWidth=150, check=True):
        if check:
            width = self.left_menu.width()
            print(width)
            maxExtend = maxWidth
            standart = 70
            if width == 70:
                widthExtended = maxExtend
                self.pb_settings.setText("Settings")
                self.pb_form.setText("Form")
                self.pb_home.setText("Home")
            else:
                widthExtended = standart
                self.pb_settings.setText("")
                self.pb_form.setText("")
                self.pb_home.setText("")
            #Animation#
            self.animation = QPropertyAnimation(
                self.left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

    def button_click(self):
        btn = self.sender()
        btn_name = btn.objectName()
        if btn_name == "pb_home":
            self.pages_widget.setCurrentWidget(self.page_home)
        if btn_name == "pb_form":
            self.pages_widget.setCurrentWidget(self.page_form)
        if btn_name == "pb_settings":
            self.pages_widget.setCurrentWidget(self.page_settings)


class WelcomePanel(QMainWindow, Ui_UserWindow):
    def __init__(self, *args, **kwargs):
        super(WelcomePanel, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #Definitions#
        self.mp = MainPanel()
        self.progressBar.setValue(0)

        #Attributes#
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 200))
        self.mainFrame.setGraphicsEffect(self.shadow)
        # Click Events#
        self.pb_login.clicked.connect(self.login_to)

    def progress(self):
        global COUNTER
        self.progressBar.setValue(COUNTER)

        if COUNTER >= 100:
            self.timer.stop()
            self.mp.show()
            self.close()

        COUNTER += 1

    def login_to(self):
        if self.le_username.text() == "admin" and self.le_password.text() == "1234":
            self.timer = QTimer()
            self.timer.timeout.connect(self.progress)
            self.timer.start(1)
            self.progress()
        else:
            self.qm = QMessageBox()
            self.qm.critical(
                self, "Attent", "Invalid Username or Password", self.qm.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomePanel()
    window.show()
    sys.exit(app.exec_())
