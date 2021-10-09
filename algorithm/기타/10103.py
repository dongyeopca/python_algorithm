n = int(input())
scorea = 100
scoreb = 100
for i in range(n):
    a,b = list(map(int,input().split()))
    if a>b:
        scoreb-=a
    elif b>a:
        scorea-=b

print(scorea)
print(scoreb)