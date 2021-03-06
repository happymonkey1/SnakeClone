import pygame
import random
import math
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

gameFont = pygame.font.SysFont("Comic Sans MS", 30)

#store the width and height of our window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

rows = 20
columns = 20

gridWidth = SCREEN_WIDTH / rows
gridHeight = SCREEN_HEIGHT / columns

def randomAppleSpawn(tail):
    while True:
        x = math.floor(random.random() * SCREEN_WIDTH / gridWidth)
        y = math.floor(random.random() * SCREEN_HEIGHT / gridHeight)
        filledPosition = False
        for block in tail:
            if x == block[0] and y == block[1]:
                filledPosition = True
        if not filledPosition:
            return (x,y)

applePosition = randomAppleSpawn([])
appleSurface = pygame.Surface((gridHeight, gridHeight))
appleSurface.fill((255,0,0))
#set our target frame rate
TARGET_FRAMERATE = 30

#color of the background of our window
BACKGROUND_COLOR = (113,111,133)

#initialize the pygame screen and store it
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
player = Player(gridWidth, gridHeight)
player.setWindowDimensions(SCREEN_WIDTH, SCREEN_HEIGHT)

#boolean for whether our game is running
game_running = True
lastFrameTime = 0
currentFrameTime = 0
deltaTime = 0

#game loop
while game_running:
    #clamp the maximum number of frames our game can have per second
    pygame.time.Clock().tick(TARGET_FRAMERATE)

    currentFrameTime = pygame.time.get_ticks()
    deltaTime = (currentFrameTime - lastFrameTime) / 1000
    
    #fill the screen with our background color
    screen.fill(BACKGROUND_COLOR)
    screen.blit(appleSurface, (applePosition[0] * gridWidth, applePosition[1] * gridHeight))
    player.update(deltaTime)
    if player.updateApple(applePosition):
        applePosition = randomAppleSpawn(player.tailBlocks)
    player.draw(screen)
    fontSurface = gameFont.render("Current Score: " + str(player.currentScore), False, (0, 0, 0))
    screen.blit(fontSurface, (8, 5))
    highScoreSurface = gameFont.render("High Score: " + str(player.highScore), False, (0, 0, 0))
    screen.blit(highScoreSurface, (8, 40))
    
    # Look at every event in the queue
    for event in pygame.event.get():
        #stop the game loop if the quit event is received
        if event.type == QUIT:
            game_running = False
    

    
    #allow any graphical changes to display to screen
    pygame.display.flip()

    lastFrameTime = currentFrameTime
'''
    if player.isDead:
        game_running = False
'''
pygame.quit()

