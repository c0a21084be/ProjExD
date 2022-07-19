import pygame
from pygame.sprite import Sprite


class Ship(Sprite): #kokaton

    def __init__(self, ai_game):                #初始化
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("fig/6.png")             #kokatonの画像を読み込み、その境界の長方形を取得します
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom                #新しいkokatonに、画面の下部の中央に配置します
        
        self.x = float(self.rect.x)             #kokkatonの属性xに10進値を格納します
        self.moving_right = False
        self.moving_left = False

    def update(self):               #kokatonの位置を調整します。
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x            # 根据self.x更新rect对象.

    def blitme(self):               #kokatonをかく       
        self.screen.blit(self.image, self.rect)

    def center_ship(self):     #画面の下部にkokatonを中央に配置します       
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

