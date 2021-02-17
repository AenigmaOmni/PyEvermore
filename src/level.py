from src.levelRender import LevelRender
from src.player import Player

class Level:
    def __init__(self):
        self.levelRenderer = LevelRender()
        self.entities = []
        self.entities.append(Player())
    
    def preUpdate(self, delta, inputMap):
        for entity in self.entities:
            entity.preUpdate(delta, inputMap)

    def postUpdate(self, delta, inputMap):
        for entity in self.entities:
            entity.postUpdate(delta, inputMap)

    def update(self, delta, inputMap):
        for entity in self.entities:
            entity.update(delta, inputMap)

    def process(self, delta, inputMap):
        self.preUpdate(delta, inputMap)
        self.update(delta, inputMap)
        self.postUpdate(delta, inputMap)

    def render(self, surface):
        self.levelRenderer.render(surface, self.entities)