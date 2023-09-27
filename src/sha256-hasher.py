import argparse
import platform
import sys
from types import SimpleNamespace
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
from hashlib import sha256


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SHA256-Hasher")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.file_label = QLabel("Datei auswählen")
        self.file_button = QPushButton("Datei öffnen")
        self.hash_label = QLabel("SHA256-Hash")
        if not env.text_edit:
            self.hash_value = QLabel("Hash Wert...")
        else:
            self.hash_value = QTextEdit("Hash Wert...")
        self.hash_copy_button = QPushButton("Hash kopieren")

        self.file_label.setAlignment(Qt.AlignLeft)
        self.hash_label.setAlignment(Qt.AlignLeft)

        self.layout = QVBoxLayout()

        self.upper_layout = QHBoxLayout()
        self.upper_layout.addWidget(self.file_label)
        self.upper_layout.addWidget(self.file_button)

        self.lower_layout = QVBoxLayout()
        self.inner_lower_layout = QHBoxLayout()
        self.inner_lower_layout.addWidget(self.hash_label)
        self.inner_lower_layout.addWidget(self.hash_value)
        self.lower_layout.addLayout(self.inner_lower_layout)
        self.lower_layout.addWidget(self.hash_copy_button)

        self.layout.addLayout(self.upper_layout)
        self.layout.addLayout(self.lower_layout)

        self.central_widget.setLayout(self.layout)

        self.file_button.clicked.connect(self.open_file)
        self.hash_copy_button.clicked.connect(self.copy_hash)

    def open_file(self):
        file_path, file_name = QFileDialog.getOpenFileName(
            self, "Datei auswählen", "", "Alle Dateien (*)")
        if not file_path:
            return

        with open(file_path, "rb") as f:
            data = f.read()

        hash_value = sha256(data).hexdigest()
        self.hash_value.setText(hash_value)

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
