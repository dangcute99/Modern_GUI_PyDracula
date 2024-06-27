# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui_newAjvXlu.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1307, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1209, 900))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"border-color: rgb(44, 43, 41);\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"\n"
"/* Icon *"
                        "/\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"\n"
"/* CONTENT SETTINGS */\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, "
                        "43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
""
                        "	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-o"
                        "rigin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-posi"
                        "tion: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(5"
                        "2, 59, 72);\n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"/* CSS cho c\u00e1c n\u00fat ch\u1ecdn (RadioButton) */\n"
"QRadioButton {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* Tr\u1ea1ng th\u00e1i k\u00edch ho\u1ea1t (checked) */\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* Tr\u1ea1ng th\u00e1i kh\u00f4ng k\u00edch ho\u1ea1t */\n"
"QRadioButton::indicator:unchecked {\n"
"    background: rgb(44, 49, 60);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* CSS cho n\u00fat ch\u1ecd"
                        "n (CheckBox) */\n"
"QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* Tr\u1ea1ng th\u00e1i k\u00edch ho\u1ea1t (checked) */\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* Tr\u1ea1ng th\u00e1i kh\u00f4ng k\u00edch ho\u1ea1t */\n"
"QCheckBox::indicator:unchecked {\n"
"    background: rgb(44, 49, 60);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QCom"
                        "boBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb("
                        "55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* ////////"
                        "/////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton::pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"QPushButton {\n"
"    /* X\u00f3a t\u1ea5t c\u1ea3 CSS m\u1eb7c \u0111\u1ecbnh */\n"
"	background-color: white;\n"
"    border: 1px solid #241f18;\n"
" \n"
"	border-color: rgb(36, 31, 24);\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgApp.sizePolicy().hasHeightForWidth())
        self.bgApp.setSizePolicy(sizePolicy1)
        self.bgApp.setMinimumSize(QSize(0, 0))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.bgApp.setLineWidth(0)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy2)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy2.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy2)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy2.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy2)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"background-color: rgb(255, 255, 255);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        self.home.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.verticalLayout_34 = QVBoxLayout(self.home)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.widget_8 = QWidget(self.home)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_19 = QVBoxLayout(self.widget_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.verticalLayout_22 = QVBoxLayout(self.widget_9)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"\n"
"font: 700 22pt \"Times New Roman\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_6)

        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_2)


        self.verticalLayout_19.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.verticalLayout_25 = QVBoxLayout(self.widget_10)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.lisTram_1 = QWidget(self.widget_10)
        self.lisTram_1.setObjectName(u"lisTram_1")
        sizePolicy.setHeightForWidth(self.lisTram_1.sizePolicy().hasHeightForWidth())
        self.lisTram_1.setSizePolicy(sizePolicy)
        self.lisTram_1.setStyleSheet(u"border-right-color: rgb(0, 0, 0);")
        self.horizontalLayout_6 = QHBoxLayout(self.lisTram_1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 30, 20)
        self.widget_17 = QWidget(self.lisTram_1)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy)
        self.widget_17.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_41 = QVBoxLayout(self.widget_17)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_46 = QWidget(self.widget_17)
        self.widget_46.setObjectName(u"widget_46")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_46.sizePolicy().hasHeightForWidth())
        self.widget_46.setSizePolicy(sizePolicy3)
        self.widget_46.setLayoutDirection(Qt.LeftToRight)
        self.widget_46.setStyleSheet(u"font: 700 16pt \"Times New Roman\";\n"
"padding:0\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_46)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_16)

        self.pushButton_anhsang_9 = QPushButton(self.widget_46)
        self.pushButton_anhsang_9.setObjectName(u"pushButton_anhsang_9")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_9.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_9.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_9.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_9.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_9.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_9.setIconSize(QSize(16, 16))

        self.horizontalLayout_19.addWidget(self.pushButton_anhsang_9)


        self.verticalLayout_41.addWidget(self.widget_46)

        self.widget_47 = QWidget(self.widget_17)
        self.widget_47.setObjectName(u"widget_47")
        sizePolicy3.setHeightForWidth(self.widget_47.sizePolicy().hasHeightForWidth())
        self.widget_47.setSizePolicy(sizePolicy3)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_48 = QWidget(self.widget_47)
        self.widget_48.setObjectName(u"widget_48")
        sizePolicy3.setHeightForWidth(self.widget_48.sizePolicy().hasHeightForWidth())
        self.widget_48.setSizePolicy(sizePolicy3)
        self.verticalLayout_27 = QVBoxLayout(self.widget_48)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 30, 0)
        self.widget_57 = QWidget(self.widget_48)
        self.widget_57.setObjectName(u"widget_57")
        sizePolicy.setHeightForWidth(self.widget_57.sizePolicy().hasHeightForWidth())
        self.widget_57.setSizePolicy(sizePolicy)
        self.verticalLayout_17 = QVBoxLayout(self.widget_57)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 20)
        self.label_8 = QLabel(self.widget_57)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")
        self.label_8.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.label_8)


        self.verticalLayout_27.addWidget(self.widget_57)

        self.widget_58 = QWidget(self.widget_48)
        self.widget_58.setObjectName(u"widget_58")
        sizePolicy3.setHeightForWidth(self.widget_58.sizePolicy().hasHeightForWidth())
        self.widget_58.setSizePolicy(sizePolicy3)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_59 = QWidget(self.widget_58)
        self.widget_59.setObjectName(u"widget_59")
        self.verticalLayout_45 = QVBoxLayout(self.widget_59)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.widget_60 = QWidget(self.widget_59)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1 = QPushButton(self.widget_60)
        self.pushButton_ac1.setObjectName(u"pushButton_ac1")
        sizePolicy4.setHeightForWidth(self.pushButton_ac1.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1.setSizePolicy(sizePolicy4)
        self.pushButton_ac1.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_23.addWidget(self.pushButton_ac1)


        self.verticalLayout_45.addWidget(self.widget_60)

        self.widget_72 = QWidget(self.widget_59)
        self.widget_72.setObjectName(u"widget_72")
        self.verticalLayout_46 = QVBoxLayout(self.widget_72)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_72)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.label_19)


        self.verticalLayout_45.addWidget(self.widget_72)


        self.horizontalLayout_16.addWidget(self.widget_59)

        self.widget_73 = QWidget(self.widget_58)
        self.widget_73.setObjectName(u"widget_73")
        self.verticalLayout_47 = QVBoxLayout(self.widget_73)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_74 = QWidget(self.widget_73)
        self.widget_74.setObjectName(u"widget_74")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_74)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2 = QPushButton(self.widget_74)
        self.pushButton_ac2.setObjectName(u"pushButton_ac2")
        sizePolicy4.setHeightForWidth(self.pushButton_ac2.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2.setSizePolicy(sizePolicy4)
        self.pushButton_ac2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_25.addWidget(self.pushButton_ac2)


        self.verticalLayout_47.addWidget(self.widget_74)

        self.widget_76 = QWidget(self.widget_73)
        self.widget_76.setObjectName(u"widget_76")
        self.verticalLayout_48 = QVBoxLayout(self.widget_76)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget_76)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.label_20)


        self.verticalLayout_47.addWidget(self.widget_76)


        self.horizontalLayout_16.addWidget(self.widget_73)


        self.verticalLayout_27.addWidget(self.widget_58)


        self.horizontalLayout_8.addWidget(self.widget_48)

        self.widget_124 = QWidget(self.widget_47)
        self.widget_124.setObjectName(u"widget_124")
        sizePolicy.setHeightForWidth(self.widget_124.sizePolicy().hasHeightForWidth())
        self.widget_124.setSizePolicy(sizePolicy)
        self.widget_124.setMinimumSize(QSize(220, 0))
        self.widget_124.setStyleSheet(u"padding-right:40px\n"
";")
        self.verticalLayout_4 = QVBoxLayout(self.widget_124)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_125 = QWidget(self.widget_124)
        self.widget_125.setObjectName(u"widget_125")
        sizePolicy3.setHeightForWidth(self.widget_125.sizePolicy().hasHeightForWidth())
        self.widget_125.setSizePolicy(sizePolicy3)
        self.widget_125.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_125)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(self.widget_125)
        self.widget_49.setObjectName(u"widget_49")
        sizePolicy4.setHeightForWidth(self.widget_49.sizePolicy().hasHeightForWidth())
        self.widget_49.setSizePolicy(sizePolicy4)
        self.widget_49.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo = QPushButton(self.widget_49)
        self.pushButton_nhietdo.setObjectName(u"pushButton_nhietdo")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo.setIconSize(QSize(16, 16))

        self.horizontalLayout_11.addWidget(self.pushButton_nhietdo)


        self.horizontalLayout_10.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.widget_125)
        self.widget_50.setObjectName(u"widget_50")
        self.verticalLayout_29 = QVBoxLayout(self.widget_50)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_3 = QLabel(self.widget_50)
        self.label_nhietdo_3.setObjectName(u"label_nhietdo_3")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_3.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_3.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_nhietdo_3.setFont(font1)
        self.label_nhietdo_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_29.addWidget(self.label_nhietdo_3)


        self.horizontalLayout_10.addWidget(self.widget_50)


        self.verticalLayout_4.addWidget(self.widget_125)

        self.widget_126 = QWidget(self.widget_124)
        self.widget_126.setObjectName(u"widget_126")
        sizePolicy3.setHeightForWidth(self.widget_126.sizePolicy().hasHeightForWidth())
        self.widget_126.setSizePolicy(sizePolicy3)
        self.horizontalLayout_29 = QHBoxLayout(self.widget_126)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_130 = QWidget(self.widget_126)
        self.widget_130.setObjectName(u"widget_130")
        sizePolicy3.setHeightForWidth(self.widget_130.sizePolicy().hasHeightForWidth())
        self.widget_130.setSizePolicy(sizePolicy3)
        self.widget_130.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_130)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_51 = QWidget(self.widget_130)
        self.widget_51.setObjectName(u"widget_51")
        sizePolicy4.setHeightForWidth(self.widget_51.sizePolicy().hasHeightForWidth())
        self.widget_51.setSizePolicy(sizePolicy4)
        self.widget_51.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton_doam = QPushButton(self.widget_51)
        self.pushButton_doam.setObjectName(u"pushButton_doam")
        sizePolicy1.setHeightForWidth(self.pushButton_doam.sizePolicy().hasHeightForWidth())
        self.pushButton_doam.setSizePolicy(sizePolicy1)
        self.pushButton_doam.setMinimumSize(QSize(50, 28))
        self.pushButton_doam.setMaximumSize(QSize(50, 28))
        self.pushButton_doam.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_doam.setIconSize(QSize(16, 16))

        self.horizontalLayout_13.addWidget(self.pushButton_doam)


        self.horizontalLayout_12.addWidget(self.widget_51)

        self.widget_55 = QWidget(self.widget_130)
        self.widget_55.setObjectName(u"widget_55")
        self.verticalLayout_37 = QVBoxLayout(self.widget_55)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_doam_2 = QLabel(self.widget_55)
        self.label_doam_2.setObjectName(u"label_doam_2")
        sizePolicy3.setHeightForWidth(self.label_doam_2.sizePolicy().hasHeightForWidth())
        self.label_doam_2.setSizePolicy(sizePolicy3)
        self.label_doam_2.setFont(font1)
        self.label_doam_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_37.addWidget(self.label_doam_2)


        self.horizontalLayout_12.addWidget(self.widget_55)


        self.horizontalLayout_29.addWidget(self.widget_130)


        self.verticalLayout_4.addWidget(self.widget_126)

        self.widget_128 = QWidget(self.widget_124)
        self.widget_128.setObjectName(u"widget_128")
        sizePolicy3.setHeightForWidth(self.widget_128.sizePolicy().hasHeightForWidth())
        self.widget_128.setSizePolicy(sizePolicy3)
        self.horizontalLayout_34 = QHBoxLayout(self.widget_128)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_132 = QWidget(self.widget_128)
        self.widget_132.setObjectName(u"widget_132")
        sizePolicy3.setHeightForWidth(self.widget_132.sizePolicy().hasHeightForWidth())
        self.widget_132.setSizePolicy(sizePolicy3)
        self.widget_132.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_132)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_56 = QWidget(self.widget_132)
        self.widget_56.setObjectName(u"widget_56")
        sizePolicy4.setHeightForWidth(self.widget_56.sizePolicy().hasHeightForWidth())
        self.widget_56.setSizePolicy(sizePolicy4)
        self.widget_56.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_30 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc1 = QPushButton(self.widget_56)
        self.pushButton_dc1.setObjectName(u"pushButton_dc1")
        sizePolicy1.setHeightForWidth(self.pushButton_dc1.sizePolicy().hasHeightForWidth())
        self.pushButton_dc1.setSizePolicy(sizePolicy1)
        self.pushButton_dc1.setMinimumSize(QSize(50, 28))
        self.pushButton_dc1.setMaximumSize(QSize(50, 28))
        self.pushButton_dc1.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_dc1.setIconSize(QSize(16, 16))

        self.horizontalLayout_30.addWidget(self.pushButton_dc1)


        self.horizontalLayout_21.addWidget(self.widget_56)

        self.widget_65 = QWidget(self.widget_132)
        self.widget_65.setObjectName(u"widget_65")
        self.verticalLayout_50 = QVBoxLayout(self.widget_65)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_dc1 = QLabel(self.widget_65)
        self.label_dc1.setObjectName(u"label_dc1")
        sizePolicy3.setHeightForWidth(self.label_dc1.sizePolicy().hasHeightForWidth())
        self.label_dc1.setSizePolicy(sizePolicy3)
        self.label_dc1.setFont(font1)
        self.label_dc1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_50.addWidget(self.label_dc1)


        self.horizontalLayout_21.addWidget(self.widget_65)


        self.horizontalLayout_34.addWidget(self.widget_132)


        self.verticalLayout_4.addWidget(self.widget_128)

        self.widget_129 = QWidget(self.widget_124)
        self.widget_129.setObjectName(u"widget_129")
        sizePolicy4.setHeightForWidth(self.widget_129.sizePolicy().hasHeightForWidth())
        self.widget_129.setSizePolicy(sizePolicy4)
        self.horizontalLayout_35 = QHBoxLayout(self.widget_129)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_133 = QWidget(self.widget_129)
        self.widget_133.setObjectName(u"widget_133")
        sizePolicy3.setHeightForWidth(self.widget_133.sizePolicy().hasHeightForWidth())
        self.widget_133.setSizePolicy(sizePolicy3)
        self.widget_133.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_31 = QHBoxLayout(self.widget_133)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_66 = QWidget(self.widget_133)
        self.widget_66.setObjectName(u"widget_66")
        sizePolicy4.setHeightForWidth(self.widget_66.sizePolicy().hasHeightForWidth())
        self.widget_66.setSizePolicy(sizePolicy4)
        self.widget_66.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc2 = QPushButton(self.widget_66)
        self.pushButton_dc2.setObjectName(u"pushButton_dc2")
        sizePolicy1.setHeightForWidth(self.pushButton_dc2.sizePolicy().hasHeightForWidth())
        self.pushButton_dc2.setSizePolicy(sizePolicy1)
        self.pushButton_dc2.setMinimumSize(QSize(50, 28))
        self.pushButton_dc2.setMaximumSize(QSize(50, 28))
        self.pushButton_dc2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_dc2.setIconSize(QSize(16, 16))

        self.horizontalLayout_32.addWidget(self.pushButton_dc2)


        self.horizontalLayout_31.addWidget(self.widget_66)

        self.widget_67 = QWidget(self.widget_133)
        self.widget_67.setObjectName(u"widget_67")
        self.verticalLayout_53 = QVBoxLayout(self.widget_67)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_dc2 = QLabel(self.widget_67)
        self.label_dc2.setObjectName(u"label_dc2")
        sizePolicy3.setHeightForWidth(self.label_dc2.sizePolicy().hasHeightForWidth())
        self.label_dc2.setSizePolicy(sizePolicy3)
        self.label_dc2.setFont(font1)
        self.label_dc2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_53.addWidget(self.label_dc2)


        self.horizontalLayout_31.addWidget(self.widget_67)


        self.horizontalLayout_35.addWidget(self.widget_133)


        self.verticalLayout_4.addWidget(self.widget_129)

        self.widget_127 = QWidget(self.widget_124)
        self.widget_127.setObjectName(u"widget_127")
        sizePolicy3.setHeightForWidth(self.widget_127.sizePolicy().hasHeightForWidth())
        self.widget_127.setSizePolicy(sizePolicy3)
        self.widget_127.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_127)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.widget_131 = QWidget(self.widget_127)
        self.widget_131.setObjectName(u"widget_131")
        sizePolicy3.setHeightForWidth(self.widget_131.sizePolicy().hasHeightForWidth())
        self.widget_131.setSizePolicy(sizePolicy3)
        self.widget_131.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_131)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_68 = QWidget(self.widget_131)
        self.widget_68.setObjectName(u"widget_68")
        sizePolicy4.setHeightForWidth(self.widget_68.sizePolicy().hasHeightForWidth())
        self.widget_68.setSizePolicy(sizePolicy4)
        self.widget_68.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pushButton_anhsang = QPushButton(self.widget_68)
        self.pushButton_anhsang.setObjectName(u"pushButton_anhsang")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang.setIconSize(QSize(16, 16))

        self.horizontalLayout_18.addWidget(self.pushButton_anhsang)


        self.horizontalLayout_17.addWidget(self.widget_68)

        self.widget_69 = QWidget(self.widget_131)
        self.widget_69.setObjectName(u"widget_69")
        self.verticalLayout_49 = QVBoxLayout(self.widget_69)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_anhsang = QLabel(self.widget_69)
        self.label_anhsang.setObjectName(u"label_anhsang")
        sizePolicy3.setHeightForWidth(self.label_anhsang.sizePolicy().hasHeightForWidth())
        self.label_anhsang.setSizePolicy(sizePolicy3)
        self.label_anhsang.setFont(font1)
        self.label_anhsang.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_49.addWidget(self.label_anhsang)


        self.horizontalLayout_17.addWidget(self.widget_69)


        self.horizontalLayout_33.addWidget(self.widget_131)


        self.verticalLayout_4.addWidget(self.widget_127)


        self.horizontalLayout_8.addWidget(self.widget_124)


        self.verticalLayout_41.addWidget(self.widget_47)


        self.horizontalLayout_6.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.lisTram_1)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy)
        self.widget_16.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_89 = QVBoxLayout(self.widget_16)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.widget_35 = QWidget(self.widget_16)
        self.widget_35.setObjectName(u"widget_35")
        sizePolicy3.setHeightForWidth(self.widget_35.sizePolicy().hasHeightForWidth())
        self.widget_35.setSizePolicy(sizePolicy3)
        self.verticalLayout_42 = QVBoxLayout(self.widget_35)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_70 = QWidget(self.widget_35)
        self.widget_70.setObjectName(u"widget_70")
        sizePolicy3.setHeightForWidth(self.widget_70.sizePolicy().hasHeightForWidth())
        self.widget_70.setSizePolicy(sizePolicy3)
        self.widget_70.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget_70)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_22.addWidget(self.label_18)

        self.pushButton_anhsang_10 = QPushButton(self.widget_70)
        self.pushButton_anhsang_10.setObjectName(u"pushButton_anhsang_10")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_10.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_10.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_10.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_10.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_10.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_10.setIconSize(QSize(16, 16))

        self.horizontalLayout_22.addWidget(self.pushButton_anhsang_10)


        self.verticalLayout_42.addWidget(self.widget_70)

        self.widget_71 = QWidget(self.widget_35)
        self.widget_71.setObjectName(u"widget_71")
        sizePolicy3.setHeightForWidth(self.widget_71.sizePolicy().hasHeightForWidth())
        self.widget_71.setSizePolicy(sizePolicy3)
        self.horizontalLayout_36 = QHBoxLayout(self.widget_71)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_75 = QWidget(self.widget_71)
        self.widget_75.setObjectName(u"widget_75")
        sizePolicy3.setHeightForWidth(self.widget_75.sizePolicy().hasHeightForWidth())
        self.widget_75.setSizePolicy(sizePolicy3)
        self.widget_75.setMinimumSize(QSize(0, 0))
        self.verticalLayout_35 = QVBoxLayout(self.widget_75)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 30, 0)
        self.widget_77 = QWidget(self.widget_75)
        self.widget_77.setObjectName(u"widget_77")
        sizePolicy.setHeightForWidth(self.widget_77.sizePolicy().hasHeightForWidth())
        self.widget_77.setSizePolicy(sizePolicy)
        self.verticalLayout_38 = QVBoxLayout(self.widget_77)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 20)
        self.label_10 = QLabel(self.widget_77)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setStyleSheet(u"")
        self.label_10.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_10.setScaledContents(True)

        self.verticalLayout_38.addWidget(self.label_10)


        self.verticalLayout_35.addWidget(self.widget_77)

        self.widget_79 = QWidget(self.widget_75)
        self.widget_79.setObjectName(u"widget_79")
        sizePolicy3.setHeightForWidth(self.widget_79.sizePolicy().hasHeightForWidth())
        self.widget_79.setSizePolicy(sizePolicy3)
        self.horizontalLayout_37 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_80 = QWidget(self.widget_79)
        self.widget_80.setObjectName(u"widget_80")
        self.verticalLayout_54 = QVBoxLayout(self.widget_80)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.widget_81 = QWidget(self.widget_80)
        self.widget_81.setObjectName(u"widget_81")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_81)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_2 = QPushButton(self.widget_81)
        self.pushButton_ac1_2.setObjectName(u"pushButton_ac1_2")
        sizePolicy4.setHeightForWidth(self.pushButton_ac1_2.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_2.setSizePolicy(sizePolicy4)
        self.pushButton_ac1_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_38.addWidget(self.pushButton_ac1_2)


        self.verticalLayout_54.addWidget(self.widget_81)

        self.widget_82 = QWidget(self.widget_80)
        self.widget_82.setObjectName(u"widget_82")
        self.verticalLayout_55 = QVBoxLayout(self.widget_82)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget_82)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_55.addWidget(self.label_21)


        self.verticalLayout_54.addWidget(self.widget_82)


        self.horizontalLayout_37.addWidget(self.widget_80)

        self.widget_83 = QWidget(self.widget_79)
        self.widget_83.setObjectName(u"widget_83")
        self.verticalLayout_56 = QVBoxLayout(self.widget_83)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.widget_84 = QWidget(self.widget_83)
        self.widget_84.setObjectName(u"widget_84")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_84)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_2 = QPushButton(self.widget_84)
        self.pushButton_ac2_2.setObjectName(u"pushButton_ac2_2")
        sizePolicy4.setHeightForWidth(self.pushButton_ac2_2.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_2.setSizePolicy(sizePolicy4)
        self.pushButton_ac2_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_39.addWidget(self.pushButton_ac2_2)


        self.verticalLayout_56.addWidget(self.widget_84)

        self.widget_85 = QWidget(self.widget_83)
        self.widget_85.setObjectName(u"widget_85")
        self.verticalLayout_57 = QVBoxLayout(self.widget_85)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.widget_85)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.label_28)


        self.verticalLayout_56.addWidget(self.widget_85)


        self.horizontalLayout_37.addWidget(self.widget_83)


        self.verticalLayout_35.addWidget(self.widget_79)


        self.horizontalLayout_36.addWidget(self.widget_75)

        self.widget_134 = QWidget(self.widget_71)
        self.widget_134.setObjectName(u"widget_134")
        sizePolicy.setHeightForWidth(self.widget_134.sizePolicy().hasHeightForWidth())
        self.widget_134.setSizePolicy(sizePolicy)
        self.widget_134.setMinimumSize(QSize(220, 0))
        self.widget_134.setStyleSheet(u"padding-right:30px;")
        self.verticalLayout_16 = QVBoxLayout(self.widget_134)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_135 = QWidget(self.widget_134)
        self.widget_135.setObjectName(u"widget_135")
        sizePolicy3.setHeightForWidth(self.widget_135.sizePolicy().hasHeightForWidth())
        self.widget_135.setSizePolicy(sizePolicy3)
        self.widget_135.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_40 = QHBoxLayout(self.widget_135)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.widget_86 = QWidget(self.widget_135)
        self.widget_86.setObjectName(u"widget_86")
        sizePolicy4.setHeightForWidth(self.widget_86.sizePolicy().hasHeightForWidth())
        self.widget_86.setSizePolicy(sizePolicy4)
        self.widget_86.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_41 = QHBoxLayout(self.widget_86)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_3 = QPushButton(self.widget_86)
        self.pushButton_nhietdo_3.setObjectName(u"pushButton_nhietdo_3")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_3.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_3.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_3.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_3.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_3.setIconSize(QSize(16, 16))

        self.horizontalLayout_41.addWidget(self.pushButton_nhietdo_3)


        self.horizontalLayout_40.addWidget(self.widget_86)

        self.widget_87 = QWidget(self.widget_135)
        self.widget_87.setObjectName(u"widget_87")
        self.verticalLayout_39 = QVBoxLayout(self.widget_87)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_8 = QLabel(self.widget_87)
        self.label_nhietdo_8.setObjectName(u"label_nhietdo_8")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_8.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_8.setSizePolicy(sizePolicy3)
        self.label_nhietdo_8.setFont(font1)
        self.label_nhietdo_8.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_39.addWidget(self.label_nhietdo_8)


        self.horizontalLayout_40.addWidget(self.widget_87)


        self.verticalLayout_16.addWidget(self.widget_135)

        self.widget_136 = QWidget(self.widget_134)
        self.widget_136.setObjectName(u"widget_136")
        sizePolicy3.setHeightForWidth(self.widget_136.sizePolicy().hasHeightForWidth())
        self.widget_136.setSizePolicy(sizePolicy3)
        self.horizontalLayout_42 = QHBoxLayout(self.widget_136)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_137 = QWidget(self.widget_136)
        self.widget_137.setObjectName(u"widget_137")
        sizePolicy3.setHeightForWidth(self.widget_137.sizePolicy().hasHeightForWidth())
        self.widget_137.setSizePolicy(sizePolicy3)
        self.widget_137.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_43 = QHBoxLayout(self.widget_137)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_88 = QWidget(self.widget_137)
        self.widget_88.setObjectName(u"widget_88")
        sizePolicy4.setHeightForWidth(self.widget_88.sizePolicy().hasHeightForWidth())
        self.widget_88.setSizePolicy(sizePolicy4)
        self.widget_88.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_44 = QHBoxLayout(self.widget_88)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.pushButton_doam_2 = QPushButton(self.widget_88)
        self.pushButton_doam_2.setObjectName(u"pushButton_doam_2")
        sizePolicy1.setHeightForWidth(self.pushButton_doam_2.sizePolicy().hasHeightForWidth())
        self.pushButton_doam_2.setSizePolicy(sizePolicy1)
        self.pushButton_doam_2.setMinimumSize(QSize(50, 28))
        self.pushButton_doam_2.setMaximumSize(QSize(50, 28))
        self.pushButton_doam_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_doam_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_44.addWidget(self.pushButton_doam_2)


        self.horizontalLayout_43.addWidget(self.widget_88)

        self.widget_89 = QWidget(self.widget_137)
        self.widget_89.setObjectName(u"widget_89")
        self.verticalLayout_40 = QVBoxLayout(self.widget_89)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_doam_3 = QLabel(self.widget_89)
        self.label_doam_3.setObjectName(u"label_doam_3")
        sizePolicy3.setHeightForWidth(self.label_doam_3.sizePolicy().hasHeightForWidth())
        self.label_doam_3.setSizePolicy(sizePolicy3)
        self.label_doam_3.setFont(font1)
        self.label_doam_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_40.addWidget(self.label_doam_3)


        self.horizontalLayout_43.addWidget(self.widget_89)


        self.horizontalLayout_42.addWidget(self.widget_137)


        self.verticalLayout_16.addWidget(self.widget_136)

        self.widget_138 = QWidget(self.widget_134)
        self.widget_138.setObjectName(u"widget_138")
        sizePolicy3.setHeightForWidth(self.widget_138.sizePolicy().hasHeightForWidth())
        self.widget_138.setSizePolicy(sizePolicy3)
        self.horizontalLayout_45 = QHBoxLayout(self.widget_138)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.widget_139 = QWidget(self.widget_138)
        self.widget_139.setObjectName(u"widget_139")
        sizePolicy3.setHeightForWidth(self.widget_139.sizePolicy().hasHeightForWidth())
        self.widget_139.setSizePolicy(sizePolicy3)
        self.widget_139.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_46 = QHBoxLayout(self.widget_139)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.widget_90 = QWidget(self.widget_139)
        self.widget_90.setObjectName(u"widget_90")
        sizePolicy4.setHeightForWidth(self.widget_90.sizePolicy().hasHeightForWidth())
        self.widget_90.setSizePolicy(sizePolicy4)
        self.widget_90.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_47 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc1_2 = QPushButton(self.widget_90)
        self.pushButton_dc1_2.setObjectName(u"pushButton_dc1_2")
        sizePolicy1.setHeightForWidth(self.pushButton_dc1_2.sizePolicy().hasHeightForWidth())
        self.pushButton_dc1_2.setSizePolicy(sizePolicy1)
        self.pushButton_dc1_2.setMinimumSize(QSize(50, 28))
        self.pushButton_dc1_2.setMaximumSize(QSize(50, 28))
        self.pushButton_dc1_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_dc1_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_47.addWidget(self.pushButton_dc1_2)


        self.horizontalLayout_46.addWidget(self.widget_90)

        self.widget_91 = QWidget(self.widget_139)
        self.widget_91.setObjectName(u"widget_91")
        self.verticalLayout_58 = QVBoxLayout(self.widget_91)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_dc1_2 = QLabel(self.widget_91)
        self.label_dc1_2.setObjectName(u"label_dc1_2")
        sizePolicy3.setHeightForWidth(self.label_dc1_2.sizePolicy().hasHeightForWidth())
        self.label_dc1_2.setSizePolicy(sizePolicy3)
        self.label_dc1_2.setFont(font1)
        self.label_dc1_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_58.addWidget(self.label_dc1_2)


        self.horizontalLayout_46.addWidget(self.widget_91)


        self.horizontalLayout_45.addWidget(self.widget_139)


        self.verticalLayout_16.addWidget(self.widget_138)

        self.widget_140 = QWidget(self.widget_134)
        self.widget_140.setObjectName(u"widget_140")
        sizePolicy4.setHeightForWidth(self.widget_140.sizePolicy().hasHeightForWidth())
        self.widget_140.setSizePolicy(sizePolicy4)
        self.horizontalLayout_48 = QHBoxLayout(self.widget_140)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.widget_141 = QWidget(self.widget_140)
        self.widget_141.setObjectName(u"widget_141")
        sizePolicy3.setHeightForWidth(self.widget_141.sizePolicy().hasHeightForWidth())
        self.widget_141.setSizePolicy(sizePolicy3)
        self.widget_141.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_49 = QHBoxLayout(self.widget_141)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.widget_92 = QWidget(self.widget_141)
        self.widget_92.setObjectName(u"widget_92")
        sizePolicy4.setHeightForWidth(self.widget_92.sizePolicy().hasHeightForWidth())
        self.widget_92.setSizePolicy(sizePolicy4)
        self.widget_92.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_50 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc2_2 = QPushButton(self.widget_92)
        self.pushButton_dc2_2.setObjectName(u"pushButton_dc2_2")
        sizePolicy1.setHeightForWidth(self.pushButton_dc2_2.sizePolicy().hasHeightForWidth())
        self.pushButton_dc2_2.setSizePolicy(sizePolicy1)
        self.pushButton_dc2_2.setMinimumSize(QSize(50, 28))
        self.pushButton_dc2_2.setMaximumSize(QSize(50, 28))
        self.pushButton_dc2_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_dc2_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_50.addWidget(self.pushButton_dc2_2)


        self.horizontalLayout_49.addWidget(self.widget_92)

        self.widget_93 = QWidget(self.widget_141)
        self.widget_93.setObjectName(u"widget_93")
        self.verticalLayout_59 = QVBoxLayout(self.widget_93)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_dc2_2 = QLabel(self.widget_93)
        self.label_dc2_2.setObjectName(u"label_dc2_2")
        sizePolicy3.setHeightForWidth(self.label_dc2_2.sizePolicy().hasHeightForWidth())
        self.label_dc2_2.setSizePolicy(sizePolicy3)
        self.label_dc2_2.setFont(font1)
        self.label_dc2_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_59.addWidget(self.label_dc2_2)


        self.horizontalLayout_49.addWidget(self.widget_93)


        self.horizontalLayout_48.addWidget(self.widget_141)


        self.verticalLayout_16.addWidget(self.widget_140)

        self.widget_142 = QWidget(self.widget_134)
        self.widget_142.setObjectName(u"widget_142")
        sizePolicy3.setHeightForWidth(self.widget_142.sizePolicy().hasHeightForWidth())
        self.widget_142.setSizePolicy(sizePolicy3)
        self.widget_142.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_51 = QHBoxLayout(self.widget_142)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.widget_143 = QWidget(self.widget_142)
        self.widget_143.setObjectName(u"widget_143")
        sizePolicy3.setHeightForWidth(self.widget_143.sizePolicy().hasHeightForWidth())
        self.widget_143.setSizePolicy(sizePolicy3)
        self.widget_143.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_52 = QHBoxLayout(self.widget_143)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.widget_94 = QWidget(self.widget_143)
        self.widget_94.setObjectName(u"widget_94")
        sizePolicy4.setHeightForWidth(self.widget_94.sizePolicy().hasHeightForWidth())
        self.widget_94.setSizePolicy(sizePolicy4)
        self.widget_94.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_53 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.pushButton_anhsang_2 = QPushButton(self.widget_94)
        self.pushButton_anhsang_2.setObjectName(u"pushButton_anhsang_2")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_2.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_2.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_2.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_2.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_53.addWidget(self.pushButton_anhsang_2)


        self.horizontalLayout_52.addWidget(self.widget_94)

        self.widget_95 = QWidget(self.widget_143)
        self.widget_95.setObjectName(u"widget_95")
        self.verticalLayout_60 = QVBoxLayout(self.widget_95)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_anhsang_2 = QLabel(self.widget_95)
        self.label_anhsang_2.setObjectName(u"label_anhsang_2")
        sizePolicy3.setHeightForWidth(self.label_anhsang_2.sizePolicy().hasHeightForWidth())
        self.label_anhsang_2.setSizePolicy(sizePolicy3)
        self.label_anhsang_2.setFont(font1)
        self.label_anhsang_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_60.addWidget(self.label_anhsang_2)


        self.horizontalLayout_52.addWidget(self.widget_95)


        self.horizontalLayout_51.addWidget(self.widget_143)


        self.verticalLayout_16.addWidget(self.widget_142)


        self.horizontalLayout_36.addWidget(self.widget_134)


        self.verticalLayout_42.addWidget(self.widget_71)


        self.verticalLayout_89.addWidget(self.widget_35)


        self.horizontalLayout_6.addWidget(self.widget_16)

        self.widget_96 = QWidget(self.lisTram_1)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_84 = QVBoxLayout(self.widget_96)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.widget_36 = QWidget(self.widget_96)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy3.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy3)
        self.verticalLayout_43 = QVBoxLayout(self.widget_36)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_97 = QWidget(self.widget_36)
        self.widget_97.setObjectName(u"widget_97")
        sizePolicy3.setHeightForWidth(self.widget_97.sizePolicy().hasHeightForWidth())
        self.widget_97.setSizePolicy(sizePolicy3)
        self.widget_97.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_97)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_97)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)
        self.label_22.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_54.addWidget(self.label_22)

        self.pushButton_anhsang_11 = QPushButton(self.widget_97)
        self.pushButton_anhsang_11.setObjectName(u"pushButton_anhsang_11")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_11.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_11.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_11.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_11.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_11.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_11.setIconSize(QSize(16, 16))

        self.horizontalLayout_54.addWidget(self.pushButton_anhsang_11)


        self.verticalLayout_43.addWidget(self.widget_97)

        self.widget_98 = QWidget(self.widget_36)
        self.widget_98.setObjectName(u"widget_98")
        sizePolicy3.setHeightForWidth(self.widget_98.sizePolicy().hasHeightForWidth())
        self.widget_98.setSizePolicy(sizePolicy3)
        self.horizontalLayout_55 = QHBoxLayout(self.widget_98)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.widget_99 = QWidget(self.widget_98)
        self.widget_99.setObjectName(u"widget_99")
        sizePolicy3.setHeightForWidth(self.widget_99.sizePolicy().hasHeightForWidth())
        self.widget_99.setSizePolicy(sizePolicy3)
        self.verticalLayout_44 = QVBoxLayout(self.widget_99)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 30, 0)
        self.widget_100 = QWidget(self.widget_99)
        self.widget_100.setObjectName(u"widget_100")
        sizePolicy.setHeightForWidth(self.widget_100.sizePolicy().hasHeightForWidth())
        self.widget_100.setSizePolicy(sizePolicy)
        self.verticalLayout_51 = QVBoxLayout(self.widget_100)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 20)
        self.label_12 = QLabel(self.widget_100)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"")
        self.label_12.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_12.setScaledContents(True)

        self.verticalLayout_51.addWidget(self.label_12)


        self.verticalLayout_44.addWidget(self.widget_100)

        self.widget_101 = QWidget(self.widget_99)
        self.widget_101.setObjectName(u"widget_101")
        sizePolicy3.setHeightForWidth(self.widget_101.sizePolicy().hasHeightForWidth())
        self.widget_101.setSizePolicy(sizePolicy3)
        self.horizontalLayout_56 = QHBoxLayout(self.widget_101)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.widget_102 = QWidget(self.widget_101)
        self.widget_102.setObjectName(u"widget_102")
        self.verticalLayout_61 = QVBoxLayout(self.widget_102)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.widget_103 = QWidget(self.widget_102)
        self.widget_103.setObjectName(u"widget_103")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_103)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_3 = QPushButton(self.widget_103)
        self.pushButton_ac1_3.setObjectName(u"pushButton_ac1_3")
        sizePolicy4.setHeightForWidth(self.pushButton_ac1_3.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_3.setSizePolicy(sizePolicy4)
        self.pushButton_ac1_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_57.addWidget(self.pushButton_ac1_3)


        self.verticalLayout_61.addWidget(self.widget_103)

        self.widget_104 = QWidget(self.widget_102)
        self.widget_104.setObjectName(u"widget_104")
        self.verticalLayout_62 = QVBoxLayout(self.widget_104)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.widget_104)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.label_29)


        self.verticalLayout_61.addWidget(self.widget_104)


        self.horizontalLayout_56.addWidget(self.widget_102)

        self.widget_105 = QWidget(self.widget_101)
        self.widget_105.setObjectName(u"widget_105")
        self.verticalLayout_63 = QVBoxLayout(self.widget_105)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.widget_106 = QWidget(self.widget_105)
        self.widget_106.setObjectName(u"widget_106")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_106)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_3 = QPushButton(self.widget_106)
        self.pushButton_ac2_3.setObjectName(u"pushButton_ac2_3")
        sizePolicy4.setHeightForWidth(self.pushButton_ac2_3.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_3.setSizePolicy(sizePolicy4)
        self.pushButton_ac2_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_58.addWidget(self.pushButton_ac2_3)


        self.verticalLayout_63.addWidget(self.widget_106)

        self.widget_107 = QWidget(self.widget_105)
        self.widget_107.setObjectName(u"widget_107")
        self.verticalLayout_64 = QVBoxLayout(self.widget_107)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.widget_107)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_30)


        self.verticalLayout_63.addWidget(self.widget_107)


        self.horizontalLayout_56.addWidget(self.widget_105)


        self.verticalLayout_44.addWidget(self.widget_101)


        self.horizontalLayout_55.addWidget(self.widget_99)

        self.widget_153 = QWidget(self.widget_98)
        self.widget_153.setObjectName(u"widget_153")
        sizePolicy.setHeightForWidth(self.widget_153.sizePolicy().hasHeightForWidth())
        self.widget_153.setSizePolicy(sizePolicy)
        self.widget_153.setMinimumSize(QSize(220, 0))
        self.widget_153.setStyleSheet(u"padding-right:30px;")
        self.verticalLayout_71 = QVBoxLayout(self.widget_153)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.widget_154 = QWidget(self.widget_153)
        self.widget_154.setObjectName(u"widget_154")
        sizePolicy3.setHeightForWidth(self.widget_154.sizePolicy().hasHeightForWidth())
        self.widget_154.setSizePolicy(sizePolicy3)
        self.widget_154.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_59 = QHBoxLayout(self.widget_154)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.widget_108 = QWidget(self.widget_154)
        self.widget_108.setObjectName(u"widget_108")
        sizePolicy4.setHeightForWidth(self.widget_108.sizePolicy().hasHeightForWidth())
        self.widget_108.setSizePolicy(sizePolicy4)
        self.widget_108.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_65 = QHBoxLayout(self.widget_108)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_14 = QPushButton(self.widget_108)
        self.pushButton_nhietdo_14.setObjectName(u"pushButton_nhietdo_14")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_14.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_14.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_14.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_14.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_14.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_14.setIconSize(QSize(16, 16))

        self.horizontalLayout_65.addWidget(self.pushButton_nhietdo_14)


        self.horizontalLayout_59.addWidget(self.widget_108)

        self.widget_109 = QWidget(self.widget_154)
        self.widget_109.setObjectName(u"widget_109")
        self.verticalLayout_72 = QVBoxLayout(self.widget_109)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_16 = QLabel(self.widget_109)
        self.label_nhietdo_16.setObjectName(u"label_nhietdo_16")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_16.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_16.setSizePolicy(sizePolicy3)
        self.label_nhietdo_16.setFont(font1)
        self.label_nhietdo_16.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_72.addWidget(self.label_nhietdo_16)


        self.horizontalLayout_59.addWidget(self.widget_109)


        self.verticalLayout_71.addWidget(self.widget_154)

        self.widget_155 = QWidget(self.widget_153)
        self.widget_155.setObjectName(u"widget_155")
        sizePolicy3.setHeightForWidth(self.widget_155.sizePolicy().hasHeightForWidth())
        self.widget_155.setSizePolicy(sizePolicy3)
        self.horizontalLayout_66 = QHBoxLayout(self.widget_155)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.widget_156 = QWidget(self.widget_155)
        self.widget_156.setObjectName(u"widget_156")
        sizePolicy3.setHeightForWidth(self.widget_156.sizePolicy().hasHeightForWidth())
        self.widget_156.setSizePolicy(sizePolicy3)
        self.widget_156.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_67 = QHBoxLayout(self.widget_156)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.widget_110 = QWidget(self.widget_156)
        self.widget_110.setObjectName(u"widget_110")
        sizePolicy4.setHeightForWidth(self.widget_110.sizePolicy().hasHeightForWidth())
        self.widget_110.setSizePolicy(sizePolicy4)
        self.widget_110.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_68 = QHBoxLayout(self.widget_110)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_15 = QPushButton(self.widget_110)
        self.pushButton_nhietdo_15.setObjectName(u"pushButton_nhietdo_15")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_15.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_15.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_15.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_15.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_15.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_15.setIconSize(QSize(16, 16))

        self.horizontalLayout_68.addWidget(self.pushButton_nhietdo_15)


        self.horizontalLayout_67.addWidget(self.widget_110)

        self.widget_111 = QWidget(self.widget_156)
        self.widget_111.setObjectName(u"widget_111")
        self.verticalLayout_73 = QVBoxLayout(self.widget_111)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_17 = QLabel(self.widget_111)
        self.label_nhietdo_17.setObjectName(u"label_nhietdo_17")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_17.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_17.setSizePolicy(sizePolicy3)
        self.label_nhietdo_17.setFont(font1)
        self.label_nhietdo_17.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";\n"
"")

        self.verticalLayout_73.addWidget(self.label_nhietdo_17)


        self.horizontalLayout_67.addWidget(self.widget_111)


        self.horizontalLayout_66.addWidget(self.widget_156)


        self.verticalLayout_71.addWidget(self.widget_155)

        self.widget_157 = QWidget(self.widget_153)
        self.widget_157.setObjectName(u"widget_157")
        sizePolicy3.setHeightForWidth(self.widget_157.sizePolicy().hasHeightForWidth())
        self.widget_157.setSizePolicy(sizePolicy3)
        self.horizontalLayout_69 = QHBoxLayout(self.widget_157)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.widget_158 = QWidget(self.widget_157)
        self.widget_158.setObjectName(u"widget_158")
        sizePolicy3.setHeightForWidth(self.widget_158.sizePolicy().hasHeightForWidth())
        self.widget_158.setSizePolicy(sizePolicy3)
        self.widget_158.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_70 = QHBoxLayout(self.widget_158)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.widget_112 = QWidget(self.widget_158)
        self.widget_112.setObjectName(u"widget_112")
        sizePolicy4.setHeightForWidth(self.widget_112.sizePolicy().hasHeightForWidth())
        self.widget_112.setSizePolicy(sizePolicy4)
        self.widget_112.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_71 = QHBoxLayout(self.widget_112)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_16 = QPushButton(self.widget_112)
        self.pushButton_nhietdo_16.setObjectName(u"pushButton_nhietdo_16")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_16.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_16.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_16.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_16.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_16.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_16.setIconSize(QSize(16, 16))

        self.horizontalLayout_71.addWidget(self.pushButton_nhietdo_16)


        self.horizontalLayout_70.addWidget(self.widget_112)

        self.widget_120 = QWidget(self.widget_158)
        self.widget_120.setObjectName(u"widget_120")
        self.verticalLayout_75 = QVBoxLayout(self.widget_120)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_18 = QLabel(self.widget_120)
        self.label_nhietdo_18.setObjectName(u"label_nhietdo_18")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_18.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_18.setSizePolicy(sizePolicy3)
        self.label_nhietdo_18.setFont(font1)
        self.label_nhietdo_18.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_75.addWidget(self.label_nhietdo_18)


        self.horizontalLayout_70.addWidget(self.widget_120)


        self.horizontalLayout_69.addWidget(self.widget_158)


        self.verticalLayout_71.addWidget(self.widget_157)

        self.widget_159 = QWidget(self.widget_153)
        self.widget_159.setObjectName(u"widget_159")
        sizePolicy4.setHeightForWidth(self.widget_159.sizePolicy().hasHeightForWidth())
        self.widget_159.setSizePolicy(sizePolicy4)
        self.horizontalLayout_72 = QHBoxLayout(self.widget_159)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.widget_160 = QWidget(self.widget_159)
        self.widget_160.setObjectName(u"widget_160")
        sizePolicy3.setHeightForWidth(self.widget_160.sizePolicy().hasHeightForWidth())
        self.widget_160.setSizePolicy(sizePolicy3)
        self.widget_160.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_73 = QHBoxLayout(self.widget_160)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.widget_121 = QWidget(self.widget_160)
        self.widget_121.setObjectName(u"widget_121")
        sizePolicy4.setHeightForWidth(self.widget_121.sizePolicy().hasHeightForWidth())
        self.widget_121.setSizePolicy(sizePolicy4)
        self.widget_121.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_74 = QHBoxLayout(self.widget_121)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_17 = QPushButton(self.widget_121)
        self.pushButton_nhietdo_17.setObjectName(u"pushButton_nhietdo_17")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_17.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_17.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_17.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_17.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_17.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_17.setIconSize(QSize(16, 16))

        self.horizontalLayout_74.addWidget(self.pushButton_nhietdo_17)


        self.horizontalLayout_73.addWidget(self.widget_121)

        self.widget_122 = QWidget(self.widget_160)
        self.widget_122.setObjectName(u"widget_122")
        self.verticalLayout_76 = QVBoxLayout(self.widget_122)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_19 = QLabel(self.widget_122)
        self.label_nhietdo_19.setObjectName(u"label_nhietdo_19")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_19.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_19.setSizePolicy(sizePolicy3)
        self.label_nhietdo_19.setFont(font1)
        self.label_nhietdo_19.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_76.addWidget(self.label_nhietdo_19)


        self.horizontalLayout_73.addWidget(self.widget_122)


        self.horizontalLayout_72.addWidget(self.widget_160)


        self.verticalLayout_71.addWidget(self.widget_159)

        self.widget_161 = QWidget(self.widget_153)
        self.widget_161.setObjectName(u"widget_161")
        sizePolicy3.setHeightForWidth(self.widget_161.sizePolicy().hasHeightForWidth())
        self.widget_161.setSizePolicy(sizePolicy3)
        self.widget_161.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_81 = QHBoxLayout(self.widget_161)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.widget_162 = QWidget(self.widget_161)
        self.widget_162.setObjectName(u"widget_162")
        sizePolicy3.setHeightForWidth(self.widget_162.sizePolicy().hasHeightForWidth())
        self.widget_162.setSizePolicy(sizePolicy3)
        self.widget_162.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_82 = QHBoxLayout(self.widget_162)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.widget_123 = QWidget(self.widget_162)
        self.widget_123.setObjectName(u"widget_123")
        sizePolicy4.setHeightForWidth(self.widget_123.sizePolicy().hasHeightForWidth())
        self.widget_123.setSizePolicy(sizePolicy4)
        self.widget_123.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_83 = QHBoxLayout(self.widget_123)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_18 = QPushButton(self.widget_123)
        self.pushButton_nhietdo_18.setObjectName(u"pushButton_nhietdo_18")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_18.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_18.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_18.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_18.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_18.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_18.setIconSize(QSize(16, 16))

        self.horizontalLayout_83.addWidget(self.pushButton_nhietdo_18)


        self.horizontalLayout_82.addWidget(self.widget_123)

        self.widget_163 = QWidget(self.widget_162)
        self.widget_163.setObjectName(u"widget_163")
        self.verticalLayout_77 = QVBoxLayout(self.widget_163)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_20 = QLabel(self.widget_163)
        self.label_nhietdo_20.setObjectName(u"label_nhietdo_20")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_20.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_20.setSizePolicy(sizePolicy3)
        self.label_nhietdo_20.setFont(font1)
        self.label_nhietdo_20.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";\n"
"")

        self.verticalLayout_77.addWidget(self.label_nhietdo_20)


        self.horizontalLayout_82.addWidget(self.widget_163)


        self.horizontalLayout_81.addWidget(self.widget_162)


        self.verticalLayout_71.addWidget(self.widget_161)


        self.horizontalLayout_55.addWidget(self.widget_153)


        self.verticalLayout_43.addWidget(self.widget_98)


        self.verticalLayout_84.addWidget(self.widget_36)


        self.horizontalLayout_6.addWidget(self.widget_96)


        self.verticalLayout_25.addWidget(self.lisTram_1)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy2.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy2)
        self.widget_12.setStyleSheet(u"\n"
"border: 1px solid rgb(85, 85, 127);\n"
"margin:5px;")
        self.horizontalLayout = QHBoxLayout(self.widget_12)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy2.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 9)
        self.widget_170 = QWidget(self.widget_14)
        self.widget_170.setObjectName(u"widget_170")
        sizePolicy4.setHeightForWidth(self.widget_170.sizePolicy().hasHeightForWidth())
        self.widget_170.setSizePolicy(sizePolicy4)
        self.widget_170.setLayoutDirection(Qt.LeftToRight)
        self.widget_170.setStyleSheet(u"border:none;\n"
"\n"
"")
        self.verticalLayout_33 = QVBoxLayout(self.widget_170)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.widget_224 = QWidget(self.widget_170)
        self.widget_224.setObjectName(u"widget_224")
        sizePolicy3.setHeightForWidth(self.widget_224.sizePolicy().hasHeightForWidth())
        self.widget_224.setSizePolicy(sizePolicy3)
        self.widget_224.setLayoutDirection(Qt.LeftToRight)
        self.widget_224.setStyleSheet(u"border:none;\n"
"\n"
"")
        self.verticalLayout_32 = QVBoxLayout(self.widget_224)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.widget_224)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy3.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy3)
        self.pushButton_11.setMinimumSize(QSize(145, 0))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"	\n"
"	\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_32.addWidget(self.pushButton_11)

        self.label_7 = QLabel(self.widget_224)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_7)


        self.verticalLayout_33.addWidget(self.widget_224)


        self.horizontalLayout_2.addWidget(self.widget_170)

        self.widget_113 = QWidget(self.widget_14)
        self.widget_113.setObjectName(u"widget_113")
        sizePolicy4.setHeightForWidth(self.widget_113.sizePolicy().hasHeightForWidth())
        self.widget_113.setSizePolicy(sizePolicy4)
        self.widget_113.setLayoutDirection(Qt.RightToLeft)
        self.widget_113.setStyleSheet(u"border:none;")
        self.verticalLayout_52 = QVBoxLayout(self.widget_113)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.widget_113)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy3.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy3)
        self.pushButton_10.setMinimumSize(QSize(100, 0))
        self.pushButton_10.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.verticalLayout_52.addWidget(self.pushButton_10)

        self.label_4 = QLabel(self.widget_113)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.widget_113)

        self.widget_114 = QWidget(self.widget_14)
        self.widget_114.setObjectName(u"widget_114")
        sizePolicy4.setHeightForWidth(self.widget_114.sizePolicy().hasHeightForWidth())
        self.widget_114.setSizePolicy(sizePolicy4)
        self.widget_114.setStyleSheet(u"border:none;")
        self.verticalLayout_65 = QVBoxLayout(self.widget_114)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.widget_114)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy3.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy3)
        self.pushButton_9.setMinimumSize(QSize(100, 0))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.verticalLayout_65.addWidget(self.pushButton_9)

        self.label_5 = QLabel(self.widget_114)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.label_5)


        self.horizontalLayout_2.addWidget(self.widget_114)


        self.horizontalLayout.addWidget(self.widget_14)


        self.verticalLayout_25.addWidget(self.widget_12)

        self.lisTram_2 = QWidget(self.widget_10)
        self.lisTram_2.setObjectName(u"lisTram_2")
        sizePolicy.setHeightForWidth(self.lisTram_2.sizePolicy().hasHeightForWidth())
        self.lisTram_2.setSizePolicy(sizePolicy)
        self.lisTram_2.setStyleSheet(u"border-right-color: rgb(0, 0, 0);")
        self.horizontalLayout_60 = QHBoxLayout(self.lisTram_2)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 15, 30, 0)
        self.widget_18 = QWidget(self.lisTram_2)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.widget_18.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_74 = QVBoxLayout(self.widget_18)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.widget_115 = QWidget(self.widget_18)
        self.widget_115.setObjectName(u"widget_115")
        sizePolicy3.setHeightForWidth(self.widget_115.sizePolicy().hasHeightForWidth())
        self.widget_115.setSizePolicy(sizePolicy3)
        self.widget_115.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_115)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.widget_115)
        self.label_31.setObjectName(u"label_31")
        sizePolicy4.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy4)
        self.label_31.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_61.addWidget(self.label_31)

        self.pushButton_anhsang_12 = QPushButton(self.widget_115)
        self.pushButton_anhsang_12.setObjectName(u"pushButton_anhsang_12")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_12.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_12.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_12.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_12.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_12.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_12.setIconSize(QSize(16, 16))

        self.horizontalLayout_61.addWidget(self.pushButton_anhsang_12)


        self.verticalLayout_74.addWidget(self.widget_115)

        self.widget_116 = QWidget(self.widget_18)
        self.widget_116.setObjectName(u"widget_116")
        sizePolicy3.setHeightForWidth(self.widget_116.sizePolicy().hasHeightForWidth())
        self.widget_116.setSizePolicy(sizePolicy3)
        self.horizontalLayout_62 = QHBoxLayout(self.widget_116)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.widget_117 = QWidget(self.widget_116)
        self.widget_117.setObjectName(u"widget_117")
        sizePolicy3.setHeightForWidth(self.widget_117.sizePolicy().hasHeightForWidth())
        self.widget_117.setSizePolicy(sizePolicy3)
        self.verticalLayout_30 = QVBoxLayout(self.widget_117)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 30, 0)
        self.widget_118 = QWidget(self.widget_117)
        self.widget_118.setObjectName(u"widget_118")
        sizePolicy.setHeightForWidth(self.widget_118.sizePolicy().hasHeightForWidth())
        self.widget_118.setSizePolicy(sizePolicy)
        self.verticalLayout_23 = QVBoxLayout(self.widget_118)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 20)
        self.label_11 = QLabel(self.widget_118)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"")
        self.label_11.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_11.setScaledContents(True)

        self.verticalLayout_23.addWidget(self.label_11)


        self.verticalLayout_30.addWidget(self.widget_118)

        self.widget_119 = QWidget(self.widget_117)
        self.widget_119.setObjectName(u"widget_119")
        sizePolicy3.setHeightForWidth(self.widget_119.sizePolicy().hasHeightForWidth())
        self.widget_119.setSizePolicy(sizePolicy3)
        self.horizontalLayout_63 = QHBoxLayout(self.widget_119)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.widget_144 = QWidget(self.widget_119)
        self.widget_144.setObjectName(u"widget_144")
        self.verticalLayout_78 = QVBoxLayout(self.widget_144)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.widget_145 = QWidget(self.widget_144)
        self.widget_145.setObjectName(u"widget_145")
        self.horizontalLayout_64 = QHBoxLayout(self.widget_145)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_4 = QPushButton(self.widget_145)
        self.pushButton_ac1_4.setObjectName(u"pushButton_ac1_4")
        sizePolicy4.setHeightForWidth(self.pushButton_ac1_4.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_4.setSizePolicy(sizePolicy4)
        self.pushButton_ac1_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_64.addWidget(self.pushButton_ac1_4)


        self.verticalLayout_78.addWidget(self.widget_145)

        self.widget_146 = QWidget(self.widget_144)
        self.widget_146.setObjectName(u"widget_146")
        self.verticalLayout_79 = QVBoxLayout(self.widget_146)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.widget_146)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.label_32)


        self.verticalLayout_78.addWidget(self.widget_146)


        self.horizontalLayout_63.addWidget(self.widget_144)

        self.widget_147 = QWidget(self.widget_119)
        self.widget_147.setObjectName(u"widget_147")
        self.verticalLayout_80 = QVBoxLayout(self.widget_147)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.widget_148 = QWidget(self.widget_147)
        self.widget_148.setObjectName(u"widget_148")
        self.horizontalLayout_75 = QHBoxLayout(self.widget_148)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_4 = QPushButton(self.widget_148)
        self.pushButton_ac2_4.setObjectName(u"pushButton_ac2_4")
        sizePolicy4.setHeightForWidth(self.pushButton_ac2_4.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_4.setSizePolicy(sizePolicy4)
        self.pushButton_ac2_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_75.addWidget(self.pushButton_ac2_4)


        self.verticalLayout_80.addWidget(self.widget_148)

        self.widget_149 = QWidget(self.widget_147)
        self.widget_149.setObjectName(u"widget_149")
        self.verticalLayout_90 = QVBoxLayout(self.widget_149)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.widget_149)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_90.addWidget(self.label_33)


        self.verticalLayout_80.addWidget(self.widget_149)


        self.horizontalLayout_63.addWidget(self.widget_147)


        self.verticalLayout_30.addWidget(self.widget_119)


        self.horizontalLayout_62.addWidget(self.widget_117)

        self.widget_150 = QWidget(self.widget_116)
        self.widget_150.setObjectName(u"widget_150")
        sizePolicy.setHeightForWidth(self.widget_150.sizePolicy().hasHeightForWidth())
        self.widget_150.setSizePolicy(sizePolicy)
        self.widget_150.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Segoe UI\";")
        self.verticalLayout_26 = QVBoxLayout(self.widget_150)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 30, 0)
        self.widget_151 = QWidget(self.widget_150)
        self.widget_151.setObjectName(u"widget_151")
        sizePolicy3.setHeightForWidth(self.widget_151.sizePolicy().hasHeightForWidth())
        self.widget_151.setSizePolicy(sizePolicy3)
        self.widget_151.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_76 = QHBoxLayout(self.widget_151)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.widget_152 = QWidget(self.widget_151)
        self.widget_152.setObjectName(u"widget_152")
        sizePolicy4.setHeightForWidth(self.widget_152.sizePolicy().hasHeightForWidth())
        self.widget_152.setSizePolicy(sizePolicy4)
        self.widget_152.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_77 = QHBoxLayout(self.widget_152)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_6 = QPushButton(self.widget_152)
        self.pushButton_nhietdo_6.setObjectName(u"pushButton_nhietdo_6")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_6.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_6.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_6.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_6.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_6.setIconSize(QSize(16, 16))

        self.horizontalLayout_77.addWidget(self.pushButton_nhietdo_6)


        self.horizontalLayout_76.addWidget(self.widget_152)

        self.widget_164 = QWidget(self.widget_151)
        self.widget_164.setObjectName(u"widget_164")
        self.verticalLayout_31 = QVBoxLayout(self.widget_164)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_5 = QLabel(self.widget_164)
        self.label_nhietdo_5.setObjectName(u"label_nhietdo_5")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_5.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_5.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_nhietdo_5.setFont(font2)
        self.label_nhietdo_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_31.addWidget(self.label_nhietdo_5)


        self.horizontalLayout_76.addWidget(self.widget_164)


        self.verticalLayout_26.addWidget(self.widget_151)

        self.widget_165 = QWidget(self.widget_150)
        self.widget_165.setObjectName(u"widget_165")
        sizePolicy3.setHeightForWidth(self.widget_165.sizePolicy().hasHeightForWidth())
        self.widget_165.setSizePolicy(sizePolicy3)
        self.horizontalLayout_78 = QHBoxLayout(self.widget_165)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.widget_166 = QWidget(self.widget_165)
        self.widget_166.setObjectName(u"widget_166")
        sizePolicy3.setHeightForWidth(self.widget_166.sizePolicy().hasHeightForWidth())
        self.widget_166.setSizePolicy(sizePolicy3)
        self.widget_166.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_79 = QHBoxLayout(self.widget_166)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.widget_167 = QWidget(self.widget_166)
        self.widget_167.setObjectName(u"widget_167")
        sizePolicy4.setHeightForWidth(self.widget_167.sizePolicy().hasHeightForWidth())
        self.widget_167.setSizePolicy(sizePolicy4)
        self.widget_167.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_80 = QHBoxLayout(self.widget_167)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_9 = QPushButton(self.widget_167)
        self.pushButton_nhietdo_9.setObjectName(u"pushButton_nhietdo_9")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_9.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_9.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_9.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_9.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_9.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_9.setIconSize(QSize(16, 16))

        self.horizontalLayout_80.addWidget(self.pushButton_nhietdo_9)


        self.horizontalLayout_79.addWidget(self.widget_167)

        self.widget_168 = QWidget(self.widget_166)
        self.widget_168.setObjectName(u"widget_168")
        self.verticalLayout_91 = QVBoxLayout(self.widget_168)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_13 = QLabel(self.widget_168)
        self.label_nhietdo_13.setObjectName(u"label_nhietdo_13")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_13.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_13.setSizePolicy(sizePolicy3)
        self.label_nhietdo_13.setFont(font2)
        self.label_nhietdo_13.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_91.addWidget(self.label_nhietdo_13)


        self.horizontalLayout_79.addWidget(self.widget_168)


        self.horizontalLayout_78.addWidget(self.widget_166)


        self.verticalLayout_26.addWidget(self.widget_165)

        self.widget_169 = QWidget(self.widget_150)
        self.widget_169.setObjectName(u"widget_169")
        sizePolicy3.setHeightForWidth(self.widget_169.sizePolicy().hasHeightForWidth())
        self.widget_169.setSizePolicy(sizePolicy3)
        self.horizontalLayout_84 = QHBoxLayout(self.widget_169)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.widget_171 = QWidget(self.widget_169)
        self.widget_171.setObjectName(u"widget_171")
        sizePolicy3.setHeightForWidth(self.widget_171.sizePolicy().hasHeightForWidth())
        self.widget_171.setSizePolicy(sizePolicy3)
        self.widget_171.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_85 = QHBoxLayout(self.widget_171)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.widget_172 = QWidget(self.widget_171)
        self.widget_172.setObjectName(u"widget_172")
        sizePolicy4.setHeightForWidth(self.widget_172.sizePolicy().hasHeightForWidth())
        self.widget_172.setSizePolicy(sizePolicy4)
        self.widget_172.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_86 = QHBoxLayout(self.widget_172)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_10 = QPushButton(self.widget_172)
        self.pushButton_nhietdo_10.setObjectName(u"pushButton_nhietdo_10")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_10.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_10.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_10.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_10.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_10.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_10.setIconSize(QSize(16, 16))

        self.horizontalLayout_86.addWidget(self.pushButton_nhietdo_10)


        self.horizontalLayout_85.addWidget(self.widget_172)

        self.widget_173 = QWidget(self.widget_171)
        self.widget_173.setObjectName(u"widget_173")
        self.verticalLayout_92 = QVBoxLayout(self.widget_173)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_14 = QLabel(self.widget_173)
        self.label_nhietdo_14.setObjectName(u"label_nhietdo_14")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_14.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_14.setSizePolicy(sizePolicy3)
        self.label_nhietdo_14.setFont(font2)
        self.label_nhietdo_14.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_92.addWidget(self.label_nhietdo_14)


        self.horizontalLayout_85.addWidget(self.widget_173)


        self.horizontalLayout_84.addWidget(self.widget_171)


        self.verticalLayout_26.addWidget(self.widget_169)

        self.widget_174 = QWidget(self.widget_150)
        self.widget_174.setObjectName(u"widget_174")
        sizePolicy4.setHeightForWidth(self.widget_174.sizePolicy().hasHeightForWidth())
        self.widget_174.setSizePolicy(sizePolicy4)
        self.horizontalLayout_87 = QHBoxLayout(self.widget_174)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.widget_175 = QWidget(self.widget_174)
        self.widget_175.setObjectName(u"widget_175")
        sizePolicy3.setHeightForWidth(self.widget_175.sizePolicy().hasHeightForWidth())
        self.widget_175.setSizePolicy(sizePolicy3)
        self.widget_175.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_88 = QHBoxLayout(self.widget_175)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.widget_176 = QWidget(self.widget_175)
        self.widget_176.setObjectName(u"widget_176")
        sizePolicy4.setHeightForWidth(self.widget_176.sizePolicy().hasHeightForWidth())
        self.widget_176.setSizePolicy(sizePolicy4)
        self.widget_176.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_89 = QHBoxLayout(self.widget_176)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_19 = QPushButton(self.widget_176)
        self.pushButton_nhietdo_19.setObjectName(u"pushButton_nhietdo_19")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_19.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_19.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_19.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_19.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_19.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_19.setIconSize(QSize(16, 16))

        self.horizontalLayout_89.addWidget(self.pushButton_nhietdo_19)


        self.horizontalLayout_88.addWidget(self.widget_176)

        self.widget_177 = QWidget(self.widget_175)
        self.widget_177.setObjectName(u"widget_177")
        self.verticalLayout_93 = QVBoxLayout(self.widget_177)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_21 = QLabel(self.widget_177)
        self.label_nhietdo_21.setObjectName(u"label_nhietdo_21")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_21.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_21.setSizePolicy(sizePolicy3)
        self.label_nhietdo_21.setFont(font2)
        self.label_nhietdo_21.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_93.addWidget(self.label_nhietdo_21)


        self.horizontalLayout_88.addWidget(self.widget_177)


        self.horizontalLayout_87.addWidget(self.widget_175)


        self.verticalLayout_26.addWidget(self.widget_174)

        self.widget_178 = QWidget(self.widget_150)
        self.widget_178.setObjectName(u"widget_178")
        sizePolicy3.setHeightForWidth(self.widget_178.sizePolicy().hasHeightForWidth())
        self.widget_178.setSizePolicy(sizePolicy3)
        self.widget_178.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_90 = QHBoxLayout(self.widget_178)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.widget_179 = QWidget(self.widget_178)
        self.widget_179.setObjectName(u"widget_179")
        sizePolicy3.setHeightForWidth(self.widget_179.sizePolicy().hasHeightForWidth())
        self.widget_179.setSizePolicy(sizePolicy3)
        self.widget_179.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_91 = QHBoxLayout(self.widget_179)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.widget_180 = QWidget(self.widget_179)
        self.widget_180.setObjectName(u"widget_180")
        sizePolicy4.setHeightForWidth(self.widget_180.sizePolicy().hasHeightForWidth())
        self.widget_180.setSizePolicy(sizePolicy4)
        self.widget_180.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_92 = QHBoxLayout(self.widget_180)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_20 = QPushButton(self.widget_180)
        self.pushButton_nhietdo_20.setObjectName(u"pushButton_nhietdo_20")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_20.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_20.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_20.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_20.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_20.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_20.setIconSize(QSize(16, 16))

        self.horizontalLayout_92.addWidget(self.pushButton_nhietdo_20)


        self.horizontalLayout_91.addWidget(self.widget_180)

        self.widget_181 = QWidget(self.widget_179)
        self.widget_181.setObjectName(u"widget_181")
        self.verticalLayout_94 = QVBoxLayout(self.widget_181)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_22 = QLabel(self.widget_181)
        self.label_nhietdo_22.setObjectName(u"label_nhietdo_22")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_22.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_22.setSizePolicy(sizePolicy3)
        self.label_nhietdo_22.setFont(font2)
        self.label_nhietdo_22.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_94.addWidget(self.label_nhietdo_22)


        self.horizontalLayout_91.addWidget(self.widget_181)


        self.horizontalLayout_90.addWidget(self.widget_179)


        self.verticalLayout_26.addWidget(self.widget_178)


        self.horizontalLayout_62.addWidget(self.widget_150)


        self.verticalLayout_74.addWidget(self.widget_116)


        self.horizontalLayout_60.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.lisTram_2)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.widget_19.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_95 = QVBoxLayout(self.widget_19)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.widget_37 = QWidget(self.widget_19)
        self.widget_37.setObjectName(u"widget_37")
        sizePolicy3.setHeightForWidth(self.widget_37.sizePolicy().hasHeightForWidth())
        self.widget_37.setSizePolicy(sizePolicy3)
        self.verticalLayout_96 = QVBoxLayout(self.widget_37)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.widget_182 = QWidget(self.widget_37)
        self.widget_182.setObjectName(u"widget_182")
        sizePolicy3.setHeightForWidth(self.widget_182.sizePolicy().hasHeightForWidth())
        self.widget_182.setSizePolicy(sizePolicy3)
        self.widget_182.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_93 = QHBoxLayout(self.widget_182)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.widget_182)
        self.label_34.setObjectName(u"label_34")
        sizePolicy4.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy4)
        self.label_34.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_93.addWidget(self.label_34)

        self.pushButton_anhsang_13 = QPushButton(self.widget_182)
        self.pushButton_anhsang_13.setObjectName(u"pushButton_anhsang_13")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_13.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_13.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_13.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_13.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_13.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_13.setIconSize(QSize(16, 16))

        self.horizontalLayout_93.addWidget(self.pushButton_anhsang_13)


        self.verticalLayout_96.addWidget(self.widget_182)

        self.widget_183 = QWidget(self.widget_37)
        self.widget_183.setObjectName(u"widget_183")
        sizePolicy3.setHeightForWidth(self.widget_183.sizePolicy().hasHeightForWidth())
        self.widget_183.setSizePolicy(sizePolicy3)
        self.horizontalLayout_94 = QHBoxLayout(self.widget_183)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.widget_184 = QWidget(self.widget_183)
        self.widget_184.setObjectName(u"widget_184")
        sizePolicy3.setHeightForWidth(self.widget_184.sizePolicy().hasHeightForWidth())
        self.widget_184.setSizePolicy(sizePolicy3)
        self.verticalLayout_97 = QVBoxLayout(self.widget_184)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 30, 0)
        self.widget_185 = QWidget(self.widget_184)
        self.widget_185.setObjectName(u"widget_185")
        sizePolicy.setHeightForWidth(self.widget_185.sizePolicy().hasHeightForWidth())
        self.widget_185.setSizePolicy(sizePolicy)
        self.verticalLayout_98 = QVBoxLayout(self.widget_185)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 20)
        self.label_13 = QLabel(self.widget_185)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"")
        self.label_13.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_13.setScaledContents(True)

        self.verticalLayout_98.addWidget(self.label_13)


        self.verticalLayout_97.addWidget(self.widget_185)

        self.widget_186 = QWidget(self.widget_184)
        self.widget_186.setObjectName(u"widget_186")
        sizePolicy3.setHeightForWidth(self.widget_186.sizePolicy().hasHeightForWidth())
        self.widget_186.setSizePolicy(sizePolicy3)
        self.horizontalLayout_95 = QHBoxLayout(self.widget_186)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.widget_187 = QWidget(self.widget_186)
        self.widget_187.setObjectName(u"widget_187")
        self.verticalLayout_99 = QVBoxLayout(self.widget_187)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.widget_188 = QWidget(self.widget_187)
        self.widget_188.setObjectName(u"widget_188")
        self.horizontalLayout_96 = QHBoxLayout(self.widget_188)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_5 = QPushButton(self.widget_188)
        self.pushButton_ac1_5.setObjectName(u"pushButton_ac1_5")
        sizePolicy4.setHeightForWidth(self.pushButton_ac1_5.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_5.setSizePolicy(sizePolicy4)
        self.pushButton_ac1_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_96.addWidget(self.pushButton_ac1_5)


        self.verticalLayout_99.addWidget(self.widget_188)

        self.widget_189 = QWidget(self.widget_187)
        self.widget_189.setObjectName(u"widget_189")
        self.verticalLayout_100 = QVBoxLayout(self.widget_189)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.widget_189)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.label_35)


        self.verticalLayout_99.addWidget(self.widget_189)


        self.horizontalLayout_95.addWidget(self.widget_187)

        self.widget_190 = QWidget(self.widget_186)
        self.widget_190.setObjectName(u"widget_190")
        self.verticalLayout_101 = QVBoxLayout(self.widget_190)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.widget_191 = QWidget(self.widget_190)
        self.widget_191.setObjectName(u"widget_191")
        self.horizontalLayout_97 = QHBoxLayout(self.widget_191)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_5 = QPushButton(self.widget_191)
        self.pushButton_ac2_5.setObjectName(u"pushButton_ac2_5")
        sizePolicy4.setHeightForWidth(self.pushButton_ac2_5.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_5.setSizePolicy(sizePolicy4)
        self.pushButton_ac2_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_97.addWidget(self.pushButton_ac2_5)


        self.verticalLayout_101.addWidget(self.widget_191)

        self.widget_192 = QWidget(self.widget_190)
        self.widget_192.setObjectName(u"widget_192")
        self.verticalLayout_102 = QVBoxLayout(self.widget_192)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget_192)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.label_36)


        self.verticalLayout_101.addWidget(self.widget_192)


        self.horizontalLayout_95.addWidget(self.widget_190)


        self.verticalLayout_97.addWidget(self.widget_186)


        self.horizontalLayout_94.addWidget(self.widget_184)

        self.widget_193 = QWidget(self.widget_183)
        self.widget_193.setObjectName(u"widget_193")
        sizePolicy.setHeightForWidth(self.widget_193.sizePolicy().hasHeightForWidth())
        self.widget_193.setSizePolicy(sizePolicy)
        self.widget_193.setStyleSheet(u"padding-right:30px;")
        self.verticalLayout_88 = QVBoxLayout(self.widget_193)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.widget_194 = QWidget(self.widget_193)
        self.widget_194.setObjectName(u"widget_194")
        sizePolicy3.setHeightForWidth(self.widget_194.sizePolicy().hasHeightForWidth())
        self.widget_194.setSizePolicy(sizePolicy3)
        self.widget_194.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_98 = QHBoxLayout(self.widget_194)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.widget_195 = QWidget(self.widget_194)
        self.widget_195.setObjectName(u"widget_195")
        sizePolicy4.setHeightForWidth(self.widget_195.sizePolicy().hasHeightForWidth())
        self.widget_195.setSizePolicy(sizePolicy4)
        self.widget_195.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_99 = QHBoxLayout(self.widget_195)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_21 = QPushButton(self.widget_195)
        self.pushButton_nhietdo_21.setObjectName(u"pushButton_nhietdo_21")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_21.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_21.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_21.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_21.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_21.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_21.setIconSize(QSize(16, 16))

        self.horizontalLayout_99.addWidget(self.pushButton_nhietdo_21)


        self.horizontalLayout_98.addWidget(self.widget_195)

        self.widget_196 = QWidget(self.widget_194)
        self.widget_196.setObjectName(u"widget_196")
        self.verticalLayout_103 = QVBoxLayout(self.widget_196)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_23 = QLabel(self.widget_196)
        self.label_nhietdo_23.setObjectName(u"label_nhietdo_23")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_23.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_23.setSizePolicy(sizePolicy3)
        self.label_nhietdo_23.setFont(font2)
        self.label_nhietdo_23.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_103.addWidget(self.label_nhietdo_23)


        self.horizontalLayout_98.addWidget(self.widget_196)


        self.verticalLayout_88.addWidget(self.widget_194)

        self.widget_197 = QWidget(self.widget_193)
        self.widget_197.setObjectName(u"widget_197")
        sizePolicy3.setHeightForWidth(self.widget_197.sizePolicy().hasHeightForWidth())
        self.widget_197.setSizePolicy(sizePolicy3)
        self.horizontalLayout_100 = QHBoxLayout(self.widget_197)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.widget_198 = QWidget(self.widget_197)
        self.widget_198.setObjectName(u"widget_198")
        sizePolicy3.setHeightForWidth(self.widget_198.sizePolicy().hasHeightForWidth())
        self.widget_198.setSizePolicy(sizePolicy3)
        self.widget_198.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_101 = QHBoxLayout(self.widget_198)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.widget_199 = QWidget(self.widget_198)
        self.widget_199.setObjectName(u"widget_199")
        sizePolicy4.setHeightForWidth(self.widget_199.sizePolicy().hasHeightForWidth())
        self.widget_199.setSizePolicy(sizePolicy4)
        self.widget_199.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_102 = QHBoxLayout(self.widget_199)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_22 = QPushButton(self.widget_199)
        self.pushButton_nhietdo_22.setObjectName(u"pushButton_nhietdo_22")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_22.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_22.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_22.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_22.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_22.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_22.setIconSize(QSize(16, 16))

        self.horizontalLayout_102.addWidget(self.pushButton_nhietdo_22)


        self.horizontalLayout_101.addWidget(self.widget_199)

        self.widget_200 = QWidget(self.widget_198)
        self.widget_200.setObjectName(u"widget_200")
        self.verticalLayout_104 = QVBoxLayout(self.widget_200)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_24 = QLabel(self.widget_200)
        self.label_nhietdo_24.setObjectName(u"label_nhietdo_24")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_24.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_24.setSizePolicy(sizePolicy3)
        self.label_nhietdo_24.setFont(font2)
        self.label_nhietdo_24.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_104.addWidget(self.label_nhietdo_24)


        self.horizontalLayout_101.addWidget(self.widget_200)


        self.horizontalLayout_100.addWidget(self.widget_198)


        self.verticalLayout_88.addWidget(self.widget_197)

        self.widget_201 = QWidget(self.widget_193)
        self.widget_201.setObjectName(u"widget_201")
        sizePolicy3.setHeightForWidth(self.widget_201.sizePolicy().hasHeightForWidth())
        self.widget_201.setSizePolicy(sizePolicy3)
        self.horizontalLayout_103 = QHBoxLayout(self.widget_201)
        self.horizontalLayout_103.setSpacing(0)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.widget_202 = QWidget(self.widget_201)
        self.widget_202.setObjectName(u"widget_202")
        sizePolicy3.setHeightForWidth(self.widget_202.sizePolicy().hasHeightForWidth())
        self.widget_202.setSizePolicy(sizePolicy3)
        self.widget_202.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_104 = QHBoxLayout(self.widget_202)
        self.horizontalLayout_104.setSpacing(0)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.widget_203 = QWidget(self.widget_202)
        self.widget_203.setObjectName(u"widget_203")
        sizePolicy4.setHeightForWidth(self.widget_203.sizePolicy().hasHeightForWidth())
        self.widget_203.setSizePolicy(sizePolicy4)
        self.widget_203.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_105 = QHBoxLayout(self.widget_203)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_23 = QPushButton(self.widget_203)
        self.pushButton_nhietdo_23.setObjectName(u"pushButton_nhietdo_23")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_23.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_23.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_23.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_23.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_23.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_23.setIconSize(QSize(16, 16))

        self.horizontalLayout_105.addWidget(self.pushButton_nhietdo_23)


        self.horizontalLayout_104.addWidget(self.widget_203)

        self.widget_204 = QWidget(self.widget_202)
        self.widget_204.setObjectName(u"widget_204")
        self.verticalLayout_105 = QVBoxLayout(self.widget_204)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_25 = QLabel(self.widget_204)
        self.label_nhietdo_25.setObjectName(u"label_nhietdo_25")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_25.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_25.setSizePolicy(sizePolicy3)
        self.label_nhietdo_25.setFont(font2)
        self.label_nhietdo_25.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_105.addWidget(self.label_nhietdo_25)


        self.horizontalLayout_104.addWidget(self.widget_204)


        self.horizontalLayout_103.addWidget(self.widget_202)


        self.verticalLayout_88.addWidget(self.widget_201)

        self.widget_205 = QWidget(self.widget_193)
        self.widget_205.setObjectName(u"widget_205")
        sizePolicy4.setHeightForWidth(self.widget_205.sizePolicy().hasHeightForWidth())
        self.widget_205.setSizePolicy(sizePolicy4)
        self.horizontalLayout_106 = QHBoxLayout(self.widget_205)
        self.horizontalLayout_106.setSpacing(0)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.widget_206 = QWidget(self.widget_205)
        self.widget_206.setObjectName(u"widget_206")
        sizePolicy3.setHeightForWidth(self.widget_206.sizePolicy().hasHeightForWidth())
        self.widget_206.setSizePolicy(sizePolicy3)
        self.widget_206.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_107 = QHBoxLayout(self.widget_206)
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.widget_207 = QWidget(self.widget_206)
        self.widget_207.setObjectName(u"widget_207")
        sizePolicy4.setHeightForWidth(self.widget_207.sizePolicy().hasHeightForWidth())
        self.widget_207.setSizePolicy(sizePolicy4)
        self.widget_207.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_108 = QHBoxLayout(self.widget_207)
        self.horizontalLayout_108.setSpacing(0)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_24 = QPushButton(self.widget_207)
        self.pushButton_nhietdo_24.setObjectName(u"pushButton_nhietdo_24")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_24.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_24.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_24.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_24.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_24.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_24.setIconSize(QSize(16, 16))

        self.horizontalLayout_108.addWidget(self.pushButton_nhietdo_24)


        self.horizontalLayout_107.addWidget(self.widget_207)

        self.widget_208 = QWidget(self.widget_206)
        self.widget_208.setObjectName(u"widget_208")
        self.verticalLayout_106 = QVBoxLayout(self.widget_208)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_26 = QLabel(self.widget_208)
        self.label_nhietdo_26.setObjectName(u"label_nhietdo_26")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_26.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_26.setSizePolicy(sizePolicy3)
        self.label_nhietdo_26.setFont(font2)
        self.label_nhietdo_26.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_106.addWidget(self.label_nhietdo_26)


        self.horizontalLayout_107.addWidget(self.widget_208)


        self.horizontalLayout_106.addWidget(self.widget_206)


        self.verticalLayout_88.addWidget(self.widget_205)

        self.widget_209 = QWidget(self.widget_193)
        self.widget_209.setObjectName(u"widget_209")
        sizePolicy3.setHeightForWidth(self.widget_209.sizePolicy().hasHeightForWidth())
        self.widget_209.setSizePolicy(sizePolicy3)
        self.widget_209.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_109 = QHBoxLayout(self.widget_209)
        self.horizontalLayout_109.setSpacing(0)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.widget_210 = QWidget(self.widget_209)
        self.widget_210.setObjectName(u"widget_210")
        sizePolicy3.setHeightForWidth(self.widget_210.sizePolicy().hasHeightForWidth())
        self.widget_210.setSizePolicy(sizePolicy3)
        self.widget_210.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_110 = QHBoxLayout(self.widget_210)
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.widget_211 = QWidget(self.widget_210)
        self.widget_211.setObjectName(u"widget_211")
        sizePolicy4.setHeightForWidth(self.widget_211.sizePolicy().hasHeightForWidth())
        self.widget_211.setSizePolicy(sizePolicy4)
        self.widget_211.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_111 = QHBoxLayout(self.widget_211)
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_25 = QPushButton(self.widget_211)
        self.pushButton_nhietdo_25.setObjectName(u"pushButton_nhietdo_25")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_25.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_25.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_25.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_25.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_25.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_25.setIconSize(QSize(16, 16))

        self.horizontalLayout_111.addWidget(self.pushButton_nhietdo_25)


        self.horizontalLayout_110.addWidget(self.widget_211)

        self.widget_212 = QWidget(self.widget_210)
        self.widget_212.setObjectName(u"widget_212")
        self.verticalLayout_107 = QVBoxLayout(self.widget_212)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_27 = QLabel(self.widget_212)
        self.label_nhietdo_27.setObjectName(u"label_nhietdo_27")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_27.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_27.setSizePolicy(sizePolicy3)
        self.label_nhietdo_27.setFont(font2)
        self.label_nhietdo_27.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_107.addWidget(self.label_nhietdo_27)


        self.horizontalLayout_110.addWidget(self.widget_212)


        self.horizontalLayout_109.addWidget(self.widget_210)


        self.verticalLayout_88.addWidget(self.widget_209)


        self.horizontalLayout_94.addWidget(self.widget_193)


        self.verticalLayout_96.addWidget(self.widget_183)


        self.verticalLayout_95.addWidget(self.widget_37)


        self.horizontalLayout_60.addWidget(self.widget_19)

        self.widget_213 = QWidget(self.lisTram_2)
        self.widget_213.setObjectName(u"widget_213")
        self.widget_213.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_108 = QVBoxLayout(self.widget_213)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.widget_214 = QWidget(self.widget_213)
        self.widget_214.setObjectName(u"widget_214")
        sizePolicy3.setHeightForWidth(self.widget_214.sizePolicy().hasHeightForWidth())
        self.widget_214.setSizePolicy(sizePolicy3)
        self.verticalLayout_109 = QVBoxLayout(self.widget_214)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.widget_215 = QWidget(self.widget_214)
        self.widget_215.setObjectName(u"widget_215")
        sizePolicy3.setHeightForWidth(self.widget_215.sizePolicy().hasHeightForWidth())
        self.widget_215.setSizePolicy(sizePolicy3)
        self.widget_215.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_112 = QHBoxLayout(self.widget_215)
        self.horizontalLayout_112.setSpacing(0)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_215)
        self.label_37.setObjectName(u"label_37")
        sizePolicy4.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy4)
        self.label_37.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_112.addWidget(self.label_37)

        self.pushButton_anhsang_14 = QPushButton(self.widget_215)
        self.pushButton_anhsang_14.setObjectName(u"pushButton_anhsang_14")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_14.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_14.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_14.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_14.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_14.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_14.setIconSize(QSize(16, 16))

        self.horizontalLayout_112.addWidget(self.pushButton_anhsang_14)


        self.verticalLayout_109.addWidget(self.widget_215)

        self.widget_216 = QWidget(self.widget_214)
        self.widget_216.setObjectName(u"widget_216")
        sizePolicy3.setHeightForWidth(self.widget_216.sizePolicy().hasHeightForWidth())
        self.widget_216.setSizePolicy(sizePolicy3)
        self.horizontalLayout_113 = QHBoxLayout(self.widget_216)
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.widget_217 = QWidget(self.widget_216)
        self.widget_217.setObjectName(u"widget_217")
        sizePolicy3.setHeightForWidth(self.widget_217.sizePolicy().hasHeightForWidth())
        self.widget_217.setSizePolicy(sizePolicy3)
        self.verticalLayout_110 = QVBoxLayout(self.widget_217)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 30, 0)
        self.widget_218 = QWidget(self.widget_217)
        self.widget_218.setObjectName(u"widget_218")
        sizePolicy.setHeightForWidth(self.widget_218.sizePolicy().hasHeightForWidth())
        self.widget_218.setSizePolicy(sizePolicy)
        self.verticalLayout_111 = QVBoxLayout(self.widget_218)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 0, 0, 20)
        self.label_14 = QLabel(self.widget_218)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"")
        self.label_14.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_14.setScaledContents(True)

        self.verticalLayout_111.addWidget(self.label_14)


        self.verticalLayout_110.addWidget(self.widget_218)

        self.widget_219 = QWidget(self.widget_217)
        self.widget_219.setObjectName(u"widget_219")
        sizePolicy3.setHeightForWidth(self.widget_219.sizePolicy().hasHeightForWidth())
        self.widget_219.setSizePolicy(sizePolicy3)
        self.horizontalLayout_114 = QHBoxLayout(self.widget_219)
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.widget_220 = QWidget(self.widget_219)
        self.widget_220.setObjectName(u"widget_220")
        self.verticalLayout_112 = QVBoxLayout(self.widget_220)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.widget_221 = QWidget(self.widget_220)
        self.widget_221.setObjectName(u"widget_221")
        self.horizontalLayout_115 = QHBoxLayout(self.widget_221)
        self.horizontalLayout_115.setSpacing(0)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_6 = QPushButton(self.widget_221)
        self.pushButton_ac1_6.setObjectName(u"pushButton_ac1_6")
        sizePolicy4.setHeightForWidth(self.pushButton_ac1_6.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_6.setSizePolicy(sizePolicy4)
        self.pushButton_ac1_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_115.addWidget(self.pushButton_ac1_6)


        self.verticalLayout_112.addWidget(self.widget_221)

        self.widget_222 = QWidget(self.widget_220)
        self.widget_222.setObjectName(u"widget_222")
        self.verticalLayout_113 = QVBoxLayout(self.widget_222)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.widget_222)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_113.addWidget(self.label_38)


        self.verticalLayout_112.addWidget(self.widget_222)


        self.horizontalLayout_114.addWidget(self.widget_220)

        self.widget_223 = QWidget(self.widget_219)
        self.widget_223.setObjectName(u"widget_223")
        self.verticalLayout_114 = QVBoxLayout(self.widget_223)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.widget_233 = QWidget(self.widget_223)
        self.widget_233.setObjectName(u"widget_233")
        self.horizontalLayout_116 = QHBoxLayout(self.widget_233)
        self.horizontalLayout_116.setSpacing(0)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_6 = QPushButton(self.widget_233)
        self.pushButton_ac2_6.setObjectName(u"pushButton_ac2_6")
        sizePolicy4.setHeightForWidth(self.pushButton_ac2_6.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_6.setSizePolicy(sizePolicy4)
        self.pushButton_ac2_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_116.addWidget(self.pushButton_ac2_6)


        self.verticalLayout_114.addWidget(self.widget_233)

        self.widget_234 = QWidget(self.widget_223)
        self.widget_234.setObjectName(u"widget_234")
        self.verticalLayout_115 = QVBoxLayout(self.widget_234)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.widget_234)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_115.addWidget(self.label_39)


        self.verticalLayout_114.addWidget(self.widget_234)


        self.horizontalLayout_114.addWidget(self.widget_223)


        self.verticalLayout_110.addWidget(self.widget_219)


        self.horizontalLayout_113.addWidget(self.widget_217)

        self.widget_235 = QWidget(self.widget_216)
        self.widget_235.setObjectName(u"widget_235")
        sizePolicy.setHeightForWidth(self.widget_235.sizePolicy().hasHeightForWidth())
        self.widget_235.setSizePolicy(sizePolicy)
        self.widget_235.setStyleSheet(u"padding-right:30px;")
        self.verticalLayout_116 = QVBoxLayout(self.widget_235)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.widget_236 = QWidget(self.widget_235)
        self.widget_236.setObjectName(u"widget_236")
        sizePolicy3.setHeightForWidth(self.widget_236.sizePolicy().hasHeightForWidth())
        self.widget_236.setSizePolicy(sizePolicy3)
        self.widget_236.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_117 = QHBoxLayout(self.widget_236)
        self.horizontalLayout_117.setSpacing(0)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.widget_237 = QWidget(self.widget_236)
        self.widget_237.setObjectName(u"widget_237")
        sizePolicy4.setHeightForWidth(self.widget_237.sizePolicy().hasHeightForWidth())
        self.widget_237.setSizePolicy(sizePolicy4)
        self.widget_237.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_118 = QHBoxLayout(self.widget_237)
        self.horizontalLayout_118.setSpacing(0)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_26 = QPushButton(self.widget_237)
        self.pushButton_nhietdo_26.setObjectName(u"pushButton_nhietdo_26")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_26.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_26.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_26.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_26.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_26.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_26.setIconSize(QSize(16, 16))

        self.horizontalLayout_118.addWidget(self.pushButton_nhietdo_26)


        self.horizontalLayout_117.addWidget(self.widget_237)

        self.widget_238 = QWidget(self.widget_236)
        self.widget_238.setObjectName(u"widget_238")
        self.verticalLayout_117 = QVBoxLayout(self.widget_238)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_28 = QLabel(self.widget_238)
        self.label_nhietdo_28.setObjectName(u"label_nhietdo_28")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_28.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_28.setSizePolicy(sizePolicy3)
        self.label_nhietdo_28.setFont(font2)
        self.label_nhietdo_28.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_117.addWidget(self.label_nhietdo_28)


        self.horizontalLayout_117.addWidget(self.widget_238)


        self.verticalLayout_116.addWidget(self.widget_236)

        self.widget_239 = QWidget(self.widget_235)
        self.widget_239.setObjectName(u"widget_239")
        sizePolicy3.setHeightForWidth(self.widget_239.sizePolicy().hasHeightForWidth())
        self.widget_239.setSizePolicy(sizePolicy3)
        self.horizontalLayout_119 = QHBoxLayout(self.widget_239)
        self.horizontalLayout_119.setSpacing(0)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.widget_240 = QWidget(self.widget_239)
        self.widget_240.setObjectName(u"widget_240")
        sizePolicy3.setHeightForWidth(self.widget_240.sizePolicy().hasHeightForWidth())
        self.widget_240.setSizePolicy(sizePolicy3)
        self.widget_240.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_120 = QHBoxLayout(self.widget_240)
        self.horizontalLayout_120.setSpacing(0)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.widget_241 = QWidget(self.widget_240)
        self.widget_241.setObjectName(u"widget_241")
        sizePolicy4.setHeightForWidth(self.widget_241.sizePolicy().hasHeightForWidth())
        self.widget_241.setSizePolicy(sizePolicy4)
        self.widget_241.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_121 = QHBoxLayout(self.widget_241)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_27 = QPushButton(self.widget_241)
        self.pushButton_nhietdo_27.setObjectName(u"pushButton_nhietdo_27")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_27.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_27.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_27.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_27.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_27.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_27.setIconSize(QSize(16, 16))

        self.horizontalLayout_121.addWidget(self.pushButton_nhietdo_27)


        self.horizontalLayout_120.addWidget(self.widget_241)

        self.widget_242 = QWidget(self.widget_240)
        self.widget_242.setObjectName(u"widget_242")
        self.verticalLayout_118 = QVBoxLayout(self.widget_242)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_29 = QLabel(self.widget_242)
        self.label_nhietdo_29.setObjectName(u"label_nhietdo_29")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_29.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_29.setSizePolicy(sizePolicy3)
        self.label_nhietdo_29.setFont(font2)
        self.label_nhietdo_29.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_118.addWidget(self.label_nhietdo_29)


        self.horizontalLayout_120.addWidget(self.widget_242)


        self.horizontalLayout_119.addWidget(self.widget_240)


        self.verticalLayout_116.addWidget(self.widget_239)

        self.widget_243 = QWidget(self.widget_235)
        self.widget_243.setObjectName(u"widget_243")
        sizePolicy3.setHeightForWidth(self.widget_243.sizePolicy().hasHeightForWidth())
        self.widget_243.setSizePolicy(sizePolicy3)
        self.horizontalLayout_122 = QHBoxLayout(self.widget_243)
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.widget_244 = QWidget(self.widget_243)
        self.widget_244.setObjectName(u"widget_244")
        sizePolicy3.setHeightForWidth(self.widget_244.sizePolicy().hasHeightForWidth())
        self.widget_244.setSizePolicy(sizePolicy3)
        self.widget_244.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_123 = QHBoxLayout(self.widget_244)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.widget_245 = QWidget(self.widget_244)
        self.widget_245.setObjectName(u"widget_245")
        sizePolicy4.setHeightForWidth(self.widget_245.sizePolicy().hasHeightForWidth())
        self.widget_245.setSizePolicy(sizePolicy4)
        self.widget_245.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_124 = QHBoxLayout(self.widget_245)
        self.horizontalLayout_124.setSpacing(0)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_28 = QPushButton(self.widget_245)
        self.pushButton_nhietdo_28.setObjectName(u"pushButton_nhietdo_28")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_28.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_28.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_28.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_28.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_28.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_28.setIconSize(QSize(16, 16))

        self.horizontalLayout_124.addWidget(self.pushButton_nhietdo_28)


        self.horizontalLayout_123.addWidget(self.widget_245)

        self.widget_246 = QWidget(self.widget_244)
        self.widget_246.setObjectName(u"widget_246")
        self.verticalLayout_119 = QVBoxLayout(self.widget_246)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_30 = QLabel(self.widget_246)
        self.label_nhietdo_30.setObjectName(u"label_nhietdo_30")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_30.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_30.setSizePolicy(sizePolicy3)
        self.label_nhietdo_30.setFont(font2)
        self.label_nhietdo_30.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_119.addWidget(self.label_nhietdo_30)


        self.horizontalLayout_123.addWidget(self.widget_246)


        self.horizontalLayout_122.addWidget(self.widget_244)


        self.verticalLayout_116.addWidget(self.widget_243)

        self.widget_247 = QWidget(self.widget_235)
        self.widget_247.setObjectName(u"widget_247")
        sizePolicy4.setHeightForWidth(self.widget_247.sizePolicy().hasHeightForWidth())
        self.widget_247.setSizePolicy(sizePolicy4)
        self.horizontalLayout_125 = QHBoxLayout(self.widget_247)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.widget_248 = QWidget(self.widget_247)
        self.widget_248.setObjectName(u"widget_248")
        sizePolicy3.setHeightForWidth(self.widget_248.sizePolicy().hasHeightForWidth())
        self.widget_248.setSizePolicy(sizePolicy3)
        self.widget_248.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_126 = QHBoxLayout(self.widget_248)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.widget_249 = QWidget(self.widget_248)
        self.widget_249.setObjectName(u"widget_249")
        sizePolicy4.setHeightForWidth(self.widget_249.sizePolicy().hasHeightForWidth())
        self.widget_249.setSizePolicy(sizePolicy4)
        self.widget_249.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_127 = QHBoxLayout(self.widget_249)
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_29 = QPushButton(self.widget_249)
        self.pushButton_nhietdo_29.setObjectName(u"pushButton_nhietdo_29")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_29.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_29.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_29.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_29.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_29.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_29.setIconSize(QSize(16, 16))

        self.horizontalLayout_127.addWidget(self.pushButton_nhietdo_29)


        self.horizontalLayout_126.addWidget(self.widget_249)

        self.widget_250 = QWidget(self.widget_248)
        self.widget_250.setObjectName(u"widget_250")
        self.verticalLayout_120 = QVBoxLayout(self.widget_250)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_31 = QLabel(self.widget_250)
        self.label_nhietdo_31.setObjectName(u"label_nhietdo_31")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_31.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_31.setSizePolicy(sizePolicy3)
        self.label_nhietdo_31.setFont(font2)
        self.label_nhietdo_31.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_120.addWidget(self.label_nhietdo_31)


        self.horizontalLayout_126.addWidget(self.widget_250)


        self.horizontalLayout_125.addWidget(self.widget_248)


        self.verticalLayout_116.addWidget(self.widget_247)

        self.widget_251 = QWidget(self.widget_235)
        self.widget_251.setObjectName(u"widget_251")
        sizePolicy3.setHeightForWidth(self.widget_251.sizePolicy().hasHeightForWidth())
        self.widget_251.setSizePolicy(sizePolicy3)
        self.widget_251.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_128 = QHBoxLayout(self.widget_251)
        self.horizontalLayout_128.setSpacing(0)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.widget_252 = QWidget(self.widget_251)
        self.widget_252.setObjectName(u"widget_252")
        sizePolicy3.setHeightForWidth(self.widget_252.sizePolicy().hasHeightForWidth())
        self.widget_252.setSizePolicy(sizePolicy3)
        self.widget_252.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_129 = QHBoxLayout(self.widget_252)
        self.horizontalLayout_129.setSpacing(0)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.widget_336 = QWidget(self.widget_252)
        self.widget_336.setObjectName(u"widget_336")
        sizePolicy4.setHeightForWidth(self.widget_336.sizePolicy().hasHeightForWidth())
        self.widget_336.setSizePolicy(sizePolicy4)
        self.widget_336.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_177 = QHBoxLayout(self.widget_336)
        self.horizontalLayout_177.setSpacing(0)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_30 = QPushButton(self.widget_336)
        self.pushButton_nhietdo_30.setObjectName(u"pushButton_nhietdo_30")
        sizePolicy1.setHeightForWidth(self.pushButton_nhietdo_30.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_30.setSizePolicy(sizePolicy1)
        self.pushButton_nhietdo_30.setMinimumSize(QSize(50, 28))
        self.pushButton_nhietdo_30.setMaximumSize(QSize(50, 28))
        self.pushButton_nhietdo_30.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_30.setIconSize(QSize(16, 16))

        self.horizontalLayout_177.addWidget(self.pushButton_nhietdo_30)


        self.horizontalLayout_129.addWidget(self.widget_336)

        self.widget_337 = QWidget(self.widget_252)
        self.widget_337.setObjectName(u"widget_337")
        self.verticalLayout_187 = QVBoxLayout(self.widget_337)
        self.verticalLayout_187.setSpacing(0)
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.verticalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.label_nhietdo_32 = QLabel(self.widget_337)
        self.label_nhietdo_32.setObjectName(u"label_nhietdo_32")
        sizePolicy3.setHeightForWidth(self.label_nhietdo_32.sizePolicy().hasHeightForWidth())
        self.label_nhietdo_32.setSizePolicy(sizePolicy3)
        self.label_nhietdo_32.setFont(font2)
        self.label_nhietdo_32.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_187.addWidget(self.label_nhietdo_32)


        self.horizontalLayout_129.addWidget(self.widget_337)


        self.horizontalLayout_128.addWidget(self.widget_252)


        self.verticalLayout_116.addWidget(self.widget_251)


        self.horizontalLayout_113.addWidget(self.widget_235)


        self.verticalLayout_109.addWidget(self.widget_216)


        self.verticalLayout_108.addWidget(self.widget_214)


        self.horizontalLayout_60.addWidget(self.widget_213)


        self.verticalLayout_25.addWidget(self.lisTram_2)


        self.verticalLayout_19.addWidget(self.widget_10)


        self.verticalLayout_34.addWidget(self.widget_8)

        self.label_3 = QLabel(self.home)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Segoe UI\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.home)
        self.Nhietdo_2 = QWidget()
        self.Nhietdo_2.setObjectName(u"Nhietdo_2")
        self.verticalLayout_156 = QVBoxLayout(self.Nhietdo_2)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.Nhietdo_widget_2 = QWidget(self.Nhietdo_2)
        self.Nhietdo_widget_2.setObjectName(u"Nhietdo_widget_2")
        self.Nhietdo_widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_154 = QVBoxLayout(self.Nhietdo_widget_2)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.title_nhietdo_2 = QLabel(self.Nhietdo_widget_2)
        self.title_nhietdo_2.setObjectName(u"title_nhietdo_2")
        sizePolicy3.setHeightForWidth(self.title_nhietdo_2.sizePolicy().hasHeightForWidth())
        self.title_nhietdo_2.setSizePolicy(sizePolicy3)
        self.title_nhietdo_2.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.title_nhietdo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_154.addWidget(self.title_nhietdo_2)

        self.thoigian_nhietdo_2 = QLabel(self.Nhietdo_widget_2)
        self.thoigian_nhietdo_2.setObjectName(u"thoigian_nhietdo_2")
        sizePolicy3.setHeightForWidth(self.thoigian_nhietdo_2.sizePolicy().hasHeightForWidth())
        self.thoigian_nhietdo_2.setSizePolicy(sizePolicy3)
        self.thoigian_nhietdo_2.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.thoigian_nhietdo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_154.addWidget(self.thoigian_nhietdo_2)

        self.widget_259 = QWidget(self.Nhietdo_widget_2)
        self.widget_259.setObjectName(u"widget_259")
        sizePolicy.setHeightForWidth(self.widget_259.sizePolicy().hasHeightForWidth())
        self.widget_259.setSizePolicy(sizePolicy)
        self.widget_259.setMinimumSize(QSize(0, 0))
        self.gridLayout_5 = QGridLayout(self.widget_259)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_19, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.screen_nhietdo_2 = QVBoxLayout()
        self.screen_nhietdo_2.setSpacing(0)
        self.screen_nhietdo_2.setObjectName(u"screen_nhietdo_2")
        self.screen_nhietdo_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.screen_nhietdo_2.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_5.addLayout(self.screen_nhietdo_2, 1, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_20, 1, 0, 1, 1)


        self.verticalLayout_154.addWidget(self.widget_259)


        self.verticalLayout_156.addWidget(self.Nhietdo_widget_2)

        self.stackedWidget.addWidget(self.Nhietdo_2)
        self.Nhietdo = QWidget()
        self.Nhietdo.setObjectName(u"Nhietdo")
        self.verticalLayout_153 = QVBoxLayout(self.Nhietdo)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.Nhietdo_widget = QWidget(self.Nhietdo)
        self.Nhietdo_widget.setObjectName(u"Nhietdo_widget")
        self.Nhietdo_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_20 = QVBoxLayout(self.Nhietdo_widget)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.title_nhietdo = QLabel(self.Nhietdo_widget)
        self.title_nhietdo.setObjectName(u"title_nhietdo")
        sizePolicy3.setHeightForWidth(self.title_nhietdo.sizePolicy().hasHeightForWidth())
        self.title_nhietdo.setSizePolicy(sizePolicy3)
        self.title_nhietdo.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.title_nhietdo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.title_nhietdo)

        self.thoigian_nhietdo = QLabel(self.Nhietdo_widget)
        self.thoigian_nhietdo.setObjectName(u"thoigian_nhietdo")
        sizePolicy3.setHeightForWidth(self.thoigian_nhietdo.sizePolicy().hasHeightForWidth())
        self.thoigian_nhietdo.setSizePolicy(sizePolicy3)
        self.thoigian_nhietdo.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.thoigian_nhietdo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.thoigian_nhietdo)

        self.widget_78 = QWidget(self.Nhietdo_widget)
        self.widget_78.setObjectName(u"widget_78")
        sizePolicy.setHeightForWidth(self.widget_78.sizePolicy().hasHeightForWidth())
        self.widget_78.setSizePolicy(sizePolicy)
        self.widget_78.setMinimumSize(QSize(0, 0))
        self.gridLayout_4 = QGridLayout(self.widget_78)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_17, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.screen_nhietdo = QVBoxLayout()
        self.screen_nhietdo.setSpacing(0)
        self.screen_nhietdo.setObjectName(u"screen_nhietdo")
        self.screen_nhietdo.setSizeConstraint(QLayout.SetMaximumSize)
        self.screen_nhietdo.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_4.addLayout(self.screen_nhietdo, 1, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_18, 1, 0, 1, 1)


        self.verticalLayout_20.addWidget(self.widget_78)


        self.verticalLayout_153.addWidget(self.Nhietdo_widget)

        self.stackedWidget.addWidget(self.Nhietdo)
        self.Doam = QWidget()
        self.Doam.setObjectName(u"Doam")
        self.Doam.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_68 = QVBoxLayout(self.Doam)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.widget_Doam = QWidget(self.Doam)
        self.widget_Doam.setObjectName(u"widget_Doam")
        self.widget_Doam.setStyleSheet(u"")
        self.verticalLayout_66 = QVBoxLayout(self.widget_Doam)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.widget_label_doam = QWidget(self.widget_Doam)
        self.widget_label_doam.setObjectName(u"widget_label_doam")
        sizePolicy.setHeightForWidth(self.widget_label_doam.sizePolicy().hasHeightForWidth())
        self.widget_label_doam.setSizePolicy(sizePolicy)
        self.widget_label_doam.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_doam.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_67 = QVBoxLayout(self.widget_label_doam)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_doam = QLabel(self.widget_label_doam)
        self.label_doam.setObjectName(u"label_doam")
        sizePolicy3.setHeightForWidth(self.label_doam.sizePolicy().hasHeightForWidth())
        self.label_doam.setSizePolicy(sizePolicy3)
        self.label_doam.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_doam.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_doam)

        self.label_thoigian_doam = QLabel(self.widget_label_doam)
        self.label_thoigian_doam.setObjectName(u"label_thoigian_doam")
        sizePolicy3.setHeightForWidth(self.label_thoigian_doam.sizePolicy().hasHeightForWidth())
        self.label_thoigian_doam.setSizePolicy(sizePolicy3)
        self.label_thoigian_doam.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_doam.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_thoigian_doam)

        self.screen_doam = QVBoxLayout()
        self.screen_doam.setSpacing(0)
        self.screen_doam.setObjectName(u"screen_doam")
        self.screen_doam.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_67.addLayout(self.screen_doam)


        self.verticalLayout_66.addWidget(self.widget_label_doam)


        self.verticalLayout_68.addWidget(self.widget_Doam)

        self.stackedWidget.addWidget(self.Doam)
        self.Doam_2 = QWidget()
        self.Doam_2.setObjectName(u"Doam_2")
        self.verticalLayout_159 = QVBoxLayout(self.Doam_2)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.widget_Doam_2 = QWidget(self.Doam_2)
        self.widget_Doam_2.setObjectName(u"widget_Doam_2")
        self.widget_Doam_2.setStyleSheet(u"")
        self.verticalLayout_157 = QVBoxLayout(self.widget_Doam_2)
        self.verticalLayout_157.setSpacing(0)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.widget_label_doam_2 = QWidget(self.widget_Doam_2)
        self.widget_label_doam_2.setObjectName(u"widget_label_doam_2")
        sizePolicy.setHeightForWidth(self.widget_label_doam_2.sizePolicy().hasHeightForWidth())
        self.widget_label_doam_2.setSizePolicy(sizePolicy)
        self.widget_label_doam_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_doam_2.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_158 = QVBoxLayout(self.widget_label_doam_2)
        self.verticalLayout_158.setSpacing(0)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.label_doam_4 = QLabel(self.widget_label_doam_2)
        self.label_doam_4.setObjectName(u"label_doam_4")
        sizePolicy3.setHeightForWidth(self.label_doam_4.sizePolicy().hasHeightForWidth())
        self.label_doam_4.setSizePolicy(sizePolicy3)
        self.label_doam_4.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_doam_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_158.addWidget(self.label_doam_4)

        self.label_thoigian_doam_2 = QLabel(self.widget_label_doam_2)
        self.label_thoigian_doam_2.setObjectName(u"label_thoigian_doam_2")
        sizePolicy3.setHeightForWidth(self.label_thoigian_doam_2.sizePolicy().hasHeightForWidth())
        self.label_thoigian_doam_2.setSizePolicy(sizePolicy3)
        self.label_thoigian_doam_2.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_doam_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_158.addWidget(self.label_thoigian_doam_2)

        self.screen_doam_2 = QVBoxLayout()
        self.screen_doam_2.setSpacing(0)
        self.screen_doam_2.setObjectName(u"screen_doam_2")
        self.screen_doam_2.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_158.addLayout(self.screen_doam_2)


        self.verticalLayout_157.addWidget(self.widget_label_doam_2)


        self.verticalLayout_159.addWidget(self.widget_Doam_2)

        self.stackedWidget.addWidget(self.Doam_2)
        self.doam_3 = QWidget()
        self.doam_3.setObjectName(u"doam_3")
        self.verticalLayout_356 = QVBoxLayout(self.doam_3)
        self.verticalLayout_356.setSpacing(0)
        self.verticalLayout_356.setObjectName(u"verticalLayout_356")
        self.verticalLayout_356.setContentsMargins(0, 0, 0, 0)
        self.widget_Doam_5 = QWidget(self.doam_3)
        self.widget_Doam_5.setObjectName(u"widget_Doam_5")
        self.widget_Doam_5.setStyleSheet(u"")
        self.verticalLayout_354 = QVBoxLayout(self.widget_Doam_5)
        self.verticalLayout_354.setSpacing(0)
        self.verticalLayout_354.setObjectName(u"verticalLayout_354")
        self.verticalLayout_354.setContentsMargins(0, 0, 0, 0)
        self.widget_label_doam_5 = QWidget(self.widget_Doam_5)
        self.widget_label_doam_5.setObjectName(u"widget_label_doam_5")
        sizePolicy.setHeightForWidth(self.widget_label_doam_5.sizePolicy().hasHeightForWidth())
        self.widget_label_doam_5.setSizePolicy(sizePolicy)
        self.widget_label_doam_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_doam_5.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_355 = QVBoxLayout(self.widget_label_doam_5)
        self.verticalLayout_355.setSpacing(0)
        self.verticalLayout_355.setObjectName(u"verticalLayout_355")
        self.verticalLayout_355.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_355.setContentsMargins(0, 0, 0, 0)
        self.label_doam_9 = QLabel(self.widget_label_doam_5)
        self.label_doam_9.setObjectName(u"label_doam_9")
        sizePolicy3.setHeightForWidth(self.label_doam_9.sizePolicy().hasHeightForWidth())
        self.label_doam_9.setSizePolicy(sizePolicy3)
        self.label_doam_9.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_doam_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_355.addWidget(self.label_doam_9)

        self.label_thoigian_doam_5 = QLabel(self.widget_label_doam_5)
        self.label_thoigian_doam_5.setObjectName(u"label_thoigian_doam_5")
        sizePolicy3.setHeightForWidth(self.label_thoigian_doam_5.sizePolicy().hasHeightForWidth())
        self.label_thoigian_doam_5.setSizePolicy(sizePolicy3)
        self.label_thoigian_doam_5.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_doam_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_355.addWidget(self.label_thoigian_doam_5)

        self.screen_doam_5 = QVBoxLayout()
        self.screen_doam_5.setSpacing(0)
        self.screen_doam_5.setObjectName(u"screen_doam_5")
        self.screen_doam_5.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_355.addLayout(self.screen_doam_5)


        self.verticalLayout_354.addWidget(self.widget_label_doam_5)


        self.verticalLayout_356.addWidget(self.widget_Doam_5)

        self.stackedWidget.addWidget(self.doam_3)
        self.Dienap = QWidget()
        self.Dienap.setObjectName(u"Dienap")
        self.verticalLayout_81 = QVBoxLayout(self.Dienap)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.widget_Dienap = QWidget(self.Dienap)
        self.widget_Dienap.setObjectName(u"widget_Dienap")
        self.widget_Dienap.setStyleSheet(u"")
        self.verticalLayout_69 = QVBoxLayout(self.widget_Dienap)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.widget_label_dienap = QWidget(self.widget_Dienap)
        self.widget_label_dienap.setObjectName(u"widget_label_dienap")
        sizePolicy.setHeightForWidth(self.widget_label_dienap.sizePolicy().hasHeightForWidth())
        self.widget_label_dienap.setSizePolicy(sizePolicy)
        self.widget_label_dienap.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_dienap.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_70 = QVBoxLayout(self.widget_label_dienap)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_diepap = QLabel(self.widget_label_dienap)
        self.label_diepap.setObjectName(u"label_diepap")
        sizePolicy3.setHeightForWidth(self.label_diepap.sizePolicy().hasHeightForWidth())
        self.label_diepap.setSizePolicy(sizePolicy3)
        self.label_diepap.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_diepap.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.label_diepap)

        self.label_thoigian_dienap = QLabel(self.widget_label_dienap)
        self.label_thoigian_dienap.setObjectName(u"label_thoigian_dienap")
        sizePolicy3.setHeightForWidth(self.label_thoigian_dienap.sizePolicy().hasHeightForWidth())
        self.label_thoigian_dienap.setSizePolicy(sizePolicy3)
        self.label_thoigian_dienap.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_dienap.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.label_thoigian_dienap)

        self.screen_dienap = QVBoxLayout()
        self.screen_dienap.setSpacing(0)
        self.screen_dienap.setObjectName(u"screen_dienap")
        self.screen_dienap.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_70.addLayout(self.screen_dienap)

        self.screen_dienap_2 = QVBoxLayout()
        self.screen_dienap_2.setSpacing(0)
        self.screen_dienap_2.setObjectName(u"screen_dienap_2")
        self.screen_dienap_2.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_70.addLayout(self.screen_dienap_2)


        self.verticalLayout_69.addWidget(self.widget_label_dienap)


        self.verticalLayout_81.addWidget(self.widget_Dienap)

        self.stackedWidget.addWidget(self.Dienap)
        self.suco = QWidget()
        self.suco.setObjectName(u"suco")
        self.verticalLayout_7 = QVBoxLayout(self.suco)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_271 = QWidget(self.suco)
        self.widget_271.setObjectName(u"widget_271")
        self.gridLayout_2 = QGridLayout(self.widget_271)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_272 = QWidget(self.widget_271)
        self.widget_272.setObjectName(u"widget_272")
        sizePolicy.setHeightForWidth(self.widget_272.sizePolicy().hasHeightForWidth())
        self.widget_272.setSizePolicy(sizePolicy)
        self.widget_272.setAutoFillBackground(False)
        self.widget_272.setStyleSheet(u"text-align: center;")
        self.verticalLayout_166 = QVBoxLayout(self.widget_272)
        self.verticalLayout_166.setSpacing(0)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.widget_272)
        self.label_43.setObjectName(u"label_43")
        sizePolicy3.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy3)
        self.label_43.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_166.addWidget(self.label_43)

        self.widget_273 = QWidget(self.widget_272)
        self.widget_273.setObjectName(u"widget_273")
        sizePolicy.setHeightForWidth(self.widget_273.sizePolicy().hasHeightForWidth())
        self.widget_273.setSizePolicy(sizePolicy)
        self.verticalLayout_175 = QVBoxLayout(self.widget_273)
        self.verticalLayout_175.setSpacing(0)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.verticalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_nhietdo_3 = QTableWidget(self.widget_273)
        if (self.tableWidget_nhietdo_3.columnCount() < 3):
            self.tableWidget_nhietdo_3.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_nhietdo_3.rowCount() < 9):
            self.tableWidget_nhietdo_3.setRowCount(9)
        font3 = QFont()
        font3.setBold(True)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_nhietdo_3.setVerticalHeaderItem(8, __qtablewidgetitem11)
        self.tableWidget_nhietdo_3.setObjectName(u"tableWidget_nhietdo_3")
        sizePolicy.setHeightForWidth(self.tableWidget_nhietdo_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_nhietdo_3.setSizePolicy(sizePolicy)
        self.tableWidget_nhietdo_3.setMinimumSize(QSize(400, 0))
        self.tableWidget_nhietdo_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_nhietdo_3.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_3.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_nhietdo_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_nhietdo_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_nhietdo_3.verticalHeader().setVisible(False)
        self.tableWidget_nhietdo_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_nhietdo_3.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_3.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_175.addWidget(self.tableWidget_nhietdo_3)


        self.verticalLayout_166.addWidget(self.widget_273)

        self.widget_274 = QWidget(self.widget_272)
        self.widget_274.setObjectName(u"widget_274")
        sizePolicy3.setHeightForWidth(self.widget_274.sizePolicy().hasHeightForWidth())
        self.widget_274.setSizePolicy(sizePolicy3)
        self.horizontalLayout_137 = QHBoxLayout(self.widget_274)
        self.horizontalLayout_137.setSpacing(0)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_3 = QPushButton(self.widget_274)
        self.pushButton_exportTem_3.setObjectName(u"pushButton_exportTem_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_3.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_3.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_137.addWidget(self.pushButton_exportTem_3)


        self.verticalLayout_166.addWidget(self.widget_274)


        self.gridLayout_2.addWidget(self.widget_272, 0, 0, 1, 1)

        self.widget_275 = QWidget(self.widget_271)
        self.widget_275.setObjectName(u"widget_275")
        self.verticalLayout_167 = QVBoxLayout(self.widget_275)
        self.verticalLayout_167.setSpacing(0)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalLayout_167.setContentsMargins(0, 0, 0, 0)
        self.widget_276 = QWidget(self.widget_275)
        self.widget_276.setObjectName(u"widget_276")
        sizePolicy.setHeightForWidth(self.widget_276.sizePolicy().hasHeightForWidth())
        self.widget_276.setSizePolicy(sizePolicy)
        self.widget_276.setAutoFillBackground(False)
        self.widget_276.setStyleSheet(u"text-align: center;")
        self.verticalLayout_176 = QVBoxLayout(self.widget_276)
        self.verticalLayout_176.setSpacing(0)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.verticalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.widget_276)
        self.label_49.setObjectName(u"label_49")
        sizePolicy3.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy3)
        self.label_49.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.verticalLayout_176.addWidget(self.label_49)

        self.widget_286 = QWidget(self.widget_276)
        self.widget_286.setObjectName(u"widget_286")
        sizePolicy.setHeightForWidth(self.widget_286.sizePolicy().hasHeightForWidth())
        self.widget_286.setSizePolicy(sizePolicy)
        self.verticalLayout_193 = QVBoxLayout(self.widget_286)
        self.verticalLayout_193.setSpacing(0)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.verticalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc1_3 = QTableWidget(self.widget_286)
        if (self.tableWidget_dc1_3.columnCount() < 3):
            self.tableWidget_dc1_3.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_dc1_3.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_dc1_3.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_dc1_3.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        if (self.tableWidget_dc1_3.rowCount() < 9):
            self.tableWidget_dc1_3.setRowCount(9)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font3);
        self.tableWidget_dc1_3.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_dc1_3.setVerticalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_dc1_3.setVerticalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_dc1_3.setVerticalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_dc1_3.setVerticalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_dc1_3.setVerticalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_dc1_3.setVerticalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_dc1_3.setVerticalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_dc1_3.setVerticalHeaderItem(8, __qtablewidgetitem23)
        self.tableWidget_dc1_3.setObjectName(u"tableWidget_dc1_3")
        sizePolicy.setHeightForWidth(self.tableWidget_dc1_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc1_3.setSizePolicy(sizePolicy)
        self.tableWidget_dc1_3.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc1_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc1_3.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_3.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc1_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc1_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc1_3.verticalHeader().setVisible(False)
        self.tableWidget_dc1_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc1_3.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_3.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_193.addWidget(self.tableWidget_dc1_3)


        self.verticalLayout_176.addWidget(self.widget_286)

        self.widget_287 = QWidget(self.widget_276)
        self.widget_287.setObjectName(u"widget_287")
        sizePolicy3.setHeightForWidth(self.widget_287.sizePolicy().hasHeightForWidth())
        self.widget_287.setSizePolicy(sizePolicy3)
        self.horizontalLayout_143 = QHBoxLayout(self.widget_287)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_9 = QPushButton(self.widget_287)
        self.pushButton_exportTem_9.setObjectName(u"pushButton_exportTem_9")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_9.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_9.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_9.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_143.addWidget(self.pushButton_exportTem_9)


        self.verticalLayout_176.addWidget(self.widget_287)


        self.verticalLayout_167.addWidget(self.widget_276)


        self.gridLayout_2.addWidget(self.widget_275, 0, 1, 1, 1)

        self.widget_289 = QWidget(self.widget_271)
        self.widget_289.setObjectName(u"widget_289")
        sizePolicy.setHeightForWidth(self.widget_289.sizePolicy().hasHeightForWidth())
        self.widget_289.setSizePolicy(sizePolicy)
        self.widget_289.setAutoFillBackground(False)
        self.widget_289.setStyleSheet(u"text-align: center;")
        self.verticalLayout_177 = QVBoxLayout(self.widget_289)
        self.verticalLayout_177.setSpacing(0)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.verticalLayout_177.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.widget_289)
        self.label_50.setObjectName(u"label_50")
        sizePolicy3.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy3)
        self.label_50.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_177.addWidget(self.label_50)

        self.widget_290 = QWidget(self.widget_289)
        self.widget_290.setObjectName(u"widget_290")
        sizePolicy.setHeightForWidth(self.widget_290.sizePolicy().hasHeightForWidth())
        self.widget_290.setSizePolicy(sizePolicy)
        self.verticalLayout_194 = QVBoxLayout(self.widget_290)
        self.verticalLayout_194.setSpacing(0)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.verticalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac1_2 = QTableWidget(self.widget_290)
        if (self.tableWidget_ac1_2.columnCount() < 3):
            self.tableWidget_ac1_2.setColumnCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_ac1_2.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_ac1_2.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_ac1_2.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        if (self.tableWidget_ac1_2.rowCount() < 9):
            self.tableWidget_ac1_2.setRowCount(9)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font3);
        self.tableWidget_ac1_2.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_ac1_2.setVerticalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_ac1_2.setVerticalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_ac1_2.setVerticalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_ac1_2.setVerticalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_ac1_2.setVerticalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_ac1_2.setVerticalHeaderItem(6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_ac1_2.setVerticalHeaderItem(7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_ac1_2.setVerticalHeaderItem(8, __qtablewidgetitem35)
        self.tableWidget_ac1_2.setObjectName(u"tableWidget_ac1_2")
        sizePolicy.setHeightForWidth(self.tableWidget_ac1_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac1_2.setSizePolicy(sizePolicy)
        self.tableWidget_ac1_2.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac1_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac1_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_2.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac1_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac1_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac1_2.verticalHeader().setVisible(False)
        self.tableWidget_ac1_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac1_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_2.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_194.addWidget(self.tableWidget_ac1_2)


        self.verticalLayout_177.addWidget(self.widget_290)

        self.widget_291 = QWidget(self.widget_289)
        self.widget_291.setObjectName(u"widget_291")
        sizePolicy3.setHeightForWidth(self.widget_291.sizePolicy().hasHeightForWidth())
        self.widget_291.setSizePolicy(sizePolicy3)
        self.horizontalLayout_144 = QHBoxLayout(self.widget_291)
        self.horizontalLayout_144.setSpacing(0)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_10 = QPushButton(self.widget_291)
        self.pushButton_exportTem_10.setObjectName(u"pushButton_exportTem_10")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_10.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_10.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_10.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_144.addWidget(self.pushButton_exportTem_10)


        self.verticalLayout_177.addWidget(self.widget_291)


        self.gridLayout_2.addWidget(self.widget_289, 0, 2, 1, 1)

        self.widget_292 = QWidget(self.widget_271)
        self.widget_292.setObjectName(u"widget_292")
        sizePolicy.setHeightForWidth(self.widget_292.sizePolicy().hasHeightForWidth())
        self.widget_292.setSizePolicy(sizePolicy)
        self.widget_292.setAutoFillBackground(False)
        self.widget_292.setStyleSheet(u"text-align: center;")
        self.verticalLayout_178 = QVBoxLayout(self.widget_292)
        self.verticalLayout_178.setSpacing(0)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.widget_292)
        self.label_51.setObjectName(u"label_51")
        sizePolicy3.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy3)
        self.label_51.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.verticalLayout_178.addWidget(self.label_51)

        self.widget_311 = QWidget(self.widget_292)
        self.widget_311.setObjectName(u"widget_311")
        sizePolicy.setHeightForWidth(self.widget_311.sizePolicy().hasHeightForWidth())
        self.widget_311.setSizePolicy(sizePolicy)
        self.verticalLayout_195 = QVBoxLayout(self.widget_311)
        self.verticalLayout_195.setSpacing(0)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.verticalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_doam_3 = QTableWidget(self.widget_311)
        if (self.tableWidget_doam_3.columnCount() < 3):
            self.tableWidget_doam_3.setColumnCount(3)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_doam_3.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_doam_3.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_doam_3.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        if (self.tableWidget_doam_3.rowCount() < 9):
            self.tableWidget_doam_3.setRowCount(9)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font3);
        self.tableWidget_doam_3.setVerticalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_doam_3.setVerticalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_doam_3.setVerticalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_doam_3.setVerticalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_doam_3.setVerticalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_doam_3.setVerticalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_doam_3.setVerticalHeaderItem(6, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_doam_3.setVerticalHeaderItem(7, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_doam_3.setVerticalHeaderItem(8, __qtablewidgetitem47)
        self.tableWidget_doam_3.setObjectName(u"tableWidget_doam_3")
        sizePolicy.setHeightForWidth(self.tableWidget_doam_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_doam_3.setSizePolicy(sizePolicy)
        self.tableWidget_doam_3.setMinimumSize(QSize(400, 0))
        self.tableWidget_doam_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_doam_3.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_3.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_doam_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_doam_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_doam_3.verticalHeader().setVisible(False)
        self.tableWidget_doam_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_doam_3.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_3.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_195.addWidget(self.tableWidget_doam_3)


        self.verticalLayout_178.addWidget(self.widget_311)

        self.widget_312 = QWidget(self.widget_292)
        self.widget_312.setObjectName(u"widget_312")
        sizePolicy3.setHeightForWidth(self.widget_312.sizePolicy().hasHeightForWidth())
        self.widget_312.setSizePolicy(sizePolicy3)
        self.horizontalLayout_145 = QHBoxLayout(self.widget_312)
        self.horizontalLayout_145.setSpacing(0)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_11 = QPushButton(self.widget_312)
        self.pushButton_exportTem_11.setObjectName(u"pushButton_exportTem_11")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_11.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_11.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_11.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_145.addWidget(self.pushButton_exportTem_11)


        self.verticalLayout_178.addWidget(self.widget_312)


        self.gridLayout_2.addWidget(self.widget_292, 1, 0, 1, 1)

        self.widget_313 = QWidget(self.widget_271)
        self.widget_313.setObjectName(u"widget_313")
        sizePolicy.setHeightForWidth(self.widget_313.sizePolicy().hasHeightForWidth())
        self.widget_313.setSizePolicy(sizePolicy)
        self.widget_313.setAutoFillBackground(False)
        self.widget_313.setStyleSheet(u"text-align: center;")
        self.verticalLayout_179 = QVBoxLayout(self.widget_313)
        self.verticalLayout_179.setSpacing(0)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.verticalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.widget_313)
        self.label_54.setObjectName(u"label_54")
        sizePolicy3.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy3)
        self.label_54.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.verticalLayout_179.addWidget(self.label_54)

        self.widget_314 = QWidget(self.widget_313)
        self.widget_314.setObjectName(u"widget_314")
        sizePolicy.setHeightForWidth(self.widget_314.sizePolicy().hasHeightForWidth())
        self.widget_314.setSizePolicy(sizePolicy)
        self.verticalLayout_196 = QVBoxLayout(self.widget_314)
        self.verticalLayout_196.setSpacing(0)
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.verticalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc2_3 = QTableWidget(self.widget_314)
        if (self.tableWidget_dc2_3.columnCount() < 3):
            self.tableWidget_dc2_3.setColumnCount(3)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_dc2_3.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_dc2_3.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_dc2_3.setHorizontalHeaderItem(2, __qtablewidgetitem50)
        if (self.tableWidget_dc2_3.rowCount() < 9):
            self.tableWidget_dc2_3.setRowCount(9)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font3);
        self.tableWidget_dc2_3.setVerticalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_dc2_3.setVerticalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_dc2_3.setVerticalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_dc2_3.setVerticalHeaderItem(3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_dc2_3.setVerticalHeaderItem(4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_dc2_3.setVerticalHeaderItem(5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_dc2_3.setVerticalHeaderItem(6, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_dc2_3.setVerticalHeaderItem(7, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_dc2_3.setVerticalHeaderItem(8, __qtablewidgetitem59)
        self.tableWidget_dc2_3.setObjectName(u"tableWidget_dc2_3")
        sizePolicy.setHeightForWidth(self.tableWidget_dc2_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc2_3.setSizePolicy(sizePolicy)
        self.tableWidget_dc2_3.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc2_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc2_3.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_3.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc2_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc2_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc2_3.verticalHeader().setVisible(False)
        self.tableWidget_dc2_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc2_3.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_3.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_196.addWidget(self.tableWidget_dc2_3)


        self.verticalLayout_179.addWidget(self.widget_314)

        self.widget_315 = QWidget(self.widget_313)
        self.widget_315.setObjectName(u"widget_315")
        sizePolicy3.setHeightForWidth(self.widget_315.sizePolicy().hasHeightForWidth())
        self.widget_315.setSizePolicy(sizePolicy3)
        self.horizontalLayout_156 = QHBoxLayout(self.widget_315)
        self.horizontalLayout_156.setSpacing(0)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_14 = QPushButton(self.widget_315)
        self.pushButton_exportTem_14.setObjectName(u"pushButton_exportTem_14")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_14.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_14.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_14.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_156.addWidget(self.pushButton_exportTem_14)


        self.verticalLayout_179.addWidget(self.widget_315)


        self.gridLayout_2.addWidget(self.widget_313, 1, 1, 1, 1)

        self.widget_316 = QWidget(self.widget_271)
        self.widget_316.setObjectName(u"widget_316")
        sizePolicy.setHeightForWidth(self.widget_316.sizePolicy().hasHeightForWidth())
        self.widget_316.setSizePolicy(sizePolicy)
        self.widget_316.setAutoFillBackground(False)
        self.widget_316.setStyleSheet(u"text-align: center;")
        self.verticalLayout_180 = QVBoxLayout(self.widget_316)
        self.verticalLayout_180.setSpacing(0)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.verticalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.widget_316)
        self.label_55.setObjectName(u"label_55")
        sizePolicy3.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy3)
        self.label_55.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.verticalLayout_180.addWidget(self.label_55)

        self.widget_317 = QWidget(self.widget_316)
        self.widget_317.setObjectName(u"widget_317")
        sizePolicy.setHeightForWidth(self.widget_317.sizePolicy().hasHeightForWidth())
        self.widget_317.setSizePolicy(sizePolicy)
        self.verticalLayout_197 = QVBoxLayout(self.widget_317)
        self.verticalLayout_197.setSpacing(0)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.verticalLayout_197.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac2_2 = QTableWidget(self.widget_317)
        if (self.tableWidget_ac2_2.columnCount() < 3):
            self.tableWidget_ac2_2.setColumnCount(3)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_ac2_2.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_ac2_2.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_ac2_2.setHorizontalHeaderItem(2, __qtablewidgetitem62)
        if (self.tableWidget_ac2_2.rowCount() < 9):
            self.tableWidget_ac2_2.setRowCount(9)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font3);
        self.tableWidget_ac2_2.setVerticalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_ac2_2.setVerticalHeaderItem(1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_ac2_2.setVerticalHeaderItem(2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_ac2_2.setVerticalHeaderItem(3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_ac2_2.setVerticalHeaderItem(4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_ac2_2.setVerticalHeaderItem(5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_ac2_2.setVerticalHeaderItem(6, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_ac2_2.setVerticalHeaderItem(7, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_ac2_2.setVerticalHeaderItem(8, __qtablewidgetitem71)
        self.tableWidget_ac2_2.setObjectName(u"tableWidget_ac2_2")
        sizePolicy.setHeightForWidth(self.tableWidget_ac2_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac2_2.setSizePolicy(sizePolicy)
        self.tableWidget_ac2_2.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac2_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac2_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_2.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac2_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac2_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac2_2.verticalHeader().setVisible(False)
        self.tableWidget_ac2_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac2_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_2.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_197.addWidget(self.tableWidget_ac2_2)


        self.verticalLayout_180.addWidget(self.widget_317)

        self.widget_318 = QWidget(self.widget_316)
        self.widget_318.setObjectName(u"widget_318")
        sizePolicy3.setHeightForWidth(self.widget_318.sizePolicy().hasHeightForWidth())
        self.widget_318.setSizePolicy(sizePolicy3)
        self.horizontalLayout_157 = QHBoxLayout(self.widget_318)
        self.horizontalLayout_157.setSpacing(0)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_15 = QPushButton(self.widget_318)
        self.pushButton_exportTem_15.setObjectName(u"pushButton_exportTem_15")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_15.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_15.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_15.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_157.addWidget(self.pushButton_exportTem_15)


        self.verticalLayout_180.addWidget(self.widget_318)


        self.gridLayout_2.addWidget(self.widget_316, 1, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_271)

        self.stackedWidget.addWidget(self.suco)
        self.Dienap_2 = QWidget()
        self.Dienap_2.setObjectName(u"Dienap_2")
        self.verticalLayout_165 = QVBoxLayout(self.Dienap_2)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.widget_Dienap_2 = QWidget(self.Dienap_2)
        self.widget_Dienap_2.setObjectName(u"widget_Dienap_2")
        self.widget_Dienap_2.setStyleSheet(u"")
        self.verticalLayout_162 = QVBoxLayout(self.widget_Dienap_2)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(0, 0, 0, 0)
        self.widget_label_dienap_2 = QWidget(self.widget_Dienap_2)
        self.widget_label_dienap_2.setObjectName(u"widget_label_dienap_2")
        sizePolicy.setHeightForWidth(self.widget_label_dienap_2.sizePolicy().hasHeightForWidth())
        self.widget_label_dienap_2.setSizePolicy(sizePolicy)
        self.widget_label_dienap_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_dienap_2.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_164 = QVBoxLayout(self.widget_label_dienap_2)
        self.verticalLayout_164.setSpacing(0)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.label_diepap_2 = QLabel(self.widget_label_dienap_2)
        self.label_diepap_2.setObjectName(u"label_diepap_2")
        sizePolicy3.setHeightForWidth(self.label_diepap_2.sizePolicy().hasHeightForWidth())
        self.label_diepap_2.setSizePolicy(sizePolicy3)
        self.label_diepap_2.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_diepap_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_164.addWidget(self.label_diepap_2)

        self.label_thoigian_dienap_2 = QLabel(self.widget_label_dienap_2)
        self.label_thoigian_dienap_2.setObjectName(u"label_thoigian_dienap_2")
        sizePolicy3.setHeightForWidth(self.label_thoigian_dienap_2.sizePolicy().hasHeightForWidth())
        self.label_thoigian_dienap_2.setSizePolicy(sizePolicy3)
        self.label_thoigian_dienap_2.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_dienap_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_164.addWidget(self.label_thoigian_dienap_2)

        self.screen_dienap_3 = QVBoxLayout()
        self.screen_dienap_3.setSpacing(0)
        self.screen_dienap_3.setObjectName(u"screen_dienap_3")
        self.screen_dienap_3.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_164.addLayout(self.screen_dienap_3)

        self.screen_dienap_4 = QVBoxLayout()
        self.screen_dienap_4.setSpacing(0)
        self.screen_dienap_4.setObjectName(u"screen_dienap_4")
        self.screen_dienap_4.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_164.addLayout(self.screen_dienap_4)


        self.verticalLayout_162.addWidget(self.widget_label_dienap_2)


        self.verticalLayout_165.addWidget(self.widget_Dienap_2)

        self.stackedWidget.addWidget(self.Dienap_2)
        self.suco_2 = QWidget()
        self.suco_2.setObjectName(u"suco_2")
        self.verticalLayout = QVBoxLayout(self.suco_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_260 = QWidget(self.suco_2)
        self.widget_260.setObjectName(u"widget_260")
        self.gridLayout = QGridLayout(self.widget_260)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_267 = QWidget(self.widget_260)
        self.widget_267.setObjectName(u"widget_267")
        sizePolicy.setHeightForWidth(self.widget_267.sizePolicy().hasHeightForWidth())
        self.widget_267.setSizePolicy(sizePolicy)
        self.widget_267.setAutoFillBackground(False)
        self.widget_267.setStyleSheet(u"text-align: center;")
        self.verticalLayout_163 = QVBoxLayout(self.widget_267)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.widget_267)
        self.label_42.setObjectName(u"label_42")
        sizePolicy3.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy3)
        self.label_42.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_163.addWidget(self.label_42)

        self.widget_268 = QWidget(self.widget_267)
        self.widget_268.setObjectName(u"widget_268")
        sizePolicy.setHeightForWidth(self.widget_268.sizePolicy().hasHeightForWidth())
        self.widget_268.setSizePolicy(sizePolicy)
        self.verticalLayout_174 = QVBoxLayout(self.widget_268)
        self.verticalLayout_174.setSpacing(0)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.verticalLayout_174.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_nhietdo_2 = QTableWidget(self.widget_268)
        if (self.tableWidget_nhietdo_2.columnCount() < 3):
            self.tableWidget_nhietdo_2.setColumnCount(3)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setHorizontalHeaderItem(0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setHorizontalHeaderItem(1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setHorizontalHeaderItem(2, __qtablewidgetitem74)
        if (self.tableWidget_nhietdo_2.rowCount() < 9):
            self.tableWidget_nhietdo_2.setRowCount(9)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFont(font3);
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(4, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(5, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(6, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(7, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_nhietdo_2.setVerticalHeaderItem(8, __qtablewidgetitem83)
        self.tableWidget_nhietdo_2.setObjectName(u"tableWidget_nhietdo_2")
        sizePolicy.setHeightForWidth(self.tableWidget_nhietdo_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_nhietdo_2.setSizePolicy(sizePolicy)
        self.tableWidget_nhietdo_2.setMinimumSize(QSize(400, 0))
        self.tableWidget_nhietdo_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_nhietdo_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_2.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_nhietdo_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_nhietdo_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_nhietdo_2.verticalHeader().setVisible(False)
        self.tableWidget_nhietdo_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_nhietdo_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_2.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_174.addWidget(self.tableWidget_nhietdo_2)


        self.verticalLayout_163.addWidget(self.widget_268)

        self.widget_269 = QWidget(self.widget_267)
        self.widget_269.setObjectName(u"widget_269")
        sizePolicy3.setHeightForWidth(self.widget_269.sizePolicy().hasHeightForWidth())
        self.widget_269.setSizePolicy(sizePolicy3)
        self.horizontalLayout_136 = QHBoxLayout(self.widget_269)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_2 = QPushButton(self.widget_269)
        self.pushButton_exportTem_2.setObjectName(u"pushButton_exportTem_2")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_2.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_2.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_136.addWidget(self.pushButton_exportTem_2)


        self.verticalLayout_163.addWidget(self.widget_269)


        self.gridLayout.addWidget(self.widget_267, 0, 0, 1, 1)

        self.widget_261 = QWidget(self.widget_260)
        self.widget_261.setObjectName(u"widget_261")
        self.verticalLayout_161 = QVBoxLayout(self.widget_261)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.widget_270 = QWidget(self.widget_261)
        self.widget_270.setObjectName(u"widget_270")
        sizePolicy.setHeightForWidth(self.widget_270.sizePolicy().hasHeightForWidth())
        self.widget_270.setSizePolicy(sizePolicy)
        self.widget_270.setAutoFillBackground(False)
        self.widget_270.setStyleSheet(u"text-align: center;")
        self.verticalLayout_173 = QVBoxLayout(self.widget_270)
        self.verticalLayout_173.setSpacing(0)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.verticalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.widget_270)
        self.label_46.setObjectName(u"label_46")
        sizePolicy3.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy3)
        self.label_46.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_173.addWidget(self.label_46)

        self.widget_277 = QWidget(self.widget_270)
        self.widget_277.setObjectName(u"widget_277")
        sizePolicy.setHeightForWidth(self.widget_277.sizePolicy().hasHeightForWidth())
        self.widget_277.setSizePolicy(sizePolicy)
        self.verticalLayout_181 = QVBoxLayout(self.widget_277)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc1_2 = QTableWidget(self.widget_277)
        if (self.tableWidget_dc1_2.columnCount() < 3):
            self.tableWidget_dc1_2.setColumnCount(3)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_dc1_2.setHorizontalHeaderItem(0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_dc1_2.setHorizontalHeaderItem(1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_dc1_2.setHorizontalHeaderItem(2, __qtablewidgetitem86)
        if (self.tableWidget_dc1_2.rowCount() < 9):
            self.tableWidget_dc1_2.setRowCount(9)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setFont(font3);
        self.tableWidget_dc1_2.setVerticalHeaderItem(0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_dc1_2.setVerticalHeaderItem(1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_dc1_2.setVerticalHeaderItem(2, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_dc1_2.setVerticalHeaderItem(3, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_dc1_2.setVerticalHeaderItem(4, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_dc1_2.setVerticalHeaderItem(5, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_dc1_2.setVerticalHeaderItem(6, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_dc1_2.setVerticalHeaderItem(7, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_dc1_2.setVerticalHeaderItem(8, __qtablewidgetitem95)
        self.tableWidget_dc1_2.setObjectName(u"tableWidget_dc1_2")
        sizePolicy.setHeightForWidth(self.tableWidget_dc1_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc1_2.setSizePolicy(sizePolicy)
        self.tableWidget_dc1_2.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc1_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc1_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_2.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc1_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc1_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc1_2.verticalHeader().setVisible(False)
        self.tableWidget_dc1_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc1_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_2.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_181.addWidget(self.tableWidget_dc1_2)


        self.verticalLayout_173.addWidget(self.widget_277)

        self.widget_278 = QWidget(self.widget_270)
        self.widget_278.setObjectName(u"widget_278")
        sizePolicy3.setHeightForWidth(self.widget_278.sizePolicy().hasHeightForWidth())
        self.widget_278.setSizePolicy(sizePolicy3)
        self.horizontalLayout_140 = QHBoxLayout(self.widget_278)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_6 = QPushButton(self.widget_278)
        self.pushButton_exportTem_6.setObjectName(u"pushButton_exportTem_6")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_6.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_6.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_6.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_140.addWidget(self.pushButton_exportTem_6)


        self.verticalLayout_173.addWidget(self.widget_278)


        self.verticalLayout_161.addWidget(self.widget_270)


        self.gridLayout.addWidget(self.widget_261, 0, 1, 1, 1)

        self.widget_279 = QWidget(self.widget_260)
        self.widget_279.setObjectName(u"widget_279")
        sizePolicy.setHeightForWidth(self.widget_279.sizePolicy().hasHeightForWidth())
        self.widget_279.setSizePolicy(sizePolicy)
        self.widget_279.setAutoFillBackground(False)
        self.widget_279.setStyleSheet(u"text-align: center;")
        self.verticalLayout_169 = QVBoxLayout(self.widget_279)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.widget_279)
        self.label_47.setObjectName(u"label_47")
        sizePolicy3.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy3)
        self.label_47.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_169.addWidget(self.label_47)

        self.widget_280 = QWidget(self.widget_279)
        self.widget_280.setObjectName(u"widget_280")
        sizePolicy.setHeightForWidth(self.widget_280.sizePolicy().hasHeightForWidth())
        self.widget_280.setSizePolicy(sizePolicy)
        self.verticalLayout_185 = QVBoxLayout(self.widget_280)
        self.verticalLayout_185.setSpacing(0)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.verticalLayout_185.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac1 = QTableWidget(self.widget_280)
        if (self.tableWidget_ac1.columnCount() < 3):
            self.tableWidget_ac1.setColumnCount(3)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_ac1.setHorizontalHeaderItem(0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_ac1.setHorizontalHeaderItem(1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_ac1.setHorizontalHeaderItem(2, __qtablewidgetitem98)
        if (self.tableWidget_ac1.rowCount() < 9):
            self.tableWidget_ac1.setRowCount(9)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setFont(font3);
        self.tableWidget_ac1.setVerticalHeaderItem(0, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_ac1.setVerticalHeaderItem(1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_ac1.setVerticalHeaderItem(2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_ac1.setVerticalHeaderItem(3, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_ac1.setVerticalHeaderItem(4, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_ac1.setVerticalHeaderItem(5, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_ac1.setVerticalHeaderItem(6, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_ac1.setVerticalHeaderItem(7, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_ac1.setVerticalHeaderItem(8, __qtablewidgetitem107)
        self.tableWidget_ac1.setObjectName(u"tableWidget_ac1")
        sizePolicy.setHeightForWidth(self.tableWidget_ac1.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac1.setSizePolicy(sizePolicy)
        self.tableWidget_ac1.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac1.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac1.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac1.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac1.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac1.verticalHeader().setVisible(False)
        self.tableWidget_ac1.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac1.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_185.addWidget(self.tableWidget_ac1)


        self.verticalLayout_169.addWidget(self.widget_280)

        self.widget_281 = QWidget(self.widget_279)
        self.widget_281.setObjectName(u"widget_281")
        sizePolicy3.setHeightForWidth(self.widget_281.sizePolicy().hasHeightForWidth())
        self.widget_281.setSizePolicy(sizePolicy3)
        self.horizontalLayout_141 = QHBoxLayout(self.widget_281)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_7 = QPushButton(self.widget_281)
        self.pushButton_exportTem_7.setObjectName(u"pushButton_exportTem_7")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_7.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_7.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_7.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_141.addWidget(self.pushButton_exportTem_7)


        self.verticalLayout_169.addWidget(self.widget_281)


        self.gridLayout.addWidget(self.widget_279, 0, 2, 1, 1)

        self.widget_282 = QWidget(self.widget_260)
        self.widget_282.setObjectName(u"widget_282")
        sizePolicy.setHeightForWidth(self.widget_282.sizePolicy().hasHeightForWidth())
        self.widget_282.setSizePolicy(sizePolicy)
        self.widget_282.setAutoFillBackground(False)
        self.widget_282.setStyleSheet(u"text-align: center;")
        self.verticalLayout_170 = QVBoxLayout(self.widget_282)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.widget_282)
        self.label_48.setObjectName(u"label_48")
        sizePolicy3.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy3)
        self.label_48.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_170.addWidget(self.label_48)

        self.widget_283 = QWidget(self.widget_282)
        self.widget_283.setObjectName(u"widget_283")
        sizePolicy.setHeightForWidth(self.widget_283.sizePolicy().hasHeightForWidth())
        self.widget_283.setSizePolicy(sizePolicy)
        self.verticalLayout_182 = QVBoxLayout(self.widget_283)
        self.verticalLayout_182.setSpacing(0)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.verticalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_doam_2 = QTableWidget(self.widget_283)
        if (self.tableWidget_doam_2.columnCount() < 3):
            self.tableWidget_doam_2.setColumnCount(3)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_doam_2.setHorizontalHeaderItem(0, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_doam_2.setHorizontalHeaderItem(1, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_doam_2.setHorizontalHeaderItem(2, __qtablewidgetitem110)
        if (self.tableWidget_doam_2.rowCount() < 9):
            self.tableWidget_doam_2.setRowCount(9)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setFont(font3);
        self.tableWidget_doam_2.setVerticalHeaderItem(0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_doam_2.setVerticalHeaderItem(1, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_doam_2.setVerticalHeaderItem(2, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_doam_2.setVerticalHeaderItem(3, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_doam_2.setVerticalHeaderItem(4, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_doam_2.setVerticalHeaderItem(5, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_doam_2.setVerticalHeaderItem(6, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_doam_2.setVerticalHeaderItem(7, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_doam_2.setVerticalHeaderItem(8, __qtablewidgetitem119)
        self.tableWidget_doam_2.setObjectName(u"tableWidget_doam_2")
        sizePolicy.setHeightForWidth(self.tableWidget_doam_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_doam_2.setSizePolicy(sizePolicy)
        self.tableWidget_doam_2.setMinimumSize(QSize(400, 0))
        self.tableWidget_doam_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_doam_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_2.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_doam_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_doam_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_doam_2.verticalHeader().setVisible(False)
        self.tableWidget_doam_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_doam_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_2.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_182.addWidget(self.tableWidget_doam_2)


        self.verticalLayout_170.addWidget(self.widget_283)

        self.widget_284 = QWidget(self.widget_282)
        self.widget_284.setObjectName(u"widget_284")
        sizePolicy3.setHeightForWidth(self.widget_284.sizePolicy().hasHeightForWidth())
        self.widget_284.setSizePolicy(sizePolicy3)
        self.horizontalLayout_142 = QHBoxLayout(self.widget_284)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_8 = QPushButton(self.widget_284)
        self.pushButton_exportTem_8.setObjectName(u"pushButton_exportTem_8")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_8.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_8.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_8.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_142.addWidget(self.pushButton_exportTem_8)


        self.verticalLayout_170.addWidget(self.widget_284)


        self.gridLayout.addWidget(self.widget_282, 1, 0, 1, 1)

        self.widget_285 = QWidget(self.widget_260)
        self.widget_285.setObjectName(u"widget_285")
        sizePolicy.setHeightForWidth(self.widget_285.sizePolicy().hasHeightForWidth())
        self.widget_285.setSizePolicy(sizePolicy)
        self.widget_285.setAutoFillBackground(False)
        self.widget_285.setStyleSheet(u"text-align: center;")
        self.verticalLayout_171 = QVBoxLayout(self.widget_285)
        self.verticalLayout_171.setSpacing(0)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.widget_285)
        self.label_52.setObjectName(u"label_52")
        sizePolicy3.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy3)
        self.label_52.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.verticalLayout_171.addWidget(self.label_52)

        self.widget_288 = QWidget(self.widget_285)
        self.widget_288.setObjectName(u"widget_288")
        sizePolicy.setHeightForWidth(self.widget_288.sizePolicy().hasHeightForWidth())
        self.widget_288.setSizePolicy(sizePolicy)
        self.verticalLayout_183 = QVBoxLayout(self.widget_288)
        self.verticalLayout_183.setSpacing(0)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.verticalLayout_183.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc2_2 = QTableWidget(self.widget_288)
        if (self.tableWidget_dc2_2.columnCount() < 3):
            self.tableWidget_dc2_2.setColumnCount(3)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_dc2_2.setHorizontalHeaderItem(0, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_dc2_2.setHorizontalHeaderItem(1, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_dc2_2.setHorizontalHeaderItem(2, __qtablewidgetitem122)
        if (self.tableWidget_dc2_2.rowCount() < 9):
            self.tableWidget_dc2_2.setRowCount(9)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setFont(font3);
        self.tableWidget_dc2_2.setVerticalHeaderItem(0, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_dc2_2.setVerticalHeaderItem(1, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_dc2_2.setVerticalHeaderItem(2, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_dc2_2.setVerticalHeaderItem(3, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_dc2_2.setVerticalHeaderItem(4, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_dc2_2.setVerticalHeaderItem(5, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_dc2_2.setVerticalHeaderItem(6, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget_dc2_2.setVerticalHeaderItem(7, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_dc2_2.setVerticalHeaderItem(8, __qtablewidgetitem131)
        self.tableWidget_dc2_2.setObjectName(u"tableWidget_dc2_2")
        sizePolicy.setHeightForWidth(self.tableWidget_dc2_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc2_2.setSizePolicy(sizePolicy)
        self.tableWidget_dc2_2.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc2_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc2_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_2.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc2_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc2_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc2_2.verticalHeader().setVisible(False)
        self.tableWidget_dc2_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc2_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_2.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_183.addWidget(self.tableWidget_dc2_2)


        self.verticalLayout_171.addWidget(self.widget_288)

        self.widget_293 = QWidget(self.widget_285)
        self.widget_293.setObjectName(u"widget_293")
        sizePolicy3.setHeightForWidth(self.widget_293.sizePolicy().hasHeightForWidth())
        self.widget_293.setSizePolicy(sizePolicy3)
        self.horizontalLayout_146 = QHBoxLayout(self.widget_293)
        self.horizontalLayout_146.setSpacing(0)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_12 = QPushButton(self.widget_293)
        self.pushButton_exportTem_12.setObjectName(u"pushButton_exportTem_12")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_12.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_12.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_12.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_146.addWidget(self.pushButton_exportTem_12)


        self.verticalLayout_171.addWidget(self.widget_293)


        self.gridLayout.addWidget(self.widget_285, 1, 1, 1, 1)

        self.widget_294 = QWidget(self.widget_260)
        self.widget_294.setObjectName(u"widget_294")
        sizePolicy.setHeightForWidth(self.widget_294.sizePolicy().hasHeightForWidth())
        self.widget_294.setSizePolicy(sizePolicy)
        self.widget_294.setAutoFillBackground(False)
        self.widget_294.setStyleSheet(u"text-align: center;")
        self.verticalLayout_172 = QVBoxLayout(self.widget_294)
        self.verticalLayout_172.setSpacing(0)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.verticalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.widget_294)
        self.label_53.setObjectName(u"label_53")
        sizePolicy3.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy3)
        self.label_53.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.verticalLayout_172.addWidget(self.label_53)

        self.widget_295 = QWidget(self.widget_294)
        self.widget_295.setObjectName(u"widget_295")
        sizePolicy.setHeightForWidth(self.widget_295.sizePolicy().hasHeightForWidth())
        self.widget_295.setSizePolicy(sizePolicy)
        self.verticalLayout_184 = QVBoxLayout(self.widget_295)
        self.verticalLayout_184.setSpacing(0)
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.verticalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac2 = QTableWidget(self.widget_295)
        if (self.tableWidget_ac2.columnCount() < 3):
            self.tableWidget_ac2.setColumnCount(3)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_ac2.setHorizontalHeaderItem(0, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_ac2.setHorizontalHeaderItem(1, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_ac2.setHorizontalHeaderItem(2, __qtablewidgetitem134)
        if (self.tableWidget_ac2.rowCount() < 9):
            self.tableWidget_ac2.setRowCount(9)
        __qtablewidgetitem135 = QTableWidgetItem()
        __qtablewidgetitem135.setFont(font3);
        self.tableWidget_ac2.setVerticalHeaderItem(0, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget_ac2.setVerticalHeaderItem(1, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_ac2.setVerticalHeaderItem(2, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_ac2.setVerticalHeaderItem(3, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_ac2.setVerticalHeaderItem(4, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_ac2.setVerticalHeaderItem(5, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_ac2.setVerticalHeaderItem(6, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_ac2.setVerticalHeaderItem(7, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_ac2.setVerticalHeaderItem(8, __qtablewidgetitem143)
        self.tableWidget_ac2.setObjectName(u"tableWidget_ac2")
        sizePolicy.setHeightForWidth(self.tableWidget_ac2.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac2.setSizePolicy(sizePolicy)
        self.tableWidget_ac2.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac2.verticalHeader().setVisible(False)
        self.tableWidget_ac2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_184.addWidget(self.tableWidget_ac2)


        self.verticalLayout_172.addWidget(self.widget_295)

        self.widget_296 = QWidget(self.widget_294)
        self.widget_296.setObjectName(u"widget_296")
        sizePolicy3.setHeightForWidth(self.widget_296.sizePolicy().hasHeightForWidth())
        self.widget_296.setSizePolicy(sizePolicy3)
        self.horizontalLayout_147 = QHBoxLayout(self.widget_296)
        self.horizontalLayout_147.setSpacing(0)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_13 = QPushButton(self.widget_296)
        self.pushButton_exportTem_13.setObjectName(u"pushButton_exportTem_13")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_13.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_13.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_13.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_147.addWidget(self.pushButton_exportTem_13)


        self.verticalLayout_172.addWidget(self.widget_296)


        self.gridLayout.addWidget(self.widget_294, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget_260)

        self.stackedWidget.addWidget(self.suco_2)
        self.nhietdo_3 = QWidget()
        self.nhietdo_3.setObjectName(u"nhietdo_3")
        self.verticalLayout_198 = QVBoxLayout(self.nhietdo_3)
        self.verticalLayout_198.setSpacing(0)
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.verticalLayout_198.setContentsMargins(0, 0, 0, 0)
        self.Nhietdo_widget_3 = QWidget(self.nhietdo_3)
        self.Nhietdo_widget_3.setObjectName(u"Nhietdo_widget_3")
        self.Nhietdo_widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_168 = QVBoxLayout(self.Nhietdo_widget_3)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.title_nhietdo_3 = QLabel(self.Nhietdo_widget_3)
        self.title_nhietdo_3.setObjectName(u"title_nhietdo_3")
        sizePolicy3.setHeightForWidth(self.title_nhietdo_3.sizePolicy().hasHeightForWidth())
        self.title_nhietdo_3.setSizePolicy(sizePolicy3)
        self.title_nhietdo_3.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.title_nhietdo_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_168.addWidget(self.title_nhietdo_3)

        self.thoigian_nhietdo_3 = QLabel(self.Nhietdo_widget_3)
        self.thoigian_nhietdo_3.setObjectName(u"thoigian_nhietdo_3")
        sizePolicy3.setHeightForWidth(self.thoigian_nhietdo_3.sizePolicy().hasHeightForWidth())
        self.thoigian_nhietdo_3.setSizePolicy(sizePolicy3)
        self.thoigian_nhietdo_3.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.thoigian_nhietdo_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_168.addWidget(self.thoigian_nhietdo_3)

        self.widget_324 = QWidget(self.Nhietdo_widget_3)
        self.widget_324.setObjectName(u"widget_324")
        sizePolicy.setHeightForWidth(self.widget_324.sizePolicy().hasHeightForWidth())
        self.widget_324.setSizePolicy(sizePolicy)
        self.widget_324.setMinimumSize(QSize(0, 0))
        self.gridLayout_6 = QGridLayout(self.widget_324)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_21, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.screen_nhietdo_3 = QVBoxLayout()
        self.screen_nhietdo_3.setSpacing(0)
        self.screen_nhietdo_3.setObjectName(u"screen_nhietdo_3")
        self.screen_nhietdo_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.screen_nhietdo_3.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_6.addLayout(self.screen_nhietdo_3, 1, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_22, 1, 0, 1, 1)


        self.verticalLayout_168.addWidget(self.widget_324)


        self.verticalLayout_198.addWidget(self.Nhietdo_widget_3)

        self.stackedWidget.addWidget(self.nhietdo_3)
        self.dienap_3 = QWidget()
        self.dienap_3.setObjectName(u"dienap_3")
        self.verticalLayout_211 = QVBoxLayout(self.dienap_3)
        self.verticalLayout_211.setSpacing(0)
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.verticalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.widget_Dienap_3 = QWidget(self.dienap_3)
        self.widget_Dienap_3.setObjectName(u"widget_Dienap_3")
        self.widget_Dienap_3.setStyleSheet(u"")
        self.verticalLayout_209 = QVBoxLayout(self.widget_Dienap_3)
        self.verticalLayout_209.setSpacing(0)
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.verticalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.widget_label_dienap_3 = QWidget(self.widget_Dienap_3)
        self.widget_label_dienap_3.setObjectName(u"widget_label_dienap_3")
        sizePolicy.setHeightForWidth(self.widget_label_dienap_3.sizePolicy().hasHeightForWidth())
        self.widget_label_dienap_3.setSizePolicy(sizePolicy)
        self.widget_label_dienap_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_dienap_3.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_210 = QVBoxLayout(self.widget_label_dienap_3)
        self.verticalLayout_210.setSpacing(0)
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.verticalLayout_210.setContentsMargins(0, 0, 0, 0)
        self.label_diepap_3 = QLabel(self.widget_label_dienap_3)
        self.label_diepap_3.setObjectName(u"label_diepap_3")
        sizePolicy3.setHeightForWidth(self.label_diepap_3.sizePolicy().hasHeightForWidth())
        self.label_diepap_3.setSizePolicy(sizePolicy3)
        self.label_diepap_3.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_diepap_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_210.addWidget(self.label_diepap_3)

        self.label_thoigian_dienap_3 = QLabel(self.widget_label_dienap_3)
        self.label_thoigian_dienap_3.setObjectName(u"label_thoigian_dienap_3")
        sizePolicy3.setHeightForWidth(self.label_thoigian_dienap_3.sizePolicy().hasHeightForWidth())
        self.label_thoigian_dienap_3.setSizePolicy(sizePolicy3)
        self.label_thoigian_dienap_3.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_dienap_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_210.addWidget(self.label_thoigian_dienap_3)

        self.screen_dienap_5 = QVBoxLayout()
        self.screen_dienap_5.setSpacing(0)
        self.screen_dienap_5.setObjectName(u"screen_dienap_5")
        self.screen_dienap_5.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_210.addLayout(self.screen_dienap_5)

        self.screen_dienap_6 = QVBoxLayout()
        self.screen_dienap_6.setSpacing(0)
        self.screen_dienap_6.setObjectName(u"screen_dienap_6")
        self.screen_dienap_6.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_210.addLayout(self.screen_dienap_6)


        self.verticalLayout_209.addWidget(self.widget_label_dienap_3)


        self.verticalLayout_211.addWidget(self.widget_Dienap_3)

        self.stackedWidget.addWidget(self.dienap_3)
        self.suco_3 = QWidget()
        self.suco_3.setObjectName(u"suco_3")
        self.verticalLayout_234 = QVBoxLayout(self.suco_3)
        self.verticalLayout_234.setSpacing(0)
        self.verticalLayout_234.setObjectName(u"verticalLayout_234")
        self.verticalLayout_234.setContentsMargins(0, 0, 0, 0)
        self.widget_327 = QWidget(self.suco_3)
        self.widget_327.setObjectName(u"widget_327")
        self.gridLayout_3 = QGridLayout(self.widget_327)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_328 = QWidget(self.widget_327)
        self.widget_328.setObjectName(u"widget_328")
        sizePolicy.setHeightForWidth(self.widget_328.sizePolicy().hasHeightForWidth())
        self.widget_328.setSizePolicy(sizePolicy)
        self.widget_328.setAutoFillBackground(False)
        self.widget_328.setStyleSheet(u"text-align: center;")
        self.verticalLayout_221 = QVBoxLayout(self.widget_328)
        self.verticalLayout_221.setSpacing(0)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.verticalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.widget_328)
        self.label_44.setObjectName(u"label_44")
        sizePolicy3.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy3)
        self.label_44.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_221.addWidget(self.label_44)

        self.widget_329 = QWidget(self.widget_328)
        self.widget_329.setObjectName(u"widget_329")
        sizePolicy.setHeightForWidth(self.widget_329.sizePolicy().hasHeightForWidth())
        self.widget_329.setSizePolicy(sizePolicy)
        self.verticalLayout_222 = QVBoxLayout(self.widget_329)
        self.verticalLayout_222.setSpacing(0)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.verticalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_nhietdo_4 = QTableWidget(self.widget_329)
        if (self.tableWidget_nhietdo_4.columnCount() < 3):
            self.tableWidget_nhietdo_4.setColumnCount(3)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setHorizontalHeaderItem(0, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setHorizontalHeaderItem(1, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setHorizontalHeaderItem(2, __qtablewidgetitem146)
        if (self.tableWidget_nhietdo_4.rowCount() < 9):
            self.tableWidget_nhietdo_4.setRowCount(9)
        __qtablewidgetitem147 = QTableWidgetItem()
        __qtablewidgetitem147.setFont(font3);
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(0, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(1, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(2, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(3, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(4, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(5, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(6, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(7, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_nhietdo_4.setVerticalHeaderItem(8, __qtablewidgetitem155)
        self.tableWidget_nhietdo_4.setObjectName(u"tableWidget_nhietdo_4")
        sizePolicy.setHeightForWidth(self.tableWidget_nhietdo_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_nhietdo_4.setSizePolicy(sizePolicy)
        self.tableWidget_nhietdo_4.setMinimumSize(QSize(400, 0))
        self.tableWidget_nhietdo_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_nhietdo_4.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_4.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_nhietdo_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_nhietdo_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_nhietdo_4.verticalHeader().setVisible(False)
        self.tableWidget_nhietdo_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_nhietdo_4.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_4.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_222.addWidget(self.tableWidget_nhietdo_4)


        self.verticalLayout_221.addWidget(self.widget_329)

        self.widget_330 = QWidget(self.widget_328)
        self.widget_330.setObjectName(u"widget_330")
        sizePolicy3.setHeightForWidth(self.widget_330.sizePolicy().hasHeightForWidth())
        self.widget_330.setSizePolicy(sizePolicy3)
        self.horizontalLayout_164 = QHBoxLayout(self.widget_330)
        self.horizontalLayout_164.setSpacing(0)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.horizontalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_4 = QPushButton(self.widget_330)
        self.pushButton_exportTem_4.setObjectName(u"pushButton_exportTem_4")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_4.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_4.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_164.addWidget(self.pushButton_exportTem_4)


        self.verticalLayout_221.addWidget(self.widget_330)


        self.gridLayout_3.addWidget(self.widget_328, 0, 0, 1, 1)

        self.widget_331 = QWidget(self.widget_327)
        self.widget_331.setObjectName(u"widget_331")
        self.verticalLayout_223 = QVBoxLayout(self.widget_331)
        self.verticalLayout_223.setSpacing(0)
        self.verticalLayout_223.setObjectName(u"verticalLayout_223")
        self.verticalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.widget_332 = QWidget(self.widget_331)
        self.widget_332.setObjectName(u"widget_332")
        sizePolicy.setHeightForWidth(self.widget_332.sizePolicy().hasHeightForWidth())
        self.widget_332.setSizePolicy(sizePolicy)
        self.widget_332.setAutoFillBackground(False)
        self.widget_332.setStyleSheet(u"text-align: center;")
        self.verticalLayout_224 = QVBoxLayout(self.widget_332)
        self.verticalLayout_224.setSpacing(0)
        self.verticalLayout_224.setObjectName(u"verticalLayout_224")
        self.verticalLayout_224.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.widget_332)
        self.label_56.setObjectName(u"label_56")
        sizePolicy3.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy3)
        self.label_56.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.verticalLayout_224.addWidget(self.label_56)

        self.widget_333 = QWidget(self.widget_332)
        self.widget_333.setObjectName(u"widget_333")
        sizePolicy.setHeightForWidth(self.widget_333.sizePolicy().hasHeightForWidth())
        self.widget_333.setSizePolicy(sizePolicy)
        self.verticalLayout_225 = QVBoxLayout(self.widget_333)
        self.verticalLayout_225.setSpacing(0)
        self.verticalLayout_225.setObjectName(u"verticalLayout_225")
        self.verticalLayout_225.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc1_4 = QTableWidget(self.widget_333)
        if (self.tableWidget_dc1_4.columnCount() < 3):
            self.tableWidget_dc1_4.setColumnCount(3)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_dc1_4.setHorizontalHeaderItem(0, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_dc1_4.setHorizontalHeaderItem(1, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_dc1_4.setHorizontalHeaderItem(2, __qtablewidgetitem158)
        if (self.tableWidget_dc1_4.rowCount() < 9):
            self.tableWidget_dc1_4.setRowCount(9)
        __qtablewidgetitem159 = QTableWidgetItem()
        __qtablewidgetitem159.setFont(font3);
        self.tableWidget_dc1_4.setVerticalHeaderItem(0, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_dc1_4.setVerticalHeaderItem(1, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_dc1_4.setVerticalHeaderItem(2, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_dc1_4.setVerticalHeaderItem(3, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_dc1_4.setVerticalHeaderItem(4, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_dc1_4.setVerticalHeaderItem(5, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_dc1_4.setVerticalHeaderItem(6, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tableWidget_dc1_4.setVerticalHeaderItem(7, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tableWidget_dc1_4.setVerticalHeaderItem(8, __qtablewidgetitem167)
        self.tableWidget_dc1_4.setObjectName(u"tableWidget_dc1_4")
        sizePolicy.setHeightForWidth(self.tableWidget_dc1_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc1_4.setSizePolicy(sizePolicy)
        self.tableWidget_dc1_4.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc1_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc1_4.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_4.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc1_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc1_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc1_4.verticalHeader().setVisible(False)
        self.tableWidget_dc1_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc1_4.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_4.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_225.addWidget(self.tableWidget_dc1_4)


        self.verticalLayout_224.addWidget(self.widget_333)

        self.widget_334 = QWidget(self.widget_332)
        self.widget_334.setObjectName(u"widget_334")
        sizePolicy3.setHeightForWidth(self.widget_334.sizePolicy().hasHeightForWidth())
        self.widget_334.setSizePolicy(sizePolicy3)
        self.horizontalLayout_165 = QHBoxLayout(self.widget_334)
        self.horizontalLayout_165.setSpacing(0)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_165.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_16 = QPushButton(self.widget_334)
        self.pushButton_exportTem_16.setObjectName(u"pushButton_exportTem_16")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_16.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_16.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_16.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_165.addWidget(self.pushButton_exportTem_16)


        self.verticalLayout_224.addWidget(self.widget_334)


        self.verticalLayout_223.addWidget(self.widget_332)


        self.gridLayout_3.addWidget(self.widget_331, 0, 1, 1, 1)

        self.widget_335 = QWidget(self.widget_327)
        self.widget_335.setObjectName(u"widget_335")
        sizePolicy.setHeightForWidth(self.widget_335.sizePolicy().hasHeightForWidth())
        self.widget_335.setSizePolicy(sizePolicy)
        self.widget_335.setAutoFillBackground(False)
        self.widget_335.setStyleSheet(u"text-align: center;")
        self.verticalLayout_226 = QVBoxLayout(self.widget_335)
        self.verticalLayout_226.setSpacing(0)
        self.verticalLayout_226.setObjectName(u"verticalLayout_226")
        self.verticalLayout_226.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.widget_335)
        self.label_57.setObjectName(u"label_57")
        sizePolicy3.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy3)
        self.label_57.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.verticalLayout_226.addWidget(self.label_57)

        self.widget_338 = QWidget(self.widget_335)
        self.widget_338.setObjectName(u"widget_338")
        sizePolicy.setHeightForWidth(self.widget_338.sizePolicy().hasHeightForWidth())
        self.widget_338.setSizePolicy(sizePolicy)
        self.verticalLayout_227 = QVBoxLayout(self.widget_338)
        self.verticalLayout_227.setSpacing(0)
        self.verticalLayout_227.setObjectName(u"verticalLayout_227")
        self.verticalLayout_227.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac1_3 = QTableWidget(self.widget_338)
        if (self.tableWidget_ac1_3.columnCount() < 3):
            self.tableWidget_ac1_3.setColumnCount(3)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tableWidget_ac1_3.setHorizontalHeaderItem(0, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tableWidget_ac1_3.setHorizontalHeaderItem(1, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tableWidget_ac1_3.setHorizontalHeaderItem(2, __qtablewidgetitem170)
        if (self.tableWidget_ac1_3.rowCount() < 9):
            self.tableWidget_ac1_3.setRowCount(9)
        __qtablewidgetitem171 = QTableWidgetItem()
        __qtablewidgetitem171.setFont(font3);
        self.tableWidget_ac1_3.setVerticalHeaderItem(0, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tableWidget_ac1_3.setVerticalHeaderItem(1, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.tableWidget_ac1_3.setVerticalHeaderItem(2, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tableWidget_ac1_3.setVerticalHeaderItem(3, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.tableWidget_ac1_3.setVerticalHeaderItem(4, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tableWidget_ac1_3.setVerticalHeaderItem(5, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.tableWidget_ac1_3.setVerticalHeaderItem(6, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tableWidget_ac1_3.setVerticalHeaderItem(7, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tableWidget_ac1_3.setVerticalHeaderItem(8, __qtablewidgetitem179)
        self.tableWidget_ac1_3.setObjectName(u"tableWidget_ac1_3")
        sizePolicy.setHeightForWidth(self.tableWidget_ac1_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac1_3.setSizePolicy(sizePolicy)
        self.tableWidget_ac1_3.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac1_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac1_3.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_3.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac1_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac1_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac1_3.verticalHeader().setVisible(False)
        self.tableWidget_ac1_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac1_3.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_3.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_227.addWidget(self.tableWidget_ac1_3)


        self.verticalLayout_226.addWidget(self.widget_338)

        self.widget_339 = QWidget(self.widget_335)
        self.widget_339.setObjectName(u"widget_339")
        sizePolicy3.setHeightForWidth(self.widget_339.sizePolicy().hasHeightForWidth())
        self.widget_339.setSizePolicy(sizePolicy3)
        self.horizontalLayout_166 = QHBoxLayout(self.widget_339)
        self.horizontalLayout_166.setSpacing(0)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.horizontalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_17 = QPushButton(self.widget_339)
        self.pushButton_exportTem_17.setObjectName(u"pushButton_exportTem_17")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_17.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_17.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_17.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_166.addWidget(self.pushButton_exportTem_17)


        self.verticalLayout_226.addWidget(self.widget_339)


        self.gridLayout_3.addWidget(self.widget_335, 0, 2, 1, 1)

        self.widget_340 = QWidget(self.widget_327)
        self.widget_340.setObjectName(u"widget_340")
        sizePolicy.setHeightForWidth(self.widget_340.sizePolicy().hasHeightForWidth())
        self.widget_340.setSizePolicy(sizePolicy)
        self.widget_340.setAutoFillBackground(False)
        self.widget_340.setStyleSheet(u"text-align: center;")
        self.verticalLayout_228 = QVBoxLayout(self.widget_340)
        self.verticalLayout_228.setSpacing(0)
        self.verticalLayout_228.setObjectName(u"verticalLayout_228")
        self.verticalLayout_228.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.widget_340)
        self.label_58.setObjectName(u"label_58")
        sizePolicy3.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy3)
        self.label_58.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.verticalLayout_228.addWidget(self.label_58)

        self.widget_341 = QWidget(self.widget_340)
        self.widget_341.setObjectName(u"widget_341")
        sizePolicy.setHeightForWidth(self.widget_341.sizePolicy().hasHeightForWidth())
        self.widget_341.setSizePolicy(sizePolicy)
        self.verticalLayout_229 = QVBoxLayout(self.widget_341)
        self.verticalLayout_229.setSpacing(0)
        self.verticalLayout_229.setObjectName(u"verticalLayout_229")
        self.verticalLayout_229.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_doam_4 = QTableWidget(self.widget_341)
        if (self.tableWidget_doam_4.columnCount() < 3):
            self.tableWidget_doam_4.setColumnCount(3)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tableWidget_doam_4.setHorizontalHeaderItem(0, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tableWidget_doam_4.setHorizontalHeaderItem(1, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.tableWidget_doam_4.setHorizontalHeaderItem(2, __qtablewidgetitem182)
        if (self.tableWidget_doam_4.rowCount() < 9):
            self.tableWidget_doam_4.setRowCount(9)
        __qtablewidgetitem183 = QTableWidgetItem()
        __qtablewidgetitem183.setFont(font3);
        self.tableWidget_doam_4.setVerticalHeaderItem(0, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.tableWidget_doam_4.setVerticalHeaderItem(1, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tableWidget_doam_4.setVerticalHeaderItem(2, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tableWidget_doam_4.setVerticalHeaderItem(3, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget_doam_4.setVerticalHeaderItem(4, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tableWidget_doam_4.setVerticalHeaderItem(5, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget_doam_4.setVerticalHeaderItem(6, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.tableWidget_doam_4.setVerticalHeaderItem(7, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tableWidget_doam_4.setVerticalHeaderItem(8, __qtablewidgetitem191)
        self.tableWidget_doam_4.setObjectName(u"tableWidget_doam_4")
        sizePolicy.setHeightForWidth(self.tableWidget_doam_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_doam_4.setSizePolicy(sizePolicy)
        self.tableWidget_doam_4.setMinimumSize(QSize(400, 0))
        self.tableWidget_doam_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_doam_4.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_4.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_doam_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_doam_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_doam_4.verticalHeader().setVisible(False)
        self.tableWidget_doam_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_doam_4.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_4.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_229.addWidget(self.tableWidget_doam_4)


        self.verticalLayout_228.addWidget(self.widget_341)

        self.widget_342 = QWidget(self.widget_340)
        self.widget_342.setObjectName(u"widget_342")
        sizePolicy3.setHeightForWidth(self.widget_342.sizePolicy().hasHeightForWidth())
        self.widget_342.setSizePolicy(sizePolicy3)
        self.horizontalLayout_167 = QHBoxLayout(self.widget_342)
        self.horizontalLayout_167.setSpacing(0)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_167.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_18 = QPushButton(self.widget_342)
        self.pushButton_exportTem_18.setObjectName(u"pushButton_exportTem_18")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_18.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_18.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_18.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_167.addWidget(self.pushButton_exportTem_18)


        self.verticalLayout_228.addWidget(self.widget_342)


        self.gridLayout_3.addWidget(self.widget_340, 1, 0, 1, 1)

        self.widget_343 = QWidget(self.widget_327)
        self.widget_343.setObjectName(u"widget_343")
        sizePolicy.setHeightForWidth(self.widget_343.sizePolicy().hasHeightForWidth())
        self.widget_343.setSizePolicy(sizePolicy)
        self.widget_343.setAutoFillBackground(False)
        self.widget_343.setStyleSheet(u"text-align: center;")
        self.verticalLayout_230 = QVBoxLayout(self.widget_343)
        self.verticalLayout_230.setSpacing(0)
        self.verticalLayout_230.setObjectName(u"verticalLayout_230")
        self.verticalLayout_230.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.widget_343)
        self.label_59.setObjectName(u"label_59")
        sizePolicy3.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy3)
        self.label_59.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_230.addWidget(self.label_59)

        self.widget_344 = QWidget(self.widget_343)
        self.widget_344.setObjectName(u"widget_344")
        sizePolicy.setHeightForWidth(self.widget_344.sizePolicy().hasHeightForWidth())
        self.widget_344.setSizePolicy(sizePolicy)
        self.verticalLayout_231 = QVBoxLayout(self.widget_344)
        self.verticalLayout_231.setSpacing(0)
        self.verticalLayout_231.setObjectName(u"verticalLayout_231")
        self.verticalLayout_231.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc2_4 = QTableWidget(self.widget_344)
        if (self.tableWidget_dc2_4.columnCount() < 3):
            self.tableWidget_dc2_4.setColumnCount(3)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.tableWidget_dc2_4.setHorizontalHeaderItem(0, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget_dc2_4.setHorizontalHeaderItem(1, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tableWidget_dc2_4.setHorizontalHeaderItem(2, __qtablewidgetitem194)
        if (self.tableWidget_dc2_4.rowCount() < 9):
            self.tableWidget_dc2_4.setRowCount(9)
        __qtablewidgetitem195 = QTableWidgetItem()
        __qtablewidgetitem195.setFont(font3);
        self.tableWidget_dc2_4.setVerticalHeaderItem(0, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tableWidget_dc2_4.setVerticalHeaderItem(1, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget_dc2_4.setVerticalHeaderItem(2, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.tableWidget_dc2_4.setVerticalHeaderItem(3, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tableWidget_dc2_4.setVerticalHeaderItem(4, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.tableWidget_dc2_4.setVerticalHeaderItem(5, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.tableWidget_dc2_4.setVerticalHeaderItem(6, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.tableWidget_dc2_4.setVerticalHeaderItem(7, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.tableWidget_dc2_4.setVerticalHeaderItem(8, __qtablewidgetitem203)
        self.tableWidget_dc2_4.setObjectName(u"tableWidget_dc2_4")
        sizePolicy.setHeightForWidth(self.tableWidget_dc2_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc2_4.setSizePolicy(sizePolicy)
        self.tableWidget_dc2_4.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc2_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc2_4.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_4.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc2_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc2_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc2_4.verticalHeader().setVisible(False)
        self.tableWidget_dc2_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc2_4.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_4.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_231.addWidget(self.tableWidget_dc2_4)


        self.verticalLayout_230.addWidget(self.widget_344)

        self.widget_345 = QWidget(self.widget_343)
        self.widget_345.setObjectName(u"widget_345")
        sizePolicy3.setHeightForWidth(self.widget_345.sizePolicy().hasHeightForWidth())
        self.widget_345.setSizePolicy(sizePolicy3)
        self.horizontalLayout_168 = QHBoxLayout(self.widget_345)
        self.horizontalLayout_168.setSpacing(0)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_19 = QPushButton(self.widget_345)
        self.pushButton_exportTem_19.setObjectName(u"pushButton_exportTem_19")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_19.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_19.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_19.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_168.addWidget(self.pushButton_exportTem_19)


        self.verticalLayout_230.addWidget(self.widget_345)


        self.gridLayout_3.addWidget(self.widget_343, 1, 1, 1, 1)

        self.widget_346 = QWidget(self.widget_327)
        self.widget_346.setObjectName(u"widget_346")
        sizePolicy.setHeightForWidth(self.widget_346.sizePolicy().hasHeightForWidth())
        self.widget_346.setSizePolicy(sizePolicy)
        self.widget_346.setAutoFillBackground(False)
        self.widget_346.setStyleSheet(u"text-align: center;")
        self.verticalLayout_232 = QVBoxLayout(self.widget_346)
        self.verticalLayout_232.setSpacing(0)
        self.verticalLayout_232.setObjectName(u"verticalLayout_232")
        self.verticalLayout_232.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.widget_346)
        self.label_60.setObjectName(u"label_60")
        sizePolicy3.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy3)
        self.label_60.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.verticalLayout_232.addWidget(self.label_60)

        self.widget_347 = QWidget(self.widget_346)
        self.widget_347.setObjectName(u"widget_347")
        sizePolicy.setHeightForWidth(self.widget_347.sizePolicy().hasHeightForWidth())
        self.widget_347.setSizePolicy(sizePolicy)
        self.verticalLayout_233 = QVBoxLayout(self.widget_347)
        self.verticalLayout_233.setSpacing(0)
        self.verticalLayout_233.setObjectName(u"verticalLayout_233")
        self.verticalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac2_3 = QTableWidget(self.widget_347)
        if (self.tableWidget_ac2_3.columnCount() < 3):
            self.tableWidget_ac2_3.setColumnCount(3)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.tableWidget_ac2_3.setHorizontalHeaderItem(0, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.tableWidget_ac2_3.setHorizontalHeaderItem(1, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.tableWidget_ac2_3.setHorizontalHeaderItem(2, __qtablewidgetitem206)
        if (self.tableWidget_ac2_3.rowCount() < 9):
            self.tableWidget_ac2_3.setRowCount(9)
        __qtablewidgetitem207 = QTableWidgetItem()
        __qtablewidgetitem207.setFont(font3);
        self.tableWidget_ac2_3.setVerticalHeaderItem(0, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.tableWidget_ac2_3.setVerticalHeaderItem(1, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tableWidget_ac2_3.setVerticalHeaderItem(2, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.tableWidget_ac2_3.setVerticalHeaderItem(3, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.tableWidget_ac2_3.setVerticalHeaderItem(4, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.tableWidget_ac2_3.setVerticalHeaderItem(5, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        self.tableWidget_ac2_3.setVerticalHeaderItem(6, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        self.tableWidget_ac2_3.setVerticalHeaderItem(7, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.tableWidget_ac2_3.setVerticalHeaderItem(8, __qtablewidgetitem215)
        self.tableWidget_ac2_3.setObjectName(u"tableWidget_ac2_3")
        sizePolicy.setHeightForWidth(self.tableWidget_ac2_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac2_3.setSizePolicy(sizePolicy)
        self.tableWidget_ac2_3.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac2_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac2_3.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_3.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac2_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac2_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac2_3.verticalHeader().setVisible(False)
        self.tableWidget_ac2_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac2_3.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_3.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_233.addWidget(self.tableWidget_ac2_3)


        self.verticalLayout_232.addWidget(self.widget_347)

        self.widget_348 = QWidget(self.widget_346)
        self.widget_348.setObjectName(u"widget_348")
        sizePolicy3.setHeightForWidth(self.widget_348.sizePolicy().hasHeightForWidth())
        self.widget_348.setSizePolicy(sizePolicy3)
        self.horizontalLayout_169 = QHBoxLayout(self.widget_348)
        self.horizontalLayout_169.setSpacing(0)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.horizontalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_20 = QPushButton(self.widget_348)
        self.pushButton_exportTem_20.setObjectName(u"pushButton_exportTem_20")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_20.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_20.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_20.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_169.addWidget(self.pushButton_exportTem_20)


        self.verticalLayout_232.addWidget(self.widget_348)


        self.gridLayout_3.addWidget(self.widget_346, 1, 2, 1, 1)


        self.verticalLayout_234.addWidget(self.widget_327)

        self.stackedWidget.addWidget(self.suco_3)
        self.doam_4 = QWidget()
        self.doam_4.setObjectName(u"doam_4")
        self.verticalLayout_359 = QVBoxLayout(self.doam_4)
        self.verticalLayout_359.setSpacing(0)
        self.verticalLayout_359.setObjectName(u"verticalLayout_359")
        self.verticalLayout_359.setContentsMargins(0, 0, 0, 0)
        self.widget_Doam_6 = QWidget(self.doam_4)
        self.widget_Doam_6.setObjectName(u"widget_Doam_6")
        self.widget_Doam_6.setStyleSheet(u"")
        self.verticalLayout_357 = QVBoxLayout(self.widget_Doam_6)
        self.verticalLayout_357.setSpacing(0)
        self.verticalLayout_357.setObjectName(u"verticalLayout_357")
        self.verticalLayout_357.setContentsMargins(0, 0, 0, 0)
        self.widget_label_doam_6 = QWidget(self.widget_Doam_6)
        self.widget_label_doam_6.setObjectName(u"widget_label_doam_6")
        sizePolicy.setHeightForWidth(self.widget_label_doam_6.sizePolicy().hasHeightForWidth())
        self.widget_label_doam_6.setSizePolicy(sizePolicy)
        self.widget_label_doam_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_doam_6.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_358 = QVBoxLayout(self.widget_label_doam_6)
        self.verticalLayout_358.setSpacing(0)
        self.verticalLayout_358.setObjectName(u"verticalLayout_358")
        self.verticalLayout_358.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_358.setContentsMargins(0, 0, 0, 0)
        self.label_doam_10 = QLabel(self.widget_label_doam_6)
        self.label_doam_10.setObjectName(u"label_doam_10")
        sizePolicy3.setHeightForWidth(self.label_doam_10.sizePolicy().hasHeightForWidth())
        self.label_doam_10.setSizePolicy(sizePolicy3)
        self.label_doam_10.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_doam_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_358.addWidget(self.label_doam_10)

        self.label_thoigian_doam_6 = QLabel(self.widget_label_doam_6)
        self.label_thoigian_doam_6.setObjectName(u"label_thoigian_doam_6")
        sizePolicy3.setHeightForWidth(self.label_thoigian_doam_6.sizePolicy().hasHeightForWidth())
        self.label_thoigian_doam_6.setSizePolicy(sizePolicy3)
        self.label_thoigian_doam_6.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_doam_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_358.addWidget(self.label_thoigian_doam_6)

        self.screen_doam_6 = QVBoxLayout()
        self.screen_doam_6.setSpacing(0)
        self.screen_doam_6.setObjectName(u"screen_doam_6")
        self.screen_doam_6.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_358.addLayout(self.screen_doam_6)


        self.verticalLayout_357.addWidget(self.widget_label_doam_6)


        self.verticalLayout_359.addWidget(self.widget_Doam_6)

        self.stackedWidget.addWidget(self.doam_4)
        self.dienap_4 = QWidget()
        self.dienap_4.setObjectName(u"dienap_4")
        self.verticalLayout_220 = QVBoxLayout(self.dienap_4)
        self.verticalLayout_220.setSpacing(0)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.verticalLayout_220.setContentsMargins(0, 0, 0, 0)
        self.widget_Dienap_6 = QWidget(self.dienap_4)
        self.widget_Dienap_6.setObjectName(u"widget_Dienap_6")
        self.widget_Dienap_6.setStyleSheet(u"")
        self.verticalLayout_218 = QVBoxLayout(self.widget_Dienap_6)
        self.verticalLayout_218.setSpacing(0)
        self.verticalLayout_218.setObjectName(u"verticalLayout_218")
        self.verticalLayout_218.setContentsMargins(0, 0, 0, 0)
        self.widget_label_dienap_6 = QWidget(self.widget_Dienap_6)
        self.widget_label_dienap_6.setObjectName(u"widget_label_dienap_6")
        sizePolicy.setHeightForWidth(self.widget_label_dienap_6.sizePolicy().hasHeightForWidth())
        self.widget_label_dienap_6.setSizePolicy(sizePolicy)
        self.widget_label_dienap_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_dienap_6.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_219 = QVBoxLayout(self.widget_label_dienap_6)
        self.verticalLayout_219.setSpacing(0)
        self.verticalLayout_219.setObjectName(u"verticalLayout_219")
        self.verticalLayout_219.setContentsMargins(0, 0, 0, 0)
        self.label_diepap_6 = QLabel(self.widget_label_dienap_6)
        self.label_diepap_6.setObjectName(u"label_diepap_6")
        sizePolicy3.setHeightForWidth(self.label_diepap_6.sizePolicy().hasHeightForWidth())
        self.label_diepap_6.setSizePolicy(sizePolicy3)
        self.label_diepap_6.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_diepap_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_219.addWidget(self.label_diepap_6)

        self.label_thoigian_dienap_6 = QLabel(self.widget_label_dienap_6)
        self.label_thoigian_dienap_6.setObjectName(u"label_thoigian_dienap_6")
        sizePolicy3.setHeightForWidth(self.label_thoigian_dienap_6.sizePolicy().hasHeightForWidth())
        self.label_thoigian_dienap_6.setSizePolicy(sizePolicy3)
        self.label_thoigian_dienap_6.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_dienap_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_219.addWidget(self.label_thoigian_dienap_6)

        self.screen_dienap_11 = QVBoxLayout()
        self.screen_dienap_11.setSpacing(0)
        self.screen_dienap_11.setObjectName(u"screen_dienap_11")
        self.screen_dienap_11.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_219.addLayout(self.screen_dienap_11)

        self.screen_dienap_12 = QVBoxLayout()
        self.screen_dienap_12.setSpacing(0)
        self.screen_dienap_12.setObjectName(u"screen_dienap_12")
        self.screen_dienap_12.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_219.addLayout(self.screen_dienap_12)


        self.verticalLayout_218.addWidget(self.widget_label_dienap_6)


        self.verticalLayout_220.addWidget(self.widget_Dienap_6)

        self.stackedWidget.addWidget(self.dienap_4)
        self.suco_4 = QWidget()
        self.suco_4.setObjectName(u"suco_4")
        self.verticalLayout_248 = QVBoxLayout(self.suco_4)
        self.verticalLayout_248.setSpacing(0)
        self.verticalLayout_248.setObjectName(u"verticalLayout_248")
        self.verticalLayout_248.setContentsMargins(0, 0, 0, 0)
        self.widget_349 = QWidget(self.suco_4)
        self.widget_349.setObjectName(u"widget_349")
        self.gridLayout_9 = QGridLayout(self.widget_349)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_350 = QWidget(self.widget_349)
        self.widget_350.setObjectName(u"widget_350")
        sizePolicy.setHeightForWidth(self.widget_350.sizePolicy().hasHeightForWidth())
        self.widget_350.setSizePolicy(sizePolicy)
        self.widget_350.setAutoFillBackground(False)
        self.widget_350.setStyleSheet(u"text-align: center;")
        self.verticalLayout_235 = QVBoxLayout(self.widget_350)
        self.verticalLayout_235.setSpacing(0)
        self.verticalLayout_235.setObjectName(u"verticalLayout_235")
        self.verticalLayout_235.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.widget_350)
        self.label_45.setObjectName(u"label_45")
        sizePolicy3.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy3)
        self.label_45.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_235.addWidget(self.label_45)

        self.widget_351 = QWidget(self.widget_350)
        self.widget_351.setObjectName(u"widget_351")
        sizePolicy.setHeightForWidth(self.widget_351.sizePolicy().hasHeightForWidth())
        self.widget_351.setSizePolicy(sizePolicy)
        self.verticalLayout_236 = QVBoxLayout(self.widget_351)
        self.verticalLayout_236.setSpacing(0)
        self.verticalLayout_236.setObjectName(u"verticalLayout_236")
        self.verticalLayout_236.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_nhietdo_5 = QTableWidget(self.widget_351)
        if (self.tableWidget_nhietdo_5.columnCount() < 3):
            self.tableWidget_nhietdo_5.setColumnCount(3)
        __qtablewidgetitem216 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setHorizontalHeaderItem(0, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setHorizontalHeaderItem(1, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setHorizontalHeaderItem(2, __qtablewidgetitem218)
        if (self.tableWidget_nhietdo_5.rowCount() < 9):
            self.tableWidget_nhietdo_5.setRowCount(9)
        __qtablewidgetitem219 = QTableWidgetItem()
        __qtablewidgetitem219.setFont(font3);
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(0, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(1, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(2, __qtablewidgetitem221)
        __qtablewidgetitem222 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(3, __qtablewidgetitem222)
        __qtablewidgetitem223 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(4, __qtablewidgetitem223)
        __qtablewidgetitem224 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(5, __qtablewidgetitem224)
        __qtablewidgetitem225 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(6, __qtablewidgetitem225)
        __qtablewidgetitem226 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(7, __qtablewidgetitem226)
        __qtablewidgetitem227 = QTableWidgetItem()
        self.tableWidget_nhietdo_5.setVerticalHeaderItem(8, __qtablewidgetitem227)
        self.tableWidget_nhietdo_5.setObjectName(u"tableWidget_nhietdo_5")
        sizePolicy.setHeightForWidth(self.tableWidget_nhietdo_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_nhietdo_5.setSizePolicy(sizePolicy)
        self.tableWidget_nhietdo_5.setMinimumSize(QSize(400, 0))
        self.tableWidget_nhietdo_5.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_nhietdo_5.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_5.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_nhietdo_5.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_nhietdo_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_nhietdo_5.verticalHeader().setVisible(False)
        self.tableWidget_nhietdo_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_nhietdo_5.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_5.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_236.addWidget(self.tableWidget_nhietdo_5)


        self.verticalLayout_235.addWidget(self.widget_351)

        self.widget_352 = QWidget(self.widget_350)
        self.widget_352.setObjectName(u"widget_352")
        sizePolicy3.setHeightForWidth(self.widget_352.sizePolicy().hasHeightForWidth())
        self.widget_352.setSizePolicy(sizePolicy3)
        self.horizontalLayout_170 = QHBoxLayout(self.widget_352)
        self.horizontalLayout_170.setSpacing(0)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_5 = QPushButton(self.widget_352)
        self.pushButton_exportTem_5.setObjectName(u"pushButton_exportTem_5")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_5.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_5.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_170.addWidget(self.pushButton_exportTem_5)


        self.verticalLayout_235.addWidget(self.widget_352)


        self.gridLayout_9.addWidget(self.widget_350, 0, 0, 1, 1)

        self.widget_353 = QWidget(self.widget_349)
        self.widget_353.setObjectName(u"widget_353")
        self.verticalLayout_237 = QVBoxLayout(self.widget_353)
        self.verticalLayout_237.setSpacing(0)
        self.verticalLayout_237.setObjectName(u"verticalLayout_237")
        self.verticalLayout_237.setContentsMargins(0, 0, 0, 0)
        self.widget_354 = QWidget(self.widget_353)
        self.widget_354.setObjectName(u"widget_354")
        sizePolicy.setHeightForWidth(self.widget_354.sizePolicy().hasHeightForWidth())
        self.widget_354.setSizePolicy(sizePolicy)
        self.widget_354.setAutoFillBackground(False)
        self.widget_354.setStyleSheet(u"text-align: center;")
        self.verticalLayout_238 = QVBoxLayout(self.widget_354)
        self.verticalLayout_238.setSpacing(0)
        self.verticalLayout_238.setObjectName(u"verticalLayout_238")
        self.verticalLayout_238.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.widget_354)
        self.label_61.setObjectName(u"label_61")
        sizePolicy3.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy3)
        self.label_61.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.verticalLayout_238.addWidget(self.label_61)

        self.widget_355 = QWidget(self.widget_354)
        self.widget_355.setObjectName(u"widget_355")
        sizePolicy.setHeightForWidth(self.widget_355.sizePolicy().hasHeightForWidth())
        self.widget_355.setSizePolicy(sizePolicy)
        self.verticalLayout_239 = QVBoxLayout(self.widget_355)
        self.verticalLayout_239.setSpacing(0)
        self.verticalLayout_239.setObjectName(u"verticalLayout_239")
        self.verticalLayout_239.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc1_5 = QTableWidget(self.widget_355)
        if (self.tableWidget_dc1_5.columnCount() < 3):
            self.tableWidget_dc1_5.setColumnCount(3)
        __qtablewidgetitem228 = QTableWidgetItem()
        self.tableWidget_dc1_5.setHorizontalHeaderItem(0, __qtablewidgetitem228)
        __qtablewidgetitem229 = QTableWidgetItem()
        self.tableWidget_dc1_5.setHorizontalHeaderItem(1, __qtablewidgetitem229)
        __qtablewidgetitem230 = QTableWidgetItem()
        self.tableWidget_dc1_5.setHorizontalHeaderItem(2, __qtablewidgetitem230)
        if (self.tableWidget_dc1_5.rowCount() < 9):
            self.tableWidget_dc1_5.setRowCount(9)
        __qtablewidgetitem231 = QTableWidgetItem()
        __qtablewidgetitem231.setFont(font3);
        self.tableWidget_dc1_5.setVerticalHeaderItem(0, __qtablewidgetitem231)
        __qtablewidgetitem232 = QTableWidgetItem()
        self.tableWidget_dc1_5.setVerticalHeaderItem(1, __qtablewidgetitem232)
        __qtablewidgetitem233 = QTableWidgetItem()
        self.tableWidget_dc1_5.setVerticalHeaderItem(2, __qtablewidgetitem233)
        __qtablewidgetitem234 = QTableWidgetItem()
        self.tableWidget_dc1_5.setVerticalHeaderItem(3, __qtablewidgetitem234)
        __qtablewidgetitem235 = QTableWidgetItem()
        self.tableWidget_dc1_5.setVerticalHeaderItem(4, __qtablewidgetitem235)
        __qtablewidgetitem236 = QTableWidgetItem()
        self.tableWidget_dc1_5.setVerticalHeaderItem(5, __qtablewidgetitem236)
        __qtablewidgetitem237 = QTableWidgetItem()
        self.tableWidget_dc1_5.setVerticalHeaderItem(6, __qtablewidgetitem237)
        __qtablewidgetitem238 = QTableWidgetItem()
        self.tableWidget_dc1_5.setVerticalHeaderItem(7, __qtablewidgetitem238)
        __qtablewidgetitem239 = QTableWidgetItem()
        self.tableWidget_dc1_5.setVerticalHeaderItem(8, __qtablewidgetitem239)
        self.tableWidget_dc1_5.setObjectName(u"tableWidget_dc1_5")
        sizePolicy.setHeightForWidth(self.tableWidget_dc1_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc1_5.setSizePolicy(sizePolicy)
        self.tableWidget_dc1_5.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc1_5.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc1_5.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_5.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc1_5.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc1_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc1_5.verticalHeader().setVisible(False)
        self.tableWidget_dc1_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc1_5.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_5.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_239.addWidget(self.tableWidget_dc1_5)


        self.verticalLayout_238.addWidget(self.widget_355)

        self.widget_356 = QWidget(self.widget_354)
        self.widget_356.setObjectName(u"widget_356")
        sizePolicy3.setHeightForWidth(self.widget_356.sizePolicy().hasHeightForWidth())
        self.widget_356.setSizePolicy(sizePolicy3)
        self.horizontalLayout_171 = QHBoxLayout(self.widget_356)
        self.horizontalLayout_171.setSpacing(0)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.horizontalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_21 = QPushButton(self.widget_356)
        self.pushButton_exportTem_21.setObjectName(u"pushButton_exportTem_21")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_21.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_21.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_21.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_171.addWidget(self.pushButton_exportTem_21)


        self.verticalLayout_238.addWidget(self.widget_356)


        self.verticalLayout_237.addWidget(self.widget_354)


        self.gridLayout_9.addWidget(self.widget_353, 0, 1, 1, 1)

        self.widget_357 = QWidget(self.widget_349)
        self.widget_357.setObjectName(u"widget_357")
        sizePolicy.setHeightForWidth(self.widget_357.sizePolicy().hasHeightForWidth())
        self.widget_357.setSizePolicy(sizePolicy)
        self.widget_357.setAutoFillBackground(False)
        self.widget_357.setStyleSheet(u"text-align: center;")
        self.verticalLayout_240 = QVBoxLayout(self.widget_357)
        self.verticalLayout_240.setSpacing(0)
        self.verticalLayout_240.setObjectName(u"verticalLayout_240")
        self.verticalLayout_240.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.widget_357)
        self.label_74.setObjectName(u"label_74")
        sizePolicy3.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy3)
        self.label_74.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.verticalLayout_240.addWidget(self.label_74)

        self.widget_358 = QWidget(self.widget_357)
        self.widget_358.setObjectName(u"widget_358")
        sizePolicy.setHeightForWidth(self.widget_358.sizePolicy().hasHeightForWidth())
        self.widget_358.setSizePolicy(sizePolicy)
        self.verticalLayout_241 = QVBoxLayout(self.widget_358)
        self.verticalLayout_241.setSpacing(0)
        self.verticalLayout_241.setObjectName(u"verticalLayout_241")
        self.verticalLayout_241.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac1_4 = QTableWidget(self.widget_358)
        if (self.tableWidget_ac1_4.columnCount() < 3):
            self.tableWidget_ac1_4.setColumnCount(3)
        __qtablewidgetitem240 = QTableWidgetItem()
        self.tableWidget_ac1_4.setHorizontalHeaderItem(0, __qtablewidgetitem240)
        __qtablewidgetitem241 = QTableWidgetItem()
        self.tableWidget_ac1_4.setHorizontalHeaderItem(1, __qtablewidgetitem241)
        __qtablewidgetitem242 = QTableWidgetItem()
        self.tableWidget_ac1_4.setHorizontalHeaderItem(2, __qtablewidgetitem242)
        if (self.tableWidget_ac1_4.rowCount() < 9):
            self.tableWidget_ac1_4.setRowCount(9)
        __qtablewidgetitem243 = QTableWidgetItem()
        __qtablewidgetitem243.setFont(font3);
        self.tableWidget_ac1_4.setVerticalHeaderItem(0, __qtablewidgetitem243)
        __qtablewidgetitem244 = QTableWidgetItem()
        self.tableWidget_ac1_4.setVerticalHeaderItem(1, __qtablewidgetitem244)
        __qtablewidgetitem245 = QTableWidgetItem()
        self.tableWidget_ac1_4.setVerticalHeaderItem(2, __qtablewidgetitem245)
        __qtablewidgetitem246 = QTableWidgetItem()
        self.tableWidget_ac1_4.setVerticalHeaderItem(3, __qtablewidgetitem246)
        __qtablewidgetitem247 = QTableWidgetItem()
        self.tableWidget_ac1_4.setVerticalHeaderItem(4, __qtablewidgetitem247)
        __qtablewidgetitem248 = QTableWidgetItem()
        self.tableWidget_ac1_4.setVerticalHeaderItem(5, __qtablewidgetitem248)
        __qtablewidgetitem249 = QTableWidgetItem()
        self.tableWidget_ac1_4.setVerticalHeaderItem(6, __qtablewidgetitem249)
        __qtablewidgetitem250 = QTableWidgetItem()
        self.tableWidget_ac1_4.setVerticalHeaderItem(7, __qtablewidgetitem250)
        __qtablewidgetitem251 = QTableWidgetItem()
        self.tableWidget_ac1_4.setVerticalHeaderItem(8, __qtablewidgetitem251)
        self.tableWidget_ac1_4.setObjectName(u"tableWidget_ac1_4")
        sizePolicy.setHeightForWidth(self.tableWidget_ac1_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac1_4.setSizePolicy(sizePolicy)
        self.tableWidget_ac1_4.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac1_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac1_4.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_4.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac1_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac1_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac1_4.verticalHeader().setVisible(False)
        self.tableWidget_ac1_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac1_4.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_4.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_241.addWidget(self.tableWidget_ac1_4)


        self.verticalLayout_240.addWidget(self.widget_358)

        self.widget_359 = QWidget(self.widget_357)
        self.widget_359.setObjectName(u"widget_359")
        sizePolicy3.setHeightForWidth(self.widget_359.sizePolicy().hasHeightForWidth())
        self.widget_359.setSizePolicy(sizePolicy3)
        self.horizontalLayout_172 = QHBoxLayout(self.widget_359)
        self.horizontalLayout_172.setSpacing(0)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.horizontalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_22 = QPushButton(self.widget_359)
        self.pushButton_exportTem_22.setObjectName(u"pushButton_exportTem_22")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_22.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_22.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_22.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_172.addWidget(self.pushButton_exportTem_22)


        self.verticalLayout_240.addWidget(self.widget_359)


        self.gridLayout_9.addWidget(self.widget_357, 0, 2, 1, 1)

        self.widget_360 = QWidget(self.widget_349)
        self.widget_360.setObjectName(u"widget_360")
        sizePolicy.setHeightForWidth(self.widget_360.sizePolicy().hasHeightForWidth())
        self.widget_360.setSizePolicy(sizePolicy)
        self.widget_360.setAutoFillBackground(False)
        self.widget_360.setStyleSheet(u"text-align: center;")
        self.verticalLayout_242 = QVBoxLayout(self.widget_360)
        self.verticalLayout_242.setSpacing(0)
        self.verticalLayout_242.setObjectName(u"verticalLayout_242")
        self.verticalLayout_242.setContentsMargins(0, 0, 0, 0)
        self.label_75 = QLabel(self.widget_360)
        self.label_75.setObjectName(u"label_75")
        sizePolicy3.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy3)
        self.label_75.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.verticalLayout_242.addWidget(self.label_75)

        self.widget_361 = QWidget(self.widget_360)
        self.widget_361.setObjectName(u"widget_361")
        sizePolicy.setHeightForWidth(self.widget_361.sizePolicy().hasHeightForWidth())
        self.widget_361.setSizePolicy(sizePolicy)
        self.verticalLayout_243 = QVBoxLayout(self.widget_361)
        self.verticalLayout_243.setSpacing(0)
        self.verticalLayout_243.setObjectName(u"verticalLayout_243")
        self.verticalLayout_243.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_doam_5 = QTableWidget(self.widget_361)
        if (self.tableWidget_doam_5.columnCount() < 3):
            self.tableWidget_doam_5.setColumnCount(3)
        __qtablewidgetitem252 = QTableWidgetItem()
        self.tableWidget_doam_5.setHorizontalHeaderItem(0, __qtablewidgetitem252)
        __qtablewidgetitem253 = QTableWidgetItem()
        self.tableWidget_doam_5.setHorizontalHeaderItem(1, __qtablewidgetitem253)
        __qtablewidgetitem254 = QTableWidgetItem()
        self.tableWidget_doam_5.setHorizontalHeaderItem(2, __qtablewidgetitem254)
        if (self.tableWidget_doam_5.rowCount() < 9):
            self.tableWidget_doam_5.setRowCount(9)
        __qtablewidgetitem255 = QTableWidgetItem()
        __qtablewidgetitem255.setFont(font3);
        self.tableWidget_doam_5.setVerticalHeaderItem(0, __qtablewidgetitem255)
        __qtablewidgetitem256 = QTableWidgetItem()
        self.tableWidget_doam_5.setVerticalHeaderItem(1, __qtablewidgetitem256)
        __qtablewidgetitem257 = QTableWidgetItem()
        self.tableWidget_doam_5.setVerticalHeaderItem(2, __qtablewidgetitem257)
        __qtablewidgetitem258 = QTableWidgetItem()
        self.tableWidget_doam_5.setVerticalHeaderItem(3, __qtablewidgetitem258)
        __qtablewidgetitem259 = QTableWidgetItem()
        self.tableWidget_doam_5.setVerticalHeaderItem(4, __qtablewidgetitem259)
        __qtablewidgetitem260 = QTableWidgetItem()
        self.tableWidget_doam_5.setVerticalHeaderItem(5, __qtablewidgetitem260)
        __qtablewidgetitem261 = QTableWidgetItem()
        self.tableWidget_doam_5.setVerticalHeaderItem(6, __qtablewidgetitem261)
        __qtablewidgetitem262 = QTableWidgetItem()
        self.tableWidget_doam_5.setVerticalHeaderItem(7, __qtablewidgetitem262)
        __qtablewidgetitem263 = QTableWidgetItem()
        self.tableWidget_doam_5.setVerticalHeaderItem(8, __qtablewidgetitem263)
        self.tableWidget_doam_5.setObjectName(u"tableWidget_doam_5")
        sizePolicy.setHeightForWidth(self.tableWidget_doam_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_doam_5.setSizePolicy(sizePolicy)
        self.tableWidget_doam_5.setMinimumSize(QSize(400, 0))
        self.tableWidget_doam_5.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_doam_5.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_5.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_doam_5.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_doam_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_doam_5.verticalHeader().setVisible(False)
        self.tableWidget_doam_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_doam_5.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_5.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_243.addWidget(self.tableWidget_doam_5)


        self.verticalLayout_242.addWidget(self.widget_361)

        self.widget_362 = QWidget(self.widget_360)
        self.widget_362.setObjectName(u"widget_362")
        sizePolicy3.setHeightForWidth(self.widget_362.sizePolicy().hasHeightForWidth())
        self.widget_362.setSizePolicy(sizePolicy3)
        self.horizontalLayout_173 = QHBoxLayout(self.widget_362)
        self.horizontalLayout_173.setSpacing(0)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_23 = QPushButton(self.widget_362)
        self.pushButton_exportTem_23.setObjectName(u"pushButton_exportTem_23")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_23.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_23.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_23.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_173.addWidget(self.pushButton_exportTem_23)


        self.verticalLayout_242.addWidget(self.widget_362)


        self.gridLayout_9.addWidget(self.widget_360, 1, 0, 1, 1)

        self.widget_363 = QWidget(self.widget_349)
        self.widget_363.setObjectName(u"widget_363")
        sizePolicy.setHeightForWidth(self.widget_363.sizePolicy().hasHeightForWidth())
        self.widget_363.setSizePolicy(sizePolicy)
        self.widget_363.setAutoFillBackground(False)
        self.widget_363.setStyleSheet(u"text-align: center;")
        self.verticalLayout_244 = QVBoxLayout(self.widget_363)
        self.verticalLayout_244.setSpacing(0)
        self.verticalLayout_244.setObjectName(u"verticalLayout_244")
        self.verticalLayout_244.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.widget_363)
        self.label_76.setObjectName(u"label_76")
        sizePolicy3.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy3)
        self.label_76.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_76.setAlignment(Qt.AlignCenter)

        self.verticalLayout_244.addWidget(self.label_76)

        self.widget_364 = QWidget(self.widget_363)
        self.widget_364.setObjectName(u"widget_364")
        sizePolicy.setHeightForWidth(self.widget_364.sizePolicy().hasHeightForWidth())
        self.widget_364.setSizePolicy(sizePolicy)
        self.verticalLayout_245 = QVBoxLayout(self.widget_364)
        self.verticalLayout_245.setSpacing(0)
        self.verticalLayout_245.setObjectName(u"verticalLayout_245")
        self.verticalLayout_245.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc2_5 = QTableWidget(self.widget_364)
        if (self.tableWidget_dc2_5.columnCount() < 3):
            self.tableWidget_dc2_5.setColumnCount(3)
        __qtablewidgetitem264 = QTableWidgetItem()
        self.tableWidget_dc2_5.setHorizontalHeaderItem(0, __qtablewidgetitem264)
        __qtablewidgetitem265 = QTableWidgetItem()
        self.tableWidget_dc2_5.setHorizontalHeaderItem(1, __qtablewidgetitem265)
        __qtablewidgetitem266 = QTableWidgetItem()
        self.tableWidget_dc2_5.setHorizontalHeaderItem(2, __qtablewidgetitem266)
        if (self.tableWidget_dc2_5.rowCount() < 9):
            self.tableWidget_dc2_5.setRowCount(9)
        __qtablewidgetitem267 = QTableWidgetItem()
        __qtablewidgetitem267.setFont(font3);
        self.tableWidget_dc2_5.setVerticalHeaderItem(0, __qtablewidgetitem267)
        __qtablewidgetitem268 = QTableWidgetItem()
        self.tableWidget_dc2_5.setVerticalHeaderItem(1, __qtablewidgetitem268)
        __qtablewidgetitem269 = QTableWidgetItem()
        self.tableWidget_dc2_5.setVerticalHeaderItem(2, __qtablewidgetitem269)
        __qtablewidgetitem270 = QTableWidgetItem()
        self.tableWidget_dc2_5.setVerticalHeaderItem(3, __qtablewidgetitem270)
        __qtablewidgetitem271 = QTableWidgetItem()
        self.tableWidget_dc2_5.setVerticalHeaderItem(4, __qtablewidgetitem271)
        __qtablewidgetitem272 = QTableWidgetItem()
        self.tableWidget_dc2_5.setVerticalHeaderItem(5, __qtablewidgetitem272)
        __qtablewidgetitem273 = QTableWidgetItem()
        self.tableWidget_dc2_5.setVerticalHeaderItem(6, __qtablewidgetitem273)
        __qtablewidgetitem274 = QTableWidgetItem()
        self.tableWidget_dc2_5.setVerticalHeaderItem(7, __qtablewidgetitem274)
        __qtablewidgetitem275 = QTableWidgetItem()
        self.tableWidget_dc2_5.setVerticalHeaderItem(8, __qtablewidgetitem275)
        self.tableWidget_dc2_5.setObjectName(u"tableWidget_dc2_5")
        sizePolicy.setHeightForWidth(self.tableWidget_dc2_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc2_5.setSizePolicy(sizePolicy)
        self.tableWidget_dc2_5.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc2_5.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc2_5.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_5.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc2_5.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc2_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc2_5.verticalHeader().setVisible(False)
        self.tableWidget_dc2_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc2_5.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_5.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_245.addWidget(self.tableWidget_dc2_5)


        self.verticalLayout_244.addWidget(self.widget_364)

        self.widget_365 = QWidget(self.widget_363)
        self.widget_365.setObjectName(u"widget_365")
        sizePolicy3.setHeightForWidth(self.widget_365.sizePolicy().hasHeightForWidth())
        self.widget_365.setSizePolicy(sizePolicy3)
        self.horizontalLayout_174 = QHBoxLayout(self.widget_365)
        self.horizontalLayout_174.setSpacing(0)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_174.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_24 = QPushButton(self.widget_365)
        self.pushButton_exportTem_24.setObjectName(u"pushButton_exportTem_24")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_24.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_24.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_24.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_174.addWidget(self.pushButton_exportTem_24)


        self.verticalLayout_244.addWidget(self.widget_365)


        self.gridLayout_9.addWidget(self.widget_363, 1, 1, 1, 1)

        self.widget_366 = QWidget(self.widget_349)
        self.widget_366.setObjectName(u"widget_366")
        sizePolicy.setHeightForWidth(self.widget_366.sizePolicy().hasHeightForWidth())
        self.widget_366.setSizePolicy(sizePolicy)
        self.widget_366.setAutoFillBackground(False)
        self.widget_366.setStyleSheet(u"text-align: center;")
        self.verticalLayout_246 = QVBoxLayout(self.widget_366)
        self.verticalLayout_246.setSpacing(0)
        self.verticalLayout_246.setObjectName(u"verticalLayout_246")
        self.verticalLayout_246.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.widget_366)
        self.label_77.setObjectName(u"label_77")
        sizePolicy3.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy3)
        self.label_77.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.verticalLayout_246.addWidget(self.label_77)

        self.widget_367 = QWidget(self.widget_366)
        self.widget_367.setObjectName(u"widget_367")
        sizePolicy.setHeightForWidth(self.widget_367.sizePolicy().hasHeightForWidth())
        self.widget_367.setSizePolicy(sizePolicy)
        self.verticalLayout_247 = QVBoxLayout(self.widget_367)
        self.verticalLayout_247.setSpacing(0)
        self.verticalLayout_247.setObjectName(u"verticalLayout_247")
        self.verticalLayout_247.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac2_4 = QTableWidget(self.widget_367)
        if (self.tableWidget_ac2_4.columnCount() < 3):
            self.tableWidget_ac2_4.setColumnCount(3)
        __qtablewidgetitem276 = QTableWidgetItem()
        self.tableWidget_ac2_4.setHorizontalHeaderItem(0, __qtablewidgetitem276)
        __qtablewidgetitem277 = QTableWidgetItem()
        self.tableWidget_ac2_4.setHorizontalHeaderItem(1, __qtablewidgetitem277)
        __qtablewidgetitem278 = QTableWidgetItem()
        self.tableWidget_ac2_4.setHorizontalHeaderItem(2, __qtablewidgetitem278)
        if (self.tableWidget_ac2_4.rowCount() < 9):
            self.tableWidget_ac2_4.setRowCount(9)
        __qtablewidgetitem279 = QTableWidgetItem()
        __qtablewidgetitem279.setFont(font3);
        self.tableWidget_ac2_4.setVerticalHeaderItem(0, __qtablewidgetitem279)
        __qtablewidgetitem280 = QTableWidgetItem()
        self.tableWidget_ac2_4.setVerticalHeaderItem(1, __qtablewidgetitem280)
        __qtablewidgetitem281 = QTableWidgetItem()
        self.tableWidget_ac2_4.setVerticalHeaderItem(2, __qtablewidgetitem281)
        __qtablewidgetitem282 = QTableWidgetItem()
        self.tableWidget_ac2_4.setVerticalHeaderItem(3, __qtablewidgetitem282)
        __qtablewidgetitem283 = QTableWidgetItem()
        self.tableWidget_ac2_4.setVerticalHeaderItem(4, __qtablewidgetitem283)
        __qtablewidgetitem284 = QTableWidgetItem()
        self.tableWidget_ac2_4.setVerticalHeaderItem(5, __qtablewidgetitem284)
        __qtablewidgetitem285 = QTableWidgetItem()
        self.tableWidget_ac2_4.setVerticalHeaderItem(6, __qtablewidgetitem285)
        __qtablewidgetitem286 = QTableWidgetItem()
        self.tableWidget_ac2_4.setVerticalHeaderItem(7, __qtablewidgetitem286)
        __qtablewidgetitem287 = QTableWidgetItem()
        self.tableWidget_ac2_4.setVerticalHeaderItem(8, __qtablewidgetitem287)
        self.tableWidget_ac2_4.setObjectName(u"tableWidget_ac2_4")
        sizePolicy.setHeightForWidth(self.tableWidget_ac2_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac2_4.setSizePolicy(sizePolicy)
        self.tableWidget_ac2_4.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac2_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac2_4.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_4.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac2_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac2_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac2_4.verticalHeader().setVisible(False)
        self.tableWidget_ac2_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac2_4.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_4.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_247.addWidget(self.tableWidget_ac2_4)


        self.verticalLayout_246.addWidget(self.widget_367)

        self.widget_368 = QWidget(self.widget_366)
        self.widget_368.setObjectName(u"widget_368")
        sizePolicy3.setHeightForWidth(self.widget_368.sizePolicy().hasHeightForWidth())
        self.widget_368.setSizePolicy(sizePolicy3)
        self.horizontalLayout_175 = QHBoxLayout(self.widget_368)
        self.horizontalLayout_175.setSpacing(0)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_25 = QPushButton(self.widget_368)
        self.pushButton_exportTem_25.setObjectName(u"pushButton_exportTem_25")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_25.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_25.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_25.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_175.addWidget(self.pushButton_exportTem_25)


        self.verticalLayout_246.addWidget(self.widget_368)


        self.gridLayout_9.addWidget(self.widget_366, 1, 2, 1, 1)


        self.verticalLayout_248.addWidget(self.widget_349)

        self.stackedWidget.addWidget(self.suco_4)
        self.nhietdo_5 = QWidget()
        self.nhietdo_5.setObjectName(u"nhietdo_5")
        self.verticalLayout_202 = QVBoxLayout(self.nhietdo_5)
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.verticalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.Nhietdo_widget_5 = QWidget(self.nhietdo_5)
        self.Nhietdo_widget_5.setObjectName(u"Nhietdo_widget_5")
        self.Nhietdo_widget_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_201 = QVBoxLayout(self.Nhietdo_widget_5)
        self.verticalLayout_201.setSpacing(0)
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.verticalLayout_201.setContentsMargins(0, 0, 0, 0)
        self.title_nhietdo_5 = QLabel(self.Nhietdo_widget_5)
        self.title_nhietdo_5.setObjectName(u"title_nhietdo_5")
        sizePolicy3.setHeightForWidth(self.title_nhietdo_5.sizePolicy().hasHeightForWidth())
        self.title_nhietdo_5.setSizePolicy(sizePolicy3)
        self.title_nhietdo_5.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.title_nhietdo_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_201.addWidget(self.title_nhietdo_5)

        self.thoigian_nhietdo_5 = QLabel(self.Nhietdo_widget_5)
        self.thoigian_nhietdo_5.setObjectName(u"thoigian_nhietdo_5")
        sizePolicy3.setHeightForWidth(self.thoigian_nhietdo_5.sizePolicy().hasHeightForWidth())
        self.thoigian_nhietdo_5.setSizePolicy(sizePolicy3)
        self.thoigian_nhietdo_5.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.thoigian_nhietdo_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_201.addWidget(self.thoigian_nhietdo_5)

        self.widget_326 = QWidget(self.Nhietdo_widget_5)
        self.widget_326.setObjectName(u"widget_326")
        sizePolicy.setHeightForWidth(self.widget_326.sizePolicy().hasHeightForWidth())
        self.widget_326.setSizePolicy(sizePolicy)
        self.widget_326.setMinimumSize(QSize(0, 0))
        self.gridLayout_8 = QGridLayout(self.widget_326)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_25, 1, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_11, 2, 1, 1, 1)

        self.screen_nhietdo_5 = QVBoxLayout()
        self.screen_nhietdo_5.setSpacing(0)
        self.screen_nhietdo_5.setObjectName(u"screen_nhietdo_5")
        self.screen_nhietdo_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.screen_nhietdo_5.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_8.addLayout(self.screen_nhietdo_5, 1, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_26, 1, 0, 1, 1)


        self.verticalLayout_201.addWidget(self.widget_326)


        self.verticalLayout_202.addWidget(self.Nhietdo_widget_5)

        self.stackedWidget.addWidget(self.nhietdo_5)
        self.dienap_5 = QWidget()
        self.dienap_5.setObjectName(u"dienap_5")
        self.verticalLayout_214 = QVBoxLayout(self.dienap_5)
        self.verticalLayout_214.setSpacing(0)
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.verticalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.widget_Dienap_4 = QWidget(self.dienap_5)
        self.widget_Dienap_4.setObjectName(u"widget_Dienap_4")
        self.widget_Dienap_4.setStyleSheet(u"")
        self.verticalLayout_212 = QVBoxLayout(self.widget_Dienap_4)
        self.verticalLayout_212.setSpacing(0)
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.verticalLayout_212.setContentsMargins(0, 0, 0, 0)
        self.widget_label_dienap_4 = QWidget(self.widget_Dienap_4)
        self.widget_label_dienap_4.setObjectName(u"widget_label_dienap_4")
        sizePolicy.setHeightForWidth(self.widget_label_dienap_4.sizePolicy().hasHeightForWidth())
        self.widget_label_dienap_4.setSizePolicy(sizePolicy)
        self.widget_label_dienap_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_dienap_4.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_213 = QVBoxLayout(self.widget_label_dienap_4)
        self.verticalLayout_213.setSpacing(0)
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.verticalLayout_213.setContentsMargins(0, 0, 0, 0)
        self.label_diepap_4 = QLabel(self.widget_label_dienap_4)
        self.label_diepap_4.setObjectName(u"label_diepap_4")
        sizePolicy3.setHeightForWidth(self.label_diepap_4.sizePolicy().hasHeightForWidth())
        self.label_diepap_4.setSizePolicy(sizePolicy3)
        self.label_diepap_4.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_diepap_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_213.addWidget(self.label_diepap_4)

        self.label_thoigian_dienap_4 = QLabel(self.widget_label_dienap_4)
        self.label_thoigian_dienap_4.setObjectName(u"label_thoigian_dienap_4")
        sizePolicy3.setHeightForWidth(self.label_thoigian_dienap_4.sizePolicy().hasHeightForWidth())
        self.label_thoigian_dienap_4.setSizePolicy(sizePolicy3)
        self.label_thoigian_dienap_4.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_dienap_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_213.addWidget(self.label_thoigian_dienap_4)

        self.screen_dienap_7 = QVBoxLayout()
        self.screen_dienap_7.setSpacing(0)
        self.screen_dienap_7.setObjectName(u"screen_dienap_7")
        self.screen_dienap_7.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_213.addLayout(self.screen_dienap_7)

        self.screen_dienap_8 = QVBoxLayout()
        self.screen_dienap_8.setSpacing(0)
        self.screen_dienap_8.setObjectName(u"screen_dienap_8")
        self.screen_dienap_8.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_213.addLayout(self.screen_dienap_8)


        self.verticalLayout_212.addWidget(self.widget_label_dienap_4)


        self.verticalLayout_214.addWidget(self.widget_Dienap_4)

        self.stackedWidget.addWidget(self.dienap_5)
        self.suco_5 = QWidget()
        self.suco_5.setObjectName(u"suco_5")
        self.verticalLayout_262 = QVBoxLayout(self.suco_5)
        self.verticalLayout_262.setSpacing(0)
        self.verticalLayout_262.setObjectName(u"verticalLayout_262")
        self.verticalLayout_262.setContentsMargins(0, 0, 0, 0)
        self.widget_369 = QWidget(self.suco_5)
        self.widget_369.setObjectName(u"widget_369")
        self.gridLayout_10 = QGridLayout(self.widget_369)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_370 = QWidget(self.widget_369)
        self.widget_370.setObjectName(u"widget_370")
        sizePolicy.setHeightForWidth(self.widget_370.sizePolicy().hasHeightForWidth())
        self.widget_370.setSizePolicy(sizePolicy)
        self.widget_370.setAutoFillBackground(False)
        self.widget_370.setStyleSheet(u"text-align: center;")
        self.verticalLayout_249 = QVBoxLayout(self.widget_370)
        self.verticalLayout_249.setSpacing(0)
        self.verticalLayout_249.setObjectName(u"verticalLayout_249")
        self.verticalLayout_249.setContentsMargins(0, 0, 0, 0)
        self.label_78 = QLabel(self.widget_370)
        self.label_78.setObjectName(u"label_78")
        sizePolicy3.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy3)
        self.label_78.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_78.setAlignment(Qt.AlignCenter)

        self.verticalLayout_249.addWidget(self.label_78)

        self.widget_371 = QWidget(self.widget_370)
        self.widget_371.setObjectName(u"widget_371")
        sizePolicy.setHeightForWidth(self.widget_371.sizePolicy().hasHeightForWidth())
        self.widget_371.setSizePolicy(sizePolicy)
        self.verticalLayout_250 = QVBoxLayout(self.widget_371)
        self.verticalLayout_250.setSpacing(0)
        self.verticalLayout_250.setObjectName(u"verticalLayout_250")
        self.verticalLayout_250.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_nhietdo_6 = QTableWidget(self.widget_371)
        if (self.tableWidget_nhietdo_6.columnCount() < 3):
            self.tableWidget_nhietdo_6.setColumnCount(3)
        __qtablewidgetitem288 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setHorizontalHeaderItem(0, __qtablewidgetitem288)
        __qtablewidgetitem289 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setHorizontalHeaderItem(1, __qtablewidgetitem289)
        __qtablewidgetitem290 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setHorizontalHeaderItem(2, __qtablewidgetitem290)
        if (self.tableWidget_nhietdo_6.rowCount() < 9):
            self.tableWidget_nhietdo_6.setRowCount(9)
        __qtablewidgetitem291 = QTableWidgetItem()
        __qtablewidgetitem291.setFont(font3);
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(0, __qtablewidgetitem291)
        __qtablewidgetitem292 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(1, __qtablewidgetitem292)
        __qtablewidgetitem293 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(2, __qtablewidgetitem293)
        __qtablewidgetitem294 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(3, __qtablewidgetitem294)
        __qtablewidgetitem295 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(4, __qtablewidgetitem295)
        __qtablewidgetitem296 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(5, __qtablewidgetitem296)
        __qtablewidgetitem297 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(6, __qtablewidgetitem297)
        __qtablewidgetitem298 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(7, __qtablewidgetitem298)
        __qtablewidgetitem299 = QTableWidgetItem()
        self.tableWidget_nhietdo_6.setVerticalHeaderItem(8, __qtablewidgetitem299)
        self.tableWidget_nhietdo_6.setObjectName(u"tableWidget_nhietdo_6")
        sizePolicy.setHeightForWidth(self.tableWidget_nhietdo_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_nhietdo_6.setSizePolicy(sizePolicy)
        self.tableWidget_nhietdo_6.setMinimumSize(QSize(400, 0))
        self.tableWidget_nhietdo_6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_nhietdo_6.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_6.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_nhietdo_6.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_nhietdo_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_nhietdo_6.verticalHeader().setVisible(False)
        self.tableWidget_nhietdo_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_nhietdo_6.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_6.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_250.addWidget(self.tableWidget_nhietdo_6)


        self.verticalLayout_249.addWidget(self.widget_371)

        self.widget_372 = QWidget(self.widget_370)
        self.widget_372.setObjectName(u"widget_372")
        sizePolicy3.setHeightForWidth(self.widget_372.sizePolicy().hasHeightForWidth())
        self.widget_372.setSizePolicy(sizePolicy3)
        self.horizontalLayout_176 = QHBoxLayout(self.widget_372)
        self.horizontalLayout_176.setSpacing(0)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_26 = QPushButton(self.widget_372)
        self.pushButton_exportTem_26.setObjectName(u"pushButton_exportTem_26")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_26.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_26.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_26.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_176.addWidget(self.pushButton_exportTem_26)


        self.verticalLayout_249.addWidget(self.widget_372)


        self.gridLayout_10.addWidget(self.widget_370, 0, 0, 1, 1)

        self.widget_373 = QWidget(self.widget_369)
        self.widget_373.setObjectName(u"widget_373")
        self.verticalLayout_251 = QVBoxLayout(self.widget_373)
        self.verticalLayout_251.setSpacing(0)
        self.verticalLayout_251.setObjectName(u"verticalLayout_251")
        self.verticalLayout_251.setContentsMargins(0, 0, 0, 0)
        self.widget_374 = QWidget(self.widget_373)
        self.widget_374.setObjectName(u"widget_374")
        sizePolicy.setHeightForWidth(self.widget_374.sizePolicy().hasHeightForWidth())
        self.widget_374.setSizePolicy(sizePolicy)
        self.widget_374.setAutoFillBackground(False)
        self.widget_374.setStyleSheet(u"text-align: center;")
        self.verticalLayout_252 = QVBoxLayout(self.widget_374)
        self.verticalLayout_252.setSpacing(0)
        self.verticalLayout_252.setObjectName(u"verticalLayout_252")
        self.verticalLayout_252.setContentsMargins(0, 0, 0, 0)
        self.label_79 = QLabel(self.widget_374)
        self.label_79.setObjectName(u"label_79")
        sizePolicy3.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy3)
        self.label_79.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.verticalLayout_252.addWidget(self.label_79)

        self.widget_375 = QWidget(self.widget_374)
        self.widget_375.setObjectName(u"widget_375")
        sizePolicy.setHeightForWidth(self.widget_375.sizePolicy().hasHeightForWidth())
        self.widget_375.setSizePolicy(sizePolicy)
        self.verticalLayout_253 = QVBoxLayout(self.widget_375)
        self.verticalLayout_253.setSpacing(0)
        self.verticalLayout_253.setObjectName(u"verticalLayout_253")
        self.verticalLayout_253.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc1_6 = QTableWidget(self.widget_375)
        if (self.tableWidget_dc1_6.columnCount() < 3):
            self.tableWidget_dc1_6.setColumnCount(3)
        __qtablewidgetitem300 = QTableWidgetItem()
        self.tableWidget_dc1_6.setHorizontalHeaderItem(0, __qtablewidgetitem300)
        __qtablewidgetitem301 = QTableWidgetItem()
        self.tableWidget_dc1_6.setHorizontalHeaderItem(1, __qtablewidgetitem301)
        __qtablewidgetitem302 = QTableWidgetItem()
        self.tableWidget_dc1_6.setHorizontalHeaderItem(2, __qtablewidgetitem302)
        if (self.tableWidget_dc1_6.rowCount() < 9):
            self.tableWidget_dc1_6.setRowCount(9)
        __qtablewidgetitem303 = QTableWidgetItem()
        __qtablewidgetitem303.setFont(font3);
        self.tableWidget_dc1_6.setVerticalHeaderItem(0, __qtablewidgetitem303)
        __qtablewidgetitem304 = QTableWidgetItem()
        self.tableWidget_dc1_6.setVerticalHeaderItem(1, __qtablewidgetitem304)
        __qtablewidgetitem305 = QTableWidgetItem()
        self.tableWidget_dc1_6.setVerticalHeaderItem(2, __qtablewidgetitem305)
        __qtablewidgetitem306 = QTableWidgetItem()
        self.tableWidget_dc1_6.setVerticalHeaderItem(3, __qtablewidgetitem306)
        __qtablewidgetitem307 = QTableWidgetItem()
        self.tableWidget_dc1_6.setVerticalHeaderItem(4, __qtablewidgetitem307)
        __qtablewidgetitem308 = QTableWidgetItem()
        self.tableWidget_dc1_6.setVerticalHeaderItem(5, __qtablewidgetitem308)
        __qtablewidgetitem309 = QTableWidgetItem()
        self.tableWidget_dc1_6.setVerticalHeaderItem(6, __qtablewidgetitem309)
        __qtablewidgetitem310 = QTableWidgetItem()
        self.tableWidget_dc1_6.setVerticalHeaderItem(7, __qtablewidgetitem310)
        __qtablewidgetitem311 = QTableWidgetItem()
        self.tableWidget_dc1_6.setVerticalHeaderItem(8, __qtablewidgetitem311)
        self.tableWidget_dc1_6.setObjectName(u"tableWidget_dc1_6")
        sizePolicy.setHeightForWidth(self.tableWidget_dc1_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc1_6.setSizePolicy(sizePolicy)
        self.tableWidget_dc1_6.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc1_6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc1_6.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_6.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc1_6.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc1_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc1_6.verticalHeader().setVisible(False)
        self.tableWidget_dc1_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc1_6.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_6.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_253.addWidget(self.tableWidget_dc1_6)


        self.verticalLayout_252.addWidget(self.widget_375)

        self.widget_376 = QWidget(self.widget_374)
        self.widget_376.setObjectName(u"widget_376")
        sizePolicy3.setHeightForWidth(self.widget_376.sizePolicy().hasHeightForWidth())
        self.widget_376.setSizePolicy(sizePolicy3)
        self.horizontalLayout_178 = QHBoxLayout(self.widget_376)
        self.horizontalLayout_178.setSpacing(0)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_27 = QPushButton(self.widget_376)
        self.pushButton_exportTem_27.setObjectName(u"pushButton_exportTem_27")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_27.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_27.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_27.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_178.addWidget(self.pushButton_exportTem_27)


        self.verticalLayout_252.addWidget(self.widget_376)


        self.verticalLayout_251.addWidget(self.widget_374)


        self.gridLayout_10.addWidget(self.widget_373, 0, 1, 1, 1)

        self.widget_377 = QWidget(self.widget_369)
        self.widget_377.setObjectName(u"widget_377")
        sizePolicy.setHeightForWidth(self.widget_377.sizePolicy().hasHeightForWidth())
        self.widget_377.setSizePolicy(sizePolicy)
        self.widget_377.setAutoFillBackground(False)
        self.widget_377.setStyleSheet(u"text-align: center;")
        self.verticalLayout_254 = QVBoxLayout(self.widget_377)
        self.verticalLayout_254.setSpacing(0)
        self.verticalLayout_254.setObjectName(u"verticalLayout_254")
        self.verticalLayout_254.setContentsMargins(0, 0, 0, 0)
        self.label_80 = QLabel(self.widget_377)
        self.label_80.setObjectName(u"label_80")
        sizePolicy3.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy3)
        self.label_80.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_80.setAlignment(Qt.AlignCenter)

        self.verticalLayout_254.addWidget(self.label_80)

        self.widget_378 = QWidget(self.widget_377)
        self.widget_378.setObjectName(u"widget_378")
        sizePolicy.setHeightForWidth(self.widget_378.sizePolicy().hasHeightForWidth())
        self.widget_378.setSizePolicy(sizePolicy)
        self.verticalLayout_255 = QVBoxLayout(self.widget_378)
        self.verticalLayout_255.setSpacing(0)
        self.verticalLayout_255.setObjectName(u"verticalLayout_255")
        self.verticalLayout_255.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac1_5 = QTableWidget(self.widget_378)
        if (self.tableWidget_ac1_5.columnCount() < 3):
            self.tableWidget_ac1_5.setColumnCount(3)
        __qtablewidgetitem312 = QTableWidgetItem()
        self.tableWidget_ac1_5.setHorizontalHeaderItem(0, __qtablewidgetitem312)
        __qtablewidgetitem313 = QTableWidgetItem()
        self.tableWidget_ac1_5.setHorizontalHeaderItem(1, __qtablewidgetitem313)
        __qtablewidgetitem314 = QTableWidgetItem()
        self.tableWidget_ac1_5.setHorizontalHeaderItem(2, __qtablewidgetitem314)
        if (self.tableWidget_ac1_5.rowCount() < 9):
            self.tableWidget_ac1_5.setRowCount(9)
        __qtablewidgetitem315 = QTableWidgetItem()
        __qtablewidgetitem315.setFont(font3);
        self.tableWidget_ac1_5.setVerticalHeaderItem(0, __qtablewidgetitem315)
        __qtablewidgetitem316 = QTableWidgetItem()
        self.tableWidget_ac1_5.setVerticalHeaderItem(1, __qtablewidgetitem316)
        __qtablewidgetitem317 = QTableWidgetItem()
        self.tableWidget_ac1_5.setVerticalHeaderItem(2, __qtablewidgetitem317)
        __qtablewidgetitem318 = QTableWidgetItem()
        self.tableWidget_ac1_5.setVerticalHeaderItem(3, __qtablewidgetitem318)
        __qtablewidgetitem319 = QTableWidgetItem()
        self.tableWidget_ac1_5.setVerticalHeaderItem(4, __qtablewidgetitem319)
        __qtablewidgetitem320 = QTableWidgetItem()
        self.tableWidget_ac1_5.setVerticalHeaderItem(5, __qtablewidgetitem320)
        __qtablewidgetitem321 = QTableWidgetItem()
        self.tableWidget_ac1_5.setVerticalHeaderItem(6, __qtablewidgetitem321)
        __qtablewidgetitem322 = QTableWidgetItem()
        self.tableWidget_ac1_5.setVerticalHeaderItem(7, __qtablewidgetitem322)
        __qtablewidgetitem323 = QTableWidgetItem()
        self.tableWidget_ac1_5.setVerticalHeaderItem(8, __qtablewidgetitem323)
        self.tableWidget_ac1_5.setObjectName(u"tableWidget_ac1_5")
        sizePolicy.setHeightForWidth(self.tableWidget_ac1_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac1_5.setSizePolicy(sizePolicy)
        self.tableWidget_ac1_5.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac1_5.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac1_5.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_5.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac1_5.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac1_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac1_5.verticalHeader().setVisible(False)
        self.tableWidget_ac1_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac1_5.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_5.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_255.addWidget(self.tableWidget_ac1_5)


        self.verticalLayout_254.addWidget(self.widget_378)

        self.widget_379 = QWidget(self.widget_377)
        self.widget_379.setObjectName(u"widget_379")
        sizePolicy3.setHeightForWidth(self.widget_379.sizePolicy().hasHeightForWidth())
        self.widget_379.setSizePolicy(sizePolicy3)
        self.horizontalLayout_179 = QHBoxLayout(self.widget_379)
        self.horizontalLayout_179.setSpacing(0)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_28 = QPushButton(self.widget_379)
        self.pushButton_exportTem_28.setObjectName(u"pushButton_exportTem_28")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_28.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_28.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_28.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_179.addWidget(self.pushButton_exportTem_28)


        self.verticalLayout_254.addWidget(self.widget_379)


        self.gridLayout_10.addWidget(self.widget_377, 0, 2, 1, 1)

        self.widget_380 = QWidget(self.widget_369)
        self.widget_380.setObjectName(u"widget_380")
        sizePolicy.setHeightForWidth(self.widget_380.sizePolicy().hasHeightForWidth())
        self.widget_380.setSizePolicy(sizePolicy)
        self.widget_380.setAutoFillBackground(False)
        self.widget_380.setStyleSheet(u"text-align: center;")
        self.verticalLayout_256 = QVBoxLayout(self.widget_380)
        self.verticalLayout_256.setSpacing(0)
        self.verticalLayout_256.setObjectName(u"verticalLayout_256")
        self.verticalLayout_256.setContentsMargins(0, 0, 0, 0)
        self.label_81 = QLabel(self.widget_380)
        self.label_81.setObjectName(u"label_81")
        sizePolicy3.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy3)
        self.label_81.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_81.setAlignment(Qt.AlignCenter)

        self.verticalLayout_256.addWidget(self.label_81)

        self.widget_381 = QWidget(self.widget_380)
        self.widget_381.setObjectName(u"widget_381")
        sizePolicy.setHeightForWidth(self.widget_381.sizePolicy().hasHeightForWidth())
        self.widget_381.setSizePolicy(sizePolicy)
        self.verticalLayout_257 = QVBoxLayout(self.widget_381)
        self.verticalLayout_257.setSpacing(0)
        self.verticalLayout_257.setObjectName(u"verticalLayout_257")
        self.verticalLayout_257.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_doam_6 = QTableWidget(self.widget_381)
        if (self.tableWidget_doam_6.columnCount() < 3):
            self.tableWidget_doam_6.setColumnCount(3)
        __qtablewidgetitem324 = QTableWidgetItem()
        self.tableWidget_doam_6.setHorizontalHeaderItem(0, __qtablewidgetitem324)
        __qtablewidgetitem325 = QTableWidgetItem()
        self.tableWidget_doam_6.setHorizontalHeaderItem(1, __qtablewidgetitem325)
        __qtablewidgetitem326 = QTableWidgetItem()
        self.tableWidget_doam_6.setHorizontalHeaderItem(2, __qtablewidgetitem326)
        if (self.tableWidget_doam_6.rowCount() < 9):
            self.tableWidget_doam_6.setRowCount(9)
        __qtablewidgetitem327 = QTableWidgetItem()
        __qtablewidgetitem327.setFont(font3);
        self.tableWidget_doam_6.setVerticalHeaderItem(0, __qtablewidgetitem327)
        __qtablewidgetitem328 = QTableWidgetItem()
        self.tableWidget_doam_6.setVerticalHeaderItem(1, __qtablewidgetitem328)
        __qtablewidgetitem329 = QTableWidgetItem()
        self.tableWidget_doam_6.setVerticalHeaderItem(2, __qtablewidgetitem329)
        __qtablewidgetitem330 = QTableWidgetItem()
        self.tableWidget_doam_6.setVerticalHeaderItem(3, __qtablewidgetitem330)
        __qtablewidgetitem331 = QTableWidgetItem()
        self.tableWidget_doam_6.setVerticalHeaderItem(4, __qtablewidgetitem331)
        __qtablewidgetitem332 = QTableWidgetItem()
        self.tableWidget_doam_6.setVerticalHeaderItem(5, __qtablewidgetitem332)
        __qtablewidgetitem333 = QTableWidgetItem()
        self.tableWidget_doam_6.setVerticalHeaderItem(6, __qtablewidgetitem333)
        __qtablewidgetitem334 = QTableWidgetItem()
        self.tableWidget_doam_6.setVerticalHeaderItem(7, __qtablewidgetitem334)
        __qtablewidgetitem335 = QTableWidgetItem()
        self.tableWidget_doam_6.setVerticalHeaderItem(8, __qtablewidgetitem335)
        self.tableWidget_doam_6.setObjectName(u"tableWidget_doam_6")
        sizePolicy.setHeightForWidth(self.tableWidget_doam_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_doam_6.setSizePolicy(sizePolicy)
        self.tableWidget_doam_6.setMinimumSize(QSize(400, 0))
        self.tableWidget_doam_6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_doam_6.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_6.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_doam_6.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_doam_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_doam_6.verticalHeader().setVisible(False)
        self.tableWidget_doam_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_doam_6.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_6.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_257.addWidget(self.tableWidget_doam_6)


        self.verticalLayout_256.addWidget(self.widget_381)

        self.widget_382 = QWidget(self.widget_380)
        self.widget_382.setObjectName(u"widget_382")
        sizePolicy3.setHeightForWidth(self.widget_382.sizePolicy().hasHeightForWidth())
        self.widget_382.setSizePolicy(sizePolicy3)
        self.horizontalLayout_180 = QHBoxLayout(self.widget_382)
        self.horizontalLayout_180.setSpacing(0)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_29 = QPushButton(self.widget_382)
        self.pushButton_exportTem_29.setObjectName(u"pushButton_exportTem_29")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_29.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_29.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_29.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_180.addWidget(self.pushButton_exportTem_29)


        self.verticalLayout_256.addWidget(self.widget_382)


        self.gridLayout_10.addWidget(self.widget_380, 1, 0, 1, 1)

        self.widget_383 = QWidget(self.widget_369)
        self.widget_383.setObjectName(u"widget_383")
        sizePolicy.setHeightForWidth(self.widget_383.sizePolicy().hasHeightForWidth())
        self.widget_383.setSizePolicy(sizePolicy)
        self.widget_383.setAutoFillBackground(False)
        self.widget_383.setStyleSheet(u"text-align: center;")
        self.verticalLayout_258 = QVBoxLayout(self.widget_383)
        self.verticalLayout_258.setSpacing(0)
        self.verticalLayout_258.setObjectName(u"verticalLayout_258")
        self.verticalLayout_258.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.widget_383)
        self.label_82.setObjectName(u"label_82")
        sizePolicy3.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy3)
        self.label_82.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_82.setAlignment(Qt.AlignCenter)

        self.verticalLayout_258.addWidget(self.label_82)

        self.widget_384 = QWidget(self.widget_383)
        self.widget_384.setObjectName(u"widget_384")
        sizePolicy.setHeightForWidth(self.widget_384.sizePolicy().hasHeightForWidth())
        self.widget_384.setSizePolicy(sizePolicy)
        self.verticalLayout_259 = QVBoxLayout(self.widget_384)
        self.verticalLayout_259.setSpacing(0)
        self.verticalLayout_259.setObjectName(u"verticalLayout_259")
        self.verticalLayout_259.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc2_6 = QTableWidget(self.widget_384)
        if (self.tableWidget_dc2_6.columnCount() < 3):
            self.tableWidget_dc2_6.setColumnCount(3)
        __qtablewidgetitem336 = QTableWidgetItem()
        self.tableWidget_dc2_6.setHorizontalHeaderItem(0, __qtablewidgetitem336)
        __qtablewidgetitem337 = QTableWidgetItem()
        self.tableWidget_dc2_6.setHorizontalHeaderItem(1, __qtablewidgetitem337)
        __qtablewidgetitem338 = QTableWidgetItem()
        self.tableWidget_dc2_6.setHorizontalHeaderItem(2, __qtablewidgetitem338)
        if (self.tableWidget_dc2_6.rowCount() < 9):
            self.tableWidget_dc2_6.setRowCount(9)
        __qtablewidgetitem339 = QTableWidgetItem()
        __qtablewidgetitem339.setFont(font3);
        self.tableWidget_dc2_6.setVerticalHeaderItem(0, __qtablewidgetitem339)
        __qtablewidgetitem340 = QTableWidgetItem()
        self.tableWidget_dc2_6.setVerticalHeaderItem(1, __qtablewidgetitem340)
        __qtablewidgetitem341 = QTableWidgetItem()
        self.tableWidget_dc2_6.setVerticalHeaderItem(2, __qtablewidgetitem341)
        __qtablewidgetitem342 = QTableWidgetItem()
        self.tableWidget_dc2_6.setVerticalHeaderItem(3, __qtablewidgetitem342)
        __qtablewidgetitem343 = QTableWidgetItem()
        self.tableWidget_dc2_6.setVerticalHeaderItem(4, __qtablewidgetitem343)
        __qtablewidgetitem344 = QTableWidgetItem()
        self.tableWidget_dc2_6.setVerticalHeaderItem(5, __qtablewidgetitem344)
        __qtablewidgetitem345 = QTableWidgetItem()
        self.tableWidget_dc2_6.setVerticalHeaderItem(6, __qtablewidgetitem345)
        __qtablewidgetitem346 = QTableWidgetItem()
        self.tableWidget_dc2_6.setVerticalHeaderItem(7, __qtablewidgetitem346)
        __qtablewidgetitem347 = QTableWidgetItem()
        self.tableWidget_dc2_6.setVerticalHeaderItem(8, __qtablewidgetitem347)
        self.tableWidget_dc2_6.setObjectName(u"tableWidget_dc2_6")
        sizePolicy.setHeightForWidth(self.tableWidget_dc2_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc2_6.setSizePolicy(sizePolicy)
        self.tableWidget_dc2_6.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc2_6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc2_6.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_6.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc2_6.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc2_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc2_6.verticalHeader().setVisible(False)
        self.tableWidget_dc2_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc2_6.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_6.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_259.addWidget(self.tableWidget_dc2_6)


        self.verticalLayout_258.addWidget(self.widget_384)

        self.widget_385 = QWidget(self.widget_383)
        self.widget_385.setObjectName(u"widget_385")
        sizePolicy3.setHeightForWidth(self.widget_385.sizePolicy().hasHeightForWidth())
        self.widget_385.setSizePolicy(sizePolicy3)
        self.horizontalLayout_181 = QHBoxLayout(self.widget_385)
        self.horizontalLayout_181.setSpacing(0)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_30 = QPushButton(self.widget_385)
        self.pushButton_exportTem_30.setObjectName(u"pushButton_exportTem_30")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_30.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_30.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_30.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_181.addWidget(self.pushButton_exportTem_30)


        self.verticalLayout_258.addWidget(self.widget_385)


        self.gridLayout_10.addWidget(self.widget_383, 1, 1, 1, 1)

        self.widget_386 = QWidget(self.widget_369)
        self.widget_386.setObjectName(u"widget_386")
        sizePolicy.setHeightForWidth(self.widget_386.sizePolicy().hasHeightForWidth())
        self.widget_386.setSizePolicy(sizePolicy)
        self.widget_386.setAutoFillBackground(False)
        self.widget_386.setStyleSheet(u"text-align: center;")
        self.verticalLayout_260 = QVBoxLayout(self.widget_386)
        self.verticalLayout_260.setSpacing(0)
        self.verticalLayout_260.setObjectName(u"verticalLayout_260")
        self.verticalLayout_260.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.widget_386)
        self.label_83.setObjectName(u"label_83")
        sizePolicy3.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy3)
        self.label_83.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.verticalLayout_260.addWidget(self.label_83)

        self.widget_387 = QWidget(self.widget_386)
        self.widget_387.setObjectName(u"widget_387")
        sizePolicy.setHeightForWidth(self.widget_387.sizePolicy().hasHeightForWidth())
        self.widget_387.setSizePolicy(sizePolicy)
        self.verticalLayout_261 = QVBoxLayout(self.widget_387)
        self.verticalLayout_261.setSpacing(0)
        self.verticalLayout_261.setObjectName(u"verticalLayout_261")
        self.verticalLayout_261.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac2_5 = QTableWidget(self.widget_387)
        if (self.tableWidget_ac2_5.columnCount() < 3):
            self.tableWidget_ac2_5.setColumnCount(3)
        __qtablewidgetitem348 = QTableWidgetItem()
        self.tableWidget_ac2_5.setHorizontalHeaderItem(0, __qtablewidgetitem348)
        __qtablewidgetitem349 = QTableWidgetItem()
        self.tableWidget_ac2_5.setHorizontalHeaderItem(1, __qtablewidgetitem349)
        __qtablewidgetitem350 = QTableWidgetItem()
        self.tableWidget_ac2_5.setHorizontalHeaderItem(2, __qtablewidgetitem350)
        if (self.tableWidget_ac2_5.rowCount() < 9):
            self.tableWidget_ac2_5.setRowCount(9)
        __qtablewidgetitem351 = QTableWidgetItem()
        __qtablewidgetitem351.setFont(font3);
        self.tableWidget_ac2_5.setVerticalHeaderItem(0, __qtablewidgetitem351)
        __qtablewidgetitem352 = QTableWidgetItem()
        self.tableWidget_ac2_5.setVerticalHeaderItem(1, __qtablewidgetitem352)
        __qtablewidgetitem353 = QTableWidgetItem()
        self.tableWidget_ac2_5.setVerticalHeaderItem(2, __qtablewidgetitem353)
        __qtablewidgetitem354 = QTableWidgetItem()
        self.tableWidget_ac2_5.setVerticalHeaderItem(3, __qtablewidgetitem354)
        __qtablewidgetitem355 = QTableWidgetItem()
        self.tableWidget_ac2_5.setVerticalHeaderItem(4, __qtablewidgetitem355)
        __qtablewidgetitem356 = QTableWidgetItem()
        self.tableWidget_ac2_5.setVerticalHeaderItem(5, __qtablewidgetitem356)
        __qtablewidgetitem357 = QTableWidgetItem()
        self.tableWidget_ac2_5.setVerticalHeaderItem(6, __qtablewidgetitem357)
        __qtablewidgetitem358 = QTableWidgetItem()
        self.tableWidget_ac2_5.setVerticalHeaderItem(7, __qtablewidgetitem358)
        __qtablewidgetitem359 = QTableWidgetItem()
        self.tableWidget_ac2_5.setVerticalHeaderItem(8, __qtablewidgetitem359)
        self.tableWidget_ac2_5.setObjectName(u"tableWidget_ac2_5")
        sizePolicy.setHeightForWidth(self.tableWidget_ac2_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac2_5.setSizePolicy(sizePolicy)
        self.tableWidget_ac2_5.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac2_5.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac2_5.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_5.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac2_5.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac2_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac2_5.verticalHeader().setVisible(False)
        self.tableWidget_ac2_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac2_5.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_5.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_261.addWidget(self.tableWidget_ac2_5)


        self.verticalLayout_260.addWidget(self.widget_387)

        self.widget_388 = QWidget(self.widget_386)
        self.widget_388.setObjectName(u"widget_388")
        sizePolicy3.setHeightForWidth(self.widget_388.sizePolicy().hasHeightForWidth())
        self.widget_388.setSizePolicy(sizePolicy3)
        self.horizontalLayout_182 = QHBoxLayout(self.widget_388)
        self.horizontalLayout_182.setSpacing(0)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_31 = QPushButton(self.widget_388)
        self.pushButton_exportTem_31.setObjectName(u"pushButton_exportTem_31")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_31.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_31.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_31.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_182.addWidget(self.pushButton_exportTem_31)


        self.verticalLayout_260.addWidget(self.widget_388)


        self.gridLayout_10.addWidget(self.widget_386, 1, 2, 1, 1)


        self.verticalLayout_262.addWidget(self.widget_369)

        self.stackedWidget.addWidget(self.suco_5)
        self.nhietdo_6 = QWidget()
        self.nhietdo_6.setObjectName(u"nhietdo_6")
        self.verticalLayout_353 = QVBoxLayout(self.nhietdo_6)
        self.verticalLayout_353.setSpacing(0)
        self.verticalLayout_353.setObjectName(u"verticalLayout_353")
        self.verticalLayout_353.setContentsMargins(0, 0, 0, 0)
        self.Nhietdo_widget_11 = QWidget(self.nhietdo_6)
        self.Nhietdo_widget_11.setObjectName(u"Nhietdo_widget_11")
        self.Nhietdo_widget_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_352 = QVBoxLayout(self.Nhietdo_widget_11)
        self.verticalLayout_352.setSpacing(0)
        self.verticalLayout_352.setObjectName(u"verticalLayout_352")
        self.verticalLayout_352.setContentsMargins(0, 0, 0, 0)
        self.title_nhietdo_11 = QLabel(self.Nhietdo_widget_11)
        self.title_nhietdo_11.setObjectName(u"title_nhietdo_11")
        sizePolicy3.setHeightForWidth(self.title_nhietdo_11.sizePolicy().hasHeightForWidth())
        self.title_nhietdo_11.setSizePolicy(sizePolicy3)
        self.title_nhietdo_11.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.title_nhietdo_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_352.addWidget(self.title_nhietdo_11)

        self.thoigian_nhietdo_11 = QLabel(self.Nhietdo_widget_11)
        self.thoigian_nhietdo_11.setObjectName(u"thoigian_nhietdo_11")
        sizePolicy3.setHeightForWidth(self.thoigian_nhietdo_11.sizePolicy().hasHeightForWidth())
        self.thoigian_nhietdo_11.setSizePolicy(sizePolicy3)
        self.thoigian_nhietdo_11.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.thoigian_nhietdo_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_352.addWidget(self.thoigian_nhietdo_11)

        self.widget_609 = QWidget(self.Nhietdo_widget_11)
        self.widget_609.setObjectName(u"widget_609")
        sizePolicy.setHeightForWidth(self.widget_609.sizePolicy().hasHeightForWidth())
        self.widget_609.setSizePolicy(sizePolicy)
        self.widget_609.setMinimumSize(QSize(0, 0))
        self.gridLayout_15 = QGridLayout(self.widget_609)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_22, 0, 1, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_37, 1, 2, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_23, 2, 1, 1, 1)

        self.screen_nhietdo_11 = QVBoxLayout()
        self.screen_nhietdo_11.setSpacing(0)
        self.screen_nhietdo_11.setObjectName(u"screen_nhietdo_11")
        self.screen_nhietdo_11.setSizeConstraint(QLayout.SetMaximumSize)
        self.screen_nhietdo_11.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_15.addLayout(self.screen_nhietdo_11, 1, 1, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_38, 1, 0, 1, 1)


        self.verticalLayout_352.addWidget(self.widget_609)


        self.verticalLayout_353.addWidget(self.Nhietdo_widget_11)

        self.stackedWidget.addWidget(self.nhietdo_6)
        self.dienap_6 = QWidget()
        self.dienap_6.setObjectName(u"dienap_6")
        self.verticalLayout_217 = QVBoxLayout(self.dienap_6)
        self.verticalLayout_217.setSpacing(0)
        self.verticalLayout_217.setObjectName(u"verticalLayout_217")
        self.verticalLayout_217.setContentsMargins(0, 0, 0, 0)
        self.widget_Dienap_5 = QWidget(self.dienap_6)
        self.widget_Dienap_5.setObjectName(u"widget_Dienap_5")
        self.widget_Dienap_5.setStyleSheet(u"")
        self.verticalLayout_215 = QVBoxLayout(self.widget_Dienap_5)
        self.verticalLayout_215.setSpacing(0)
        self.verticalLayout_215.setObjectName(u"verticalLayout_215")
        self.verticalLayout_215.setContentsMargins(0, 0, 0, 0)
        self.widget_label_dienap_5 = QWidget(self.widget_Dienap_5)
        self.widget_label_dienap_5.setObjectName(u"widget_label_dienap_5")
        sizePolicy.setHeightForWidth(self.widget_label_dienap_5.sizePolicy().hasHeightForWidth())
        self.widget_label_dienap_5.setSizePolicy(sizePolicy)
        self.widget_label_dienap_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_dienap_5.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_216 = QVBoxLayout(self.widget_label_dienap_5)
        self.verticalLayout_216.setSpacing(0)
        self.verticalLayout_216.setObjectName(u"verticalLayout_216")
        self.verticalLayout_216.setContentsMargins(0, 0, 0, 0)
        self.label_diepap_5 = QLabel(self.widget_label_dienap_5)
        self.label_diepap_5.setObjectName(u"label_diepap_5")
        sizePolicy3.setHeightForWidth(self.label_diepap_5.sizePolicy().hasHeightForWidth())
        self.label_diepap_5.setSizePolicy(sizePolicy3)
        self.label_diepap_5.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_diepap_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_216.addWidget(self.label_diepap_5)

        self.label_thoigian_dienap_5 = QLabel(self.widget_label_dienap_5)
        self.label_thoigian_dienap_5.setObjectName(u"label_thoigian_dienap_5")
        sizePolicy3.setHeightForWidth(self.label_thoigian_dienap_5.sizePolicy().hasHeightForWidth())
        self.label_thoigian_dienap_5.setSizePolicy(sizePolicy3)
        self.label_thoigian_dienap_5.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_dienap_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_216.addWidget(self.label_thoigian_dienap_5)

        self.screen_dienap_9 = QVBoxLayout()
        self.screen_dienap_9.setSpacing(0)
        self.screen_dienap_9.setObjectName(u"screen_dienap_9")
        self.screen_dienap_9.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_216.addLayout(self.screen_dienap_9)

        self.screen_dienap_10 = QVBoxLayout()
        self.screen_dienap_10.setSpacing(0)
        self.screen_dienap_10.setObjectName(u"screen_dienap_10")
        self.screen_dienap_10.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_216.addLayout(self.screen_dienap_10)


        self.verticalLayout_215.addWidget(self.widget_label_dienap_5)


        self.verticalLayout_217.addWidget(self.widget_Dienap_5)

        self.stackedWidget.addWidget(self.dienap_6)
        self.suco_6 = QWidget()
        self.suco_6.setObjectName(u"suco_6")
        self.verticalLayout_276 = QVBoxLayout(self.suco_6)
        self.verticalLayout_276.setSpacing(0)
        self.verticalLayout_276.setObjectName(u"verticalLayout_276")
        self.verticalLayout_276.setContentsMargins(0, 0, 0, 0)
        self.widget_389 = QWidget(self.suco_6)
        self.widget_389.setObjectName(u"widget_389")
        self.gridLayout_11 = QGridLayout(self.widget_389)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_390 = QWidget(self.widget_389)
        self.widget_390.setObjectName(u"widget_390")
        sizePolicy.setHeightForWidth(self.widget_390.sizePolicy().hasHeightForWidth())
        self.widget_390.setSizePolicy(sizePolicy)
        self.widget_390.setAutoFillBackground(False)
        self.widget_390.setStyleSheet(u"text-align: center;")
        self.verticalLayout_263 = QVBoxLayout(self.widget_390)
        self.verticalLayout_263.setSpacing(0)
        self.verticalLayout_263.setObjectName(u"verticalLayout_263")
        self.verticalLayout_263.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.widget_390)
        self.label_84.setObjectName(u"label_84")
        sizePolicy3.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy3)
        self.label_84.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_84.setAlignment(Qt.AlignCenter)

        self.verticalLayout_263.addWidget(self.label_84)

        self.widget_391 = QWidget(self.widget_390)
        self.widget_391.setObjectName(u"widget_391")
        sizePolicy.setHeightForWidth(self.widget_391.sizePolicy().hasHeightForWidth())
        self.widget_391.setSizePolicy(sizePolicy)
        self.verticalLayout_264 = QVBoxLayout(self.widget_391)
        self.verticalLayout_264.setSpacing(0)
        self.verticalLayout_264.setObjectName(u"verticalLayout_264")
        self.verticalLayout_264.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_nhietdo_7 = QTableWidget(self.widget_391)
        if (self.tableWidget_nhietdo_7.columnCount() < 3):
            self.tableWidget_nhietdo_7.setColumnCount(3)
        __qtablewidgetitem360 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setHorizontalHeaderItem(0, __qtablewidgetitem360)
        __qtablewidgetitem361 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setHorizontalHeaderItem(1, __qtablewidgetitem361)
        __qtablewidgetitem362 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setHorizontalHeaderItem(2, __qtablewidgetitem362)
        if (self.tableWidget_nhietdo_7.rowCount() < 9):
            self.tableWidget_nhietdo_7.setRowCount(9)
        __qtablewidgetitem363 = QTableWidgetItem()
        __qtablewidgetitem363.setFont(font3);
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(0, __qtablewidgetitem363)
        __qtablewidgetitem364 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(1, __qtablewidgetitem364)
        __qtablewidgetitem365 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(2, __qtablewidgetitem365)
        __qtablewidgetitem366 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(3, __qtablewidgetitem366)
        __qtablewidgetitem367 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(4, __qtablewidgetitem367)
        __qtablewidgetitem368 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(5, __qtablewidgetitem368)
        __qtablewidgetitem369 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(6, __qtablewidgetitem369)
        __qtablewidgetitem370 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(7, __qtablewidgetitem370)
        __qtablewidgetitem371 = QTableWidgetItem()
        self.tableWidget_nhietdo_7.setVerticalHeaderItem(8, __qtablewidgetitem371)
        self.tableWidget_nhietdo_7.setObjectName(u"tableWidget_nhietdo_7")
        sizePolicy.setHeightForWidth(self.tableWidget_nhietdo_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_nhietdo_7.setSizePolicy(sizePolicy)
        self.tableWidget_nhietdo_7.setMinimumSize(QSize(400, 0))
        self.tableWidget_nhietdo_7.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_nhietdo_7.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_7.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_nhietdo_7.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_nhietdo_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_nhietdo_7.verticalHeader().setVisible(False)
        self.tableWidget_nhietdo_7.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_nhietdo_7.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_nhietdo_7.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_264.addWidget(self.tableWidget_nhietdo_7)


        self.verticalLayout_263.addWidget(self.widget_391)

        self.widget_392 = QWidget(self.widget_390)
        self.widget_392.setObjectName(u"widget_392")
        sizePolicy3.setHeightForWidth(self.widget_392.sizePolicy().hasHeightForWidth())
        self.widget_392.setSizePolicy(sizePolicy3)
        self.horizontalLayout_183 = QHBoxLayout(self.widget_392)
        self.horizontalLayout_183.setSpacing(0)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.horizontalLayout_183.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_32 = QPushButton(self.widget_392)
        self.pushButton_exportTem_32.setObjectName(u"pushButton_exportTem_32")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_32.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_32.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_32.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_183.addWidget(self.pushButton_exportTem_32)


        self.verticalLayout_263.addWidget(self.widget_392)


        self.gridLayout_11.addWidget(self.widget_390, 0, 0, 1, 1)

        self.widget_393 = QWidget(self.widget_389)
        self.widget_393.setObjectName(u"widget_393")
        self.verticalLayout_265 = QVBoxLayout(self.widget_393)
        self.verticalLayout_265.setSpacing(0)
        self.verticalLayout_265.setObjectName(u"verticalLayout_265")
        self.verticalLayout_265.setContentsMargins(0, 0, 0, 0)
        self.widget_394 = QWidget(self.widget_393)
        self.widget_394.setObjectName(u"widget_394")
        sizePolicy.setHeightForWidth(self.widget_394.sizePolicy().hasHeightForWidth())
        self.widget_394.setSizePolicy(sizePolicy)
        self.widget_394.setAutoFillBackground(False)
        self.widget_394.setStyleSheet(u"text-align: center;")
        self.verticalLayout_266 = QVBoxLayout(self.widget_394)
        self.verticalLayout_266.setSpacing(0)
        self.verticalLayout_266.setObjectName(u"verticalLayout_266")
        self.verticalLayout_266.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.widget_394)
        self.label_85.setObjectName(u"label_85")
        sizePolicy3.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy3)
        self.label_85.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.verticalLayout_266.addWidget(self.label_85)

        self.widget_395 = QWidget(self.widget_394)
        self.widget_395.setObjectName(u"widget_395")
        sizePolicy.setHeightForWidth(self.widget_395.sizePolicy().hasHeightForWidth())
        self.widget_395.setSizePolicy(sizePolicy)
        self.verticalLayout_267 = QVBoxLayout(self.widget_395)
        self.verticalLayout_267.setSpacing(0)
        self.verticalLayout_267.setObjectName(u"verticalLayout_267")
        self.verticalLayout_267.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc1_7 = QTableWidget(self.widget_395)
        if (self.tableWidget_dc1_7.columnCount() < 3):
            self.tableWidget_dc1_7.setColumnCount(3)
        __qtablewidgetitem372 = QTableWidgetItem()
        self.tableWidget_dc1_7.setHorizontalHeaderItem(0, __qtablewidgetitem372)
        __qtablewidgetitem373 = QTableWidgetItem()
        self.tableWidget_dc1_7.setHorizontalHeaderItem(1, __qtablewidgetitem373)
        __qtablewidgetitem374 = QTableWidgetItem()
        self.tableWidget_dc1_7.setHorizontalHeaderItem(2, __qtablewidgetitem374)
        if (self.tableWidget_dc1_7.rowCount() < 9):
            self.tableWidget_dc1_7.setRowCount(9)
        __qtablewidgetitem375 = QTableWidgetItem()
        __qtablewidgetitem375.setFont(font3);
        self.tableWidget_dc1_7.setVerticalHeaderItem(0, __qtablewidgetitem375)
        __qtablewidgetitem376 = QTableWidgetItem()
        self.tableWidget_dc1_7.setVerticalHeaderItem(1, __qtablewidgetitem376)
        __qtablewidgetitem377 = QTableWidgetItem()
        self.tableWidget_dc1_7.setVerticalHeaderItem(2, __qtablewidgetitem377)
        __qtablewidgetitem378 = QTableWidgetItem()
        self.tableWidget_dc1_7.setVerticalHeaderItem(3, __qtablewidgetitem378)
        __qtablewidgetitem379 = QTableWidgetItem()
        self.tableWidget_dc1_7.setVerticalHeaderItem(4, __qtablewidgetitem379)
        __qtablewidgetitem380 = QTableWidgetItem()
        self.tableWidget_dc1_7.setVerticalHeaderItem(5, __qtablewidgetitem380)
        __qtablewidgetitem381 = QTableWidgetItem()
        self.tableWidget_dc1_7.setVerticalHeaderItem(6, __qtablewidgetitem381)
        __qtablewidgetitem382 = QTableWidgetItem()
        self.tableWidget_dc1_7.setVerticalHeaderItem(7, __qtablewidgetitem382)
        __qtablewidgetitem383 = QTableWidgetItem()
        self.tableWidget_dc1_7.setVerticalHeaderItem(8, __qtablewidgetitem383)
        self.tableWidget_dc1_7.setObjectName(u"tableWidget_dc1_7")
        sizePolicy.setHeightForWidth(self.tableWidget_dc1_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc1_7.setSizePolicy(sizePolicy)
        self.tableWidget_dc1_7.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc1_7.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc1_7.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_7.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc1_7.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc1_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc1_7.verticalHeader().setVisible(False)
        self.tableWidget_dc1_7.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc1_7.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc1_7.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_267.addWidget(self.tableWidget_dc1_7)


        self.verticalLayout_266.addWidget(self.widget_395)

        self.widget_396 = QWidget(self.widget_394)
        self.widget_396.setObjectName(u"widget_396")
        sizePolicy3.setHeightForWidth(self.widget_396.sizePolicy().hasHeightForWidth())
        self.widget_396.setSizePolicy(sizePolicy3)
        self.horizontalLayout_184 = QHBoxLayout(self.widget_396)
        self.horizontalLayout_184.setSpacing(0)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_33 = QPushButton(self.widget_396)
        self.pushButton_exportTem_33.setObjectName(u"pushButton_exportTem_33")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_33.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_33.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_33.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_184.addWidget(self.pushButton_exportTem_33)


        self.verticalLayout_266.addWidget(self.widget_396)


        self.verticalLayout_265.addWidget(self.widget_394)


        self.gridLayout_11.addWidget(self.widget_393, 0, 1, 1, 1)

        self.widget_397 = QWidget(self.widget_389)
        self.widget_397.setObjectName(u"widget_397")
        sizePolicy.setHeightForWidth(self.widget_397.sizePolicy().hasHeightForWidth())
        self.widget_397.setSizePolicy(sizePolicy)
        self.widget_397.setAutoFillBackground(False)
        self.widget_397.setStyleSheet(u"text-align: center;")
        self.verticalLayout_268 = QVBoxLayout(self.widget_397)
        self.verticalLayout_268.setSpacing(0)
        self.verticalLayout_268.setObjectName(u"verticalLayout_268")
        self.verticalLayout_268.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.widget_397)
        self.label_86.setObjectName(u"label_86")
        sizePolicy3.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy3)
        self.label_86.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.verticalLayout_268.addWidget(self.label_86)

        self.widget_398 = QWidget(self.widget_397)
        self.widget_398.setObjectName(u"widget_398")
        sizePolicy.setHeightForWidth(self.widget_398.sizePolicy().hasHeightForWidth())
        self.widget_398.setSizePolicy(sizePolicy)
        self.verticalLayout_269 = QVBoxLayout(self.widget_398)
        self.verticalLayout_269.setSpacing(0)
        self.verticalLayout_269.setObjectName(u"verticalLayout_269")
        self.verticalLayout_269.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac1_6 = QTableWidget(self.widget_398)
        if (self.tableWidget_ac1_6.columnCount() < 3):
            self.tableWidget_ac1_6.setColumnCount(3)
        __qtablewidgetitem384 = QTableWidgetItem()
        self.tableWidget_ac1_6.setHorizontalHeaderItem(0, __qtablewidgetitem384)
        __qtablewidgetitem385 = QTableWidgetItem()
        self.tableWidget_ac1_6.setHorizontalHeaderItem(1, __qtablewidgetitem385)
        __qtablewidgetitem386 = QTableWidgetItem()
        self.tableWidget_ac1_6.setHorizontalHeaderItem(2, __qtablewidgetitem386)
        if (self.tableWidget_ac1_6.rowCount() < 9):
            self.tableWidget_ac1_6.setRowCount(9)
        __qtablewidgetitem387 = QTableWidgetItem()
        __qtablewidgetitem387.setFont(font3);
        self.tableWidget_ac1_6.setVerticalHeaderItem(0, __qtablewidgetitem387)
        __qtablewidgetitem388 = QTableWidgetItem()
        self.tableWidget_ac1_6.setVerticalHeaderItem(1, __qtablewidgetitem388)
        __qtablewidgetitem389 = QTableWidgetItem()
        self.tableWidget_ac1_6.setVerticalHeaderItem(2, __qtablewidgetitem389)
        __qtablewidgetitem390 = QTableWidgetItem()
        self.tableWidget_ac1_6.setVerticalHeaderItem(3, __qtablewidgetitem390)
        __qtablewidgetitem391 = QTableWidgetItem()
        self.tableWidget_ac1_6.setVerticalHeaderItem(4, __qtablewidgetitem391)
        __qtablewidgetitem392 = QTableWidgetItem()
        self.tableWidget_ac1_6.setVerticalHeaderItem(5, __qtablewidgetitem392)
        __qtablewidgetitem393 = QTableWidgetItem()
        self.tableWidget_ac1_6.setVerticalHeaderItem(6, __qtablewidgetitem393)
        __qtablewidgetitem394 = QTableWidgetItem()
        self.tableWidget_ac1_6.setVerticalHeaderItem(7, __qtablewidgetitem394)
        __qtablewidgetitem395 = QTableWidgetItem()
        self.tableWidget_ac1_6.setVerticalHeaderItem(8, __qtablewidgetitem395)
        self.tableWidget_ac1_6.setObjectName(u"tableWidget_ac1_6")
        sizePolicy.setHeightForWidth(self.tableWidget_ac1_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac1_6.setSizePolicy(sizePolicy)
        self.tableWidget_ac1_6.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac1_6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac1_6.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_6.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac1_6.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac1_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac1_6.verticalHeader().setVisible(False)
        self.tableWidget_ac1_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac1_6.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac1_6.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_269.addWidget(self.tableWidget_ac1_6)


        self.verticalLayout_268.addWidget(self.widget_398)

        self.widget_399 = QWidget(self.widget_397)
        self.widget_399.setObjectName(u"widget_399")
        sizePolicy3.setHeightForWidth(self.widget_399.sizePolicy().hasHeightForWidth())
        self.widget_399.setSizePolicy(sizePolicy3)
        self.horizontalLayout_185 = QHBoxLayout(self.widget_399)
        self.horizontalLayout_185.setSpacing(0)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.horizontalLayout_185.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_34 = QPushButton(self.widget_399)
        self.pushButton_exportTem_34.setObjectName(u"pushButton_exportTem_34")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_34.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_34.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_34.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_185.addWidget(self.pushButton_exportTem_34)


        self.verticalLayout_268.addWidget(self.widget_399)


        self.gridLayout_11.addWidget(self.widget_397, 0, 2, 1, 1)

        self.widget_400 = QWidget(self.widget_389)
        self.widget_400.setObjectName(u"widget_400")
        sizePolicy.setHeightForWidth(self.widget_400.sizePolicy().hasHeightForWidth())
        self.widget_400.setSizePolicy(sizePolicy)
        self.widget_400.setAutoFillBackground(False)
        self.widget_400.setStyleSheet(u"text-align: center;")
        self.verticalLayout_270 = QVBoxLayout(self.widget_400)
        self.verticalLayout_270.setSpacing(0)
        self.verticalLayout_270.setObjectName(u"verticalLayout_270")
        self.verticalLayout_270.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.widget_400)
        self.label_87.setObjectName(u"label_87")
        sizePolicy3.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy3)
        self.label_87.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.verticalLayout_270.addWidget(self.label_87)

        self.widget_401 = QWidget(self.widget_400)
        self.widget_401.setObjectName(u"widget_401")
        sizePolicy.setHeightForWidth(self.widget_401.sizePolicy().hasHeightForWidth())
        self.widget_401.setSizePolicy(sizePolicy)
        self.verticalLayout_271 = QVBoxLayout(self.widget_401)
        self.verticalLayout_271.setSpacing(0)
        self.verticalLayout_271.setObjectName(u"verticalLayout_271")
        self.verticalLayout_271.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_doam_7 = QTableWidget(self.widget_401)
        if (self.tableWidget_doam_7.columnCount() < 3):
            self.tableWidget_doam_7.setColumnCount(3)
        __qtablewidgetitem396 = QTableWidgetItem()
        self.tableWidget_doam_7.setHorizontalHeaderItem(0, __qtablewidgetitem396)
        __qtablewidgetitem397 = QTableWidgetItem()
        self.tableWidget_doam_7.setHorizontalHeaderItem(1, __qtablewidgetitem397)
        __qtablewidgetitem398 = QTableWidgetItem()
        self.tableWidget_doam_7.setHorizontalHeaderItem(2, __qtablewidgetitem398)
        if (self.tableWidget_doam_7.rowCount() < 9):
            self.tableWidget_doam_7.setRowCount(9)
        __qtablewidgetitem399 = QTableWidgetItem()
        __qtablewidgetitem399.setFont(font3);
        self.tableWidget_doam_7.setVerticalHeaderItem(0, __qtablewidgetitem399)
        __qtablewidgetitem400 = QTableWidgetItem()
        self.tableWidget_doam_7.setVerticalHeaderItem(1, __qtablewidgetitem400)
        __qtablewidgetitem401 = QTableWidgetItem()
        self.tableWidget_doam_7.setVerticalHeaderItem(2, __qtablewidgetitem401)
        __qtablewidgetitem402 = QTableWidgetItem()
        self.tableWidget_doam_7.setVerticalHeaderItem(3, __qtablewidgetitem402)
        __qtablewidgetitem403 = QTableWidgetItem()
        self.tableWidget_doam_7.setVerticalHeaderItem(4, __qtablewidgetitem403)
        __qtablewidgetitem404 = QTableWidgetItem()
        self.tableWidget_doam_7.setVerticalHeaderItem(5, __qtablewidgetitem404)
        __qtablewidgetitem405 = QTableWidgetItem()
        self.tableWidget_doam_7.setVerticalHeaderItem(6, __qtablewidgetitem405)
        __qtablewidgetitem406 = QTableWidgetItem()
        self.tableWidget_doam_7.setVerticalHeaderItem(7, __qtablewidgetitem406)
        __qtablewidgetitem407 = QTableWidgetItem()
        self.tableWidget_doam_7.setVerticalHeaderItem(8, __qtablewidgetitem407)
        self.tableWidget_doam_7.setObjectName(u"tableWidget_doam_7")
        sizePolicy.setHeightForWidth(self.tableWidget_doam_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_doam_7.setSizePolicy(sizePolicy)
        self.tableWidget_doam_7.setMinimumSize(QSize(400, 0))
        self.tableWidget_doam_7.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_doam_7.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_7.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_doam_7.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_doam_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_doam_7.verticalHeader().setVisible(False)
        self.tableWidget_doam_7.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_doam_7.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_doam_7.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_271.addWidget(self.tableWidget_doam_7)


        self.verticalLayout_270.addWidget(self.widget_401)

        self.widget_402 = QWidget(self.widget_400)
        self.widget_402.setObjectName(u"widget_402")
        sizePolicy3.setHeightForWidth(self.widget_402.sizePolicy().hasHeightForWidth())
        self.widget_402.setSizePolicy(sizePolicy3)
        self.horizontalLayout_186 = QHBoxLayout(self.widget_402)
        self.horizontalLayout_186.setSpacing(0)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_35 = QPushButton(self.widget_402)
        self.pushButton_exportTem_35.setObjectName(u"pushButton_exportTem_35")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_35.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_35.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_35.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_186.addWidget(self.pushButton_exportTem_35)


        self.verticalLayout_270.addWidget(self.widget_402)


        self.gridLayout_11.addWidget(self.widget_400, 1, 0, 1, 1)

        self.widget_403 = QWidget(self.widget_389)
        self.widget_403.setObjectName(u"widget_403")
        sizePolicy.setHeightForWidth(self.widget_403.sizePolicy().hasHeightForWidth())
        self.widget_403.setSizePolicy(sizePolicy)
        self.widget_403.setAutoFillBackground(False)
        self.widget_403.setStyleSheet(u"text-align: center;")
        self.verticalLayout_272 = QVBoxLayout(self.widget_403)
        self.verticalLayout_272.setSpacing(0)
        self.verticalLayout_272.setObjectName(u"verticalLayout_272")
        self.verticalLayout_272.setContentsMargins(0, 0, 0, 0)
        self.label_88 = QLabel(self.widget_403)
        self.label_88.setObjectName(u"label_88")
        sizePolicy3.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy3)
        self.label_88.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_88.setAlignment(Qt.AlignCenter)

        self.verticalLayout_272.addWidget(self.label_88)

        self.widget_404 = QWidget(self.widget_403)
        self.widget_404.setObjectName(u"widget_404")
        sizePolicy.setHeightForWidth(self.widget_404.sizePolicy().hasHeightForWidth())
        self.widget_404.setSizePolicy(sizePolicy)
        self.verticalLayout_273 = QVBoxLayout(self.widget_404)
        self.verticalLayout_273.setSpacing(0)
        self.verticalLayout_273.setObjectName(u"verticalLayout_273")
        self.verticalLayout_273.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_dc2_7 = QTableWidget(self.widget_404)
        if (self.tableWidget_dc2_7.columnCount() < 3):
            self.tableWidget_dc2_7.setColumnCount(3)
        __qtablewidgetitem408 = QTableWidgetItem()
        self.tableWidget_dc2_7.setHorizontalHeaderItem(0, __qtablewidgetitem408)
        __qtablewidgetitem409 = QTableWidgetItem()
        self.tableWidget_dc2_7.setHorizontalHeaderItem(1, __qtablewidgetitem409)
        __qtablewidgetitem410 = QTableWidgetItem()
        self.tableWidget_dc2_7.setHorizontalHeaderItem(2, __qtablewidgetitem410)
        if (self.tableWidget_dc2_7.rowCount() < 9):
            self.tableWidget_dc2_7.setRowCount(9)
        __qtablewidgetitem411 = QTableWidgetItem()
        __qtablewidgetitem411.setFont(font3);
        self.tableWidget_dc2_7.setVerticalHeaderItem(0, __qtablewidgetitem411)
        __qtablewidgetitem412 = QTableWidgetItem()
        self.tableWidget_dc2_7.setVerticalHeaderItem(1, __qtablewidgetitem412)
        __qtablewidgetitem413 = QTableWidgetItem()
        self.tableWidget_dc2_7.setVerticalHeaderItem(2, __qtablewidgetitem413)
        __qtablewidgetitem414 = QTableWidgetItem()
        self.tableWidget_dc2_7.setVerticalHeaderItem(3, __qtablewidgetitem414)
        __qtablewidgetitem415 = QTableWidgetItem()
        self.tableWidget_dc2_7.setVerticalHeaderItem(4, __qtablewidgetitem415)
        __qtablewidgetitem416 = QTableWidgetItem()
        self.tableWidget_dc2_7.setVerticalHeaderItem(5, __qtablewidgetitem416)
        __qtablewidgetitem417 = QTableWidgetItem()
        self.tableWidget_dc2_7.setVerticalHeaderItem(6, __qtablewidgetitem417)
        __qtablewidgetitem418 = QTableWidgetItem()
        self.tableWidget_dc2_7.setVerticalHeaderItem(7, __qtablewidgetitem418)
        __qtablewidgetitem419 = QTableWidgetItem()
        self.tableWidget_dc2_7.setVerticalHeaderItem(8, __qtablewidgetitem419)
        self.tableWidget_dc2_7.setObjectName(u"tableWidget_dc2_7")
        sizePolicy.setHeightForWidth(self.tableWidget_dc2_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_dc2_7.setSizePolicy(sizePolicy)
        self.tableWidget_dc2_7.setMinimumSize(QSize(400, 0))
        self.tableWidget_dc2_7.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dc2_7.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_7.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_dc2_7.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_dc2_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dc2_7.verticalHeader().setVisible(False)
        self.tableWidget_dc2_7.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_dc2_7.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_dc2_7.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_273.addWidget(self.tableWidget_dc2_7)


        self.verticalLayout_272.addWidget(self.widget_404)

        self.widget_405 = QWidget(self.widget_403)
        self.widget_405.setObjectName(u"widget_405")
        sizePolicy3.setHeightForWidth(self.widget_405.sizePolicy().hasHeightForWidth())
        self.widget_405.setSizePolicy(sizePolicy3)
        self.horizontalLayout_187 = QHBoxLayout(self.widget_405)
        self.horizontalLayout_187.setSpacing(0)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_36 = QPushButton(self.widget_405)
        self.pushButton_exportTem_36.setObjectName(u"pushButton_exportTem_36")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_36.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_36.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_36.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_187.addWidget(self.pushButton_exportTem_36)


        self.verticalLayout_272.addWidget(self.widget_405)


        self.gridLayout_11.addWidget(self.widget_403, 1, 1, 1, 1)

        self.widget_406 = QWidget(self.widget_389)
        self.widget_406.setObjectName(u"widget_406")
        sizePolicy.setHeightForWidth(self.widget_406.sizePolicy().hasHeightForWidth())
        self.widget_406.setSizePolicy(sizePolicy)
        self.widget_406.setAutoFillBackground(False)
        self.widget_406.setStyleSheet(u"text-align: center;")
        self.verticalLayout_274 = QVBoxLayout(self.widget_406)
        self.verticalLayout_274.setSpacing(0)
        self.verticalLayout_274.setObjectName(u"verticalLayout_274")
        self.verticalLayout_274.setContentsMargins(0, 0, 0, 0)
        self.label_89 = QLabel(self.widget_406)
        self.label_89.setObjectName(u"label_89")
        sizePolicy3.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy3)
        self.label_89.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Times New Roman\";")
        self.label_89.setAlignment(Qt.AlignCenter)

        self.verticalLayout_274.addWidget(self.label_89)

        self.widget_407 = QWidget(self.widget_406)
        self.widget_407.setObjectName(u"widget_407")
        sizePolicy.setHeightForWidth(self.widget_407.sizePolicy().hasHeightForWidth())
        self.widget_407.setSizePolicy(sizePolicy)
        self.verticalLayout_275 = QVBoxLayout(self.widget_407)
        self.verticalLayout_275.setSpacing(0)
        self.verticalLayout_275.setObjectName(u"verticalLayout_275")
        self.verticalLayout_275.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_ac2_6 = QTableWidget(self.widget_407)
        if (self.tableWidget_ac2_6.columnCount() < 3):
            self.tableWidget_ac2_6.setColumnCount(3)
        __qtablewidgetitem420 = QTableWidgetItem()
        self.tableWidget_ac2_6.setHorizontalHeaderItem(0, __qtablewidgetitem420)
        __qtablewidgetitem421 = QTableWidgetItem()
        self.tableWidget_ac2_6.setHorizontalHeaderItem(1, __qtablewidgetitem421)
        __qtablewidgetitem422 = QTableWidgetItem()
        self.tableWidget_ac2_6.setHorizontalHeaderItem(2, __qtablewidgetitem422)
        if (self.tableWidget_ac2_6.rowCount() < 9):
            self.tableWidget_ac2_6.setRowCount(9)
        __qtablewidgetitem423 = QTableWidgetItem()
        __qtablewidgetitem423.setFont(font3);
        self.tableWidget_ac2_6.setVerticalHeaderItem(0, __qtablewidgetitem423)
        __qtablewidgetitem424 = QTableWidgetItem()
        self.tableWidget_ac2_6.setVerticalHeaderItem(1, __qtablewidgetitem424)
        __qtablewidgetitem425 = QTableWidgetItem()
        self.tableWidget_ac2_6.setVerticalHeaderItem(2, __qtablewidgetitem425)
        __qtablewidgetitem426 = QTableWidgetItem()
        self.tableWidget_ac2_6.setVerticalHeaderItem(3, __qtablewidgetitem426)
        __qtablewidgetitem427 = QTableWidgetItem()
        self.tableWidget_ac2_6.setVerticalHeaderItem(4, __qtablewidgetitem427)
        __qtablewidgetitem428 = QTableWidgetItem()
        self.tableWidget_ac2_6.setVerticalHeaderItem(5, __qtablewidgetitem428)
        __qtablewidgetitem429 = QTableWidgetItem()
        self.tableWidget_ac2_6.setVerticalHeaderItem(6, __qtablewidgetitem429)
        __qtablewidgetitem430 = QTableWidgetItem()
        self.tableWidget_ac2_6.setVerticalHeaderItem(7, __qtablewidgetitem430)
        __qtablewidgetitem431 = QTableWidgetItem()
        self.tableWidget_ac2_6.setVerticalHeaderItem(8, __qtablewidgetitem431)
        self.tableWidget_ac2_6.setObjectName(u"tableWidget_ac2_6")
        sizePolicy.setHeightForWidth(self.tableWidget_ac2_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_ac2_6.setSizePolicy(sizePolicy)
        self.tableWidget_ac2_6.setMinimumSize(QSize(400, 0))
        self.tableWidget_ac2_6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ac2_6.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_6.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_ac2_6.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_ac2_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ac2_6.verticalHeader().setVisible(False)
        self.tableWidget_ac2_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ac2_6.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_ac2_6.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_275.addWidget(self.tableWidget_ac2_6)


        self.verticalLayout_274.addWidget(self.widget_407)

        self.widget_408 = QWidget(self.widget_406)
        self.widget_408.setObjectName(u"widget_408")
        sizePolicy3.setHeightForWidth(self.widget_408.sizePolicy().hasHeightForWidth())
        self.widget_408.setSizePolicy(sizePolicy3)
        self.horizontalLayout_188 = QHBoxLayout(self.widget_408)
        self.horizontalLayout_188.setSpacing(0)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportTem_37 = QPushButton(self.widget_408)
        self.pushButton_exportTem_37.setObjectName(u"pushButton_exportTem_37")
        sizePolicy5.setHeightForWidth(self.pushButton_exportTem_37.sizePolicy().hasHeightForWidth())
        self.pushButton_exportTem_37.setSizePolicy(sizePolicy5)
        self.pushButton_exportTem_37.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_188.addWidget(self.pushButton_exportTem_37)


        self.verticalLayout_274.addWidget(self.widget_408)


        self.gridLayout_11.addWidget(self.widget_406, 1, 2, 1, 1)


        self.verticalLayout_276.addWidget(self.widget_389)

        self.stackedWidget.addWidget(self.suco_6)
        self.doam_6 = QWidget()
        self.doam_6.setObjectName(u"doam_6")
        self.verticalLayout_205 = QVBoxLayout(self.doam_6)
        self.verticalLayout_205.setSpacing(0)
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.verticalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.widget_Doam_3 = QWidget(self.doam_6)
        self.widget_Doam_3.setObjectName(u"widget_Doam_3")
        self.widget_Doam_3.setStyleSheet(u"")
        self.verticalLayout_203 = QVBoxLayout(self.widget_Doam_3)
        self.verticalLayout_203.setSpacing(0)
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.verticalLayout_203.setContentsMargins(0, 0, 0, 0)
        self.widget_label_doam_3 = QWidget(self.widget_Doam_3)
        self.widget_label_doam_3.setObjectName(u"widget_label_doam_3")
        sizePolicy.setHeightForWidth(self.widget_label_doam_3.sizePolicy().hasHeightForWidth())
        self.widget_label_doam_3.setSizePolicy(sizePolicy)
        self.widget_label_doam_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_doam_3.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_204 = QVBoxLayout(self.widget_label_doam_3)
        self.verticalLayout_204.setSpacing(0)
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.verticalLayout_204.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_204.setContentsMargins(0, 0, 0, 0)
        self.label_doam_5 = QLabel(self.widget_label_doam_3)
        self.label_doam_5.setObjectName(u"label_doam_5")
        sizePolicy3.setHeightForWidth(self.label_doam_5.sizePolicy().hasHeightForWidth())
        self.label_doam_5.setSizePolicy(sizePolicy3)
        self.label_doam_5.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_doam_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_204.addWidget(self.label_doam_5)

        self.label_thoigian_doam_3 = QLabel(self.widget_label_doam_3)
        self.label_thoigian_doam_3.setObjectName(u"label_thoigian_doam_3")
        sizePolicy3.setHeightForWidth(self.label_thoigian_doam_3.sizePolicy().hasHeightForWidth())
        self.label_thoigian_doam_3.setSizePolicy(sizePolicy3)
        self.label_thoigian_doam_3.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_doam_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_204.addWidget(self.label_thoigian_doam_3)

        self.screen_doam_3 = QVBoxLayout()
        self.screen_doam_3.setSpacing(0)
        self.screen_doam_3.setObjectName(u"screen_doam_3")
        self.screen_doam_3.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_204.addLayout(self.screen_doam_3)


        self.verticalLayout_203.addWidget(self.widget_label_doam_3)


        self.verticalLayout_205.addWidget(self.widget_Doam_3)

        self.stackedWidget.addWidget(self.doam_6)
        self.doam_5 = QWidget()
        self.doam_5.setObjectName(u"doam_5")
        self.verticalLayout_208 = QVBoxLayout(self.doam_5)
        self.verticalLayout_208.setSpacing(0)
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.verticalLayout_208.setContentsMargins(0, 0, 0, 0)
        self.widget_Doam_4 = QWidget(self.doam_5)
        self.widget_Doam_4.setObjectName(u"widget_Doam_4")
        self.widget_Doam_4.setStyleSheet(u"")
        self.verticalLayout_206 = QVBoxLayout(self.widget_Doam_4)
        self.verticalLayout_206.setSpacing(0)
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.verticalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.widget_label_doam_4 = QWidget(self.widget_Doam_4)
        self.widget_label_doam_4.setObjectName(u"widget_label_doam_4")
        sizePolicy.setHeightForWidth(self.widget_label_doam_4.sizePolicy().hasHeightForWidth())
        self.widget_label_doam_4.setSizePolicy(sizePolicy)
        self.widget_label_doam_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_doam_4.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_207 = QVBoxLayout(self.widget_label_doam_4)
        self.verticalLayout_207.setSpacing(0)
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.verticalLayout_207.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_207.setContentsMargins(0, 0, 0, 0)
        self.label_doam_6 = QLabel(self.widget_label_doam_4)
        self.label_doam_6.setObjectName(u"label_doam_6")
        sizePolicy3.setHeightForWidth(self.label_doam_6.sizePolicy().hasHeightForWidth())
        self.label_doam_6.setSizePolicy(sizePolicy3)
        self.label_doam_6.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_doam_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_207.addWidget(self.label_doam_6)

        self.label_thoigian_doam_4 = QLabel(self.widget_label_doam_4)
        self.label_thoigian_doam_4.setObjectName(u"label_thoigian_doam_4")
        sizePolicy3.setHeightForWidth(self.label_thoigian_doam_4.sizePolicy().hasHeightForWidth())
        self.label_thoigian_doam_4.setSizePolicy(sizePolicy3)
        self.label_thoigian_doam_4.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_doam_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_207.addWidget(self.label_thoigian_doam_4)

        self.screen_doam_4 = QVBoxLayout()
        self.screen_doam_4.setSpacing(0)
        self.screen_doam_4.setObjectName(u"screen_doam_4")
        self.screen_doam_4.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_207.addLayout(self.screen_doam_4)


        self.verticalLayout_206.addWidget(self.widget_label_doam_4)


        self.verticalLayout_208.addWidget(self.widget_Doam_4)

        self.stackedWidget.addWidget(self.doam_5)
        self.nhietdo_4 = QWidget()
        self.nhietdo_4.setObjectName(u"nhietdo_4")
        self.verticalLayout_200 = QVBoxLayout(self.nhietdo_4)
        self.verticalLayout_200.setSpacing(0)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.Nhietdo_widget_4 = QWidget(self.nhietdo_4)
        self.Nhietdo_widget_4.setObjectName(u"Nhietdo_widget_4")
        self.Nhietdo_widget_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_199 = QVBoxLayout(self.Nhietdo_widget_4)
        self.verticalLayout_199.setSpacing(0)
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.verticalLayout_199.setContentsMargins(0, 0, 0, 0)
        self.title_nhietdo_4 = QLabel(self.Nhietdo_widget_4)
        self.title_nhietdo_4.setObjectName(u"title_nhietdo_4")
        sizePolicy3.setHeightForWidth(self.title_nhietdo_4.sizePolicy().hasHeightForWidth())
        self.title_nhietdo_4.setSizePolicy(sizePolicy3)
        self.title_nhietdo_4.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.title_nhietdo_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_199.addWidget(self.title_nhietdo_4)

        self.thoigian_nhietdo_4 = QLabel(self.Nhietdo_widget_4)
        self.thoigian_nhietdo_4.setObjectName(u"thoigian_nhietdo_4")
        sizePolicy3.setHeightForWidth(self.thoigian_nhietdo_4.sizePolicy().hasHeightForWidth())
        self.thoigian_nhietdo_4.setSizePolicy(sizePolicy3)
        self.thoigian_nhietdo_4.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.thoigian_nhietdo_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_199.addWidget(self.thoigian_nhietdo_4)

        self.widget_325 = QWidget(self.Nhietdo_widget_4)
        self.widget_325.setObjectName(u"widget_325")
        sizePolicy.setHeightForWidth(self.widget_325.sizePolicy().hasHeightForWidth())
        self.widget_325.setSizePolicy(sizePolicy)
        self.widget_325.setMinimumSize(QSize(0, 0))
        self.gridLayout_7 = QGridLayout(self.widget_325)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_23, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 2, 1, 1, 1)

        self.screen_nhietdo_4 = QVBoxLayout()
        self.screen_nhietdo_4.setSpacing(0)
        self.screen_nhietdo_4.setObjectName(u"screen_nhietdo_4")
        self.screen_nhietdo_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.screen_nhietdo_4.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_7.addLayout(self.screen_nhietdo_4, 1, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_24, 1, 0, 1, 1)


        self.verticalLayout_199.addWidget(self.widget_325)


        self.verticalLayout_200.addWidget(self.Nhietdo_widget_4)

        self.stackedWidget.addWidget(self.nhietdo_4)
        self.huondansd = QWidget()
        self.huondansd.setObjectName(u"huondansd")
        self.verticalLayout_87 = QVBoxLayout(self.huondansd)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.widget_53 = QWidget(self.huondansd)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_132 = QVBoxLayout(self.widget_53)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.label_9 = QLabel(self.widget_53)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"\n"
"font: 700 22pt \"Times New Roman\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_132.addWidget(self.label_9)

        self.widget_54 = QWidget(self.widget_53)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setStyleSheet(u"border-color: 1px solid rgb(0, 0, 0);")
        self.verticalLayout_152 = QVBoxLayout(self.widget_54)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.verticalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.widget_61 = QWidget(self.widget_54)
        self.widget_61.setObjectName(u"widget_61")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_61.sizePolicy().hasHeightForWidth())
        self.widget_61.setSizePolicy(sizePolicy6)
        self.widget_61.setStyleSheet(u"border: 1px solid #000;")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_64 = QWidget(self.widget_61)
        self.widget_64.setObjectName(u"widget_64")
        sizePolicy5.setHeightForWidth(self.widget_64.sizePolicy().hasHeightForWidth())
        self.widget_64.setSizePolicy(sizePolicy5)
        self.widget_64.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_159 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_159.setSpacing(0)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.widget_64)
        self.label_63.setObjectName(u"label_63")
        sizePolicy5.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy5)
        self.label_63.setMinimumSize(QSize(300, 0))
        self.label_63.setMaximumSize(QSize(0, 16777215))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_63.setFont(font4)
        self.label_63.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_63.setScaledContents(True)
        self.label_63.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_63.setWordWrap(True)

        self.horizontalLayout_159.addWidget(self.label_63)

        self.label_62 = QLabel(self.widget_64)
        self.label_62.setObjectName(u"label_62")
        sizePolicy5.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy5)
        self.label_62.setMinimumSize(QSize(300, 250))
        self.label_62.setMaximumSize(QSize(1000, 16777215))
        self.label_62.setPixmap(QPixmap(u":/images/images/images/Screenshot 2023-10-31 224519.png"))
        self.label_62.setScaledContents(True)

        self.horizontalLayout_159.addWidget(self.label_62)


        self.horizontalLayout_24.addWidget(self.widget_64)

        self.widget_319 = QWidget(self.widget_61)
        self.widget_319.setObjectName(u"widget_319")
        sizePolicy5.setHeightForWidth(self.widget_319.sizePolicy().hasHeightForWidth())
        self.widget_319.setSizePolicy(sizePolicy5)
        self.horizontalLayout_158 = QHBoxLayout(self.widget_319)
        self.horizontalLayout_158.setSpacing(0)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.widget_319)
        self.label_64.setObjectName(u"label_64")
        sizePolicy4.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy4)
        self.label_64.setMinimumSize(QSize(300, 0))
        self.label_64.setPixmap(QPixmap(u":/images/images/images/Screenshot 2023-10-31 234909.png"))
        self.label_64.setScaledContents(True)

        self.horizontalLayout_158.addWidget(self.label_64)

        self.label_65 = QLabel(self.widget_319)
        self.label_65.setObjectName(u"label_65")
        sizePolicy5.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy5)
        self.label_65.setFont(font4)
        self.label_65.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.label_65.setScaledContents(True)
        self.label_65.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_65.setWordWrap(True)

        self.horizontalLayout_158.addWidget(self.label_65)


        self.horizontalLayout_24.addWidget(self.widget_319)


        self.verticalLayout_152.addWidget(self.widget_61)

        self.widget_62 = QWidget(self.widget_54)
        self.widget_62.setObjectName(u"widget_62")
        sizePolicy6.setHeightForWidth(self.widget_62.sizePolicy().hasHeightForWidth())
        self.widget_62.setSizePolicy(sizePolicy6)
        self.widget_62.setStyleSheet(u"border: 1px solid #000;")
        self.horizontalLayout_138 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.widget_321 = QWidget(self.widget_62)
        self.widget_321.setObjectName(u"widget_321")
        sizePolicy5.setHeightForWidth(self.widget_321.sizePolicy().hasHeightForWidth())
        self.widget_321.setSizePolicy(sizePolicy5)
        self.horizontalLayout_161 = QHBoxLayout(self.widget_321)
        self.horizontalLayout_161.setSpacing(0)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.widget_321)
        self.label_68.setObjectName(u"label_68")
        sizePolicy4.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy4)
        self.label_68.setMinimumSize(QSize(300, 250))
        self.label_68.setPixmap(QPixmap(u":/images/images/images/Screenshot 2023-10-31 234909.png"))
        self.label_68.setScaledContents(True)

        self.horizontalLayout_161.addWidget(self.label_68)

        self.label_69 = QLabel(self.widget_321)
        self.label_69.setObjectName(u"label_69")
        sizePolicy5.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy5)
        self.label_69.setFont(font4)
        self.label_69.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.label_69.setScaledContents(True)
        self.label_69.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_69.setWordWrap(True)

        self.horizontalLayout_161.addWidget(self.label_69)


        self.horizontalLayout_138.addWidget(self.widget_321)

        self.widget_320 = QWidget(self.widget_62)
        self.widget_320.setObjectName(u"widget_320")
        sizePolicy5.setHeightForWidth(self.widget_320.sizePolicy().hasHeightForWidth())
        self.widget_320.setSizePolicy(sizePolicy5)
        self.horizontalLayout_160 = QHBoxLayout(self.widget_320)
        self.horizontalLayout_160.setSpacing(0)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.widget_320)
        self.label_66.setObjectName(u"label_66")
        sizePolicy4.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy4)
        self.label_66.setMinimumSize(QSize(300, 0))
        self.label_66.setPixmap(QPixmap(u":/images/images/images/Screenshot 2023-11-01 001639.png"))
        self.label_66.setScaledContents(True)

        self.horizontalLayout_160.addWidget(self.label_66)

        self.label_67 = QLabel(self.widget_320)
        self.label_67.setObjectName(u"label_67")
        sizePolicy5.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy5)
        self.label_67.setFont(font4)
        self.label_67.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.label_67.setScaledContents(True)
        self.label_67.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_67.setWordWrap(True)

        self.horizontalLayout_160.addWidget(self.label_67)


        self.horizontalLayout_138.addWidget(self.widget_320)


        self.verticalLayout_152.addWidget(self.widget_62)

        self.widget_63 = QWidget(self.widget_54)
        self.widget_63.setObjectName(u"widget_63")
        sizePolicy6.setHeightForWidth(self.widget_63.sizePolicy().hasHeightForWidth())
        self.widget_63.setSizePolicy(sizePolicy6)
        self.widget_63.setStyleSheet(u"border: 1px solid #000;")
        self.horizontalLayout_139 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.widget_323 = QWidget(self.widget_63)
        self.widget_323.setObjectName(u"widget_323")
        sizePolicy5.setHeightForWidth(self.widget_323.sizePolicy().hasHeightForWidth())
        self.widget_323.setSizePolicy(sizePolicy5)
        self.horizontalLayout_163 = QHBoxLayout(self.widget_323)
        self.horizontalLayout_163.setSpacing(0)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.widget_323)
        self.label_72.setObjectName(u"label_72")
        sizePolicy4.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy4)
        self.label_72.setMinimumSize(QSize(300, 0))
        self.label_72.setPixmap(QPixmap(u":/images/images/images/Screenshot 2023-11-01 002148.png"))
        self.label_72.setScaledContents(True)
        self.label_72.setWordWrap(True)

        self.horizontalLayout_163.addWidget(self.label_72)

        self.label_73 = QLabel(self.widget_323)
        self.label_73.setObjectName(u"label_73")
        sizePolicy5.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy5)
        self.label_73.setFont(font4)
        self.label_73.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.label_73.setScaledContents(False)
        self.label_73.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_73.setWordWrap(True)

        self.horizontalLayout_163.addWidget(self.label_73)


        self.horizontalLayout_139.addWidget(self.widget_323)

        self.widget_322 = QWidget(self.widget_63)
        self.widget_322.setObjectName(u"widget_322")
        sizePolicy5.setHeightForWidth(self.widget_322.sizePolicy().hasHeightForWidth())
        self.widget_322.setSizePolicy(sizePolicy5)
        self.horizontalLayout_162 = QHBoxLayout(self.widget_322)
        self.horizontalLayout_162.setSpacing(0)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(0, 0, -1, 0)
        self.label_70 = QLabel(self.widget_322)
        self.label_70.setObjectName(u"label_70")
        sizePolicy4.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy4)
        self.label_70.setMinimumSize(QSize(300, 0))
        self.label_70.setPixmap(QPixmap(u":/images/images/images/Screenshot 2023-11-01 001728.png"))
        self.label_70.setScaledContents(True)

        self.horizontalLayout_162.addWidget(self.label_70)

        self.label_71 = QLabel(self.widget_322)
        self.label_71.setObjectName(u"label_71")
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMinimumSize(QSize(371, 0))
        self.label_71.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_71.setPixmap(QPixmap(u":/images/images/images/Screenshot 2023-11-01 002415.png"))
        self.label_71.setScaledContents(True)
        self.label_71.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_71.setWordWrap(True)

        self.horizontalLayout_162.addWidget(self.label_71)


        self.horizontalLayout_139.addWidget(self.widget_322)


        self.verticalLayout_152.addWidget(self.widget_63)


        self.verticalLayout_132.addWidget(self.widget_54)


        self.verticalLayout_87.addWidget(self.widget_53)

        self.stackedWidget.addWidget(self.huondansd)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_23 = QWidget(self.page)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_21 = QVBoxLayout(self.widget_23)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy2.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy2)
        self.verticalLayout_24 = QVBoxLayout(self.widget_24)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_24)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"\n"
"font: 700 22pt \"Times New Roman\";")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_15)

        self.label_17 = QLabel(self.widget_24)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_17)


        self.verticalLayout_21.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_23)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.verticalLayout_36 = QVBoxLayout(self.widget_25)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.lisTram_3 = QWidget(self.widget_25)
        self.lisTram_3.setObjectName(u"lisTram_3")
        sizePolicy.setHeightForWidth(self.lisTram_3.sizePolicy().hasHeightForWidth())
        self.lisTram_3.setSizePolicy(sizePolicy)
        self.lisTram_3.setStyleSheet(u"border-right-color: rgb(0, 0, 0);")
        self.horizontalLayout_7 = QHBoxLayout(self.lisTram_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 30, 20)
        self.widget_26 = QWidget(self.lisTram_3)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy)
        self.widget_26.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_121 = QVBoxLayout(self.widget_26)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.widget_225 = QWidget(self.widget_26)
        self.widget_225.setObjectName(u"widget_225")
        sizePolicy3.setHeightForWidth(self.widget_225.sizePolicy().hasHeightForWidth())
        self.widget_225.setSizePolicy(sizePolicy3)
        self.widget_225.setLayoutDirection(Qt.LeftToRight)
        self.widget_225.setStyleSheet(u"font: 700 16pt \"Times New Roman\";\n"
"padding:0\n"
"")
        self.horizontalLayout_131 = QHBoxLayout(self.widget_225)
        self.horizontalLayout_131.setSpacing(0)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_225)
        self.label_23.setObjectName(u"label_23")
        sizePolicy4.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy4)
        self.label_23.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_131.addWidget(self.label_23)

        self.pushButton_anhsang_15 = QPushButton(self.widget_225)
        self.pushButton_anhsang_15.setObjectName(u"pushButton_anhsang_15")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_15.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_15.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_15.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_15.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_15.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_15.setIconSize(QSize(16, 16))

        self.horizontalLayout_131.addWidget(self.pushButton_anhsang_15)


        self.verticalLayout_121.addWidget(self.widget_225)

        self.widget_226 = QWidget(self.widget_26)
        self.widget_226.setObjectName(u"widget_226")
        sizePolicy3.setHeightForWidth(self.widget_226.sizePolicy().hasHeightForWidth())
        self.widget_226.setSizePolicy(sizePolicy3)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_226)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_227 = QWidget(self.widget_226)
        self.widget_227.setObjectName(u"widget_227")
        sizePolicy3.setHeightForWidth(self.widget_227.sizePolicy().hasHeightForWidth())
        self.widget_227.setSizePolicy(sizePolicy3)
        self.verticalLayout_122 = QVBoxLayout(self.widget_227)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 30, 0)
        self.widget_228 = QWidget(self.widget_227)
        self.widget_228.setObjectName(u"widget_228")
        sizePolicy.setHeightForWidth(self.widget_228.sizePolicy().hasHeightForWidth())
        self.widget_228.setSizePolicy(sizePolicy)
        self.verticalLayout_123 = QVBoxLayout(self.widget_228)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 20)
        self.label_24 = QLabel(self.widget_228)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"")
        self.label_24.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_24.setScaledContents(True)

        self.verticalLayout_123.addWidget(self.label_24)


        self.verticalLayout_122.addWidget(self.widget_228)

        self.widget_229 = QWidget(self.widget_227)
        self.widget_229.setObjectName(u"widget_229")
        sizePolicy3.setHeightForWidth(self.widget_229.sizePolicy().hasHeightForWidth())
        self.widget_229.setSizePolicy(sizePolicy3)
        self.horizontalLayout_132 = QHBoxLayout(self.widget_229)
        self.horizontalLayout_132.setSpacing(0)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.widget_230 = QWidget(self.widget_229)
        self.widget_230.setObjectName(u"widget_230")
        self.verticalLayout_124 = QVBoxLayout(self.widget_230)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.widget_232 = QWidget(self.widget_230)
        self.widget_232.setObjectName(u"widget_232")
        self.verticalLayout_125 = QVBoxLayout(self.widget_232)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_124.addWidget(self.widget_232)


        self.horizontalLayout_132.addWidget(self.widget_230)

        self.widget_253 = QWidget(self.widget_229)
        self.widget_253.setObjectName(u"widget_253")
        self.verticalLayout_126 = QVBoxLayout(self.widget_253)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_132.addWidget(self.widget_253)


        self.verticalLayout_122.addWidget(self.widget_229)


        self.horizontalLayout_9.addWidget(self.widget_227)


        self.verticalLayout_121.addWidget(self.widget_226)


        self.horizontalLayout_7.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.lisTram_3)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy)
        self.widget_27.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_134 = QVBoxLayout(self.widget_27)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.widget_38 = QWidget(self.widget_27)
        self.widget_38.setObjectName(u"widget_38")
        sizePolicy3.setHeightForWidth(self.widget_38.sizePolicy().hasHeightForWidth())
        self.widget_38.setSizePolicy(sizePolicy3)
        self.verticalLayout_135 = QVBoxLayout(self.widget_38)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.widget_310 = QWidget(self.widget_38)
        self.widget_310.setObjectName(u"widget_310")
        sizePolicy3.setHeightForWidth(self.widget_310.sizePolicy().hasHeightForWidth())
        self.widget_310.setSizePolicy(sizePolicy3)
        self.widget_310.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_193 = QHBoxLayout(self.widget_310)
        self.horizontalLayout_193.setSpacing(0)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.widget_310)
        self.label_27.setObjectName(u"label_27")
        sizePolicy4.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy4)
        self.label_27.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_193.addWidget(self.label_27)

        self.pushButton_anhsang_16 = QPushButton(self.widget_310)
        self.pushButton_anhsang_16.setObjectName(u"pushButton_anhsang_16")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_16.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_16.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_16.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_16.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_16.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_16.setIconSize(QSize(16, 16))

        self.horizontalLayout_193.addWidget(self.pushButton_anhsang_16)


        self.verticalLayout_135.addWidget(self.widget_310)

        self.widget_409 = QWidget(self.widget_38)
        self.widget_409.setObjectName(u"widget_409")
        sizePolicy3.setHeightForWidth(self.widget_409.sizePolicy().hasHeightForWidth())
        self.widget_409.setSizePolicy(sizePolicy3)
        self.horizontalLayout_194 = QHBoxLayout(self.widget_409)
        self.horizontalLayout_194.setSpacing(0)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.widget_410 = QWidget(self.widget_409)
        self.widget_410.setObjectName(u"widget_410")
        sizePolicy3.setHeightForWidth(self.widget_410.sizePolicy().hasHeightForWidth())
        self.widget_410.setSizePolicy(sizePolicy3)
        self.widget_410.setMinimumSize(QSize(0, 0))
        self.verticalLayout_136 = QVBoxLayout(self.widget_410)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 30, 0)
        self.widget_411 = QWidget(self.widget_410)
        self.widget_411.setObjectName(u"widget_411")
        sizePolicy.setHeightForWidth(self.widget_411.sizePolicy().hasHeightForWidth())
        self.widget_411.setSizePolicy(sizePolicy)
        self.verticalLayout_137 = QVBoxLayout(self.widget_411)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 20)
        self.label_40 = QLabel(self.widget_411)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 0))
        self.label_40.setStyleSheet(u"")
        self.label_40.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_40.setScaledContents(True)

        self.verticalLayout_137.addWidget(self.label_40)


        self.verticalLayout_136.addWidget(self.widget_411)

        self.widget_412 = QWidget(self.widget_410)
        self.widget_412.setObjectName(u"widget_412")
        sizePolicy3.setHeightForWidth(self.widget_412.sizePolicy().hasHeightForWidth())
        self.widget_412.setSizePolicy(sizePolicy3)
        self.horizontalLayout_195 = QHBoxLayout(self.widget_412)
        self.horizontalLayout_195.setSpacing(0)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.widget_413 = QWidget(self.widget_412)
        self.widget_413.setObjectName(u"widget_413")
        self.verticalLayout_138 = QVBoxLayout(self.widget_413)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.widget_415 = QWidget(self.widget_413)
        self.widget_415.setObjectName(u"widget_415")
        self.verticalLayout_139 = QVBoxLayout(self.widget_415)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_138.addWidget(self.widget_415)


        self.horizontalLayout_195.addWidget(self.widget_413)

        self.widget_416 = QWidget(self.widget_412)
        self.widget_416.setObjectName(u"widget_416")
        self.verticalLayout_140 = QVBoxLayout(self.widget_416)
        self.verticalLayout_140.setSpacing(0)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_195.addWidget(self.widget_416)


        self.verticalLayout_136.addWidget(self.widget_412)


        self.horizontalLayout_194.addWidget(self.widget_410)


        self.verticalLayout_135.addWidget(self.widget_409)


        self.verticalLayout_134.addWidget(self.widget_38)


        self.horizontalLayout_7.addWidget(self.widget_27)

        self.widget_439 = QWidget(self.lisTram_3)
        self.widget_439.setObjectName(u"widget_439")
        self.widget_439.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_148 = QVBoxLayout(self.widget_439)
        self.verticalLayout_148.setSpacing(0)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.verticalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.widget_39 = QWidget(self.widget_439)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy3.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy3)
        self.verticalLayout_149 = QVBoxLayout(self.widget_39)
        self.verticalLayout_149.setSpacing(0)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.widget_440 = QWidget(self.widget_39)
        self.widget_440.setObjectName(u"widget_440")
        sizePolicy3.setHeightForWidth(self.widget_440.sizePolicy().hasHeightForWidth())
        self.widget_440.setSizePolicy(sizePolicy3)
        self.widget_440.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_212 = QHBoxLayout(self.widget_440)
        self.horizontalLayout_212.setSpacing(0)
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.horizontalLayout_212.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.widget_440)
        self.label_91.setObjectName(u"label_91")
        sizePolicy4.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy4)
        self.label_91.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_212.addWidget(self.label_91)

        self.pushButton_anhsang_17 = QPushButton(self.widget_440)
        self.pushButton_anhsang_17.setObjectName(u"pushButton_anhsang_17")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_17.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_17.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_17.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_17.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_17.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_17.setIconSize(QSize(16, 16))

        self.horizontalLayout_212.addWidget(self.pushButton_anhsang_17)


        self.verticalLayout_149.addWidget(self.widget_440)

        self.widget_441 = QWidget(self.widget_39)
        self.widget_441.setObjectName(u"widget_441")
        sizePolicy3.setHeightForWidth(self.widget_441.sizePolicy().hasHeightForWidth())
        self.widget_441.setSizePolicy(sizePolicy3)
        self.horizontalLayout_213 = QHBoxLayout(self.widget_441)
        self.horizontalLayout_213.setSpacing(0)
        self.horizontalLayout_213.setObjectName(u"horizontalLayout_213")
        self.horizontalLayout_213.setContentsMargins(0, 0, 0, 0)
        self.widget_442 = QWidget(self.widget_441)
        self.widget_442.setObjectName(u"widget_442")
        sizePolicy3.setHeightForWidth(self.widget_442.sizePolicy().hasHeightForWidth())
        self.widget_442.setSizePolicy(sizePolicy3)
        self.verticalLayout_186 = QVBoxLayout(self.widget_442)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(0, 0, 30, 0)
        self.widget_443 = QWidget(self.widget_442)
        self.widget_443.setObjectName(u"widget_443")
        sizePolicy.setHeightForWidth(self.widget_443.sizePolicy().hasHeightForWidth())
        self.widget_443.setSizePolicy(sizePolicy)
        self.verticalLayout_188 = QVBoxLayout(self.widget_443)
        self.verticalLayout_188.setSpacing(0)
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.verticalLayout_188.setContentsMargins(0, 0, 0, 20)
        self.label_92 = QLabel(self.widget_443)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setStyleSheet(u"")
        self.label_92.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_92.setScaledContents(True)

        self.verticalLayout_188.addWidget(self.label_92)


        self.verticalLayout_186.addWidget(self.widget_443)

        self.widget_444 = QWidget(self.widget_442)
        self.widget_444.setObjectName(u"widget_444")
        sizePolicy3.setHeightForWidth(self.widget_444.sizePolicy().hasHeightForWidth())
        self.widget_444.setSizePolicy(sizePolicy3)
        self.horizontalLayout_214 = QHBoxLayout(self.widget_444)
        self.horizontalLayout_214.setSpacing(0)
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.horizontalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.widget_445 = QWidget(self.widget_444)
        self.widget_445.setObjectName(u"widget_445")
        self.verticalLayout_189 = QVBoxLayout(self.widget_445)
        self.verticalLayout_189.setSpacing(0)
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.verticalLayout_189.setContentsMargins(0, 0, 0, 0)
        self.widget_446 = QWidget(self.widget_445)
        self.widget_446.setObjectName(u"widget_446")
        self.horizontalLayout_215 = QHBoxLayout(self.widget_446)
        self.horizontalLayout_215.setSpacing(0)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalLayout_215.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_9 = QPushButton(self.widget_446)
        self.pushButton_ac1_9.setObjectName(u"pushButton_ac1_9")
        sizePolicy4.setHeightForWidth(self.pushButton_ac1_9.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_9.setSizePolicy(sizePolicy4)
        self.pushButton_ac1_9.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_215.addWidget(self.pushButton_ac1_9)


        self.verticalLayout_189.addWidget(self.widget_446)

        self.widget_447 = QWidget(self.widget_445)
        self.widget_447.setObjectName(u"widget_447")
        self.verticalLayout_190 = QVBoxLayout(self.widget_447)
        self.verticalLayout_190.setSpacing(0)
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.verticalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.label_93 = QLabel(self.widget_447)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_93.setAlignment(Qt.AlignCenter)

        self.verticalLayout_190.addWidget(self.label_93)


        self.verticalLayout_189.addWidget(self.widget_447)


        self.horizontalLayout_214.addWidget(self.widget_445)

        self.widget_448 = QWidget(self.widget_444)
        self.widget_448.setObjectName(u"widget_448")
        self.verticalLayout_191 = QVBoxLayout(self.widget_448)
        self.verticalLayout_191.setSpacing(0)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.verticalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.widget_449 = QWidget(self.widget_448)
        self.widget_449.setObjectName(u"widget_449")
        self.horizontalLayout_216 = QHBoxLayout(self.widget_449)
        self.horizontalLayout_216.setSpacing(0)
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.horizontalLayout_216.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_9 = QPushButton(self.widget_449)
        self.pushButton_ac2_9.setObjectName(u"pushButton_ac2_9")
        sizePolicy4.setHeightForWidth(self.pushButton_ac2_9.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_9.setSizePolicy(sizePolicy4)
        self.pushButton_ac2_9.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_216.addWidget(self.pushButton_ac2_9)


        self.verticalLayout_191.addWidget(self.widget_449)

        self.widget_450 = QWidget(self.widget_448)
        self.widget_450.setObjectName(u"widget_450")
        self.verticalLayout_192 = QVBoxLayout(self.widget_450)
        self.verticalLayout_192.setSpacing(0)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.verticalLayout_192.setContentsMargins(0, 0, 0, 0)
        self.label_94 = QLabel(self.widget_450)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.verticalLayout_192.addWidget(self.label_94)


        self.verticalLayout_191.addWidget(self.widget_450)


        self.horizontalLayout_214.addWidget(self.widget_448)


        self.verticalLayout_186.addWidget(self.widget_444)


        self.horizontalLayout_213.addWidget(self.widget_442)


        self.verticalLayout_149.addWidget(self.widget_441)


        self.verticalLayout_148.addWidget(self.widget_39)


        self.horizontalLayout_7.addWidget(self.widget_439)


        self.verticalLayout_36.addWidget(self.lisTram_3)

        self.widget_28 = QWidget(self.widget_25)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy2.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy2)
        self.widget_28.setStyleSheet(u"\n"
"border: 1px solid rgb(85, 85, 127);\n"
"margin:5px;")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy2.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy2)
        self.horizontalLayout_231 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_231.setSpacing(0)
        self.horizontalLayout_231.setObjectName(u"horizontalLayout_231")
        self.horizontalLayout_231.setContentsMargins(0, 9, 0, 9)
        self.widget_471 = QWidget(self.widget_29)
        self.widget_471.setObjectName(u"widget_471")
        sizePolicy4.setHeightForWidth(self.widget_471.sizePolicy().hasHeightForWidth())
        self.widget_471.setSizePolicy(sizePolicy4)
        self.widget_471.setLayoutDirection(Qt.LeftToRight)
        self.widget_471.setStyleSheet(u"border:none;\n"
"\n"
"")
        self.verticalLayout_283 = QVBoxLayout(self.widget_471)
        self.verticalLayout_283.setSpacing(0)
        self.verticalLayout_283.setObjectName(u"verticalLayout_283")
        self.verticalLayout_283.setContentsMargins(0, 0, 0, 0)
        self.widget_472 = QWidget(self.widget_471)
        self.widget_472.setObjectName(u"widget_472")
        sizePolicy3.setHeightForWidth(self.widget_472.sizePolicy().hasHeightForWidth())
        self.widget_472.setSizePolicy(sizePolicy3)
        self.widget_472.setLayoutDirection(Qt.LeftToRight)
        self.widget_472.setStyleSheet(u"border:none;\n"
"\n"
"")
        self.verticalLayout_284 = QVBoxLayout(self.widget_472)
        self.verticalLayout_284.setSpacing(0)
        self.verticalLayout_284.setObjectName(u"verticalLayout_284")
        self.verticalLayout_284.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.widget_472)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy3.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy3)
        self.pushButton_12.setMinimumSize(QSize(145, 0))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"	\n"
"	\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_284.addWidget(self.pushButton_12)

        self.label_95 = QLabel(self.widget_472)
        self.label_95.setObjectName(u"label_95")
        sizePolicy3.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy3)
        self.label_95.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_95.setAlignment(Qt.AlignCenter)

        self.verticalLayout_284.addWidget(self.label_95)


        self.verticalLayout_283.addWidget(self.widget_472)


        self.horizontalLayout_231.addWidget(self.widget_471)

        self.widget_473 = QWidget(self.widget_29)
        self.widget_473.setObjectName(u"widget_473")
        sizePolicy4.setHeightForWidth(self.widget_473.sizePolicy().hasHeightForWidth())
        self.widget_473.setSizePolicy(sizePolicy4)
        self.widget_473.setLayoutDirection(Qt.RightToLeft)
        self.widget_473.setStyleSheet(u"border:none;")
        self.verticalLayout_285 = QVBoxLayout(self.widget_473)
        self.verticalLayout_285.setSpacing(0)
        self.verticalLayout_285.setObjectName(u"verticalLayout_285")
        self.verticalLayout_285.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_285.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.widget_473)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy3.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy3)
        self.pushButton_13.setMinimumSize(QSize(100, 0))
        self.pushButton_13.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.verticalLayout_285.addWidget(self.pushButton_13)

        self.label_96 = QLabel(self.widget_473)
        self.label_96.setObjectName(u"label_96")
        sizePolicy4.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy4)
        self.label_96.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_96.setAlignment(Qt.AlignCenter)

        self.verticalLayout_285.addWidget(self.label_96)


        self.horizontalLayout_231.addWidget(self.widget_473)

        self.widget_474 = QWidget(self.widget_29)
        self.widget_474.setObjectName(u"widget_474")
        sizePolicy4.setHeightForWidth(self.widget_474.sizePolicy().hasHeightForWidth())
        self.widget_474.setSizePolicy(sizePolicy4)
        self.widget_474.setStyleSheet(u"border:none;")
        self.verticalLayout_286 = QVBoxLayout(self.widget_474)
        self.verticalLayout_286.setSpacing(0)
        self.verticalLayout_286.setObjectName(u"verticalLayout_286")
        self.verticalLayout_286.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.widget_474)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy3.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy3)
        self.pushButton_14.setMinimumSize(QSize(100, 0))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.verticalLayout_286.addWidget(self.pushButton_14)

        self.label_97 = QLabel(self.widget_474)
        self.label_97.setObjectName(u"label_97")
        sizePolicy4.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy4)
        self.label_97.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_97.setAlignment(Qt.AlignCenter)

        self.verticalLayout_286.addWidget(self.label_97)


        self.horizontalLayout_231.addWidget(self.widget_474)


        self.horizontalLayout_5.addWidget(self.widget_29)


        self.verticalLayout_36.addWidget(self.widget_28)

        self.lisTram_4 = QWidget(self.widget_25)
        self.lisTram_4.setObjectName(u"lisTram_4")
        sizePolicy.setHeightForWidth(self.lisTram_4.sizePolicy().hasHeightForWidth())
        self.lisTram_4.setSizePolicy(sizePolicy)
        self.lisTram_4.setStyleSheet(u"border-right-color: rgb(0, 0, 0);")
        self.horizontalLayout_232 = QHBoxLayout(self.lisTram_4)
        self.horizontalLayout_232.setSpacing(0)
        self.horizontalLayout_232.setObjectName(u"horizontalLayout_232")
        self.horizontalLayout_232.setContentsMargins(0, 15, 30, 0)
        self.widget_30 = QWidget(self.lisTram_4)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy)
        self.widget_30.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_287 = QVBoxLayout(self.widget_30)
        self.verticalLayout_287.setSpacing(0)
        self.verticalLayout_287.setObjectName(u"verticalLayout_287")
        self.verticalLayout_287.setContentsMargins(0, 0, 0, 0)
        self.widget_475 = QWidget(self.widget_30)
        self.widget_475.setObjectName(u"widget_475")
        sizePolicy3.setHeightForWidth(self.widget_475.sizePolicy().hasHeightForWidth())
        self.widget_475.setSizePolicy(sizePolicy3)
        self.widget_475.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_233 = QHBoxLayout(self.widget_475)
        self.horizontalLayout_233.setSpacing(0)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.widget_475)
        self.label_98.setObjectName(u"label_98")
        sizePolicy4.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy4)
        self.label_98.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_233.addWidget(self.label_98)

        self.pushButton_anhsang_18 = QPushButton(self.widget_475)
        self.pushButton_anhsang_18.setObjectName(u"pushButton_anhsang_18")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_18.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_18.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_18.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_18.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_18.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_18.setIconSize(QSize(16, 16))

        self.horizontalLayout_233.addWidget(self.pushButton_anhsang_18)


        self.verticalLayout_287.addWidget(self.widget_475)

        self.widget_476 = QWidget(self.widget_30)
        self.widget_476.setObjectName(u"widget_476")
        sizePolicy3.setHeightForWidth(self.widget_476.sizePolicy().hasHeightForWidth())
        self.widget_476.setSizePolicy(sizePolicy3)
        self.horizontalLayout_234 = QHBoxLayout(self.widget_476)
        self.horizontalLayout_234.setSpacing(0)
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.horizontalLayout_234.setContentsMargins(0, 0, 0, 0)
        self.widget_477 = QWidget(self.widget_476)
        self.widget_477.setObjectName(u"widget_477")
        sizePolicy3.setHeightForWidth(self.widget_477.sizePolicy().hasHeightForWidth())
        self.widget_477.setSizePolicy(sizePolicy3)
        self.verticalLayout_288 = QVBoxLayout(self.widget_477)
        self.verticalLayout_288.setSpacing(0)
        self.verticalLayout_288.setObjectName(u"verticalLayout_288")
        self.verticalLayout_288.setContentsMargins(0, 0, 30, 0)
        self.widget_478 = QWidget(self.widget_477)
        self.widget_478.setObjectName(u"widget_478")
        sizePolicy.setHeightForWidth(self.widget_478.sizePolicy().hasHeightForWidth())
        self.widget_478.setSizePolicy(sizePolicy)
        self.verticalLayout_289 = QVBoxLayout(self.widget_478)
        self.verticalLayout_289.setSpacing(0)
        self.verticalLayout_289.setObjectName(u"verticalLayout_289")
        self.verticalLayout_289.setContentsMargins(0, 0, 0, 20)
        self.label_99 = QLabel(self.widget_478)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setStyleSheet(u"")
        self.label_99.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_99.setScaledContents(True)

        self.verticalLayout_289.addWidget(self.label_99)


        self.verticalLayout_288.addWidget(self.widget_478)

        self.widget_479 = QWidget(self.widget_477)
        self.widget_479.setObjectName(u"widget_479")
        sizePolicy3.setHeightForWidth(self.widget_479.sizePolicy().hasHeightForWidth())
        self.widget_479.setSizePolicy(sizePolicy3)
        self.horizontalLayout_235 = QHBoxLayout(self.widget_479)
        self.horizontalLayout_235.setSpacing(0)
        self.horizontalLayout_235.setObjectName(u"horizontalLayout_235")
        self.horizontalLayout_235.setContentsMargins(0, 0, 0, 0)
        self.widget_480 = QWidget(self.widget_479)
        self.widget_480.setObjectName(u"widget_480")
        self.verticalLayout_290 = QVBoxLayout(self.widget_480)
        self.verticalLayout_290.setSpacing(0)
        self.verticalLayout_290.setObjectName(u"verticalLayout_290")
        self.verticalLayout_290.setContentsMargins(0, 0, 0, 0)
        self.widget_482 = QWidget(self.widget_480)
        self.widget_482.setObjectName(u"widget_482")
        self.verticalLayout_291 = QVBoxLayout(self.widget_482)
        self.verticalLayout_291.setSpacing(0)
        self.verticalLayout_291.setObjectName(u"verticalLayout_291")
        self.verticalLayout_291.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_290.addWidget(self.widget_482)


        self.horizontalLayout_235.addWidget(self.widget_480)

        self.widget_483 = QWidget(self.widget_479)
        self.widget_483.setObjectName(u"widget_483")
        self.verticalLayout_292 = QVBoxLayout(self.widget_483)
        self.verticalLayout_292.setSpacing(0)
        self.verticalLayout_292.setObjectName(u"verticalLayout_292")
        self.verticalLayout_292.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_235.addWidget(self.widget_483)


        self.verticalLayout_288.addWidget(self.widget_479)


        self.horizontalLayout_234.addWidget(self.widget_477)


        self.verticalLayout_287.addWidget(self.widget_476)


        self.horizontalLayout_232.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.lisTram_4)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy)
        self.widget_31.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_300 = QVBoxLayout(self.widget_31)
        self.verticalLayout_300.setObjectName(u"verticalLayout_300")
        self.verticalLayout_300.setContentsMargins(0, 0, 0, 0)
        self.widget_40 = QWidget(self.widget_31)
        self.widget_40.setObjectName(u"widget_40")
        sizePolicy3.setHeightForWidth(self.widget_40.sizePolicy().hasHeightForWidth())
        self.widget_40.setSizePolicy(sizePolicy3)
        self.verticalLayout_301 = QVBoxLayout(self.widget_40)
        self.verticalLayout_301.setSpacing(0)
        self.verticalLayout_301.setObjectName(u"verticalLayout_301")
        self.verticalLayout_301.setContentsMargins(0, 0, 0, 0)
        self.widget_506 = QWidget(self.widget_40)
        self.widget_506.setObjectName(u"widget_506")
        sizePolicy3.setHeightForWidth(self.widget_506.sizePolicy().hasHeightForWidth())
        self.widget_506.setSizePolicy(sizePolicy3)
        self.widget_506.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_252 = QHBoxLayout(self.widget_506)
        self.horizontalLayout_252.setSpacing(0)
        self.horizontalLayout_252.setObjectName(u"horizontalLayout_252")
        self.horizontalLayout_252.setContentsMargins(0, 0, 0, 0)
        self.label_102 = QLabel(self.widget_506)
        self.label_102.setObjectName(u"label_102")
        sizePolicy4.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy4)
        self.label_102.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_252.addWidget(self.label_102)

        self.pushButton_anhsang_19 = QPushButton(self.widget_506)
        self.pushButton_anhsang_19.setObjectName(u"pushButton_anhsang_19")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_19.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_19.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_19.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_19.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_19.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_19.setIconSize(QSize(16, 16))

        self.horizontalLayout_252.addWidget(self.pushButton_anhsang_19)


        self.verticalLayout_301.addWidget(self.widget_506)

        self.widget_507 = QWidget(self.widget_40)
        self.widget_507.setObjectName(u"widget_507")
        sizePolicy3.setHeightForWidth(self.widget_507.sizePolicy().hasHeightForWidth())
        self.widget_507.setSizePolicy(sizePolicy3)
        self.horizontalLayout_253 = QHBoxLayout(self.widget_507)
        self.horizontalLayout_253.setSpacing(0)
        self.horizontalLayout_253.setObjectName(u"horizontalLayout_253")
        self.horizontalLayout_253.setContentsMargins(0, 0, 0, 0)
        self.widget_508 = QWidget(self.widget_507)
        self.widget_508.setObjectName(u"widget_508")
        sizePolicy3.setHeightForWidth(self.widget_508.sizePolicy().hasHeightForWidth())
        self.widget_508.setSizePolicy(sizePolicy3)
        self.verticalLayout_302 = QVBoxLayout(self.widget_508)
        self.verticalLayout_302.setSpacing(0)
        self.verticalLayout_302.setObjectName(u"verticalLayout_302")
        self.verticalLayout_302.setContentsMargins(0, 0, 30, 0)
        self.widget_509 = QWidget(self.widget_508)
        self.widget_509.setObjectName(u"widget_509")
        sizePolicy.setHeightForWidth(self.widget_509.sizePolicy().hasHeightForWidth())
        self.widget_509.setSizePolicy(sizePolicy)
        self.verticalLayout_303 = QVBoxLayout(self.widget_509)
        self.verticalLayout_303.setSpacing(0)
        self.verticalLayout_303.setObjectName(u"verticalLayout_303")
        self.verticalLayout_303.setContentsMargins(0, 0, 0, 20)
        self.label_103 = QLabel(self.widget_509)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setStyleSheet(u"")
        self.label_103.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_103.setScaledContents(True)

        self.verticalLayout_303.addWidget(self.label_103)


        self.verticalLayout_302.addWidget(self.widget_509)

        self.widget_510 = QWidget(self.widget_508)
        self.widget_510.setObjectName(u"widget_510")
        sizePolicy3.setHeightForWidth(self.widget_510.sizePolicy().hasHeightForWidth())
        self.widget_510.setSizePolicy(sizePolicy3)
        self.horizontalLayout_254 = QHBoxLayout(self.widget_510)
        self.horizontalLayout_254.setSpacing(0)
        self.horizontalLayout_254.setObjectName(u"horizontalLayout_254")
        self.horizontalLayout_254.setContentsMargins(0, 0, 0, 0)
        self.widget_511 = QWidget(self.widget_510)
        self.widget_511.setObjectName(u"widget_511")
        self.verticalLayout_304 = QVBoxLayout(self.widget_511)
        self.verticalLayout_304.setSpacing(0)
        self.verticalLayout_304.setObjectName(u"verticalLayout_304")
        self.verticalLayout_304.setContentsMargins(0, 0, 0, 0)
        self.widget_513 = QWidget(self.widget_511)
        self.widget_513.setObjectName(u"widget_513")
        self.verticalLayout_305 = QVBoxLayout(self.widget_513)
        self.verticalLayout_305.setSpacing(0)
        self.verticalLayout_305.setObjectName(u"verticalLayout_305")
        self.verticalLayout_305.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_304.addWidget(self.widget_513)


        self.horizontalLayout_254.addWidget(self.widget_511)


        self.verticalLayout_302.addWidget(self.widget_510)


        self.horizontalLayout_253.addWidget(self.widget_508)


        self.verticalLayout_301.addWidget(self.widget_507)


        self.verticalLayout_300.addWidget(self.widget_40)


        self.horizontalLayout_232.addWidget(self.widget_31)

        self.widget_537 = QWidget(self.lisTram_4)
        self.widget_537.setObjectName(u"widget_537")
        self.widget_537.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_314 = QVBoxLayout(self.widget_537)
        self.verticalLayout_314.setSpacing(0)
        self.verticalLayout_314.setObjectName(u"verticalLayout_314")
        self.verticalLayout_314.setContentsMargins(0, 0, 0, 0)
        self.widget_538 = QWidget(self.widget_537)
        self.widget_538.setObjectName(u"widget_538")
        sizePolicy3.setHeightForWidth(self.widget_538.sizePolicy().hasHeightForWidth())
        self.widget_538.setSizePolicy(sizePolicy3)
        self.verticalLayout_315 = QVBoxLayout(self.widget_538)
        self.verticalLayout_315.setSpacing(0)
        self.verticalLayout_315.setObjectName(u"verticalLayout_315")
        self.verticalLayout_315.setContentsMargins(0, 0, 0, 0)
        self.widget_539 = QWidget(self.widget_538)
        self.widget_539.setObjectName(u"widget_539")
        sizePolicy3.setHeightForWidth(self.widget_539.sizePolicy().hasHeightForWidth())
        self.widget_539.setSizePolicy(sizePolicy3)
        self.widget_539.setStyleSheet(u"font: 700 16pt \"Times New Roman\";")
        self.horizontalLayout_271 = QHBoxLayout(self.widget_539)
        self.horizontalLayout_271.setSpacing(0)
        self.horizontalLayout_271.setObjectName(u"horizontalLayout_271")
        self.horizontalLayout_271.setContentsMargins(0, 0, 0, 0)
        self.label_106 = QLabel(self.widget_539)
        self.label_106.setObjectName(u"label_106")
        sizePolicy4.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy4)
        self.label_106.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_271.addWidget(self.label_106)

        self.pushButton_anhsang_20 = QPushButton(self.widget_539)
        self.pushButton_anhsang_20.setObjectName(u"pushButton_anhsang_20")
        sizePolicy1.setHeightForWidth(self.pushButton_anhsang_20.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_20.setSizePolicy(sizePolicy1)
        self.pushButton_anhsang_20.setMinimumSize(QSize(50, 28))
        self.pushButton_anhsang_20.setMaximumSize(QSize(50, 28))
        self.pushButton_anhsang_20.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_anhsang_20.setIconSize(QSize(16, 16))

        self.horizontalLayout_271.addWidget(self.pushButton_anhsang_20)


        self.verticalLayout_315.addWidget(self.widget_539)

        self.widget_540 = QWidget(self.widget_538)
        self.widget_540.setObjectName(u"widget_540")
        sizePolicy3.setHeightForWidth(self.widget_540.sizePolicy().hasHeightForWidth())
        self.widget_540.setSizePolicy(sizePolicy3)
        self.horizontalLayout_272 = QHBoxLayout(self.widget_540)
        self.horizontalLayout_272.setSpacing(0)
        self.horizontalLayout_272.setObjectName(u"horizontalLayout_272")
        self.horizontalLayout_272.setContentsMargins(0, 0, 0, 0)
        self.widget_541 = QWidget(self.widget_540)
        self.widget_541.setObjectName(u"widget_541")
        sizePolicy3.setHeightForWidth(self.widget_541.sizePolicy().hasHeightForWidth())
        self.widget_541.setSizePolicy(sizePolicy3)
        self.verticalLayout_316 = QVBoxLayout(self.widget_541)
        self.verticalLayout_316.setSpacing(0)
        self.verticalLayout_316.setObjectName(u"verticalLayout_316")
        self.verticalLayout_316.setContentsMargins(0, 0, 30, 0)
        self.widget_542 = QWidget(self.widget_541)
        self.widget_542.setObjectName(u"widget_542")
        sizePolicy.setHeightForWidth(self.widget_542.sizePolicy().hasHeightForWidth())
        self.widget_542.setSizePolicy(sizePolicy)
        self.verticalLayout_317 = QVBoxLayout(self.widget_542)
        self.verticalLayout_317.setSpacing(0)
        self.verticalLayout_317.setObjectName(u"verticalLayout_317")
        self.verticalLayout_317.setContentsMargins(0, 0, 0, 20)
        self.label_107 = QLabel(self.widget_542)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"")
        self.label_107.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_107.setScaledContents(True)

        self.verticalLayout_317.addWidget(self.label_107)


        self.verticalLayout_316.addWidget(self.widget_542)

        self.widget_543 = QWidget(self.widget_541)
        self.widget_543.setObjectName(u"widget_543")
        sizePolicy3.setHeightForWidth(self.widget_543.sizePolicy().hasHeightForWidth())
        self.widget_543.setSizePolicy(sizePolicy3)
        self.horizontalLayout_273 = QHBoxLayout(self.widget_543)
        self.horizontalLayout_273.setSpacing(0)
        self.horizontalLayout_273.setObjectName(u"horizontalLayout_273")
        self.horizontalLayout_273.setContentsMargins(0, 0, 0, 0)
        self.widget_544 = QWidget(self.widget_543)
        self.widget_544.setObjectName(u"widget_544")
        self.verticalLayout_318 = QVBoxLayout(self.widget_544)
        self.verticalLayout_318.setSpacing(0)
        self.verticalLayout_318.setObjectName(u"verticalLayout_318")
        self.verticalLayout_318.setContentsMargins(0, 0, 0, 0)
        self.widget_546 = QWidget(self.widget_544)
        self.widget_546.setObjectName(u"widget_546")
        self.verticalLayout_319 = QVBoxLayout(self.widget_546)
        self.verticalLayout_319.setSpacing(0)
        self.verticalLayout_319.setObjectName(u"verticalLayout_319")
        self.verticalLayout_319.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_318.addWidget(self.widget_546)


        self.horizontalLayout_273.addWidget(self.widget_544)


        self.verticalLayout_316.addWidget(self.widget_543)


        self.horizontalLayout_272.addWidget(self.widget_541)


        self.verticalLayout_315.addWidget(self.widget_540)


        self.verticalLayout_314.addWidget(self.widget_538)


        self.horizontalLayout_232.addWidget(self.widget_537)


        self.verticalLayout_36.addWidget(self.lisTram_4)


        self.verticalLayout_21.addWidget(self.widget_25)


        self.verticalLayout_3.addWidget(self.widget_23)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_134 = QPushButton(self.widget)
        self.pushButton_134.setObjectName(u"pushButton_134")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_134.sizePolicy().hasHeightForWidth())
        self.pushButton_134.setSizePolicy(sizePolicy7)
        self.pushButton_134.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_134.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Times New Roman\";\n"
"")
        self.pushButton_134.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_134)

        self.pushButton_HDSD = QPushButton(self.widget)
        self.pushButton_HDSD.setObjectName(u"pushButton_HDSD")
        sizePolicy7.setHeightForWidth(self.pushButton_HDSD.sizePolicy().hasHeightForWidth())
        self.pushButton_HDSD.setSizePolicy(sizePolicy7)
        self.pushButton_HDSD.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_HDSD.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Times New Roman\";\n"
"")
        self.pushButton_HDSD.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_HDSD)

        self.pushButton_135 = QPushButton(self.widget)
        self.pushButton_135.setObjectName(u"pushButton_135")
        sizePolicy7.setHeightForWidth(self.pushButton_135.sizePolicy().hasHeightForWidth())
        self.pushButton_135.setSizePolicy(sizePolicy7)
        self.pushButton_135.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_135.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Times New Roman\";\n"
"")
        self.pushButton_135.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_135)


        self.verticalLayout_3.addWidget(self.widget)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout_14.addWidget(self.stackedWidget)

        self.verticalScrollBar = QScrollBar(self.pagesContainer)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalScrollBar)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(26)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"H\u1ec6 TH\u1ed0NG GI\u00c1M S\u00c1T, C\u1ea2NH B\u00c1O T\u1eea XA CHO C\u00c1C TR\u1ea0M V\u00c0 KHO TH\u00d4NG TIN", None))
        self.label_2.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A70", None))
        self.pushButton_anhsang_9.setText("")
        self.label_8.setText("")
        self.pushButton_ac1.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u" AC1", None))
        self.pushButton_ac2.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u" AC2", None))
        self.pushButton_nhietdo.setText("")
        self.label_nhietdo_3.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9:", None))
        self.pushButton_doam.setText("")
        self.label_doam_2.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 \u1ea9m:", None))
        self.pushButton_dc1.setText("")
        self.label_dc1.setText(QCoreApplication.translate("MainWindow", u"DC1:", None))
        self.pushButton_dc2.setText("")
        self.label_dc2.setText(QCoreApplication.translate("MainWindow", u"DC2 :", None))
        self.pushButton_anhsang.setText("")
        self.label_anhsang.setText(QCoreApplication.translate("MainWindow", u"\u00c1nh s\u00e1ng:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A45", None))
        self.pushButton_anhsang_10.setText("")
        self.label_10.setText("")
        self.pushButton_ac1_2.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u" AC1", None))
        self.pushButton_ac2_2.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u" AC2", None))
        self.pushButton_nhietdo_3.setText("")
        self.label_nhietdo_8.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9:", None))
        self.pushButton_doam_2.setText("")
        self.label_doam_3.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 \u1ea9m:", None))
        self.pushButton_dc1_2.setText("")
        self.label_dc1_2.setText(QCoreApplication.translate("MainWindow", u"DC1:", None))
        self.pushButton_dc2_2.setText("")
        self.label_dc2_2.setText(QCoreApplication.translate("MainWindow", u"DC2 :", None))
        self.pushButton_anhsang_2.setText("")
        self.label_anhsang_2.setText(QCoreApplication.translate("MainWindow", u"\u00c1nh s\u00e1ng:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A01", None))
        self.pushButton_anhsang_11.setText("")
        self.label_12.setText("")
        self.pushButton_ac1_3.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u" AC1", None))
        self.pushButton_ac2_3.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u" AC2", None))
        self.pushButton_nhietdo_14.setText("")
        self.label_nhietdo_16.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9:", None))
        self.pushButton_nhietdo_15.setText("")
        self.label_nhietdo_17.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 \u1ea9m:", None))
        self.pushButton_nhietdo_16.setText("")
        self.label_nhietdo_18.setText(QCoreApplication.translate("MainWindow", u"DC1:", None))
        self.pushButton_nhietdo_17.setText("")
        self.label_nhietdo_19.setText(QCoreApplication.translate("MainWindow", u"DC2 :", None))
        self.pushButton_nhietdo_18.setText("")
        self.label_nhietdo_20.setText(QCoreApplication.translate("MainWindow", u"\u00c1nh s\u00e1ng:", None))
        self.pushButton_11.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"T\u1ed0T", None))
        self.pushButton_10.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"C\u1ea3nh b\u00e1o m\u1ee9c 1", None))
        self.pushButton_9.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"C\u1ea3nh b\u00e1o m\u1ee9c 2", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A48", None))
        self.pushButton_anhsang_12.setText("")
        self.label_11.setText("")
        self.pushButton_ac1_4.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u" AC1", None))
        self.pushButton_ac2_4.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u" AC2", None))
        self.pushButton_nhietdo_6.setText("")
        self.label_nhietdo_5.setText(QCoreApplication.translate("MainWindow", u" Nhi\u1ec7t \u0111\u1ed9:", None))
        self.pushButton_nhietdo_9.setText("")
        self.label_nhietdo_13.setText(QCoreApplication.translate("MainWindow", u" \u0110\u1ed9 \u1ea9m:", None))
        self.pushButton_nhietdo_10.setText("")
        self.label_nhietdo_14.setText(QCoreApplication.translate("MainWindow", u" DC1:", None))
        self.pushButton_nhietdo_19.setText("")
        self.label_nhietdo_21.setText(QCoreApplication.translate("MainWindow", u" DC2:", None))
        self.pushButton_nhietdo_20.setText("")
        self.label_nhietdo_22.setText(QCoreApplication.translate("MainWindow", u" \u00c1nh s\u00e1ng:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A71", None))
        self.pushButton_anhsang_13.setText("")
        self.label_13.setText("")
        self.pushButton_ac1_5.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u" AC1", None))
        self.pushButton_ac2_5.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u" AC2", None))
        self.pushButton_nhietdo_21.setText("")
        self.label_nhietdo_23.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9:", None))
        self.pushButton_nhietdo_22.setText("")
        self.label_nhietdo_24.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 \u1ea9m:", None))
        self.pushButton_nhietdo_23.setText("")
        self.label_nhietdo_25.setText(QCoreApplication.translate("MainWindow", u"DC1:", None))
        self.pushButton_nhietdo_24.setText("")
        self.label_nhietdo_26.setText(QCoreApplication.translate("MainWindow", u"DC2:", None))
        self.pushButton_nhietdo_25.setText("")
        self.label_nhietdo_27.setText(QCoreApplication.translate("MainWindow", u"\u00c1nh s\u00e1ng:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A76", None))
        self.pushButton_anhsang_14.setText("")
        self.label_14.setText("")
        self.pushButton_ac1_6.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u" AC1", None))
        self.pushButton_ac2_6.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u" AC2", None))
        self.pushButton_nhietdo_26.setText("")
        self.label_nhietdo_28.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9:", None))
        self.pushButton_nhietdo_27.setText("")
        self.label_nhietdo_29.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 \u1ea9m:", None))
        self.pushButton_nhietdo_28.setText("")
        self.label_nhietdo_30.setText(QCoreApplication.translate("MainWindow", u"DC1:", None))
        self.pushButton_nhietdo_29.setText("")
        self.label_nhietdo_31.setText(QCoreApplication.translate("MainWindow", u"DC2:", None))
        self.pushButton_nhietdo_30.setText("")
        self.label_nhietdo_32.setText(QCoreApplication.translate("MainWindow", u"\u00c1nh s\u00e1ng:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"L\u1eef \u0111o\u00e0n 139", None))
        self.title_nhietdo_2.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 nhi\u1ec7t \u0111\u1ed9", None))
        self.thoigian_nhietdo_2.setText("")
        self.title_nhietdo.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 nhi\u1ec7t \u0111\u1ed9", None))
        self.thoigian_nhietdo.setText("")
        self.label_doam.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0111\u1ed9 \u1ea9m", None))
        self.label_thoigian_doam.setText("")
        self.label_doam_4.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0111\u1ed9 \u1ea9m", None))
        self.label_thoigian_doam_2.setText("")
        self.label_doam_9.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0111\u1ed9 \u1ea9m", None))
        self.label_thoigian_doam_5.setText("")
        self.label_diepap.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0110i\u1ec7n \u00e1p", None))
        self.label_thoigian_dienap.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 nhi\u1ec7t \u0111\u1ed9", None))
        ___qtablewidgetitem = self.tableWidget_nhietdo_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem1 = self.tableWidget_nhietdo_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem2 = self.tableWidget_nhietdo_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem3 = self.tableWidget_nhietdo_3.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget_nhietdo_3.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem5 = self.tableWidget_nhietdo_3.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem6 = self.tableWidget_nhietdo_3.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem7 = self.tableWidget_nhietdo_3.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem8 = self.tableWidget_nhietdo_3.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem9 = self.tableWidget_nhietdo_3.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem10 = self.tableWidget_nhietdo_3.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem11 = self.tableWidget_nhietdo_3.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_3.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC1", None))
        ___qtablewidgetitem12 = self.tableWidget_dc1_3.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem13 = self.tableWidget_dc1_3.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem14 = self.tableWidget_dc1_3.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem15 = self.tableWidget_dc1_3.verticalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem16 = self.tableWidget_dc1_3.verticalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem17 = self.tableWidget_dc1_3.verticalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem18 = self.tableWidget_dc1_3.verticalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem19 = self.tableWidget_dc1_3.verticalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem20 = self.tableWidget_dc1_3.verticalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem21 = self.tableWidget_dc1_3.verticalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem22 = self.tableWidget_dc1_3.verticalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem23 = self.tableWidget_dc1_3.verticalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_9.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC1", None))
        ___qtablewidgetitem24 = self.tableWidget_ac1_2.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem25 = self.tableWidget_ac1_2.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem26 = self.tableWidget_ac1_2.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem27 = self.tableWidget_ac1_2.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem28 = self.tableWidget_ac1_2.verticalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem29 = self.tableWidget_ac1_2.verticalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem30 = self.tableWidget_ac1_2.verticalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem31 = self.tableWidget_ac1_2.verticalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem32 = self.tableWidget_ac1_2.verticalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem33 = self.tableWidget_ac1_2.verticalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem34 = self.tableWidget_ac1_2.verticalHeaderItem(7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem35 = self.tableWidget_ac1_2.verticalHeaderItem(8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_10.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111\u1ed9 \u1ea9m", None))
        ___qtablewidgetitem36 = self.tableWidget_doam_3.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem37 = self.tableWidget_doam_3.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem38 = self.tableWidget_doam_3.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem39 = self.tableWidget_doam_3.verticalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem40 = self.tableWidget_doam_3.verticalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem41 = self.tableWidget_doam_3.verticalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem42 = self.tableWidget_doam_3.verticalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem43 = self.tableWidget_doam_3.verticalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem44 = self.tableWidget_doam_3.verticalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem45 = self.tableWidget_doam_3.verticalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem46 = self.tableWidget_doam_3.verticalHeaderItem(7)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem47 = self.tableWidget_doam_3.verticalHeaderItem(8)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_11.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC2", None))
        ___qtablewidgetitem48 = self.tableWidget_dc2_3.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem49 = self.tableWidget_dc2_3.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem50 = self.tableWidget_dc2_3.horizontalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem51 = self.tableWidget_dc2_3.verticalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem52 = self.tableWidget_dc2_3.verticalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem53 = self.tableWidget_dc2_3.verticalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem54 = self.tableWidget_dc2_3.verticalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem55 = self.tableWidget_dc2_3.verticalHeaderItem(4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem56 = self.tableWidget_dc2_3.verticalHeaderItem(5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem57 = self.tableWidget_dc2_3.verticalHeaderItem(6)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem58 = self.tableWidget_dc2_3.verticalHeaderItem(7)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem59 = self.tableWidget_dc2_3.verticalHeaderItem(8)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_14.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC2", None))
        ___qtablewidgetitem60 = self.tableWidget_ac2_2.horizontalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem61 = self.tableWidget_ac2_2.horizontalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem62 = self.tableWidget_ac2_2.horizontalHeaderItem(2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem63 = self.tableWidget_ac2_2.verticalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem64 = self.tableWidget_ac2_2.verticalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem65 = self.tableWidget_ac2_2.verticalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem66 = self.tableWidget_ac2_2.verticalHeaderItem(3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem67 = self.tableWidget_ac2_2.verticalHeaderItem(4)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem68 = self.tableWidget_ac2_2.verticalHeaderItem(5)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem69 = self.tableWidget_ac2_2.verticalHeaderItem(6)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem70 = self.tableWidget_ac2_2.verticalHeaderItem(7)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem71 = self.tableWidget_ac2_2.verticalHeaderItem(8)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_15.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_diepap_2.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0110i\u1ec7n \u00e1p", None))
        self.label_thoigian_dienap_2.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 nhi\u1ec7t \u0111\u1ed9", None))
        ___qtablewidgetitem72 = self.tableWidget_nhietdo_2.horizontalHeaderItem(0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem73 = self.tableWidget_nhietdo_2.horizontalHeaderItem(1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem74 = self.tableWidget_nhietdo_2.horizontalHeaderItem(2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem75 = self.tableWidget_nhietdo_2.verticalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem76 = self.tableWidget_nhietdo_2.verticalHeaderItem(1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem77 = self.tableWidget_nhietdo_2.verticalHeaderItem(2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem78 = self.tableWidget_nhietdo_2.verticalHeaderItem(3)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem79 = self.tableWidget_nhietdo_2.verticalHeaderItem(4)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem80 = self.tableWidget_nhietdo_2.verticalHeaderItem(5)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem81 = self.tableWidget_nhietdo_2.verticalHeaderItem(6)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem82 = self.tableWidget_nhietdo_2.verticalHeaderItem(7)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem83 = self.tableWidget_nhietdo_2.verticalHeaderItem(8)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_2.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC1", None))
        ___qtablewidgetitem84 = self.tableWidget_dc1_2.horizontalHeaderItem(0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem85 = self.tableWidget_dc1_2.horizontalHeaderItem(1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem86 = self.tableWidget_dc1_2.horizontalHeaderItem(2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem87 = self.tableWidget_dc1_2.verticalHeaderItem(0)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem88 = self.tableWidget_dc1_2.verticalHeaderItem(1)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem89 = self.tableWidget_dc1_2.verticalHeaderItem(2)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem90 = self.tableWidget_dc1_2.verticalHeaderItem(3)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem91 = self.tableWidget_dc1_2.verticalHeaderItem(4)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem92 = self.tableWidget_dc1_2.verticalHeaderItem(5)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem93 = self.tableWidget_dc1_2.verticalHeaderItem(6)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem94 = self.tableWidget_dc1_2.verticalHeaderItem(7)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem95 = self.tableWidget_dc1_2.verticalHeaderItem(8)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_6.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC1", None))
        ___qtablewidgetitem96 = self.tableWidget_ac1.horizontalHeaderItem(0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem97 = self.tableWidget_ac1.horizontalHeaderItem(1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem98 = self.tableWidget_ac1.horizontalHeaderItem(2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem99 = self.tableWidget_ac1.verticalHeaderItem(0)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem100 = self.tableWidget_ac1.verticalHeaderItem(1)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem101 = self.tableWidget_ac1.verticalHeaderItem(2)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem102 = self.tableWidget_ac1.verticalHeaderItem(3)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem103 = self.tableWidget_ac1.verticalHeaderItem(4)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem104 = self.tableWidget_ac1.verticalHeaderItem(5)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem105 = self.tableWidget_ac1.verticalHeaderItem(6)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem106 = self.tableWidget_ac1.verticalHeaderItem(7)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem107 = self.tableWidget_ac1.verticalHeaderItem(8)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_7.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111\u1ed9 \u1ea9m", None))
        ___qtablewidgetitem108 = self.tableWidget_doam_2.horizontalHeaderItem(0)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem109 = self.tableWidget_doam_2.horizontalHeaderItem(1)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem110 = self.tableWidget_doam_2.horizontalHeaderItem(2)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem111 = self.tableWidget_doam_2.verticalHeaderItem(0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem112 = self.tableWidget_doam_2.verticalHeaderItem(1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem113 = self.tableWidget_doam_2.verticalHeaderItem(2)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem114 = self.tableWidget_doam_2.verticalHeaderItem(3)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem115 = self.tableWidget_doam_2.verticalHeaderItem(4)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem116 = self.tableWidget_doam_2.verticalHeaderItem(5)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem117 = self.tableWidget_doam_2.verticalHeaderItem(6)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem118 = self.tableWidget_doam_2.verticalHeaderItem(7)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem119 = self.tableWidget_doam_2.verticalHeaderItem(8)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_8.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC2", None))
        ___qtablewidgetitem120 = self.tableWidget_dc2_2.horizontalHeaderItem(0)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem121 = self.tableWidget_dc2_2.horizontalHeaderItem(1)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem122 = self.tableWidget_dc2_2.horizontalHeaderItem(2)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem123 = self.tableWidget_dc2_2.verticalHeaderItem(0)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem124 = self.tableWidget_dc2_2.verticalHeaderItem(1)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem125 = self.tableWidget_dc2_2.verticalHeaderItem(2)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem126 = self.tableWidget_dc2_2.verticalHeaderItem(3)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem127 = self.tableWidget_dc2_2.verticalHeaderItem(4)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem128 = self.tableWidget_dc2_2.verticalHeaderItem(5)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem129 = self.tableWidget_dc2_2.verticalHeaderItem(6)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem130 = self.tableWidget_dc2_2.verticalHeaderItem(7)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem131 = self.tableWidget_dc2_2.verticalHeaderItem(8)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_12.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC2", None))
        ___qtablewidgetitem132 = self.tableWidget_ac2.horizontalHeaderItem(0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem133 = self.tableWidget_ac2.horizontalHeaderItem(1)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem134 = self.tableWidget_ac2.horizontalHeaderItem(2)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem135 = self.tableWidget_ac2.verticalHeaderItem(0)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem136 = self.tableWidget_ac2.verticalHeaderItem(1)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem137 = self.tableWidget_ac2.verticalHeaderItem(2)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem138 = self.tableWidget_ac2.verticalHeaderItem(3)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem139 = self.tableWidget_ac2.verticalHeaderItem(4)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem140 = self.tableWidget_ac2.verticalHeaderItem(5)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem141 = self.tableWidget_ac2.verticalHeaderItem(6)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem142 = self.tableWidget_ac2.verticalHeaderItem(7)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem143 = self.tableWidget_ac2.verticalHeaderItem(8)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_13.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.title_nhietdo_3.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 nhi\u1ec7t \u0111\u1ed9", None))
        self.thoigian_nhietdo_3.setText("")
        self.label_diepap_3.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0110i\u1ec7n \u00e1p", None))
        self.label_thoigian_dienap_3.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 nhi\u1ec7t \u0111\u1ed9", None))
        ___qtablewidgetitem144 = self.tableWidget_nhietdo_4.horizontalHeaderItem(0)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem145 = self.tableWidget_nhietdo_4.horizontalHeaderItem(1)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem146 = self.tableWidget_nhietdo_4.horizontalHeaderItem(2)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem147 = self.tableWidget_nhietdo_4.verticalHeaderItem(0)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem148 = self.tableWidget_nhietdo_4.verticalHeaderItem(1)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem149 = self.tableWidget_nhietdo_4.verticalHeaderItem(2)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem150 = self.tableWidget_nhietdo_4.verticalHeaderItem(3)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem151 = self.tableWidget_nhietdo_4.verticalHeaderItem(4)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem152 = self.tableWidget_nhietdo_4.verticalHeaderItem(5)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem153 = self.tableWidget_nhietdo_4.verticalHeaderItem(6)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem154 = self.tableWidget_nhietdo_4.verticalHeaderItem(7)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem155 = self.tableWidget_nhietdo_4.verticalHeaderItem(8)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_4.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC1", None))
        ___qtablewidgetitem156 = self.tableWidget_dc1_4.horizontalHeaderItem(0)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem157 = self.tableWidget_dc1_4.horizontalHeaderItem(1)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem158 = self.tableWidget_dc1_4.horizontalHeaderItem(2)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem159 = self.tableWidget_dc1_4.verticalHeaderItem(0)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem160 = self.tableWidget_dc1_4.verticalHeaderItem(1)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem161 = self.tableWidget_dc1_4.verticalHeaderItem(2)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem162 = self.tableWidget_dc1_4.verticalHeaderItem(3)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem163 = self.tableWidget_dc1_4.verticalHeaderItem(4)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem164 = self.tableWidget_dc1_4.verticalHeaderItem(5)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem165 = self.tableWidget_dc1_4.verticalHeaderItem(6)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem166 = self.tableWidget_dc1_4.verticalHeaderItem(7)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem167 = self.tableWidget_dc1_4.verticalHeaderItem(8)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_16.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC1", None))
        ___qtablewidgetitem168 = self.tableWidget_ac1_3.horizontalHeaderItem(0)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem169 = self.tableWidget_ac1_3.horizontalHeaderItem(1)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem170 = self.tableWidget_ac1_3.horizontalHeaderItem(2)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem171 = self.tableWidget_ac1_3.verticalHeaderItem(0)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem172 = self.tableWidget_ac1_3.verticalHeaderItem(1)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem173 = self.tableWidget_ac1_3.verticalHeaderItem(2)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem174 = self.tableWidget_ac1_3.verticalHeaderItem(3)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem175 = self.tableWidget_ac1_3.verticalHeaderItem(4)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem176 = self.tableWidget_ac1_3.verticalHeaderItem(5)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem177 = self.tableWidget_ac1_3.verticalHeaderItem(6)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem178 = self.tableWidget_ac1_3.verticalHeaderItem(7)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem179 = self.tableWidget_ac1_3.verticalHeaderItem(8)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_17.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111\u1ed9 \u1ea9m", None))
        ___qtablewidgetitem180 = self.tableWidget_doam_4.horizontalHeaderItem(0)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem181 = self.tableWidget_doam_4.horizontalHeaderItem(1)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem182 = self.tableWidget_doam_4.horizontalHeaderItem(2)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem183 = self.tableWidget_doam_4.verticalHeaderItem(0)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem184 = self.tableWidget_doam_4.verticalHeaderItem(1)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem185 = self.tableWidget_doam_4.verticalHeaderItem(2)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem186 = self.tableWidget_doam_4.verticalHeaderItem(3)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem187 = self.tableWidget_doam_4.verticalHeaderItem(4)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem188 = self.tableWidget_doam_4.verticalHeaderItem(5)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem189 = self.tableWidget_doam_4.verticalHeaderItem(6)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem190 = self.tableWidget_doam_4.verticalHeaderItem(7)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem191 = self.tableWidget_doam_4.verticalHeaderItem(8)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_18.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC2", None))
        ___qtablewidgetitem192 = self.tableWidget_dc2_4.horizontalHeaderItem(0)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem193 = self.tableWidget_dc2_4.horizontalHeaderItem(1)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem194 = self.tableWidget_dc2_4.horizontalHeaderItem(2)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem195 = self.tableWidget_dc2_4.verticalHeaderItem(0)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem196 = self.tableWidget_dc2_4.verticalHeaderItem(1)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem197 = self.tableWidget_dc2_4.verticalHeaderItem(2)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem198 = self.tableWidget_dc2_4.verticalHeaderItem(3)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem199 = self.tableWidget_dc2_4.verticalHeaderItem(4)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem200 = self.tableWidget_dc2_4.verticalHeaderItem(5)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem201 = self.tableWidget_dc2_4.verticalHeaderItem(6)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem202 = self.tableWidget_dc2_4.verticalHeaderItem(7)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem203 = self.tableWidget_dc2_4.verticalHeaderItem(8)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_19.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC2", None))
        ___qtablewidgetitem204 = self.tableWidget_ac2_3.horizontalHeaderItem(0)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem205 = self.tableWidget_ac2_3.horizontalHeaderItem(1)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem206 = self.tableWidget_ac2_3.horizontalHeaderItem(2)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem207 = self.tableWidget_ac2_3.verticalHeaderItem(0)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem208 = self.tableWidget_ac2_3.verticalHeaderItem(1)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem209 = self.tableWidget_ac2_3.verticalHeaderItem(2)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem210 = self.tableWidget_ac2_3.verticalHeaderItem(3)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem211 = self.tableWidget_ac2_3.verticalHeaderItem(4)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem212 = self.tableWidget_ac2_3.verticalHeaderItem(5)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem213 = self.tableWidget_ac2_3.verticalHeaderItem(6)
        ___qtablewidgetitem213.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem214 = self.tableWidget_ac2_3.verticalHeaderItem(7)
        ___qtablewidgetitem214.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem215 = self.tableWidget_ac2_3.verticalHeaderItem(8)
        ___qtablewidgetitem215.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_20.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_doam_10.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0111\u1ed9 \u1ea9m", None))
        self.label_thoigian_doam_6.setText("")
        self.label_diepap_6.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0110i\u1ec7n \u00e1p", None))
        self.label_thoigian_dienap_6.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 nhi\u1ec7t \u0111\u1ed9", None))
        ___qtablewidgetitem216 = self.tableWidget_nhietdo_5.horizontalHeaderItem(0)
        ___qtablewidgetitem216.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem217 = self.tableWidget_nhietdo_5.horizontalHeaderItem(1)
        ___qtablewidgetitem217.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem218 = self.tableWidget_nhietdo_5.horizontalHeaderItem(2)
        ___qtablewidgetitem218.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem219 = self.tableWidget_nhietdo_5.verticalHeaderItem(0)
        ___qtablewidgetitem219.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem220 = self.tableWidget_nhietdo_5.verticalHeaderItem(1)
        ___qtablewidgetitem220.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem221 = self.tableWidget_nhietdo_5.verticalHeaderItem(2)
        ___qtablewidgetitem221.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem222 = self.tableWidget_nhietdo_5.verticalHeaderItem(3)
        ___qtablewidgetitem222.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem223 = self.tableWidget_nhietdo_5.verticalHeaderItem(4)
        ___qtablewidgetitem223.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem224 = self.tableWidget_nhietdo_5.verticalHeaderItem(5)
        ___qtablewidgetitem224.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem225 = self.tableWidget_nhietdo_5.verticalHeaderItem(6)
        ___qtablewidgetitem225.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem226 = self.tableWidget_nhietdo_5.verticalHeaderItem(7)
        ___qtablewidgetitem226.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem227 = self.tableWidget_nhietdo_5.verticalHeaderItem(8)
        ___qtablewidgetitem227.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_5.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC1", None))
        ___qtablewidgetitem228 = self.tableWidget_dc1_5.horizontalHeaderItem(0)
        ___qtablewidgetitem228.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem229 = self.tableWidget_dc1_5.horizontalHeaderItem(1)
        ___qtablewidgetitem229.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem230 = self.tableWidget_dc1_5.horizontalHeaderItem(2)
        ___qtablewidgetitem230.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem231 = self.tableWidget_dc1_5.verticalHeaderItem(0)
        ___qtablewidgetitem231.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem232 = self.tableWidget_dc1_5.verticalHeaderItem(1)
        ___qtablewidgetitem232.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem233 = self.tableWidget_dc1_5.verticalHeaderItem(2)
        ___qtablewidgetitem233.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem234 = self.tableWidget_dc1_5.verticalHeaderItem(3)
        ___qtablewidgetitem234.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem235 = self.tableWidget_dc1_5.verticalHeaderItem(4)
        ___qtablewidgetitem235.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem236 = self.tableWidget_dc1_5.verticalHeaderItem(5)
        ___qtablewidgetitem236.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem237 = self.tableWidget_dc1_5.verticalHeaderItem(6)
        ___qtablewidgetitem237.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem238 = self.tableWidget_dc1_5.verticalHeaderItem(7)
        ___qtablewidgetitem238.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem239 = self.tableWidget_dc1_5.verticalHeaderItem(8)
        ___qtablewidgetitem239.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_21.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC1", None))
        ___qtablewidgetitem240 = self.tableWidget_ac1_4.horizontalHeaderItem(0)
        ___qtablewidgetitem240.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem241 = self.tableWidget_ac1_4.horizontalHeaderItem(1)
        ___qtablewidgetitem241.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem242 = self.tableWidget_ac1_4.horizontalHeaderItem(2)
        ___qtablewidgetitem242.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem243 = self.tableWidget_ac1_4.verticalHeaderItem(0)
        ___qtablewidgetitem243.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem244 = self.tableWidget_ac1_4.verticalHeaderItem(1)
        ___qtablewidgetitem244.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem245 = self.tableWidget_ac1_4.verticalHeaderItem(2)
        ___qtablewidgetitem245.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem246 = self.tableWidget_ac1_4.verticalHeaderItem(3)
        ___qtablewidgetitem246.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem247 = self.tableWidget_ac1_4.verticalHeaderItem(4)
        ___qtablewidgetitem247.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem248 = self.tableWidget_ac1_4.verticalHeaderItem(5)
        ___qtablewidgetitem248.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem249 = self.tableWidget_ac1_4.verticalHeaderItem(6)
        ___qtablewidgetitem249.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem250 = self.tableWidget_ac1_4.verticalHeaderItem(7)
        ___qtablewidgetitem250.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem251 = self.tableWidget_ac1_4.verticalHeaderItem(8)
        ___qtablewidgetitem251.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_22.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111\u1ed9 \u1ea9m", None))
        ___qtablewidgetitem252 = self.tableWidget_doam_5.horizontalHeaderItem(0)
        ___qtablewidgetitem252.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem253 = self.tableWidget_doam_5.horizontalHeaderItem(1)
        ___qtablewidgetitem253.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem254 = self.tableWidget_doam_5.horizontalHeaderItem(2)
        ___qtablewidgetitem254.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem255 = self.tableWidget_doam_5.verticalHeaderItem(0)
        ___qtablewidgetitem255.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem256 = self.tableWidget_doam_5.verticalHeaderItem(1)
        ___qtablewidgetitem256.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem257 = self.tableWidget_doam_5.verticalHeaderItem(2)
        ___qtablewidgetitem257.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem258 = self.tableWidget_doam_5.verticalHeaderItem(3)
        ___qtablewidgetitem258.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem259 = self.tableWidget_doam_5.verticalHeaderItem(4)
        ___qtablewidgetitem259.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem260 = self.tableWidget_doam_5.verticalHeaderItem(5)
        ___qtablewidgetitem260.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem261 = self.tableWidget_doam_5.verticalHeaderItem(6)
        ___qtablewidgetitem261.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem262 = self.tableWidget_doam_5.verticalHeaderItem(7)
        ___qtablewidgetitem262.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem263 = self.tableWidget_doam_5.verticalHeaderItem(8)
        ___qtablewidgetitem263.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_23.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC2", None))
        ___qtablewidgetitem264 = self.tableWidget_dc2_5.horizontalHeaderItem(0)
        ___qtablewidgetitem264.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem265 = self.tableWidget_dc2_5.horizontalHeaderItem(1)
        ___qtablewidgetitem265.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem266 = self.tableWidget_dc2_5.horizontalHeaderItem(2)
        ___qtablewidgetitem266.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem267 = self.tableWidget_dc2_5.verticalHeaderItem(0)
        ___qtablewidgetitem267.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem268 = self.tableWidget_dc2_5.verticalHeaderItem(1)
        ___qtablewidgetitem268.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem269 = self.tableWidget_dc2_5.verticalHeaderItem(2)
        ___qtablewidgetitem269.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem270 = self.tableWidget_dc2_5.verticalHeaderItem(3)
        ___qtablewidgetitem270.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem271 = self.tableWidget_dc2_5.verticalHeaderItem(4)
        ___qtablewidgetitem271.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem272 = self.tableWidget_dc2_5.verticalHeaderItem(5)
        ___qtablewidgetitem272.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem273 = self.tableWidget_dc2_5.verticalHeaderItem(6)
        ___qtablewidgetitem273.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem274 = self.tableWidget_dc2_5.verticalHeaderItem(7)
        ___qtablewidgetitem274.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem275 = self.tableWidget_dc2_5.verticalHeaderItem(8)
        ___qtablewidgetitem275.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_24.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC2", None))
        ___qtablewidgetitem276 = self.tableWidget_ac2_4.horizontalHeaderItem(0)
        ___qtablewidgetitem276.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem277 = self.tableWidget_ac2_4.horizontalHeaderItem(1)
        ___qtablewidgetitem277.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem278 = self.tableWidget_ac2_4.horizontalHeaderItem(2)
        ___qtablewidgetitem278.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem279 = self.tableWidget_ac2_4.verticalHeaderItem(0)
        ___qtablewidgetitem279.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem280 = self.tableWidget_ac2_4.verticalHeaderItem(1)
        ___qtablewidgetitem280.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem281 = self.tableWidget_ac2_4.verticalHeaderItem(2)
        ___qtablewidgetitem281.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem282 = self.tableWidget_ac2_4.verticalHeaderItem(3)
        ___qtablewidgetitem282.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem283 = self.tableWidget_ac2_4.verticalHeaderItem(4)
        ___qtablewidgetitem283.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem284 = self.tableWidget_ac2_4.verticalHeaderItem(5)
        ___qtablewidgetitem284.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem285 = self.tableWidget_ac2_4.verticalHeaderItem(6)
        ___qtablewidgetitem285.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem286 = self.tableWidget_ac2_4.verticalHeaderItem(7)
        ___qtablewidgetitem286.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem287 = self.tableWidget_ac2_4.verticalHeaderItem(8)
        ___qtablewidgetitem287.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_25.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.title_nhietdo_5.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 nhi\u1ec7t \u0111\u1ed9", None))
        self.thoigian_nhietdo_5.setText("")
        self.label_diepap_4.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0110i\u1ec7n \u00e1p", None))
        self.label_thoigian_dienap_4.setText("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 nhi\u1ec7t \u0111\u1ed9", None))
        ___qtablewidgetitem288 = self.tableWidget_nhietdo_6.horizontalHeaderItem(0)
        ___qtablewidgetitem288.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem289 = self.tableWidget_nhietdo_6.horizontalHeaderItem(1)
        ___qtablewidgetitem289.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem290 = self.tableWidget_nhietdo_6.horizontalHeaderItem(2)
        ___qtablewidgetitem290.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem291 = self.tableWidget_nhietdo_6.verticalHeaderItem(0)
        ___qtablewidgetitem291.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem292 = self.tableWidget_nhietdo_6.verticalHeaderItem(1)
        ___qtablewidgetitem292.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem293 = self.tableWidget_nhietdo_6.verticalHeaderItem(2)
        ___qtablewidgetitem293.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem294 = self.tableWidget_nhietdo_6.verticalHeaderItem(3)
        ___qtablewidgetitem294.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem295 = self.tableWidget_nhietdo_6.verticalHeaderItem(4)
        ___qtablewidgetitem295.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem296 = self.tableWidget_nhietdo_6.verticalHeaderItem(5)
        ___qtablewidgetitem296.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem297 = self.tableWidget_nhietdo_6.verticalHeaderItem(6)
        ___qtablewidgetitem297.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem298 = self.tableWidget_nhietdo_6.verticalHeaderItem(7)
        ___qtablewidgetitem298.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem299 = self.tableWidget_nhietdo_6.verticalHeaderItem(8)
        ___qtablewidgetitem299.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_26.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC1", None))
        ___qtablewidgetitem300 = self.tableWidget_dc1_6.horizontalHeaderItem(0)
        ___qtablewidgetitem300.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem301 = self.tableWidget_dc1_6.horizontalHeaderItem(1)
        ___qtablewidgetitem301.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem302 = self.tableWidget_dc1_6.horizontalHeaderItem(2)
        ___qtablewidgetitem302.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem303 = self.tableWidget_dc1_6.verticalHeaderItem(0)
        ___qtablewidgetitem303.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem304 = self.tableWidget_dc1_6.verticalHeaderItem(1)
        ___qtablewidgetitem304.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem305 = self.tableWidget_dc1_6.verticalHeaderItem(2)
        ___qtablewidgetitem305.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem306 = self.tableWidget_dc1_6.verticalHeaderItem(3)
        ___qtablewidgetitem306.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem307 = self.tableWidget_dc1_6.verticalHeaderItem(4)
        ___qtablewidgetitem307.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem308 = self.tableWidget_dc1_6.verticalHeaderItem(5)
        ___qtablewidgetitem308.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem309 = self.tableWidget_dc1_6.verticalHeaderItem(6)
        ___qtablewidgetitem309.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem310 = self.tableWidget_dc1_6.verticalHeaderItem(7)
        ___qtablewidgetitem310.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem311 = self.tableWidget_dc1_6.verticalHeaderItem(8)
        ___qtablewidgetitem311.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_27.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC1", None))
        ___qtablewidgetitem312 = self.tableWidget_ac1_5.horizontalHeaderItem(0)
        ___qtablewidgetitem312.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem313 = self.tableWidget_ac1_5.horizontalHeaderItem(1)
        ___qtablewidgetitem313.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem314 = self.tableWidget_ac1_5.horizontalHeaderItem(2)
        ___qtablewidgetitem314.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem315 = self.tableWidget_ac1_5.verticalHeaderItem(0)
        ___qtablewidgetitem315.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem316 = self.tableWidget_ac1_5.verticalHeaderItem(1)
        ___qtablewidgetitem316.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem317 = self.tableWidget_ac1_5.verticalHeaderItem(2)
        ___qtablewidgetitem317.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem318 = self.tableWidget_ac1_5.verticalHeaderItem(3)
        ___qtablewidgetitem318.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem319 = self.tableWidget_ac1_5.verticalHeaderItem(4)
        ___qtablewidgetitem319.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem320 = self.tableWidget_ac1_5.verticalHeaderItem(5)
        ___qtablewidgetitem320.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem321 = self.tableWidget_ac1_5.verticalHeaderItem(6)
        ___qtablewidgetitem321.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem322 = self.tableWidget_ac1_5.verticalHeaderItem(7)
        ___qtablewidgetitem322.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem323 = self.tableWidget_ac1_5.verticalHeaderItem(8)
        ___qtablewidgetitem323.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_28.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111\u1ed9 \u1ea9m", None))
        ___qtablewidgetitem324 = self.tableWidget_doam_6.horizontalHeaderItem(0)
        ___qtablewidgetitem324.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem325 = self.tableWidget_doam_6.horizontalHeaderItem(1)
        ___qtablewidgetitem325.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem326 = self.tableWidget_doam_6.horizontalHeaderItem(2)
        ___qtablewidgetitem326.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem327 = self.tableWidget_doam_6.verticalHeaderItem(0)
        ___qtablewidgetitem327.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem328 = self.tableWidget_doam_6.verticalHeaderItem(1)
        ___qtablewidgetitem328.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem329 = self.tableWidget_doam_6.verticalHeaderItem(2)
        ___qtablewidgetitem329.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem330 = self.tableWidget_doam_6.verticalHeaderItem(3)
        ___qtablewidgetitem330.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem331 = self.tableWidget_doam_6.verticalHeaderItem(4)
        ___qtablewidgetitem331.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem332 = self.tableWidget_doam_6.verticalHeaderItem(5)
        ___qtablewidgetitem332.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem333 = self.tableWidget_doam_6.verticalHeaderItem(6)
        ___qtablewidgetitem333.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem334 = self.tableWidget_doam_6.verticalHeaderItem(7)
        ___qtablewidgetitem334.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem335 = self.tableWidget_doam_6.verticalHeaderItem(8)
        ___qtablewidgetitem335.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_29.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC2", None))
        ___qtablewidgetitem336 = self.tableWidget_dc2_6.horizontalHeaderItem(0)
        ___qtablewidgetitem336.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem337 = self.tableWidget_dc2_6.horizontalHeaderItem(1)
        ___qtablewidgetitem337.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem338 = self.tableWidget_dc2_6.horizontalHeaderItem(2)
        ___qtablewidgetitem338.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem339 = self.tableWidget_dc2_6.verticalHeaderItem(0)
        ___qtablewidgetitem339.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem340 = self.tableWidget_dc2_6.verticalHeaderItem(1)
        ___qtablewidgetitem340.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem341 = self.tableWidget_dc2_6.verticalHeaderItem(2)
        ___qtablewidgetitem341.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem342 = self.tableWidget_dc2_6.verticalHeaderItem(3)
        ___qtablewidgetitem342.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem343 = self.tableWidget_dc2_6.verticalHeaderItem(4)
        ___qtablewidgetitem343.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem344 = self.tableWidget_dc2_6.verticalHeaderItem(5)
        ___qtablewidgetitem344.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem345 = self.tableWidget_dc2_6.verticalHeaderItem(6)
        ___qtablewidgetitem345.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem346 = self.tableWidget_dc2_6.verticalHeaderItem(7)
        ___qtablewidgetitem346.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem347 = self.tableWidget_dc2_6.verticalHeaderItem(8)
        ___qtablewidgetitem347.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_30.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC2", None))
        ___qtablewidgetitem348 = self.tableWidget_ac2_5.horizontalHeaderItem(0)
        ___qtablewidgetitem348.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem349 = self.tableWidget_ac2_5.horizontalHeaderItem(1)
        ___qtablewidgetitem349.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem350 = self.tableWidget_ac2_5.horizontalHeaderItem(2)
        ___qtablewidgetitem350.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem351 = self.tableWidget_ac2_5.verticalHeaderItem(0)
        ___qtablewidgetitem351.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem352 = self.tableWidget_ac2_5.verticalHeaderItem(1)
        ___qtablewidgetitem352.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem353 = self.tableWidget_ac2_5.verticalHeaderItem(2)
        ___qtablewidgetitem353.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem354 = self.tableWidget_ac2_5.verticalHeaderItem(3)
        ___qtablewidgetitem354.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem355 = self.tableWidget_ac2_5.verticalHeaderItem(4)
        ___qtablewidgetitem355.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem356 = self.tableWidget_ac2_5.verticalHeaderItem(5)
        ___qtablewidgetitem356.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem357 = self.tableWidget_ac2_5.verticalHeaderItem(6)
        ___qtablewidgetitem357.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem358 = self.tableWidget_ac2_5.verticalHeaderItem(7)
        ___qtablewidgetitem358.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem359 = self.tableWidget_ac2_5.verticalHeaderItem(8)
        ___qtablewidgetitem359.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_31.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.title_nhietdo_11.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 nhi\u1ec7t \u0111\u1ed9", None))
        self.thoigian_nhietdo_11.setText("")
        self.label_diepap_5.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0110i\u1ec7n \u00e1p", None))
        self.label_thoigian_dienap_5.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 nhi\u1ec7t \u0111\u1ed9", None))
        ___qtablewidgetitem360 = self.tableWidget_nhietdo_7.horizontalHeaderItem(0)
        ___qtablewidgetitem360.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem361 = self.tableWidget_nhietdo_7.horizontalHeaderItem(1)
        ___qtablewidgetitem361.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem362 = self.tableWidget_nhietdo_7.horizontalHeaderItem(2)
        ___qtablewidgetitem362.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem363 = self.tableWidget_nhietdo_7.verticalHeaderItem(0)
        ___qtablewidgetitem363.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem364 = self.tableWidget_nhietdo_7.verticalHeaderItem(1)
        ___qtablewidgetitem364.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem365 = self.tableWidget_nhietdo_7.verticalHeaderItem(2)
        ___qtablewidgetitem365.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem366 = self.tableWidget_nhietdo_7.verticalHeaderItem(3)
        ___qtablewidgetitem366.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem367 = self.tableWidget_nhietdo_7.verticalHeaderItem(4)
        ___qtablewidgetitem367.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem368 = self.tableWidget_nhietdo_7.verticalHeaderItem(5)
        ___qtablewidgetitem368.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem369 = self.tableWidget_nhietdo_7.verticalHeaderItem(6)
        ___qtablewidgetitem369.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem370 = self.tableWidget_nhietdo_7.verticalHeaderItem(7)
        ___qtablewidgetitem370.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem371 = self.tableWidget_nhietdo_7.verticalHeaderItem(8)
        ___qtablewidgetitem371.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_32.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC1", None))
        ___qtablewidgetitem372 = self.tableWidget_dc1_7.horizontalHeaderItem(0)
        ___qtablewidgetitem372.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem373 = self.tableWidget_dc1_7.horizontalHeaderItem(1)
        ___qtablewidgetitem373.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem374 = self.tableWidget_dc1_7.horizontalHeaderItem(2)
        ___qtablewidgetitem374.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem375 = self.tableWidget_dc1_7.verticalHeaderItem(0)
        ___qtablewidgetitem375.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem376 = self.tableWidget_dc1_7.verticalHeaderItem(1)
        ___qtablewidgetitem376.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem377 = self.tableWidget_dc1_7.verticalHeaderItem(2)
        ___qtablewidgetitem377.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem378 = self.tableWidget_dc1_7.verticalHeaderItem(3)
        ___qtablewidgetitem378.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem379 = self.tableWidget_dc1_7.verticalHeaderItem(4)
        ___qtablewidgetitem379.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem380 = self.tableWidget_dc1_7.verticalHeaderItem(5)
        ___qtablewidgetitem380.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem381 = self.tableWidget_dc1_7.verticalHeaderItem(6)
        ___qtablewidgetitem381.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem382 = self.tableWidget_dc1_7.verticalHeaderItem(7)
        ___qtablewidgetitem382.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem383 = self.tableWidget_dc1_7.verticalHeaderItem(8)
        ___qtablewidgetitem383.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_33.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC1", None))
        ___qtablewidgetitem384 = self.tableWidget_ac1_6.horizontalHeaderItem(0)
        ___qtablewidgetitem384.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem385 = self.tableWidget_ac1_6.horizontalHeaderItem(1)
        ___qtablewidgetitem385.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem386 = self.tableWidget_ac1_6.horizontalHeaderItem(2)
        ___qtablewidgetitem386.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem387 = self.tableWidget_ac1_6.verticalHeaderItem(0)
        ___qtablewidgetitem387.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem388 = self.tableWidget_ac1_6.verticalHeaderItem(1)
        ___qtablewidgetitem388.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem389 = self.tableWidget_ac1_6.verticalHeaderItem(2)
        ___qtablewidgetitem389.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem390 = self.tableWidget_ac1_6.verticalHeaderItem(3)
        ___qtablewidgetitem390.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem391 = self.tableWidget_ac1_6.verticalHeaderItem(4)
        ___qtablewidgetitem391.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem392 = self.tableWidget_ac1_6.verticalHeaderItem(5)
        ___qtablewidgetitem392.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem393 = self.tableWidget_ac1_6.verticalHeaderItem(6)
        ___qtablewidgetitem393.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem394 = self.tableWidget_ac1_6.verticalHeaderItem(7)
        ___qtablewidgetitem394.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem395 = self.tableWidget_ac1_6.verticalHeaderItem(8)
        ___qtablewidgetitem395.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_34.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111\u1ed9 \u1ea9m", None))
        ___qtablewidgetitem396 = self.tableWidget_doam_7.horizontalHeaderItem(0)
        ___qtablewidgetitem396.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem397 = self.tableWidget_doam_7.horizontalHeaderItem(1)
        ___qtablewidgetitem397.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem398 = self.tableWidget_doam_7.horizontalHeaderItem(2)
        ___qtablewidgetitem398.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem399 = self.tableWidget_doam_7.verticalHeaderItem(0)
        ___qtablewidgetitem399.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem400 = self.tableWidget_doam_7.verticalHeaderItem(1)
        ___qtablewidgetitem400.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem401 = self.tableWidget_doam_7.verticalHeaderItem(2)
        ___qtablewidgetitem401.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem402 = self.tableWidget_doam_7.verticalHeaderItem(3)
        ___qtablewidgetitem402.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem403 = self.tableWidget_doam_7.verticalHeaderItem(4)
        ___qtablewidgetitem403.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem404 = self.tableWidget_doam_7.verticalHeaderItem(5)
        ___qtablewidgetitem404.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem405 = self.tableWidget_doam_7.verticalHeaderItem(6)
        ___qtablewidgetitem405.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem406 = self.tableWidget_doam_7.verticalHeaderItem(7)
        ___qtablewidgetitem406.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem407 = self.tableWidget_doam_7.verticalHeaderItem(8)
        ___qtablewidgetitem407.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_35.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p DC2", None))
        ___qtablewidgetitem408 = self.tableWidget_dc2_7.horizontalHeaderItem(0)
        ___qtablewidgetitem408.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem409 = self.tableWidget_dc2_7.horizontalHeaderItem(1)
        ___qtablewidgetitem409.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem410 = self.tableWidget_dc2_7.horizontalHeaderItem(2)
        ___qtablewidgetitem410.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem411 = self.tableWidget_dc2_7.verticalHeaderItem(0)
        ___qtablewidgetitem411.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem412 = self.tableWidget_dc2_7.verticalHeaderItem(1)
        ___qtablewidgetitem412.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem413 = self.tableWidget_dc2_7.verticalHeaderItem(2)
        ___qtablewidgetitem413.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem414 = self.tableWidget_dc2_7.verticalHeaderItem(3)
        ___qtablewidgetitem414.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem415 = self.tableWidget_dc2_7.verticalHeaderItem(4)
        ___qtablewidgetitem415.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem416 = self.tableWidget_dc2_7.verticalHeaderItem(5)
        ___qtablewidgetitem416.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem417 = self.tableWidget_dc2_7.verticalHeaderItem(6)
        ___qtablewidgetitem417.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem418 = self.tableWidget_dc2_7.verticalHeaderItem(7)
        ___qtablewidgetitem418.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem419 = self.tableWidget_dc2_7.verticalHeaderItem(8)
        ___qtablewidgetitem419.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_36.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"S\u1ef1 c\u1ed1 v\u1ec1 \u0111i\u1ec7n \u00e1p AC2", None))
        ___qtablewidgetitem420 = self.tableWidget_ac2_6.horizontalHeaderItem(0)
        ___qtablewidgetitem420.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ef1 c\u1ed1", None));
        ___qtablewidgetitem421 = self.tableWidget_ac2_6.horizontalHeaderItem(1)
        ___qtablewidgetitem421.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None));
        ___qtablewidgetitem422 = self.tableWidget_ac2_6.horizontalHeaderItem(2)
        ___qtablewidgetitem422.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian k\u1ebft th\u00fac", None));
        ___qtablewidgetitem423 = self.tableWidget_ac2_6.verticalHeaderItem(0)
        ___qtablewidgetitem423.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem424 = self.tableWidget_ac2_6.verticalHeaderItem(1)
        ___qtablewidgetitem424.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem425 = self.tableWidget_ac2_6.verticalHeaderItem(2)
        ___qtablewidgetitem425.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem426 = self.tableWidget_ac2_6.verticalHeaderItem(3)
        ___qtablewidgetitem426.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem427 = self.tableWidget_ac2_6.verticalHeaderItem(4)
        ___qtablewidgetitem427.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem428 = self.tableWidget_ac2_6.verticalHeaderItem(5)
        ___qtablewidgetitem428.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem429 = self.tableWidget_ac2_6.verticalHeaderItem(6)
        ___qtablewidgetitem429.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem430 = self.tableWidget_ac2_6.verticalHeaderItem(7)
        ___qtablewidgetitem430.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem431 = self.tableWidget_ac2_6.verticalHeaderItem(8)
        ___qtablewidgetitem431.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.pushButton_exportTem_37.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.label_doam_5.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0111\u1ed9 \u1ea9m", None))
        self.label_thoigian_doam_3.setText("")
        self.label_doam_6.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0111\u1ed9 \u1ea9m", None))
        self.label_thoigian_doam_4.setText("")
        self.title_nhietdo_4.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 nhi\u1ec7t \u0111\u1ed9", None))
        self.thoigian_nhietdo_4.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"H\u01af\u1edaNG D\u1eaaN S\u1eec D\u1ee4NG", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Ng\u01b0\u1eddi d\u00f9ng \u1ea5n v\u00e0o \u1ee9ng d\u1ee5ng Qu\u1ea3n l\u00fd  tr\u00ean m\u00e0n h\u00ecnh v\u00e0 \u0111\u0103ng nh\u1eadp b\u1eb1ng t\u00e0i kho\u1ea3n c\u00f3 s\u1eb5n.", None))
        self.label_62.setText("")
        self.label_64.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Giao di\u1ec7n ph\u1ea7n m\u1ec1m g\u1ed3m c\u00f3 thanh menu \u1edf b\u00ean tr\u00e1i, hi\u1ec3n th\u1ecb th\u1eddi gian v\u00e0  tr\u1ea1ng th\u00e1i c\u00e1c tham s\u1ed1 c\u1ee7a c\u00e1c tr\u1ea1m th\u00f4ng tin.\n"
"-Nhi\u1ec7t \u0111\u1ed9: gi\u00e1 tr\u1ecb nhi\u1ec7t \u0111\u1ed9 \u0111o \u0111\u01b0\u1ee3c t\u1eeb tr\u1ea1m th\u00f4ng tin.\n"
"-\u0110\u1ed9 \u1ea9m: gi\u00e1 tr\u1ecb \u0111\u1ed9 \u1ea9m \u0111o \u0111\u01b0\u1ee3c t\u1eeb tr\u1ea1m th\u00f4ng tin.\n"
"-\u00c1nh s\u00e1ng: tr\u1ea1ng th\u00e1i B\u1eadt/t\u1eaft c\u1ee7a \u00e1nh s\u00e1ng.\n"
"-	B\u00e1o ch\u00e1y: tr\u1ea1ng th\u00e1i C\u00f3/Kh\u00f4ng.\n"
"-Ngu\u1ed3n DC1: gi\u00e1 tr\u1ecb \u0111i\u1ec7n \u00e1p DC \u0111o \u0111\u01b0\u1ee3c t\u1eeb b\u1ed9 ngu\u1ed3n P4-01 CT th\u1ee9 nh\u1ea5t c\u1ee7a tr\u1ea1m th\u00f4ng tin.\n"
"-Ngu\u1ed3n DC2: gi\u00e1 tr\u1ecb \u0111i\u1ec7n \u00e1p DC \u0111o \u0111\u01b0\u1ee3c t\u1eeb b\u1ed9 ngu\u1ed3n P4-01 CT th\u1ee9 hai c\u1ee7a tr\u1ea1m th\u00f4ng tin.\n"
"-Ngu\u1ed3n AC1: tr\u1ea1"
                        "ng th\u00e1i c\u00f3/m\u1ea5t ngu\u1ed3n AC \u0111i\u1ec7n l\u01b0\u1edbi.\n"
"-Ngu\u1ed3n AC2: tr\u1ea1ng th\u00e1i c\u00f3/m\u1ea5t ngu\u1ed3n AC \u1edf \u0111\u1ea7u ra c\u1ee7a b\u1ed9 Inverter.\n"
"", None))
        self.label_68.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i c\u1ee7a c\u00e1c tham s\u1ed1: \n"
"-M\u00e0u xanh: T\u1ed1t \n"
"-M\u00e0u v\u00e0ng: C\u1ea3nh b\u00e1o m\u1ee9c 1\n"
"-M\u00e0u \u0111\u1ecf: C\u1ea3nh b\u00e1o m\u1ee9c 2.\n"
"Khi kh\u00f4ng x\u1ea3y ra s\u1ef1 c\u1ed1 hay c\u1ea3nh b\u00e1o g\u00ec th\u00ec tr\u1ea1ng th\u00e1i c\u1ee7a c\u00e1c tham s\u1ed1 hi\u1ec3n th\u1ecb s\u1ebd c\u00f3 m\u00e0u xanh. Ng\u01b0\u1ee3c l\u1ea1i khi c\u00f3 c\u1ea3nh b\u00e1o th\u00ec c\u00e1c tr\u1ea1ng th\u00e1i n\u00e0y s\u1ebd chuy\u1ec3n t\u1eeb m\u00e0u xanh sang m\u00e0u v\u00e0ng ho\u1eb7c \u0111\u1ecf.\n"
"\u0110\u1ec3 bi\u1ebft th\u00eam th\u00f4ng tin v\u1ec1 tham s\u1ed1 c\u00e1c tr\u1ea1m, ng\u01b0\u1eddi d\u00f9ng click v\u00e0o L\u1eef \u0111o\u00e0n hi\u1ec3n th\u1ecb \u1edf thanh menu -> t\u00ean tr\u1ea1m -> tham s\u1ed1 c\u1ea7n theo d\u00f5i,", None))
        self.label_66.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Mu\u1ed1n bi\u1ebft th\u00f4ng tin v\u1ec1 nhi\u1ec7t \u0111\u1ed9 c\u1ee7a tr\u1ea1m A70 / L\u1eef 139, ng\u01b0\u1eddi d\u00f9ng click v\u00e0o L\u1eef \u0111o\u00e0n 139 -> Tr\u1ea1m A70 -> Bi\u1ec3u \u0111\u1ed3 nhi\u1ec7t \u0111\u1ed9.\n"
"Th\u00f4ng tin v\u1ec1 gi\u00e1 tr\u1ecb tham s\u1ed1 nhi\u1ec7t \u0111\u1ed9 qua th\u1eddi gian s\u1ebd \u0111\u01b0\u1ee3c hi\u1ec7n th\u1ecb tr\u00ean m\u00e0n h\u00ecnh d\u01b0\u1edbi d\u1ea1ng bi\u1ec3u \u0111\u1ed3, bao g\u1ed3m c\u00e1c ng\u01b0\u1ee1ng cho ph\u00e9p v\u00e0 s\u1ebd b\u00e1o hi\u1ec7u khi v\u01b0\u1ee3t qu\u00e1 ng\u01b0\u1ee1ng cho ph\u00e9p. C\u00e1c \u0111i\u1ec3m n\u1eb1m ngo\u00e0i kho\u1ea3ng ho\u1ea1t \u0111\u1ed9ng tin c\u1eady s\u1ebd c\u00f3 m\u00e0u \u0111\u1ecf, c\u00e1c \u0111i\u1ec3m n\u1eb1m trong kho\u1ea3ng ho\u1ea1t \u0111\u1ed9ng tin c\u1eady s\u1ebd c\u00f3 m\u00e0u xanh.\n"
"", None))
        self.label_72.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ec3  bi\u1ebft th\u00eam th\u00f4ng tin v\u1ec1 s\u1ef1 c\u1ed1 c\u1ee7a c\u00e1c tr\u1ea1m, ng\u01b0\u1eddi d\u00f9ng click v\u00e0o L\u1eef \u0111o\u00e0n hi\u1ec3n th\u1ecb \u1edf thanh menu -> t\u00ean tr\u1ea1m -> s\u1ef1 c\u1ed1. M\u00e0n h\u00ecnh s\u1ebd hi\u1ec3n th\u1ecb c\u1eeda s\u1ed5 ch\u1ecdn ng\u00e0y xem s\u1ef1 s\u1ed1, ng\u01b0\u1eddi d\u00f9ng c\u00f3 th\u1ec3 ch\u1ecdn xem s\u1ef1 c\u1ed1 trong kho\u1ea3ng th\u1eddi gian b\u1ea5t k\u00ec. Ph\u1ea7n m\u1ec1m \u0111\u01b0\u1ee3c thi\u1ebft k\u1ebf \u0111\u1ec3 th\u1ed1ng k\u00ea 6 b\u1ea3ng s\u1ef1 c\u1ed1, bao g\u1ed3m s\u1ef1 c\u1ed1 nhi\u1ec7t \u0111\u1ed9, s\u1ef1 c\u1ed1 \u0111\u1ed9 \u1ea9m, s\u1ef1 c\u1ed1 ngu\u1ed3n AC1, s\u1ef1 c\u1ed1 ngu\u1ed3n AC2, s\u1ef1 c\u1ed1 ngu\u1ed3n DC1, s\u1ef1 c\u1ed1 ngu\u1ed3n DC2. N\u1ed9i dung trong c\u00e1c b\u1ea3ng s\u1ef1 c\u1ed1 l\u00e0 t\u00ean s\u1ef1 c\u1ed1, th\u1eddi gian x\u1ea3y ra s\u1ef1 c\u1ed1 v\u00e0 th\u1eddi gian k\u1ebft th\u00fac s\u1ef1 c\u1ed1.Ph\u1ea7n m\u1ec1m c\u00f3"
                        " kh\u1ea3 n\u0103ng xu\u1ea5t c\u00e1c b\u1ea3ng s\u1ef1 c\u1ed1 th\u00e0nh file Excel \u0111\u1ec3 thu\u1eadn ti\u1ec7n cho ng\u01b0\u1eddi d\u00f9ng trong c\u00f4ng t\u00e1c th\u1ed1ng k\u00ea, theo d\u00f5i.\n"
" \u0110\u1ec3 xu\u1ea5t d\u1eef li\u1ec7u s\u1ef1 s\u1ed1 c\u1ee7a m\u1ed9t b\u1ea3ng s\u1ef1 c\u1ed1 sang file Excel, ng\u01b0\u1eddi d\u00f9ng th\u1ef1c hi\u1ec7n c\u00e1c b\u01b0\u1edbc sau:\n"
" B\u01b0\u1edbc 1: Ng\u01b0\u1eddi d\u00f9ng click v\u00e0o \u00f4 xu\u1ea5t d\u1eef li\u1ec7u c\u1ee7a m\u1ed9t tham s\u1ed1.\n"
" B\u01b0\u1edbc 2: Ch\u1ecdn v\u1ecb tr\u00ed mu\u1ed1n l\u01b0u d\u1eef li\u1ec7u, \u0111\u1eb7t t\u00ean file, ch\u1ecdn ki\u1ec3u file Excel ->  ch\u1ecdn Save.\n"
"", None))
        self.label_70.setText("")
        self.label_71.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"H\u1ec6 TH\u1ed0NG GI\u00c1M S\u00c1T, C\u1ea2NH B\u00c1O T\u1eea XA CHO C\u00c1C TR\u1ea0M V\u00c0 KHO TH\u00d4NG TIN", None))
        self.label_17.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A70", None))
        self.pushButton_anhsang_15.setText("")
        self.label_24.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A45", None))
        self.pushButton_anhsang_16.setText("")
        self.label_40.setText("")
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A01", None))
        self.pushButton_anhsang_17.setText("")
        self.label_92.setText("")
        self.pushButton_ac1_9.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u" AC1", None))
        self.pushButton_ac2_9.setText("")
        self.label_94.setText(QCoreApplication.translate("MainWindow", u" AC2", None))
        self.pushButton_12.setText("")
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"T\u1ed0T", None))
        self.pushButton_13.setText("")
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"C\u1ea3nh b\u00e1o m\u1ee9c 1", None))
        self.pushButton_14.setText("")
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"C\u1ea3nh b\u00e1o m\u1ee9c 2", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A48", None))
        self.pushButton_anhsang_18.setText("")
        self.label_99.setText("")
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A71", None))
        self.pushButton_anhsang_19.setText("")
        self.label_103.setText("")
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A76", None))
        self.pushButton_anhsang_20.setText("")
        self.label_107.setText("")
        self.pushButton_134.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00d3NG \u1ee8NG D\u1ee4NG", None))
        self.pushButton_HDSD.setText(QCoreApplication.translate("MainWindow", u"H\u01af\u1edaNG D\u1eaaN SD", None))
        self.pushButton_135.setText(QCoreApplication.translate("MainWindow", u"T\u1eaeT C\u1ea2NH B\u00c1O", None))
    # retranslateUi

