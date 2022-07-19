import pygame
from pygame.sprite import Sprite


class Alien(Sprite):                    #敵を作る

    def __init__(self, ai_game):        #敵を初期化し、開始位置を設定します
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("fig/w2.png")                    #敵の画像
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width                   #各敵は最初は画面の左上
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)                     #敵の正確な水平位置を保存します

    def update(self):                   #敵を右または左に移動   
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):                      #敵が画面の端にいる場合はTrueを返します
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
