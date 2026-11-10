from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QListWidget


class AssetBrowserApp : 
    def __init__(self):
        print("Activation de l'assets Browser")
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


    
asset_browser_app = AssetBrowserApp()
asset_browser_app.afficher_fenetre()
asset_browser_app.app.exec()