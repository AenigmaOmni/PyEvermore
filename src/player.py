import pygame
from pygame.locals import *
from src.weapon import Weapon

class Player:
    def __init__(self):
        self.x = 64
        self.y = 64
        self.dx = 0
        self.dy = 0
        self.speed = 100
        self.height = 32
        self.width = 32
        self.lastDir = "down"
        self.dir = "down"
        self.image = pygame.image.load("res/sprites/hero_1/walk_down.png")
        self.maxFrames = 4
        self.currentFrame = 0
        self.time = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.animTime = 0.25
        self.weapon = Weapon()
        self.weapon.loadImage("res/sprites/sword_1.png")

    def switchAnim(self):
        if self.dir == "down":
            self.image = pygame.image.load("res/sprites/hero_1/walk_down.png")
        elif self.dir == "up":
            self.image = pygame.image.load("res/sprites/hero_1/walk_up.png")
        elif self.dir == "left":
            self.image = pygame.image.load("res/sprites/hero_1/walk_left.png")
        elif self.dir == "right":
            self.image = pygame.image.load("res/sprites/hero_1/walk_right.png")

    def renderPlayer(self, surface):
        surface.blit(self.image, (self.x, self.y), pygame.Rect(32 * self.currentFrame, 0, self.width, self.height))

    def renderWeapon(self, surface):
        self.weapon.render(surface)

    def render(self, surface):
        if self.dir == "up":
            self.renderWeapon(surface)
            self.renderPlayer(surface)
        elif self.dir == "down":
            self.renderPlayer(surface)
            self.renderWeapon(surface)
        elif self.dir == "left":
            self.renderWeapon(surface)
            self.renderPlayer(surface)
        elif self.dir == "right":
            self.renderPlayer(surface)
            self.renderWeapon(surface)

    def update(self, delta, inputMap):
        self.animate(delta)
        #self.currentFrame = 0

    def preUpdate(self, delta, inputMap):
        self.getInput(delta, inputMap)

    def postUpdate(self, delta, inputMap):
        self.doMove(delta)
        self.dx = 0
        self.dy = 0
        self.weapon.update(delta, self)

        if self.lastDir != self.dir:
            self.lastDir = self.dir
            self.switchAnim()

    def getInput(self, delta, inputMap):
        if inputMap.w == True:
            self.dy = -1
            self.dir = "up"
        if inputMap.s == True:
            self.dy = 1
            self.dir = "down"
        if inputMap.a == True:
            self.dx = -1
            self.dir = "left"
        if inputMap.d == True:
            self.dx = 1
            self.dir = "right"

    def getMoveRect(self, delta):
        rect = pygame.Rect(self.x + self.width / 2 - ((self.width / 2) / 2), self.y, self.width / 2, self.height)
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

    def animate(self, delta):
        self.time += delta
        if self.time >= self.animTime:
            self.time = 0
            self.currentFrame += 1
            if self.currentFrame >= self.maxFrames:
                self.currentFrame = 0