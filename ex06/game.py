import sys
from time import sleep
import pygame
from pygame.constants import  MOUSEBUTTONDOWN
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard  
#C0A21078
from pygame import mixer


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("打って！こうかとん")

        #ゲームの統計を保存するインスタンスを作成する
        #スコアボードを作成します
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #再生ボタンを作成
        self.play_button = Button(self, "Play")

    def run_game(self):
        # start the game
        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_screen()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _update_bullets(self):
        #弾丸の位置を更新し、欠落している弾丸を削除します
        #弾丸の位置を更新します。
        self.bullets.update()

        #不足している箇条書きを削除する
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #弾丸が敵に当たったかどうかを確認します
        #はいの場合、対応する弾丸と敵を削除します
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
        if not self.aliens:
            #既存の弾丸を削除し、敵の新しいグループを作成します
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            #レベルアップ
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        #宇宙船がエイリアンに襲われたときの反応
        if self.stats.ships_left > 0:
            # ships_left-1
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #残りの敵と弾丸を空にする
            self.aliens.empty()
            self.bullets.empty()

            #tekiの新しいグループを作成し、画面の下部にkokkatonを中央に配置します
            self._create_fleet()
            self.ship.center_ship()
            # stop
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
    
         #  画面の端に敵がいるかどうかを確認
        self._check_fleet_edges()
        self.aliens.update()
        # 接触判定
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # tekiが画面の下部に到達したかどうかを確認します
        self._check_aliens_bottom()

    def _check_events(self):
        #ケースとマウスイベントに応答する
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        #プレーヤーが再生ボタンをクリックすると新しいゲームを開始します
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # ゲーム設定をリセット
            self.settings.initialize_dynamic_settings()
            # ゲーム情報をリセット
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 残りのtekiと弾丸を空にします
            self.aliens.empty()
            self.bullets.empty()

            # tetkiの新しいグループを作成し、kokatoを中央に配置します
            self._create_fleet()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        # 応答ボタン
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            #C0A21078
            mixer.init()
            mixer.music.load("発砲音.mp3")
            mixer.music.play(1)

    def _check_keyup_events(self, event):  
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):    # tekiの人口を作成する
        # tekiを作成し、何人のtekiが一列に収まるかを数えます
        # tekiの間隔はtekiの幅です
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_alien_x = available_space_x//(2*alien_width)

        # 画面が保持できるtekiの行数を計算します
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3*alien_height) - ship_height)
        number_rows = available_space_y//(2*alien_height)

        # tekiの群集を作成する
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._creat_alien(alien_number, row_number)

    def _check_fleet_edges(self):               # 
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():             # 敵のグループ全体を下に移動し、方向を変えます
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _creat_alien(self, alien_number, row_number):
        alien = Alien(self)                 # 敵を作成し、現在の行に追加します。
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_screen(self):                   # 画面の画像を更新し、新しい画面に切り替えます。
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.sb.show_score()                #スコアを表示

        if not self.stats.game_active:
            self.play_button.draw_button()              #ゲームが非アクティブの場合、再生ボタンが描画されます

        pygame.display.flip()                   #最後に描画した画面を表示する

    def _check_aliens_bottom(self):                 #kokatonが画面の下部に到達したかどうかを確認してください
        
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break


if __name__ == '__main__':              #ゲームインスタンスを作成してゲームを実行します。
    ai = AlienInvasion()
    ai.run_game()

