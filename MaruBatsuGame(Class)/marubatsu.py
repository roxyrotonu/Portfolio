from enum import Enum

from mbexception import MBException,OutOfBoundError,AlreadyExistError,FormatError

# marubatsu.py

# from ファイル名 import クラス名
# 表示、入力を独立させたい。　別クラスで実現
# ビジネスロジックを単独のクラスにまとめる。

class MaruBatsu :

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYXZ"
    Z_ALPHABET = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    # 日本語をint()で数値に置き換え、そのインデックスで参照する。

    class Player(Enum):
        NONE = " • " 
        MARU = " ○ "  
        BATSU = " x " 

    def __init__(self,size) :
        self.size = size
        self.field = []   
        self.turn = self.Player.MARU 
        self.initialize() 
        self.game_ongoing = True

    def initialize(self): 
        """初期化""" 
        for _ in range(self.size): 
            x_list =[] 
            for _ in range(self.size): 
                x_list.append(self.Player.NONE) 
            self.field.append(x_list) 
        print(self.field) 

    def change_int(self,pos):
        """A ~ Z を 数値に置き換える関数 A:1 Z:26"""
        pos = (pos).upper()
        num = MaruBatsu.ALPHABET.find(pos) 
        if num == -1: # 全角のアルファベットを数値に置き換える
            num = MaruBatsu.Z_ALPHABET.find(pos)
        return num
    
    def getpos(self,pos): 
        """x,y並べ替え→数値変換→配置可能チェック"""
        if pos[0].isdigit():
            x = self.change_int(pos[1]) #アルファベット
            y = int(pos[0]) #数字
        else:
            x = self.change_int(pos[0]) #アルファベット
            y = int(pos[1]) #数字

        if x >= self.size or y >= self.size:
            raise OutOfBoundError(pos)
        if self.field[x][y] != self.Player.NONE:
            raise AlreadyExistError(pos)
        
        return x,y 
        

    def player_change(self):
        if self.turn == self.Player.MARU:
            self.turn = self.Player.BATSU
        else:
            self.turn = self.Player.MARU

    def play_turn(self,pos):
        self.error_check_all(pos)
        x,y = self.getpos(pos)

        self.field[x][y] = self.turn

    def error_check_all(self,pos):
        """エラーであれば警告とTrueを返します。
            error_check_all()はエラーチェックのみではなく、
            インスタンス変数の書き換えまでしてしまう。
            メソッド名と実際の機能に乖離が生まれている。
            """
        
        if len(pos) != 2:
            raise FormatError(pos)
        elif pos.isdigit() or pos.isalpha() or " " in pos or "-" in pos:
            raise FormatError(pos)
        else :
            pass
    
    def check_victory(self):
        """勝利条件を満たすか確認する"""

        field = self.field
        n = self.size
        turn = self.turn
        nothing = self.Player.NONE
        win = False
        
        # 斜め判定 
        win = all([ field[(n-1)-p][p] == turn for p in range(n) ])
        win = win or all([ field[p][p] == turn for p in range(n) ])
        # 縦判定 [x][y] 
        win = win or any([all([field[x][p] == turn for p in range(n)]) for x in range(n) ])
        # 横判定 [x][y]
        win = win or any([all([field[p][y] == turn for p in range(n)]) for y in range(n) ])
        
        # 全埋まり判定 縦横判定が全部noneではない場合。
        self.game_ongoing = not all([all([field[x][y] != nothing for x in range(n)]) for y in range(n) ])

        return win
    
    # クラスの中に、input処理を入れたくない。

    # -1 

    # error_check(pos)

    # if x is None:
    #     continue 