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
from PyQt5.QtWidgets import QGraphicsScene
# from PyQt5.QtGui import QPen, QBrush, QTransform
# from PyQt5.QtCore import QRectF
# from PyQt5.QtWidgets import QGraphicsRectItem

from TBDIC_core import TBDIC_core


class DATA:
    """
    This class contains all the data that is used in the program.
    """

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


class TBDIC_drawer:
    """
    This class contains all the functions that draw the diagrams.

    The diagrams are drawn using the PyQt5 library
    in the 'graphicsView_diagramDisplay' widget.
    """

    def __init__(self, drawing_area):
        self.drawing_area = drawing_area
        self.scene = QGraphicsScene()
        self.drawing_area.setScene(self.scene)

    def draw_rectangle(self, starting_point: tuple, width, height, rounded=False, color=None, obj=None):
        pass


class MainApp(QMainWindow):
    """
    This class contains the main application.
    """

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)

        self.data_loader = DATA()
        self.ui_loader = UiLoader()
        self.tbdic_core = TBDIC_core()
        self.tbdic_drawer = TBDIC_drawer(self)

        self.stacked_widget = QStackedWidget()

        self.main_window = self.ui_loader.load_ui(
            self.data_loader.getUIBasePath() + 'TBDIC.ui')

        self.configure_connections()

        self.stacked_widget.addWidget(self.main_window)
        self.setCentralWidget(self.stacked_widget)

        self.setFixedSize(DATA.INITIAL_SIZE[0], DATA.INITIAL_SIZE[1])
        # self.show()

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and
            event.key() == Qt.Key_Return and
                source is self.text_edit):

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

        self.QApplication.instance().quit()

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

        # Remove empty lines
        # Remove comments (starting with #!)
        command_text = [line for line in command_text if line != '']
        command_text = [line for line in command_text if line[0] != '#!']

        # Loop through all commands

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
