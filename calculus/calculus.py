from classes import *
from datetime import datetime, timedelta
#start()


if __name__ == "__main__" :
    #fake scenario creation
    param = Parametre(datetime(2022, 1, 3), datetime(2025, 10, 5), True, False)
    scenar = Scenario("test 1", param, 0.5)
    
    mat_1 = Materiel(0, 0, 2, 2)
    mat_2 = Materiel(1, 0, 2, 2)
    mat_3 = Materiel(2, 1, 2, 2)

    centre_1 = Centre(1, "centre 1", [mat_1, mat_2]) 
    centre_2 = Centre(2, "centre 2", [mat_3])

    com_1 = Communication(0, centre_2, centre_1, 1000)
    com_2 = Communication(1, centre_2, centre_2, 5000)

    scenar.list_centre.append(centre_1)
    scenar.list_centre.append(centre_2)

    scenar.list_communication.append(com_1)
    scenar.list_communication.append(com_2)

    scenar.actualize()
    print(len(scenar.list_centre))
    bilan = Bilan("chemin_fichier")
    bilan.printer(scenar)


