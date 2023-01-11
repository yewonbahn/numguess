from random import choice,shuffle

doors = [0,0,1] # sport car =1 
# 5 번 게임 반복 구현 셋팅
for i in range(5):
    shuffle(doors)
    choice(doors)
    