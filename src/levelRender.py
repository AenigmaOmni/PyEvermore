from pytmx.util_pygame import load_pygame

class LevelRender:
    def __init__(self):
        self.tiled_map = load_pygame('res/maps/test_map_1.tmx')

    def render(self, surface, entities):
        self.renderBackground(surface)
        self.renderEntities(surface, entities)
        self.renderForeground(surface)

    def renderForeground(self, surface):
        upper = self.tiled_map.layers[4]

        for x, y, image in upper.tiles():
            surface.blit(image, (x * self.tiled_map.tilewidth, y * self.tiled_map.tileheight))

    def renderBackground(self, surface):
        ground = self.tiled_map.layers[0]
        ground2 = self.tiled_map.layers[1]
        objects = self.tiled_map.layers[2]
        objects2 = self.tiled_map.layers[3]

        for x, y, image in ground.tiles():
            surface.blit(image, (x * self.tiled_map.tilewidth, y * self.tiled_map.tileheight))

        for x, y, image in ground2.tiles():
            surface.blit(image, (x * self.tiled_map.tilewidth, y * self.tiled_map.tileheight))

        for x, y, image in objects.tiles():
            surface.blit(image, (x * self.tiled_map.tilewidth, y * self.tiled_map.tileheight))

        for x, y, image in objects2.tiles():
            surface.blit(image, (x * self.tiled_map.tilewidth, y * self.tiled_map.tileheight))

    def renderEntities(self, surface, entities):
        for entity in entities:
            entity.render(surface)