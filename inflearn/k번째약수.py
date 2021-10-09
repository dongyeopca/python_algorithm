n,k = map(int,input().split())
answer = []
for i in range(1,n+1):
    if n%i == 0:
        answer.append(i)
    else:
        continue

if len(answer)<k:
    print(-1)
else:
    print(answer[k-1])

#for else구문
# n,k = map(int,input().split())
# cnt = 0
# for i in range(1,n+1):
#     if n%i==0:
#         cnt+=1
#     if cnt==k:
#         print(i)
#         break
# else:
#     print(-1)
