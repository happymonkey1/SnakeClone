#CODE FOR PLAYER
import pygame
import random
import math
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, KEYDOWN, QUIT, K_w, K_a, K_s, K_d)
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
        self.lastDirection = self.direction
        self.isDead = False
        self.internalClock = 0
        self.tailBlocks = []
        self.maxSpace = gridWidth * gridHeight
        self.pauseGame = False
        self.currentScore = 0
        self.readHighScore()

    def setWindowDimensions(self, width, height):
        self.screenWidth = width
        self.screenHeight = height
        self.xPosition = width / 2
        self.yPosition = height / 2
        self.xGridPosition = math.floor(self.xPosition / self.gridWidth)
        self.yGridPosition = math.floor(self.yPosition / self.gridHeight)
        self.tailBlocks = [(self.xGridPosition, self.yGridPosition)]

    def draw(self, screen):
        for tail in self.tailBlocks:
            x = tail[0]
            y = tail[1]
            screen.blit(self.surf, (x * self.gridWidth, y * self.gridHeight))

    #determines what direction the snake goes based on the buttons you press
    def controls(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            if self.lastDirection != (0,1) or len(self.tailBlocks) == 1:
                self.changeDirection(0,-1)
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            if self.lastDirection != (0,-1) or len(self.tailBlocks) == 1:
                self.changeDirection(0,1)
        elif pressed_keys[K_LEFT] or pressed_keys[K_a]:
            if self.lastDirection != (1,0) or len(self.tailBlocks) == 1:
                self.changeDirection(-1,0)
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            if self.lastDirection != (-1,0) or len(self.tailBlocks) == 1:
                self.changeDirection(1,0)
        elif pressed_keys[K_SPACE]:
            self.pauseGame = not self.pauseGame
            
    def changeDirection(self, x, y):
        self.direction = (x,y)
        self.lastDirection = self.direction

    def update(self, deltaTime):
        self.controls()
        if self.pauseGame:
            return
        nextMove = 1 / self.speed
        if self.internalClock >= nextMove:
            #self.xPosition += self.speed * self.getXDirection()
            #self.yPosition += self.speed * self.getYDirection()
            tail = self.tailBlocks.pop(len(self.tailBlocks) - 1)
            headGridXPos = 0
            headGridYPos = 0
            if len(self.tailBlocks) > 0:
                headGridXPos = self.tailBlocks[0][0]
                headGridYPos = self.tailBlocks[0][1]
            else:
                headGridXPos = tail[0]
                headGridYPos = tail[1]
            moveGridXPos = headGridXPos + self.getXDirection()
            moveGridYPos = headGridYPos + self.getYDirection()
            self.xPosition = moveGridXPos * self.gridWidth
            self.yPosition = moveGridYPos * self.gridHeight
            self.tailBlocks.insert(0,(moveGridXPos, moveGridYPos))
            #self.xGridPosition += self.getXDirection()
            #self.yGridPosition += self.getYDirection()
            self.checkSelfCollision()
            self.ifOnEdgeDie()
            self.internalClock -= nextMove
        else:
            self.internalClock += deltaTime

    def updateApple(self, applePosition):
        if applePosition[0] == self.tailBlocks[0][0] and applePosition[1] == self.tailBlocks[0][1]:
            self.tailBlocks.insert(0,(applePosition[0], applePosition[1]))
            self.currentScore += 1
            if self.currentScore > self.highScore:
                self.highScore = self.currentScore
                self.saveHighScore()
            if len(self.tailBlocks) == self.maxSpace:
                print("Congratulations! You Win!")
                self.isDead = True
                self.reset()
            return True
        else:
            return False
    
    def saveHighScore(self):
        f = open("highScore.txt", "w")
        f.write(str(self.highScore))
        f.close()

    def readHighScore(self):
        try:
            f = open("highScore.txt", "r")
            self.highScore = int(f.read().strip())
            f.close()
        except:
            self.highScore = 0

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

    def checkSelfCollision(self):
        headPosition = self.tailBlocks[0]
        for index,tail in enumerate(self.tailBlocks):
            if index > 0:
                if headPosition[0] == tail[0] and headPosition[1] == tail[1]:
                    self.isDead = True
                    self.reset()
                    break
    
    def reset(self):
        if self.isDead:
            self.xGridPosition = math.floor(self.screenWidth / 2 / self.gridWidth)
            self.yGridPosition = math.floor(self.screenHeight / 2 / self.gridHeight)
            self.tailBlocks = [(self.xGridPosition, self.yGridPosition)]
            self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
            self.internalClock = 0
            self.isDead = False
            self.pauseGame = False
            self.currentScore = 0

#Customization: Head of snake is unique (a black a dot for an eye, etc.)