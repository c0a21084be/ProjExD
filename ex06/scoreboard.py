
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:       # 得点を表す

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.tect_color = (30, 30, 30)          #　字体の設定
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()               #　得点の更新
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
    
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.tect_color, self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()               # 画面右上にスコアを表示する
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):               # 得点を表示する
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.tect_color, self.settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()             # 画面の上部中央に最高のスコアを配置します
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):             #新しいトップスコアが作成されたかどうかを確認
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.tect_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()               # 画面右上にスコアを表示する
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):               # 残りの敵の数を表示
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

