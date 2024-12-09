# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gameRqgjxf.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(611, 607)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 90, 351, 461))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font = QFont()
        font.setFamilies([u"\ud734\uba3c\ub9e4\uc9c1\uccb4"])
        font.setPointSize(11)
        font.setBold(False)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"padding:5px ;\n"
"background-color: rgb(255, 248, 248)")

        self.gridLayout.addWidget(self.comboBox, 1, 5, 1, 1)

        self.result = QTextBrowser(self.widget)
        self.result.setObjectName(u"result")
        self.result.setStyleSheet(u"border: none;\n"
"outlink: none;")

        self.gridLayout.addWidget(self.result, 8, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"\ud734\uba3c\ub9e4\uc9c1\uccb4"])
        font1.setPointSize(11)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"\ud734\uba3c\ub9e4\uc9c1\uccb4"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"padding:5px;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 5, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.reset_btn = QPushButton(self.widget)
        self.reset_btn.setObjectName(u"reset_btn")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.reset_btn.setFont(font3)
        self.reset_btn.setStyleSheet(u"background-color: rgb(255, 94, 97);")

        self.verticalLayout.addWidget(self.reset_btn)

        self.start_btn = QPushButton(self.widget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setFont(font3)
        self.start_btn.setStyleSheet(u"background-color: rgb(255, 94, 97);")

        self.verticalLayout.addWidget(self.start_btn)

        self.downLoad_btn = QPushButton(self.widget)
        self.downLoad_btn.setObjectName(u"downLoad_btn")
        self.downLoad_btn.setFont(font3)
        self.downLoad_btn.setStyleSheet(u"background-color: rgb(255, 94, 97);")

        self.verticalLayout.addWidget(self.downLoad_btn)

        self.quit_btn = QPushButton(self.widget)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setFont(font3)
        self.quit_btn.setStyleSheet(u"background-color: rgb(255, 94, 97);")

        self.verticalLayout.addWidget(self.quit_btn)


        self.gridLayout.addLayout(self.verticalLayout, 8, 5, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 8, 4, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(23)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"background-color: rgb(255, 34, 38);\n"
"border: none;\n"
"outline: none;\n"
"padding: 0;\n"
"margin: 0;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\uac8c\uc784", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\uc601\ud654", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"HAPPY DAY", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"category", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"RESET", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"START", None))
        self.downLoad_btn.setText(QCoreApplication.translate("Form", u"GET", None))
        self.quit_btn.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"YOUTUBE", None))
    # retranslateUi

