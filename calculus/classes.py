NBR_CENTER = 0
NBR_MATERIEL = 0

class Centre :
    def __init__(self, name, mat_list):
        self.id_centre = NBR_CENTER
        ID_CENTER +=1
        self.name = name
        self.mat_list = mat_list.copy()
        bilan_graph = [[][]]


class Materiel :
    def __init__(self):
        self.id = NBR_MATERIEL
        NBR_MATERIEL +=1
        self.id_centre = id_centre
        self.id_materiel = id_materiel
        self.sous_id_materiel = sous_id_materiel
        #not finished

class Communication :
    def __init__(self, id_com, centre_1, centre_2, requettes) :
        self.id_com = id_com
        self.centre_1 = centre_1
        self.centre_2 = centre_2
        self.requettes = requettes

class Parametre :
    def __init__(self, date_debut, date_fin, bilan_print, bilan_fichier) :
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.bilan_print = bilan_print
        self.bilan_fichier = bilan_fichier

class Scenario :
    def __init__(self, nom_scenario, parametre, kwTOco2):
        self.list_centre = []
        self.list_communication = []
        self.parametre = parametre
        self.kwTOco2 = kwTOco2

class Bilan :
    def __init__(self, chemin_fichier) :
        self.chemin_fichier = chemin_fichier

    def printer(self):
        print("bilan printer func")

    def writer(self):
        print("bilan writer func")



