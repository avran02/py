import pygame
from pygame.locals import *
from random import randint
from settings import *
pygame.init()

def get_random_coords():
    max_x = int((WIDTH-FOOD_SIZE)/SPEED)
    max_y = int((HEIGHT-FOOD_SIZE)/SPEED)
    x = randint(0, max_x) * SPEED
    y = randint(0, max_y) * SPEED
    return x, y

def spawn_tail():
    if len(BODY) == 0:
        x = HEAD.x-DIRECTION[0]*2
        y = HEAD.y-DIRECTION[1]*2
    else:
        x = BODY[-1].x-DIRECTION[0]
        y = BODY[-1].y-DIRECTION[1]
    
    new_tail_part = Rect(x, y, HEAD_SIZE, HEAD_SIZE)
    BODY.append(new_tail_part)

def handle_food_touch():
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
    pygame.draw.rect(screen, HEAD_COLOR, HEAD)
    handle_food_touch()

    handle_wall_touch()
    handle_keys()
    HEAD.move_ip(DIRECTION)

    for tail_part in BODY:
        tail_part.move_ip(DIRECTION)
        pygame.draw.rect(screen, BODY_COLOR, tail_part)

    # Отображаем изменения на экране
    pygame.display.flip()

    # Максимальный FPS
    clock.tick(10)



pygame.quit()
