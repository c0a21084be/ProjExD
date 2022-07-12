import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    s = 0
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)
        self.sfc = pg.music.load("fig/house_lo.mp3")
        self.sfc = pg.music.play(100)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_LSHIFT]       == True: Bird.s = 2.5
        else: Bird.s = 1
        if key_states[pg.K_UP]: 
            self.rct.centery -= Bird.s
        if key_states[pg.K_DOWN]: 
            self.rct.centery +=  Bird.s
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -=  Bird.s
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx +=  Bird.s
        # # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery +=  Bird.s
            if key_states[pg.K_DOWN]: 
                self.rct.centery -=  Bird.s
            if key_states[pg.K_LEFT]: 
                self.rct.centerx +=  Bird.s
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -=  Bird.s
        self.blit(scr)
    def attack(self):
        return Shot(self)

class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)          

class Shot:

    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/beam.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.25)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.midleft = chr.rct.center

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen): 
        # 練習6
        self.rct.move_ip(+5,0)
        self.blit(scr)
        # 練習7
        if check_bound(self.rct, scr.rct) != (1,1):
            del self          

class Enemy:
    def __init__(self, vxy, scr: Screen, img):
        self.sfc = pg.image.load(img)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        
        self.rct.move_ip(self.vx, self.vy)
        
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)    
    
class goal:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((5*size, 5*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)          
class Explosion:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        self.blit(scr)
    

def main(): 
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)
    bkd1 = Bomb((255,0,0), 10, (+1,+1), scr)
    bkd2 = goal((0,255,0), 25, (+1,+1), scr)
    enm = Enemy((+1, +1), scr,"fig/alien1.gif")
   
    beams = [] 
    bombs = [(Bomb((255,0,0), 10, (+1,+1), scr))for _ in range(5)]
    while True:
        scr.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE: 
                beams.append(kkt.attack())

        kkt.update(scr)
        bkd.update(scr)
        bkd1.update(scr)
        bkd2.update(scr)
        enm.update(scr)

        
        if kkt.rct.colliderect(bkd.rct) :
            ex = Explosion("fig/1.png", 6.0, (900, 400))
            ex.update(scr)
            pg.display.update()
            pg.init()
            pg.music.load("fig/house_lo.mp3")
            pg.music.play(1)
            tkm.showwarning("GAME OVER","もう一度挑戦してね")
            return
        pg.display.update()
        clock.tick(1000)

# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
