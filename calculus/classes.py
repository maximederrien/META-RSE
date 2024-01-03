from datetime import datetime, timedelta
import matplotlib.pyplot as plt

DELTA = timedelta(hours = 1) #dela of one hour

class Centre :
    def __init__(self, id_centre, name, mat_list):
        self.id_centre = id_centre
        self.name = name
        self.mat_list = mat_list.copy()
        self.bilan_graph = {"date" : [] , "value" : []}

    def create_bilan(self, date_debut, date_fin):
        date_actu = date_debut
        while (date_actu < date_fin) :
            date_actu += DELTA
            self.bilan_graph["date"].append(date_actu)
            conso_score = 0
            for materiel in self.mat_list :
                conso_score += materiel.get_cost(date_actu)
            self.bilan_graph["value"].append(conso_score)



class Materiel :
    def __init__(self,id_mat, id_centre, id_materiel, sous_id_materiel):
        self.id = id_mat
        self.id_centre = id_centre
        self.id_materiel = id_materiel
        self.sous_id_materiel = sous_id_materiel
        self.crea_cost = 0
        self.end_cost = 0
        
    def get_cost(self, date) :
        #not finished
        return 1

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
        self.nom = nom_scenario
        self.list_centre = []
        self.list_communication = []
        self.parametre = parametre
        self.kwTOco2 = kwTOco2

    def actualize(self):
        for centre in self.list_centre :
            centre.create_bilan(self.parametre.date_debut,self.parametre.date_fin)
        #TODO miss part for communication

class Bilan :
    def __init__(self, chemin_fichier) :
        self.chemin_fichier = chemin_fichier

    def printer(self, scenario):
        plt.title(scenario.nom)
        plt.legend(title = "impacte environemental du système")
        for centre in scenario.list_centre :
            plt.plot(centre.bilan_graph["date"], centre.bilan_graph["value"], color = 'red', label = str(centre.id_centre))
        plt.show()

    def writer(self, scenario):
        print("bilan writer func")



