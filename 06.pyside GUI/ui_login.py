# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginxlayEr.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(232, 483)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-4, 0, 261, 351))
        self.label.setStyleSheet(u"background-color : white;\n"
"padding : 5px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(36, 110, 81, 20))
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(36, 170, 121, 16))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.login_btn = QPushButton(self.centralwidget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(36, 260, 161, 24))
        self.login_btn.setStyleSheet(u"background-color: rgba(232,30,37,0.8);\n"
"color:white;\n"
"border-radius: 10px;\n"
"")
        self.account_id = QLineEdit(self.centralwidget)
        self.account_id.setObjectName(u"account_id")
        self.account_id.setGeometry(QRect(36, 130, 161, 31))
        self.account_id.setStyleSheet(u"\n"
"padding-left: 6px;\n"
"background-color : rgb(170 187 204);")
        self.account_pw = QLineEdit(self.centralwidget)
        self.account_pw.setObjectName(u"account_pw")
        self.account_pw.setGeometry(QRect(36, 190, 161, 31))
        self.account_pw.setStyleSheet(u"\n"
"padding-left: 6px;\n"
"background-color : rgb(170 187 204);")
        self.account_pw.setEchoMode(QLineEdit.EchoMode.Normal)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(36, 70, 141, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(36, 230, 111, 20))
        font2 = QFont()
        font2.setPointSize(6)
        self.checkBox.setFont(font2)
        self.blog_visit_btn = QPushButton(self.centralwidget)
        self.blog_visit_btn.setObjectName(u"blog_visit_btn")
        self.blog_visit_btn.setGeometry(QRect(40, 290, 151, 24))
        font3 = QFont()
        font3.setPointSize(7)
        self.blog_visit_btn.setFont(font3)
        self.blog_visit_btn.setStyleSheet(u"background-color : white;\n"
"color:blue;\n"
"border: none;")
        self.main_logo = QLabel(self.centralwidget)
        self.main_logo.setObjectName(u"main_logo")
        self.main_logo.setGeometry(QRect(80, 20, 50, 41))
        self.main_logo.setStyleSheet(u"background-color: rgb(255, 242, 245);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778", None))
        self.account_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.account_pw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ucca0\ucc9c\ubb34\uae30(\uc11c\uc774\uc8fc)", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815 \uae30\uc5b5\ud558\uae30", None))
        self.blog_visit_btn.setText(QCoreApplication.translate("MainWindow", u"\ucca0\ucc9c\ubb34\uae30 \uad6c\uacbd\ud558\ub7ec \uac00\uae30", None))
        self.main_logo.setText("")
    # retranslateUi

