import pygame
from pygame import sprite
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)                  #正しい位置を設定した後、（0、0）で弾丸を表す長方形を作成します
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)                 #銃弾の個数を保存します

    def update(self):   #弾丸を打つ
        
        self.y -= self.settings.bullet_speed                    
        self.rect.y = self.y                            #弾丸の位置を更新します

    def draw_bullet(self):  #弾丸を描く
    
        pygame.draw.rect(self.screen, self.color, self.rect)
