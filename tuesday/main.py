import pygame
from pygame.locals import *
from utils import get_random_coords

SPEED = 20
POINTS = 0
WIDTH = 800
HEIGHT = 600
HEAD_SIZE = 20
PLAY = True
BACKGROUND_COLOR = "#333333"
DIRECTION = (0,0)
pygame.font.init()
font = pygame.font.Font('font/GochiHand-Regular.ttf', 36)
# font = pygame.font.SysFont(None, 36)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

head_color = "#5c89d1"
head_x = (WIDTH-HEAD_SIZE)/2
head_y = (HEIGHT-HEAD_SIZE)/2
HEAD = Rect(head_x, head_y, HEAD_SIZE, HEAD_SIZE) # (x, y, ширина, высота)

TAIL_COLOR = "#2e4770"
BODY = []

FONT_COLOR = "#fa13ef75"
FOOD_COLOR = "#36e485"
FOOD_SIZE = 20
FOOD_POS = get_random_coords(WIDTH, HEIGHT, HEAD_SIZE)
FOOD = pygame.draw.circle(screen, FOOD_COLOR, FOOD_POS, FOOD_SIZE)    

def render_score():
    text_to_render = "score: " + str(POINTS)
    text = font.render(text_to_render, True, FONT_COLOR)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT*0.2))
    screen.blit(text, text_rect)

def spawn_tail():
    new_tail_part = Rect(HEAD.x, HEAD.y, HEAD_SIZE, HEAD_SIZE)
    BODY.append(new_tail_part)

def handle_food_touch():
    global POINTS, FOOD_POS
    FOOD = pygame.draw.circle(screen, FOOD_COLOR, FOOD_POS, FOOD_SIZE)    

    if FOOD.colliderect(HEAD):
        POINTS += 1
        FOOD_POS = get_random_coords(WIDTH, HEIGHT, HEAD_SIZE)
        FOOD.move_ip(FOOD_POS)
        spawn_tail()


def move(head):
    global DIRECTION
    # Изменяем направление, при нажатии на клавиши
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        DIRECTION = (0, -SPEED)
    if pressed_keys[K_DOWN]:
        DIRECTION = (0, SPEED)
    if pressed_keys[K_LEFT]:
        DIRECTION = (-SPEED, 0)
    if pressed_keys[K_RIGHT]:
        DIRECTION = (SPEED, 0)
    # Телепортируем змейку в случае выхода за границы экрана
    if head.top < 0:
        head.move_ip(0, HEIGHT)
    if head.bottom > HEIGHT:
        head.move_ip(0, -HEIGHT)
    if head.left < 0:
        head.move_ip(WIDTH, 0)
    if head.right > WIDTH:
        head.move_ip(-WIDTH, 0)
    # Двигаем змейку
    if len(BODY) == 0:
        head.move_ip(DIRECTION)
        return
    BODY[0].x = head.x
    BODY[0].y = head.y
    for i in range(len(BODY)-1, 0, -1):
        BODY[i].x = BODY[i-1].x
        BODY[i].y = BODY[i-1].y

    head.move_ip(DIRECTION)



while PLAY:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False
    
    screen.fill(BACKGROUND_COLOR) # Ставим фон
    move(HEAD)
    pygame.draw.rect(screen, head_color, HEAD) # Рисуем голову
    handle_food_touch()
    render_score()


    for tail_part in BODY:
        pygame.draw.rect(screen, TAIL_COLOR, tail_part) 

    pygame.display.flip() # Отображаем изменения на экране
    clock.tick(15) # Максимальный FPS



pygame.quit()
