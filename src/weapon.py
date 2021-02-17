import pygame
from pygame.locals import *


class Weapon:
    def __init__(self):
        self.image = None
        self.weaponSprite = self.image
        self.x = 0
        self.y = 0
        self.angle = 0

    def loadImage(self, path):
        self.image = pygame.image.load(path)

    def update(self, dt, player):
        self.x = player.x
        self.y = player.y

    def render(self, surface):
        self.weaponSprite = pygame.transform.rotate(self.image, self.angle)
        surface.blit(self.weaponSprite, (self.x, self.y))