import os

def save_matrix(matrix, filename=None):
    #Sauvegarder la matrice dans un fichier avec un nom personnalisé.
    if filename is None:
        filename = input("Entrez le nom de la sauvegarde: ") + ".txt"

    with open(filename, 'w') as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")
    print(f"Matrice sauvegardée dans {filename}")

