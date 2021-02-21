import random

class WanderAI:
    def __init__(self, entity, walkTime, cooldownTime, speed):
        self.entity = entity
        self.entity.speed = speed
        self.entity.regularSpeed = speed
        self.walkTime = walkTime + random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
        self.cooldownTime = cooldownTime + random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
        self.walkTimer = 0
        self.cooldownTimer = 0
        self.walking = False
        self.cooling = False

    def walk(self):
        random.seed()
        choice = [1, 2, 3, 4]
        rand = random.choice(choice)
        self.walking = True
        if rand == 1:
            self.entity.dx = -1
            self.entity.dy = 0
        elif rand == 2:
            self.entity.dx = 1
            self.entity.dy = 0
        elif rand == 3:
            self.entity.dy = 1
            self.entity.dx = 0
        elif rand == 4:
            self.entity.dy = -1
            self.entity.dx = 0
    
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