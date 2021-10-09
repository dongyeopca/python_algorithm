import sys

n = int(input())
queue = list()
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        queue.append(order[1])
    if order[0] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    if order[0] == "size":
        print(len(queue))
    if order[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    if order[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    if order[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
            