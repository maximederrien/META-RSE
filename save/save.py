import datetime
import pandas as pd
def save(file_path, debut, fin, materiels, centres, reseaux):
    # Créer un fichier tiers (vous pouvez ajuster le chemin et le nom de fichier selon vos besoins)
    '''
    with open(file_path, "w") as f:
        f.write(f"Fichier à ouvrir: {file_path}\n")
        f.write(f"Date de début: {debut}\n")
        f.write(f"Date de fin: {fin}\n")
        f.write(f"Liste Matériel: {materiels}\n")
        f.write(f"Liste Centre: {centres}\n")
        f.write(f"Liste Réseaux: {reseaux}\n")
    '''
    materiels.to_excel(file_path+"_materiels.xlsx")
    centres.to_excel(file_path+"_centres.xlsx")
    reseaux.to_excel(file_path+"_reseaux.xlsx")
    print("saving done")
    return 0

def load(file_path, debut, fin, materiels, centres, reseaux):
    '''
    with open(file_path.value, "r") as f:
        print("i tried to load a shit")
        lines = f.readlines()

        # Mettre à jour les widgets avec les valeurs lues depuis le fichier
        debut.value = datetime.datetime.strptime(lines[1].split(":")[1].strip(), "%Y-%m-%d").date()
        fin.value = datetime.datetime.strptime(lines[2].split(":")[1].strip(), "%Y-%m-%d").date()
        materiels.label = lines[3].split(":")[1].strip()
        centres.label = lines[4].split(":")[1].strip()
        reseaux.label = lines[5].split(":")[1].strip()
    '''
    materiels = pd.read_excel(file_path+"_materiels.xlsx")
    centres = pd.read_excel(file_path+"_centres.xlsx")
    reseaux = pd.read_excel(file_path+"_reseaux.xlsx")
    return 0
