import pygame
from pygame.locals import *
from src.globals import *
from src.actor import Actor

class Enemy(Actor):
    def __init__(self, path, entobj):
        super().__init__(entobj)
        self.maxFrames = 2
        self.load(path)
        self.collisionMask = ENEMY_MASK
        self.hitBumpDirection = "down"
        self.hitBumpTime = 0.1
        self.hitBumpSpeed = 625
        self.regularSpeed = self.speed
        self.hitBumpTimer = 0
        self.hit = False
        self.walkAI = None
        self.autoTurnOffWalk = False
        self.invicibleTime = 0.3
        self.invTimer = 0
        self.invicible = False
        self.spawnRect = None

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
        if not self.walkAI == None and not self.hit:
            self.walkAI.preUpdate(delta)
        if self.invicible:
            self.invTimer += delta
            if self.invTimer >= self.invicibleTime:
                self.invTimer = 0
                self.invicible = False

    def postUpdate(self, delta):
        self.stayInSpawnArea(delta)
        if not self.walkAI == None and not self.hit:
            self.walkAI.postUpdate(delta)
        super().postUpdate(delta)

    def takeDamage(self, damage):
        pass

    def stayInSpawnArea(self, delta):
        rect = self.getMoveRect(delta)
        point = (rect.x, rect.y)
        if not self.spawnRect.collidepoint(point):
            can = False
            self.walkAI.stopWalking()
            if self.dx == -1 and self.dy == 0:
                self.dx = 1
            elif self.dx == 1 and self.dy == 0:
                self.dx = -1
            elif self.dy == -1 and self.dx == 0:
                self.dy = 1
            elif self.dy == 1 and self.dx == 0:
                self.dy = -1
            self.walkAI.walk()
            rect = self.getMoveRect(delta)
            point = (rect.x, rect.y)
            if not self.spawnRect.collidepoint(point):
                while not can:
                    self.walkAI.walk()
                    rect = self.getMoveRect(delta)
                    point = (rect.x, rect.y)
                    if self.spawnRect.collidepoint(point):
                        can = True
                    else:
                        self.walkAI.stopWalking()

    def takeHit(self, damage, direction):
        if not self.invicible:
            self.hit = True
            self.hitBumpDirection = direction
            self.speed = self.hitBumpSpeed
            self.invicible = True
            self.takeDamage(damage)

