from src.globals import TILE_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH
from src.camera import Camera
from src.map import Map

class Level:
    def __init__(self):
        self.camera = Camera(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.map = Map("res/maps/test_map_1.tmx", self.camera)
        self.map.load()

    def preUpdate(self, delta, inputMap):
        self.map.preUpdate(delta, inputMap)

    def postUpdate(self, delta):
        self.map.postUpdate(delta)
        self.camera.update(self.map.player)
        
    def update(self, delta):
        self.map.update(delta)

    def process(self, delta, inputMap):
        self.preUpdate(delta, inputMap)
        self.update(delta)
        self.postUpdate(delta)

    def render(self, surface):
        self.map.render(surface)