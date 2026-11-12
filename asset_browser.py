from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QListWidget, QPushButton
from lists_function import get_asset_files, get_category_assets,get_kind_categories,get_project_kinds

class AssetBrowserApp : 
    def __init__(self):
        print("Activation de l'assets Browser")
        self.path_project = "D:/Python PROJ/AssetManager/Projet/"
        self.app = QApplication()

        self.fenetre_principale = QMainWindow()
        self.fenetre_principale.resize(1024,468)
        self.fenetre_principale.setWindowTitle("Assets Browser")

        #Widget 
        self.widget_principale = QWidget()
        self.fenetre_principale.setCentralWidget(self.widget_principale)

        #Layout horizontal 
        self.layout_principale = QHBoxLayout()
        self.widget_principale.setLayout(self.layout_principale)

        #Listes 
        kind_list = QListWidget()
        category_list = QListWidget()
        assets_list = QListWidget()
        file_list = QListWidget()
        self.layout_principale.addWidget(kind_list)
        self.layout_principale.addWidget(category_list)
        self.layout_principale.addWidget(assets_list)
        self.layout_principale.addWidget(file_list)

    def __del__(self):
        print("Merc d'avoir utilisé l'assets browser")

    def afficher_fenetre(self):
        self.fenetre_principale.show()

    def update_list(self): 
        get_project_kinds(self.path_project)
        

    
asset_browser_app = AssetBrowserApp()
asset_browser_app.afficher_fenetre()
asset_browser_app.app.exec()