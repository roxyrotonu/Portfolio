from marubatsu import MaruBatsu
from view import View
import mbexception

# user.py
# ゲームフロー
n = 3
mb = MaruBatsu(n)
v = View(mb)
v.print_field()

while mb.game_ongoing:    
    print(f"{mb.turn.value}さんの番です")
    pos = input("座標入力 a1 1a :")

    try:
        mb.play_turn(pos)
    except mbexception.MBException as e:
        print(e)
        continue

    v.print_field()

    if mb.check_victory():
        print(f"{mb.turn.value}さんの勝利です！")
        mb.game_ongoing = False
        break

    # 盤面が全て埋まった場合の処理が未解決
    mb.player_change()

    print("1turn_end")