from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

app = QApplication([])

tree = QTreeWidget()
tree.setColumnCount(1)
tree.setHeaderLabels(["Symbol Categories"])

# Create root items
root1 = QTreeWidgetItem(tree, ["Shapes"])
root2 = QTreeWidgetItem(tree, ["Letters"])

# Create child items under root1
child1 = QTreeWidgetItem(root1, ["Circle"])
child2 = QTreeWidgetItem(root1, ["Square"])
child3 = QTreeWidgetItem(root1, ["Triangle"])

# Create child items under root2
child4 = QTreeWidgetItem(root2, ["A"])
child5 = QTreeWidgetItem(root2, ["B"])

# Show the tree
tree.show()

app.exec_()
