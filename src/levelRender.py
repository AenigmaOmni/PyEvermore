from pytmx.util_pygame import load_pygame
from src.globals import *
import pygame

class LevelRender:
    def __init__(self, player):
        self.player = player
        self.startX = self.player.tx - 10
        self.startY = self.player.ty - 7
        self.endX = self.player.tx + 10
        self.endY = self.player.ty + 7

    def render(self, camera, map, surface, entities):
        self.startX = self.player.tx - 10
        self.startY = self.player.ty - 10
        self.endX = self.player.tx + 10
        self.endY = self.player.ty + 10
        
        self.renderBackground(map, surface, camera)
        self.renderEntities(surface, entities, camera)
        self.renderForeground(map, surface, camera)

    def renderForeground(self, map, surface, camera):
        upper = map.layers[4]

        for x, y, image in upper.tiles():
            if x >= self.startX and x <= self.endX:
                if y >= self.startY and y <= self.endY:
                    surface.blit(image, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))

    def renderBackground(self, map, surface, camera):
        ground = map.layers[0]
        ground2 = map.layers[1]
        objects = map.layers[2]
        objects2 = map.layers[3]

        #Draw ground
        for x, y, image in ground.tiles():
            if x >= self.startX and x <= self.endX:
                if y >= self.startY and y <= self.endY:
                    surface.blit(image, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))

        #Draw ground2
        for x, y, image in ground2.tiles():
            if x >= self.startX and x <= self.endX:
                if y >= self.startY and y <= self.endY:
                    surface.blit(image, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))

        #Draw objects1
        for x, y, image in objects.tiles():
            if x >= self.startX and x <= self.endX:
                if y >= self.startY and y <= self.endY:
                    surface.blit(image, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))

        #Draw objects2
        for x, y, image in objects2.tiles():
            if x >= self.startX and x <= self.endX:
                if y >= self.startY and y <= self.endY:
                    surface.blit(image, (x * map.tilewidth + camera.x, y * map.tileheight + camera.y))

    def renderEntities(self, surface, entities, camera):
        for entity in entities:
            if entity.tx >= self.startX and entity.tx <= self.endX:
                if entity.ty >= self.startY and entity.ty <= self.endY:
                    entity.render(surface, camera)
            