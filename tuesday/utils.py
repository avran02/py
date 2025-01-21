from random import randint

def get_random_coords(WIDTH, HEIGHT, HEAD_SIZE):
    x = randint(0, WIDTH-HEAD_SIZE)
    y = randint(0, HEIGHT-HEAD_SIZE)
    return x, y
