import pygame
from pygame.locals import *
from src.globals import *

class Weapon:
    def __init__(self):
        self.image = None
        self.weaponSprite = None
        self.attacking = False
        self.x = 0
        self.y = 0
        self.angle = 180
        self.image = None
        self.hitSprite = None
        self.hitImageX = self.x
        self.hitImageY = self.y
        self.hitAngle = 180
        self.flipX = False
        self.flipY = False
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.collisionMask = WEAPON_MASK

    def loadImage(self, path):
        self.image = pygame.image.load(path)
        self.hitImage = pygame.image.load("res/sprites/slash.png")

    def update(self, dt, player):
        self.updatePositionals(dt, player)
        if player.dir == "down":
            self.rect.x = player.x
            self.rect.y = player.y + 25
        elif player.dir == "up":
            self.rect.x = player.x
            self.rect.y = player.y - 25
        elif player.dir == "left":
            self.rect.y = player.y
            self.rect.x = player.x - 25
        elif player.dir == "right":
            self.rect.y = player.y
            self.rect.x = player.x + 25

    def render(self, surface):
        self.weaponSprite = pygame.transform.rotate(self.image, self.angle)
        self.hitSprite = pygame.transform.rotate(self.hitImage, self.hitAngle)
        if self.flipX or self.flipY:
            self.hitSprite = pygame.transform.flip(self.hitImage, self.flipX, self.flipY)
        surface.blit(self.weaponSprite, (self.x, self.y))
        if(self.attacking):
            surface.blit(self.hitSprite, (self.hitImageX, self.hitImageY))

    def updatePositionals(self, dt, player):
        if player.dir == "down":
            if player.currentFrame == 0 or player.currentFrame == 2:
                self.x = player.drawX - 8
                self.y = player.drawY - 9
            elif player.currentFrame == 1:
                self.x = player.drawX - 9
                self.y = player.drawY - 9
            elif player.currentFrame == 3:
                self.x = player.drawX - 6
                self.y = player.drawY - 9
            if self.attacking:
                self.x = player.drawX - 8
                self.y = player.drawY + 21                
                self.angle = 0
                self.flipX = False
                self.flipY = False
                self.hitImageX = self.x + 10
                self.hitImageY = self.y + 10
                self.hitAngle = 0
            else:
                self.angle = 180
        elif player.dir == "left":
            if player.currentFrame == 0:
                self.x = player.drawX - 6
                self.y = player.drawY - 9
            elif player.currentFrame == 1 or player.currentFrame == 3:
                self.x = player.drawX + 2
                self.y = player.drawY - 9
            elif player.currentFrame == 2:
                self.x = player.drawX + 1
                self.y = player.drawY - 9
            if self.attacking:
                self.x = player.drawX - 26
                self.y = player.drawY + 9
                self.angle = 270
                self.hitImageX = self.x
                self.flipX = False
                self.flipY = False
                self.hitImageY = self.y - 10
                self.hitAngle = 180
            else:
                self.angle = 180
        elif player.dir == "right":
            if player.currentFrame == 0 or player.currentFrame == 2:
                self.x = player.drawX + 2
                self.y = player.drawY - 10
            elif player.currentFrame == 1:
                self.x = player.drawX - 1
                self.y = player.drawY - 7
            elif player.currentFrame == 3:
                self.x = player.drawX - 6
                self.y = player.drawY - 10
            if self.attacking:
                self.x = player.drawX + 15
                self.y = player.drawY + 11
                self.angle = 90
                self.hitImageX = self.x + 10
                self.flipX = False
                self.flipY = True
                self.hitImageY = self.y - 12
                self.hitAngle = 180
            else:
                self.angle = 180
        elif player.dir == "up":
            if player.currentFrame == 1 or player.currentFrame == 3:
                self.x = player.drawX + 11
                self.y = player.drawY- 10
            elif player.currentFrame == 0:
                self.x = player.drawX + 12
                self.y = player.drawY - 9
            elif player.currentFrame == 2:
                self.x = player.drawX + 10
                self.y = player.drawY - 10
            if self.attacking:
                self.x = player.drawX + 11
                self.y = player.drawY - 18
                self.hitImageX = self.x - 12
                self.flipX = True
                self.flipY = True
                self.hitImageY = self.y
                self.hitAngle = 180
            else:
                self.angle = 180