import pygame
from pygame.locals import *
from random import randint

POINTS = 0
WIDTH = 800
HEIGHT = 600
HEAD_SIZE = 50
PLAY = True
DIRECTION = (0,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen.fill("#333333") # Ставим фон

head_color = "#5c89d1"
head_x = (WIDTH-HEAD_SIZE)/2
head_y = (HEIGHT-HEAD_SIZE)/2
HEAD = Rect(head_x, head_y, HEAD_SIZE, HEAD_SIZE) # (x, y, ширина, высота)

FOOD_COLOR = "#36e485"
FOOD_SIZE = 30

def get_random_coords():
    x = randint(0, WIDTH-HEAD_SIZE)
    y = randint(0, HEIGHT-HEAD_SIZE)
    return x, y

food = pygame.draw.circle(screen, FOOD_COLOR, get_random_coords(), FOOD_SIZE)


def spawn_food():
    global POINTS
    
    if food.colliderect(HEAD):
        POINTS += 1
        print("Ам ням ням")
        food.move_ip(get_random_coords())

def handle_keys():
    global DIRECTION
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        DIRECTION = (0, -3)
    if pressed_keys[K_DOWN]:
        DIRECTION = (0, 3)
    if pressed_keys[K_LEFT]:
        DIRECTION = (-3, 0)
    if pressed_keys[K_RIGHT]:
        DIRECTION = (3, 0)

def handle_wall_touch(head):
    if head.top < 0:
        head.move_ip(0, HEIGHT)
    if head.bottom > HEIGHT:
        head.move_ip(0, -HEIGHT)
    if head.left < 0:
        head.move_ip(WIDTH, 0)
    if head.right > WIDTH:
        head.move_ip(-WIDTH, 0)

spawn_food()
while PLAY:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False
    pygame.draw.rect(screen, head_color, HEAD) # Рисуем голову
    HEAD.move_ip(DIRECTION)
    handle_wall_touch(HEAD)
    handle_keys()

    pygame.display.flip() # Отображаем изменения на экране
    clock.tick(60) # Максимальный FPS



pygame.quit()
