n,m = map(int,input().split())
arr = list(map(int,input().split()))
lt = 0
rt = 1
tot = arr[lt]
cnt = 0
while lt<8:
    
    if tot == m:
        cnt+=1
        lt +=1
        rt +=1
        tot = arr[lt]
    elif tot <m:
        tot += arr[rt]
        rt+=1
    elif tot >m:
        lt +=1
        rt = lt+1
        tot = arr[lt]
print()

