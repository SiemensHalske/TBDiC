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
from PyQt5.QtGui import QPen, QColor
# from PyQt5.QtCore import QRectF
# from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtWidgets import QGraphicsRectItem
from typing import Union, Optional

from TBDIC_core import TBDIC_core


def feature_enabled(func):
    """
    This decorator checks whether a feature is enabled or not.
    """

    def wrapper(self, *args, **kwargs):
        if CoreFunctions.feature_enabled(func.__name__):
            return func(self, *args, **kwargs)
        else:
            return None
    return wrapper


class DATA:
    """
    This class contains all the data that is used in the program.

    FEATURE_STATUS: This dictionary contains the status of all the features.
                    All new features should be added here and set to False.
    """

    UI_BASE_PATH = '/home/hendrik/Documents/Projects/TBDiC/gui/'
    INITIAL_SIZE = (1280, 720)

    FEATURE_STATUS = {
        '_applyRoundedCorners': False,
        '_imageLoader': False,
    }

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

    def _check_if_feature_enabled(self):
        """
        This function checks whether a feature is enabled or not.
        """
        pass

    def feature_enabled(self, feature_name: str) -> bool:
        """
        This function checks whether a feature is enabled or not.
        """
        feature_status = False

        return feature_status


class UiLoader:
    def load_ui(self, ui_file_name):
        ui = QMainWindow()
        loadUi(ui_file_name, ui)
        return ui


class TBDIC_drawer_helper:
    """
    This class contains all the helper functions for the TBDIC_drawer class.
    """

    def __init__(self):
        pass

    def _setColor(
        self,
        pen_size: int = 2,
        color: Union[tuple, Optional[str]] = None
    ) -> QPen:
        """
        This function sets the color of the pen.

        @param color: The color of the pen. (rgb tuple or color name)

        @return: The pen with the color set.
        """

        pen = QPen()
        pen.setWidth(pen_size)

        if color is not None:
            if isinstance(color, tuple):
                pen.setColor(QColor(color[0], color[1], color[2]))
            elif isinstance(color, str):
                pen.setColor(QColor(color))

        return pen

    def _setObject(self):
        pass

    @feature_enabled
    def _imageLoader(self):
        pass

    @feature_enabled
    def _applyRoundedCorners(self, rect_item: QGraphicsRectItem):
        pass


class TBDIC_drawer(TBDIC_drawer_helper):
    """
    This class contains all the functions that draw the diagrams.

    The diagrams are drawn using the PyQt5 library
    in the 'graphicsView_diagramDisplay' widget.
    """

    auto_name_template_line = 'line_{}'
    auto_name_template_arrow = 'arrow_{}'
    auto_name_template_rectangle = 'rectangle_{}'
    auto_name_template_ellipse = 'ellipse_{}'
    auto_name_template_circle = 'circle_{}'
    AUTO_ELEMENT_NAMES = []

    def __init__(self, drawing_area):
        self.drawing_area = drawing_area
        self.scene = QGraphicsScene()
        self.drawing_area.setScene(self.scene)

    def _addElementName(self, name: str, auto_name: bool = True) -> bool:
        """
        This function adds an element name to the list of element names.

        @param name: The name of the element.
        @param auto_name: Whether the name should be automatically generated.

        @return: bool - Whether the name was added successfully.
        """
        if auto_name:
            if name.startswith('line'):
                prefix = 'line'
            elif name.startswith('rectangle'):
                prefix = 'rectangle'
            elif name.startswith('circle'):
                prefix = 'circle'
            elif name.startswith('ellipse'):
                prefix = 'ellipse'
            elif name.startswith('arrow'):
                prefix = 'arrow'
            else:
                return False

            # Find the smallest index for the corresponding name
            index = 1
            while f"{prefix}_{index}" in self.AUTO_ELEMENT_NAMES:
                index += 1

            name = f"{prefix}_{index}"

        self.AUTO_ELEMENT_NAMES.append(name)
        return True

    def draw_line(
        self,
        name: str,
        starting_point: tuple,
        ending_point: tuple,
        color: Union[tuple, Optional[str]] = None
    ) -> None:
        """
        This function draws a line.
        """

        if name is None:
            ack = self._addElementName(name=name)
        else:
            ack = self._addElementName(name=name, auto_name=False)

        if not ack:
            return -1

        pen = self._setColor(color=color)

        self.scene.addLine(
            starting_point[0],
            starting_point[1],
            ending_point[0],
            ending_point[1],
            pen
        )

    def draw_arrow(
        self,
        name: str,
        starting_point: tuple,
        ending_point: tuple,
        color: Union[tuple, Optional[str]] = None
    ):
        """
        This function draws an arrow.
        """

        pass

    def draw_rectangle(
        self,
        name: str = "rectangle",
        starting_point: tuple = (0, 0),
        width: int = 0,  # width (rightward x-coordinate)
        height: int = 0,  # heigth (downward y-coordinate)
        rotation: int = 0,  # rotation in degrees
        rounded: bool = False,  # rounded edges or not?
        color: Union[tuple, Optional[str]] = None,  # color of the rectangle
        display_object: list = None  # list of the object to display
    ):
        """
        This function draws a rectangle.
        """

        if name is None:
            ack = self._addElementName(name=name)
        else:
            ack = self._addElementName(name=name, auto_name=False)

        if not ack:
            return -1

        # Set the color
        pen = self._setColor(color=color)

        # Create a QGraphicsRectItem
        rect_item = QGraphicsRectItem(
            starting_point[0], starting_point[1], width, height)

        # Set pen (color and other settings)
        rect_item.setPen(pen)

        # Apply rotation
        if rotation != 0:
            rect_item.setRotation(rotation)

        # Apply rounded corners
        if rounded:
            # You'll have to implement this yourself, QGraphicsRectItem doesn't
            # support it out-of-the-box
            self._applyRoundedCorners(rect_item)

        # Add the item to the scene
        self.scene.addItem(rect_item)

    def draw_ellipse(
        self,
        name: str,
        starting_point: tuple,
        width: int,
        height: int,
        rotation: int,
        color: Union[tuple, Optional[str]] = None,
        display_object=None
    ):
        """
        This function draws an ellipse.
        """

        pass

    def draw_circle(
        self,
        name: str,
        starting_point: tuple,
        radius: int,
        color: Union[tuple, Optional[str]] = None,
        display_object=None
    ):
        """
        This function draws a circle.
        """

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
