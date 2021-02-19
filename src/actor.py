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
        self.walking = False

    def load(self, downPath, upPath, leftPath, rightPath):
        self.downAnim = pygame.image.load(downPath)
        self.upAnim = pygame.image.load(upPath)
        self.leftAnim = pygame.image.load(leftPath)
        self.rightAnim = pygame.image.load(rightPath)

    def switchAnim(self):
        if self.dir == "down":
            self.image = self.downAnim
        elif self.dir == "up":
            self.image = self.upAnim
        elif self.dir == "left":
            self.image = self.leftAnim
        elif self.dir == "right":
            self.image = self.rightAnim

    def animate(self, delta):
        if self.walking:
            self.time += delta
            if self.time >= self.animTime:
                self.time = 0
                self.currentFrame += 1
                if self.currentFrame >= self.maxFrames:
                    self.currentFrame = 0
        else:
            if self.dir == "down":
                self.currentFrame = 0
            elif self.dir == "up":
                self.currentFrame = 1
            elif self.dir == "left":
                self.currentFrame = 1
            elif self.dir == "right":
                self.currentFrame = 0
                
    def preUpdate(self, delta):
        super().preUpdate(delta)

    def update(self, delta):
        super().update(delta)
        self.animate(delta)

    def render(self, surface, camera):
        x = self.x + camera.x
        y = self.y + camera.y
        surface.blit(self.image, (x, y), pygame.Rect(ENEMY_SIZE * self.currentFrame, 0, self.width, self.height))