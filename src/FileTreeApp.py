import os
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QFileSystemModel, QTreeView


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
