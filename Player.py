#CODE FOR PLAYER
import pygame
import random
import math
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_w, K_a, K_s, K_d)
class Player(pygame.sprite.Sprite):

    def __init__(self, gridWidth, gridHeight):
        super(Player, self).__init__()
        self.playerWidth = gridWidth
        self.playerHeight = gridHeight
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.surf = pygame.Surface((self.playerWidth, self.playerHeight))
        self.surf.fill((50, 205, 50))
        self.rect = self.surf.get_rect()
        self.speed = 5
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.isDead = False
        self.internalClock = 0

    def setWindowDimensions(self, width, height):
        self.screenWidth = width
        self.screenHeight = height
        self.xPosition = width / 2
        self.yPosition = height / 2
        self.xGridPosition = math.floor(self.xPosition / self.gridWidth)
        self.yGridPosition = math.floor(self.yPosition / self.gridHeight)

    def draw(self, screen):
        screen.blit(self.surf, (self.xGridPosition * self.gridWidth, self.yGridPosition * self.gridHeight))

    #determines what direction the snake goes based on the buttons you press
    def controls(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.changeDirection(0,-1)
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.changeDirection(0,1)
        elif pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.changeDirection(-1,0)
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.changeDirection(1,0)
            
    def changeDirection(self, x, y):
        self.direction = (x,y)

    def update(self, deltaTime):
        self.controls()
        nextMove = 1 / self.speed
        if self.internalClock >= nextMove:
            #self.xPosition += self.speed * self.getXDirection()
            #self.yPosition += self.speed * self.getYDirection()
            self.xGridPosition += self.getXDirection()
            self.yGridPosition += self.getYDirection()
            self.ifOnEdgeDie()
            self.internalClock -= nextMove
        else:
            self.internalClock += deltaTime


    def getXDirection(self):
        return self.direction[0]

    def getYDirection(self):
        return self.direction[1]

    def ifOnEdgeDie(self):
        if self.xGridPosition * self.gridWidth > self.screenWidth or self.xGridPosition < 0:
            self.isDead = True
            self.reset()
        if self.yGridPosition * self.gridHeight > self.screenHeight or self.yGridPosition < 0:
            self.isDead = True
            self.reset()
    
    def reset(self):
        if self.isDead:
            self.xGridPosition = math.floor(self.screenWidth / 2 / self.gridWidth)
            self.yGridPosition = math.floor(self.screenHeight / 2 / self.gridHeight)
            self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
            self.internalClock = 0
            self.isDead = False

    #Add collision/snake eating apple, then set apple to new random positions not on the snake
    #Spawn extra snake part at the back of the the snake
    #Make sure all parts of the snake moves not just the head