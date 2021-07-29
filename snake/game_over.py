import sys
import time

import pygame

from settings import red, frame_size_y, frame_size_x, black, game_window
from show_score import show_score


def game_over(score):
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Вы проиграли', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20, score)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()
