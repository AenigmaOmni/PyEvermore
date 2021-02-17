import pygame
from pygame.locals import *
from src.level import Level
from src.inputMap import InputMap

class Game:
    def __init__(self, window_width, window_height, design_width, design_height, title):
        self.running = True
        self.on_init(window_width, window_height, design_width, design_height, title)
        self.level = Level()
        self.lastTime = 0
        self.cameraScale = 3
        self.inputMap = InputMap()
        self.post_init(title)

    def run(self):
        while self.running:
            self.processEvents()
            self.update()
            self.render()
        self.cleanUp()

    def processEvents(self):
        self.inputMap.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            self.inputMap.d = True
        if keys[K_a]:
            self.inputMap.a = True
        if keys[K_s]:
            self.inputMap.s = True
        if keys[K_w]:
            self.inputMap.w = True

    def update(self):
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        delta = (t - self.lastTime) / 1000.0
        self.lastTime = t

        self.level.process(delta, self.inputMap)

    def render(self):
        self.screen.fill((0,0,0))
        self.level.render(self.backBuffer)
        self.screen.blit(self.backBuffer, (0 + self.level.camera.x, 0 + self.level.camera.y))
        pygame.display.flip()

    def cleanUp(self):
        pygame.quit()

    def on_init(self, width, height, dw, dh, title):
        pygame.init()
        self.size = self.width, self.height = width, height
        self.design_width = dw
        self.design_height = dh
        self.dSize = self.design_width, self.design_height
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def post_init(self, title):
        pygame.display.set_caption(title)
        self.backBuffer = pygame.Surface((self.level.tiled_map.width * 32, 
            self.level.tiled_map.height * 32), pygame.HWSURFACE | pygame.DOUBLEBUF)