# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'naver_kin.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(451, 378)
        font = QFont()
        font.setFamilies([u"\ud734\uba3c\uc61b\uccb4"])
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.keyword = QLineEdit(Form)
        self.keyword.setObjectName(u"keyword")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.keyword)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.page = QLineEdit(Form)
        self.page.setObjectName(u"page")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.page)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.start_btn = QPushButton(Form)
        self.start_btn.setObjectName(u"start_btn")

        self.verticalLayout_2.addWidget(self.start_btn)

        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")

        self.verticalLayout_2.addWidget(self.reset_btn)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.save_btn = QPushButton(Form)
        self.save_btn.setObjectName(u"save_btn")

        self.verticalLayout_2.addWidget(self.save_btn)

        self.quit_btn = QPushButton(Form)
        self.quit_btn.setObjectName(u"quit_btn")

        self.verticalLayout_2.addWidget(self.quit_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#429101;\">\ub124\uc774\ubc84 \uc9c0\uc2dd\uc778 \ud06c\ub864\ub9c1</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\ud398\uc774\uc9c0\uc218", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ud0a4\uc6cc\ub4dc", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"\ucd94\ucd9c \uc2dc\uc791", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"\ub9ac\uc14b", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5", None))
        self.quit_btn.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc", None))
    # retranslateUi

