import pygame
from pygame.locals import *
from src.level import Level
from src.inputMap import InputMap
from src.globals import *

class Game:
    def __init__(self):
        self.running = True
        self.on_init()
        self.level = Level()
        self.lastTime = 0
        self.inputMap = InputMap()
        self.post_init()

    def run(self):
        while self.running:
            self.processEvents()
            self.update()
            self.render()
            self.fpsClock.tick(self.fpsLimit)

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
        self.backBuffer.fill((0,0,0))
        self.level.render(self.backBuffer)
        
        img = self.font.render("FPS: " + str(round(self.fpsClock.get_fps())), True, (255, 255, 255))
        scaled = pygame.transform.scale(self.backBuffer, self.size)

        self.screen.blit(scaled, (0,0))
        self.screen.blit(img, (20, 20))
        pygame.display.flip()

    def cleanUp(self):
        pygame.quit()

    def on_init(self):
        pygame.init()
        self.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(self.size, DOUBLEBUF | HWSURFACE)
        self.backBuffer = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), DOUBLEBUF | HWSURFACE)

    def post_init(self):
        pygame.display.set_caption(TITLE)
        self.fpsLimit = 200
        self.fpsClock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 40)