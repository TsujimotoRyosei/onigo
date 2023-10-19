import random
import math
import sys

player_x = int(random.randrange(0,11))
player_y = int(random.randrange(0,11))
fugitive_x = int(random.randrange(0,11))
fugitive_y = int(random.randrange(0,11))
turn_count = 0
charge = 0
def calc(x1,y1,x2,y2):
    x = x1 - x2
    y = y1 - y2
    distance = math.sqrt(x**2 + y**2)
    return distance

def fugitive_move(fugitive_x,fugitive_y,player_x,player_y):
    fugitive_ch = str(random.randrange(0,2))
    if fugitive_ch == "0":
        if player_x <= fugitive_x:
            fugitive_x += 1
        else:
            fugitive_x -= 1
    else:
        if player_y <= fugitive_y:
            fugitive_y += 1
        else:
            fugitive_y -=1
    return fugitive_x,fugitive_y

while player_x != fugitive_x or player_y != fugitive_y:
    if turn_count >= 1 and charge < 3:
        fugitive_x,fugitive_y = fugitive_move(fugitive_x,fugitive_y,player_x,player_y)
    if charge == 6:
        charge = 0
    if charge == 3:
        print("技を発動しました")
        print("逃走者は3ターン停止します")
    distance = calc(player_x,player_y,fugitive_x,fugitive_y)
    print(player_x,player_y)
    print(fugitive_x,fugitive_y)
    print("逃走者との距離は"+ str(distance))
    print("w:上 s:下 a:左 d:右")
    player_ch = input()
    if player_ch == "w": #上
        player_y +=  1
    elif player_ch == "s": #下
        player_y -= 1
    elif player_ch == "d": #右
        player_x += 1
    elif player_ch == "a": #左
        player_x -= 1
    elif player_ch == "q": #ゲーム終了
        print("鬼ごっこを終了します")
        sys.exit(0)
    turn_count += 1
    charge += 1
print("捕まえました")