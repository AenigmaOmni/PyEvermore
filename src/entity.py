from src.globals import *
import pygame

class Entity:
    def __init__(self):
        self.x = 64
        self.y = 64
        self.tx = 0
        self.ty = 0
        self.dx = 0
        self.dy = 0
        self.speed = 100
        self.height = PLAYER_SIZE
        self.width = PLAYER_SIZE
        self.lastDir = "down"
        self.rect = pygame.Rect(0, 0, 12, 12)
        self.dir = "down"
        self.image = pygame.image.load("res/sprites/hero_1/walk_down.png")

    def getMoveRect(self, delta):
        x = self.x + ( (self.width / 2) - self.rect.width / 2)
        x = x + self.dx * self.speed * delta
        y = self.y + self.height - self.rect.height / 2
        y = y + self.dy * self.speed * delta
        rect = pygame.Rect(x, y, self.rect.width, self.rect.height)
        rect.x =  rect.x + self.dx * self.speed * delta
        rect.y = rect.y + self.dy * self.speed * delta
        return rect

    def doMove(self, delta):
        nx = self.x + self.dx * self.speed * delta
        ny = self.y + self.dy * self.speed * delta
        self.x = nx
        self.y = ny
        self.rect.x = self.x
        self.rect.y = self.y
        self.tx = int(self.x / TILE_SIZE)
        self.ty = int(self.y / TILE_SIZE)

    def preUpdate(self, delta):
        pass

    def update(self, delta):
        pass

    def postUpdate(self, delta, inputMap):
        self.doMove(delta)
        self.dx = 0
        self.dy = 0
        self.weapon.update(delta, self)
        if self.lastDir != self.dir:
            self.lastDir = self.dir
            self.switchAnim()