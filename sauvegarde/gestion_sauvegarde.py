def save_matrix(matrix, filename="matrix_save.txt"):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")
    print(f"Matrice sauvegardée dans {filename}")
