class GameStats:        # ゲームの進行更新

    def __init__(self, ai_game):        #初期化
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False    #　ゲームが起動されたばかりのとき状態。
        
        self.high_score = 0         # 最大スコアをリセットしない

    def reset_stats(self):      #初期化変数
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

