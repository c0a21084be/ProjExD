import pygame.font


class Button:
    def __init__(self, ai_game, msg):       #初期化
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50       #ボタンのサイズ
        self.button_color = (0, 255, 0)
        self.tect_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)          # ボタンの位置
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)         # 一回のみ

    def _prep_msg(self, msg):               #ボタンの文字
        self.msg_image = self.font.render(
            msg, True, self.tect_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):          #ボタンの色
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

