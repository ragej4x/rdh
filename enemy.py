import random
import player
import effects
import pygame as pg

class slime_class:
    def __init__(self, x):
        self.slime_idle_image = pg.image.load("data/enem_anim/slime_idle.png")
        self.slime_idle_image = pg.transform.scale(self.slime_idle_image,(20,17))
        self.x = x
        self.y = 160
        self.j_vel = 5
        self.enem = []
        self.left = False
        self.right = False
        self.jump = False
        self.health = 100

        #animation
        self.jump_left_list = []
        self.jump_right_list = []
        self.j_frame_right = 0
        self.j_frame_left = 0


        self.j_count = 10
        self.j_cd = False
        self.rect = pg.Rect((self.x - player.rdh.camera_x, self.y, 18,18))


    def update(self, pg, window):
        self.rect = pg.Rect((self.x - player.rdh.camera_x, self.y, 18,18))
        #pg.draw.rect(window,(255,255,255), (self.rect),1)

        #movement
        self.j_count += 0.3
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
                self.j_frame_right = 0

        if player.rdh.x >= self.x +1 and self.j_count == 10:
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
                self.j_frame_left = 0

        if player.rdh.x <= self.x -1 and self.j_count == 10:
            self.j_count = 0
            self.left = True
            self.jump = True

        if not player.rdh.x <= self.x:
            self.left = False

    def fx(self, window):
        #SLIME GUSH FX

            #LEFT
        if player.rdh.left == True and self.rect.colliderect(player.rdh.cmb_rect_left):
            if player.rdh.cmb1 == True and player.rdh.c1_frame_left >= 2:
                effects.fx.gush_left = True

        if effects.fx.gush_left == True:
            effects.fx.slime_gush_left_anim(pg, window)
            if effects.fx.slime_gush_frame >= 10:
                effects.fx.slime_gush_frame = 0
                effects.fx.gush_left = False

            #RIGHT
        if player.rdh.right == True and self.rect.colliderect(player.rdh.cmb_rect_right):
            if player.rdh.cmb1 == True and player.rdh.c1_frame_right >= 2:
                effects.fx.gush_right = True

        if effects.fx.gush_right == True:
            effects.fx.slime_gush_right_anim(pg, window)
            if effects.fx.slime_gush_frame >= 10:
                effects.fx.slime_gush_frame = 0
                effects.fx.gush_right = False

        """
        self.left = False
        self.right = False
        """
        print(player.rdh.c1_frame_left)


#ANIMATION
    def jump_left_anim(self, window):
        for num in range(1,27 + 1):
            image = pg.image.load(f"data/enem_anim/slime_jump{num}.png")
            image = pg.transform.flip(image, True, False)
            self.jump_left_list.append(image)
            window.blit(self.jump_left_list[int(self.j_frame_left)],(self.x - player.rdh.camera_x - 5, self.y - 7))
        self.j_frame_left += 0.8

    def jump_right_anim(self, window):
        for num in range(1,27 + 1):
            image = pg.image.load(f"data/enem_anim/slime_jump{num}.png")
            self.jump_right_list.append(image)
            window.blit(self.jump_right_list[int(self.j_frame_right)],(self.x - player.rdh.camera_x - 5, self.y - 7))
        self.j_frame_right += 0.8


slime = slime_class(random.randint(-100,0))
