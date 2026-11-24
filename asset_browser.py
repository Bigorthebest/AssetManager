from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QListWidget
from PySide6.QtGui import QIcon
from lists_function import get_project_kinds, get_kind_categories, get_category_assets, get_asset_files

PROJECT_PATH = "D:\\Python PROJ\\_Exemple_projet"

class AssetBrowserApp : 
    def __init__(self, project_path):
        print("Activation de l'assets Browser")
        self.app = QApplication()
        self.project_path = project_path

        self.fenetre_principale = QMainWindow()
        self.fenetre_principale.resize(1024,468)
        self.fenetre_principale.setWindowTitle("Assets Browser")
        self.fenetre_principale.setWindowIcon(QIcon(".\\icon\\Floral.ico"))

        #Widget 
        self.widget_principale = QWidget()
        self.fenetre_principale.setCentralWidget(self.widget_principale)

        #Layout horizontal 
        self.layout_principale = QHBoxLayout()
        self.widget_principale.setLayout(self.layout_principale)

        #Listes 
        self.kind_list = QListWidget()
        self.category_list = QListWidget()
        self.assets_list = QListWidget()
        self.file_list = QListWidget()
        self.layout_principale.addWidget(self.kind_list)
        self.layout_principale.addWidget(self.category_list)
        self.layout_principale.addWidget(self.assets_list)
        self.layout_principale.addWidget(self.file_list)

        #Connection 
        self.kind_list.itemClicked.connect(self.quandCliqueSurKind)
        self.category_list.itemClicked.connect(self.quandCliqueSurCategorie)
        self.assets_list.itemClicked.connect(self.quandCliqueSurAsset)
        self.file_list.itemClicked.connect(self.quandCliqueSurFile)

    def __del__(self):
        print("Merc d'avoir utilisé l'assets browser")

    def afficher_fenetre(self):
        self.refresh_kind_list()
        self.fenetre_principale.show()

    def refresh_kind_list(self): 
        self.kind_list.clear()
        kinds = get_project_kinds(self.project_path)
        self.kind_list.addItems(kinds)

    def refresh_categories_list(self):
        self.category_list.clear()
        selecteds_kind_items = self.kind_list.selectedItems()
        if selecteds_kind_items :
            selected_kind_name = selecteds_kind_items[0].text()
            categories = get_kind_categories(self.project_path,selected_kind_name)
            self.category_list.addItems(categories)

    def refresh_assets_list(self): 
        self.assets_list.clear()
        selected_kind_items = self.kind_list.selectedItems()
        selected_category_items = self.category_list.selectedItems()
        if selected_category_items and selected_kind_items:
            selected_kind_name = selected_kind_items[0].text()
            selected_category_name = selected_category_items[0].text()
            assets = get_category_assets(self.project_path,selected_kind_name,selected_category_name)
            self.assets_list.addItems(assets)

    def refresh_files_list(self): 
        self.file_list.clear()
        selected_kind_items = self.kind_list.selectedItems()
        selected_category_items = self.category_list.selectedItems()
        selected_assets_items = self.assets_list.selectedItems()
        if selected_kind_items and selected_category_items and selected_assets_items :
            selected_kind_name = selected_kind_items[0].text()
            selected_category_name = selected_category_items[0].text()
            selected_assets_name = selected_assets_items[0].text()
            files = get_asset_files(self.project_path,selected_kind_name,selected_category_name,selected_assets_name)
            self.file_list.addItems(files)

    def quandCliqueSurKind(self): 
        self.category_list.clear()
        self.refresh_categories_list()
        self.assets_list.clear()
        self.refresh_assets_list()
        self.file_list.clear()
        self.refresh_files_list()

    def quandCliqueSurCategorie(self): 
        self.assets_list.clear()
        self.refresh_assets_list()
        self.file_list.clear()
        self.refresh_files_list()

    def quandCliqueSurAsset(self): 
        self.file_list.clear()
        self.refresh_files_list()

    def quandCliqueSurFile(self): 
        pass 

    
asset_browser_app = AssetBrowserApp(PROJECT_PATH)
asset_browser_app.afficher_fenetre()
asset_browser_app.app.exec()