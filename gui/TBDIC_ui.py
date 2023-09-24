# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TBDIC.ui'
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
        self.actionOpen_Github_help_page = QAction(MainWindow)
        self.actionOpen_Github_help_page.setObjectName(u"actionOpen_Github_help_page")
        self.actionCheck_for_updates = QAction(MainWindow)
        self.actionCheck_for_updates.setObjectName(u"actionCheck_for_updates")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 580, 1261, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_Command = QLabel(self.horizontalLayoutWidget)
        self.label_Command.setObjectName(u"label_Command")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Command.sizePolicy().hasHeightForWidth())
        self.label_Command.setSizePolicy(sizePolicy)
        self.label_Command.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Command.setFont(font)
        self.label_Command.setAutoFillBackground(True)
        self.label_Command.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_Command)

        self.textEdit_commandInput = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_commandInput.setObjectName(u"textEdit_commandInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_commandInput.sizePolicy().hasHeightForWidth())
        self.textEdit_commandInput.setSizePolicy(sizePolicy1)
        self.textEdit_commandInput.setAutoFillBackground(True)

        self.horizontalLayout.addWidget(self.textEdit_commandInput)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(640, 0, 631, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView_diagramDisplay = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView_diagramDisplay.setObjectName(u"graphicsView_diagramDisplay")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.graphicsView_diagramDisplay.setFont(font1)
        self.graphicsView_diagramDisplay.setAutoFillBackground(True)
        self.graphicsView_diagramDisplay.setInteractive(False)

        self.verticalLayout.addWidget(self.graphicsView_diagramDisplay)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 611, 581))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_symbolTree = QTreeWidget(self.verticalLayoutWidget_2)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget_symbolTree)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget_symbolTree)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        self.treeWidget_symbolTree.setObjectName(u"treeWidget_symbolTree")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeWidget_symbolTree.sizePolicy().hasHeightForWidth())
        self.treeWidget_symbolTree.setSizePolicy(sizePolicy2)
        self.treeWidget_symbolTree.setAutoFillBackground(True)

        self.verticalLayout_2.addWidget(self.treeWidget_symbolTree)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_8 = QFrame(self.verticalLayoutWidget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 4, 2, 1, 1)

        self.checkBox_quickSetting3 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting3.setObjectName(u"checkBox_quickSetting3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting3.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting3.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting3.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting3, 1, 4, 1, 1)

        self.line_9 = QFrame(self.verticalLayoutWidget_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 4, 4, 1, 1)

        self.checkBox_quickSetting5 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting5.setObjectName(u"checkBox_quickSetting5")
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting5.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting5.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting5.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting5, 3, 2, 1, 1)

        self.checkBox_quickSetting2 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting2.setObjectName(u"checkBox_quickSetting2")
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting2.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting2.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting2.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting2, 1, 2, 1, 1)

        self.checkBox_quickSetting1 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting1.setObjectName(u"checkBox_quickSetting1")
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting1.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting1.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting1.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting1, 1, 0, 1, 1)

        self.line = QFrame(self.verticalLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 5, 1)

        self.line_7 = QFrame(self.verticalLayoutWidget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 4, 0, 1, 1)

        self.line_5 = QFrame(self.verticalLayoutWidget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 2, 2, 1, 1)

        self.checkBox_quickSetting9 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting9.setObjectName(u"checkBox_quickSetting9")
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting9.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting9.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting9.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting9, 5, 4, 1, 1)

        self.line_6 = QFrame(self.verticalLayoutWidget_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 2, 4, 1, 1)

        self.checkBox_quickSetting6 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting6.setObjectName(u"checkBox_quickSetting6")
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting6.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting6.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting6.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting6, 3, 4, 1, 1)

        self.line_10 = QFrame(self.verticalLayoutWidget_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_10, 0, 0, 1, 5)

        self.checkBox_quickSetting8 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting8.setObjectName(u"checkBox_quickSetting8")
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting8.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting8.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting8.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting8, 5, 2, 1, 1)

        self.checkBox_quickSetting7 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting7.setObjectName(u"checkBox_quickSetting7")
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting7.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting7.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting7.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting7, 5, 0, 1, 1)

        self.line_2 = QFrame(self.verticalLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 3, 5, 1)

        self.checkBox_quickSetting4 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_quickSetting4.setObjectName(u"checkBox_quickSetting4")
        sizePolicy3.setHeightForWidth(self.checkBox_quickSetting4.sizePolicy().hasHeightForWidth())
        self.checkBox_quickSetting4.setSizePolicy(sizePolicy3)
        self.checkBox_quickSetting4.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.checkBox_quickSetting4, 3, 0, 1, 1)

        self.line_3 = QFrame(self.verticalLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 0, 1, 1)

        self.line_11 = QFrame(self.verticalLayoutWidget_2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_11, 6, 0, 1, 5)


        self.verticalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionOpen_Github_help_page)
        self.menuHelp.addAction(self.actionCheck_for_updates)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionOpen_Github_help_page.setText(QCoreApplication.translate("MainWindow", u"Open Github help page", None))
        self.actionCheck_for_updates.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.label_Command.setText(QCoreApplication.translate("MainWindow", u"Command", None))
        ___qtreewidgetitem = self.treeWidget_symbolTree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Symbols", None));

        __sortingEnabled = self.treeWidget_symbolTree.isSortingEnabled()
        self.treeWidget_symbolTree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_symbolTree.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Basic symbols", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"A normal arrow", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Arrow", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"A normal line", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"A normal rectangle", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Rectangle", None));
        ___qtreewidgetitem5 = self.treeWidget_symbolTree.topLevelItem(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Advanced symbols", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Test 1", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem5.child(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Test 2", None));
        self.treeWidget_symbolTree.setSortingEnabled(__sortingEnabled)

        self.checkBox_quickSetting3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_quickSetting5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_quickSetting2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_quickSetting1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_quickSetting9.setText(QCoreApplication.translate("MainWindow", u"Dark background", None))
        self.checkBox_quickSetting6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_quickSetting8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_quickSetting7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_quickSetting4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

