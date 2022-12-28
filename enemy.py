import random
import player
import pygame as pg
class slime_class:
    def __init__(self, x):
        self.x = x
        self.y = 160
        self.j_vel = 5
        self.enem = []
        self.left = False
        self.right = False
        self.jump = False


        self.j_count = 10
        self.j_cd = False
        self.rect = pg.Rect((self.x - player.rdh.camera_x, self.y, 16,16))
    def update(self, pg, window):
        self.rect = pg.Rect((self.x - player.rdh.camera_x, self.y, 16,16))
        pg.draw.rect(window,(255,255,255), (self.rect),1)

        #movement
        self.j_count += 0.2
        if self.j_count >= 9:
            #self.left = True
            self.j_count = 10

        #print(self.j_count)

        # AI MOVEMENT RIGHT
        if self.jump == True and self.right == True:
            self.y -= self.j_vel
            self.j_vel -= 0.5
            self.x += 1
            if self.j_vel <-5:
                self.jump = False
                self.j_vel = 5
                self.y = 160

        if player.rdh.x >= self.x +15 and self.j_count == 10:
            self.j_count = 0
            self.right = True
            self.jump = True

        if not player.rdh.x >= self.x:
            self.right = False

        # AI MOVEMENT LEFT

        if self.jump == True and self.left == True:
            self.y -= self.j_vel
            self.j_vel -= 0.5
            self.x -= 1
            if self.j_vel <-5:
                self.jump = False
                self.j_vel = 5
                self.y = 160

        if player.rdh.x <= self.x -15 and self.j_count == 10:
            self.j_count = 0
            self.left = True
            self.jump = True

        if not player.rdh.x <= self.x:
            self.left = False



slime = slime_class(random.randint(0,100))
