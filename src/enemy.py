import pygame
from pygame.locals import *
from src.globals import *
from src.actor import Actor

class Enemy(Actor):
    def __init__(self, path):
        self.anim = pygame.image.load(path)
        self.maxFrames = 2


    def update(self, delta, inputMap=None):
        super().update(delta)

