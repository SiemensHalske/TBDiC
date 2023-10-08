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
import datetime
import json
import sys
import os
import hashlib
import inspect
# import sqlite3 as sql

from types import SimpleNamespace
from typing import Optional, Union
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QStackedWidget, QFileDialog
from PyQt5.QtWidgets import QFileSystemModel, QTreeView
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi

from Crypto.Hash import RIPEMD160
from blake3 import blake3
from FileTreeApp import FileTreeApp

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, FileHash, Timestamp

# Global variables

PACKAGE_PATH = "/home/hendrik/Documents/Projects/TBDiC/"

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

    def redesign_file_list(self, file_list: list[str]) -> list[str, str]:
        """
            Redesigns the file list to a list of
            tuples with the file path and an empty string
        """
        return [(file_path, "") for file_path in file_list]

    def _convertListToJson(self, file_list: list[str, str]) -> str:
        """Converts the file list to a JSON string."""

        return json.dumps(file_list)

    def createJobFile(
        self,
        file_list: list[str, str],
        hash_type: str,
        workingtime: str,
        planned: bool = False
    ) -> None:

        file_list_json = self._convertListToJson(file_list)

        # create a job file
        # depending on 'planned' it is decided
        # if it is a planned job or a manual one
        # -> also decides storage location

        # planned job
        if planned:
            # create directory if it doesn't exist
            # -> ../data/planned_jobs/
            if not os.path.exists(f"{PACKAGE_PATH}data/planned_jobs"):
                os.makedirs(f"{PACKAGE_PATH}data/planned_jobs")

            # create the file
            # -> ../data/planned_jobs/<workingtime>.json
            filename = f"planned_{workingtime}_{hash_type}.json"
            with open(
                f"{PACKAGE_PATH}data/planned_jobs/{filename}",
                    "w") as f:
                f.write(file_list_json)

        # manual job
        else:
            # create directory if it doesn't exist
            # -> ../data/
            if not os.path.exists(f"{PACKAGE_PATH}data"):
                os.makedirs(f"{PACKAGE_PATH}data")

            # create the file
            # -> ../data/<workingtime>.json
            with open(f"{PACKAGE_PATH}data/{workingtime}_{hash_type}.json",
                      "w") as f:
                f.write(file_list_json)

        return


class UiLoader:
    # ../gui/
    base_ui_path = "/home/hendrik/Documents/Projects/TBDiC/gui/"
    ui_list = {
        "main": "main.ui"
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
    DB_PATH = "/home/hendrik/Documents/Projects/TBDiC/data/"
    DB_NAME = "hashkeeper.db"

    def __init__(self) -> None:
        pass

    def get_db_session(self) -> sessionmaker:
        engine = create_engine(
            f"sqlite:///{HashKeeperCore.DB_PATH}{HashKeeperCore.DB_NAME}",
            echo=True
        )

        Session = sessionmaker(bind=engine)
        session = Session()

        return session

    def _change_db(self, new_path: str) -> int:
        """Changes the database path.
        new_path: str -> absolute path to the new database
            |
            |--> extract db_path
            |--> extract db_name
        """
        try:
            # Check if the path exists
            if not os.path.exists(new_path):
                raise ValueError("Path does not exist.")

            # Extract db_path
            db_path = os.path.dirname(new_path)

            # Extract db_name
            db_name = os.path.basename(new_path)

            # Update class variables
            self.DB_PATH = db_path
            self.DB_NAME = db_name

            return 0
        except ValueError as e:
            print(f"Error: {e}")
            return -1

    def create_database(self, db_path: str):
        """Creates the database."""

        # Check if the path exists
        if not os.path.exists(db_path):
            raise ValueError("Path does not exist.")

        # Update class variables
        self.DB_PATH = os.path.dirname(db_path)
        self.DB_NAME = os.path.basename(db_path)

        # Create database
        engine = create_engine(
            f"sqlite:///{self.DB_PATH}{self.DB_NAME}",
            echo=True
        )

        Base.metadata.create_all(engine)

        return 0


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

    _hash_type: str = ""
    _file_list: list[str, str] = []

    def __init__(self) -> None:
        super().__init__()

        self._file_list: list[str, str] = ["", ""]
        self._hash_type: str = ""
        self._base_dir: str = ""

        self._runSelfTest()

    def _runSelfTest(self) -> None:
        """Runs a self test to check if the system is ready to use."""
        msg = """
        Running self test...
        Okay... I'm ready to go!
        """
        print(msg)
        return

    def _insertIntoDatabase(self, file_list: list[str, str]) -> int:
        """Inserts the file list into the database."""
        return_code: int = -1

        session = self.get_db_session()
        try:
            # Create a new timestamp and add it to the database
            timestamp = Timestamp()
            session.add(timestamp)

            # Add each file hash to the database with a foreign
            # key to the timestamp
            for file_tuple in file_list:
                file_hash = FileHash(
                    timestamp_id=timestamp.id,
                    file_path=file_tuple[0],
                    hash_type=self._hash_type,
                    file_hash=file_tuple[1]
                )
                session.add(file_hash)

            session.commit()
            return_code = 0
        except Exception as e:
            print(f"Error: {e}")
            session.rollback()
        finally:
            session.close()
            if return_code == 0:
                print("File hashes added to database.")
            else:
                print("Error adding file hashes to database.")
        return return_code

    def setFileList(self, file_list: list[str, str]) -> None:
        """Sets the file list."""
        self._file_list = file_list
        return

    def setHashType(self, hash_type: str) -> None:
        """Sets the hash type."""
        self._hash_type = hash_type
        return

    def firstRun(self) -> None:
        """First run of the system."""
        hashed_file_list = []
        for file_tuple in self._file_list:
            file_hash = getattr(coreCryptoFunctions, self._hash_type)(
                self, file_tuple[0])
            hashed_file_list.append((file_tuple[0], file_hash))

        self._insertIntoDatabase(self._file_list)


class TimedHashKeeper:
    plans_location = HashKeeperCore.DB_PATH + "planned_jobs/"
    plans_file_extension = "_planned.json"

    planned_jobs = []

    hash_type = "hashFile_md5"

    def __init__(self) -> None:
        pass

    def load_planned_jobs(self) -> None:
        """
        Loads the planned jobs ('_planned.json')
        from the planned_jobs file.
        """

        # check if the directory exists
        if not os.path.exists(self.plans_location):
            raise ValueError("Path does not exist.")

        # get all files in the directory
        files = os.listdir(self.plans_location)

        # filter for planned jobs
        files = [file for file in files if file.endswith(
            self.plans_file_extension)]

        # load the files
        for file in files:
            with open(self.plans_location + file, "r") as f:
                self.planned_jobs.append(json.load(f))

        # check if the function was called from an instance method
        frame = inspect.currentframe()
        if frame is not None:
            caller_locals = frame.f_back.f_locals
            if 'self' in caller_locals:
                return self.planned_jobs

        return 0

    def get_planned_jobs(self) -> list[str]:
        """Returns the planned jobs."""
        return self.planned_jobs

    def get_planned_job(self, job_id: int) -> dict[str, str]:
        """Returns a planned job."""
        return self.planned_jobs[job_id]

    def run(self, file_list: list[str, str], hash_type: str) -> int:
        """Runs a hash round on a planned job / a list of files."""

        timestamp = Timestamp()

        # check if the hash type is supported
        if hash_type not in HashKeeperCore.enabled_hash_types:
            raise ValueError("Hash type not supported.")

        # check if the file list is not empty
        if not file_list:
            raise ValueError("File list is empty.")

        # hash the files
        hashed_file_list = []
        for file_tuple in file_list:
            file_hash = getattr(coreCryptoFunctions, hash_type)(
                self, file_tuple[0])
            hashed_file_list.append((file_tuple[0], file_hash))

        # TODO: #2 insert the hashes into the database
        message_set = self._insertIntoDatabase(hashed_file_list, timestamp)
        return message_set

    def _insertIntoDatabase(
            self,
            file_list: list[str, str],
            timestamp: Timestamp) -> int:
        """Inserts the file list into the database."""
        return_code: int = -1

        session = self.get_db_session()
        try:
            # Create a new timestamp and add it to the database
            session.add(timestamp)

            # Add each file hash to the database with a foreign
            # key to the timestamp
            for file_tuple in file_list:
                file_hash = FileHash(
                    timestamp_id=timestamp.id,
                    file_path=file_tuple[0],
                    hash_type=self._hash_type,
                    file_hash=file_tuple[1]
                )
                session.add(file_hash)

            session.commit()
            return_code = 0
        except Exception as e:
            print(f"Error: {e}")
            session.rollback()
        finally:
            session.close()
            if return_code == 0:
                print("File hashes added to database.")
            else:
                print("Error adding file hashes to database.")
        return return_code


class FileTreeApp_old(QObject):
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
    _hash_type = ""
    _workingtime: str = ""

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

    def getHashType(self):
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
        """Starts a hash round."""
        print("Starting hash round...")

        self._hash_type = self.getHashType()
        self._workingtime = getCustomTimestamp()

        self.hashing_system.setHashType(self._hash_type)
        self.hashing_system.setFileList(self.FILE_LIST)

        CoreFunctions().createJobFile(
            self.FILE_LIST, self._hash_type, self._workingtime)

        self.hashing_system.firstRun()

        CoreFunctions.createJobFile(
            self.FILE_LIST, self._hash_type, self._workingtime, planned=True)
        self.onPopulateTextBrowser(self.FILE_LIST)

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


def getCustomTimestamp() -> str:
    """Returns a custom timestamp."""
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


if __name__ == "__main__":
    operating_system = os.name
    if operating_system == "nt" and sys.argv[1] != "nocheck":
        sys.exit("This script is not compatible with Windows.")
    CoreFunctions().clear_screen()
    env = setup()
    exit_code = main(sys.argv, env)

    sys.exit(exit_code)
