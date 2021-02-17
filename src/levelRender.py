from pytmx.util_pygame import load_pygame

class LevelRender:
    def __init__(self):
        pass

    def render(self, map, surface, entities):
        self.renderBackground(map, surface)
        self.renderEntities(surface, entities)
        self.renderForeground(map, surface)

    def renderForeground(self, map, surface):
        upper = map.layers[4]

        for x, y, image in upper.tiles():
            surface.blit(image, (x * map.tilewidth, y * map.tileheight))

    def renderBackground(self, map, surface):
        ground = map.layers[0]
        ground2 = map.layers[1]
        objects = map.layers[2]
        objects2 = map.layers[3]

        for x, y, image in ground.tiles():
            surface.blit(image, (x * map.tilewidth, y * map.tileheight))

        for x, y, image in ground2.tiles():
            surface.blit(image, (x * map.tilewidth, y * map.tileheight))

        for x, y, image in objects.tiles():
            surface.blit(image, (x * map.tilewidth, y * map.tileheight))

        for x, y, image in objects2.tiles():
            surface.blit(image, (x * map.tilewidth, y * map.tileheight))

    def renderEntities(self, surface, entities):
        for entity in entities:
            entity.render(surface)