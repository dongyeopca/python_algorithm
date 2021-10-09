n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
rsum = 0
lsum = 0
g = 0
for i in range(5):
    dsum = a[i][i]
    dsum2 = a[4-i][4-i]
    for j in range(5):
        rsum += a[i][j]
        lsum += a[j][i]
    g = max(rsum,lsum)
    rsum,lsum = 0
print(max(g,dsum,dsum2))