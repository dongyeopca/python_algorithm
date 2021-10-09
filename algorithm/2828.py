#사과게임
n,m = map(int,input().split())
j = int(input())
a = []
move = 0
right = m
left = 1
for _ in range(j):
    a.append(int(input()))

for i in a:
    if i>right:
        move+=i-right
        right= i
        left = right-m+1
    elif i<left:
        move+=left-i
        left = i
        right = left+m-1
    else:
        continue
print(move)

