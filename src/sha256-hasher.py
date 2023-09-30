import argparse
import platform
import sys
from types import SimpleNamespace
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
from hashlib import sha1, sha256, sha512


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FileHasher")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QVBoxLayout()
        self.main_layout.addW
        
    def open_file(self):
        file_path, file_name = QFileDialog.getOpenFileName(
            self, "Datei auswählen", "", "Alle Dateien (*)")
        if not file_path:
            return

        with open(file_path, "rb") as f:
            data = f.read()

        return data

    def copy_hash(self):
        if not env.text_edit:
            text = self.hash_value.text()
        else:
            text = self.hash_value.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)


def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text_edit', action='store_true',
                        help='Enable textEdit mode')
    parser.add_argument('--textedit', action='store_true',
                        help='Enable textEdit mode')

    args = parser.parse_args()

    glob = SimpleNamespace()
    glob.text_edit = True
    glob.text_edit = True if args.textedit else False
    print(glob.text_edit)

    return glob


if __name__ == "__main__":

    env = setup()

    print(f"textedit = {env.text_edit}")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
