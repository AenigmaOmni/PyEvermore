import random

class WanderAI:
    def __init__(self, entity, walkTime, cooldownTime, speed):
        self.entity = entity
        self.entity.speed = speed
        self.entity.regularSpeed = speed
        self.walkTime = walkTime
        self.cooldownTime = cooldownTime
        self.walkTimer = 0
        self.cooldownTimer = 0
        self.walking = False
        self.cooling = False

    def walk(self):
        rand = random.randrange(0, 3)
        self.walking = True
        if rand == 0:
            self.entity.dx = -1
            self.entity.dy = 0
        elif rand == 1:
            self.entity.dx = 1
            self.entity.dy = 0
        elif rand == 2:
            self.entity.dy = 1
            self.entity.dx = 0
        elif rand == 3:
            self.entity.dy = -1
            self.entity.dy = 0
    
    def stopWalking(self):
        self.entity.dx = 0
        self.entity.dy = 0
        self.walking = False
        self.walkTimer = 0
        self.cooling = True
        self.cooldownTimer = 0

    def update(self, dt):
        if not self.walking:
            if not self.cooling:
                self.walk()

    def postUpdate(self, delta):
        pass

    def preUpdate(self, delta):
        if self.walking:
            self.walkTimer += delta
            if self.walkTimer >= self.walkTime:
                self.stopWalking()

        if self.cooling:
            self.cooldownTimer += delta
            if self.cooldownTimer >= self.cooldownTime:
                self.cooling = False
                self.cooldownTimer = 0