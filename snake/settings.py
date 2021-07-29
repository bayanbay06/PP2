import pygame

difficulty = 25
frame_size_x = 720
frame_size_y = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

snake_pos = [100, 50]
snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
score = 0
