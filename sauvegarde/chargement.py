import numpy as np
import os

def load_matrix(filename):

  #  Charger une matrice depuis un fichier.
   
    if not os.path.exists(filename):
        print(f"Erreur : Le fichier {filename} n'existe pas.")
        return None

    with open(filename, 'r') as f:
        lines = f.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
    
    print(f"Matrice chargée depuis {filename}")
    return np.array(matrix)

def list_saves():
    
   # Liste tous les fichiers de sauvegarde disponibles dans le répertoire actuel.
    
    saves = [f for f in os.listdir() if f.endswith(".txt")]
    if not saves:
        print("Aucune sauvegarde trouvée.")
    else:
        print("Sauvegardes disponibles :")
        for i, save in enumerate(saves, 1):
            print(f"{i}. {save}")
    return saves

def select_save():
    
    #Permet à l'utilisateur de sélectionner une sauvegarde à charger.
    
    saves = list_saves()
    if not saves:
        return None

    choice = input("Entrez le numéro de la sauvegarde que vous souhaitez charger : ")
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(saves):
            return saves[choice_index]
        else:
            print("Numéro invalide.")
            return None
    except ValueError:
        print("Entrée invalide.")
        return None
