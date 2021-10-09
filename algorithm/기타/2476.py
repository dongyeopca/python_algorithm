n= int(input())
reward = list()
count = list()
for i in range(n):
    dice = list(map(int,input().split()))
    for i in range(len(dice)):
        count.append(dice.count(dice[i]))
    if max(count) == 3:
        reward.append(10000+dice[0]*1000)
    elif max(count) == 2:
        reward.append(1000+100*dice[count.index(2)])
    elif max(count) == 1:
        reward.append(100*max(dice))
    count = list()
print(max(reward))
        