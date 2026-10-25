from path_resolver import get_file_path
from shutil import copyfile
import os 

path_du_projet = "D:/MonSuperProjet/"

template_collection = {
    "blend": "D:/Python PROJ/AssetManager/_templates/model.blend",
    "png": "/_templates/texture.png",
    "psd": "/_templates/texture.psd",
    "tif": "/_templates/texture.tif",
    "nk": "/_templates/compo.nk",
}

def create_file_path(name,kind,catergory,type,extension,version = 1,suffix = None):
    """Fonction permettant de créer un fichier composant un asset en fonction des paramètre donnée"""
    #Création et verification des chemins de fichier
    new_asset_file_path = get_file_path(name,kind,catergory,type,extension,version,suffix)
    parent_directory = os.path.dirname(new_asset_file_path)
    os.makedirs(parent_directory, exist_ok=True)
    #Création du template objets
    template_path = template_collection[extension] #Vulnérabilité
    copyfile(template_path,new_asset_file_path)

if __name__ == "__main__" :
    print("Debut prog")
    create_file_path('Juno','character','animal','model','blend')
    print("Fin du programme create_asset.py")