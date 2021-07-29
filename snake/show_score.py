import pygame

from settings import frame_size_y, frame_size_x, game_window


def show_score(choice, color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(str(score) + ' очков', True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)
    pygame.display.flip()
