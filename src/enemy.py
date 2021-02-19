import pygame
from pygame.locals import *
from src.globals import *
from src.actor import Actor

class Enemy(Actor):
    def __init__(self, path):
        super().__init__()
        self.maxFrames = 2
        self.load(path)
        self.collisionMask = ENEMY_MASK

    def load(self, path):
        self.image = pygame.image.load(path)

    def update(self, delta, inputMap=None):
        super().update(delta)

    def preUpdate(self, delta):
        super().preUpdate(delta)

    def postUpdate(self, delta):
        super().postUpdate(delta)

