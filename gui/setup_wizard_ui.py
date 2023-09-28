# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup_wizard.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Wizard(object):
    def setupUi(self, Wizard):
        if not Wizard.objectName():
            Wizard.setObjectName(u"Wizard")
        Wizard.resize(530, 686)
        self.wizardPage1 = QWizardPage()
        self.wizardPage1.setObjectName(u"wizardPage1")
        self.verticalLayoutWidget = QWidget(self.wizardPage1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 494, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_6 = QFrame(self.verticalLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_uPromptSelectPath = QLabel(self.verticalLayoutWidget)
        self.label_uPromptSelectPath.setObjectName(u"label_uPromptSelectPath")
        self.label_uPromptSelectPath.setAutoFillBackground(True)
        self.label_uPromptSelectPath.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_uPromptSelectPath)

        self.pushButton_openDatabaseFileDialog = QPushButton(self.verticalLayoutWidget)
        self.pushButton_openDatabaseFileDialog.setObjectName(u"pushButton_openDatabaseFileDialog")

        self.verticalLayout_5.addWidget(self.pushButton_openDatabaseFileDialog)

        self.line_5 = QFrame(self.verticalLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_5)

        self.label_displayDatabasePath = QLabel(self.verticalLayoutWidget)
        self.label_displayDatabasePath.setObjectName(u"label_displayDatabasePath")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_displayDatabasePath.sizePolicy().hasHeightForWidth())
        self.label_displayDatabasePath.setSizePolicy(sizePolicy)
        self.label_displayDatabasePath.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_displayDatabasePath)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_uPromptSelectTimezone = QLabel(self.verticalLayoutWidget)
        self.label_uPromptSelectTimezone.setObjectName(u"label_uPromptSelectTimezone")
        self.label_uPromptSelectTimezone.setAutoFillBackground(True)
        self.label_uPromptSelectTimezone.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_uPromptSelectTimezone)

        self.line_4 = QFrame(self.verticalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_autoTimezone = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_autoTimezone.setObjectName(u"checkBox_autoTimezone")

        self.verticalLayout_3.addWidget(self.checkBox_autoTimezone)

        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.comboBox_selectTimezone = QComboBox(self.verticalLayoutWidget)
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.setObjectName(u"comboBox_selectTimezone")

        self.verticalLayout_3.addWidget(self.comboBox_selectTimezone)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_7 = QFrame(self.verticalLayoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_6.addWidget(self.checkBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_uSelectPermanentAlgorithm = QLabel(self.verticalLayoutWidget)
        self.label_uSelectPermanentAlgorithm.setObjectName(u"label_uSelectPermanentAlgorithm")
        self.label_uSelectPermanentAlgorithm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_uSelectPermanentAlgorithm)

        self.comboBox_selectPermanentAlgorithm = QComboBox(self.verticalLayoutWidget)
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.addItem("")
        self.comboBox_selectPermanentAlgorithm.setObjectName(u"comboBox_selectPermanentAlgorithm")
        self.comboBox_selectPermanentAlgorithm.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.comboBox_selectPermanentAlgorithm)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_6.addWidget(self.checkBox)

        self.comboBox_selectPermanentAlgorithm_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.addItem("")
        self.comboBox_selectPermanentAlgorithm_2.setObjectName(u"comboBox_selectPermanentAlgorithm_2")
        self.comboBox_selectPermanentAlgorithm_2.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.comboBox_selectPermanentAlgorithm_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.verticalLayoutWidget_3 = QWidget(self.wizardPage2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 491, 571))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_10, 0, 2, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 2, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 3, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_11, 8, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 2, 2, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 5, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 7, 0, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.progressBar = QProgressBar(self.verticalLayoutWidget_3)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 7, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 4, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 6, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 7, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_7, 8, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 8, 3, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 8, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_15, 2, 3, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_16, 2, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_17, 6, 3, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_18, 6, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)

        QMetaObject.connectSlotsByName(Wizard)
    # setupUi

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QCoreApplication.translate("Wizard", u"Wizard", None))
        self.label_uPromptSelectPath.setText(QCoreApplication.translate("Wizard", u"Select a path for the database:", None))
        self.pushButton_openDatabaseFileDialog.setText(QCoreApplication.translate("Wizard", u"Open file dialog", None))
        self.label_displayDatabasePath.setText(QCoreApplication.translate("Wizard", u"DB filepath", None))
        self.label_uPromptSelectTimezone.setText(QCoreApplication.translate("Wizard", u"Set the timezone you're in:", None))
        self.checkBox_autoTimezone.setText(QCoreApplication.translate("Wizard", u"Auto detect timezone", None))
        self.comboBox_selectTimezone.setItemText(0, QCoreApplication.translate("Wizard", u"UTC", None))
        self.comboBox_selectTimezone.setItemText(1, QCoreApplication.translate("Wizard", u"Europe / London", None))
        self.comboBox_selectTimezone.setItemText(2, QCoreApplication.translate("Wizard", u"Europe / Berlin", None))
        self.comboBox_selectTimezone.setItemText(3, QCoreApplication.translate("Wizard", u"Europe / Paris", None))
        self.comboBox_selectTimezone.setItemText(4, QCoreApplication.translate("Wizard", u"Europe / Moscow", None))
        self.comboBox_selectTimezone.setItemText(5, QCoreApplication.translate("Wizard", u"Asia / Tokyo", None))

        self.checkBox_2.setText(QCoreApplication.translate("Wizard", u"Enable permanent hash algorithm", None))
        self.label_uSelectPermanentAlgorithm.setText(QCoreApplication.translate("Wizard", u"Permanent hash algorithm (CAUTION!)", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(0, QCoreApplication.translate("Wizard", u"- - - ", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(1, QCoreApplication.translate("Wizard", u"MD5", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(2, QCoreApplication.translate("Wizard", u"SHA-1", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(3, QCoreApplication.translate("Wizard", u"SHA256", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(4, QCoreApplication.translate("Wizard", u"SHA-3", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(5, QCoreApplication.translate("Wizard", u"SHA512", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(6, QCoreApplication.translate("Wizard", u"Whirlpool", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(7, QCoreApplication.translate("Wizard", u"Blake3", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(8, QCoreApplication.translate("Wizard", u"RIPEMD-160", None))
        self.comboBox_selectPermanentAlgorithm.setItemText(9, QCoreApplication.translate("Wizard", u"Tiger", None))

        self.comboBox_selectPermanentAlgorithm.setCurrentText(QCoreApplication.translate("Wizard", u"- - - ", None))
        self.checkBox.setText(QCoreApplication.translate("Wizard", u"Encrypt database", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(0, QCoreApplication.translate("Wizard", u"- - - ", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(1, QCoreApplication.translate("Wizard", u"MD5", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(2, QCoreApplication.translate("Wizard", u"SHA-1", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(3, QCoreApplication.translate("Wizard", u"SHA256", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(4, QCoreApplication.translate("Wizard", u"SHA-3", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(5, QCoreApplication.translate("Wizard", u"SHA512", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(6, QCoreApplication.translate("Wizard", u"Whirlpool", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(7, QCoreApplication.translate("Wizard", u"Blake3", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(8, QCoreApplication.translate("Wizard", u"RIPEMD-160", None))
        self.comboBox_selectPermanentAlgorithm_2.setItemText(9, QCoreApplication.translate("Wizard", u"Tiger", None))

        self.comboBox_selectPermanentAlgorithm_2.setCurrentText(QCoreApplication.translate("Wizard", u"- - - ", None))
        self.label.setText(QCoreApplication.translate("Wizard", u"Your configuration", None))
        self.label_3.setText(QCoreApplication.translate("Wizard", u"Database path", None))
        self.label_8.setText(QCoreApplication.translate("Wizard", u"- - -", None))
        self.label_6.setText(QCoreApplication.translate("Wizard", u"Current date and time", None))
        self.label_4.setText(QCoreApplication.translate("Wizard", u"- - -", None))
        self.label_7.setText(QCoreApplication.translate("Wizard", u"- - -", None))
        self.label_2.setText(QCoreApplication.translate("Wizard", u"Database ready?", None))
        self.label_5.setText(QCoreApplication.translate("Wizard", u"Timezone", None))
    # retranslateUi

