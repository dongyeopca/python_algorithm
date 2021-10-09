n = int(input())
answer = list()
for i in range(n):
    a = list(map(int,input().split()))
    b = set(a)
    if len(b)==1:
        answer.append(10000+1000*list(b)[0])
    elif len(b)==3:
        answer.append(100*max(b))
    else:
        for i in a:
            if a.count(i) == 2:
                answer.append(1000+i*100)
                break
print(max(answer))
