#CODE FOR PLAYER
import pygame
import random
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_w, K_a, K_s, K_d)
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.playerWidth = 25
        self.playerHeight = 25
        self.surf = pygame.Surface((self.playerWidth, self.playerHeight))
        self.surf.fill((50, 205, 50))
        self.rect = self.surf.get_rect()
        self.speed = 5
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.isDead = False

    def setWindowDimensions(self, width, height):
        self.screenWidth = width
        self.screenHeight = height
        self.xPosition = width / 2
        self.yPosition = height / 2

    def draw(self, screen):
        screen.blit(self.surf, (self.xPosition, self.yPosition))

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

    def update(self):
        self.controls()
        self.xPosition += self.speed * self.getXDirection()
        self.yPosition += self.speed * self.getYDirection()
        self.ifOnEdgeDie()

    def getXDirection(self):
        return self.direction[0]

    def getYDirection(self):
        return self.direction[1]

    def ifOnEdgeDie(self):
        if self.xPosition + self.playerWidth > self.screenWidth or self.xPosition < 0:
            self.isDead = True
            self.reset()
        if self.yPosition + self.playerHeight > self.screenHeight or self.yPosition < 0:
            self.isDead = True
            self.reset()
    
    def reset(self):
        if self.isDead:
            self.xPosition = self.screenWidth / 2
            self.yPosition = self.screenHeight / 2
            self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
            self.isDead = False