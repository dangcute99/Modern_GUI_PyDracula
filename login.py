# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginBoIuKd.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"ĐĂNG NHẬP")
        Form.resize(740, 360)
        
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(130, 0))
        self.label.setPixmap(QPixmap(u":/images/images/images/logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font: 700 20pt \"Times New Roman\";\n"
"color: rgb(85, 170, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font: 700 17pt \"Times New Roman\";\n"
"color: rgb(255, 0, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 8)
        self.horizontalSpacer = QSpacerItem(212, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer)

        self.verticalSpacer = QSpacerItem(20, 216, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_3 = QPushButton(self.widget_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(u"border-radius: 5px;")
        icon = QIcon()
        icon.addFile(u"C:/Users/FPT SHop/Downloads/caidat.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(20, 20))
        self.pushButton_3.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(300, 0))
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"font: 700 14pt \"Times New Roman\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.widget_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.verticalLayout_5.addWidget(self.lineEdit_2)

        self.checkBox = QCheckBox(self.widget_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.checkBox)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.widget_7)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.horizontalSpacer_2 = QSpacerItem(173, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Đăng Nhập", u"Đăng Nhập", None))
        Form.setWindowIcon(QIcon("images/images/images/icon-1.ico"))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"BINH CH\u1ee6NG TH\u00d4NG TIN LI\u00caN L\u1ea0C", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"H\u1ec6 TH\u1ed0NG GI\u00c1M S\u00c1T, C\u1ea2NH B\u00c1O TR\u1ea0M TH\u00d4NG TIN", None))
        self.pushButton_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u" \u0110\u1ed3ng ch\u00ed nh\u1eadp th\u00f4ng tin", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Nh\u1edb th\u00f4ng tin \u0111\u0103ng nh\u1eadp", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0110\u0103ng nh\u1eadp", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0110\u0103ng k\u00ed", None))
    # retranslateUi

