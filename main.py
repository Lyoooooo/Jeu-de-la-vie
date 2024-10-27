import numpy as np
import pygame
from moteur_jeu.gestion_matrice import init_matrix
from moteur_jeu.evaluation import evaluate
from interface.affichage_grille import draw_matrix
from interface.boutons import draw_button
from sauvegarde.gestion_sauvegarde import save_matrix

# Initialiser pygame
pygame.init()

# Définir les dimensions de la fenêtre et des cellules
TAILLE_CELLULE = 10
TAILLE_GRILLE = 30
LARGEUR = HAUTEUR = TAILLE_GRILLE * TAILLE_CELLULE
LARGEUR_TOTALE = LARGEUR
HAUTEUR_TOTALE = HAUTEUR + 80

# Créer la fenêtre
screen = pygame.display.set_mode((LARGEUR_TOTALE, HAUTEUR_TOTALE))
pygame.display.set_caption("Jeu de la Vie avec Pause/Play et Sauvegarde")

# Couleurs
COULEUR_VIVANT = (0, 255, 0)
COULEUR_MORT = (0, 0, 0)
COULEUR_GRILLE = (40, 40, 40)
COULEUR_BOUTON = (70, 130, 180)
COULEUR_TEXTE = (255, 255, 255)

# Charger la police pour le texte
font = pygame.font.Font(None, 36)

# Initialiser la matrice
n = TAILLE_GRILLE
matrix = init_matrix(n)

# Variable de pause
paused = False

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(COULEUR_MORT)
    draw_matrix(screen, matrix, TAILLE_CELLULE, COULEUR_VIVANT, COULEUR_MORT, COULEUR_GRILLE)
    
    # Dessiner les boutons
    button_pause_rect = draw_button(screen, font, "Play" if paused else "Pause", 10, HAUTEUR + 10)
    button_save_rect = draw_button(screen, font, "Sauvegarder", 10, HAUTEUR + 50)

    pygame.display.flip()

    if not paused:
        matrix = evaluate(matrix)

    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if button_pause_rect.collidepoint(x, y):
                paused = not paused
            if button_save_rect.collidepoint(x, y):
                save_matrix(matrix)
            if y < HAUTEUR:
                n = y // TAILLE_CELLULE
                m = x // TAILLE_CELLULE
                matrix[n, m] = 1 if matrix[n, m] == 0 else 0

    clock.tick(10)

pygame.quit()
