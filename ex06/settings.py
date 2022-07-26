from time import sleep
import pygame

class Settings:
   

    def __init__(self):
        # 画面設定
        self.screen_width = 1200
        self.screen_height = 800
        #self.screen = pygame.image.load('pg_bg.jpg')
        self.bg_color = (152, 255, 152)
        # kokatonセットアップ
        self.ship_speed = 1.5
        self.ship_limit = 3
        # 弾丸の設定
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        # teki設定
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction が 1 の場合は右シフト、-1 の場合は左シフトを意味する。
        self.fleet_direction = 1
        # ゲームのテンポを速める
        self.speedup_scale = 1.1
        # tekiスコアの改善スピード
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ゲームの進行に伴って変化する設定の初期化"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction が 1 の場合は右、-1 の場合は左を意味する
        self.fleet_direction = 1
        # スコアリング
        self.alien_points = 50

    def increase_speed(self):
        """速度設定とtekiスコアの改善"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)

