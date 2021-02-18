import pygame
from pygame.locals import *
from src.globals import *
from src.entity import Entity

class Actor(Entity):
    def __init__(self):
        super().__init__()
        self.animTime = 0.25
        self.maxFrames = 4
        self.currentFrame = 0
        self.time = 0

    def switchAnim(self):
        if self.dir == "down":
            self.image = pygame.image.load("res/sprites/hero_1/walk_down.png")
        elif self.dir == "up":
            self.image = pygame.image.load("res/sprites/hero_1/walk_up.png")
        elif self.dir == "left":
            self.image = pygame.image.load("res/sprites/hero_1/walk_left.png")
        elif self.dir == "right":
            self.image = pygame.image.load("res/sprites/hero_1/walk_right.png")

    def animate(self, delta):
        self.time += delta
        if self.time >= self.animTime:
            self.time = 0
            self.currentFrame += 1
            if self.currentFrame >= self.maxFrames:
                self.currentFrame = 0

    def update(self, delta, inputMap):
        self.animate(delta)