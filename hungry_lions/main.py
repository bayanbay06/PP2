import sys
import random
import time

import pygame

x = 50
y = 50
width = 720
height = 480
speed = 10
score = 0
food_spawn, enemy_spawn = False, False
eat_elem, enemy_pos_i = 0, 0

pygame.display.set_caption('Hungry Lions')
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 32)
food_pos = [[random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10] for _ in range(20)]
enemy_pos = [[random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10] for _ in range(20)]


def show_score(choice, color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(str(score) + ' очков', True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (width / 10, 15)
    else:
        score_rect.midtop = (width / 2, height / 1.25)
    screen.blit(score_surface, score_rect)
    pygame.display.flip()


if __name__ == '__main__':
    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        mx = enemy_pos[0][1]
        for i in enemy_pos:
            if mx < i[1]:
                mx = i[1]
        import pdb

        pdb.set_trace()
        for i, enemy in enumerate(enemy_pos):
            if x == enemy[0] and y == enemy[1]:
                print("enemy")
                score -= 1
                enemy_spawn = False
                enemy_pos_i = i

            enemy[1] += 1

        for i, food in enumerate(food_pos):
            if x == food[0] and y == food[1]:
                print("eating")
                score += 1
                food_spawn = False
                eat_elem = i

        if not enemy_spawn:
            enemy_pos[enemy_pos_i] = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        enemy_spawn = True
        if not food_spawn:
            food_pos[eat_elem] = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawn = True

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 255), (x, y, 10, 10))
        for element in food_pos:
            pygame.draw.rect(screen,
                             pygame.Color(0, 255, 0),
                             pygame.Rect(element[0], element[1], 15, 15))
        for element in enemy_pos:
            pygame.draw.rect(screen,
                             pygame.Color(255, 0, 0),
                             pygame.Rect(element[0], element[1], 15, 15))
        show_score(1, pygame.Color(255, 255, 255), 'consolas', 20, score)
        pygame.display.update()
