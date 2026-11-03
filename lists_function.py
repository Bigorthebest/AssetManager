import os 


path = "D:/Python PROJ/AssetManager/"

def get_project_kinds(project_path) : 
    """lister les répertoires des différents kinds, prend le chemin vers le dit projet"""
    kinds_filtered_list = []

    kinds_list = os.listdir(project_path)
    for file in kinds_list : 
        if os.path.isdir(f"{project_path}/{file}") == True and file.startswith(".") == False:
            kinds_filtered_list.append(file)
            
    return kinds_filtered_list

def get_kind_categories(project_path, kind):
    categorie__filtered_list = []

    categorie_list = os.listdir(f"{project_path}/{kind}")
    for file in categorie_list :
        if os.path.isdir(f"{project_path}/{kind}/{file}") == True and file.startswith(".") == False:
            categorie__filtered_list.append(file)
            
    return categorie__filtered_list

def get_category_assets(project_path, kind, category):
    assets__filtered_list = []

    assets_list = os.listdir(f"{project_path}/{kind}/{category}")
    for file in assets_list :
        if os.path.isdir(f"{project_path}/{kind}/{category}/{file}") == True and file.startswith(".") == False:
            assets__filtered_list.append(file)
    return assets__filtered_list

def get_asset_files(project_path, kind, category, asset_name):
    file_filtered_list = []

    file_list = os.listdir(f"{project_path}/{kind}/{category}/{asset_name}")
    for file in file_list :
        if os.path.isfile(f"{project_path}/{kind}/{category}/{asset_name}/{file}") and file.startswith(".") == False:
            file_filtered_list.append(file)

    return file_filtered_list

if __name__ == "__main__" : 
    pass