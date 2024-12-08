# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainjjqEyH.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(451, 557)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"backgroud-color : rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 181, 251))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px outset rgb(255, 30, 41);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 340, 181, 181))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px outset rgb(255, 30, 41);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 431, 511))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px outset rgb(255, 30, 41);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 340, 221, 181))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px outset rgb(255, 30, 41);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 101, 31))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px outset rgb(255, 30, 41);\n"
"color: rgb(255, 30, 41);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 80, 221, 251))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px outset rgb(255, 30, 41);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 30, 121, 31))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px outset rgb(255, 30, 41);\n"
"color: rgb(255, 30, 41);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 90, 71, 21))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(270, 90, 91, 21))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(280, 350, 91, 21))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 350, 111, 21))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.keyword_add_btn = QPushButton(self.centralwidget)
        self.keyword_add_btn.setObjectName(u"keyword_add_btn")
        self.keyword_add_btn.setGeometry(QRect(350, 140, 31, 31))
        font1 = QFont()
        font1.setPointSize(7)
        self.keyword_add_btn.setFont(font1)
        self.keyword_add_btn.setStyleSheet(u"QPushButton{\n"
"border-radius: 8px;\n"
"color: white;\n"
"background: rgb(255, 30, 41);\n"
"}\n"
"QPushButton:hover{\n"
"background: rgb(226, 7, 255);\n"
"}\n"
"")
        self.keyword_delet_btn = QPushButton(self.centralwidget)
        self.keyword_delet_btn.setObjectName(u"keyword_delet_btn")
        self.keyword_delet_btn.setGeometry(QRect(390, 140, 31, 31))
        self.keyword_delet_btn.setFont(font1)
        self.keyword_delet_btn.setStyleSheet(u"QPushButton{\n"
"border-radius: 8px;\n"
"color: white;\n"
"background: rgb(255, 30, 41);\n"
"}\n"
"QPushButton:hover{\n"
"background: rgb(226, 7, 255);\n"
"}\n"
"")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 110, 141, 21))
        font2 = QFont()
        font2.setPointSize(8)
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 110, 201, 21))
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 380, 181, 21))
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 140, 50, 16))
        font3 = QFont()
        font3.setBold(True)
        self.label_15.setFont(font3)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 200, 50, 16))
        self.label_16.setFont(font3)
        self.naver_id = QLineEdit(self.centralwidget)
        self.naver_id.setObjectName(u"naver_id")
        self.naver_id.setGeometry(QRect(30, 160, 151, 31))
        self.naver_id.setFont(font1)
        self.naver_id.setStyleSheet(u"border-radius: 4px;\n"
"background: rgb(243, 245, 255);\n"
"padding-left: 8px;")
        self.naver_pw = QLineEdit(self.centralwidget)
        self.naver_pw.setObjectName(u"naver_pw")
        self.naver_pw.setGeometry(QRect(30, 220, 151, 31))
        self.naver_pw.setFont(font1)
        self.naver_pw.setStyleSheet(u"border-radius: 4px;\n"
"background: rgb(243, 245, 255);\n"
"padding-left: 8px;")
        self.keyword_input = QLineEdit(self.centralwidget)
        self.keyword_input.setObjectName(u"keyword_input")
        self.keyword_input.setGeometry(QRect(220, 140, 121, 31))
        self.keyword_input.setFont(font1)
        self.keyword_input.setStyleSheet(u"border-radius: 4px;\n"
"background: rgb(243, 245, 255);\n"
"padding-left: 8px;")
        self.keyword_table = QTableWidget(self.centralwidget)
        if (self.keyword_table.columnCount() < 1):
            self.keyword_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.keyword_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.keyword_table.setObjectName(u"keyword_table")
        self.keyword_table.setGeometry(QRect(217, 180, 204, 141))
        self.keyword_table.setStyleSheet(u"QTableView {\n"
"    border: none;\n"
"    padding: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: rgba(239, 240, 244, 0.8);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"    background-color: #f1f2f6;\n"
"    border: 1px solid #d3d3d3; \n"
"    padding: 0px;  \n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    background-color: #f0f1f5;\n"
"    color: #6e6e6e;\n"
"    font-size: 13px;\n"
"    border: 1px solid #d3d3d3;\n"
"    padding: 0px;\n"
"    text-align: center;\n"
"}\n"
"")
        self.keyword_table.horizontalHeader().setMinimumSectionSize(18)
        self.keyword_table.horizontalHeader().setDefaultSectionSize(203)
        self.comment_box = QPlainTextEdit(self.centralwidget)
        self.comment_box.setObjectName(u"comment_box")
        self.comment_box.setGeometry(QRect(30, 400, 161, 111))
        self.logbox = QPlainTextEdit(self.centralwidget)
        self.logbox.setObjectName(u"logbox")
        self.logbox.setGeometry(QRect(220, 380, 201, 91))
        self.process_start = QPushButton(self.centralwidget)
        self.process_start.setObjectName(u"process_start")
        self.process_start.setGeometry(QRect(220, 480, 201, 31))
        self.process_start.setFont(font)
        self.process_start.setStyleSheet(u"QPushButton{\n"
"border-radius: 8px;\n"
"color: white;\n"
"background: rgb(255, 30, 41);\n"
"}\n"
"QPushButton:hover{\n"
"background: rgb(226, 7, 255);\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_6.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.keyword_add_btn.raise_()
        self.keyword_delet_btn.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.naver_id.raise_()
        self.naver_pw.raise_()
        self.keyword_input.raise_()
        self.keyword_table.raise_()
        self.comment_box.raise_()
        self.logbox.raise_()
        self.process_start.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText("")
        self.label_6.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"2025-12-31\uae4c\uc9c0", None))
        self.label_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc548\ub155\ud558\uc138\uc694 00\ub2d8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815 \uc815\ubcf4", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\ud0a4\uc6cc\ub4dc \ucd94\ucd9c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uc11c\uc774\ucd94 \uc791\ub3d9", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc6c3 \uc2e0\uccad \uba58\ud2b8", None))
        self.keyword_add_btn.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00", None))
        self.keyword_delet_btn.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\ub124\uc774\ubc84 \uacc4\uc815\uc744 \uc785\ub825\ud558\uc138\uc694", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\ud0a4\uc6cc\ub4dc\ub85c \uc774\uc6c3\uc744 \ucd94\ucd9c\ud569\ub2c8\ub2e4.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc6c3 \uc2e0\uccad\uc5d0 \uc0ac\uc6a9\ub420 \uba58\ud2b8\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.naver_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        self.naver_pw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        self.keyword_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ud0a4\uc6cc\ub4dc\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        ___qtablewidgetitem = self.keyword_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\ud0a4\uc6cc\ub4dc", None));
        self.process_start.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc6c3 \uc2e0\uccad \uc2dc\uc791", None))
    # retranslateUi

