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
        Wizard.resize(530, 646)
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
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.checkBox_autodetectTimezone = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_autodetectTimezone.setObjectName(u"checkBox_autodetectTimezone")
        self.checkBox_autodetectTimezone.setAutoFillBackground(True)

        self.horizontalLayout_3.addWidget(self.checkBox_autodetectTimezone)

        self.comboBox_selectTimezone = QComboBox(self.verticalLayoutWidget)
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.addItem("")
        self.comboBox_selectTimezone.setObjectName(u"comboBox_selectTimezone")

        self.horizontalLayout_3.addWidget(self.comboBox_selectTimezone)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        Wizard.addPage(self.wizardPage2)
        QWidget.setTabOrder(self.pushButton_2, self.checkBox_autodetectTimezone)
        QWidget.setTabOrder(self.checkBox_autodetectTimezone, self.comboBox_selectTimezone)
        QWidget.setTabOrder(self.comboBox_selectTimezone, self.pushButton_3)

        self.retranslateUi(Wizard)

        QMetaObject.connectSlotsByName(Wizard)
    # setupUi

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QCoreApplication.translate("Wizard", u"Wizard", None))
        self.label.setText(QCoreApplication.translate("Wizard", u"Select a path for the database:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Wizard", u"Open file dialog", None))
        self.label_3.setText(QCoreApplication.translate("Wizard", u"Set the timezone you're in:", None))
        self.checkBox_autodetectTimezone.setText(QCoreApplication.translate("Wizard", u"Auto detect timezone", None))
        self.comboBox_selectTimezone.setItemText(0, QCoreApplication.translate("Wizard", u"UTC", None))
        self.comboBox_selectTimezone.setItemText(1, QCoreApplication.translate("Wizard", u"Europe / London", None))
        self.comboBox_selectTimezone.setItemText(2, QCoreApplication.translate("Wizard", u"Europe / Berlin", None))
        self.comboBox_selectTimezone.setItemText(3, QCoreApplication.translate("Wizard", u"Europe / Paris", None))
        self.comboBox_selectTimezone.setItemText(4, QCoreApplication.translate("Wizard", u"Europe / Moscow", None))
        self.comboBox_selectTimezone.setItemText(5, QCoreApplication.translate("Wizard", u"Asia / Tokyo", None))

        self.label_2.setText(QCoreApplication.translate("Wizard", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("Wizard", u"PushButton", None))
    # retranslateUi

