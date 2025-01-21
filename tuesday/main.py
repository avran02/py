import pygame
from pygame.locals import *
from utils import get_random_coords

SPEED = 3
POINTS = 0
WIDTH = 800
HEIGHT = 600
HEAD_SIZE = 50
PLAY = True
DIRECTION = (0,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

head_color = "#5c89d1"
head_x = (WIDTH-HEAD_SIZE)/2
head_y = (HEIGHT-HEAD_SIZE)/2
HEAD = Rect(head_x, head_y, HEAD_SIZE, HEAD_SIZE) # (x, y, ширина, высота)

FOOD_COLOR = "#36e485"
FOOD_SIZE = 30
FOOD_POS = get_random_coords(WIDTH, HEIGHT, HEAD_SIZE)
FOOD = pygame.draw.circle(screen, FOOD_COLOR, FOOD_POS, FOOD_SIZE)    

def handle_food_touch():
    global POINTS, FOOD_POS
    FOOD = pygame.draw.circle(screen, FOOD_COLOR, FOOD_POS, FOOD_SIZE)    

    if FOOD.colliderect(HEAD):
        POINTS += 1
        print("Ам ням ням")
        FOOD_POS = get_random_coords(WIDTH, HEIGHT, HEAD_SIZE)
        FOOD.move_ip(FOOD_POS)


def handle_keys():
    global DIRECTION
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        DIRECTION = (0, -SPEED)
    if pressed_keys[K_DOWN]:
        DIRECTION = (0, SPEED)
    if pressed_keys[K_LEFT]:
        DIRECTION = (-SPEED, 0)
    if pressed_keys[K_RIGHT]:
        DIRECTION = (SPEED, 0)

def handle_wall_touch(head):
    if head.top < 0:
        head.move_ip(0, HEIGHT)
    if head.bottom > HEIGHT:
        head.move_ip(0, -HEIGHT)
    if head.left < 0:
        head.move_ip(WIDTH, 0)
    if head.right > WIDTH:
        head.move_ip(-WIDTH, 0)

while PLAY:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False
    
    screen.fill("#333333") # Ставим фон
    pygame.draw.rect(screen, head_color, HEAD) # Рисуем голову
    HEAD.move_ip(DIRECTION)
    handle_wall_touch(HEAD)
    handle_keys()
    handle_food_touch()

    pygame.display.flip() # Отображаем изменения на экране
    clock.tick(60) # Максимальный FPS



pygame.quit()
 