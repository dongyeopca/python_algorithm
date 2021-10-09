t,m,s = list(map(int,input().split()))
d = int(input())
while d>=0:
    if d>=3600:
        t +=1
        d-=3600
    elif d>3600 and d>=60:
        m +=1
        d-=60
    else:
        s+=d
        break
while s>=60:
    s-=60
    m+=1
while m>=60:
    m-=60
    t+=1
while t>=24:
    t-=24

print(t,m,s)

