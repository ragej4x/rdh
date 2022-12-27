import random

class enemy_class:
    def __init__(self, x):
        self.x = x
        self.y = 120
        self.enem = []

    def update(self, pg, window):
        for num in range(1,5):
            self.enem.append(pg.draw.rect(window,(255,255,255), (self.x, self.y, 16,20 ),1))



enem = enemy_class(random.randint(0,100))
