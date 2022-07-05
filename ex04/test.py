import pygame as pg
import sys

def main():

     clock= pg.time.Clock()

     pg.display.set_caption("The First Pygame")
     screen = pg.display.set_mode((800,600))

     tori_img = pg.image.load("fig/5.png")
     tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
     tori_rect = tori_img.get_rect()
     tori_rect.center = 700,400
     screen.blit(tori_img, tori_rect)

    # fonto = pg.font.Font(None, 80)
    # txt  = fonto.render(str(tmr), True, WHITE)
    # screen.blit(txt, (300, 200))
    
     pg.display.update()

     clock.tick(0.2)
     for event in pg.event.get():
        if event.type == pg.QUIT: return
        if event.type == pg.KEYDOWN and event.key == pg.K_F1:
            screen = pg.display.set_mode((800,600), pg.FULLSCREEN)
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            screen = pg.display.set_mode((800,600)) 
        #if event.type == pg.MOUSEBUTTONDOWN:
        key_lst = pg.key.get_pressed()
        print(key_lst[pg.K_SPACE])
        print(pg.mouse.get_pos())
    #pass
    

if __name__ == '__main__':  
    pg.init()
    main()
    pg.quit()
    sys.exit()