import pygame

class Camera:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.camera = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, target):
        self.x = -target.x + int(1024 / 2)
        self.y = -target.y + int(768 / 2)
        self.camera = pygame.Rect(self.x, self.y, self.width, self.height)