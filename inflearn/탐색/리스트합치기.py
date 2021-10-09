n = int(input())
a = list(map(int,input().split()))
b = int(input())
c = list(map(int,input().split()))
d = []
# d = a+c
# print(sorted(d))
p1=p2=0
while p1<n or p2<b:
    if a[p1]<=c[p2]:
        d.append(a[p1])
        p1+=1
    else:
        d.append(c[p2])
        p2+=1
if p1<n:
    d = d+a[p1:]
else:
    d = d+c[p2]