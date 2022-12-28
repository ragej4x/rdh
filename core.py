import pygame as pg
import player , enemy
#DISPLAY
width,height = 1024,620
display = pg.display.set_mode((width,height))
window = pg.Surface((width//3, height//3))
pg.display.set_caption("RDH")

fps = pg.time.Clock()
loop = True
bg = pg.image.load("data/bg.png")

#PLAYER
def player_func():
    keyinput = pg.key.get_pressed()
    player.rdh.update(pg, window)
#RUN

    if player.rdh.move_left == True and player.rdh.move_right == False and player.rdh.jump == False:
        player.rdh.run_left_anim(pg, window)

    if player.rdh.move_right == True and player.rdh.move_left == False and player.rdh.jump == False:
        player.rdh.run_right_anim(pg, window)

#IDLE
    if player.rdh.left == True and player.rdh.move_right == False and player.rdh.move_left == False and player.rdh.jump == False and player.rdh.cmb1 == False:
        player.rdh.idle_left_anim(pg, window)

    if player.rdh.right == True and player.rdh.move_right == False and player.rdh.move_left == False and player.rdh.jump == False and player.rdh.cmb1 == False:
        player.rdh.idle_right_anim(pg, window)
#JUMP
    if player.rdh.jump == True and player.rdh.left == True :
        player.rdh.jump_left_anim(pg, window)

    if player.rdh.jump == True and player.rdh.right == True :
        player.rdh.jump_right_anim(pg, window)

#COMBAT 1
    if player.rdh.cmb1 == True and player.rdh.right == True and player.rdh.jump == False:
        player.rdh.cmb1_right_anim(pg, window)

    if player.rdh.cmb1 == True and player.rdh.left == True and player.rdh.jump == False:
        player.rdh.cmb1_left_anim(pg, window)

#fIX BUG IF "a" and "d" is helding
    if keyinput[pg.K_a] == True and keyinput[pg.K_d] == True and player.rdh.jump == False and player.rdh.cmb1 == False:
        player.rdh.idle_right_anim(pg, window)
        player.move_right = True
        player.rdh.right = True
        player.rdh.left = False

#ENEMY PHYSICS
    if player.rdh.rect.colliderect(enemy.slime.rect) and enemy.slime.jump == True:
        if enemy.slime.left == True:
            player.rdh.x -= 10
            print("DMG")
            remove(player.rdh.player_health)

        if enemy.slime.right == True:
            player.rdh.x += 10
            print("DMG")


    print(player.rdh.player_health)


#EVENT HANDLER
def event_handler():
    global loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False

    surface = pg.transform.scale(window, (width, height))
    display.blit(surface,(0,0))

    pg.display.flip()
    fps.tick(40)

while loop == True:
    window.fill(0)
    display.fill(0)
    window.blit(bg,(-250 - player.rdh.camera_x,-250))

    enemy.slime.update(pg, window)
    player_func()
    event_handler()
