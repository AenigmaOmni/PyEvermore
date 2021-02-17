from src.levelRender import LevelRender
from src.player import Player

class Level:
    def __init__(self):
        self.levelRenderer = LevelRender()
        self.entities = []
        self.entities.append(Player())
    
    def update(self, delta):
        for entity in self.entities:
            entity.update(delta)

    def render(self, surface):
        self.levelRenderer.render(surface, self.entities)