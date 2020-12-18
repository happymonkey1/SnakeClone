#CODE FOR PLAYER
import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_w, K_a, K_s, K_d)
class Player(pygame.sprite.Sprite):

    def __init__(self, grid_width, grid_height):
        super(Player, self).__init__()
        self.playerWidth = grid_width
        self.playerHeight = grid_height
        self.surf = pygame.Surface((self.playerWidth, self.playerHeight))
        self.surf.fill((50, 205, 50))
        self.rect = self.surf.get_rect()
        self.speed = 15 #grid changes per second
        self._internal_clock = 0
        self.direction = (0,-1)
        self.last_direction = (0,-1)
        self.isDead = False
        
        self.GRID_WIDTH = grid_width
        self.GRID_HEIGHT = grid_height
        
        self.tail = []
        

    def setWindowDimensions(self, width, height):
        self.screenWidth = width
        self.screenHeight = height
        self.xPosition = width / 2
        self.yPosition = height / 2
        
        self.calcAndSetGridPos(self.xPosition, self.yPosition)

    def draw(self, screen):
        for piece in self.tail:
            x,y = piece
            screen.blit(self.surf, (x * self.GRID_WIDTH, y * self.GRID_HEIGHT))

    #determines what direction the snake goes based on the buttons you press
    def controls(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            if self.get_last_direction()[1] != 1:
                self.changeDirection(0,-1)
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            if self.get_last_direction()[1] != -1:
                self.changeDirection(0,1)
        elif pressed_keys[K_LEFT] or pressed_keys[K_a]:
            if self.get_last_direction()[0] != 1:
                self.changeDirection(-1,0)
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            if self.get_last_direction()[0] != -1:
                self.changeDirection(1,0)
            
    def changeDirection(self, x, y):
        self.direction = (x,y)

    def update(self, delta_time):
        self.controls()
        # self.xPosition += self.speed * self.getXDirection() * delta_time
        # self.yPosition += self.speed * self.getYDirection() * delta_time
        
        
        nextMove = 1 / self.speed
        if self._internal_clock >= nextMove:
            self.move()
            self._internal_clock = 0
        else:
            self._internal_clock += delta_time

    def move(self):
        
        
        tail = self.tail.pop(len(self.tail)-1)
        head_x, head_y = self.tail[0] if len(self.tail) > 0 else tail
        
        move_grid_x, move_grid_y = head_x + self.getXDirection(), head_y + self.getYDirection()
        self.last_direction = (self.getXDirection(), self.getYDirection())
        self.xPosition, self.yPosition = move_grid_x * self.GRID_WIDTH, move_grid_y * self.GRID_HEIGHT
        self.tail.insert(0,(move_grid_x, move_grid_y))
        
        self.check_tail_collision()
        self.ifOnEdgeDie()
        
    def update_tail(self):
        for index in range(len(self.tail)-1, -1, -1):
            self.tail[index] = self.tail[index-1]

    def getXDirection(self):
        return self.direction[0]

    def getYDirection(self):
        return self.direction[1]
    
    def get_last_direction(self):
        return self.last_direction
    
    def calcAndSetGridPos(self, x, y):
        self.tail.append((x / self.GRID_WIDTH, y / self.GRID_HEIGHT))

    def ifOnEdgeDie(self):
        if self.xPosition + self.playerWidth > self.screenWidth or self.xPosition < 0:
            self.isDead = True
        if self.yPosition + self.playerHeight > self.screenHeight or self.yPosition < 0:
            self.isDead = True
            
    def check_apple(self, pos):
        x,y = self.tail[0]
        if pos[0] == x and pos[1] == y:
            self.tail.insert(0, (x, y))
            return True
        else:
            return False
        
    def check_tail_collision(self):
        head_x, head_y = self.tail[0]
        for index, tail_part in enumerate(self.tail):
            if index != 0:
                tail_x, tail_y = tail_part
                if head_x == tail_x and head_y == tail_y:
                    self.isDead = True
                