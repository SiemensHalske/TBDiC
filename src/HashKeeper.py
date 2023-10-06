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
import hashlib

from types import SimpleNamespace
from typing import Optional, Union
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QStackedWidget, QFileDialog
from PyQt5.QtWidgets import QFileSystemModel, QTreeView
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi

from Crypto.Hash import RIPEMD160
from blake3 import blake3


# Global variables

ENABLED_HASH_TYPES = {
    "md5": True,
    "sha1": True,
    "sha256": True,
    "sha3": True,
    "sha512": True,
    "blake3": True,
    "ripemd160": True,
    "whirlpool": False,
    "tiger192": False
}

# Decorators


def feature_status_hash(keyword):
    """Decorator to check if a feature is enabled."""
    def wrapper(func):
        def inner(self, *args, **kwargs):
            # replace with your own feature dictionary
            # feature_dict = {"feature1": True, "feature2": False}
            if keyword in ENABLED_HASH_TYPES.keys() and \
                    ENABLED_HASH_TYPES[keyword]:
                return func(self, *args, **kwargs)
            else:
                print(f"Error: {keyword} is not supported yet.")
        return inner
    return wrapper


# Class definitions

class DATA:
    MAIN_WINDOW_SIZE = (1280, 720)
    MAIN_WINDOW_TITLE = "HashKeeper"

    def __init__(self) -> None:
        pass


class coreCryptoFunctions:
    enabled_hash_types = [
        "md5",
        "sha1",
        "sha256",
        "sha3"
        "sha512",
        "blake3",
        "ripemd160",
        "whirlpool",
        "tiger192"
    ]

    def __init__(self) -> None:
        pass

    @feature_status_hash("md5")
    def hashFile_md5(self, file_path: str) -> str:
        file_hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
        return file_hash

    @feature_status_hash("sha1")
    def hashFile_sha1(self, file_path: str) -> str:
        file_hash = hashlib.sha1(open(file_path, "rb").read()).hexdigest()
        return file_hash

    @feature_status_hash("sha256")
    def hashFile_sha256(self, file_path: str) -> str:
        file_hash = hashlib.sha256(open(file_path, "rb").read()).hexdigest()
        return file_hash

    @feature_status_hash("sha3")
    def hashFile_sha3(self, file_path: str) -> str:
        file_hash = hashlib.sha3_512(open(file_path, "rb").read()).hexdigest()
        return file_hash

    @feature_status_hash("sha512")
    def hashFile_sha512(self, file_path: str) -> str:
        file_hash = hashlib.sha512(open(file_path, "rb").read()).hexdigest()
        return file_hash

    @feature_status_hash("whirlpool")
    def hashFile_whirlpool(self, file_path: str) -> str:
        # file_hash = Whirlpool.new(open(file_path, "rb").read()).hexdigest()
        file_hash = "Whirlpool not supported"
        return file_hash

    @feature_status_hash("blake3")
    def hashFile_blake3(self, file_path: str) -> str:
        file_hash = blake3(open(file_path, "rb").read()).hexdigest()
        return file_hash

    @feature_status_hash("ripemd160")
    def hashFile_ripemd160(self, file_path: str) -> str:
        file_hash = RIPEMD160.new(open(file_path, "rb").read()).hexdigest()
        return file_hash

    @feature_status_hash("tiger192")
    def hashFile_tiger192(self, file_path: str) -> str:
        # file_hash = Tiger.new(open(file_path, "rb").read()).hexdigest()
        file_hash = "Tiger not supported"
        return file_hash


class CoreFunctions(coreCryptoFunctions):
    def __init__(self) -> None:
        pass

    def clear_screen(self) -> None:
        """Clears the screen"""
        os.system("cls" if os.name == "nt" else "clear")

<<<<<<< HEAD
    def redesign_file_list(self, file_list: list[str]) -> list[str, str]:
        """
            Redesigns the file list to a list of
            tuples with the file path and an empty string
        """
        return [(file_path, "") for file_path in file_list]
=======
    def _uiPathAssembler(
        self,
        display_window: str,
    ) -> str:
        pass
>>>>>>> 8a4266cb8e7accf2652c79104da5937adadcc474


class UiLoader:
    # ../gui/
    base_ui_path = "/home/hendrik/Documents/Projects/TBDiC/gui/"
    ui_list = {
        "main": "main.ui",
    }

    def __init__(self):
        pass

    def ui_resolver(
        self,
        ui_name: str,
        auto_load: bool = True
    ) -> Union[str, QMainWindow]:
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


class HashKeeperCore:
    def __init__(self) -> None:
        pass

    def _runSelfTest(self):
        """Runs a self test to check if everything is working as expected."""
        selftest_message = """
        ********************
        Running self test...
        Nothing to do here...
        Self test successful.
        ********************
        """

        print(selftest_message)

    def _hashRound(
        self,
        file_list: list[str, str],
        hash_type: str
    ) -> list[str, str]:
        """Performs a hash round."""
        # Loop for every file in the list and apply the
        # selected hash algorithm.
        # The first value of the list (multiple lists.. list in list...)
        # is the file path.
        # The second value is reserved for the hash string to be generated

        hashed_list = []

        # print(f"Length of file list: {len(file_list)}")
        # print(f"File list: {file_list}")
        # return file_list

        for file in file_list:
            file_hash = getattr(CoreFunctions(), hash_type)(file[0])
            hashed_list.append((file[0], file_hash))

        return hashed_list


class HashKeeperSystem(HashKeeperCore):
    enabled_hash_types = [
        "hashFile_md5",
        "hashFile_sha1",
        "hashFile_sha256",
        "hashFile_sha3"
        "hashFile_sha512",
        "hashFile_blake3",
        "hashFile_ripemd160",
        # "hashFile_whirlpool",
        # "hashFile_tiger192"
    ]

    def __init__(self) -> None:
        super().__init__()
        self._runSelfTest()

        self._file_list: list[str, str] = ["", ""]
        self._hash_type: str = ""
        self._base_dir: str = ""

    def start(self, start_hash_round: bool = True) -> list[str, str]:
        """Starts the HashKeeper system."""
        if start_hash_round and self._file_list and self._hash_type:
            file_list = self.onStartHashRound()
            return file_list
        else:
            print("Error: Could not start HashKeeper system.")
            return -1

    def onStartHashRound(self) -> list[str, str]:
        """Starts a hash round."""
        file_list = self._hashRound(self._file_list, self._hash_type)
        return file_list

    def setFileList(self, file_list: list[str, str]) -> int:
        """#!DO NOT CHANGE! Sets the file list."""
        if not self._file_list:
            print("Uhoh, something's fishy here...")
            return -1

        self._file_list = file_list

        # old -> list[str]; new is list[str, str]
        # self._base_dir = str(self._file_list[0].rsplit("/", 1)[0])
        self._base_dir = str(self._file_list[0][0].rsplit("/", 1)[0])

        return 0

    def setHashType(self, hash_type: str) -> None:
        """#!DO NOT CHANGE! Sets the hash type."""
        if hash_type not in HashKeeperSystem.enabled_hash_types:
            print("Error: Hash type not supported.")
            return -1

        self._hash_type = hash_type
        return 0

    def hashFile(self, file_path: str, hash_type: str) -> str:
        """#!DO NOT CHANGE! Hashes a file."""

        if hash_type not in HashKeeperSystem.enabled_hash_types:
            print("Error: Hash type not supported.")
            return "Unsupported hash type"
        elif not os.path.exists(file_path):
            print("Error: File does not exist.")
            return "File does not exist"

        return getattr(CoreFunctions(), hash_type)(file_path)


class FileTreeApp(QObject):
    selectedFilesChanged = pyqtSignal(list)

    def __init__(self, tree_view_widget):
        super().__init__()

        self.tree = tree_view_widget
        self.model = QFileSystemModel()
        self.tree.setModel(self.model)
        self.tree.setSelectionMode(QTreeView.MultiSelection)

        self.tree.selectionModel().selectionChanged.connect(
            self.on_selection_changed)
        self.all_files = set()

    def set_base_dir(self, base_dir):
        if os.path.exists(base_dir):
            self.model.setRootPath(base_dir)
            self.tree.setRootIndex(self.model.index(base_dir))

    def on_selection_changed(self, selected, deselected):
        # Handling selected files
        for index in selected.indexes():
            if index.column() == 0:  # Only consider the first column
                path = self.model.filePath(index)
                if os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            self.all_files.add(os.path.join(root, file))
                else:
                    self.all_files.add(path)

        # Handling deselected files
        for index in deselected.indexes():
            if index.column() == 0:  # Only consider the first column
                path = self.model.filePath(index)
                if os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            self.all_files.discard(os.path.join(root, file))
                else:
                    self.all_files.discard(path)

        # Convert set back to list before emitting
        self.selectedFilesChanged.emit(list(self.all_files))
        # print(f"Selected files: {self.all_files}")


class MainApp(QMainWindow):
    FILE_LIST = []

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.ui_loader = UiLoader()

        self.hashing_system = HashKeeperSystem()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        try:
            self.main_window = self.ui_loader.ui_resolver(
                "main", auto_load=True)
            if not isinstance(self.main_window, QMainWindow) and \
                    not self.main_window:
                raise TypeError("Loaded UI is not of type QMainWindow.")
        except ValueError and TypeError as e:
            print(f"Error: {e}")
            self.onCloseApplication()

        self.main_window.setWindowTitle(DATA.MAIN_WINDOW_TITLE)
        self.main_window.setFixedSize(*DATA.MAIN_WINDOW_SIZE)
        self.configureConnects()

        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.setCurrentWidget(self.main_window)

        self.file_tree_app = FileTreeApp(
            self.main_window.treeView_fileSelection)
        self.file_tree_app.selectedFilesChanged.connect(self.onReceiveFileList)

        self.show()

    def configureConnects(self):
        self.main_window.pushButton_Exit.clicked.connect(
            self.onCloseApplication)
        self.main_window.actionClose.triggered.connect(
            self.onCloseApplication)

        self.main_window.pushButton_selectBaseDir.clicked.connect(
            self.onSelectBaseDirectory)
        self.main_window.pushButton_startHashRound.clicked.connect(
            self.onStartHashRound)

        # auto set md5 to checked in case the user doesn't select any hash type
        # (checkBox_hashFile_md5)
        self.main_window.checkBox_hashFile_md5.setChecked(True)

    def getkHashType(self):
        """Checks which hash type is selected."""
        checkBox_basename = "checkBox_hashFile_"

        for hash_type in HashKeeperSystem.enabled_hash_types:
            checkBox = getattr(
                self.main_window, checkBox_basename + hash_type.replace(
                    "hashFile_", ""))
            if checkBox.isChecked():
                return hash_type

        return "checkBox_md5"

    def onCloseApplication(self):
        print("Closing application...")
        QApplication.instance().quit()

    def onSelectBaseDirectory(self):
        """
            Opens a file dialog to select the base directory
            for further operations.
        """

        print("Selecting base directory...")
        base_dir = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"
        ))

        self.file_tree_app.set_base_dir(base_dir)

    def onReceiveFileList(self, selected_files):
        selected_files = CoreFunctions().redesign_file_list(selected_files)
        self.FILE_LIST = selected_files

    def onStartHashRound(self):
        pass

    def onPopulateTextBrowser(self, file_list: list[str, str]):
        # Clear previous results
        self.main_window.textBrowser_displayResults.clear()

        if not file_list:
            self.main_window.textBrowser_displayResults.append(
                "No files selected.")
            return

        self.main_window.textBrowser_displayResults.append(
            "Selected files and/or directories:\n")
        for file in file_list:
            self.main_window.textBrowser_displayResults.append(
                f"File:\n{file[0]}\nHash:{file[1]}\n\n")

    def _assembleDisplayMessage(self, file_list: list[str]) -> dict[str, str]:
        """Assembles the display message for the text browser."""
        pass


# Function defintion


def main(
    system_arglist: list[str],
    env: SimpleNamespace,
    override_main_show: Optional[bool] = False
) -> int:
    """Main function"""

    app = QApplication(system_arglist)
    window = MainApp()
    if override_main_show:
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
