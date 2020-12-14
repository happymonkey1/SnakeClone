import pygame
from Player import Player
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
BACKGROUND_COLOR = (113,111,133)

#initialize the pygame screen and store it
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
player = Player()
player.setWindowDimensions(SCREEN_WIDTH, SCREEN_HEIGHT)

#boolean for whether our game is running
game_running = True

#game loop
while game_running:
    #fill the screen with our background color
    screen.fill(BACKGROUND_COLOR)
    player.update()
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
pygame.quit()
#Add snake sprite
#Add Apples that increase snake length
#Border than kills snake
#Snake dies on impact with itself
#End game if snake reaches certain length
#Grid based