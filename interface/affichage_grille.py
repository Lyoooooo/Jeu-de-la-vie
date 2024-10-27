import pygame

def draw_grid(screen, largeur, hauteur, taille_cellule, couleur_grille):
    for x in range(0, largeur, taille_cellule):
        pygame.draw.line(screen, couleur_grille, (x, 0), (x, hauteur))
    for y in range(0, hauteur, taille_cellule):
        pygame.draw.line(screen, couleur_grille, (0, y), (largeur, y))

def draw_matrix(screen, matrix, taille_cellule, couleur_vivant, couleur_mort, couleur_grille):
    rows, cols = matrix.shape
    for n in range(rows):
        for m in range(cols):
            rect = pygame.Rect(m * taille_cellule, n * taille_cellule, taille_cellule, taille_cellule)
            if matrix[n, m] == 1:
                pygame.draw.rect(screen, couleur_vivant, rect)
            else:
                pygame.draw.rect(screen, couleur_mort, rect)
    draw_grid(screen, rows * taille_cellule, cols * taille_cellule, taille_cellule, couleur_grille)
