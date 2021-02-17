import pygame
from pygame.locals import *


class Weapon:
    def __init__(self):
        self.image = None
        self.weaponSprite = self.image
        self.x = 0
        self.y = 0
        self.angle = 180

    def loadImage(self, path):
        self.image = pygame.image.load(path)

    def update(self, dt, player):
        if player.dir == "down":
            if player.currentFrame == 0 or player.currentFrame == 2:
                self.x = player.x - 8
                self.y = player.y - 9
            elif player.currentFrame == 1:
                self.x = player.x - 9
                self.y = player.y - 9
            elif player.currentFrame == 3:
                self.x = player.x - 6
                self.y = player.y - 9
        elif player.dir == "left":
            if player.currentFrame == 0:
                self.x = player.x - 6
                self.y = player.y - 9
            elif player.currentFrame == 1 or player.currentFrame == 3:
                self.x = player.x + 2
                self.y = player.y - 9
            elif player.currentFrame == 2:
                self.x = player.x + 1
                self.y = player.y - 9
        elif player.dir == "right":
            if player.currentFrame == 0 or player.currentFrame == 2:
                self.x = player.x + 2
                self.y = player.y - 10
            elif player.currentFrame == 1:
                self.x = player.x - 1
                self.y = player.y - 7
            elif player.currentFrame == 3:
                self.x = player.x - 6
                self.y = player.y - 10
        elif player.dir == "up":
            if player.currentFrame == 1 or player.currentFrame == 3:
                self.x = player.x + 11
                self.y = player.y - 10
            elif player.currentFrame == 0:
                self.x = player.x + 12
                self.y = player.y - 9
            elif player.currentFrame == 2:
                self.x = player.x + 10
                self.y = player.y - 10

    def render(self, surface):
        self.weaponSprite = pygame.transform.rotate(self.image, self.angle)
        surface.blit(self.weaponSprite, (self.x, self.y))