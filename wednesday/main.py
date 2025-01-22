import pygame
from pygame.locals import *
from random import randint
from settings import *
pygame.init()

def get_random_coords():
    x = randint(0, WIDTH-FOOD_SIZE)
    y = randint(0, HEIGHT-FOOD_SIZE)
    return x, y

def spawn_tail():
    new_tail_part = Rect(HEAD.x, HEAD.y, HEAD_SIZE, HEAD_SIZE)
    BODY.append(new_tail_part)

def spawn_food():
    global FOOD_POSITION, FOOD, SCORE
    FOOD = pygame.draw.circle(screen, FOOD_COLOR, FOOD_POSITION, FOOD_SIZE)
    if FOOD.colliderect(HEAD):
        SCORE += 1
        print(SCORE,"points")
        FOOD_POSITION = get_random_coords() 
        spawn_tail()

def handle_keys():
    global DIRECTION
    pressed_keys = pygame.key.get_pressed()
    # arrows
    if pressed_keys[K_UP]:
        DIRECTION = (0, -SPEED)
    if pressed_keys[K_DOWN]:
        DIRECTION = (0, SPEED)
    if pressed_keys[K_LEFT]:
        DIRECTION = (-SPEED, 0)
    if pressed_keys[K_RIGHT]:
        DIRECTION = (SPEED, 0)
    # wasd
    if pressed_keys[K_w]:
        DIRECTION = (0, -SPEED)
    if pressed_keys[K_s]:
        DIRECTION = (0, SPEED)
    if pressed_keys[K_a]:
        DIRECTION = (-SPEED, 0)
    if pressed_keys[K_d]:
        DIRECTION = (SPEED, 0)

def handle_wall_touch():
    if HEAD.left < 0:
        HEAD.move_ip(WIDTH, 0)
    if HEAD.right > WIDTH:
        HEAD.move_ip(-WIDTH, 0)
    if HEAD.bottom > HEIGHT:
        HEAD.move_ip(0, -HEIGHT)
    if HEAD.top < 0:
        HEAD.move_ip(0, HEIGHT)

while RUNNING:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    # Ставим фон
    screen.fill(BACKGROUND_COLOR)
    spawn_food()
    pygame.draw.rect(screen, HEAD_COLOR, HEAD)

    handle_wall_touch()
    handle_keys()
    HEAD.move_ip(DIRECTION)

    for tail_part in BODY:
        pygame.draw.rect(screen, BODY_COLOR, tail_part)

    # Отображаем изменения на экране
    pygame.display.flip()

    # Максимальный FPS
    clock.tick(10)



pygame.quit()
