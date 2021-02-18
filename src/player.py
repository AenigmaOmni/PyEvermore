import pygame
from src.actor import Actor
from src.globals import *
from pygame.locals import *
from src.weapon import Weapon

class Player(Actor):
    def __init__(self):
        path = "res/sprites/hero_1/"
        super().__init__(path + "walk_down.png", path + "walk_up.png", path + "walk_left.png", path + "walk_right.png")
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

    def preUpdate(self, delta, inputMap):
        super().preUpdate(delta)
        self.getInput(delta, inputMap)
    
    def postUpdate(self, delta):
        super().postUpdate(delta)

    def update(self, delta):
        super().update(delta)