# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ahakeuMmF.ui'
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
        Form.resize(355, 596)
        Form.setStyleSheet(u"background-color:rgb(225, 228, 255);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: blue;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.keyword_input = QLineEdit(Form)
        self.keyword_input.setObjectName(u"keyword_input")
        font2 = QFont()
        font2.setPointSize(10)
        self.keyword_input.setFont(font2)
        self.keyword_input.setStyleSheet(u"background-color: rgb(237, 249, 255);\n"
"border: none;\n"
"border-radius: 5px")

        self.verticalLayout.addWidget(self.keyword_input)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.detailCategory_input = QLineEdit(Form)
        self.detailCategory_input.setObjectName(u"detailCategory_input")
        self.detailCategory_input.setFont(font2)
        self.detailCategory_input.setStyleSheet(u"background-color: rgb(237, 249, 255);\n"
"border: none;\n"
"border-radius: 5px")

        self.verticalLayout.addWidget(self.detailCategory_input)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setBold(True)
        self.label_5.setFont(font3)

        self.verticalLayout.addWidget(self.label_5)

        self.scroll_number = QLineEdit(Form)
        self.scroll_number.setObjectName(u"scroll_number")
        self.scroll_number.setFont(font2)

        self.verticalLayout.addWidget(self.scroll_number)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.result = QTextEdit(Form)
        self.result.setObjectName(u"result")
        self.result.setStyleSheet(u"background-color: rgb(237, 249, 255);\n"
"border: none;\n"
"border-radius: 5px")

        self.verticalLayout.addWidget(self.result)

        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setWeight(QFont.DemiBold)
        self.reset_btn.setFont(font4)
        self.reset_btn.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgba(71, 47, 255, 0.8);\n"
"color: white;\n"
"font-weight: 600;")

        self.verticalLayout.addWidget(self.reset_btn)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)

        self.quit_btn = QPushButton(Form)
        self.quit_btn.setObjectName(u"quit_btn")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setWeight(QFont.DemiBold)
        self.quit_btn.setFont(font5)
        self.quit_btn.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgba(71, 47, 255, 0.8);\n"
"color: white;\n"
"font-weight: 600;")

        self.gridLayout.addWidget(self.quit_btn, 4, 0, 1, 2)

        self.start_btn = QPushButton(Form)
        self.start_btn.setObjectName(u"start_btn")
        font6 = QFont()
        font6.setPointSize(15)
        font6.setWeight(QFont.DemiBold)
        self.start_btn.setFont(font6)
        self.start_btn.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgba(71, 47, 255, 0.8);\n"
"color: white;\n"
"font-weight: 600;")

        self.gridLayout.addWidget(self.start_btn, 2, 0, 1, 2)

        self.downLoad_btn = QPushButton(Form)
        self.downLoad_btn.setObjectName(u"downLoad_btn")
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.downLoad_btn.setFont(font7)
        self.downLoad_btn.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgba(71, 47, 255, 0.8);\n"
"color: white;\n"
"font-weight: 700;")

        self.gridLayout.addWidget(self.downLoad_btn, 3, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc544\ud558!", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ud0a4\uc6cc\ub4dc", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\uc0c1\uc138\ud0a4\uc6cc\ub4dc", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\uc2a4\ud06c\ub864 \uc218", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\uacb0\uacfc", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"\ub9ac\uc14b \ud558\uae30!", None))
        self.quit_btn.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc\ud558\uae30", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"\ucd94\ucd9c \ud558\uae30!", None))
        self.downLoad_btn.setText(QCoreApplication.translate("Form", u"\uc5d1\uc140\ub85c \ub0b4\ub824\ubc1b\uae30", None))
    # retranslateUi

