import pygame
import Player
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
SCREEN_HEIGHT = 600

#color of the background of our window
BACKGROUND_COLOR = (0,0,0)

#initialize the pygame screen and store it
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#boolean for whether our game is running
game_running = True

#game loop
while game_running:
    #fill the screen with our background color
    screen.fill(BACKGROUND_COLOR)
    
    # Look at every event in the queue
    for event in pygame.event.get():
        #stop the game loop if the quit event is received
        if event.type == QUIT:
            game_running = False
    
    #allow any graphical changes to display to screen
    pygame.display.flip()