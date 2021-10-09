n = int(input())
s = list(map(int,input().split()))
s.sort()
count=0
result = 0
for i in s:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)
