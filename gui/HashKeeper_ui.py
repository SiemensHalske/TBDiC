# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HashKeeper.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionOpen_config_file = QAction(MainWindow)
        self.actionOpen_config_file.setObjectName(u"actionOpen_config_file")
        self.actionExport_config_file = QAction(MainWindow)
        self.actionExport_config_file.setObjectName(u"actionExport_config_file")
        self.actionSetup_HashKeeper = QAction(MainWindow)
        self.actionSetup_HashKeeper.setObjectName(u"actionSetup_HashKeeper")
        self.actionOpen_Preferences = QAction(MainWindow)
        self.actionOpen_Preferences.setObjectName(u"actionOpen_Preferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 651, 541))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView_selectDirectories = QListView(self.verticalLayoutWidget)
        self.listView_selectDirectories.setObjectName(u"listView_selectDirectories")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_selectDirectories.sizePolicy().hasHeightForWidth())
        self.listView_selectDirectories.setSizePolicy(sizePolicy)
        self.listView_selectDirectories.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout.addWidget(self.listView_selectDirectories)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_13 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setAutoFillBackground(True)

        self.gridLayout_3.addWidget(self.checkBox_13, 3, 1, 1, 1)

        self.checkBox_hashOnlyFiles = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_hashOnlyFiles.setObjectName(u"checkBox_hashOnlyFiles")
        self.checkBox_hashOnlyFiles.setAutoFillBackground(True)

        self.gridLayout_3.addWidget(self.checkBox_hashOnlyFiles, 2, 1, 1, 1)

        self.checkBox_hashDirectoriesOnly = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_hashDirectoriesOnly.setObjectName(u"checkBox_hashDirectoriesOnly")
        self.checkBox_hashDirectoriesOnly.setAutoFillBackground(True)

        self.gridLayout_3.addWidget(self.checkBox_hashDirectoriesOnly, 2, 0, 1, 1)

        self.checkBox_onlyHashNewFiles = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_onlyHashNewFiles.setObjectName(u"checkBox_onlyHashNewFiles")
        self.checkBox_onlyHashNewFiles.setAutoFillBackground(True)

        self.gridLayout_3.addWidget(self.checkBox_onlyHashNewFiles, 3, 0, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox_2, 2, 1, 1, 1)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox, 2, 2, 1, 1)

        self.checkBox_9 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox_9, 4, 2, 1, 1)

        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox_7, 4, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox_4, 3, 2, 1, 1)

        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox_6, 3, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox_8, 4, 1, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)

        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox_5, 2, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.checkBox_3, 3, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.timeEdit = QTimeEdit(self.verticalLayoutWidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setLayoutDirection(Qt.LeftToRight)
        self.timeEdit.setAutoFillBackground(True)
        self.timeEdit.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)

        self.horizontalLayout_3.addWidget(self.timeEdit)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setAutoFillBackground(True)

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(669, 0, 601, 541))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser_displayResults = QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_displayResults.setObjectName(u"textBrowser_displayResults")

        self.gridLayout.addWidget(self.textBrowser_displayResults, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 550, 1261, 111))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.verticalLayoutWidget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAutoFillBackground(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.progressBar_remainingTimeHR = QProgressBar(self.verticalLayoutWidget_3)
        self.progressBar_remainingTimeHR.setObjectName(u"progressBar_remainingTimeHR")
        self.progressBar_remainingTimeHR.setAutoFillBackground(True)
        self.progressBar_remainingTimeHR.setValue(100)

        self.horizontalLayout_4.addWidget(self.progressBar_remainingTimeHR)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Exit = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_Exit.setObjectName(u"pushButton_Exit")
        self.pushButton_Exit.setAutoFillBackground(True)

        self.horizontalLayout.addWidget(self.pushButton_Exit)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setAutoFillBackground(True)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_remainingTimeHR = QLabel(self.verticalLayoutWidget_3)
        self.label_remainingTimeHR.setObjectName(u"label_remainingTimeHR")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_remainingTimeHR.sizePolicy().hasHeightForWidth())
        self.label_remainingTimeHR.setSizePolicy(sizePolicy2)
        self.label_remainingTimeHR.setAutoFillBackground(True)
        self.label_remainingTimeHR.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_remainingTimeHR)

        self.lcdNumber_remainingTimeHour = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_remainingTimeHour.setObjectName(u"lcdNumber_remainingTimeHour")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lcdNumber_remainingTimeHour.sizePolicy().hasHeightForWidth())
        self.lcdNumber_remainingTimeHour.setSizePolicy(sizePolicy3)
        self.lcdNumber_remainingTimeHour.setAutoFillBackground(True)
        self.lcdNumber_remainingTimeHour.setDigitCount(2)

        self.horizontalLayout.addWidget(self.lcdNumber_remainingTimeHour)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.lcdNumber_remainingTimeMinute = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_remainingTimeMinute.setObjectName(u"lcdNumber_remainingTimeMinute")
        sizePolicy3.setHeightForWidth(self.lcdNumber_remainingTimeMinute.sizePolicy().hasHeightForWidth())
        self.lcdNumber_remainingTimeMinute.setSizePolicy(sizePolicy3)
        self.lcdNumber_remainingTimeMinute.setAutoFillBackground(True)
        self.lcdNumber_remainingTimeMinute.setDigitCount(2)

        self.horizontalLayout.addWidget(self.lcdNumber_remainingTimeMinute)

        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.lcdNumber_remainingTimeSecond = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_remainingTimeSecond.setObjectName(u"lcdNumber_remainingTimeSecond")
        sizePolicy3.setHeightForWidth(self.lcdNumber_remainingTimeSecond.sizePolicy().hasHeightForWidth())
        self.lcdNumber_remainingTimeSecond.setSizePolicy(sizePolicy3)
        self.lcdNumber_remainingTimeSecond.setAutoFillBackground(True)
        self.lcdNumber_remainingTimeSecond.setDigitCount(2)

        self.horizontalLayout.addWidget(self.lcdNumber_remainingTimeSecond)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.line_3 = QFrame(self.verticalLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.line_4 = QFrame(self.verticalLayoutWidget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_remainingTimeHR_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_remainingTimeHR_2.setObjectName(u"label_remainingTimeHR_2")
        sizePolicy2.setHeightForWidth(self.label_remainingTimeHR_2.sizePolicy().hasHeightForWidth())
        self.label_remainingTimeHR_2.setSizePolicy(sizePolicy2)
        self.label_remainingTimeHR_2.setAutoFillBackground(True)
        self.label_remainingTimeHR_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_remainingTimeHR_2)

        self.lcdNumber_2 = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        sizePolicy3.setHeightForWidth(self.lcdNumber_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_2.setSizePolicy(sizePolicy3)
        self.lcdNumber_2.setAutoFillBackground(True)
        self.lcdNumber_2.setDigitCount(2)

        self.horizontalLayout.addWidget(self.lcdNumber_2)

        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setAutoFillBackground(True)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.lcdNumber_3 = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        sizePolicy3.setHeightForWidth(self.lcdNumber_3.sizePolicy().hasHeightForWidth())
        self.lcdNumber_3.setSizePolicy(sizePolicy3)
        self.lcdNumber_3.setAutoFillBackground(True)
        self.lcdNumber_3.setDigitCount(2)

        self.horizontalLayout.addWidget(self.lcdNumber_3)

        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setAutoFillBackground(True)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.lcdNumber = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy3.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy3)
        self.lcdNumber.setAutoFillBackground(True)
        self.lcdNumber.setDigitCount(2)

        self.horizontalLayout.addWidget(self.lcdNumber)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSetup = QMenu(self.menubar)
        self.menuSetup.setObjectName(u"menuSetup")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_config_file)
        self.menuFile.addAction(self.actionExport_config_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionHelp)
        self.menuSetup.addAction(self.actionSetup_HashKeeper)
        self.menuSetup.addAction(self.actionOpen_Preferences)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Open Github Repo", None))
        self.actionOpen_config_file.setText(QCoreApplication.translate("MainWindow", u"Open config file", None))
        self.actionExport_config_file.setText(QCoreApplication.translate("MainWindow", u"Export config file", None))
        self.actionSetup_HashKeeper.setText(QCoreApplication.translate("MainWindow", u"Setup HashKeeper", None))
        self.actionOpen_Preferences.setText(QCoreApplication.translate("MainWindow", u"Open Preferences", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Close application after finish", None))
        self.checkBox_hashOnlyFiles.setText(QCoreApplication.translate("MainWindow", u"Files only", None))
        self.checkBox_hashDirectoriesOnly.setText(QCoreApplication.translate("MainWindow", u"Directories only", None))
        self.checkBox_onlyHashNewFiles.setText(QCoreApplication.translate("MainWindow", u"Only hash new files", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hash round settings", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"SHA-1", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"SHA256", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Tiger", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"BLAKE2", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Whirlpool", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"SHA-3", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"RIPEMD-160", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hash algorithm options", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"MD5", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"SHA512", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Set daily time", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Start / Set", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"  Progress in current round:  ", None))
        self.pushButton_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_remainingTimeHR.setText(QCoreApplication.translate("MainWindow", u"Remaining time 'til next hashing round:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_remainingTimeHR_2.setText(QCoreApplication.translate("MainWindow", u"Current time:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSetup.setTitle(QCoreApplication.translate("MainWindow", u"Setup", None))
    # retranslateUi

