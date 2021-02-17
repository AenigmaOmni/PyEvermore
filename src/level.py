from src.globals import WINDOW_HEIGHT, WINDOW_WIDTH
import pygame
from pygame.locals import *
from src.levelRender import LevelRender
from src.player import Player
from pytmx.util_pygame import load_pygame
from src.camera import Camera

class Level:
    def __init__(self):
        self.tiled_map = load_pygame('res/maps/test_map_1.tmx')
        self.staticColliders = []
        self.entities = []
        self.on_init()
        self.camera = Camera(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    def on_init(self):
        self.player = Player()
        self.entities.append(self.player)
        self.loadStaticColliders()
        self.levelRenderer = LevelRender(self.player)

    def loadStaticColliders(self):
        objects = self.tiled_map.get_layer_by_name("Blocked")
        for obj in objects:
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            self.staticColliders.append(rect)

    def checkEntityStaticCollision(self, delta):
        for static in self.staticColliders:
            for en in self.entities:
                if static.colliderect(en.getMoveRect(delta)):
                    en.dx = 0
                    en.dy = 0

    def preUpdate(self, delta, inputMap):
        for entity in self.entities:
            entity.preUpdate(delta, inputMap)

    def postUpdate(self, delta, inputMap):
        for entity in self.entities:
            entity.postUpdate(delta, inputMap)

        self.camera.update(self.player)
        

    def update(self, delta, inputMap):
        for entity in self.entities:
            entity.update(delta, inputMap)
        self.checkEntityStaticCollision(delta)

    def process(self, delta, inputMap):
        self.preUpdate(delta, inputMap)
        self.update(delta, inputMap)
        self.postUpdate(delta, inputMap)

    def render(self, surface):
        self.levelRenderer.render(self.camera, self.tiled_map, surface, self.entities)