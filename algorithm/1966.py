import collections

n = int(input())
for _ in range(n):
    count=0
    p,want_see = map(int,input().split())
    importance = collections.deque(map(int,input().split()))
    importance_c = collections.deque(range(p))
    importance_c[want_see] = "target"
    while True:
        if importance[0] == max(importance):
            count+=1
            if importance_c[0] == "target":
                break
            else:
                importance.popleft()
                importance_c.popleft()
        else:
            importance.append(importance.popleft())
            importance_c.append(importance_c.popleft())
    print(count)