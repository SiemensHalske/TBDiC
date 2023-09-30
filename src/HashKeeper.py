#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script Name: HashKeeper.py
Author: Hendrik Siemens
Date Created: 26-09-2023
Last Modified: 26-09-2023
Version: 0.1

Description:
    HashKeeper is a tool to keep track of hashes of selected
    files and directories.

Usage:
    python3 HashKeeper.py [options]

Requirements:
    - Python >= 3.6: https://www.python.org/downloads/
    - Additional libraries: # TODO

License:
    MIT License

Copyright (c) 2023 Hendrik Siemens
"""

# Import statements
import sys
import os

from types import SimpleNamespace
from typing import Union
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


# Global variables


# Class definitions

class CoreFunctions:
    def __init__(self) -> None:
        pass

    def clear_screen(self) -> None:
        """Clears the screen"""
        os.system("cls" if os.name == "nt" else "clear")
        
    def


class UiLoader:
    # ../gui/
    base_ui_path = "/home/hendrik/Documents/Projects/TBDiC/gui/"
    ui_list = {
        "main": "main.ui",
    }

    def __init__(self):
        pass

    def ui_resolver(self, ui_name: str, auto_load: bool = True) -> Union[str, QMainWindow]:
        """
            Resolves the path to the UI file.
            Uses a restrictiv approach to prevent
            loading of arbitrary files.
        """

        if ui_name not in UiLoader.ui_list.keys():
            raise ValueError("Unknown UI file name.")

        ui_path = UiLoader.base_ui_path + UiLoader.ui_list[ui_name]

        if not auto_load:
            return ui_path

        return self.load_ui(ui_path)

    def load_ui(self, ui_file_name):
        ui = QMainWindow()
        loadUi(ui_file_name, ui)
        return ui


class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.ui_loader = UiLoader()

        self.main_window = self.ui_loader.ui_resolver("main", auto_load=True)

    def configureConnects(self):
        pass

# Function defintion


def main(system_arglist: list[str], env: SimpleNamespace) -> int:
    """Main function"""

    app = QApplication(system_arglist)
    window = MainApp()
    window.show()

    return app.exec_()


def setup() -> SimpleNamespace:
    glob = SimpleNamespace()

    return glob


if __name__ == "__main__":
    operating_system = os.name
    if operating_system == "nt" and sys.argv[1] != "nocheck":
        sys.exit("This script is not compatible with Windows.")
    CoreFunctions().clear_screen()
    env = setup()
    exit_code = main(sys.argv, env)

    sys.exit(exit_code)
