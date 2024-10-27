import numpy as np
import pygame
from moteur_jeu.gestion_matrice import init_matrix
from moteur_jeu.evaluation import evaluate
from interface.affichage_grille import draw_matrix
from interface.boutons import draw_button
from interface.ecran_demarrage import start_screen, select_save_screen, save_game_screen, confirmation_screen
from sauvegarde.chargement import load_matrix, list_saves
from sauvegarde.sauvegarde import save_matrix

# Initialiser pygame
pygame.init()

# Dimensions de la fenêtre et des cellules
TAILLE_CELLULE = 10  # Taille de chaque cellule dans la grille
TAILLE_GRILLE = 30  # Nombre de cellules par côté
LARGEUR = HAUTEUR = TAILLE_GRILLE * TAILLE_CELLULE *1.5 # Taille de la grille
LARGEUR_TOTALE = LARGEUR  # Largeur totale de la fenêtre
HAUTEUR_TOTALE = HAUTEUR + 100  # Hauteur totale de la fenêtre avec espace pour les boutons

# Créer la fenêtre du jeu
screen = pygame.display.set_mode((LARGEUR_TOTALE, HAUTEUR_TOTALE))
pygame.display.set_caption("Jeu de la Vie")

# Définition des couleurs et de la police
COULEUR_VIVANT = (0, 255, 0)  # Couleur pour les cellules vivantes
COULEUR_MORT = (0, 0, 0)  # Couleur pour les cellules mortes
COULEUR_GRILLE = (40, 40, 40)  # Couleur des lignes de la grille
font = pygame.font.Font(None, 36)  # Police pour les textes

def main_game_loop(matrix, save_filename=None):
    
    #Boucle principale du jeu de la vie.
    #Si save_filename est fourni, le jeu sauvegarde directement dans ce fichier lors de l'utilisation du bouton Sauvegarder.
    
    paused = False  # Variable pour contrôler la pause du jeu
    running = True  # Variable pour contrôler la boucle principale du jeu
    clock = pygame.time.Clock()  # Objet pour contrôler la vitesse d'exécution

    while running:
        # Remplir l'arrière-plan de la fenêtre
        screen.fill(COULEUR_MORT)
        
        # Afficher la grille de jeu
        draw_matrix(screen, matrix, TAILLE_CELLULE, COULEUR_VIVANT, COULEUR_MORT, COULEUR_GRILLE)
        
        # Afficher les boutons Pause/Play et Sauvegarder
        button_pause_rect = draw_button(screen, font, "Play" if paused else "Pause", 10, HAUTEUR + 10)
        button_save_rect = draw_button(screen, font, "Sauvegarder", 10, HAUTEUR + 50)
        
        # Mettre à jour l'affichage
        pygame.display.flip()

        # Si le jeu n'est pas en pause, évaluer la prochaine génération de la matrice
        if not paused:
            matrix = evaluate(matrix)

        # Gérer les événements utilisateur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quitter le jeu si l'utilisateur ferme la fenêtre
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Gérer les clics de souris
                x, y = pygame.mouse.get_pos()
                if button_pause_rect.collidepoint(x, y):
                    # Basculer l'état de pause si on clique sur le bouton Pause/Play
                    paused = not paused
                elif button_save_rect.collidepoint(x, y):
                    # Sauvegarder la partie
                    if save_filename:
                        # Si un fichier de sauvegarde est déjà défini (partie chargée), sauvegarder directement
                        save_matrix(matrix, filename=save_filename)
                    else:
                        # Sinon, demander un nom pour la sauvegarde (nouvelle partie)
                        save_filename = save_game_screen(screen, LARGEUR, HAUTEUR, font, matrix)
                    
                    # Afficher l'écran de confirmation après la sauvegarde
                    choice = confirmation_screen(screen, LARGEUR, HAUTEUR, font)
                    if choice == "menu":
                        # Retourner au menu principal si l'utilisateur le souhaite
                        return
                elif y < HAUTEUR:
                    # Permet à l'utilisateur de cliquer sur une cellule pour la rendre vivante ou morte
                    n = y // TAILLE_CELLULE
                    m = x // TAILLE_CELLULE
                    matrix[n, m] = 1 if matrix[n, m] == 0 else 0

        # Limiter la vitesse de la boucle
        clock.tick(10)

# Boucle du menu principal
while True:
    # Afficher l'écran de démarrage avec les options Nouvelle Partie et Charger Partie
    button_new_game, button_load_game = start_screen(screen, LARGEUR, HAUTEUR, font)
    selected_matrix = None  # Initialisation de la matrice sélectionnée

    # Boucle pour gérer les événements dans le menu principal
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quitter le jeu si l'utilisateur ferme la fenêtre
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Gérer les clics de souris
                if button_new_game.collidepoint(event.pos):
                    # Si Nouvelle Partie est sélectionnée
                    selected_matrix = init_matrix(TAILLE_GRILLE)
                    main_game_loop(selected_matrix)  # Lancer la boucle de jeu
                    menu_running = False  # Sortir de la boucle de menu pour revenir au jeu
                elif button_load_game.collidepoint(event.pos):
                    # Si Charger Partie est sélectionnée
                    filename = select_save_screen(screen, LARGEUR, HAUTEUR, font)
                    if filename:
                        # Charger la matrice depuis le fichier sélectionné
                        selected_matrix = load_matrix(filename)
                        main_game_loop(selected_matrix, save_filename=filename)  # Lancer le jeu avec sauvegarde directe
                        menu_running = False  # Sortir de la boucle de menu pour revenir au jeu
        # Mettre à jour l'affichage du menu principal
        pygame.display.flip()
