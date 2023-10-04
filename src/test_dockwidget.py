"""
    This is just a test file for QDockWidget
    to show it's functionality.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDockWidget Test")

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.dock = QDockWidget("Dock", self)
        self.dock.setAllowedAreas(
            Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        self.setupDockWidget()
        
    def setupDockWidget(self):
        self.dock_text_edit = QTextEdit()
        self.dock_text_edit.setReadOnly(True)
        self.dock_text_edit.setText("Dock Text Edit")
        
        self.dock.setWidget(self.dock_text_edit)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())