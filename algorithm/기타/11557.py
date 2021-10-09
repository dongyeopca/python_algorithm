t = int(input())
for i in range(t):
    n = int(input())
    alcohol = list()
    for j in range(n):
        s,l = input().split()
        alcohol.append([s,int(l)])
    alcohol = sorted(alcohol,key=lambda x:x[1])
    print(alcohol[-1][0])