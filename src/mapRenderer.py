from pytmx.util_pygame import load_pygame
from src.globals import *
import pygame
from src.player import Player

class MapRenderer:
    def __init__(self, player):
        self.player = player
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0

    def render(self, camera, map, surface, entities):
        self.startX = self.player.tx - VIEW_RADIUS
        self.startY = self.player.ty - VIEW_RADIUS
        self.endX = self.player.tx + VIEW_RADIUS
        self.endY = self.player.ty + VIEW_RADIUS

        self.renderBackground(map, surface, camera)
        self.renderEntities(surface, entities, camera)
        self.renderPlayer(surface)
        self.renderForeground(map, surface, camera)

    def renderForeground(self, map, surface, camera):
        for y in range(self.startY, self.endY):
            for x in range(self.startX, self.endX):
                if not x < 0 and not y < 0:
                    tile = map.get_tile_image(x, y, 3)
                    if(tile != None):
                        surface.blit(tile, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))

    def renderBackground(self, map, surface, camera):
        for y in range(self.startY, self.endY):
            for x in range(self.startX, self.endX):
                if not x < 0 and not y < 0:
                    groundTile = map.get_tile_image(x, y, 0)
                    if(groundTile != None):
                        surface.blit(groundTile, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))
                    objectTile = map.get_tile_image(x, y, 1)
                    if(objectTile != None):
                        surface.blit(objectTile, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))
                    object2Tile = map.get_tile_image(x, y, 2)
                    if(object2Tile != None):
                        surface.blit(object2Tile, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))

    def renderEntities(self, surface, entities, camera):
        for entity in entities:
            if entity.tx >= self.startX and entity.tx <= self.endX:
                if entity.ty >= self.startY and entity.ty <= self.endY:
                    if not isinstance(entity, Player):
                        entity.render(surface, camera)

    def renderPlayer(self, surface):
        self.player.render(surface)