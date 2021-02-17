import pygame

class Camera:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.camera = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, target):
        self.x = -target.x - (target.width / 2) + int(self.width / 2)
        self.y = -target.y - (target.height / 2) + int(self.height / 2)
        self.camera = pygame.Rect(self.x, self.y, self.width, self.height)