import pygame
from src.actor import Actor
from src.globals import *
from pygame.locals import *
from src.weapon import Weapon

class Player(Actor):
    def __init__(self):
        super().__init__()
        self.drawX = 0 + GAME_WIDTH / 2 - PLAYER_SIZE / 2
        self.drawY = 0 + GAME_HEIGHT / 2 - PLAYER_SIZE / 2
        self.rect = pygame.Rect(0, 0, 12, 12)
        self.weapon = Weapon()
        self.weapon.loadImage("res/sprites/sword_1.png")

    def renderPlayer(self, surface):
        surface.blit(self.image, (self.drawX, self.drawY), 
            pygame.Rect(PLAYER_SIZE * self.currentFrame, 0, self.width, self.height))

    def renderWeapon(self, surface):
        self.weapon.render(surface)

    def render(self, surface, camera):
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