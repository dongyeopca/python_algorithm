e,s,m = list(map(int,input().split()))
a=1
b=1
c=1
year = 1
while True:
    if a==e and b==s and c==m:
        print(year)
        break
    else:
        a+=1
        b+=1
        c+=1
        if a>15:
            a-=15
        if b>28:
            b-=28
        if c>19:
            c-=19
        year+=1

