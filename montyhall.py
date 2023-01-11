from random import choice,shuffle

doors = [0,0,1] # sport car =1 
notchange_cnt = 0
change_cnt =0

# 100번 게임 반복 구현 셋팅
for i in range(10000):
    shuffle(doors)
    answer=choice(doors)
    if answer==1:
        notchange_cnt+=1
    else:
        change_cnt+=1
print((change_cnt/10000)*100,"%",(notchange_cnt/10000)*100,"%")

    