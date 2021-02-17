import pygame
from pygame.locals import *
from src.globals import *

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
                self.x = 0 + WINDOW_WIDTH / 2 - 8
                self.y = 0 + WINDOW_HEIGHT / 2 - 9
            elif player.currentFrame == 1:
                self.x = 0 + WINDOW_WIDTH / 2 - 9
                self.y = 0 + WINDOW_HEIGHT / 2 - 9
            elif player.currentFrame == 3:
                self.x = 0 + WINDOW_WIDTH / 2 - 6
                self.y = 0 + WINDOW_HEIGHT / 2 - 9
        elif player.dir == "left":
            if player.currentFrame == 0:
                self.x = 0 + WINDOW_WIDTH / 2- 6
                self.y = 0 + WINDOW_HEIGHT / 2 - 9
            elif player.currentFrame == 1 or player.currentFrame == 3:
                self.x = 0 + WINDOW_WIDTH / 2 + 2
                self.y = 0 + WINDOW_HEIGHT / 2- 9
            elif player.currentFrame == 2:
                self.x = 0 + WINDOW_WIDTH / 2 + 1
                self.y = 0 + WINDOW_HEIGHT / 2 - 9
        elif player.dir == "right":
            if player.currentFrame == 0 or player.currentFrame == 2:
                self.x = 0 + WINDOW_WIDTH / 2 + 2
                self.y = 0 + WINDOW_HEIGHT / 2 - 10
            elif player.currentFrame == 1:
                self.x = 0 + WINDOW_WIDTH / 2 - 1
                self.y = 0 + WINDOW_HEIGHT / 2 - 7
            elif player.currentFrame == 3:
                self.x = 0 + WINDOW_WIDTH / 2 - 6
                self.y = 0 + WINDOW_HEIGHT / 2 - 10
        elif player.dir == "up":
            if player.currentFrame == 1 or player.currentFrame == 3:
                self.x = 0 + WINDOW_WIDTH / 2 + 11
                self.y = 0 + WINDOW_HEIGHT / 2- 10
            elif player.currentFrame == 0:
                self.x = 0 + WINDOW_WIDTH / 2 + 12
                self.y = 0 + WINDOW_HEIGHT / 2 - 9
            elif player.currentFrame == 2:
                self.x = 0 + WINDOW_WIDTH / 2 + 10
                self.y = 0 + WINDOW_HEIGHT / 2 - 10

    def render(self, surface):
        self.weaponSprite = pygame.transform.rotate(self.image, self.angle)
        surface.blit(self.weaponSprite, (self.x, self.y))