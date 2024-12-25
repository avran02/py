import pygame
from pygame.locals import *

HEIGHT = 600
WIDTH = 800
RUNNING = True
BACKGROUND_COLOR = "#666666"
HEAD_COLOR = "#e84adb"
HEAD_SIZE = 50
DIRECTION = (2, 0)
HEAD = Rect(WIDTH/2-HEAD_SIZE/2, HEIGHT/2-HEAD_SIZE/2, HEAD_SIZE, HEAD_SIZE)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def handle_keys():
    global DIRECTION
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        DIRECTION = (0, -2)
    if pressed_keys[K_DOWN]:
        DIRECTION = (0, 2)
    if pressed_keys[K_LEFT]:
        DIRECTION = (-2, 0)
    if pressed_keys[K_RIGHT]:
        DIRECTION = (2, 0)
    if pressed_keys[K_w]:
        DIRECTION = (0, -2)
    if pressed_keys[K_s]:
        DIRECTION = (0, 2)
    if pressed_keys[K_a]:
        DIRECTION = (-2, 0)
    if pressed_keys[K_d]:
        DIRECTION = (2, 0)

while RUNNING:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    # Ставим фон
    screen.fill(BACKGROUND_COLOR)

    # Куда рисовать, Какого цвета, что рисовать
    pygame.draw.rect(screen, HEAD_COLOR, HEAD)

    if HEAD.left < 0:
        HEAD.move_ip(WIDTH, 0)
    if HEAD.right > WIDTH:
        HEAD.move_ip(-WIDTH, 0)
    if HEAD.bottom > HEIGHT:
        HEAD.move_ip(0, -HEIGHT)
    if HEAD.top < 0:
        HEAD.move_ip(0, HEIGHT)
    
    handle_keys()
    HEAD.move_ip(DIRECTION)

    # Отображаем изменения на экране
    pygame.display.flip()

    # Максимальный FPS
    clock.tick(60)
pygame.quit()



