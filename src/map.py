from src.mapRenderer import MapRenderer
from pytmx.util_pygame import load_pygame
import pygame
from pygame.locals import *
from src.globals import *
from src.player import Player

class Map:
    def __init__(self, path, cam):
        self.tiled_map = load_pygame(path)
        self.staticColliders = []
        self.entities = []
        self.camera = cam

    def load(self):
        self.player = Player()
        self.entities.append(self.player)
        self.loadStaticColliders()
        self.getPlayerStart()
        self.mapRenderer = MapRenderer(self.player)

    def preUpdate(self, delta, inputMap):
        for entity in self.entities:
            if isinstance(entity, Player):
                entity.preUpdate(delta, inputMap)
            else:
                entity.preUpdate(delta)

    def update(self, delta):
        for entity in self.entities:
            entity.update(delta)
        self.checkEntityStaticCollision(delta)

    def postUpdate(self, delta):
        for entity in self.entities:
            entity.postUpdate(delta)

    def loadStaticColliders(self):
        colliders = self.tiled_map.get_layer_by_name("Blocked")
        for collider in colliders:
            self.staticColliders.append(pygame.Rect(collider.x, collider.y, collider.width, collider.height))

    def checkEntityStaticCollision(self, delta):
        for static in self.staticColliders:
            for en in self.entities:
                if static.colliderect(en.getMoveRect(delta)):
                    en.dx = 0
                    en.dy = 0

    def getPlayerStart(self):
        obj = self.tiled_map.get_object_by_name("Start")
        tx = int(obj.x / TILE_SIZE)
        ty = int(obj.y / TILE_SIZE)
        self.player.x = tx * TILE_SIZE
        self.player.y = ty * TILE_SIZE

    def render(self, surface):
        self.mapRenderer.render(self.camera, self.tiled_map, surface, self.entities)