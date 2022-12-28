import math
class rdh_class:
    def __init__(self):
        self.x = 0
        self.y = 140
        self.speed = 3
        self.jump = False
        self.jump_vel = 5
        self.move_left = False
        self.move_right = False
        self.left = False
        self.right = True

        #COMBAT
        self.player_get_dmg = False
        self.cmb1 = False


        self.camera_x = 0
        self.camera_y = 0
        #=-=
        self.run_left_list = []
        self.run_right_list = []
        self.r_frame_left = 0
        self.r_frame_right = 0
        #=-=
        self.idle_left_list = []
        self.idle_right_list = []
        self.i_frame_left = 0
        self.i_frame_right = 0
        #=-=
        self.jump_left_list = []
        self.jump_right_list = []
        self.j_frame_left = 0
        self.j_frame_right = 0
        #=-=
        self.cmb1_left_list = []
        self.cmb1_right_list = []
        self.c1_frame_left = 0
        self.c1_frame_right = 0


        self.r,self.g,self.b = (255,0,0),(0,255,0),(0,0,255)
        self.rect = ((self.x - self.camera_x + 2, self.y + 16 , 16,20))
    def update(self, pg, window):
        self.move_left = False
        self.move_right = False

        self.rect = ((self.x - self.camera_x + 2, self.y + 16 , 16,20))
        self.rect = pg.draw.rect(window, (self.b),(self.rect),1)


        self.keyinput = pg.key.get_pressed()
        #X,Y MOVEMENT
        if self.keyinput[pg.K_a] and self.cmb1 == False:
            self.x -= self.speed
            self.move_left = True
            self.left = True
            self.right = False
            self.camera_x -= 2

        if self.keyinput[pg.K_d] and self.cmb1 == False:
            self.x += self.speed
            self.move_right = True
            self.right = True
            self.left = False
            self.camera_x += 2


        #CAMERA SMOOTH SCROLLING
        if self.camera_x + 120 <= self.x:
            self.camera_x += 0.8

        if self.camera_x + 120 >= self.x:
            self.camera_x -= 0.8

        #JUMP
        if self.keyinput[pg.K_w] and self.cmb1 == False:
            self.jump = True

        if self.jump == True and self.left == True and self.right == False and self.j_frame_left >= 2:
            self.right = False
            self.speed = 1
            self.y -= self.jump_vel *1.5
            self.jump_vel -= 0.4
            self.x -= 1.5
            if self.jump_vel <-5:
                self.speed = 3
                self.jump = False
                self.jump_vel = 5
                self.y = 140
                self.j_frame_left = 0

        if self.jump == True and self.right == True and self.left == False and self.j_frame_right >= 2:
            self.left = False
            self.speed = 1
            self.y -= self.jump_vel *1.5
            self.jump_vel -= 0.4
            self.x += 1.5
            if self.jump_vel <-5:
                self.speed = 3
                self.jump = False
                self.jump_vel = 5
                self.y = 140
                self.j_frame_right = 0

        #COMBO 1
        if self.keyinput[pg.K_u] and self.player_get_dmg == False:
            self.cmb1 = True

        if self.c1_frame_right >= 22:
            self.cmb1 = False
            self.c1_frame_right = 0


        if self.c1_frame_left >= 22:
            self.cmb1 = False
            self.c1_frame_left = 0

        #PHYSICS
        if self.c1_frame_left == 1.8:
            self.x -= 15
        if self.c1_frame_left == 8.399999999999999:
            self.x -= 15
        if self.c1_frame_left == 15.900000000000016:
            self.x -= 15

        if self.c1_frame_right == 1.8:
            self.x += 15
        if self.c1_frame_right == 8.399999999999999:
            self.x += 20
        if self.c1_frame_right == 15.900000000000016:
            self.x += 20

        #print(self.c1_frame_right)

    #RUN ANIMATION
    def run_left_anim(self, pg, window):
        for num in range(1,24 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_run{num}.png")
            image.set_colorkey((255,0,255))
            self.run_left_list.append(image)
            window.blit(self.run_left_list[int(self.r_frame_left)], (self.x - self.camera_x, self.y))
        self.r_frame_left += 00.5

    def run_right_anim(self, pg, window):
        for num in range(1,24 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_run{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.run_right_list.append(image)
            window.blit(self.run_right_list[int(self.r_frame_right)], (self.x - self.camera_x, self.y))
        self.r_frame_right += 00.5

    #IDLE ANIMATION
    def idle_left_anim(self, pg, window):
        for num in range(1,18 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_idle{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.idle_left_list.append(image)
            window.blit(self.idle_left_list[int(self.i_frame_left)],(self.x - self.camera_x, self.y))
        self.i_frame_left += 00.3

    def idle_right_anim(self, pg, window):
        for num in range(1,18 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_idle{num}.png")
            image.set_colorkey((255,0,255))
            self.idle_right_list.append(image)
            window.blit(self.idle_right_list[int(self.i_frame_right)],(self.x - self.camera_x, self.y))
        self.i_frame_right += 00.3

    #JUMP ANIMATION
    def jump_left_anim(self, pg,window):
        for num in range(1,17 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_jump{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.jump_left_list.append(image)
            window.blit(self.jump_left_list[int(self.j_frame_left)],(self.x - self.camera_x, self.y))
        self.j_frame_left += 00.60


    def jump_right_anim(self, pg,window):
        for num in range(1,17 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_jump{num}.png")
            image.set_colorkey((255,0,255))
            self.jump_right_list.append(image)
            window.blit(self.jump_right_list[int(self.j_frame_right)],(self.x - self.camera_x, self.y))
        self.j_frame_right += 00.60

    #COMBO 1 ANIMATION
    def cmb1_left_anim(self, pg,window):
        for num in range(1,22 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_firstcmb{num}.png")
            image.set_colorkey((255,0,255))
            self.cmb1_left_list.append(image)
            window.blit(self.cmb1_left_list[int(self.c1_frame_left)],(self.x - self.camera_x - 10, self.y))
        self.c1_frame_left += 00.3

    def cmb1_right_anim(self, pg,window):
        for num in range(1,22 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_firstcmb{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.cmb1_right_list.append(image)
            window.blit(self.cmb1_right_list[int(self.c1_frame_right)],(self.x - self.camera_x - 10, self.y))
        self.c1_frame_right += 00.3

rdh = rdh_class()
