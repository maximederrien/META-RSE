from magicgui import widgets
from magicgui.widgets import LineEdit, SpinBox, CheckBox, Container, ComboBox, Label
import datetime
import pandas as pd
from save import *

def init_interface():
    init = widgets.PushButton(value=True, text='Start')
    file_path = widgets.FileEdit(value="/votre_document", label="Fichier à ouvrir:")
    debut = widgets.DateEdit(value=datetime.date(1999, 12, 31), label="Date de début:")
    fin = widgets.DateEdit(value=datetime.date(2000, 2, 18), label="Date de fin:")
    save_b = widgets.Button(value=True, text='Save')
    materiels = widgets.Label(label='Liste Matériel')
    centres = widgets.Label(label='Liste Centre') 
    reseaux = widgets.Label(label='Liste Réseaux')



    widgets_list = [
        init ,
        file_path,
        debut,
        fin,
        materiels,
        centres,
        reseaux,
        save_b
    ]

    materiels = pd.DataFrame(columns=['id_centre', 'id_materiel', 'sous_id_materiel', 'consommation', 'nombre'])
    centres = pd.DataFrame(columns=['id_centre', 'nom_centre'])
    reseaux = pd.DataFrame(columns=['id_connexion', 'centre1', 'centre2','nb_de_requette'])



    save_b.clicked.connect((lambda: save(file_path.value, debut.value, fin.value, materiels, centres, reseaux)))
    init.clicked.connect((lambda : load(file_path, debut, fin, materiels, centres, reseaux)))

    container = widgets.Container(widgets=widgets_list)
    container.show(run=True)
