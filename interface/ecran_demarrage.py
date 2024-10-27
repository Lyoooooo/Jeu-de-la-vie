import pygame
from interface.boutons import draw_button
from sauvegarde.sauvegarde import save_matrix
from sauvegarde.chargement import list_saves

COULEUR_MORT = (0, 0, 0)
COULEUR_TEXTE = (255, 255, 255)

def start_screen(screen, largeur, hauteur, font):
    screen.fill(COULEUR_MORT)
    title_text = font.render("Bienvenue dans le Jeu de la Vie", True, COULEUR_TEXTE)
    screen.blit(title_text, (largeur // 2 - title_text.get_width() // 2, hauteur // 4))

    button_new_game = draw_button(screen, font, "Nouvelle Partie", largeur // 2 - 100, hauteur // 2)
    button_load_game = draw_button(screen, font, "Charger Partie", largeur // 2 - 100, hauteur // 2 + 50)
    pygame.display.flip()
    
    return button_new_game, button_load_game

def select_save_screen(screen, largeur, hauteur, font):
    saves = list_saves()
    if not saves:
        screen.fill(COULEUR_MORT)
        no_save_text = font.render("Aucune sauvegarde trouvée.", True, COULEUR_TEXTE)
        screen.blit(no_save_text, (largeur // 2 - no_save_text.get_width() // 2, hauteur // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        return None

    screen.fill(COULEUR_MORT)
    save_text = font.render("Sélectionnez une sauvegarde :", True, COULEUR_TEXTE)
    screen.blit(save_text, (largeur // 2 - save_text.get_width() // 2, hauteur // 4))

    buttons = []
    for i, save in enumerate(saves):
        button = draw_button(screen, font, save, largeur // 2 - 100, hauteur // 2 + i * 40)
        buttons.append((button, save))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button, filename in buttons:
                    if button.collidepoint(event.pos):
                        return filename

def save_game_screen(screen, largeur, hauteur, font, matrix):
    input_text = ""
    running = True
    while running:
        screen.fill(COULEUR_MORT)
        instruction_text = font.render("Entrez le nom de la sauvegarde :", True, COULEUR_TEXTE)
        screen.blit(instruction_text, (largeur // 2 - instruction_text.get_width() // 2, hauteur // 4))

        text_surface = font.render(input_text, True, COULEUR_TEXTE)
        pygame.draw.rect(screen, COULEUR_TEXTE, (largeur // 2 - 100, hauteur // 2, 200, 40), 2)
        screen.blit(text_surface, (largeur // 2 - text_surface.get_width() // 2, hauteur // 2 + 5))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_text:
                    save_matrix(matrix, filename=input_text + ".txt")
                    return input_text + ".txt"
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

def confirmation_screen(screen, largeur, hauteur, font):
    
    #Affiche un écran de confirmation après la sauvegarde pour permettre de revenir ou quitter.
    
    screen.fill(COULEUR_MORT)
    message_text = font.render("Sauvegarde réussie !", True, COULEUR_TEXTE)
    screen.blit(message_text, (largeur // 2 - message_text.get_width() // 2, hauteur // 3))

    button_return = draw_button(screen, font, "Retourner à la partie", largeur // 2 - 100, hauteur // 2)
    button_menu = draw_button(screen, font, "Quitter vers le menu", largeur // 2 - 100, hauteur // 2 + 50)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_return.collidepoint(event.pos):
                    return "return"
                elif button_menu.collidepoint(event.pos):
                    return "menu"
