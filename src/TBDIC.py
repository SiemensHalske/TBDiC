#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script Name: TBDIC.py
Author: Hendrik
Date Created: 23-09-2023
Last Modified: 23-09-2023
Version: v0.1

Description:
    TBDIC.py is a script that generates diagrams from text input from a file or
    from the command line.

Usage:
    python3 TBDIC.py [options]

Requirements:
    - Python >= 3.6: python
    - Additional libraries:
        - PyQt5

License:
    license

Copyright (c) 2023 Hendrik
"""

# Import statements
import signal
import sys
import os
from types import SimpleNamespace
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QEvent
# from PyQt5.QtWidgets import QGraphicsScene
# from PyQt5.QtCore import QRectF
# from PyQt5.QtWidgets import QGraphicsRectItem
# from typing import Union, Optional

from TBDIC_core import TBDIC_core
from TBDIC_drawer import TBDIC_drawer


class DATA:
    """
    This class contains all the data that is used in the program.

    FEATURE_STATUS: This dictionary contains the status of all the features.
                    All new features should be added here and set to False.
    """

    GITHUB_REPO_URL = 'https://github.com/SiemensHalske/TBDiC'
    UI_BASE_PATH = '/home/hendrik/Documents/Projects/TBDiC/gui/'
    INITIAL_SIZE = (1280, 720)

    def __init__(self):
        pass

    def getUIBasePath(self):
        return self.UI_BASE_PATH


class CoreFunctions:
    """
    This class contains all the core functions.
    """

    def __init__(self):
        pass


class UiLoader:
    def load_ui(self, ui_file_name):
        ui = QMainWindow()
        loadUi(ui_file_name, ui)
        return ui


class MainApp(QMainWindow):
    """
    This class contains the main application.
    """

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)

        self.data_loader = DATA()
        self.ui_loader = UiLoader()
        self.tbdic_core = TBDIC_core()

        self.stacked_widget = QStackedWidget()

        self.main_window = self.ui_loader.load_ui(
            self.data_loader.getUIBasePath() + 'TBDIC.ui')

        self.tbdic_drawer = TBDIC_drawer(
            self.main_window.graphicsView_diagramDisplay)
        self.configure_connections()

        self.stacked_widget.addWidget(self.main_window)
        self.setCentralWidget(self.stacked_widget)

        self.setFixedSize(DATA.INITIAL_SIZE[0], DATA.INITIAL_SIZE[1])
        # self.show()

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and
            event.key() == Qt.Key_Return and
            event.modifiers() == Qt.ControlModifier and  # Prüfe auf CTRL
                source is self.main_window.textEdit_commandInput):

            # Get the text from QTextEdit and pass it to onCommandHandling
            self.onCommandHandling()

            return True  # Event was consumed

        return super().eventFilter(source, event)

    def configure_connections(self):
        """
        This function configures the connections between the widgets elements.
        """

        self.main_window.actionClose.triggered.connect(self.onCloseApplication)
        self.main_window.checkBox_quickSetting9.stateChanged.connect(
            self.onCheckBoxQuickSetting)

        self.main_window.textEdit_commandInput.installEventFilter(self)

    def onCloseApplication(self):
        """
        This function closes the application.
        """

        QApplication.instance().quit()

    def onCheckBoxQuickSetting(self):
        # Create a list of all check boxes
        all_check_boxes = [
            self.main_window.checkBox_quickSetting1,
            self.main_window.checkBox_quickSetting2,
            self.main_window.checkBox_quickSetting3,
            self.main_window.checkBox_quickSetting4,
            self.main_window.checkBox_quickSetting5,
            self.main_window.checkBox_quickSetting6,
            self.main_window.checkBox_quickSetting7,
            self.main_window.checkBox_quickSetting8,
            self.main_window.checkBox_quickSetting9,
        ]

        # Create a list of lists of check boxes, representing rows
        check_box_rows = [
            [all_check_boxes[0], all_check_boxes[1], all_check_boxes[2]],
            [all_check_boxes[3], all_check_boxes[4], all_check_boxes[5]],
            [all_check_boxes[6], all_check_boxes[7], all_check_boxes[8]],
        ]

        # Create a list of lists of button states, representing rows
        button_states = [
            [False, False, False],
            [False, False, False],
            [False, False, False],
        ]

        # Loop through all 9 check buttons
        for i, row in enumerate(check_box_rows):
            for j, check_box in enumerate(row):
                if check_box.isChecked():
                    button_states[i][j] = True

        print(button_states)

    def onCommandHandling(self):
        raw_command_text = self.main_window.textEdit_commandInput.toPlainText()
        command_text: list = raw_command_text.split('\n')

        self.main_window.textEdit_commandInput.clear()

        for line in command_text:
            # grab the text til the first whitespace -> command
            command = line.split(' ')[0]

            if command == '':
                continue
            elif command.startswith('!'):
                command = command[1:]
                if command == 'clear':
                    self.tbdic_drawer.clear_scene()
                elif command == 'exit':
                    self.onCloseApplication()
                elif command == 'help':
                    os.system(f"xdg-open {DATA.GITHUB_REPO_URL}")
            elif command.startswith('draw'):
                self.onDrawCommand(command)

        # TODO: #1 Add... the rest

        self.setNotificationBox('Command executed. OK!')

    def render_diagram(self):
        pass


def clear_screen():
    """
    This function clears the terminal screen.
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def setup():
    """
    This function sets up the environment variables.
    """
    global env

    env = SimpleNamespace()

    return env


if __name__ == '__main__':
    clear_screen()
    env = setup()

    app = QApplication(sys.argv)
    main_app = MainApp()

    main_app.show()

    app.aboutToQuit.connect(app.deleteLater)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())
