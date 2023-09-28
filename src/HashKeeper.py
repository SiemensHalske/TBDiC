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


class UiLoader:
    ui_list = {
        "main": "ui/main.ui",
    }

    def __init__(self):
        pass

    def load_ui(self, ui_file_name):
        ui = QMainWindow()
        loadUi(ui_file_name, ui)
        return ui


class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.ui_loader = UiLoader()


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
    CoreFunctions().clear_screen()
    env = setup()
    exit_code = main(sys.argv, env)

    sys.exit(exit_code)
