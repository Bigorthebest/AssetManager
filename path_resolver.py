asset_name = "Juno"
asset_kind = "character"
asset_category = "animal"
file_type = "model"
file_extension = "ma"
file_version = 1 


def get_file_path(name,kind,catergory,type,extension,version,suffix = None):
    """Fonction qui va retourner le bon path avec les informations de l'assets en param"""
    file_version_padded = str(version).zfill(3)
    if suffix == None :
        template_path = f"{kind}/{catergory}/{name}/{catergory}__{name}__{file_version_padded}.{extension}"
    else :
        template_path = f"{kind}/{catergory}/{name}/{catergory}__{name}__{file_version_padded}__{suffix}.{extension}"

    return template_path


if __name__ == "__main__" :
    chemin_fichier = get_file_path(asset_name,asset_kind,asset_category,file_type,file_extension,file_version)
    print(f"Le chemin généré est : {chemin_fichier}")
    chemin_fichier_normalmap = get_file_path(asset_name,asset_kind,asset_category,file_type,file_extension,file_version,"normal")
    print(f"Chemin de la normal map est {chemin_fichier_normalmap}")