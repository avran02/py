import pygame
from pygame.locals import *

SPEED = 50
HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = '#666666'
SCORE = 0
RUNNING = True

HEAD_SIZE = 50
HEAD_COLOR = '#e84adb'
DIRECTION = (0, 0)

BODY = []
BODY_COLOR = "#2e4770"

FOOD_SIZE = 25
FOOD_COLOR = '#36e485'
FOOD_POSITION = (100,100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

FOOD = pygame.draw.circle(screen, FOOD_COLOR, FOOD_POSITION, FOOD_SIZE)
HEAD = Rect(
    WIDTH/2-HEAD_SIZE/2,  # начальный X 
    HEIGHT/2-HEAD_SIZE/2, # начальный Y
    HEAD_SIZE,            # ширина
    HEAD_SIZE,            # высота
)
