
n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
answer=0

for i in range(1,n+1):
    money = coin[-i]
    if k>=money:
        answer+=(k//money)
        k-= (k//money)*money
        

print(answer)