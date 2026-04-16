import pygame
from settings import *
from camera import *
from player import *
from grid import *
from collision import *

background_image = pygame.image.load("images/map2.png")

pygame.init()

def init():
    #initialize all of the game here
    pygame.display.set_caption("ITECH 210 Final")
    config = {}


    #collider grid
    collider_grid = grid
    for x in range(LEVEL[0]//CELL_SIZE):
        for y in range(LEVEL[1]//CELL_SIZE):
            collider_grid[f"{x},{y}"] = None
    config['collider_grid'] = collider_grid
    
    #add colliders to the grid
    add_collider_to_grid((0,20), (30,3), collider_grid)
    add_collider_to_grid((7,17), (7,1), collider_grid)
    add_collider_to_grid((21,11), (2,1), collider_grid)
    add_collider_to_grid((17,8), (3,1), collider_grid)
    add_collider_to_grid((10,5), (5,1), collider_grid)
    add_collider_to_grid((26,15), (2,5), collider_grid)
    add_collider_to_grid((30,20), (11,1), collider_grid)
    add_collider_to_grid((46,19), (1,1), collider_grid)
    add_collider_to_grid((15,14), (5,1), collider_grid)
    add_collider_to_grid((49,18), (14,2), collider_grid)
    add_collider_to_grid((35,10), (4,1), collider_grid)
    add_collider_to_grid((44,7), (4,1), collider_grid)
    add_collider_to_grid((47,8), (1,1), collider_grid)
    add_collider_to_grid((47,9), (3,1), collider_grid)
    add_collider_to_grid((51,12), (3,1), collider_grid)
    add_collider_to_grid((56,11), (7,7), collider_grid)
    add_collider_to_grid((55,15), (1,1), collider_grid)
    add_collider_to_grid((40,21), (1,3), collider_grid)
    add_collider_to_grid((32,23), (8,1), collider_grid)
    add_collider_to_grid((30,24), (1,1), collider_grid)
    add_collider_to_grid((35,26), (11,2), collider_grid)
    add_collider_to_grid((27,23), (1,4), collider_grid)
    add_collider_to_grid((28,26), (1,2), collider_grid)
    add_collider_to_grid((28,28), (8,1), collider_grid)
    add_collider_to_grid((53,20), (31,6), collider_grid)
    #lower section
    add_collider_to_grid((46,22), (4,1), collider_grid)
    add_collider_to_grid((46,23), (1,1), collider_grid)
    add_collider_to_grid((48,26), (1,1), collider_grid)
    add_collider_to_grid((49,29), (1,1), collider_grid)
    add_collider_to_grid((47,32), (1,1), collider_grid)
    add_collider_to_grid((45,35), (1,1), collider_grid)
    add_collider_to_grid((29,33), (1,1), collider_grid)
    add_collider_to_grid((32,35), (1,1), collider_grid)
    add_collider_to_grid((28,36), (28,1), collider_grid)
    add_collider_to_grid((27,30), (1,7), collider_grid)
    add_collider_to_grid((28,30), (8,1), collider_grid)
    add_collider_to_grid((35,31), (5,2), collider_grid)
    add_collider_to_grid((40,30), (4,2), collider_grid)
    add_collider_to_grid((44,28), (2,2), collider_grid)
    add_collider_to_grid((50,25), (2,9), collider_grid)
    add_collider_to_grid((52,25), (1,1), collider_grid)
    add_collider_to_grid((52,28), (1,6), collider_grid)
    add_collider_to_grid((53,28), (1,4), collider_grid)
    add_collider_to_grid((54,28), (1,1), collider_grid)
    add_collider_to_grid((54,35), (2,1), collider_grid)
    add_collider_to_grid((56,33), (3,3), collider_grid)
    add_collider_to_grid((58,31), (3,2), collider_grid)
    add_collider_to_grid((57,28), (2,1), collider_grid)
    add_collider_to_grid((61,26), (1,6), collider_grid)
    #ice half
    add_collider_to_grid((76,11), (3,1), collider_grid)
    add_collider_to_grid((80,14), (4,1), collider_grid)
    add_collider_to_grid((75,17), (5,1), collider_grid)


    #camera
    config['camera'] = camera

    #objects
    objects = []
    config['objects'] = objects

    #player
    config['player'] = player
    objects.append(player)

    
    game_loop(screen, clock, config)

def update(dt, objects):
    #all update calls are made here
    for obj in objects:
        obj['update'](dt)

def draw(surface, camera, objects):
    screen.blit(background_image, (-camera['pos'][0],-camera['pos'][1]))
    #all draw calls are made from here
    for obj in objects:
        obj['draw'](surface, camera)
    

def game_loop(screen, clock, config):
    #where the main game loop happens
    camera = config['camera']
    grid = config['collider_grid']
    objects = config['objects']
    player = config['player']

    running = True

    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update(dt, objects)
        update_camera(player)
        
        screen.fill(BLACK)
        draw(screen, camera, objects)

        #debug mode
        if debug:
            draw_colliders(screen, camera, grid)
            draw_grid(screen, camera, grid)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    init()