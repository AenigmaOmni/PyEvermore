from pytmx.util_pygame import load_pygame
from src.globals import *

class LevelRender:
    def __init__(self, player):
        self.player = player

    def render(self, map, surface, entities):
        self.renderBackground(map, surface)
        self.renderEntities(surface, entities)
        #self.renderForeground(map, surface)

    def renderForeground(self, map, surface):
        upper = map.layers[4]

        for x, y, image in upper.tiles():
            surface.blit(image, (x * map.tilewidth, y * map.tileheight))

    def renderBackground(self, map, surface):
        ground = map.layers[0]
        ground2 = map.layers[1]
        objects = map.layers[2]
        objects2 = map.layers[3]

        x = self.player.tx - 7
        y = self.player.ty - 7
        maxX = self.player.tx + 7
        maxY = self.player.ty + 7

        #render ground
        for i in range(y, maxY):  
            for j in range(x, maxX):
                gid = ground.data[i][j]
                if(map.images[gid] != None):
                    surface.blit(map.images[gid], (j * TILE_SIZE, i * TILE_SIZE))

    def renderEntities(self, surface, entities):
        for entity in entities:
            entity.render(surface)