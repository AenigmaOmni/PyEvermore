import pygame
from src.actor import Actor
from src.globals import *
from pygame.locals import *
from src.weapon import Weapon

class Player(Actor):
    def __init__(self):
        path = "res/sprites/hero_1/"
        super().__init__()
        self.drawX = 0 + GAME_WIDTH / 2 - PLAYER_SIZE / 2
        self.drawY = 0 + GAME_HEIGHT / 2 - PLAYER_SIZE / 2
        self.rect = pygame.Rect(0, 0, 12, 12)
        self.weapon = Weapon()
        self.weapon.loadImage("res/sprites/sword_1.png")
        self.load(path + "walk_down.png", path + "walk_up.png", path + "walk_left.png", path + "walk_right.png")
        self.attacking = False
        self.attackCooldown = False
        self.attackCooldownTime = 0.3
        self.attackCooldownTimer = 0
        self.attackTime = 0.2
        self.attackTimer = 0

    def renderPlayer(self, surface):
        surface.blit(self.image, (self.drawX, self.drawY), 
            pygame.Rect(PLAYER_SIZE * self.currentFrame, 0, self.width, self.height))

    def renderWeapon(self, surface):
        self.weapon.render(surface)

    def render(self, surface):
        if self.dir == "up":
            self.renderWeapon(surface)
            self.renderPlayer(surface)
        elif self.dir == "down":
            self.renderPlayer(surface)
            self.renderWeapon(surface)
        elif self.dir == "left":
            self.renderWeapon(surface)
            self.renderPlayer(surface)
        elif self.dir == "right":
            self.renderPlayer(surface)
            self.renderWeapon(surface)    

    def getInput(self, delta, inputMap):
        if inputMap.w == True:
            self.dy = -1
            self.dir = "up"
        if inputMap.s == True:
            self.dy = 1
            self.dir = "down"
        if inputMap.a == True:
            self.dx = -1
            self.dir = "left"
        if inputMap.d == True:
            self.dx = 1
            self.dir = "right"
        if inputMap.space == True:
            if not self.attackCooldown:
                if not self.attacking:
                    self.attacking = True
                    self.weapon.attacking = True

    def preUpdate(self, delta, inputMap):
        super().preUpdate(delta)
        self.getInput(delta, inputMap)
    
    def postUpdate(self, delta):
        super().postUpdate(delta)
        self.weapon.update(delta, self)
        if self.lastDir != self.dir:
            self.lastDir = self.dir
            self.switchAnim()
        if self.attacking:
            if self.dir == "left":
                self.currentFrame = 0
            elif self.dir == "down":
                self.currentFrame = 3
            elif self.dir == "up":
                self.currentFrame = 2
            elif self.dir == "right":
                self.currentFrame = 1

    def update(self, delta):
        super().update(delta)
        if self.attacking:
            self.attackTimer += delta
            if self.attackTimer >= self.attackTime:
                self.attackTimer = 0
                self.attacking = False
                self.weapon.attacking = False
                self.attackCooldown = True
        if self.attackCooldown:
            self.attackCooldownTimer += delta
            if self.attackCooldownTimer >= self.attackCooldownTime:
                self.attackCooldown = False
                self.attackCooldownTimer = 0
