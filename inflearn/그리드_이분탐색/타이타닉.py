N,M = map(int,input().split())
passenger = list(map(int,input().split()))
passenger.sort()
cnt = 0
print(passenger)
while passenger:
    if len(passenger)== 1:
        cnt+=1
        break
    if passenger[0]+passenger[-1]>M:
        passenger.pop()
        cnt+=1
    else:
        passenger.pop(0)
        passenger.pop()
        cnt+=1

print(cnt)
