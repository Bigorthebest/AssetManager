from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QListWidget

app = QApplication()

fenetre_principale = QMainWindow()
fenetre_principale.resize(1024,468)
fenetre_principale.show()

#Widget 
widget_principale = QWidget()
fenetre_principale.setCentralWidget(widget_principale)

#Layout horizontal 
layout_principale = QHBoxLayout()
widget_principale.setLayout(layout_principale)

#Listes 
kind_list = QListWidget()
category_list = QListWidget()
assets_list = QListWidget()
file_list = QListWidget()
layout_principale.addWidget(kind_list)
layout_principale.addWidget(category_list)
layout_principale.addWidget(assets_list)
layout_principale.addWidget(file_list)

app.exec()