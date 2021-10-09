n = int(input())
size = []
rank = [n]*n
for _ in range(n):
    size.append(list(map(int,input().split())))

for i in range(len(size)-1):
    for j in range(i+1,len(size)):
        if size[i][0]<size[j][0] and size[i][1]<size[j][1]:
            rank[j]-=1
        elif size[i][0]>size[j][0] and size[i][1]>size[j][1]:
            rank[i]-=1
        else:
            rank[i]-=1
            rank[j]-=1
for _ in rank:
    print(_,end=' ')

