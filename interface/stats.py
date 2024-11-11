import pygame

def draw_value(screen, titre, text, x, y):

    font = pygame.font.Font(None, 20)

    # Rendre le texte pour obtenir sa taille
    text_surface = font.render(titre + "" + str(text), True, (255, 255, 255))
    text_rect = text_surface.get_rect()

    # Positionner le texte aux coordonnées spécifiées
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

