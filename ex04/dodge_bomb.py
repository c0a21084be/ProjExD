import random
import pygame as pg
import sys
import math

def main():

    clock= pg.time.Clock()

    pg.display.set_caption("Run away! KouKaTon !!!")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc  = pg.image.load("pg_bg.jpg")
    bgimg_rct  = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
    # practice 3
    kkimg_sfc = pg.image.load(f"fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400

    #practice 5
    bmimg_sfc_1 = pg.Surface((20,20))
    bmimg_sfc_1.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc_1,(255,0,0), (10,10), 10)
    bmimg_rct_1 = bmimg_sfc_1.get_rect()
    bmimg_rct_1.centerx = random.randint(0, screen_rct.width)
    bmimg_rct_1.centery = random.randint(0, screen_rct.height)
    vx1, vy1 = +1, +1

    # bmimg_sfc_2 = pg.Surface((20,20))
    # bmimg_sfc_2.set_colorkey((0,0,0))
    # pg.draw.circle(bmimg_sfc_2,(255,0,0), (10,10), 10)
    # bmimg_rct_2 = bmimg_sfc_2.get_rect()
    # bmimg_rct_2.centerx = random.randint(0, screen_rct.width)
    # bmimg_rct_2.centery = random.randint(0, screen_rct.height)
    # vx2, vy2 = +2, +2


    # bmimg_sfc_3 = pg.Surface((20,20))
    # bmimg_sfc_3.set_colorkey((0,0,0))
    # pg.draw.circle(bmimg_sfc_3,(255,0,0), (10,10), 10)
    # bmimg_rct_3 = bmimg_sfc_3.get_rect()
    # bmimg_rct_3.centerx = random.randint(0, screen_rct.width)
    # bmimg_rct_3.centery = random.randint(0, screen_rct.height)
    # vx3, vy3 = *math.pi, *math.pi

    
    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        
        #practice 2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
       
        #practice 4
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]       == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]     == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]     == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT]    == True: kkimg_rct.centerx += 1
        if c_b(kkimg_rct,screen_rct) != (1, 1):
            if key_states[pg.K_UP]       == True: kkimg_rct.centery += 1
            if key_states[pg.K_DOWN]     == True: kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT]     == True: kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT]    == True: kkimg_rct.centerx -= 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        bmimg_rct_1.move_ip(vx1,vy1)      
        screen_sfc.blit(bmimg_sfc_1, bmimg_rct_1)

        # bmimg_rct_2.move_ip(vx2,vy2)
        # screen_sfc.blit(bmimg_sfc_2, bmimg_rct_2)

        # bmimg_rct_3.move_ip(vx3,vy3)
        # screen_sfc.blit(bmimg_sfc_3, bmimg_rct_3)
       
        #p7
        w, h = c_b(bmimg_rct_1, screen_rct)
        vx1 *= w
        vy1 *= h
       
        # w, h = c_b(bmimg_rct_2, screen_rct)
        # vx2 *= w
        # vy2 *= h
       
        # w, h = c_b(bmimg_rct_3, screen_rct) 
        # vx3 *= w
        # vy3 *= h       
        
        #p8
        if kkimg_rct.colliderect(bmimg_rct_1):
            return


        pg.display.update()
        clock.tick(1000)

def c_b(rct,scr_rct):

    w, h = +1, +1

    if rct.left < scr_rct.left or scr_rct.right  < rct.right:  w = -1
    if rct.top  <  scr_rct.top or scr_rct.bottom < rct.bottom: h = -1

    return w, h


if __name__ == '__main__':  
    
    
    pg.init()
    main()
    pg.quit()
    sys.exit()