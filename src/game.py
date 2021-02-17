import pygame
from pygame.locals import *
from src.level import Level

class Game:
    def __init__(self, width, height, title):
        self.running = True
        self.on_init(width, height, title)
        self.level = Level()
        self.lastTime = 0

    def run(self):
        while self.running:
            self.processEvents()
            self.update()
            self.render()
        self.cleanUp()

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        delta = (t - self.lastTime) / 1000.0
        self.lastTime = t
        
        self.level.update(delta)

    def render(self):
        self.screen.fill((0,0,0))
        self.level.render(self.screen)
        pygame.display.flip()

    def cleanUp(self):
        pygame.quit()

    def on_init(self, width, height, title):
        pygame.init()
        self.size = self.width, self.height = width, height
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)