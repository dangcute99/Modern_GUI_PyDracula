# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connectMysqldrOOBN.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Kết Nối MySql")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
       
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(300, 0))
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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

        self.lineEdit_3 = QLineEdit(self.widget_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.verticalLayout_5.addWidget(self.lineEdit_3)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.widget_7)

        self.pushButton_ketnoi_mySql = QPushButton(self.widget_5)
        self.pushButton_ketnoi_mySql.setObjectName(u"pushButton_ketnoi_mySql")
        self.pushButton_ketnoi_mySql.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_ketnoi_mySql.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.pushButton_ketnoi_mySql)


        self.verticalLayout.addWidget(self.widget_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Kết Nối MySql", u"Kết Nối MySql", None))
        Form.setWindowIcon(QIcon("images/images/images/icon-1.ico"))
        self.label_4.setText(QCoreApplication.translate("Kết Nối MySql", u"K\u1ebft n\u1ed1i MySQL", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Host...", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"User...", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Password...", None))
        self.pushButton_ketnoi_mySql.setText(QCoreApplication.translate("Form", u"K\u1ebft N\u1ed1i", None))
    # retranslateUi

