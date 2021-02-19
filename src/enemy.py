import pygame
from pygame.locals import *
from src.globals import *
from src.actor import Actor

class Enemy(Actor):
    def __init__(self, path):
        super().__init__()
        self.maxFrames = 2
        self.load(path)
        self.collisionMask = ENEMY_MASK
        self.hitBumpDirection = "down"
        self.hitBumpTime = 0.1
        self.hitBumpSpeed = 350
        self.regularSpeed = self.speed
        self.hitBumpTimer = 0
        self.hit = False
        self.walkAI = None
        self.autoTurnOffWalk = False

    def applyWalkAI(self, ai):
        self.walkAI = ai

    def load(self, path):
        self.image = pygame.image.load(path)

    def update(self, delta, inputMap=None):
        super().update(delta)
        if not self.walkAI == None:
            self.walkAI.update(delta)

        if self.hit:
            self.hitBumpTimer += delta
            if self.hitBumpTimer >= self.hitBumpTime:
                self.hit = False
                self.dx = 0
                self.dy = 0
                self.hitBumpTimer = 0
                self.speed = self.regularSpeed

        if self.hit:
            if self.hitBumpDirection == "left":
                self.dx = -1
                self.dy = 0
            elif self.hitBumpDirection == "right":
                self.dx = 1
                self.dy = 0
            elif self.hitBumpDirection == "down":
                self.dx = 0
                self.dy = 1
            elif self.hitBumpDirection == "up":
                self.dy = 0
                self.dy = -1

    def preUpdate(self, delta):
        super().preUpdate(delta)
        if not self.walkAI == None:
            self.walkAI.preUpdate(delta)

    def postUpdate(self, delta):
        if not self.walkAI == None:
            self.walkAI.postUpdate(delta)
        super().postUpdate(delta)

    def takeHit(self, damage, direction):
        self.hit = True
        self.hitBumpDirection = direction
        self.speed = self.hitBumpSpeed

