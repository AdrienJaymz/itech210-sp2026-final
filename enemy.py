import pygame 
from settings import *
from collision import *
from grid import *
from player import *
import random

RIGHT = [1,0]
LEFT = [-1,0]


enemys = [[29,27], [33,35]]
enemy_dirs = [RIGHT, LEFT]

def draw_enemy(screen, x, y):
    pygame.draw.rect(surface, RED_A, (pos, enemy['size']))



for i, enemy in enumerate(enemys):
    if random.random() < 0.10:
        #randomly changes direction
        dirs = [LEFT, RIGHT]
        random.shuffle(dirs)
        enemy_dirs[i] = dirs[0] 

    test_x = enemy[0] + enemy_dirs[i][0]
    test_y = enemy[1] + enemy_dirs[i][1]
    if get_collisions == False: #([test_x, test_y]):
        enemy[0] += enemy_dirs[i][0]
        enemy[1] += enemy_dirs[i][1]
    else:
        dirs = [LEFT, RIGHT]
        random.shuffle(dirs)
        enemy_dirs[i] = dirs[0]