# 第 6 回
## 打って！こうかとん（ ex06/game.py)
### ゲーム概要
- ex06/game.pyを実行すると，こうかとんを移動させ銃弾で敵を打って殺す
- こうかとんが敵と接触するとゲームオーバーで終了すると　
- こうかとんが全部敵が殺したらレベルアップして、も一度ゲームする。
- 敵だんだん下まで移動する
- 敵一つ殺したら５０点くれます
- 最高点数は中上で表示します
- 今の点数は右上で表示します
- 残りのチャンスは左上で図の形で表示します
- こうかとんが四回のチャンスがあって、できるだけ高い点数を取って！！！
### 操作方法
- 矢印キーでこうかとんを敵にぶつからないように左右に移動。
- SPACEでこうかとんが攻撃します。 敵を消す。
- 4回のチャンスにできるだけ多めの敵を殺して、点数を取る。
### ToDo
- backgrounの設定とbackground storyの紹介
- background music の設定
- 敵をぶつかった時の音が設定
### メモ
- class Alien   敵を作る
- class Bullet  銃弾を作る
- class Button  スタートのボタンを作る
- class Game_states 変数を初期化
- class Scoreboard  得点を作る
            
- class Ship    こうかとんがを作る
- class AlienInvasion   gameを初期化して、実行する

- C0A21078(追加)
- 発砲音を追加 SHIFTを押したときの音  
- BGMの追加　ゲーム開始時野ＢＧＭ　　 
### 参考
- https://sourceexample.com/article/jp/1a97957135d173a2eb1eec32a
- https://pygame-zero.readthedocs.io/ja/latest/builtins.html
- https://realpython.com/pygame-a-primer/
- https://blog.csdn.net/angus_17/article/details/80349561?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165820479716781685334943%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165820479716781685334943&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-80349561-null-null.142^v32^new_blog_fixed_pos,185^v2^control&utm_term=Python%E3%80%80%E9%A3%9E%E6%9C%BA&spm=1018.2226.3001.4187
- https://blog.csdn.net/u012252959/article/details/87883194?ops_request_misc=&request_id=&biz_id=102&utm_term=Python%E3%80%80%E9%A3%9E%E6%9C%BA&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-87883194.142^v32^new_blog_fixed_pos,185^v2^control&spm=1018.2226.3001.4187
- https://blog.csdn.net/qq_62870237/article/details/121384975?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165821634516782425145738%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165821634516782425145738&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-121384975-null-null.142^v32^new_blog_fixed_pos,185^v2^control&utm_term=python%E5%B0%8F%E6%B8%B8%E6%88%8F%E9%A3%9E%E6%9C%BA%E5%A4%A7%E6%88%98&spm=1018.2226.3001.4187
- https://blog.csdn.net/XiuBi_251/article/details/124389095?ops_request_misc=&request_id=&biz_id=102&utm_term=python%E5%B0%8F%E6%B8%B8%E6%88%8F%E9%A3%9E%E6%9C%BA%E5%A4%A7%E6%88%98&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-124389095.142^v32^new_blog_fixed_pos,185^v2^control&spm=1018.2226.3001.4187
- https://blog.csdn.net/weixin_54556126/article/details/121679078

