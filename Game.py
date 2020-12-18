import pygame
from Player import Player
from random import random
from math import floor
#https://realpython.com/pygame-a-primer/#pygame-concepts

#import keybind locals from pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


#must be called to initialize code for pygame
pygame.init()

#store the width and height of our window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#color of the background of our window
BACKGROUND_COLOR = (113,111,133)

#init variables for grid
ROWS, COLUMNS = 20, 20

GRID_WIDTH = SCREEN_WIDTH/ROWS
GRID_HEIGHT = SCREEN_HEIGHT/COLUMNS

#initialize the pygame screen and store it
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

#init player
player = Player(GRID_WIDTH, GRID_HEIGHT)
player.setWindowDimensions(SCREEN_WIDTH, SCREEN_HEIGHT)

#boolean for whether our game is running
game_running = True

#init variables for delta time calc
last_frame_time = 0
current_frame_time = 0
delta_time = 0

#store pygame clock 
clock = pygame.time.Clock()

#set our target frame rate
TARGET_FRAMERATE = 144

#apple
def new_random_apple_spawn():
    return (floor(random() * SCREEN_WIDTH / GRID_WIDTH), floor(random() * SCREEN_HEIGHT / GRID_HEIGHT))

def draw_apple(surf, pos):
    screen.blit(surf, (pos[0] * GRID_WIDTH, pos[1] * GRID_HEIGHT))
    
apple_pos = new_random_apple_spawn()
apple_surf = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
apple_surf.fill((255,0,0))

#game loop
while game_running:
    #clamp the maximum number of frames our game can have per second and get the frame time
    clock.tick(TARGET_FRAMERATE)

    #get the current frame time
    current_frame_time = pygame.time.get_ticks()

    #calculate delta time 
    delta_time = (current_frame_time - last_frame_time) / 1000

    #fill the screen with our background color
    screen.fill(BACKGROUND_COLOR)
    draw_apple(apple_surf, apple_pos)
    
    player.update(delta_time)
    if player.check_apple(apple_pos):
        apple_pos = new_random_apple_spawn()
    player.draw(screen)
    
    # Look at every event in the queue
    for event in pygame.event.get():
        #stop the game loop if the quit event is received
        if event.type == QUIT:
            game_running = False

    
    #allow any graphical changes to display to screen
    pygame.display.flip()

    if player.isDead:
        game_running = False

    #set last frame time
    last_frame_time = current_frame_time
pygame.quit()
#Add snake sprite
#Add Apples that increase snake length
#Border than kills snake
#Snake dies on impact with itself
#End game if snake reaches certain length
#Grid based