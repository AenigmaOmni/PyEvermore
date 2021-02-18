import pygame
from pygame.locals import *
from src.globals import *
from src.actor import Actor

class Enemy(Actor):
    def __init__(self, path):
        super().__init__()
        self.maxFrames = 2
        self.load(path)

    def load(self, path):
        self.image = pygame.image.load(path)

    def update(self, delta, inputMap=None):
        super().update(delta)

