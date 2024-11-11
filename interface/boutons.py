import pygame

def draw_button(screen, font, text, x, y, padding=10, height=30):
    # Rendre le texte pour obtenir sa taille
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()

    # Ajuster la largeur du bouton en fonction de la largeur du texte, avec un padding
    width = text_rect.width + padding * 2
    button_rect = pygame.Rect(x, y, width, height)
    
    # Dessiner le rectangle du bouton et le texte
    pygame.draw.rect(screen, (70, 130, 180), button_rect)
    text_rect.center = button_rect.center
    screen.blit(text_surface, text_rect)
    
    # Initialiser les boutons Zoom avant de les utiliser dans la boucle principale
    button_zoom_in_rect = draw_button(screen, font, "Zoom +", 200, HAUTEUR + 10)
    button_zoom_out_rect = draw_button(screen, font, "Zoom -", 200, HAUTEUR + 50)
    
    return button_rect
