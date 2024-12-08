# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ahaFpxNCE.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(309, 418)
        Form.setStyleSheet(u"background-color:rgb(225, 228, 255);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.keyword_input = QLineEdit(Form)
        self.keyword_input.setObjectName(u"keyword_input")
        font1 = QFont()
        font1.setPointSize(10)
        self.keyword_input.setFont(font1)
        self.keyword_input.setStyleSheet(u"background-color: rgb(237, 249, 255);\n"
"border: none;\n"
"border-radius: 5px")

        self.verticalLayout.addWidget(self.keyword_input)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(237, 249, 255);\n"
"border: none;\n"
"border-radius: 5px")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.result = QTextEdit(Form)
        self.result.setObjectName(u"result")
        self.result.setStyleSheet(u"background-color: rgb(237, 249, 255);\n"
"border: none;\n"
"border-radius: 5px")

        self.verticalLayout.addWidget(self.result)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setWeight(QFont.DemiBold)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgba(71, 47, 255, 0.8);\n"
"color: white;\n"
"font-weight: 600;")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(17)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: blue;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ud0a4\uc6cc\ub4dc", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\uc0c1\uc138\ud0a4\uc6cc\ub4dc", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\uacb0\uacfc", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\ucd94\ucd9c \ud558\uae30!", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc544\ud558!", None))
    # retranslateUi

