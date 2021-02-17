import pygame
from pygame.locals import *

class Player:
    def __init__(self):
        self.x = 64
        self.y = 64
        self.image = pygame.image.load("res/sprites/hero_1/walk_down.png")
        self.maxFrames = 4
        self.currentFrame = 0
        self.time = 0
        self.animTime = 0.25

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y), pygame.Rect(32 * self.currentFrame, 0, 32, 32))


    def update(self, delta):
        self.animate(delta)

    def animate(self, delta):
        self.time += delta
        if self.time >= self.animTime:
            self.time = 0
            self.currentFrame += 1
            if self.currentFrame >= self.maxFrames:
                self.currentFrame = 0