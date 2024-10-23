import numpy as np
import pygame

# Initialiser pygame
pygame.init()

# Définir les dimensions de la fenêtre et des cellules
TAILLE_CELLULE = 10
TAILLE_GRILLE = 30  # Taille de la grille (30x30)
LARGEUR = HAUTEUR = TAILLE_GRILLE * TAILLE_CELLULE
LARGEUR_TOTALE = LARGEUR
HAUTEUR_TOTALE = HAUTEUR + 80  # Espace pour deux boutons

# Créer la fenêtre
screen = pygame.display.set_mode((LARGEUR_TOTALE, HAUTEUR_TOTALE))
pygame.display.set_caption("Jeu de la Vie avec Pause/Play et Sauvegarde")

# Couleurs
COULEUR_VIVANT = (0, 255, 0)  # Vert
COULEUR_MORT = (0, 0, 0)      # Noir
COULEUR_GRILLE = (40, 40, 40)  # Gris
COULEUR_BOUTON = (70, 130, 180)  # Bleu clair
COULEUR_TEXTE = (255, 255, 255)  # Blanc

# Charger la police pour le texte
font = pygame.font.Font(None, 36)

def init_matrix(taille):
    return np.zeros((taille, taille), dtype=int)

def find_neighbors(matrix, n, m):
    neighbors = []
    rows, cols = matrix.shape
    
    # Parcourir les voisins dans les 8 directions
    for i in range(max(0, n-1), min(n+2, rows)):
        for j in range(max(0, m-1), min(m+2, cols)):
            if i == n and j == m:
                continue  # Ne pas inclure l'élément central
            neighbors.append(matrix[i][j])
    
    return neighbors

def evaluate_dead(matrix, n, m):
    neighbors = find_neighbors(matrix, n, m)
    return 1 if np.sum(neighbors) == 3 else 0

def evaluate_alive(matrix, n, m):
    neighbors = find_neighbors(matrix, n, m)
    return 1 if np.sum(neighbors) in [2, 3] else 0

def evaluate(matrix):
    rows, cols = matrix.shape
    new_matrix = np.copy(matrix)  # Créer une copie de la matrice originale
    
    # Parcourir les indices de la matrice
    for n in range(rows):
        for m in range(cols):
            cell = matrix[n, m]
            if cell == 1:
                new_matrix[n, m] = evaluate_alive(matrix, n, m)
            else:
                new_matrix[n, m] = evaluate_dead(matrix, n, m)
    
    return new_matrix

def draw_grid():
    for x in range(0, LARGEUR, TAILLE_CELLULE):
        pygame.draw.line(screen, COULEUR_GRILLE, (x, 0), (x, HAUTEUR))
    for y in range(0, HAUTEUR, TAILLE_CELLULE):
        pygame.draw.line(screen, COULEUR_GRILLE, (0, y), (LARGEUR, y))

def draw_matrix(matrix):
    rows, cols = matrix.shape
    for n in range(rows):
        for m in range(cols):
            rect = pygame.Rect(m * TAILLE_CELLULE, n * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE)
            if matrix[n, m] == 1:
                pygame.draw.rect(screen, COULEUR_VIVANT, rect)
            else:
                pygame.draw.rect(screen, COULEUR_MORT, rect)
    draw_grid()

def draw_button(text, x, y, width=100, height=30):
    # Dessiner le bouton
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, COULEUR_BOUTON, button_rect)
    
    # Texte du bouton
    text_surface = font.render(text, True, COULEUR_TEXTE)
    
    # Centrer le texte sur le bouton
    text_rect = text_surface.get_rect(center=button_rect.center)
    
    # Dessiner le texte
    screen.blit(text_surface, text_rect)
    
    return button_rect

def save_matrix(matrix, filename="matrix_save.txt"):
    """Sauvegarder la matrice dans un fichier texte"""
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")
    print(f"Matrice sauvegardée dans {filename}")

# Initialiser la matrice
n = TAILLE_GRILLE
matrix = init_matrix(n)

# Variable de pause
paused = False

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(COULEUR_MORT)  # Effacer l'écran à chaque itération
    draw_matrix(matrix)        # Dessiner la matrice actuelle

    # Dessiner les boutons
    button_pause_rect = draw_button("Play" if paused else "Pause", 10, HAUTEUR + 10)
    button_save_rect = draw_button("Sauvegarder", 10, HAUTEUR + 50)

    pygame.display.flip()  # Mettre à jour l'affichage

    # Si le jeu n'est pas en pause, calculer la prochaine génération
    if not paused:
        matrix = evaluate(matrix)

    # Gérer les événements de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Détecter les clics de souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()  # Obtenir la position du clic

            # Si le clic est dans la zone du bouton Pause/Play, basculer l'état
            if button_pause_rect.collidepoint(x, y):
                paused = not paused

            # Si le clic est dans la zone du bouton Sauvegarder, sauvegarder la matrice
            if button_save_rect.collidepoint(x, y):
                save_matrix(matrix)

            # Convertir les coordonnées en indices de matrice pour les cellules
            if y < HAUTEUR:  # S'assurer que le clic est dans la grille, pas sur les boutons
                n = y // TAILLE_CELLULE
                m = x // TAILLE_CELLULE
                # Changer l'état de la cellule (vivante/morte)
                matrix[n, m] = 1 if matrix[n, m] == 0 else 0

    # Limiter la vitesse de l'animation
    clock.tick(10)  # 10 itérations par seconde

# Quitter pygame proprement
pygame.quit()
