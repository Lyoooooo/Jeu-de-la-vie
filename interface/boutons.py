import pygame

def draw_button(screen, font, text, x, y, width=100, height=30):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (70, 130, 180), button_rect)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect
